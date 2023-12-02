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
    XmpByte,
    XmpHex,
    XmpShort,
    XmpInt,
    XmpLong,
    XmpSequence,
    XmpStr,
    XmpMacAddress,
    XmpIPv4Address,
    Hex,
)
from .enums import (
    OnOff,
    IsPermanent,
    AutoOrManual,
    L47TrafficState,
    L47PortState,
    L47PortSpeed,
    IsPresent,
    LicenseSpeed,
    DhcpState,
    DhcpVlanState
)
from . import subtypes


@register_command
@dataclass
class P4_TRAFFIC:
    """
    Gives a traffic state command to a L47 port.
    """

    code: typing.ClassVar[int] = 700
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        traffic_state: L47TrafficState = field(XmpByte())
        """coded byte, the traffic state command issued to the port."""

    def set(self, traffic_state: L47TrafficState) -> Token[None]:
        """Set L47 port traffic state.

        :param traffic_state: the traffic state command issued to the port
        :type traffic_state: L47TrafficState
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, traffic_state=traffic_state))

    set_off = functools.partialmethod(set, L47TrafficState.OFF)
    """Set L47 port traffic state to Off."""

    set_on = functools.partialmethod(set, L47TrafficState.ON)
    """Set L47 port traffic state to On."""

    set_stop = functools.partialmethod(set, L47TrafficState.STOP)
    """Set L47 port traffic state to Stop."""

    set_prepare = functools.partialmethod(set, L47TrafficState.PREPARE)
    """Set L47 port traffic state to Prepare."""

    set_prerun = functools.partialmethod(set, L47TrafficState.PRERUN)
    """Set L47 port traffic state to Prerun."""


@register_command
@dataclass
class P4_STATE:
    """
    Display the current state of the L47 port.
    """

    code: typing.ClassVar[int] = 701
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        state: L47PortState = field(XmpByte())
        """coded byte, specifying the current state for this port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the current state of the L47 port.

        :return: the current state of the L47 port
        :rtype: P4_STATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_CAPABILITIES:
    """
    Report the speeds supported by the L47 port.
    """

    code: typing.ClassVar[int] = 702
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        auto: int = field(XmpByte())
        """byte, autoneg supported"""
        N100_mbps: int = field(XmpByte())
        """byte, 100M speed supported"""
        N1_gbps: int = field(XmpByte())
        """byte, 1G speed supported"""
        N2_5_gbps: int = field(XmpByte())
        """byte, 2.5G speed supported"""
        N5_gbps: int = field(XmpByte())
        """byte, 5G speed supported"""
        N10_gbps: int = field(XmpByte())
        """byte, 10G speed supported"""
        N25_gbps: int = field(XmpByte())
        """byte, 25G speed supported"""
        N40_gbps: int = field(XmpByte())
        """byte, 40G speed supported"""
        N50_gbps: int = field(XmpByte())
        """byte, 50G speed supported"""
        N100_gbps: int = field(XmpByte())
        """byte, 100G speed supported"""

    def get(self) -> Token[GetDataAttr]:
        """Get the speeds supported by the L47 port.

        :return: the speeds supported by the L47 port
        :rtype: P4_CAPABILITIES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_STATE_STATUS:
    """
    Returns status of the last port state change. If the port state has changed to
    PREPARE_FAIL, the status contains information about the reason for the fail.
    Currently the status will be "OK"in all other states.
    """

    code: typing.ClassVar[int] = 703
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        status: str = field(XmpStr())
        """string, status for the last port state change"""

    def get(self) -> Token[GetDataAttr]:
        """Get status of the last port state change.

        :return: status of the last port state change
        :rtype: P4_STATE_STATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_VLAN_OFFLOAD:
    """
    Specifies if 802.1Q VLAN tag should be inserted and stripped by the Ethernet
    device. If VLAN Offload is switched ON, VLAN tags will not be present in frames
    captured by the L47 Server.
    """

    code: typing.ClassVar[int] = 704
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        offload: OnOff = field(XmpByte())
        """coded byte, specifies if VLAN Offload is switched ON"""

    class SetDataAttr(RequestBodyStruct):
        offload: OnOff = field(XmpByte())
        """coded byte, specifies if VLAN Offload is switched ON"""

    def get(self) -> Token[GetDataAttr]:
        """Get the VLAN offload status.

        :return: VLAN offload status
        :rtype: P4_VLAN_OFFLOAD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, offload: OnOff) -> Token[None]:
        """Set the VLAN offload state.

        :param offload: specifies if VLAN Offload is enabled
        :type offload: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, offload=offload))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable VLAN offload."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable VLAN offload."""


@register_command
@dataclass
class P4_ARP_CONFIG:
    """
    Configure the value of the ARP request transmission rate, retransmission timeout
    and max. retries.
    """

    code: typing.ClassVar[int] = 705
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        rate: int = field(XmpInt())
        """integer, ARP Request transmission rate (requests / sec) - must be larger than 0"""
        retrans_timeout: int = field(XmpInt())
        """integer, ARP Request retransmission timeout [ms] - must be larger than 0"""
        retries: int = field(XmpByte())
        """byte, maximum ARP Request retransmission retries"""

    class SetDataAttr(RequestBodyStruct):
        rate: int = field(XmpInt())
        """integer, ARP Request transmission rate (requests / sec) - must be larger than 0"""
        retrans_timeout: int = field(XmpInt())
        """integer, ARP Request retransmission timeout [ms] - must be larger than 0"""
        retries: int = field(XmpByte())
        """byte, maximum ARP Request retransmission retries"""

    def get(self) -> Token[GetDataAttr]:
        """Get the ARP configuration on the port.

        :return: the ARP configuration on the port
        :rtype: P4_ARP_CONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, rate: int, retrans_timeout: int, retries: int) -> Token[None]:
        """Set the ARP configuration on the port.

        :param rate: ARP Request transmission rate (requests/sec) - must be larger than 0
        :type rate: int
        :param retrans_timeout: ARP Request retransmission timeout [ms] - must be larger than 0
        :type retrans_timeout: int
        :param retries: maximum ARP Request retransmission retries
        :type retries: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, rate=rate, retrans_timeout=retrans_timeout, retries=retries))


