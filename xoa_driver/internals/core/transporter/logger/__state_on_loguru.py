from __future__ import annotations
import sys
import typing as t

if t.TYPE_CHECKING:
    try:
        from loguru import Logger
    except ImportError:
        pass
    from .__logger import TransportationLogger


SYMBOL_REQUEST = "<G><w> -> </w></G>"
SYMBOL_PUSH = "<M><w> -P </w></M>"
SYMBOL_RESPONSE = "<Y><e> <- </e></Y>"


class StateOnLoguru:

    @staticmethod
    def setup(connid: str, logger: "Logger") -> "Logger":
        logger.remove()  # All configured handlers are removed
        fmt = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <level>{message}</level>"
        logger.add(sys.stdout, format=fmt)
        logger = logger.bind(connid=connid)
        return logger

    @staticmethod
    def info(inst: "TransportationLogger", msg: t.Any) -> None:
        _loger = t.cast("Logger", inst._logger)
        _loger.opt(lazy=True, colors=True).info(msg)

    @staticmethod
    def error(inst: "TransportationLogger", msg: t.Any) -> None:
        _loger = t.cast("Logger", inst._logger)
        _loger.opt(lazy=True, colors=True).error(msg)

    @staticmethod
    def debug_request(inst: "TransportationLogger", request: object) -> None:
        _loger = t.cast("Logger", inst._logger)
        _loger.opt(lazy=True, colors=True).debug(f"{SYMBOL_REQUEST} {request!r}")

    @staticmethod
    def debug_response(inst: "TransportationLogger", response: object) -> None:
        _loger = t.cast("Logger", inst._logger)
        _loger.opt(lazy=True, colors=True).debug(f"{SYMBOL_RESPONSE} {response!r}")

    @staticmethod
    def debug_push(inst: "TransportationLogger", response: object) -> None:
        _loger = t.cast("Logger", inst._logger)
        _loger.opt(lazy=True, colors=True).debug(f"{SYMBOL_PUSH} {response!r}")
