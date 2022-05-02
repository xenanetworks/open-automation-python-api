#: L23 Port RX Statistics Commands

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
class PR_TPLDJITTER:
    """
    Obtains statistics concerning the jitter experienced by the packets with a
    particular test payload id received on a port. The values are the difference in
    packet-to-packet latency, and the minimum will usually be zero.A special value
    of -1 is returned if jitter numbers are not applicable. They are only available
    for TID values 0..31.
    """

    code: typing.ClassVar[int] = 239
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _test_payload_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        min_val: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, minimum jitter for test payload stream
        avg_val: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, average jitter for test payload stream
        max_val: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, maximum jitter for test payload stream
        avg_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, average jitter over last 1-second period
        min_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, minimum jitter during last 1-second period
        max_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, maximum jitter during last 1-second period

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning the jitter experienced by the packets with a particular test payload id received on a port.

        :return: minimum|average|maximum jitter (nanoseconds), average|average|maximum jitter over last 1-second period (nanoseconds)
        :rtype: PR_TPLDJITTER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._test_payload_xindex]))


@register_command
@dataclass
class PR_TOTAL:
    """
    Obtains statistics concerning all the packets received on a port.
    """

    code: typing.ClassVar[int] = 240
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bit_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits received in the last second.
        packet_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received in the last second.
        byte_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes received since statistics were cleared.
        packet_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets received on a port.

        :return:
            number of bits received in the last second, 
            number of packets received in the last second, 
            number of bytes received since statistics were cleared, 
            and number of packets received since statistics were cleared.

        :rtype: PR_TOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PR_NOTPLD:
    """
    Obtains statistics concerning the packets without a test payload received on a
    port.
    """

    code: typing.ClassVar[int] = 241
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bit_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits received in the last second.
        packet_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received in the last second.
        byte_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes received since statistics were cleared.
        packet_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning the packets without a test payload received on a port.

        :return:
            number of bits received in the last second, 
            number of packets received in the last second, 
            number of bytes received since statistics were cleared, 
            and number of packets received since statistics were cleared.

        :rtype: PR_NOTPLD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PR_EXTRA:
    """
    Obtains statistics concerning special errors received on a port since received statistics were cleared.
    """

    code: typing.ClassVar[int] = 242
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        fcs_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with frame checksum errors.
        pause_frame_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of Ethernet pause frames.
        rx_arp_request_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of ARP request packets received.
        rx_arp_reply_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of ARP reply packets received.
        rx_ping_request_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of PING request packets received.
        rx_ping_reply_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of PING reply packets received.
        gap_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of gap-monitored gaps encountered.
        gap_duration: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, combined duration of gap-monitored gaps encountered, microseconds.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning special packets received on a port since statistics were cleared.

        :return: number of packets with fcs error frames, pause frames, arp rxreq, arp rxrsp, ping rxreq, ping rxrsp, gap events, and gap microseconds.
        :rtype: PR_EXTRA.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PR_TPLDS:
    """
    Obtain the set of test payload IDs observed among the received packets since
    receive statistics were cleared. Traffic statistics for these test payload
    streams will have non-zero byte and packet count.
    """

    code: typing.ClassVar[int] = 243
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        test_payload_identifiers: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the identifiers of the test payload.

    def get(self) -> "Token[GetDataAttr]":
        """Get the set of test payload IDs observed among the received packets since
        receive statistics were cleared. Traffic statistics for these test payload
        streams will have non-zero byte and packet count.

        :return: the identifiers of the test payload
        :rtype: PR_TPLDS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PR_TPLDTRAFFIC:
    """
    Obtains traffic statistics concerning the packets with a particular test payload
    identifier received on a port.
    """

    code: typing.ClassVar[int] = 244
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _test_payload_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bit_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits received in the last second.
        packet_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received in the last second.
        byte_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes received since statistics were cleared.
        packet_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get traffic statistics concerning the packets with a particular test payload
        identifier received on a port.

        :return:
            number of bits received in the last second,
            number of packets received in the last second,
            number of bytes received since statistics were cleared,
            number of packets received since statistics were cleared

        :rtype: PR_TPLDTRAFFIC.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._test_payload_xindex]))


@register_command
@dataclass
class PR_TPLDERRORS:
    """
    Obtains statistics concerning errors in the packets with a particular test
    payload id received on a port. The error information is derived from analysing
    the various fields contained in the embedded test payloads of the received
    packets, independent of which chassis and port may have originated the packets.
    Note that packet-lost statistics involve both a transmitting port and a
    receiving port, and in particular knowing which port originated the packets with
    a particular test payload identifier. This information requires knowledge of the
    global test environment, and is not supported at the port-level.
    """

    code: typing.ClassVar[int] = 245
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _test_payload_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        dummy: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, not in use.
        non_incre_seq_event_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of non-incrementing-sequence-number events.
        swapped_seq_misorder_event_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of swapped-sequence-number misorder events.
        non_incre_payload_packet_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with non-incrementing payload content.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning errors in the packets with a particular test payload id received on a port.

        :return:
            number of non-incrementing-sequence-number events,
            number of swapped-sequence-number misorder events,
            number of packets with non-incrementing payload content

        :rtype: PR_TPLDERRORS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._test_payload_xindex]))


@register_command
@dataclass
class PR_TPLDLATENCY:
    """
    Obtains statistics concerning the latency experienced by the packets with a
    particular test payload id received on a port. The values are adjusted by the
    port-level P_LATENCYOFFSET value. A special value of -1 is returned if latency
    numbers are not applicable. Latency is only meaningful when the clocks of the
    transmitter and receiver are synchronized. This requires the two ports to be on
    the same test module, and it requires knowledge of the global test environment
    to ensure that packets are in fact routed between these ports.
    """

    code: typing.ClassVar[int] = 246
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _test_payload_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        min_val: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, minimum latency for test payload stream
        avg_val: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, average latency for test payload stream
        max_val: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, maximum latency for test payload stream
        avg_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, average latency over last 1-second period
        min_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, minimum latency during last 1-second period
        max_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, nanoseconds, maximum latency during last 1-second period

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning the latency experienced by the packets with a particular test payload id received on a port.

        :return: minimum|average|maximum latency (nanoseconds), average|average|maximum latency over last 1-second period (nanoseconds)
        :rtype: PR_TPLDLATENCY.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._test_payload_xindex]))


@register_command
@dataclass
class PR_FILTER:
    """
    Obtains statistics concerning the packets satisfying the condition of a
    particular filter for a port.
    """

    code: typing.ClassVar[int] = 247
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _filter_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bit_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits received in the last second.
        packet_count_last_sec: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received in the last second.
        byte_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes received since statistics were cleared.
        packet_count_since_cleared: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning the packets satisfying the condition of a particular filter for a port

        :return:
            number of bits received in the last second,
            number of packets received in the last second,
            number of bytes received since statistics were cleared,
            number of packets received since statistics were cleared

        :rtype: PR_FILTER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._filter_xindex]))


@register_command
@dataclass
class PR_CLEAR:
    """
    Clear all the receive statistics for a port. The byte and packet counts will
    restart at zero.
    """

    code: typing.ClassVar[int] = 248
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clear all the receive statistics for a port. The byte and packet counts will
        restart at zero.
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
class PR_CALIBRATE:
    """
    Calibrate the latency calculation for packets received on a port. The lowest
    detected latency value (across all Test Payload IDs) will be set as the new
    base.
    """

    code: typing.ClassVar[int] = 249
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Calibrate the latency calculation for packets received on a port. The lowest
        detected latency value (across all Test Payload IDs) will be set as the new
        base.
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
class PR_UAT_STATUS:
    """
    This command will show the current UAT (UnAvailable Time) state, which is used
    in Valkyrie1564
    """

    code: typing.ClassVar[int] = 252
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the state of the affected stream counter.

    def get(self) -> "Token[GetDataAttr]":
        """Get the current UAT (UnAvailable Time) state, which is used
        in Valkyrie1564.

        :return: the state of the affected stream counter
        :rtype: PR_UAT_STATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PR_UAT_TIME:
    """
    This command will show the current number of unavailable seconds, which is used in Valkyrie1564.
    """

    code: typing.ClassVar[int] = 256
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        time: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of unavailable seconds.

    def get(self) -> "Token[GetDataAttr]":
        """Get the current UAT (UnAvailable Time) state, which is used
        in Valkyrie1564.

        :return: number of unavailable seconds
        :rtype: PR_UAT_TIME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PR_PFCSTATS:
    """
    Obtains statistics of received Priority Flow Control (PFC) packets on a port.
    """

    code: typing.ClassVar[int] = 374
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        rx_pfc_packet_count: XmpField[XmpLongList] = XmpField(XmpLongList)  # long integer, the total number of Priority Flow Control (PFC) packets received since statistics were cleared.

    def get(self) -> "Token[GetDataAttr]":
        """Get the statistics of received Priority Flow Control (PFC) packets on a port.

        :return: the total number of Priority Flow Control (PFC) packets received since statistics were cleared
        :rtype: PR_PFCSTATS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PR_FLOWTOTAL:
    """
    Obtains statistics concerning all the packets received from a flow between this
    receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1741
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        l2_bps: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bits received at layer 2 in the last second for the flow.
        pps: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received in the last second for the flow.
        byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes received since statistics were cleared for the flow.
        packet_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets received since statistics were cleared for the flow.

    def get(self) -> "Token[GetDataAttr]":
        """(Chimera only) Get statistics concerning all the packets received from a flow between this receive port and its partner TX port.

        :return:
            number of bits received at layer 2 in the last second for the flow,
            number of packets received in the last second for the flow,
            number of bytes received since statistics were cleared for the flow,
            number of packets received since statistics were cleared for the flow
            
        :rtype: PR_FLOWTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PR_FLOWCLEAR:
    """
    Clear all the receive statistics on a particular flow for a Chimera port. The
    byte and packet counts will restart at zero.
    """

    code: typing.ClassVar[int] = 1743
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """(Chimera only) Clear all the receive statistics on a particular flow for a Chimera port. The byte and packet counts will restart at zero.
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


