from __future__ import annotations
import typing as t

if t.TYPE_CHECKING:
    from .__logger import (
        TransportationLogger,
        CustomLogger,
    )


RESET = "\x1b[0m"
YELLOW = "\x1b[30;43m"
GREEN = "\x1b[30;42m"
MAGENTA = "\x1b[1;45m"

SYMBOL_REQUEST = f"{GREEN} -> {RESET}"
SYMBOL_PUSH = f"{MAGENTA} -P {RESET}"
SYMBOL_RESPONSE = f"{YELLOW} <- {RESET}"

class StateOnUser:
    @staticmethod
    def setup(connid: str, logger: "CustomLogger") -> "CustomLogger" | None:
        return logger

    @staticmethod
    def info(inst: "TransportationLogger", msg: t.Any) -> None:
        _logger = t.cast("CustomLogger", inst._logger)
        _logger.info(msg)

    @staticmethod
    def error(inst: "TransportationLogger", msg: t.Any) -> None:
        _logger = t.cast("CustomLogger", inst._logger)
        _logger.error(msg)

    @staticmethod
    def debug_request(inst: "TransportationLogger", request: object) -> None:
        _logger = t.cast("CustomLogger", inst._logger)
        _logger.debug(f"{SYMBOL_REQUEST} {request!r}")

    @staticmethod
    def debug_response(inst: "TransportationLogger", response: object) -> None:
        _logger = t.cast("CustomLogger", inst._logger)
        _logger.debug(f"{SYMBOL_RESPONSE} {response!r}")

    @staticmethod
    def debug_push(inst: "TransportationLogger", response: object) -> None:
        _logger = t.cast("CustomLogger", inst._logger)
        _logger.debug(f"{SYMBOL_PUSH} {response!r}")