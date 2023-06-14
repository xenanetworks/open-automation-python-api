from __future__ import annotations
import asyncio
from typing import Callable
from uuid import uuid4
from .logger import (
    TransportationLogger,
    CustomLogger
)
from .protocol.struct_request import Request
from .protocol.struct_header import ResponseHeader
from ._request_id_counter import RequestIdCounter
from ._stream import StreamReader
from ._processor import PacketsProcessor
from ._publisher import ResponsePublisher
from ._typings import ICommand


class TransportationHandler(asyncio.Protocol):
    """Handling sending and receiving of the XMP commands."""

    __slots__ = (
        "identity",
        "peername",
        "__log",
        "__transport",
        "__id_counter",
        "__stream",
        "__resp_publisher",
        "__pkt_processor"
    )

    def __init__(self, *, enable_logging: bool = False, custom_logger: CustomLogger | None = None) -> None:
        self.identity = uuid4().hex[:6]
        self.peername: tuple[str, int] | None = None
        self.__transport: asyncio.Transport | None = None
        self.__id_counter = RequestIdCounter()
        self.__log = TransportationLogger(
            cid=self.identity,
            enabled=enable_logging,
            logger=custom_logger
        )
        self.__stream = StreamReader(header_struct=ResponseHeader)
        self.__resp_publisher = ResponsePublisher(logger=self.__log)
        self.__pkt_processor = PacketsProcessor(
            stream=self.__stream,
            publish_func=self.__resp_publisher.publish
        )

    @property
    def is_connected(self) -> bool:
        return not (self.__transport is None or self.__transport.is_closing())

    def connection_made(self, transport: asyncio.Transport) -> None:
        self.__transport = transport
        self.peername = transport.get_extra_info("peername")
        self.__pkt_processor.start()
        self.__log.info(f"Connected to {self.peername}")

    def data_received(self, data: bytes) -> None:
        """Process received data from xenaserver."""
        try:
            self.__stream.feed_data(data)
        except AssertionError:
            if self.is_connected:
                self.__stream._eof = False
                self.__stream.feed_data(data)
            else:
                self.close()

    def eof_received(self) -> None:
        self.__stream.feed_eof()
        self.__log.info("EOF received")

    def connection_lost(self, exc: Exception | None) -> None:
        self.__resp_publisher.publish_connection_lost(self.peername)
        self.__transport = None
        self.__pkt_processor.stop()
        if exc:
            self.__log.error(exc)
        else:
            self.__log.info(f"The server {self.peername} closed the connection")

    def send(self, data: bytes | bytearray | memoryview) -> None:
        """
        Send applied commands from sending queue to
        xenaserver and liberate the sending queue.
        """
        if not self.is_connected:
            raise BrokenPipeError("No socket!")
        self.__transport.write(data)  # type: ignore[reportOptionalMemberAccess]

    def close(self) -> None:
        """Close connection with xenaserver."""
        if self.is_connected:
            self.__transport.close()  # type: ignore[reportOptionalMemberAccess]
        self.__transport = None

    async def prepare_data(self, request: Request) -> tuple[bytes, asyncio.Future]:
        assert self.is_connected, "Cannot add command because Socket is disconnected"
        request_id_ = await self.__id_counter.get_number()
        request.update_identifier(request_id_)
        self.__pkt_processor.register(
            req_id=request_id_,
            cmd_code=request.cmd_code
        )
        fut_ = self.__resp_publisher.register_request(
            req_id=request_id_,
            cmd_name=request.class_name
        )
        self.__log.debug_request(request)
        return bytes(request), fut_

    def subscribe(self, xmc_cls: ICommand, callback: Callable) -> None:
        """Register the callback on the command which supports Server PUSH notification."""
        assert xmc_cls.pushed, "Command is not subscribable."
        assert callback, "Callback function is required."
        self.__resp_publisher.subscribe(
            evt=xmc_cls.code,
            func=callback
        )

    def on_disconnected(self, callback: Callable) -> None:
        """Regiser users callback which will be called after connection was terminated."""
        self.__resp_publisher.subscribe_connection_lost(callback)

    def set_outdated(self) -> None:
        pass