from __future__ import annotations
import typing as t

if t.TYPE_CHECKING:
    from ...protocol.struct_response import Response
    from ...protocol.struct_request import Request
    from .__logger import TransportationLogger


class StateOff:

    @staticmethod
    def setup(connid: str, logger) -> None:
        return None

    @staticmethod
    def info(inst: "TransportationLogger", msg: t.Any) -> None:
        return None

    @staticmethod
    def error(inst: "TransportationLogger", msg: t.Any) -> None:
        return None

    @staticmethod
    def debug_request(inst: "TransportationLogger", request: "Request") -> None:
        return None

    @staticmethod
    def debug_response(inst: "TransportationLogger", response: "Response") -> None:
        return None

    @staticmethod
    def debug_push(inst: "TransportationLogger", response: "Response") -> None:
        return None
