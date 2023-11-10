from __future__ import annotations
from dataclasses import dataclass
import typing
import functools

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
    XmpHex,
    XmpInt,
    XmpLong,
    XmpSequence,
    Hex,
)
from .enums import (
    StartTrigger,
    StopTrigger,
    PacketType,
)


@register_command
@dataclass
class PC_TRIGGER:
    """
    The criteria for when to start and stop the capture process for a port. Even
    when capture is enabled with :class:`P_CAPTURE`, the actual capturing of packets can be
    delayed until a particular start criteria is met by a received packet.
    Likewise, a stop criteria can be specified, based on a received packet. If no
    explicit stop criteria is specified, capture  stops when the internal buffer
    runs full. In buffer overflow situations, if there is an explicit  stop
    criteria, then the latest packets will be retained (and the early ones
    discarded),  and otherwise, the earliest packets are retained (and the later
    ones discarded).
    """

    code: typing.ClassVar[int] = 221
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        start_criteria: StartTrigger = field(XmpInt())
        """The criteria for starting the actual packet capture.

        :type: StartTrigger
        """
        start_criteria_filter: int = field(XmpInt())
        """The index of a particular filter for the start criteria.

        :type: int
        """
        stop_criteria: StopTrigger = field(XmpInt())
        """The criteria for stopping the actual packet capture.

        :type: StopTrigger
        """
        stop_criteria_filter: int = field(XmpInt())
        """The index of a particular filter for the stop criteria.

        :type: int
        """

    class SetDataAttr(RequestBodyStruct):
        start_criteria: StartTrigger = field(XmpInt())
        """coded integer, the criteria for starting the actual packet capture"""
        start_criteria_filter: int = field(XmpInt())
        """integer, the index of a particular filter for the start criteria."""
        stop_criteria: StopTrigger = field(XmpInt())
        """coded integer, the criteria for stopping the actual packet capture"""
        stop_criteria_filter: int = field(XmpInt())
        """integer, the index of a particular filter for the stop criteria."""

    def get(self) -> Token[GetDataAttr]:
        """Get the capture criteria configurations.

        :return: capture criteria configuration.
        :rtype: ~PC_TRIGGER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, start_criteria: StartTrigger, start_criteria_filter: int, stop_criteria: StopTrigger, stop_criteria_filter: int) -> Token[None]:
        """Set the capture criteria configurations.

        :param start_criteria: the criteria for starting the actual packet capture
        :type start_criteria: StartTrigger
        :param start_criteria_filter: the index of a particular filter for the start criteria
        :type start_criteria_filter: int
        :param stop_criteria: the criteria for stopping the actual packet capture
        :type stop_criteria: StopTrigger
        :param stop_criteria_filter: the index of a particular filter for the stop criteria
        :type stop_criteria_filter: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                start_criteria=start_criteria,
                start_criteria_filter=start_criteria_filter,
                stop_criteria=stop_criteria,
                stop_criteria_filter=stop_criteria_filter
            )
        )


