from __future__ import annotations
from asyncio.futures import Future
from typing import TYPE_CHECKING, Protocol
if TYPE_CHECKING:
    from ..protocol.struct_request import Request

from collections import UserDict
from .exceptions import RepeatedRequestID

class Header(Protocol):
    cmd_code: int
    request_identifier: int

    @property
    def is_pushed(self) -> bool:
        ...


class CommandsCodeMapper(UserDict):
    data: dict[int, int]

    def add_code(self, req_id: int, cmd_code: int) -> None:
        self.data[req_id] = cmd_code

    def pop_code(self, req_id: int) -> int | None:
        return self.data.pop(req_id, None)


class FuturesMapper(UserDict):
    data: dict[tuple[int, str], Future]

    def make_future(self, req_id: int, cmd_name: str) -> Future:
        self.data[(req_id, cmd_name)] = fut = Future()
        return fut

    def pop_future(self, req_id: int, cmd_name: str) -> Future | None:
        return self.data.pop((req_id, cmd_name), None)


class MessagesMapper:
    __slots__ = ("__codes_mapper", "__response_awaiters")

    def __init__(self) -> None:
        self.__codes_mapper = CommandsCodeMapper()
        self.__response_awaiters = FuturesMapper()

    def register(self, request: "Request") -> Future:
        # header_ = request.header
        # request_id_ = header_.request_identifier
        # self.__codes_mapper.add_code(
        #     req_id=request_id_,
        #     cmd_code=header_.cmd_code
        # )
        return self.__response_awaiters.make_future(
            req_id=request_id_,
            cmd_name=request.class_name
        )

    def get_result_future(self, response) -> Future | None:
        return self.__response_awaiters.pop_future(
            req_id=response.header.request_identifier,
            cmd_name=response.class_name,
        )

    def get_command_code(self, header: Header) -> int:
        command_idx = (
            header.cmd_code
            if header.is_pushed
            else self.__codes_mapper.pop_code(header.request_identifier)
        )
        if not command_idx:
            raise RepeatedRequestID(header)
        return command_idx
