from asyncio.futures import Future
from typing import (
    Dict,
    TYPE_CHECKING,
    Tuple,
    Optional,
)
if TYPE_CHECKING:
    from .. import protocol

class CommandsManager:
    
    __slots__ = ("__cmd_handler", "__received_futures")
    
    def __init__(self) -> None:
        self.__cmd_handler: Dict[int, int] = {}
        self.__received_futures: Dict[Tuple[int, str], Future] = {}
    
    def append(self, request: "protocol.Request") -> "Future":
        self.__cmd_handler[request.header.request_identifier] = request.header.cmd_code
        self.__received_futures[
            (
                request.header.request_identifier, 
                request.class_name
            )
        ] = fut = Future()
        return fut

    def get_command_handler_id(self, req_id) -> Optional[int]:
        return self.__cmd_handler.pop(req_id, None)
    
    def get_result_future(self, response) -> Optional["Future"]:
        return self.__received_futures.pop(
            (
                response.header.request_identifier, 
                response.class_name
            ),
            None
        )

