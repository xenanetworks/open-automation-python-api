import asyncio
from concurrent.futures import ThreadPoolExecutor
from asyncio.futures import Future
from typing import (
    Callable,
    TYPE_CHECKING,
    Optional,
    Tuple,
    Union,
)

from uuid import uuid4

if TYPE_CHECKING:
    from asyncio.transports import Transport

from ..protocol import command_builders
from ..protocol import constants as const
from ..registry import COMMANDS_REGISTRY
from .. import interfaces as x_types
from .. import protocol

from . import events_observer as eveo
from . import logging as log
from . import exceptions as t_ex
from . import commands_manager as cm
from .request_id import RequestId


class TransportationHandler(asyncio.Protocol):
    """Handling sending and receiving of the XMP commands."""

    __slots__ = (
        "identity",
        "is_connected",
        "__log",
        "__transport",
        "events_observer",
        "cmd_mngr",
        "__req_id",
        "commands_registry",
        "magic_word",
        "aggregate",
        "_worker",
    )

    def __init__(self, debug: bool = False) -> None:
        self.identity = uuid4().hex
        self.is_connected: bool = False
        self._worker = ThreadPoolExecutor()

        self.__log = log.TransportationLogger(self.identity[:6], debug)

        self.__transport: Optional["Transport"] = None
        self.events_observer = eveo.EventsObserver()
        self.cmd_mngr = cm.CommandsManager()
        self.__req_id: RequestId = RequestId()

        self.commands_registry = COMMANDS_REGISTRY
        self.magic_word = const.MAGIC_WORD
        self.aggregate: bytearray = bytearray()

    def connection_made(self, transport: "Transport") -> None:
        self.__transport = transport
        self.is_connected = True
        peername = transport.get_extra_info("peername")
        self.__log.info(f"Connection to {peername}")

    def __handle_push_response(self, response: protocol.Response) -> None:
        self.__log.push_obj(response)
        self.events_observer.dispatch(
            response.header.cmd_code,
            response
        )

    def __handle_param_response(self, response: protocol.Response) -> None:
        self.__log.response_obj(response)
        future = self.cmd_mngr.get_result_future(response)
        if not future: raise t_ex.LostFuture(response)
        if not response.is_ok:
            future.set_exception(t_ex.BadStatus(response))
        else:
            future.set_result(response.values)

    def data_received(self, data: bytes) -> None:
        """Process received data from xenaserver."""
        self.aggregate.extend(data)
        while len(self.aggregate) > 0:
            packet_position = self.read_data_with_magic_word(self.aggregate)
            if not packet_position:
                return None
            del self.aggregate[packet_position]
        # self.__log.draw_separator()


    def read_data_with_magic_word(self, extractor: bytearray) -> Optional[slice]:
        # read data which starts from magic word.
        HEADER_POS = slice(16)
        header_bytes = extractor[HEADER_POS]
        if (len(header_bytes) < HEADER_POS.stop) or (not header_bytes.startswith(self.magic_word)):
            return None
        header = protocol.ResponseHeader.from_buffer_copy(header_bytes)
        packet_body_length = header.body_size
        BODY_POS = slice(HEADER_POS.stop, HEADER_POS.stop + header.body_size)
        body_bytes = extractor[BODY_POS]
        if len(body_bytes) < packet_body_length:
            return None
        asyncio.create_task(
            self.process_data(header, body_bytes)
        )
        return slice(BODY_POS.stop)


    async def process_data(self, header, data: bytearray) -> None:
        try:
            response = await self.__serialize_to_response(header, data)
        except t_ex.RepeatedRequestID as e:
            self.__log.error(f"{e} Original Data: {data}")
        else:
            if response.header.is_pushed:
                self.__handle_push_response(response)
            else:
                self.__handle_param_response(response)

    async def __serialize_to_response(self, header, data: bytearray) -> protocol.Response:
        """Applying received bytes to structured representation."""
        command_idx: Optional[int] = (
            header.cmd_code
            if header.is_pushed
            else self.cmd_mngr.get_command_handler_id(
                header.request_identifier
            )
        )
        if not command_idx:
            raise t_ex.RepeatedRequestID(header)
        xmc_type: Optional[x_types.CMD_TYPE] = self.commands_registry.get(command_idx, None)
        if not xmc_type:
            raise t_ex.NotImplementedCommand(header)
        r = self._worker.submit(
            command_builders.build_from_bytes,
            xmc_type,
            header,
            bytes(data)
        )
        return await asyncio.wrap_future(r)

    def eof_received(self) -> None:
        self.__log.info("EOF received")

    def connection_lost(self, exc) -> None:
        self.is_connected = False
        self._worker.shutdown()
        self.events_observer.dispatch(
            eveo.ON_EVT_DISCONNECTED,
            self.__transport.get_extra_info("peername") if self.__transport else None
        )
        self.__transport = None
        self.__log.info(f"The server closed the connection {exc}")

    def send(self, requests: Union[bytes, bytearray]) -> None:
        """
        Send applied commands from sending queue to
        xenaserver and eliberate sending queue.
        """
        if self.__transport is None:
            raise BrokenPipeError("No socket!")
        self.__transport.write(requests)
        # self.__log.draw_separator()

    def close(self) -> None:
        """Close connection with xenaserver."""
        if self.__transport is not None and not self.__transport.is_closing():
            self.__transport.close()

    async def prepare_data(self, request: protocol.Request) -> Tuple[bytes, Future]:
        assert self.is_connected, "Cannot add command because Socket is disconnected"
        request.header.request_identifier = await self.__req_id.get_avaliable()
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