@register_command
@dataclass
class P4_NDP_CONFIG:
    """
    Configure the value of the NDP Neighbor Solicitation transmission rate,
    retransmission timeout and max. retries.
    """

    code: typing.ClassVar[int] = 706
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        rate: int = field(XmpInt())
        """integer, NDP Neighbor Solicitation transmission rate (requests / sec) - must be larger than 0"""
        retrans_timeout: int = field(XmpInt())
        """integer, NDP Neighbor Solicitation retransmission timeout [ms] - must be larger than 0"""
        retries: int = field(XmpByte())
        """byte, Max. NDP Neighbor Solicitation retransmission retries"""

    class SetDataAttr(RequestBodyStruct):
        rate: int = field(XmpInt())
        """integer, NDP Neighbor Solicitation transmission rate (requests / sec) - must be larger than 0"""
        retrans_timeout: int = field(XmpInt())
        """integer, NDP Neighbor Solicitation retransmission timeout [ms] - must be larger than 0"""
        retries: int = field(XmpByte())
        """byte, Max. NDP Neighbor Solicitation retransmission retries"""

    def get(self) -> Token[GetDataAttr]:
        """Get the NDP configuration on the port.

        :return: the NDP configuration on the port
        :rtype: P4_NDP_CONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, rate: int, retrans_timeout: int, retries: int) -> Token[None]:
        """Set the NDP configuration on the port.

        :param rate: NDP Neighbor Solicitation transmission rate (requests/sec) - must be larger than 0
        :type rate: int
        :param retrans_timeout: NDP Neighbor Solicitation retransmission timeout [ms] - must be larger than 0
        :type retrans_timeout: int
        :param retries: maximum NDP Neighbor Solicitation retransmission retries
        :type retries: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, rate=rate, retrans_timeout=retrans_timeout, retries=retries))


