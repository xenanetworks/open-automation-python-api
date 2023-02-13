from __future__ import annotations
import asyncio
from dataclasses import dataclass
from typing import Callable, Generator, Protocol
from collections import UserDict

from ..protocol.struct_response import Response
from ..protocol.struct_header import ResponseHeader
from ..protocol.command_builders import build_from_bytes
from .. import registry
from .exceptions import RepeatedRequestID


class Stream(Protocol):
    async def read(self) -> Generator[tuple, None, None]:
        ...


class OnResponseCallback(Protocol):
    def __call__(self, response: Response) -> None:
        ...


class CommandsCodeMapper(UserDict):
    data: dict[int, int]

    def add_code(self, req_id: int, cmd_code: int) -> None:
        self.data[req_id] = cmd_code

    def pop_code(self, req_id: int) -> int | None:
        return self.data.pop(req_id, None)


class PacketsProcessor:
    """Process reading packets from he stream and create a response object for each packet"""

    __slots__ = ("__stream", "__cm_mapper", "__evt_do_job", "__consumer", "__handle_push_response", "__handle_param_response")

    def __init__(self, stream: Stream) -> None:
        self.__stream = stream
        self.__cm_mapper = CommandsCodeMapper()
        self.__evt_do_job = asyncio.Event()
        self.__consumer: asyncio.Task | None = None
        self.__handle_push_response = lambda r: None
        self.__handle_param_response = lambda r: None

    @property
    def is_running(self) -> bool:
        return not (self.__consumer is None or self.__consumer.done())

    def start(self) -> None:
        if self.is_running:
            return None
        self.__evt_do_job.set()
        self.__consumer = asyncio.create_task(self.__consume())
        # self.__consumer.add_done_callback(self.__handle_exceptions)

    def __handle_exceptions(self, fut: asyncio.Future) -> None:
        if fut.cancelled():
            return None
        if e := fut.exception():
            raise e

    def stop(self) -> None:
        if not self.is_running:
            return None
        self.__evt_do_job.clear()
        self.__consumer.cancel()  # type: ignore[ReportOptionalMemberAccess]
        self.__consumer = None

    def register(self, req_id: int, cmd_code: int) -> None:
        self.__cm_mapper.add_code(req_id=req_id, cmd_code=cmd_code)

    def on_push_response(self, callback: OnResponseCallback) -> None:
        self.__handle_push_response = callback

    def on_param_response(self, callback: OnResponseCallback) -> None:
        self.__handle_param_response = callback

    async def __consume(self) -> None:
        # TODO: Handle exceptions
        cnsm_ = Consumer(self.__cm_mapper, self.__handle_push_response, self.__handle_param_response)
        async for header, body_bytes in self.__stream.read():
            cnsm_.run(header, body_bytes)
            if not self.__evt_do_job.is_set():
                return None

    def __serialize_to_response(self, header: ResponseHeader, body_bytes: bytearray) -> Response:
        """Applying received bytes to structured representation."""
        command_idx = header.cmd_code if header.is_pushed else self.__cm_mapper.pop_code(header.request_identifier)
        if not command_idx:
            raise RepeatedRequestID(header)
        xmc_type = registry.get_command(command_idx)
        return build_from_bytes(xmc_type, header, body_bytes)


@dataclass
class Consumer:
    _cm_mapper: CommandsCodeMapper
    _handle_push_response: Callable
    _handle_param_response: Callable

    def __serialize_to_response(self, header: ResponseHeader, body_bytes: bytearray) -> Response:
        """Applying received bytes to structured representation."""
        command_idx = header.cmd_code if header.is_pushed else self._cm_mapper.pop_code(header.request_identifier)
        if not command_idx:
            raise RepeatedRequestID(header)
        xmc_type = registry.get_command(command_idx)
        return build_from_bytes(xmc_type, header, body_bytes)

    async def __consume(self, header, body_bytes) -> None:
        response = self.__serialize_to_response(header, body_bytes)
        if header.is_pushed:
            self._handle_push_response(response)
        else:
            self._handle_param_response(response)

    def run(self, header, body_bytes) -> None:
        asyncio.create_task(self.__consume(header, body_bytes))
