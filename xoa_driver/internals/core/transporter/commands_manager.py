from __future__ import annotations
from asyncio.futures import Future
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..protocol.struct_request import Request


class CommandsManager:
    __slots__ = ("__cmd_handler", "__received_futures")

    def __init__(self) -> None:
        self.__cmd_handler: dict[int, int] = {}
        self.__received_futures: dict[tuple[int, str], Future] = {}

    def append(self, request: "Request") -> Future:
        self.__cmd_handler[request.header.request_identifier] = request.header.cmd_code
        self.__received_futures[
            (
                request.header.request_identifier,
                request.class_name
            )
        ] = fut = Future()
        return fut

    def get_command_handler_id(self, req_id) -> int | None:
        return self.__cmd_handler.pop(req_id, None)

    def get_result_future(self, response) -> Future | None:
        return self.__received_futures.pop(
            (
                response.header.request_identifier,
                response.class_name
            ),
            None
        )
