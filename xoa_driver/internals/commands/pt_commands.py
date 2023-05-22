from __future__ import annotations
from dataclasses import dataclass
import typing

from xoa_driver.internals.core.builders import (
    build_get_request,
    build_set_request
)
from xoa_driver.internals.core import interfaces
from xoa_driver.internals.core.token import Token
from xoa_driver.internals.core.transporter.registry import register_command
from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    RequestBodyStruct,
    ResponseBodyStruct,
    XmpLong,
    XmpSequence,
)


@register_command
@dataclass
class PT_TOTAL:
    """
    Obtains statistics concerning all the packets transmitted on a port.
    """

    code: typing.ClassVar[int] = 230
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bit_count_last_sec: int = field(XmpLong())
        """long integer, number of bits transmitted in the last second."""
        packet_count_last_sec: int = field(XmpLong())
        """long integer, number of packets transmitted in the last second."""
        byte_count_since_cleared: int = field(XmpLong())
        """long integer, number of bytes transmitted since statistics were cleared."""
        packet_count_since_cleared: int = field(XmpLong())
        """long integer, number of packets transmitted since statistics were cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get statistics concerning all the packets transmitted on a port.

        :return: number of bits transmitted in the last second, number of packets transmitted in the last second,
            number of bytes transmitted since statistics were cleared, and number of packets transmitted since statistics were cleared.
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bit_count_last_sec: int = field(XmpLong())
        """long integer, number of bits transmitted in the last second."""
        packet_count_last_sec: int = field(XmpLong())
        """long integer, number of packets transmitted in the last second."""
        byte_count_since_cleared: int = field(XmpLong())
        """long integer, number of bytes transmitted since statistics were cleared."""
        packet_count_since_cleared: int = field(XmpLong())
        """long integer, number of packets transmitted since statistics were cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get statistics concerning the packets without a test payload transmitted on a port.

        :return: number of bits transmitted in the last second, number of packets transmitted in the last second,
            number of bytes transmitted since statistics were cleared, and number of packets transmitted since statistics were cleared
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        bit_count_last_sec: int = field(XmpLong())
        """long integer, number of bits transmitted in the last second."""
        packet_count_last_sec: int = field(XmpLong())
        """long integer, number of packets transmitted in the last second."""
        byte_count_since_cleared: int = field(XmpLong())
        """long integer, number of bytes transmitted since statistics were cleared."""
        packet_count_since_cleared: int = field(XmpLong())
        """long integer, number of packets transmitted since statistics were cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get statistics concerning the packets of a specific stream transmitted on a port.

        :return: number of bits transmitted in the last second, number of packets transmitted in the last second,
            number of bytes transmitted since statistics were cleared, and number of packets transmitted since statistics were cleared.
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Clear all the transmit statistics for a port. The byte and packet counts will restart at zero.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PT_EXTRA:
    """
    Obtains additional statistics for packets transmitted on a port.
    """

    code: typing.ClassVar[int] = 235
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        tx_arp_req_count: typing.List[int] = field(XmpSequence(types_chunk=[XmpLong()]))
        """long integer, number of ARP requests transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get additional statistics for packets transmitted on a port.

        :return: number of ARP requests transmitted
        :rtype: PT_EXTRA.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PT_TOTALEXT:
    """
    .. versionadded: v1.1

    An extension to :class:`PT_TOTAL` that also includes a calculation of bytes transmitted in the last second.
    It returns list of long integers; this list may be expanded in future software releases.
    """

    code: typing.ClassVar[int] = 236
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bit_count_last_sec: int = field(XmpLong())
        """long integer, number of bits transmitted in the last second."""
        byte_count_last_sec: int = field(XmpLong())
        """long integer, number of bytes transmitted in the last second."""
        packet_count_last_sec: int = field(XmpLong())
        """long integer, number of packets transmitted in the last second."""
        byte_count_since_cleared: int = field(XmpLong())
        """long integer, number of bytes transmitted since statistics were cleared."""
        packet_count_since_cleared: int = field(XmpLong())
        """long integer, number of packets transmitted since statistics were cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get statistics concerning all the packets transmitted on a port.

        :return: number of bits transmitted in the last second, number of bytes transmitted in the last second,
            number of packets transmitted in the last second, number of bytes transmitted since statistics were cleared,
            and number of packets transmitted since statistics were cleared.
        :rtype: PT_TOTALEXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PT_NOTPLDEXT:
    """
    .. versionadded: v1.1

    An extension to :class:`PT_NOTPLD` that also includes a calculation of bytes transmitted in the last second.
    It returns list of long integers; this list may be expanded in future software releases.
    """

    code: typing.ClassVar[int] = 237
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bit_count_last_sec: int = field(XmpLong())
        """long integer, number of bits transmitted in the last second."""
        byte_count_last_sec: int = field(XmpLong())
        """long integer, number of bytes transmitted in the last second."""
        packet_count_last_sec: int = field(XmpLong())
        """long integer, number of packets transmitted in the last second."""
        byte_count_since_cleared: int = field(XmpLong())
        """long integer, number of bytes transmitted since statistics were cleared."""
        packet_count_since_cleared: int = field(XmpLong())
        """long integer, number of packets transmitted since statistics were cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get statistics concerning the packets without a test payload transmitted on a port.

        :return: number of bits transmitted in the last second, number of bytes transmitted in the last second,
            number of packets transmitted in the last second, number of bytes transmitted since statistics were cleared,
            and number of packets transmitted since statistics were cleared
        :rtype: PT_NOTPLDEXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PT_STREAMEXT:
    """
    .. versionadded: v1.1

    An extension to :class:`PT_STREAM` that also includes a calculation of bytes transmitted in the last second.
    It returns list of long integers; this list may be expanded in future software releases.
    """

    code: typing.ClassVar[int] = 238
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        bit_count_last_sec: int = field(XmpLong())
        """long integer, number of bits transmitted in the last second."""
        byte_count_last_sec: int = field(XmpLong())
        """long integer, number of bytes transmitted in the last second."""
        packet_count_last_sec: int = field(XmpLong())
        """long integer, number of packets transmitted in the last second."""
        byte_count_since_cleared: int = field(XmpLong())
        """long integer, number of bytes transmitted since statistics were cleared."""
        packet_count_since_cleared: int = field(XmpLong())
        """long integer, number of packets transmitted since statistics were cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get statistics concerning the packets of a specific stream transmitted on a port.

        :return: number of bits transmitted in the last second, number of bytes transmitted in the last second,
            number of packets transmitted in the last second, number of bytes transmitted since statistics were cleared,
            and number of packets transmitted since statistics were cleared.
        :rtype: PT_STREAMEXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PT_FLOWTOTAL:
    """
    Obtains statistics concerning all the packets transmitted from a between this
    receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1740
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        l2_bps: int = field(XmpLong())
        """long integer, number of bits transmitted at layer 2 in the last second for the flow."""
        pps: int = field(XmpLong())
        """long integer, number of packets transmitted in the last second for the flow."""
        byte_count: int = field(XmpLong())
        """long integer, number of bytes transmitted since statistics were cleared for the flow."""
        packet_count: int = field(XmpLong())
        """long integer, number of packets transmitted since statistics were cleared for the flow."""

    def get(self) -> Token[GetDataAttr]:
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """(Chimera only) Clear all the transmit statistics on a particular flow for a Chimera port. The byte and packet counts will restart at zero.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))
