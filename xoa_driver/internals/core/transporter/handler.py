from __future__ import annotations
import asyncio

from asyncio.transports import Transport
from typing import Callable
from uuid import uuid4

from .logger import (
    TransportationLogger,
    CustomLogger,
)
from .request_id_counter import RequestIdCounter
from .rx_buffer import RxBuffer
from .processor import PacketsProcessor
from .publisher import ResponsePublisher
from ..protocol.struct_header import ResponseHeader
from ..protocol.struct_request import Request
from ..interfaces import CMD_TYPE


class TransportationHandler(asyncio.Protocol):
    """Handling sending and receiving of the XMP commands."""

    __slots__ = ("identity", "peername", "__log", "__transport", "__id_counter", "__rx_buff", "__resp_publisher", "__pkt_processor")

    def __init__(self, *, enable_logging: bool = False, custom_logger: CustomLogger | None = None) -> None:
        self.identity = uuid4().hex[:6]
        self.peername: tuple[str, int] | None = None
        self.__log = TransportationLogger(
            cid=self.identity,
            enabled=enable_logging,
            logger=custom_logger
        )
        self.__transport: Transport | None = None
        self.__id_counter = RequestIdCounter()
        self.__rx_buff = RxBuffer(header_struct=ResponseHeader)
        self.__resp_publisher = ResponsePublisher(logger=self.__log)
        self.__pkt_processor = PacketsProcessor(self.__rx_buff)
        self.__pkt_processor.on_push_response(self.__resp_publisher.publish_push_response)
        self.__pkt_processor.on_param_response(self.__resp_publisher.publish_param_response)

    @property
    def is_connected(self) -> bool:
        return not (self.__transport is None or self.__transport.is_closing())

    def connection_made(self, transport: "Transport") -> None:
        self.__transport = transport
        self.peername = transport.get_extra_info("peername")
        self.__pkt_processor.start()
        self.__log.info(f"Connected to {self.peername}")

    def data_received(self, data: bytes) -> None:
        """Process received data from xenaserver."""
        self.__rx_buff.write(data)

    def eof_received(self) -> None:
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

    async def prepare_data(self, request: Request) -> tuple[bytes, asyncio.Future]:
        assert self.is_connected, "Cannot add command because Socket is disconnected"
        request_id_ = await self.__id_counter.get_number()
        request.update_identifier(request_id_)
        self.__pkt_processor.register(
            req_id=request_id_,
            cmd_code=request.header.cmd_code
        )
        fut_ = self.__resp_publisher.register_request(
            req_id=request_id_,
            cmd_name=request.class_name
        )
        self.__log.debug_request(request)
        return bytes(request), fut_

    def subscribe(self, xmc_cls: CMD_TYPE, callback: "Callable") -> None:
        """Register the callback on the command which supports Server PUSH notification."""
        assert xmc_cls.pushed, "Command is not subscribable."
        assert callback, "Callback function is required."
        self.__resp_publisher.subscribe(
            xmc_cls.code,
            callback
        )

    def on_disconnected(self, callback: "Callable") -> None:
        """Regiser users callback which will be called after connection was terminated."""
        self.__resp_publisher.subscribe_connection_lost(callback)
