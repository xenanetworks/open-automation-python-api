from __future__ import annotations
import asyncio
# from concurrent.futures import ThreadPoolExecutor
from asyncio.futures import Future
from typing import Callable


from uuid import uuid4


from asyncio.transports import Transport

from ..protocol import constants as const
from ..registry import COMMANDS_REGISTRY
from .. import interfaces as x_types

from . import events_observer as eveo
from . import logging as log
# from . import exceptions as t_ex
from . import commands_manager as cm
from .request_id_counter import RequestIdCounter
from .stream import Stream
from .processor import PacketsProcessor
from ..protocol.struct_header import ResponseHeader
# from ..protocol.struct_response import Response
from ..protocol.struct_request import Request


class TransportationHandler(asyncio.Protocol):
    """Handling sending and receiving of the XMP commands."""

    def __init__(self, debug: bool = False) -> None:
        self.identity = uuid4().hex
        self.__transport: Transport | None = None
        self.__req_id = RequestIdCounter()
        self.__stream = Stream(ResponseHeader, const.MAGIC_WORD)
        self.__pkt_processor = PacketsProcessor(self.__stream)

        # self._worker = ThreadPoolExecutor()

        self.__log = log.TransportationLogger(self.identity[:6], debug)

        self.events_observer = eveo.EventsObserver()
        self.cmd_mngr = cm.CommandsManager()

        # self.commands_registry = COMMANDS_REGISTRY
        # self.magic_word = const.MAGIC_WORD
        # self.aggregate: bytearray = bytearray()

    @property
    def is_connected(self) -> bool:
        return not (self.__transport is None or self.__transport.is_closing())

    def connection_made(self, transport: "Transport") -> None:
        self.__transport = transport
        peername = transport.get_extra_info("peername")
        self.__pkt_processor.start()
        self.__log.info(f"Connection to {peername}")

    def data_received(self, data: bytes) -> None:
        """Process received data from xenaserver."""
        self.__stream.write(data)

    def eof_received(self) -> None:
        self.__log.info("EOF received")

    def connection_lost(self, exc) -> None:
        self.events_observer.dispatch(
            eveo.ON_EVT_DISCONNECTED,
            self.__transport.get_extra_info("peername") if self.__transport else None
        )
        self.__transport = None
        self.__pkt_processor.stop()
        self.__log.info(f"The server closed the connection {exc}")

    def send(self, requests: bytes | bytearray | memoryview) -> None:
        """
        Send applied commands from sending queue to
        xenaserver and liberate the sending queue.
        """
        if not self.is_connected:
            raise BrokenPipeError("No socket!")
        self.__transport.write(requests) # type: ignore

    def close(self) -> None:
        """Close connection with xenaserver."""
        if self.is_connected:
            self.__transport.close()  # type: ignore

    async def prepare_data(self, request: Request) -> tuple[bytes, Future]:
        assert self.is_connected, "Cannot add command because Socket is disconnected"
        request.update_identifier(
            await self.__req_id.get_avaliable()
        )
        self.__log.request_obj(request)
        return bytes(request), self.cmd_mngr.append(request)

    def subscribe(self, xmc_cls: x_types.CMD_TYPE, callback: "Callable") -> None:
        assert xmc_cls.pushed, "Command is not subscribable."
        assert callback, "Callback function is required."
        self.events_observer.subscribe(
            xmc_cls.code,
            callback
        )

    def on_disconnected(self, callback: "Callable") -> None:
        self.events_observer.subscribe(
            eveo.ON_EVT_DISCONNECTED,
            callback
        )
