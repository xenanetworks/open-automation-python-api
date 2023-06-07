from __future__ import annotations
import asyncio
import typing as t
from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.transporter.protocol.struct_request import Request
from xoa_driver.internals.core.transporter._typings import ICommand


class Green:
    @staticmethod
    def is_connected(inst: itf.IConnection) -> bool:
        return inst.is_connected

    @staticmethod
    def send(inst: itf.IConnection, data: bytes | bytearray | memoryview) -> None:
        return inst.send(data)

    @staticmethod
    def close(inst: itf.IConnection) -> None:
        return inst.close()

    @staticmethod
    async def prepare_data(inst: itf.IConnection, request: "Request") -> tuple[bytes, asyncio.Future]:
        return await inst.prepare_data(request)

    @staticmethod
    def subscribe(inst: itf.IConnection, xmc_cls: "ICommand", callback: t.Callable) -> None:
        return inst.subscribe(xmc_cls, callback)

    @staticmethod
    def on_disconnected(inst: itf.IConnection, callback: t.Callable) -> None:
        return inst.on_disconnected(callback)


class Red:
    @staticmethod
    def is_connected(inst: itf.IConnection) -> bool:
        return False

    @staticmethod
    def send(inst: itf.IConnection, data: bytes | bytearray | memoryview) -> None:
        raise ConnectionRefusedError("The instance is not valid anymore, please obtain() a new one.")

    @staticmethod
    def close(inst) -> None:
        raise ConnectionRefusedError("The instance is not valid anymore, please obtain() a new one.")

    @staticmethod
    async def prepare_data(inst, request: "Request") -> tuple[bytes, asyncio.Future]:
        raise ConnectionRefusedError("The instance is not valid anymore, please obtain() a new one.")

    @staticmethod
    def subscribe(inst, xmc_cls: "ICommand", callback: t.Callable) -> None:
        raise ConnectionRefusedError("The instance is not valid anymore, please obtain() a new one.")

    @staticmethod
    def on_disconnected(inst, callback: t.Callable) -> None:
        raise ConnectionRefusedError("The instance is not valid anymore, please obtain() a new one.")


class ConnectionTrafficLight:
    __slots__ = ("_conn", "state")

    def __init__(self, connection: itf.IConnection) -> None:
        self._conn = connection
        self.state = Green

    def set_outdated(self) -> None:
        self.state = Red

    @property
    def is_connected(self) -> bool:
        return self.state.is_connected(self._conn)

    def send(self, data: bytes | bytearray | memoryview) -> None:
        return self.state.send(self._conn, data)

    def close(self) -> None:
        return self.state.close(self._conn)

    async def prepare_data(self, request: "Request") -> tuple[bytes, asyncio.Future]:
        return await self.state.prepare_data(self._conn, request)

    def subscribe(self, xmc_cls: "ICommand", callback: t.Callable) -> None:
        return self.state.subscribe(self._conn, xmc_cls, callback)

    def on_disconnected(self, callback: t.Callable) -> None:
        return self.state.on_disconnected(self._conn, callback)