@register_command
@dataclass
class PC_KEEP:
    """
    Which packets to keep once the start criteria has been triggered for a port.
    Also how big a portion of each packet to retain, saving space for more packets
    in the capture buffer.
    """

    code: typing.ClassVar[int] = 222
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        kind: PacketType = field(XmpInt())
        """The type of packet to keep.

        :type: PacketType
        """
        index: int = field(XmpInt())
        """Test payload id or filter index for which packets to keep.

        :type: int
        """
        byte_count: int = field(XmpInt())
        """How many bytes to keep in the buffer for of each packet. The value -1 means no limit on packet size.

        :type: int
        """

    class SetDataAttr(RequestBodyStruct):
        kind: PacketType = field(XmpInt())
        """coded integer, which general kind of packets to keep"""
        index: int = field(XmpInt())
        """integer, test payload id or filter index for which packets to keep."""
        byte_count: int = field(XmpInt())
        """integer, how many bytes to keep in the buffer for of each packet. The value -1 means no limit on packet size."""

    def get(self) -> Token[GetDataAttr]:
        """Get the configuration of how to keep captured packets.

        :return: the configuration of how to keep captured packets
        :rtype: ~PC_KEEP.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, kind: PacketType, index: int, byte_count: int) -> Token[None]:
        """Set the configuration of how to keep captured packets.

        :param kind: which general kind of packets to keep
        :type kind: PacketType
        :param index: test payload id or filter index for which packets to keep
        :type index: int
        :param byte_count: how many bytes to keep in the buffer for of each packet. The value -1 means no limit on packet size.
        :type byte_count: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, kind=kind, index=index, byte_count=byte_count))

    set_all = functools.partialmethod(set, PacketType.ALL)
    """Keep all types of packets.
    """

    set_fcserr = functools.partialmethod(set, PacketType.FCSERR)
    """Only keep the packets with FCS errors.
    """

    set_notpld = functools.partialmethod(set, PacketType.NOTPLD)
    """Only keep the packets without test payload.
    """

    set_tpld = functools.partialmethod(set, PacketType.TPLD)
    """Only keep the packets with test payload.
    """

    set_filter = functools.partialmethod(set, PacketType.FILTER)
    """Only keep the packets that satisfy the given filter.
    """

    set_plderr = functools.partialmethod(set, PacketType.PLDERR)
    """Only keep the packets with payload error in.
    """


@register_command
@dataclass
class PC_STATS:
    """
    Obtains the number of packets currently in the capture buffer for a port. The
    count is reset to zero when capture is turned on.
    """

    code: typing.ClassVar[int] = 224
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        status: int = field(XmpLong())
        """Capture status, 1 if capture has been stopped because of overflow, 0 if still running.

        :type: int
        """
        packets: int = field(XmpLong())
        """The number of packets in the buffer.

        :type: int
        """
        start_time: int = field(XmpLong())
        """Time when capture was started, in **nanoseconds** since 2010-01-01.

        :type: int
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the number of packets currently in the capture buffer for a port. The count is reset to zero when capture is turned on.

        :return: status of the capture, number of packets in the buffer, and start time in nanoseconds since 2010-01-01.
        :rtype: ~PC_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PC_EXTRA:
    """
    Obtains extra information about a captured packet for a port. The information
    comprises time of capture, latency, inter-frame gap, and original packet length.
    Latency is only valid for packets with test payloads and where the originating
    port is on the same module and therefore has the same clock.
    """

    code: typing.ClassVar[int] = 225
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _capture_packet_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        time_captured: int = field(XmpLong())
        """
        Time of capture, in **nanoseconds** since 2010-01-01.

        :type: int
        """
        latency: int = field(XmpLong())
        """
        The number of **nanoseconds** since the packet was transmitted.

        :type: int
        """
        byte_time_count: int = field(XmpLong())
        """
        The number of byte-times since previous packet.

        :type: int
        """
        length: int = field(XmpInt())
        """
        The real length of the packet on the wire.

        :type: int
        """

    def get(self) -> Token[GetDataAttr]:
        """Get extra information about a captured packet for a port.

        :return: Extra information about a captured packet for a port.

        :rtype: ~PC_EXTRA.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._capture_packet_xindex]))


@register_command
@dataclass
class PC_PACKET:
    """
    Obtains the raw bytes of a captured packet for a port. The packet data may be
    truncated if the :class:`PC_KEEP` command specified a limit on the number of bytes kept.
    """

    code: typing.ClassVar[int] = 226
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _capture_packet_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        hex_data: Hex = field(XmpHex())
        """The raw bytes kept for the packet.

        :type: list
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the raw bytes of a captured packet for a port.

        :return: the raw bytes of a captured packet
        :rtype: ~PC_PACKET.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._capture_packet_xindex]))