@register_command
@dataclass
class P4_CAPTURE:
    """
    Starts or stops packet capture on this port.
    """

    code: typing.ClassVar[int] = 707
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, specifying whether to capture traffic on this port"""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, specifying whether to capture traffic on this port"""

    def get(self) -> Token[GetDataAttr]:
        """Get packet capture state on this port.

        :return: packet capture state on this port
        :rtype: P4_CAPTURE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set packet capture state on this port.

        :param on_off: specifying whether to capture traffic on this port
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Stop packet capture on this port."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """Start packet capture on this port."""


@register_command
@dataclass
class P4_CAPTURE_GET_FIRST:
    """
    Returns the first captured frame on the port. Command is only valid when port is
    in state STOPPED
    """

    code: typing.ClassVar[int] = 708
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        index: int = field(XmpInt())
        """integer, index of frame returned"""
        second: int = field(XmpInt())
        """integer, second value of frame capture timestamp"""
        microsecond: int = field(XmpInt())
        """integer, microsecond value of frame capture timestamp"""
        capture_length: int = field(XmpInt())
        """integer, length of captured portion of the frame"""
        frame_length: int = field(XmpInt())
        """integer, length of the frame"""
        frame: Hex = field(XmpHex())
        """list of hex bytes, the captured frame (capture_len bytes)"""

    def get(self) -> Token[GetDataAttr]:
        """Get the first captured frame on the port

        :return: the first captured frame on the port
        :rtype: P4_CAPTURE_GET_FIRST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_CAPTURE_GET_NEXT:
    """
    Returns the next captured frame on the port. Command is only valid when port is
    in state STOPPED
    """

    code: typing.ClassVar[int] = 709
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        index: int = field(XmpInt())
        """integer, index of frame returned"""
        second: int = field(XmpInt())
        """integer, second value of frame capture timestamp"""
        microsecond: int = field(XmpInt())
        """integer, microsecond value of frame capture timestamp"""
        capture_length: int = field(XmpInt())
        """integer, length of captured portion of the frame"""
        frame_length: int = field(XmpInt())
        """integer, length of the frame"""
        frame: Hex = field(XmpHex())
        """hex data, the captured frame (capture_len bytes)"""

    def get(self) -> Token[GetDataAttr]:
        """Get the next captured frame on the port

        :return: the next captured frame on the port
        :rtype: P4_CAPTURE_GET_NEXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ETH_TX_COUNTERS:
    """
    Return total port Ethernet transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 710
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        bits_per_sec: int = field(XmpLong())
        """long integer, bit/second of (layer 2) bytes transmitted"""
        packets_per_sec: int = field(XmpLong())
        """long integer, packets/second of packets transmitted"""
        byte_count: int = field(XmpLong())
        """long integer, total number of (layer 2) bytes transmitted"""
        packet_count: int = field(XmpLong())
        """long integer, total number of packets transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total port Ethernet transmit statistics since last clear.

        :return: total port Ethernet transmit statistics since last clear.
        :rtype: P4_ETH_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ETH_RX_COUNTERS:
    """
    Return total port Ethernet receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 711
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        bits_per_sec: int = field(XmpLong())
        """long integer, bit/second of (layer 2) bytes received"""
        packets_per_sec: int = field(XmpLong())
        """long, integer packets/second of received packets"""
        byte_count: int = field(XmpLong())
        """long integer, total number of (layer 2) bytes received"""
        packet_count: int = field(XmpLong())
        """long integer, total number of packets received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total port Ethernet receive statistics since last clear.

        :return: total port Ethernet receive statistics since last clear.
        :rtype: P4_ETH_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_PORT_TX_COUNTERS:
    """
    Return total port transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 712
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        vlan_packet_count: int = field(XmpLong())
        """long integer, total number of 802.1Q VLAN tagged packets transmitted"""
        bits_per_sec: int = field(XmpLong())
        """long integer, bit/second of (layer 1) bits transmitted."""
        byte_count: int = field(XmpLong())
        """long integer, total number of (layer 1) bytes received."""

    def get(self) -> Token[GetDataAttr]:
        """Get total port transmit statistics since last clear.

        :return: total port transmit statistics since last clear.
        :rtype: P4_PORT_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_PORT_RX_COUNTERS:
    """
    Return total port receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 713
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        vlan_packet_count: int = field(XmpLong())
        """long integer, total number of 802.1Q VLAN tagged packets received"""
        bits_per_sec: int = field(XmpLong())
        """long integer, bit/second of (layer 1) bits received."""
        byte_count: int = field(XmpLong())
        """long integer, total number of (layer 1) bytes received."""

    def get(self) -> Token[GetDataAttr]:
        """Get total port receive statistics since last clear.

        :return: total port receive statistics since last clear.
        :rtype: P4_PORT_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_PORT_COUNTERS:
    """
    Return total port transmit error statistics since last clear.
    """

    code: typing.ClassVar[int] = 714
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        invalid_eth_count: int = field(XmpLong())
        """long integer, total number of invalid (e.g. short) Ethernet packets received"""
        unknown_eth_count: int = field(XmpLong())
        """long integer, total number of unknown or unsupported Ethernet packets received"""
        mismatch_vlan_error_count: int = field(XmpLong())
        """long integer, total number of packets with mismatching vlan info received"""
        pkt_rate_limit_count: int = field(XmpLong())
        """long integer, number of times that number of packets transmitted has been limited by the maximum packet rate limiter."""

    def get(self) -> Token[GetDataAttr]:
        """Get total port transmit error statistics since last clear.

        :return: total port transmit error statistics since last clear.
        :rtype: P4_PORT_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_TX_PACKET_SIZE:
    """
    Return histogram over transmitted (layer 2) packets sizes in 100 bytes intervals.
    """

    code: typing.ClassVar[int] = 715
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        bin_00: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_01: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_02: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_03: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_04: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_05: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_06: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_07: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_08: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_09: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_10: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_11: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_12: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_13: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_14: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_15: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""

    def get(self) -> Token[GetDataAttr]:
        """Get a histogram over transmitted (layer 2) packets sizes in 100 bytes intervals.

        :return: histogram over transmitted (layer 2) packets sizes in 100 bytes intervals.
        :rtype: P4_TX_PACKET_SIZE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_RX_PACKET_SIZE:
    """
    Return a histogram over received (layer 2) packets sizes in 100 bytes intervals.
    """

    code: typing.ClassVar[int] = 716
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        bin_00: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_01: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_02: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_03: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_04: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_05: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_06: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_07: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_08: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_09: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_10: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_11: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_12: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_13: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_14: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""
        bin_15: int = field(XmpLong())
        """long integer, number of packets received with a (layer 2) size in the given interval."""

    def get(self) -> Token[GetDataAttr]:
        """Get a histogram over received (layer 2) packets sizes in 100 bytes intervals.

        :return: a histogram over received (layer 2) packets sizes in 100 bytes intervals.
        :rtype: P4_RX_PACKET_SIZE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_TX_MTU:
    """
    Return histogram over transmitted (layer 3) packets sizes in 1 byte intervals.
    Each bin represents a packet size in the interval [576..1500] bytes.
    """

    code: typing.ClassVar[int] = 717
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bins: typing.List[int] = field(XmpSequence(types_chunk=[XmpByte()]))
        """925 x byte, '1' if any packets were transmitted with the specified layer 3 size, otherwise '0'."""

    def get(self) -> Token[GetDataAttr]:
        """Get histogram over transmitted (layer 3) packets sizes in 1 byte intervals.

        :return: histogram over transmitted (layer 3) packets sizes in 1 byte intervals.
        :rtype: P4_TX_MTU.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_RX_MTU:
    """
    Return histogram over received (layer 3) packets sizes in 1 byte intervals. Each
    bin represents a packet size in the interval [576..1500] bytes.
    """

    code: typing.ClassVar[int] = 718
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bins: typing.List[int] = field(XmpSequence(types_chunk=[XmpByte()]))
        """925 x byte, '1' if any packets were received with the specified layer 3 size, otherwise '0'."""

    def get(self) -> Token[GetDataAttr]:
        """Get histogram over received (layer 3) packets sizes in 1 byte intervals.

        :return: histogram over received (layer 3) packets sizes in 1 byte intervals.
        :rtype: P4_RX_MTU.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_IPV4_RX_COUNTERS:
    """
    Return total Port IPv4 protocol receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 719
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of IPv4 packets received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port IPv4 protocol receive statistics since last clear.

        :return: total Port IPv4 protocol receive statistics since last clear.
        :rtype: P4_IPV4_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_IPV4_TX_COUNTERS:
    """
    Return total Port IPv4 protocol transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 720
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of IPv4 packets transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port IPv4 protocol transmit statistics since last clear.

        :return: total Port IPv4 protocol transmit statistics since last clear.
        :rtype: P4_IPV4_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_IPV4_COUNTERS:
    """
    Return total Port IPv4 protocol error statistics since last clear.
    """

    code: typing.ClassVar[int] = 721
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        checksum_error_count: int = field(XmpLong())
        """long integer, total number of IPv4 packets which ip header checksum error"""
        invalid_packet_count: int = field(XmpLong())
        """long integer, total number of IPv4 packets which are malformed"""
        unknown_packet_count: int = field(XmpLong())
        """long integer, total number of IPv4 packets with unknown protocol"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port IPv4 protocol error statistics since last clear.

        :return: total Port IPv4 protocol error statistics since last clear.
        :rtype: P4_IPV4_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_IPV6_RX_COUNTERS:
    """
    Return total Port IPv6 protocol receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 722
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of IPv6 packets received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port IPv6 protocol receive statistics since last clear.

        :return: total Port IPv6 protocol receive statistics since last clear.
        :rtype: P4_IPV6_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_IPV6_TX_COUNTERS:
    """
    Return total Port IPv6 protocol transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 723
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of IPv6 packets transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port IPv6 protocol transmit statistics since last clear.

        :return: total Port IPv6 protocol transmit statistics since last clear.
        :rtype: P4_IPV6_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_IPV6_COUNTERS:
    """
    Return total Port IPv6 protocol error statistics since last clear.
    """

    code: typing.ClassVar[int] = 724
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        invalid_packet_count: int = field(XmpLong())
        """long integer, total number of ipv6 packets which are malformed"""
        unknown_packet_count: int = field(XmpLong())
        """long integer, total number of ipv6 packets with unknown protocol"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port IPv6 protocol error statistics since last clear.

        :return: total Port IPv6 protocol error statistics since last clear.
        :rtype: P4_IPV6_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ARP_RX_COUNTERS:
    """
    Return total Port ARP protocol receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 725
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        arp_request_count: int = field(XmpLong())
        """long integer, total number ARP Requests received"""
        arp_reply_count: int = field(XmpLong())
        """long integer, total number ARP Replies received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port ARP protocol receive statistics since last clear.

        :return: total Port ARP protocol receive statistics since last clear.
        :rtype: P4_ARP_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ARP_TX_COUNTERS:
    """
    Return total Port ARP protocol transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 726
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        arp_request_count: int = field(XmpLong())
        """long integer, total number ARP Requests transmitted"""
        arp_reply_count: int = field(XmpLong())
        """long integer, total number ARP Replies transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port ARP protocol transmit statistics since last clear.

        :return: total Port ARP protocol transmit statistics since last clear.
        :rtype: P4_ARP_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ARP_COUNTERS:
    """
    Return total Port ARP protocol error statistics since last clear.
    """

    code: typing.ClassVar[int] = 727
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        invalid_arp_count: int = field(XmpLong())
        """long integer, total number of invalid ARP packets received"""
        arp_request_lookup_failure_count: int = field(XmpLong())
        """long integer, number of ARP requests received that could not be resolved"""
        arp_reply_lookup_failure_count: int = field(XmpLong())
        """long integer, number of ARP replies received that could not be resolved"""
        arp_request_retrans_count: int = field(XmpLong())
        """long integer, number of retransmitted ARP requests"""
        arp_resolved_count: int = field(XmpLong())
        """long integer, number of correct resolved IP addresses"""
        arp_failed_count: int = field(XmpLong())
        """long integer, number of IP address that was not resolved"""
        arp_table_lookup_failure_count: int = field(XmpLong())
        """long integer, number of dest IP addresses not found in the ARP table"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port ARP protocol error statistics since last clear.

        :return: total Port ARP protocol error statistics since last clear.
        :rtype: P4_ARP_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_NDP_RX_COUNTERS:
    """
    Return total Port NDP protocol receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 728
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        ndp_request_count: int = field(XmpLong())
        """long integer, total number NDP Requests received"""
        ndp_reply_count: int = field(XmpLong())
        """long integer, total number NDP Replies received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port NDP protocol receive statistics since last clear.

        :return: total Port NDP protocol receive statistics since last clear.
        :rtype: P4_NDP_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_NDP_TX_COUNTERS:
    """
    Return total Port NDP protocol transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 729
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        ndp_request_count: int = field(XmpLong())
        """long integer, total number NDP Requests transmitted"""
        ndp_reply_count: int = field(XmpLong())
        """long integer, total number NDP Replies transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port NDP protocol transmit statistics since last clear.

        :return: total Port NDP protocol transmit statistics since last clear.
        :rtype: P4_NDP_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_NDP_COUNTERS:
    """
    Return total Port NDP protocol error statistics since last clear.
    """

    code: typing.ClassVar[int] = 730
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        invalid_ndp_count: int = field(XmpLong())
        """long integer, total number of invalid NDP packets received"""
        ndp_request_lookup_failure_count: int = field(XmpLong())
        """long integer, number of NDP requests received that could not be resolved"""
        ndp_reply_lookup_failure_count: int = field(XmpLong())
        """long integer, number of NDP replies received that could not be resolved"""
        ndp_request_retrans_count: int = field(XmpLong())
        """long integer, number of retransmitted NDP requests"""
        ndp_resolved_count: int = field(XmpLong())
        """long integer, number of correct resolved IP addresses"""
        ndp_failed_count: int = field(XmpLong())
        """long integer, number of IP address that was not resolved"""
        ndp_table_lookup_failure_count: int = field(XmpLong())
        """long integer, number of dest IP addresses not found in the NDP table"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port NDP protocol error statistics since last clear.

        :return: total Port NDP protocol error statistics since last clear.
        :rtype: P4_NDP_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ICMP_RX_COUNTERS:
    """
    Return total Port ICMP protocol receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 731
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        icmp_echo_request_count: int = field(XmpLong())
        """long integer, total number of ICMP Echo requests received"""
        icmp_echo_reply_count: int = field(XmpLong())
        """long integer, total number of ICMP Echo replies received"""
        icmp_dest_unknown_count: int = field(XmpLong())
        """long integer, total number of ICMP Destination unknown received"""
        icmp_time_excessive_count: int = field(XmpLong())
        """long integer, total number of ICMP Time exceeded received"""
        icmpv6_count: int = field(XmpLong())
        """long integer, total number of ICMPv6 packets received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port ICMP protocol receive statistics since last clear.

        :return: total Port ICMP protocol receive statistics since last clear.
        :rtype: P4_ICMP_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ICMP_TX_COUNTERS:
    """
    Return total Port ICMP protocol transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 732
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        icmp_echo_request_count: int = field(XmpLong())
        """long integer, total number of ICMP Echo requests transmitted"""
        icmp_echo_reply_count: int = field(XmpLong())
        """long integer, total number of ICMP Echo replies transmitted"""
        icmp_dest_unknown_count: int = field(XmpLong())
        """long integer, total number of ICMP Destination unknown transmitted"""
        icmp_time_excessive_count: int = field(XmpLong())
        """long integer, total number of ICMP Time exceeded transmitted"""
        icmpv6_count: int = field(XmpLong())
        """long integer, total number of ICMPv6 packets transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port ICMP protocol transmit statistics since last clear.

        :return: total Port ICMP protocol transmit statistics since last clear.
        :rtype: P4_ICMP_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ICMP_COUNTERS:
    """
    Return total Port ICMP protocol error statistics since last clear.
    """

    code: typing.ClassVar[int] = 733
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        invalid_icmp_count: int = field(XmpLong())
        """long integer, total number of unknown or invalid ICMP packets received"""
        unknown_icmp_count: int = field(XmpLong())
        """long integer, total number of unknown or unsupported ICMP packets received"""
        invalid_icmpv6_count: int = field(XmpLong())
        """long integer, total number of unknown or invalid ICMPv6 packets received"""
        unknown_icmpv6_count: int = field(XmpLong())
        """long integer, total number of unknown or unsupported ICMPv6 packets received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port ICMP protocol error statistics since last clear.

        :return: total Port ICMP protocol error statistics since last clear.
        :rtype: P4_ICMP_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_TCP_RX_COUNTERS:
    """
    Return total Port TCP protocol receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 734
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of TCP packets received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port TCP protocol receive statistics since last clear.

        :return: total Port TCP protocol receive statistics since last clear.
        :rtype: P4_TCP_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_TCP_TX_COUNTERS:
    """
    Return total Port TCP protocol transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 735
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of TCP packets transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port TCP protocol transmit statistics since last clear.

        :return: total Port TCP protocol transmit statistics since last clear.
        :rtype: P4_TCP_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_TCP_COUNTERS:
    """
    Return total Port TCP protocol error statistics since last clear.
    """

    code: typing.ClassVar[int] = 736
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        checksum_error_count: int = field(XmpLong())
        """long integer, total number of tcp packets which tcp header checksum error"""
        invalid_tcp_count: int = field(XmpLong())
        """long integer, total number of TCP packets which are malformed"""
        tcp_lookup_failure_count: int = field(XmpLong())
        """long integer, number of TCP packets received that could not be resolved"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port TCP protocol error statistics since last clear.

        :return: total Port TCP protocol error statistics since last clear.
        :rtype: P4_TCP_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_UDP_RX_COUNTERS:
    """
    Return total Port UDP protocol receive statistics since last clear.
    """

    code: typing.ClassVar[int] = 737
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of UDP packets received"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port UDP protocol receive statistics since last clear.

        :return: total Port UDP protocol receive statistics since last clear.
        :rtype: P4_UDP_RX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_UDP_TX_COUNTERS:
    """
    Return total Port UDP protocol transmit statistics since last clear.
    """

    code: typing.ClassVar[int] = 738
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        packet_count: int = field(XmpLong())
        """long integer, total number of UDP packets transmitted"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port UDP protocol transmit statistics since last clear.

        :return: total Port UDP protocol transmit statistics since last clear.
        :rtype: P4_UDP_TX_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_UDP_COUNTERS:
    """
    Return total Port UDP protocol error statistics since last clear.
    """

    code: typing.ClassVar[int] = 739
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        checksum_error_count: int = field(XmpLong())
        """long integer, total number of udp packets which udp header checksum error"""
        invalid_udp_count: int = field(XmpLong())
        """long integer, total number of UDP packets which are malformed"""
        udp_lookup_failure_count: int = field(XmpLong())
        """long integer, number of UDP packets received that could not be resolved"""

    def get(self) -> Token[GetDataAttr]:
        """Get total Port UDP protocol error statistics since last clear.

        :return: total Port UDP protocol error statistics since last clear.
        :rtype: P4_UDP_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_CLEAR_COUNTERS:
    """
    Clears all run-time port counters.
    """

    code: typing.ClassVar[int] = 740
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Clears all run-time port counters.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_ETH_COUNTERS:
    """
    Return total port Ethernet statistics since last clear.
    """

    code: typing.ClassVar[int] = 765
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_time: int = field(XmpLong())
        """long integer, the current time (mSec since module restart)"""
        ref_time: int = field(XmpLong())
        """long integer, reference time (mSec for P4_TRAFFIC on)"""
        tx_error_count: int = field(XmpLong())
        """long integer, TX errors"""
        rx_error_count: int = field(XmpLong())
        """long integer, RX errors"""
        rx_packet_lost_count: int = field(XmpLong())
        """long integer, packets lost by the Ethernet driver due to RX queue overflow"""

    def get(self) -> Token[GetDataAttr]:
        """Get total port Ethernet statistics since last clear.

        :return: total port Ethernet statistics since last clear.
        :rtype: P4_ETH_COUNTERS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_CLEAR:
    """
    Set the Port State to OFF and delete all configured Connection Groups for the port.
    """

    code: typing.ClassVar[int] = 766
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Set the Port State to OFF and delete all configured Connection Groups for the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_SPEEDSELECTION:
    """
    Sets the port speed. The selected speed must be one of the speeds supported by
    the port, which can be retrieved with P4_CAPABILITIES.
    """

    code: typing.ClassVar[int] = 767
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        speed: L47PortSpeed = field(XmpByte())
        """coded byte, specifies the speed of the port"""

    class SetDataAttr(RequestBodyStruct):
        speed: L47PortSpeed = field(XmpByte())
        """coded byte, specifies the speed of the port"""

    def get(self) -> Token[GetDataAttr]:
        """Get the port speed mode.

        :return: the port speed mode.
        :rtype: P4_SPEEDSELECTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, speed: L47PortSpeed) -> Token[None]:
        """Set the port speed mode.

        :param speed: specifies the speed mode of the port
        :type speed: L47PortSpeed
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, speed=speed))

    set_auto = functools.partialmethod(set, L47PortSpeed.AUTO)
    """Set the port speed mode to Auto."""

    set_f100m = functools.partialmethod(set, L47PortSpeed.F100M)
    """Set the port speed mode to 100 Mbit/s."""

    set_f1g = functools.partialmethod(set, L47PortSpeed.F1G)
    """Set the port speed mode to 1 Gbit/s."""

    set_f2_5g = functools.partialmethod(set, L47PortSpeed.F2_5G)
    """Set the port speed mode to 2.5 Gbit/s."""

    set_f5g = functools.partialmethod(set, L47PortSpeed.F5G)
    """Set the port speed mode to 5 Gbit/s."""

    set_f10g = functools.partialmethod(set, L47PortSpeed.F10G)
    """Set the port speed mode to 10 Gbit/s."""

    set_f25g = functools.partialmethod(set, L47PortSpeed.F25G)
    """Set the port speed mode to 25 Gbit/s."""

    set_f40g = functools.partialmethod(set, L47PortSpeed.F40G)
    """Set the port speed mode to 40 Gbit/s."""

    set_f50g = functools.partialmethod(set, L47PortSpeed.F50G)
    """Set the port speed mode to 50 Gbit/s."""

    set_f100g = functools.partialmethod(set, L47PortSpeed.F100G)
    """Set the port speed mode to 100 Gbit/s."""

@register_command
@dataclass
class P4_ETH_QUEUE_COUNTERS:
    """
    Get the stats of the all active queues of the port
    """

    code: typing.ClassVar[int] = 775
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        last_update:    int = field(XmpLong()) # long integer, the current time (mSec since module restart)
        stat_ref_time:  int = field(XmpLong()) # long integer, reference time (mSec for P4_TRAFFIC on)
        num_queues:     int = field(XmpInt())
        queue_list: typing.List[subtypes.QueueStatsElem] = field(XmpSequence(types_chunk=[XmpLong(), XmpLong(), XmpLong(), XmpLong()]))

    def get(self) -> "Token[GetDataAttr]":
        """Get the stats of the all active queues of the port
        :return: The current time (mSec since module restart)
        :rtype: P4_ETH_QUEUE_COUNTERS.GetDataAttr
        :return: Reference time (mSec for P4_TRAFFIC on)
        :rtype: P4_ETH_QUEUE_COUNTERS.GetDataAttr
        :return: Number of Active queues
        :rtype: P4_ETH_QUEUE_COUNTERS.GetDataAttr
        :return: A list that each contains stats of a queue
        :rtype: P4_ETH_QUEUE_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

