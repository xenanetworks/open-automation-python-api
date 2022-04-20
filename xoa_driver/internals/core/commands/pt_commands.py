#: L23 Port TX Statistics Commands

from dataclasses import dataclass
import typing

from ..protocol.command_builders import (
    build_get_request,
    build_set_request
)
from .. import interfaces
from ..transporter.token import Token
from ..protocol.fields.data_types import *
from ..protocol.fields.field import XmpField
from ..registry import register_command
from .enums import *

@register_command
@dataclass
class PT_TOTAL:
    """
    Obtains statistics concerning all the packets transmitted on a port.
    """

    code: typing.ClassVar[int] = 230
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bit_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits transmitted in the last second.
        packet_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted in the last second.
        byte_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes transmitted since statistics were cleared.
        packet_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets transmitted on a port.

        :return: number of bits transmitted in the last second, number of packets transmitted in the last second, number of bytes transmitted since statistics were cleared, and number of packets transmitted since statistics were cleared.
        :rtype: PT_TOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PT_NOTPLD:
    """
    Obtains statistics concerning the packets without a test payload transmitted on
    a port.
    """

    code: typing.ClassVar[int] = 231
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bit_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits transmitted in the last second.
        packet_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted in the last second.
        byte_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes transmitted since statistics were cleared.
        packet_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning the packets without a test payload transmitted on a port.

        :return: number of bits transmitted in the last second, number of packets transmitted in the last second, number of bytes transmitted since statistics were cleared, and number of packets transmitted since statistics were cleared
        :rtype: PT_NOTPLD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PT_STREAM:
    """
    Obtains statistics concerning the packets of a specific stream transmitted on a
    port.
    """

    code: typing.ClassVar[int] = 232
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _stream_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bit_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits transmitted in the last second.
        packet_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted in the last second.
        byte_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes transmitted since statistics were cleared.
        packet_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning the packets of a specific stream transmitted on a port.

        :return: number of bits transmitted in the last second, number of packets transmitted in the last second, number of bytes transmitted since statistics were cleared, and number of packets transmitted since statistics were cleared.
        :rtype: PT_STREAM.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PT_CLEAR:
    """
    Clear all the transmit statistics for a port. The byte and packet counts will
    restart at zero.
    """

    code: typing.ClassVar[int] = 233
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clear all the transmit statistics for a port. The byte and packet counts will restart at zero.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
            ),
        )


@register_command
@dataclass
class PT_EXTRA:
    """
    Obtains additional statistics for packets transmitted on a port.
    """

    code: typing.ClassVar[int] = 235
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        tx_arp_req_count: XmpField[XmpLongList] = XmpField(XmpLongList)  # long integer, number of ARP requests transmitted

    def get(self) -> "Token[GetDataAttr]":
        """Get additional statistics for packets transmitted on a port.

        :return: number of ARP requests transmitted
        :rtype: PT_EXTRA.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PT_FLOWTOTAL:
    """
    Obtains statistics concerning all the packets transmitted from a between this
    receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1740
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        l2_bps: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits transmitted at layer 2 in the last second for the flow.
        pps: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted in the last second for the flow.
        byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes transmitted since statistics were cleared for the flow.
        packet_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets transmitted since statistics were cleared for the flow.

    def get(self) -> "Token[GetDataAttr]":
        """(Chimera only) Get statistics concerning all the packets transmitted from a between this receive port and its partner TX port.

        :return:
            number of bits transmitted at layer 2 in the last second for the flow, 
            number of packets transmitted in the last second for the flow,
            number of bytes transmitted since statistics were cleared for the flow,
            number of packets transmitted since statistics were cleared for the flow
            
        :rtype: PT_FLOWTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PT_FLOWCLEAR:
    """
    Clear all the transmit statistics on a particular flow for a Chimera port. The
    byte and packet counts will restart at zero.
    """

    code: typing.ClassVar[int] = 1742
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """(Chimera only) Clear all the transmit statistics on a particular flow for a Chimera port. The byte and packet counts will restart at zero.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex],
            ),
        )


