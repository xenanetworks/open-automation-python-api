from __future__ import annotations
import sys
import typing as t
import logging

if t.TYPE_CHECKING:
    from .__logger import TransportationLogger


RESET = "\x1b[0m"
YELLOW = "\x1b[30;43m"
GREEN = "\x1b[30;42m"
MAGENTA = "\x1b[1;45m"

SYMBOL_REQUEST = f"{GREEN} -> {RESET}"
SYMBOL_PUSH = f"{MAGENTA} -P {RESET}"
SYMBOL_RESPONSE = f"{YELLOW} <- {RESET}"


class XoaLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg: t.Any, kwargs: t.MutableMapping[str, t.Any]):
        if not self.extra:
            return f"{msg}", kwargs
        return f"[{self.extra['connid']}] {msg}", kwargs


class StateOnDefault:
    @staticmethod
    def setup(connid: str, logger: logging.Logger | None) -> XoaLoggerAdapter:
        log_stream_formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s"
        )
        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setFormatter(log_stream_formatter)
        if not logger:
            logger = logging.getLogger("XOA_Driver")
            logger.propagate = False
            logger.addHandler(console_handler)
            logger.setLevel(logging.DEBUG)
        return XoaLoggerAdapter(logger, {'connid': connid})

    @staticmethod
    def info(inst: "TransportationLogger", msg: t.Any) -> None:
        _logger = t.cast(logging.Logger, inst._logger)
        if _logger.isEnabledFor(logging.INFO):
            _logger.info(msg)

    @staticmethod
    def error(inst: "TransportationLogger", msg: t.Any) -> None:
        _logger = t.cast(logging.Logger, inst._logger)
        if _logger.isEnabledFor(logging.ERROR):
            _logger.error(msg)

    @staticmethod
    def debug_request(inst: "TransportationLogger", request: object) -> None:
        _logger = t.cast(logging.Logger, inst._logger)
        if _logger.isEnabledFor(logging.DEBUG):
            _logger.debug(f"{SYMBOL_REQUEST} {request!r}")

    @staticmethod
    def debug_response(inst: "TransportationLogger", response: object) -> None:
        _logger = t.cast(logging.Logger, inst._logger)
        if _logger.isEnabledFor(logging.DEBUG):
            _logger.debug(f"{SYMBOL_RESPONSE} {response!r}")

    @staticmethod
    def debug_push(inst: "TransportationLogger", response: object) -> None:
        _logger = t.cast(logging.Logger, inst._logger)
        if _logger.isEnabledFor(logging.DEBUG):
            _logger.debug(f"{SYMBOL_PUSH} {response!r}")