@register_command
@dataclass
class P4_DHCP_CONFIG:
    """
    Configure DHCP Client in order to aquire a pool of ip addresses.
    """
    
    code: typing.ClassVar[int] = 780
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        num_requests:       int = field(XmpInt(signed=False))   # Number of DHCP requests to be sent
        retransmit_retries: int = field(XmpInt(signed=False))   # Max Request retransmission retries
        timeout:            int = field(XmpInt(signed=False))   # retransmission timeout [ms]
        base_hw_addr:       Hex = field(XmpMacAddress())        # base hw address for generating DHCP requests (the first 3 bytes are being used)

    class GetDataAttr(ResponseBodyStruct):
        num_requests:       int = field(XmpInt(signed=False))   # Number of DHCP request to acuire IP addresses
        retransmit_retries: int = field(XmpInt(signed=False))   # Max Request retransmission retries
        timeout:            int = field(XmpInt(signed=False))   # retransmission timeout [ms]
        base_hw_addr:       Hex = field(XmpMacAddress())        # base hw address for generating DHCP requests (the first 3 bytes is being used)

    def get(self) -> "Token[GetDataAttr]":
        """Get the DHCP configuration.

        :return: the DHCP configuration
        :rtype: P4_DHCP_CONFIG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, num_requests: int, retransmit_retries: int, timeout: int, base_hw_addr: str) -> "Token":
        """Set the DHCP configuration.

        :param num_requests: Number of DHCP requests - must be larger than 0
        :type num_requests: unsigned int
        :param retransmit_retries: maximum DHCP Request retransmission retries - must be larger than 0
        :type retransmit_retries: unsigned int
        :param timeout: retransmission timeout [ms]
        :type timeout: unsigned int
        :param base_hw_addr: base hw address for generating DHCP requests (the first 3 bytes is being used)
        :type base_hw_addr: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, num_requests=num_requests, 
                                                            retransmit_retries=retransmit_retries, timeout=timeout, base_hw_addr=base_hw_addr))


