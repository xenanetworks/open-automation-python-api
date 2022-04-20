#: L23 Port Capture Commands

from dataclasses import dataclass
import typing
import functools

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
class PC_TRIGGER:
    """
    The criteria for when to start and stop the capture process for a port. Even
    when capture is enabled with P_CAPTURE, the actual capturing of packets can be
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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        start_criteria: XmpField[XmpInt] = XmpField(XmpInt, choices=StartTrigger)  # coded integer, the criteria for starting the actual packet capture
        start_criteria_filter: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the index of a particular filter for the start criteria.
        stop_criteria: XmpField[XmpInt] = XmpField(XmpInt, choices=StopTrigger)  # coded integer, the criteria for stopping the actual packet capture
        stop_criteria_filter: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the index of a particular filter for the stop criteria.

    @dataclass(frozen=True)
    class GetDataAttr:
        start_criteria: XmpField[XmpInt] = XmpField(XmpInt, choices=StartTrigger)  # coded integer, the criteria for starting the actual packet capture
        start_criteria_filter: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the index of a particular filter for the start criteria.
        stop_criteria: XmpField[XmpInt] = XmpField(XmpInt, choices=StopTrigger)  # coded integer, the criteria for stopping the actual packet capture
        stop_criteria_filter: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the index of a particular filter for the stop criteria.

    def get(self) -> "Token[GetDataAttr]":
        """Get the capture criteria configurations.

        :return: capture criteria configuration.
        :rtype: PC_TRIGGER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, start_criteria: StartTrigger, start_criteria_filter: int, stop_criteria: StopTrigger, stop_criteria_filter: int) -> "Token":
        """Set the capture criteria configurations.

        :param start_criteria: the criteria for starting the actual packet capture
        :type start_criteria: StartTrigger
        :param start_criteria_filter: the index of a particular filter for the start criteria
        :type start_criteria_filter: int
        :param stop_criteria: the criteria for stopping the actual packet capture
        :type stop_criteria: int
        :param stop_criteria_filter: the index of a particular filter for the stop criteria
        :type stop_criteria_filter: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, start_criteria=start_criteria, start_criteria_filter=start_criteria_filter, stop_criteria=stop_criteria, stop_criteria_filter=stop_criteria_filter))


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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        kind: XmpField[XmpInt] = XmpField(XmpInt, choices=PacketType)  # coded integer, which general kind of packets to keep
        index: XmpField[XmpInt] = XmpField(XmpInt)  # integer, test payload id or filter index for which packets to keep.
        byte_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, how many bytes to keep in the buffer for of each packet. The value -1 means no limit on packet size.

    @dataclass(frozen=True)
    class GetDataAttr:
        kind: XmpField[XmpInt] = XmpField(XmpInt, choices=PacketType)  # coded integer, which general kind of packets to keep
        index: XmpField[XmpInt] = XmpField(XmpInt)  # integer, test payload id or filter index for which packets to keep.
        byte_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, how many bytes to keep in the buffer for of each packet. The value -1 means no limit on packet size.

    def get(self) -> "Token[GetDataAttr]":
        """Get the configuration of how to keep captured packets.

        :return: the configuration of how to keep captured packets
        :rtype: PC_KEEP.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, kind: PacketType, index: int, byte_count: int) -> "Token":
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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, 1 if capture has been stopped because of overflow, 0 if still running.
        packets: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of packets in the buffer.
        starttime: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, time when capture was started, in nano-seconds since 2010-01-01.

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of packets currently in the capture buffer for a port. The count is reset to zero when capture is turned on.
        
        :return: status of the capture, number of packets in the buffer, and start time in nanoseconds since 2010-01-01.
        :rtype: PC_STATS.GetDataAttr
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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    capture_packet_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        time_captured: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, time when packet was captured, in nanoseconds since 2010-01-01.
        latency: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of nanoseconds since the packet was transmitted.
        byte_time_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of byte-times since previous packet.
        length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the real length of the packet on the wire.

    def get(self) -> "Token[GetDataAttr]":
        """Get extra information about a captured packet for a port.

        :return: time of capture, the number of nanoseconds since the packet was transmitted, the number of byte-times since previous packet, and the real length of the packet on the wire.
        :rtype: PC_EXTRA.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self.capture_packet_xindex]))


@register_command
@dataclass
class PC_PACKET:
    """
    Obtains the raw bytes of a captured packet for a port. The packet data may be
    truncated if the PC_KEEP command specified a limit on the number of bytes
    kept.
    """

    code: typing.ClassVar[int] = 226
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    capture_packet_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        hex_data: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, the raw bytes kept for the packet.

    def get(self) -> "Token[GetDataAttr]":
        """Get the raw bytes of a captured packet for a port. 

        :return: the raw bytes of a captured packet
        :rtype: PC_PACKET.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self.capture_packet_xindex]))


