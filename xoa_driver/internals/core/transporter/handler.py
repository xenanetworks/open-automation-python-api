from __future__ import annotations
import asyncio

from typing import Callable


from uuid import uuid4


from asyncio.transports import Transport

from ..protocol import constants as const
from .. import interfaces as x_types

from .logging import TransportationLogger
from .request_id_counter import RequestIdCounter
from .stream import Stream
from .processor import PacketsProcessor
from .publisher import ResponsePublisher
from ..protocol.struct_header import ResponseHeader
from ..protocol.struct_request import Request


class TransportationHandler(asyncio.Protocol):
    """Handling sending and receiving of the XMP commands."""

    def __init__(self, *, debug: bool = False, logger: None = None) -> None:
        self.identity = uuid4().hex[:6]
        self.__log = TransportationLogger(self.identity, debug, logger)
        self.__transport: Transport | None = None
        self.__id_counter = RequestIdCounter()
        self.__stream = Stream(
            header_struct=ResponseHeader,
            magic_wrd=const.MAGIC_WORD
        )
        self.__resp_publisher = ResponsePublisher(logger=self.__log)
        self.__pkt_processor = PacketsProcessor(self.__stream)
        self.__pkt_processor.on_push_response(self.__resp_publisher.publish_push_response)
        self.__pkt_processor.on_param_response(self.__resp_publisher.publish_param_response)

    @property
    def is_connected(self) -> bool:
        return not (self.__transport is None or self.__transport.is_closing())

    def connection_made(self, transport: "Transport") -> None:
        self.__transport = transport
        peername = transport.get_extra_info("peername")
        self.__pkt_processor.start()
        self.__log.info(f"Connected to {peername}")

    def data_received(self, data: bytes) -> None:
        """Process received data from xenaserver."""
        self.__stream.write(data)

    def eof_received(self) -> None:
        self.__log.info("EOF received")

    def connection_lost(self, exc) -> None:
        self.__resp_publisher.publish_connection_lost(self.__transport.get_extra_info("peername") if self.__transport else None)
        self.__transport = None
        self.__pkt_processor.stop()
        self.__log.info(f"The server closed the connection {exc}")

    def send(self, data: bytes | bytearray | memoryview) -> None:
        """
        Send applied commands from sending queue to
        xenaserver and liberate the sending queue.
        """
        if not self.is_connected:
            raise BrokenPipeError("No socket!")
        self.__transport.write(data)  # type: ignore[reportOption alMemberAccess]

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
        self.__log.request_obj(request)
        return bytes(request), fut_

    def subscribe(self, xmc_cls: x_types.CMD_TYPE, callback: "Callable") -> None:
        assert xmc_cls.pushed, "Command is not subscribable."
        assert callback, "Callback function is required."
        self.__resp_publisher.subscribe(
            xmc_cls.code,
            callback
        )

    def on_disconnected(self, callback: "Callable") -> None:
        self.__resp_publisher.subscribe_connection_lost(callback)