@register_command
@dataclass
class P4_DHCP_RUN:
    """
    Run DHCP Client process to obtain a pool of address.
    """

    code: typing.ClassVar[int] = 781
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> "Token":
        """Run DHCP Client Process.

        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_DHCP_STATE:
    """
    Get the last state of the DHCP Client Process.
    """

    code: typing.ClassVar[int] = 782
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        dhcp_state:     DhcpState   = field(XmpByte())  # The last state of the DHCP Client Process.
        num_success:    int         = field(XmpInt())   # Current number of successfully optained ip addresses
        num_failure:    int         = field(XmpInt())   # Current number of failed dhcp requests

    def get(self) -> "Token[GetDataAttr]":
        """Get the last state of the DHCP Client Process.
            The dhcp_state is an enum type of DhcpState{DHCP_STATE_UNKNOWN=0, DHCP_STATE_RUNNING=1, DHCP_STATE_COMPLETED=2, DHCP_STATE_FAILED=3}

        :return: the last state of the DHCP Client Process.
        :rtype: P4_DHCP_STATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_DHCP_RESULT:
    """
    Get the port's last DHCP client process result
    """

    code: typing.ClassVar[int] = 783
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        dhcp_chunks: typing.List[subtypes.DhcpChunk] = field(XmpSequence(types_chunk=[XmpIPv4Address(), XmpIPv4Address(), XmpIPv4Address(), XmpIPv4Address(), XmpInt(), XmpMacAddress()]))

    def get(self) -> "Token[GetDataAttr]":
        """Get the port's the result of the last DHCP client process

        :return: A list that contains the response for each DHCP request that had lunched by the last DHCP client process 
        :rtype: P4_DHCP_RESULT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_DHCP_VLAN:
    """
    Configure a set of VLAN tags for current DHCP Process.
    """

    code: typing.ClassVar[int] = 784
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    
    class SetDataAttr(RequestBodyStruct):
        state:  DhcpVlanState = field(XmpByte()) # Enable/Disable Vlan configuration
        vlans:  typing.List[subtypes.VlanTag] = field(XmpSequence(types_chunk=[XmpShort(), XmpByte()])) # A list of vlans. up to 8 TCIs can be define
    
    class GetDataAttr(ResponseBodyStruct):
        state:  DhcpVlanState = field(XmpByte()) # Determines whether VLAN is configured or not.
        vlans:  typing.List[subtypes.VlanTag] = field(XmpSequence(types_chunk=[XmpShort(), XmpByte()])) # A list of vlans. up to 8 TCIs can be define

    def set(self, state: DhcpVlanState, vlans: typing.List[subtypes.VlanTag]) -> "Token":
        """Set a list of VLANs for current DHCP Process, up to 8 TCIs can be defined. The order of the VLANs is like the following: ethernet/vlan0/vlan1/../vlanN/uppler_layer(like IPv4)
            
        :param state: Enable/Disable Vlan configuration
        :type state: DhcpVlanState
        :param vlans: specifying a list of VlanTag
        :type vlans: typing.List[subtypes.VlanTag]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, 
                                                            state=state, vlans=vlans))
    def get(self) -> "Token[GetDataAttr]":
        """Get the DHCP VLAN configuration
        :return: Whether DHCP VLAN is configured or not
        :rtype:  P4_DHCP_RESULT.GetDataAttr
        :return: A list of vlans 
        :rtype: P4_DHCP_RESULT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

@register_command
@dataclass
class P4_MAX_PACKET_RATE:
    """
    Specifies the maximum number of packets per second allowed to be transmitted on the port.
    """

    code: typing.ClassVar[int] = 950
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: AutoOrManual = field(XmpByte())
        """coded byte, specifies the mode of the max. pps mechanism"""
        rate: int = field(XmpInt())
        """integer, maximum number of packets per second to transmit on this port"""
        time_window: int = field(XmpInt())
        """integer, time window [us] to measure the pps rate"""

    class SetDataAttr(RequestBodyStruct):
        mode: AutoOrManual = field(XmpByte())
        """coded byte, specifies the mode of the max. pps mechanism"""
        rate: int = field(XmpInt())
        """integer, maximum number of packets per second to transmit on this port"""
        time_window: int = field(XmpInt())
        """integer, time window [us] to measure the pps rate"""

    def get(self) -> Token[GetDataAttr]:
        """Get the maximum number of packets per second allowed to be transmitted on the port.

        :return: the maximum number of packets per second allowed to be transmitted on the port.
        :rtype: P4_MAX_PACKET_RATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: AutoOrManual, rate: int, time_window: int) -> Token[None]:
        """Set the maximum number of packets per second allowed to be transmitted on the port.

        :param mode: specifies the mode of the max. pps mechanism
        :type mode: AutoOrManual
        :param rate: maximum number of packets per second to transmit on this port
        :type rate: int
        :param time_window: time window [us] to measure the pps rate
        :type time_window: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode, rate=rate, time_window=time_window))

    set_automatic = functools.partialmethod(set, AutoOrManual.AUTOMATIC)
    """Set port max packet rate mode to Automatic."""

    set_manual = functools.partialmethod(set, AutoOrManual.MANUAL)
    """Set port max packet rate mode to Manual."""


@register_command
@dataclass
class P4_PCI_INFO:
    """
    Report the port PCI info.
    """

    code: typing.ClassVar[int] = 960
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        vendor_id: Hex = field(XmpHex(size=4))
        """four hex bytes, PCI Vendor ID"""
        device_id: Hex = field(XmpHex(size=4))
        """four hex bytes, PCI Device ID"""
        sub_vendor_id: Hex = field(XmpHex(size=4))
        """four hex bytes, PCI Subsystem Vendor ID"""
        sub_device_id: Hex = field(XmpHex(size=4))
        """four hex bytes, PCI Subsystem Device ID"""
        rev: int = field(XmpInt())
        """integer, Revision"""

    def get(self) -> Token[GetDataAttr]:
        """Get the port PCI info.

        :return: the port PCI info
        :rtype: P4_PCI_INFO.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_FW_VER:
    """
    Report the firmware version of the port (NIC).
    """

    code: typing.ClassVar[int] = 961
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        major: int = field(XmpInt())
        """integer, Major firmware version"""
        minor: int = field(XmpInt())
        """integer, Minor firmware version"""

    def get(self) -> Token[GetDataAttr]:
        """Get the firmware version of the port (NIC).

        :return: the firmware version of the port (NIC)
        :rtype: P4_FW_VER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_DEV_NAME:
    """
    Report the name of the device (NIC) on which the port is located.
    """

    code: typing.ClassVar[int] = 962
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        name: str = field(XmpStr())
        """string, name of the device (NIC) on which the port is located"""

    def get(self) -> Token[GetDataAttr]:
        """Get the name of the device (NIC) on which the port is located.

        :return: the name of the device (NIC) on which the port is located.
        :rtype: P4_DEV_NAME.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_PORT_TYPE:
    """
    Report the port type. The different possible ports are divided into types.
    """

    code: typing.ClassVar[int] = 963
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        type_number: int = field(XmpInt())
        """integer, enumerated port type"""
        type_string: str = field(XmpStr())
        """string, textual representation of the port type"""

    def get(self) -> Token[GetDataAttr]:
        """Get the L47 port type.

        :return: the L47 port type
        :rtype: P4_PORT_TYPE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_LICENSE_INFO:
    """
    Returns the information on the license assigned to the port - if any.
    """

    code: typing.ClassVar[int] = 964
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        present: IsPresent = field(XmpByte())
        """coded byte, specifies if a license is assigned to the port"""
        speed: LicenseSpeed = field(XmpByte())
        """coded byte, if a license is assigned to the port, specifies the speed of the license"""
        permanency: IsPermanent = field(XmpByte())
        """coded byte, if a license is assigned to the port, specifies if the license is permanent"""
        expiration: int = field(XmpLong())
        """long integer, if a license is assigned to the port and it is not permanent, specifies the expiration date of the license - in seconds since Jan 1, 1970."""

    def get(self) -> Token[GetDataAttr]:
        """Get the information on the license assigned to the port.

        :return: the information on the license assigned to the port
        :rtype: P4_LICENSE_INFO.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4_APTITUDES:
    """
    Returns the ports aptitudes - i.e. what is possible to configure on the port in
    terms of features and performance.

    Current schema of the BSON document:

    .. code-block::

        schema = {
            'chassis': {
                'type': 'int32',
                'required': True,
                'enum': ['CHASSIS_TYPE_UNKNOWN',
                        'CHASSIS_TYPE_APPLIANCE',
                        'CHASSIS_TYPE_BAY',
                        'CHASSIS_TYPE_COMPACT',
                        'CHASSIS_TYPE_SAFIRE']
            },
            'tcp_udp': {
                'type': 'document',
                'required': True,
                'properties': {
                    'cc': {
                        'type': 'int32',
                        'required': True,
                    },
                }
            },
            'tls': {
                'type': 'document',
                'required': True,
                'properties': {
                    'supported': {
                        'type': 'bool',
                        'required': True,
                    },
                    'cc': {
                        'type': 'int32',
                        'required': True,
                    }
                }
            }
        }
    """

    code: typing.ClassVar[int] = 1200
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bson: typing.List[int] = field(XmpSequence(types_chunk=[XmpByte()]))
        """list of hex bytes, bson document containing the ports aptitudes"""

    def get(self) -> Token[GetDataAttr]:
        """Get the ports aptitudes

        :return: the ports aptitudes in BSON format
        :rtype: P4_APTITUDES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
