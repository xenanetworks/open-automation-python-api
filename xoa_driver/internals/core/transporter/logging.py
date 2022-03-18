import re
from typing import (
    Iterable,
    Callable,
    Union,
    Type,
)
from loguru import logger
from .. import protocol

SYMBOL_REQUEST = "<G><w> -> </w></G>"
SYMBOL_PUSH = "<M><w> -P </w></M>"
SYMBOL_RESPONSE = "<Y><e> <- </e></Y>"


class TransportationLogger:
    __slots__ = ("debug", "identity_name", "__logger", "__state")
    def __init__(self, uid: str, debug: bool = False):
        self.debug = debug
        self.identity_name = f"bifrost-{uid}"
        self.__state: Union[Type[StateDebugOn], Type[StateDebugOff]] = StateDebugOff
        self.__logger = logger.bind(logger_name=self.identity_name)
        if self.debug:
            self.__logger.add(f"{self.identity_name}-info.log", rotation="100 MB", level="INFO")
            self.__logger.add(f"{self.identity_name}-debug.log", rotation="100 MB", level="DEBUG")
            self.__logger.add(f"{self.identity_name}-error.log", rotation="100 MB", level="ERROR")
            self.__logger.add(f"{self.identity_name}-warning.log", rotation="100 MB", level="WARNING")
            self.__state = StateDebugOn

    def _log(self, *args: Iterable[str], log_fn: Callable = logger.opt(colors=True).debug) -> None:
        for v in args: log_fn(v)

    def info(self, *args) -> None:
        self.__state.info(self, *args)

    def error(self, *args) -> None:
        self.__state.error(self, *args)

    def request_obj(self, request: protocol.Request) -> None:
        self.__state.request_obj(self, request)

    def response_obj(self, response: protocol.Response) -> None:
        self.__state.response_obj(self, response)
    
    def push_obj(self, response: protocol.Response) -> None:
        self.__state.push_obj(self, response)

    def draw_separator(self, symbol: str = "=") -> None:
        self.__state.draw_separator(self, symbol)


class StateDebugOn:
    @staticmethod
    def info(inst: "TransportationLogger", *args) -> None:
        inst._log(*args, log_fn=logger.info)

    @staticmethod
    def error(inst: "TransportationLogger", *args) -> None:
        inst._log(*args, log_fn=logger.error)

    @staticmethod
    def request_obj(inst: "TransportationLogger", request: protocol.Request) -> None:
        inst._log(f"{SYMBOL_REQUEST} {request!r}")

    @staticmethod
    def response_obj(inst: "TransportationLogger", response: protocol.Response) -> None:
        inst._log(f"{SYMBOL_RESPONSE} {response!r}")
    
    @staticmethod
    def push_obj(inst: "TransportationLogger", response: protocol.Response) -> None:
        inst._log(f"{SYMBOL_PUSH} {response!r}")

    @staticmethod
    def draw_separator(inst: "TransportationLogger", symbol: str) -> None:
        inst._log(symbol * 100, log_fn=logger.info)


class StateDebugOff:
    @staticmethod
    def info(inst: "TransportationLogger", *args) -> None:
        return None

    @staticmethod
    def error(inst: "TransportationLogger", *args) -> None:
        return None

    @staticmethod
    def request_obj(inst: "TransportationLogger", request: protocol.Request) -> None:
        return None

    @staticmethod
    def response_obj(inst: "TransportationLogger", response: protocol.Response) -> None:
        return None

    @staticmethod
    def push_obj(inst: "TransportationLogger", response: protocol.Response) -> None:
        return None

    @staticmethod
    def draw_separator(inst: "TransportationLogger", symbol: str) -> None:
        return None