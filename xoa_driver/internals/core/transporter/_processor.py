from __future__ import annotations
import asyncio
from typing import (
    AsyncIterator,
    Callable,
    Type,
)
from collections import UserDict
from . import registry
from . import exceptions
from ._typings import XoaCommandType
from .protocol.struct_header import ResponseHeader
from .protocol.struct_response import Response


def create_response_obj(cmd: Type[XoaCommandType], header: ResponseHeader, data: bytes) -> Response:
    """Parse bytes retrieved from server to Response structure."""
    return Response(
        class_name=cmd.__name__,
        header=header,
        buffer=data,
        response_struct=getattr(cmd, "GetDataAttr", None)
    )


class CommandsCodeMapper(UserDict):
    data: dict[int, int]

    def add_code(self, req_id: int, cmd_code: int) -> None:
        self.data[req_id] = cmd_code

    def pop_code(self, req_id: int) -> int:
        if command_idx := self.data.pop(req_id, None):
            return command_idx
        raise exceptions.RepeatedRequestID(req_id)


Publisher = Callable[[Response], None]


class PacketsProcessor:
    """Process reading packets from he stream and create a response object for each packet"""

    __slots__ = ("__stream", "__cm_mapper", "__evt_do_job", "__consumer", "__publish",)

    def __init__(self, stream: AsyncIterator[tuple[ResponseHeader, bytes]], publish_func: Publisher) -> None:
        self.__stream = stream
        self.__cm_mapper = CommandsCodeMapper()
        self.__evt_do_job = asyncio.Event()
        self.__consumer: asyncio.Task | None = None
        self.__publish = publish_func

    @property
    def is_running(self) -> bool:
        return not (self.__consumer is None or self.__consumer.done())

    def start(self) -> None:
        if self.is_running:
            return None
        self.__evt_do_job.set()
        self.__consumer = asyncio.create_task(self.__consume())

    def stop(self) -> None:
        if not self.is_running:
            return None
        self.__evt_do_job.clear()
        self.__consumer.cancel()  # type: ignore[ReportOptionalMemberAccess]
        self.__consumer = None

    def register(self, req_id: int, cmd_code: int) -> None:
        self.__cm_mapper.add_code(req_id=req_id, cmd_code=cmd_code)

    async def __task(self, header: ResponseHeader, body_bytes: bytes) -> None:
        command_idx = header.cmd_code if header.is_pushed else self.__cm_mapper.pop_code(header.request_identifier)
        xmc_type = registry.get_command(command_idx)
        response = create_response_obj(xmc_type, header, body_bytes)
        self.__publish(response)

    async def __consume(self) -> None:
        async for header, body_bytes in self.__stream:
            asyncio.create_task(self.__task(header, body_bytes))
            if not self.__evt_do_job.is_set():
                return None
