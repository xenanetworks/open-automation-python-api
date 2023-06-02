from __future__ import annotations
import typing as t
import logging

from .__state_off import StateOff
from .__state_on_default import StateOnDefault
from .__state_on_loguru import StateOnLoguru
from .__state_on_user import StateOnUser


class TransportationLogger:
    __slots__ = ("enabled", "identity_name", "_logger", "__state")

    def __init__(self, cid: str, enabled: bool = False, logger: CustomLogger | None = None) -> None:
        self.enabled = enabled
        self.identity_name = f"{cid}"
        self.__state = self.__select_state(logger)
        self._logger = self.__state.setup(self.identity_name, logger)

    def __select_state(self, logger) -> t.Type[LoggerState]:
        if not self.enabled:
            return StateOff
        elif self.enabled and logger is None:
            return StateOnDefault
        elif isinstance(logger, logging.Logger):
            return StateOnDefault
        try:
            from loguru import Logger as LoguruLogger
        except ImportError:
            pass
        else:
            if isinstance(logger, LoguruLogger):
                return StateOnLoguru
        return StateOnUser

    def info(self, msg: t.Any) -> None:
        self.__state.info(self, msg)

    def error(self, msg: t.Any) -> None:
        self.__state.error(self, msg)

    def debug_request(self, request: object) -> None:
        self.__state.debug_request(self, request)

    def debug_response(self, response: object) -> None:
        self.__state.debug_response(self, response)

    def debug_push(self, response: object) -> None:
        self.__state.debug_push(self, response)


class CustomLogger(t.Protocol):
    """
        The custom logger must be an instance of python Logger or Loguru Logger.
        by providing the custom class of the logger we will not waranty as all of 
        the messages will be visible to the user.
    """
    def debug(self, msg, /, *args, **kwargs: t.Any) -> None:
        ...

    def info(self, msg, /, *args, **kwargs: t.Any) -> None:
        ...

    def warning(self, msg, /, *args, **kwargs: t.Any) -> None:
        ...

    def error(self, msg, /, *args, **kwargs: t.Any) -> None:
        ...


class LoggerState(t.Protocol):
    @staticmethod
    def setup(connid: str, logger) -> CustomLogger | None:
        return None

    @staticmethod
    def info(inst: "TransportationLogger", msg: t.Any) -> None:
        ...

    @staticmethod
    def error(inst: "TransportationLogger", msg: t.Any) -> None:
        ...

    @staticmethod
    def debug_request(inst: "TransportationLogger", request: object) -> None:
        ...

    @staticmethod
    def debug_response(inst: "TransportationLogger", response: object) -> None:
        ...

    @staticmethod
    def debug_push(inst: "TransportationLogger", response: object) -> None:
        ...
