from __future__ import annotations
from dataclasses import dataclass
import ipaddress
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
    XmpInt,
    XmpIPv4Address,
    XmpIPv6Address,
    XmpLong,
    XmpShort,
    XmpMacAddress,
    XmpSequence,
    XmpStr,
    Hex,
)
from .subtypes import (
    ArpChunk,
    NdpChunk,
)
from .enums import (
    ReservedStatus,
    ReservedAction,
    OnOff,
    YesNo,
    PortSpeedMode,
    SyncStatus,
    LoopbackMode,
    TrafficOnOff,
    StartOrStop,
    LatencyMode,
    MDIXMode,
    MulticastOperation,
    MulticastExtOperation,
    IGMPVersion,
    TXMode,
    PayloadMode,
    BRRMode,
    TXHState,
    RXHState,
    TXCState,
    RXCState,
    LinkState,
    FaultSignaling,
    LocalFaultStatus,
    RemoteFaultStatus,
    TPLDMode,
    MulticastHeaderFormat,
    TrafficError,
    TrafficEngine,
    ReconciliationSublayerSupport,
    MACSecSCIMode,
    MACSecCipherSuite,
    # MACSecVLANMode,
    MACSecRekeyMode,
    MACSecEncryptionMode,
    MACSecPNMode,
)


@register_command
@dataclass
class P_RESERVATION:
    """
    You set this command to reserve, release, or relinquish a port. The port must be reserved before any of its configuration can be changed, including streams, filters, capture, and datasets.The owner of the session must already have been specified. Reservation will fail if the chassis or module is reserved to other users.
    """

    code: typing.ClassVar[int] = 102
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        status: ReservedStatus = field(XmpByte())
        """coded byte, containing the operation to perform.
        The reservation parameters are asymmetric with respect to set/get.
        When set, it contains the operation to perform. When get, it contains the status.
        """

    class SetDataAttr(RequestBodyStruct):
        operation: ReservedAction = field(XmpByte())
        """coded byte, containing the operation to perform.
        The reservation parameters are asymmetric with respect to set/get.
        When set, it contains the operation to perform.
        When get, it contains the status.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the reservation status of the test port.

        :return: the reservation status of the test port.
        :rtype: ReservedStatus
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, operation: ReservedAction) -> Token[None]:
        """Set the reservation of the test port, i.e., reserve, release, or relinquish.

        :param operation: the reservation of the test port, i.e., reserve, release, or relinquish.
        :type operation: ReservedAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, operation=operation))

    set_release = functools.partialmethod(set, ReservedAction.RELEASE)
    """Release the port from your ownership.
    """

    set_reserve = functools.partialmethod(set, ReservedAction.RESERVE)
    """Reserve the port.
    """

    set_relinquish = functools.partialmethod(set, ReservedAction.RELINQUISH)
    """Release the port from others' ownership.
    """


@register_command
@dataclass
class P_RESERVEDBY:
    """
    Identify the user who has a port reserved. The empty string if the port is not currently reserved. Note that multiple connections can specify the same name with C_OWNER, but a resource can only be reserved to one connection. Therefore you cannot count on having the port just because it is reserved in your name. The port is reserved to this connection only if P_RESERVATION returns RESERVED_BY_YOU.
    """

    code: typing.ClassVar[int] = 103
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        username: str = field(XmpStr())
        """string, containing the name of the current owner of the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the username of the user who has the port reserved.

        :return: the username of the user who has the port reserved.
        :rtype: P_RESERVEDBY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_RESET:
    """
    Reset port-level parameters to standard values, and delete all streams, filters,
    capture, and dataset definitions.
    """

    code: typing.ClassVar[int] = 104
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Reset the port to its default configuration.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_CAPABILITIES:
    """
    A series of integer values specifying various internal limits of a port.
    integer: integer, internally defined limit values.
    """

    code: typing.ClassVar[int] = 106
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        max_speed: int = field(XmpInt())
        """integer, max wire speed in Mbps, for fastest transceiver and mode"""
        max_speed_reduction: int = field(XmpInt())
        """integer, max ppm value of speed reduction"""
        min_interframe_gap: int = field(XmpInt())
        """integer, min bytes between frames"""
        max_interframe_gap: int = field(XmpInt())
        """integer, max explicit bytes between frames"""
        max_preamble: int = field(XmpInt())
        """integer, max preamble bytes included in frame"""
        max_streams_per_port: int = field(XmpInt())
        """integer, max streams per port"""
        max_percent: int = field(XmpInt())
        """integer, max input rate in percent"""
        max_pps: int = field(XmpInt(signed=False))
        """integer,  max input rate in pps"""
        max_mbps: int = field(XmpInt())
        """integer, max input rate in mbps"""
        max_seed: int = field(XmpInt())
        """integer, max random seed"""
        max_tx_packet_limit: int = field(XmpInt())
        """integer, max stop-after-n-packet limitation"""
        max_burst_size: int = field(XmpInt())
        """integer, max packets per burst"""
        min_packet_length: int = field(XmpInt())
        """integer, min bytes in total packet"""
        max_packet_length: int = field(XmpInt())
        """integer, max bytes in total packet"""
        max_header_length: int = field(XmpInt())
        """integer, max bytes in auto-generated packet header"""
        max_protocol_segments: int = field(XmpInt())
        """integer, max number of protocol segments"""
        max_pattern_length: int = field(XmpInt())
        """integer, max bytes in repeating payload pattern"""
        max_modifiers: int = field(XmpInt())
        """integer, max 16-bit modifiers per stream"""
        max_modifier_bytes: int = field(XmpInt())
        """integer, max bytes in modified field"""
        max_repeat: int = field(XmpInt())
        """integer, max packet repeats for modifier"""
        max_tpid: int = field(XmpInt())
        """integer, max test payload id"""
        max_manual_packets: int = field(XmpInt())
        """integer, max manual packets"""
        max_match_terms: int = field(XmpInt())
        """integer, max filter match terms per port"""
        max_length_terms: int = field(XmpInt())
        """integer, max filter length terms per port"""
        max_ors: int = field(XmpInt())
        """integer, max or-terms per filter"""
        max_nots: int = field(XmpInt())
        """integer, max or-terms with nots per filter"""
        max_filters: int = field(XmpInt())
        """integer, max filters per port"""
        max_captured_packets: int = field(XmpInt())
        """integer, max captured packets at one time"""
        max_tpld_stats: int = field(XmpInt())
        """integer, max number of different tplds for rx statistics"""
        max_histogram: int = field(XmpInt())
        """integer, max number of sampled histograms"""
        max_32bit_modifiers: int = field(XmpInt())
        """integer, max 32-bit modifiers per stream"""
        can_set_autoneg: int = field(XmpInt())
        """integer, whether supports auto negotiation"""
        can_tcp_checksum: int = field(XmpInt())
        """integer, whether supports TCP with valid checksum"""
        can_udp_checksum: int = field(XmpInt())
        """integer, whether supports UDP with valid checksum"""
        can_eee: int = field(XmpInt())
        """integer, whether supports EEE"""
        can_hw_reg_access: int = field(XmpInt())
        """integer, whether supports hardware register access"""
        can_tcvr_mii_reg_access: int = field(XmpInt())
        """integer, whether supports transceiver MII access"""
        can_adv_phy_man: int = field(XmpInt())
        """integer, whether supports advanced PHY management"""
        can_micro_tpld: int = field(XmpInt())
        """integer, whether supports micro TPLD"""
        can_mdi_mdix: int = field(XmpInt())
        """integer, whether supports MDI/MDIX"""
        can_payload_mode: int = field(XmpInt())
        """integer, whether supports payload mode"""
        can_custom_data_fields: int = field(XmpInt())
        """integer, whether supports custom data fields"""
        can_ext_payload: int = field(XmpInt())
        """integer, whether supports extended payload"""
        can_dyn_traffic_change: int = field(XmpInt())
        """integer, whether supports dynamic traffic change"""
        can_sync_traffic_start: int = field(XmpInt())
        """integer, whether supports synchronized traffic start"""
        can_pfc: int = field(XmpInt())
        """integer, whether supports Priority Flow Control"""
        can_pcs_pma_config: int = field(XmpInt())
        """integer, whether this port can provide PCS/PMA configuration and status"""
        can_fec: int = field(XmpInt(signed=False))
        """bit map encoded,
            [0] = KR FEC,
            [1] = KP FEC,
            [2] = FC FEC,
            [31] = Mandatory (If this bit is set, you have to have FEC mode turned on in either of the supported mode, but you cannot turn FEC off.)
        """
        can_fec_stats: int = field(XmpInt())
        """bit map encoded, can this port provide advanced FEC stats of type x? [0] = symbol error distribution"""
        can_tx_eq: int = field(XmpInt())
        """integer, whether supports TX EQ settings"""
        can_rx_retune: int = field(XmpInt())
        """integer, whether supports RX retuning"""
        prbs_types_supported: int = field(XmpInt())
        """bit map encoded, [0] = lane-based, [1] = PHY-based, [2-31] = reserved"""
        prbs_inversions_supported: int = field(XmpInt())
        """bit map encoded, [0] = lane-based supports inv, [1] = PHY-based supports inv, [2-31] = reserved"""
        prbs_polys_supported: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()], length=5))
        """5 integers, bit map for each PRBS type (above).
            [0] = PRBS7,
            [1] = PRBS9,
            [2] = PRBS11,
            [3] = PRBS15,
            [4] = PRBS23,
            [5] = PRBS31,
            [6] = PRBS58,
            [7] = PRBS49,
            [8] = PRBS10,
            [9] = PRBS20,
            [10] = PRBS13
        """
        serdes_count: int = field(XmpInt())
        """integer, number of physical serdes on line-side"""
        lane_count: int = field(XmpInt())
        """integer, number of lanes (virtual)"""
        tx_eq_tap_count: int = field(XmpInt())
        """integer, number of TXEQ taps"""
        tx_eq_tap_max_val: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()], length=10))
        """10 integers, max-value of individual TXEQ taps"""
        tx_eq_tap_min_val: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()], length=10))
        """10 integers, min-value of individual TXEQ taps"""
        max_fec_correctable_symbol_count: int = field(XmpInt())
        """integer, max number of symbols correctable by the current FEC"""
        max_xmit_one_packet_length: int = field(XmpInt())
        """integer, maximum size (in bytes) of packets, which can be sent using xmitone (replay/streaming interface)"""
        tx_runt_packet_min_length: int = field(XmpInt())
        """integer, minimum TX packet size supported by runt block. Zero = not supported"""
        rx_runt_packet_min_length: int = field(XmpInt())
        """integer, minimum RX packet size supported by runt block. Zero = not supported"""
        can_manipulate_preamble: int = field(XmpInt())
        """integer, whether this port can manipulate the preamble"""
        can_set_link_train: int = field(XmpInt())
        """integer, whether this port can set link training"""
        can_link_flap: int = field(XmpInt())
        """integer, whether this port supports link flap"""
        can_auto_neg_base_r: int = field(XmpInt())
        """integer, whether the port currently can perform BASE-R auto-negotiation (as opposed to RJ45 BASE-T)"""
        can_pma_error_pulse: int = field(XmpInt())
        """integer, whether this port supports 'PMA pulse error injection'"""
        is_chimera: int = field(XmpInt())
        """integer, whether this is a Chimera port"""
        has_p2p_loop_partner: int = field(XmpInt())
        """integer, whether this port currently has a port-to-port loop partner"""
        p2p_loop_partner: int = field(XmpInt())
        """integer, The port-to-port loop partner for the port. N/A = -1."""
        traffic_engine: TrafficEngine = field(XmpInt(), min_version=456)
        """integer, Enabled traffic engine on port. 0x01 = TGA, 0x02 = uTGA."""
        reconc_sublayer: ReconciliationSublayerSupport = field(XmpInt(), min_version=456)
        """integer, Reconciliation Sublayer support, bitmask, 0 = fault signalling not support; 1 = fault signalling supported (XMP: P_FAULTSTATUS/P_FAULTSIGNALING)"""
        max_match_term_pos: int = field(XmpInt(), min_version=457)
        """integer, max match term position in bytes"""
        stream_misc: int = field(XmpInt(), min_version=457)
        """integer, bit pattern, what streams on this port can do. [0]: Whether the port supports streams with DEC8/INC16/DEC16 payload. [1]: Whether the port supports INCPLDFROM0 stream option (refer to the PS_OPTIONS command)."""
        rxeq_cap_ctle_low_min: int = field(XmpInt(), min_version=457) 
        """min value of CTLE LOW."""
        rxeq_cap_ctle_high_min: int = field(XmpInt(), min_version=457)
        """min value of CTLE HIGH."""
        rxeq_cap_agc_min: int = field(XmpInt(), min_version=457)
        """min value of Automatic Gain Control."""
        rxeq_cap_oc_min: int = field(XmpInt(), min_version=457)
        """min value of Offset Cancellation."""
        rxeq_cap_cdr_min: int = field(XmpInt(), min_version=457)
        """min value of CDR, always 0."""
        rxeq_cap_ffe_pre1_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 1."""
        rxeq_cap_ffe_pre2_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 2."""
        rxeq_cap_ffe_pre3_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 3."""
        rxeq_cap_ffe_pre4_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 4."""
        rxeq_cap_ffe_pre5_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 5."""
        rxeq_cap_ffe_pre6_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 6."""
        rxeq_cap_ffe_pre7_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 7."""
        rxeq_cap_ffe_pre8_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Pre 8."""
        rxeq_cap_dfe_min: int = field(XmpInt(), min_version=457)
        """min value of DFE, always 0."""
        rxeq_cap_ffe_post1_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 1."""
        rxeq_cap_ffe_post2_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 2."""
        rxeq_cap_ffe_post3_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 3."""
        rxeq_cap_ffe_post4_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 4."""
        rxeq_cap_ffe_post5_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 5."""
        rxeq_cap_ffe_post6_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 6."""
        rxeq_cap_ffe_post7_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 7."""
        rxeq_cap_ffe_post8_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 8."""
        rxeq_cap_ffe_post9_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 9."""
        rxeq_cap_ffe_post10_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 10."""
        rxeq_cap_ffe_post11_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 11."""
        rxeq_cap_ffe_post12_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 12."""
        rxeq_cap_ffe_post13_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 13."""
        rxeq_cap_ffe_post14_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 14."""
        rxeq_cap_ffe_post15_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 15."""
        rxeq_cap_ffe_post16_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 16."""
        rxeq_cap_ffe_post17_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 17."""
        rxeq_cap_ffe_post18_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 18."""
        rxeq_cap_ffe_post19_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 19."""
        rxeq_cap_ffe_post20_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 20."""
        rxeq_cap_ffe_post21_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 21."""
        rxeq_cap_ffe_post22_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 22."""
        rxeq_cap_ffe_post23_min: int = field(XmpInt(), min_version=457)
        """min value of FFE Post 23."""
        reserved_min_1: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_min_2: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_min_3: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_min_4: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_min_5: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_min_6: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_min_7: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_min_8: int = field(XmpInt(), min_version=457)
        """Reserved."""
        rxeq_cap_ctle_low_max: int = field(XmpInt(), min_version=457)
        """max value of CTLE LOW."""
        rxeq_cap_ctle_high_max: int = field(XmpInt(), min_version=457)
        """max value of CTLE HIGH."""
        rxeq_cap_agc_max: int = field(XmpInt(), min_version=457)
        """max value of Automatic Gain Control."""
        rxeq_cap_oc_max: int = field(XmpInt(), min_version=457)
        """max value of Offset Cancellation."""
        rxeq_cap_cdr_max: int = field(XmpInt(), min_version=457)
        """max value of CDR, always 0."""
        rxeq_cap_ffe_pre1_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 1."""
        rxeq_cap_ffe_pre2_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 2."""
        rxeq_cap_ffe_pre3_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 3."""
        rxeq_cap_ffe_pre4_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 4."""
        rxeq_cap_ffe_pre5_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 5."""
        rxeq_cap_ffe_pre6_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 6."""
        rxeq_cap_ffe_pre7_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 7."""
        rxeq_cap_ffe_pre8_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Pre 8."""
        rxeq_cap_dfe_max: int = field(XmpInt(), min_version=457)
        """max value of DFE, always 0."""
        rxeq_cap_ffe_post1_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 1."""
        rxeq_cap_ffe_post2_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 2."""
        rxeq_cap_ffe_post3_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 3."""
        rxeq_cap_ffe_post4_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 4."""
        rxeq_cap_ffe_post5_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 5."""
        rxeq_cap_ffe_post6_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 6."""
        rxeq_cap_ffe_post7_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 7."""
        rxeq_cap_ffe_post8_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 8."""
        rxeq_cap_ffe_post9_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 9."""
        rxeq_cap_ffe_post10_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 10."""
        rxeq_cap_ffe_post11_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 11."""
        rxeq_cap_ffe_post12_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 12."""
        rxeq_cap_ffe_post13_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 13."""
        rxeq_cap_ffe_post14_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 14."""
        rxeq_cap_ffe_post15_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 15."""
        rxeq_cap_ffe_post16_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 16."""
        rxeq_cap_ffe_post17_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 17."""
        rxeq_cap_ffe_post18_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 18."""
        rxeq_cap_ffe_post19_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 19."""
        rxeq_cap_ffe_post20_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 20."""
        rxeq_cap_ffe_post21_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 21."""
        rxeq_cap_ffe_post22_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 22."""
        rxeq_cap_ffe_post23_max: int = field(XmpInt(), min_version=457)
        """max value of FFE Post 23."""
        reserved_max_1: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_max_2: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_max_3: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_max_4: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_max_5: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_max_6: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_max_7: int = field(XmpInt(), min_version=457)
        """Reserved."""
        reserved_max_8: int = field(XmpInt(), min_version=457)
        """Reserved."""
        length_histogram_step_min: int = field(XmpInt(), min_version=457)
        """minimum step size for length histograms."""
        length_histogram_step_max: int = field(XmpInt(), min_version=457)
        """maximum step size for length histograms."""
        latency_histogram_step_min: int = field(XmpInt(), min_version=457)
        """minimum step size for latency histograms."""
        latency_histogram_step_max: int = field(XmpInt(), min_version=457)
        """maximum step size for latency histograms."""
        min_i2c_frequency: int = field(XmpInt(), min_version=463)
        """minimum I2C frequency"""
        max_i2c_frequency: int = field(XmpInt(), min_version=463)
        """maximum I2C frequency"""
        can_eyescan: int = field(XmpInt(), min_version=463)
        """Bit 0 ==1 => Sampled Eye Scan supported."""
        layer1_misc: int = field(XmpInt(), min_version=465)
        """
        * Bit 0: Can IEEE variant
        * Bit 1: Can ETC (Ethernet Consortium) PCS variant
        * Bit 2: Can monitor PCS RX Lane Map
        * Bit 3: Can control PCS TX Lane Map
        * Bit 4: Can monitor PCS RX Lane Skew
        * Bit 5: Can control PCS TX Lane Skew
        * Bit 6: Can FEC error injection
        """
        # fec_engines: int = field(XmpInt(), min_version=465)
        # """The number of FEC engines available"""
        can_macsec: int = field(XmpInt(), min_version=470)
        """If the port supports MACsec"""
        editable_mixlength_indices: int = field(XmpInt(), min_version=470)
        """
        * Bit 0: Is Mix length index 0 editable
        * Bit 1: Is Mix length index 1 editable
        * Bit 2: Is Mix length index 2 editable
        * Bit 3: Is Mix length index 3 editable
        * Bit 4: Is Mix length index 4 editable
        * Bit 5: Is Mix length index 5 editable
        * Bit 6: Is Mix length index 6 editable
        * Bit 7: Is Mix length index 7 editable
        * Bit 8: Is Mix length index 8 editable
        * Bit 9: Is Mix length index 9 editable
        * Bit 10: Is Mix length index 10 editable
        * Bit 11: Is Mix length index 11 editable
        * Bit 12: Is Mix length index 12 editable
        * Bit 13: Is Mix length index 13 editable
        * Bit 14: Is Mix length index 14 editable
        * Bit 15: Is Mix length index 15 editable
        """
        can_modifier_le: int = field(XmpInt(), min_version=470)
        """
        * Bit 0: Normal modifier (16/24-bit) supports little-endian
        * Bit 1: Extended modifier (32-bit) supports little-endian
        """
        


    def get(self) -> Token[GetDataAttr]:
        """Get the internal limits, aka. capabilities, of the port.

        :return: the internal limits, aka. capabilities, of the port.
        :rtype: P_CAPABILITIES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

@register_command
@dataclass
class P_CAPABILITIES_EXT:
    """
    Get the Port Capabilities in JSON Format. The same as P_CAPABILITIES but in JSON.
    """

    code: typing.ClassVar[int] = 423
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    class GetDataAttr(ResponseBodyStruct):
        data: str = field(XmpStr())
        """string, containing the port capabilities in JSON format"""

    def get(self) -> Token[GetDataAttr]:
        """Get the port capabilities in JSON Format

        :return: The Port capabilities in JSON String
        :rtype: P_CAPABILITIES_EXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_INTERFACE:
    """
    Obtains the name of the physical interface type of a port.
    """

    code: typing.ClassVar[int] = 107
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        interface: str = field(XmpStr())
        """string, describing the interface type."""

    def get(self) -> Token[GetDataAttr]:
        """Get the name of the physical interface type of a port.

        :return: the name of the physical interface type of a port.
        :rtype: P_INTERFACE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_SPEEDSELECTION:
    """
    The speed mode of an autoneg port with an interface type supporting multiple speeds.

    .. note::

        This is only a settable command when speed is selected at the port level. Use the M_CFPCONFIGEXT command when speed is selected at the module level.

    """

    code: typing.ClassVar[int] = 109
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: PortSpeedMode = field(XmpByte())
        """coded byte, containing the speed mode for the port."""

    class SetDataAttr(RequestBodyStruct):
        mode: PortSpeedMode = field(XmpByte())
        """coded byte, containing the speed mode for the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the speed mode of the port with an interface type supporting multiple speeds.

        :return: the speed mode of the port with an interface type supporting multiple speeds.
        :rtype: P_SPEEDSELECTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: PortSpeedMode) -> Token[None]:
        """Set the speed mode of the port with an interface type supporting multiple speeds.

        :param mode: the speed mode of the port with an interface type supporting multiple speeds
        :type mode: PortSpeedMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_auto = functools.partialmethod(set, PortSpeedMode.AUTO)
    """Set the speed mode to auto (all speeds used in auto negotiation).
    """

    set_f10m = functools.partialmethod(set, PortSpeedMode.F10M)
    """Set the speed mode to 10 Mbit/s.
    """

    set_f100m = functools.partialmethod(set, PortSpeedMode.F100M)
    """Set the speed mode to 100 Mbit/s.
    """

    set_f1g = functools.partialmethod(set, PortSpeedMode.F1G)
    """Set the speed mode to 1 Gbit/s.
    """

    set_f10g = functools.partialmethod(set, PortSpeedMode.F10G)
    """Set the speed mode to 10 Gbit/s.
    """

    set_f40g = functools.partialmethod(set, PortSpeedMode.F40G)
    """Set the speed mode to 40 Gbit/s.
    """

    set_f100g = functools.partialmethod(set, PortSpeedMode.F100G)
    """Set the speed mode to 100 Gbit/s.
    """

    set_f10mhdx = functools.partialmethod(set, PortSpeedMode.F10MHDX)
    """Set the speed mode to 10 Mbit/s Half Duplex.
    """

    set_f100mhdx = functools.partialmethod(set, PortSpeedMode.F100MHDX)
    """Set the speed mode to 100 Mbit/s Half Duplex.
    """

    set_f10m100m = functools.partialmethod(set, PortSpeedMode.F10M100M)
    """Set the speed mode to 10/100 Mbit/s.
    """

    set_f100m1g = functools.partialmethod(set, PortSpeedMode.F100M1G)
    """Set the speed mode to 100 Mbit/s / 1 Gbit/s.
    """

    set_f100m1g10g = functools.partialmethod(set, PortSpeedMode.F100M1G10G)
    """Set the speed mode to 100 Mbit/s / 1 Gbit/s / 10 Gbit/s.
    """

    set_f2500m = functools.partialmethod(set, PortSpeedMode.F2500M)
    """Set the speed mode to 2500 Mbit/s.
    """

    set_f5g = functools.partialmethod(set, PortSpeedMode.F5G)
    """Set the speed mode to 5 Gbit/s.
    """

    set_f100m1g2500m = functools.partialmethod(set, PortSpeedMode.F100M1G2500M)
    """Set the speed mode to 100 Mbit/s / 1 Gbit/s / 2500 Mbit/s.
    """

    set_unknown = functools.partialmethod(set, PortSpeedMode.UNKNOWN)
    """Set the speed mode to unknown.
    """


@register_command
@dataclass
class P_SPEED:
    """
    Obtains the current physical speed of a port's interface.
    """

    code: typing.ClassVar[int] = 110
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        port_speed: int = field(XmpInt())
        """integer, current speed in units of Mbps."""

    def get(self) -> Token[GetDataAttr]:
        """Get the current physical speed of the port's interface.

        :return: the current physical speed of the port's interface.
        :rtype: P_SPEED.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_RECEIVESYNC:
    """
    Obtains the current in-sync status of a port's receive interface.
    """

    code: typing.ClassVar[int] = 111
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        sync_status: SyncStatus = field(XmpByte())
        """coded byte, describing the current sync status of the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the current in-sync status for a port's receive interface.

        :return: the current in-sync status for a port's receive interface.
        :rtype: P_RECEIVESYNC.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_COMMENT:
    """
    The description of a port.
    """

    code: typing.ClassVar[int] = 112
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        comment: str = field(XmpStr())
        """string, containing the description of the port."""

    class SetDataAttr(RequestBodyStruct):
        comment: str = field(XmpStr())
        """string, containing the description of the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the description of the port.

        :return: the description of the port
        :rtype: P_COMMENT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, comment: str) -> Token[None]:
        """Set the description of the port.

        :param comment: the description of the port
        :type comment: str
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, comment=comment))


@register_command
@dataclass
class P_SPEEDREDUCTION:
    """
    A speed reduction applied to the transmitting side of a port, resulting in an effective traffic rate that is slightly lower than the rate of the physical interface. Speed reduction is effectuated by inserting short idle periods in the generated traffic pattern to consume part of the port's physical bandwidth. The port's clock speed is not altered.
    """

    code: typing.ClassVar[int] = 113
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ppm: int = field(XmpInt())
        """integer, specifying the speed reduction in units of parts-per-million."""

    class SetDataAttr(RequestBodyStruct):
        ppm: int = field(XmpInt())
        """integer, specifying the speed reduction in units of parts-per-million."""

    def get(self) -> Token[GetDataAttr]:
        """Get the speed reduction ppm value of the test port.

        :return: the speed reduction ppm value of the test port.
        :rtype: P_SPEEDREDUCTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, ppm: int) -> Token[None]:
        """Set the speed reduction ppm value of the test port.

        :param ppm: the speed reduction ppm value of the test port
        :type ppm: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, ppm=ppm))


@register_command
@dataclass
class P_INTERFRAMEGAP:
    """
    The minimum gap between packets in the traffic generated for a port. The gap includes the Ethernet preamble.
    """

    code: typing.ClassVar[int] = 114
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        min_byte_count: int = field(XmpInt())
        """integer, specifying the minimum number of byte-times between generated packets."""

    class SetDataAttr(RequestBodyStruct):
        min_byte_count: int = field(XmpInt())
        """integer, specifying the minimum number of byte-times between generated packets."""

    def get(self) -> Token[GetDataAttr]:
        """Get the minimum gap between packets in the traffic generated for a port. The gap includes the Ethernet preamble.

        :return: the minimum gap between packets in the traffic generated for a port. The gap includes the Ethernet preamble.
        :rtype: P_INTERFRAMEGAP.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, min_byte_count: int) -> Token[None]:
        """Set the minimum gap between packets in the traffic generated for a port. The gap includes the Ethernet preamble.

        :param min_byte_count: the minimum gap between packets in the traffic generated for a port. The gap includes the Ethernet preamble.
        :type min_byte_count: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, min_byte_count=min_byte_count))


@register_command
@dataclass
class P_MACADDRESS:
    """
    A 48-bit Ethernet MAC address specified for a port. This address is used as the
    default source MAC field in the header of generated traffic for the port, and is
    also used for support of the ARP protocol.
    """

    code: typing.ClassVar[int] = 116
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mac_address: Hex = field(XmpMacAddress())
        """six hex bytes, specifying the six bytes of the MAC address."""

    class SetDataAttr(RequestBodyStruct):
        mac_address: Hex = field(XmpMacAddress())
        """six hex bytes, specifying the six bytes of the MAC address."""

    def get(self) -> Token[GetDataAttr]:
        """Get the MAC address of the port.

        :return: the MAC address of the port.
        :rtype: P_MACADDRESS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mac_address: Hex) -> Token[None]:
        """Set the MAC address of the port.

        :param mac_address: the MAC address of the port
        :type mac_address: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mac_address=mac_address))


@register_command
@dataclass
class P_IPADDRESS:
    """
    An IPv4 network configuration specified for a port. The address is used as the
    default source address field in the IP header of generated traffic, and the
    configuration is also used for support of the ARP and PING protocols.
    """

    code: typing.ClassVar[int] = 117
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ipv4_address: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, the IP address of the port."""
        subnet_mask: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, the subnet mask of the local network segment for the port."""
        gateway: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, the gateway of the local network segment for the port."""
        wild: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, wildcards used for ARP and PING replies, and each byte must be 255 (0xFF) or 0 (0x00)."""

    class SetDataAttr(RequestBodyStruct):
        ipv4_address: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, the IP address of the port."""
        subnet_mask: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, the subnet mask of the local network segment for the port."""
        gateway: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, the gateway of the local network segment for the port."""
        wild: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, wildcards used for ARP and PING replies, must be 255 or 0."""

    def get(self) -> Token[GetDataAttr]:
        """Get the IPv4 address, subnet mask, gateway address and wildcard used for ARP and PING replies of the port.

        :return: the IPv4 address, subnet mask, gateway address and wildcard used for ARP and PING replies of the port
        :rtype: P_IPADDRESS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, ipv4_address: ipaddress.IPv4Address, subnet_mask: ipaddress.IPv4Address, gateway: ipaddress.IPv4Address, wild: ipaddress.IPv4Address) -> Token[None]:
        """Set the IPv4 address, subnet mask, gateway address and wildcard used for ARP and PING replies of the port.

        :param ipv4_address: the IPv4 address of the port
        :type ipv4_address: Union[str, int, ipaddress.IPv4Address]
        :param subnet_mask: the subnet mask of the local network segment for the port
        :type subnet_mask: Union[str, int, ipaddress.IPv4Address]
        :param gateway: the gateway of the local network segment for the port
        :type gateway: Union[str, int, ipaddress.IPv4Address]
        :param wild: wildcards used for ARP and PING replies, and each byte must be 255 (0xFF) or 0 (0x00)
        :type wild: Union[str, int, ipaddress.IPv4Address]
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, ipv4_address=ipv4_address, subnet_mask=subnet_mask, gateway=gateway, wild=wild)
        )


@register_command
@dataclass
class P_ARPREPLY:
    """
    Whether the port replies to ARP requests. The
    port can reply to incoming ARP requests by mapping the IP address specified for
    the port to the MAC address specified for the port. ARP/NDP reply generation is
    independent of whether traffic and capture is on for the port.
    """

    code: typing.ClassVar[int] = 118
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to ARP requests."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to ARP requests."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of whether the port replies to ARP requests.

        :return: the status of whether the port replies to ARP requests
        :rtype: P_ARPREPLY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the status of whether the port replies to ARP requests.

        :param on_off: whether the port replies to ARP requests
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the port from replying to incoming ARP requests.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the port to reply to incoming ARP requests.
    """


@register_command
@dataclass
class P_PINGREPLY:
    """
    Whether the port replies to IPv4/IPv6 PING. The port can
    reply to incoming IPv4/IPv6 PING requests to the IP address specified for the port. IPv4/IPv6 PING
    reply generation is independent of whether traffic and capture is on for the
    port.
    """

    code: typing.ClassVar[int] = 119
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to PING requests."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to PING requests."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of whether the port replies to IPv4/IPv6 PING requests.

        :return: the status of whether the port replies to IPv4/IPv6 PING requests
        :rtype: P_PINGREPLY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the status of whether the port replies to IPv4/IPv6 PING requests.

        :param on_off: whether the port replies to IPv4/IPv6 PING requests
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Enable IPv4/IPv6 PING reply on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable IPv4/IPv6 PING reply on the port.
    """


@register_command
@dataclass
class P_PAUSE:
    """
    Whether a port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.
    """

    code: typing.ClassVar[int] = 120
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether PAUSE response is enabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether PAUSE response is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of whether the port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.

        :return: the status of whether the port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.
        :rtype: P_PAUSE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the status of whether the port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.

        :param on_off: the status of whether the port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the port to respond to incoming Ethernet PAUSE frames.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the port to respond to incoming Ethernet PAUSE frames.
    """


@register_command
@dataclass
class P_RANDOMSEED:
    """
    A fixed seed value specified for a port. This value is used for a pseudo-random number generator used when generating traffic that requires random variation in packet length, payload, or modified fields. As long as no part of the port configuration is changed, the generated traffic patterns are reproducible when restarting traffic for the port. A specified seed value of -1 instead creates variation by using a new time-based seed value each time traffic generation is restarted.
    """

    code: typing.ClassVar[int] = 121
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        seed: int = field(XmpInt())
        """integer, specifying a fixed seed value for the pseudo-random number generator. -1 = new random sequence for each start."""

    class SetDataAttr(RequestBodyStruct):
        seed: int = field(XmpInt())
        """integer, specifying a fixed seed value for the pseudo-random number generator. -1 = new random sequence for each start."""

    def get(self) -> Token[GetDataAttr]:
        """Get the seed value specified for the port.

        :return: the seed value specified for the port.
        :rtype: P_RANDOMSEED.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, seed: int) -> Token[None]:
        """Set the seed value for the port.

        :param seed: the seed value for the port
        :type seed: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, seed=seed))


@register_command
@dataclass
class P_LOOPBACK:
    """
    The loopback mode for a port. Ports can be configured to perform two different kinds of loopback: 1) External RX-to-TX loopback, where the received packets are re-transmitted immediately. The packets are still processed by the receive logic, and can be captured and analyzed. 2) Internal TX-to-RX loopback, where the transmitted packets are received directly by the port itself. This is mainly useful for testing the generated traffic patterns before actual use.

    """

    code: typing.ClassVar[int] = 122
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: LoopbackMode = field(XmpByte())
        """coded byte, specifying the loopback mode of the port."""

    class SetDataAttr(RequestBodyStruct):
        mode: LoopbackMode = field(XmpByte())
        """coded byte, specifying the loopback mode of the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the loop back mode of the port.

        :return: the loop back mode of the port.
        :rtype: P_LOOPBACK.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: LoopbackMode) -> Token[None]:
        """Set the loop back mode of the port.

        :param mode: the loop back mode of the port
        :type mode: LoopbackMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_none = functools.partialmethod(set, LoopbackMode.NONE)
    """Set the port loop back mode to non-looped.
    """

    set_l1rx2tx = functools.partialmethod(set, LoopbackMode.L1RX2TX)
    """Set the port loop back mode to L1RX2TX, transmit byte-by-byte copy of the incoming packet.
    """

    set_l2rx2tx = functools.partialmethod(set, LoopbackMode.L2RX2TX)
    """Set the port loop back mode to L2RX2TX, swap source and destination MAC addresses.
    """

    set_l3rx2tx = functools.partialmethod(set, LoopbackMode.L3RX2TX)
    """Set the port loop back mode to L3RX2TX, swap source and destination MAC addresses and swap source and destination IP addresses.
    """

    set_txon2rx = functools.partialmethod(set, LoopbackMode.TXON2RX)
    """Set the port loop back mode to TXON2RX, packet is also transmitted from the port.
    """

    set_txoff2rx = functools.partialmethod(set, LoopbackMode.TXOFF2RX)
    """Set the port loop back mode to TXOFF2RX, port transmitter is off.
    """

    set_port2port = functools.partialmethod(set, LoopbackMode.PORT2PORT)
    """Set the port loop back mode to PORT2PORT, packets received on one port is sent out again on the neighbor port for inline monitoring.
    """


@register_command
@dataclass
class P_FLASH:
    """
    Make the test port LED for a particular port flash on and off with a 1-second
    interval. This is helpful when you need to identify a specific port within a
    chassis.
    """

    code: typing.ClassVar[int] = 123
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the test port LED is blinking."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the test port LED is blinking."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of the LED flashing status of the port.

        :return: the status of the LED flashing status of the port.
        :rtype: P_FLASH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the status of the LED flashing status of the port.

        :param on_off: the status of the LED flashing status of the port.
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable port LED from flashing.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable port LED to flash.
    """


@register_command
@dataclass
class P_TRAFFIC:
    """
    Whether a port is transmitting packets. When on, the port generates a sequence
    of packets with contributions from each stream that is enabled. The streams are configured using the PS_xxx parameters.

    .. note::

        If any of the specified packet sizes cannot fit into the packet generator, this command will return FAILED and not start the traffic.
        While traffic is on the streams for this port cannot be enabled or disabled, and the configuration of those streams that are enabled cannot be changed.

    """

    code: typing.ClassVar[int] = 124
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: TrafficOnOff = field(XmpByte())
        """coded byte, determines whether to start or stop traffic generation on this port."""

    class SetDataAttr(RequestBodyStruct):
        on_off: StartOrStop = field(XmpByte())
        """coded byte, determines whether to start or stop traffic generation on this port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the traffic generation status of the port.

        :return: the traffic generation status of the port
        :rtype: P_TRAFFIC.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: StartOrStop) -> Token[None]:
        """Set the traffic generation status of the port.

        :param on_off: the traffic generation status of the port.
        :type on_off: StartOrStop
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_stop = functools.partialmethod(set, StartOrStop.STOP)
    """Stop the traffic generation of the port.
    """

    set_start = functools.partialmethod(set, StartOrStop.START)
    """Start the traffic generation of the port.
    """


@register_command
@dataclass
class P_CAPTURE:
    """
    Whether a port is capturing packets. When on, the port retains the received
    packets and makes them available for inspection. The capture criteria are
    configured using the PC_xxx parameters. While capture is on the capture
    parameters cannot be changed.
    """

    code: typing.ClassVar[int] = 125
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether capture is active for this port."""

    class SetDataAttr(RequestBodyStruct):
        on_off: StartOrStop = field(XmpByte())
        """coded byte, whether capture is active for this port."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the port is capturing packets.

        :return: whether the port is capturing packets.
        :rtype: P_CAPTURE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: StartOrStop) -> Token[None]:
        """Set whether the port is capturing packets.

        :param on_off: whether the port is capturing packets.
        :type on_off: StartOrStop
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_stop = functools.partialmethod(set, StartOrStop.STOP)
    """Stop packet capturing on the port.
    """

    set_start = functools.partialmethod(set, StartOrStop.START)
    """Start packet capturing on the port.
    """


@register_command
@dataclass
class P_XMITONE:
    """
    Transmits a single packet from a port, independent of the stream definitions,
    and independent of whether traffic is on. A valid Frame Check Sum is written
    into the final four bytes.
    """

    code: typing.ClassVar[int] = 126
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, the data content of the packet to be transmitted."""

    def set(self, hex_data: Hex) -> Token[None]:
        """Transmits a single packet from a port, independent of the stream definitions, and independent of whether traffic is on.
        A valid Frame Check Sum is written into the final four bytes.

        :param hex_data: raw bytes of the packet in hex to transmit
        :rtype: typing.List[str]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, hex_data=hex_data))


@register_command
@dataclass
class P_LATENCYOFFSET:
    """
    An offset applied to the latency measurements performed for received traffic
    containing test payloads. This value affects the minimum, average, and maximum
    latency values obtained through the PR_TPLDLATENCY command.
    """

    code: typing.ClassVar[int] = 127
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        offset: int = field(XmpInt())
        """integer, specifying the offset for the latency measurements."""

    class SetDataAttr(RequestBodyStruct):
        offset: int = field(XmpInt())
        """integer, specifying the offset for the latency measurements."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port latency offset value in nanoseconds.

        :return: the port latency offset value in nanoseconds
        :rtype: P_LATENCYOFFSET.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, offset: int) -> Token[None]:
        """Set the port latency offset value in nanoseconds.

        :param offset: the port latency offset value in nanoseconds
        :type offset: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, offset=offset))


@register_command
@dataclass
class P_LATENCYMODE:
    """
    Latency is measured by inserting a time-stamp in each packet when it is
    transmitted, and relating it to the time when the packet is received. There are
    four separate modes for calculating the latency:

        1)  Last-bit-out to last-bit-in, which measures basic bit-transit time,
            independent of packet length.
        2)  First-bit-out to last-bit-in, which adds the time taken to transmit the
            packet itself.
        3)  Last-bit-out to first-bit-in, which subtracts the time taken to transmit the
            packet itself. The same latency mode must be configured for the transmitting
            port and the receiving port; otherwise invalid measurements will occur.
        4)  First-bit-out to first-bit-in, which adds the time taken to transmit the
            packet itself, and subtracts the time taken to transmit the packet itself.
            The same latency mode must be configured for the transmitting
            port and the receiving port; otherwise invalid measurements will occur.

    """

    code: typing.ClassVar[int] = 128
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: LatencyMode = field(XmpByte())
        """coded byte, which calculation mode to use."""

    class SetDataAttr(RequestBodyStruct):
        mode: LatencyMode = field(XmpByte())
        """coded byte, which calculation mode to use."""

    def get(self) -> Token[GetDataAttr]:
        """Get the latency measurement mode of the port.

        :return: the latency measurement mode of the port
        :rtype: P_LATENCYMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: LatencyMode) -> Token[None]:
        """Set the latency measurement mode of the port.

        :param mode: the latency measurement mode of the port
        :type mode: LatencyMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_last2last = functools.partialmethod(set, LatencyMode.LAST2LAST)
    """Set the port latency mode to LAST2LAST (Last-bit-out to last-bit-in, which measures basic bit-transit time, independent of packet length).
    """

    set_first2last = functools.partialmethod(set, LatencyMode.FIRST2LAST)
    """Set the port latency mode to FIRST2LAST (First-bit-out to last-bit-in, which adds the time taken to transmit the packet itself).
    """

    set_last2first = functools.partialmethod(set, LatencyMode.LAST2FIRST)
    """Set the port latency mode to LAST2FIRST (Last-bit-out to first-bit-in, which subtracts the time taken to transmit the packet itself.
    The same latency mode must be configured for the transmitting port and the receiving port; otherwise invalid measurements will occur).
    """

    set_first2first = functools.partialmethod(set, LatencyMode.FIRST2FIRST)
    """Set the port latency mode to FIRST2FIRST
    (First-bit-out to first-bit-in, which adds the time taken to transmit the packet itself, and subtracts the time taken to transmit the packet itself.
    The same latency mode must be configured for the transmitting port and the receiving port; otherwise invalid measurements will occur).
    """


@register_command
@dataclass
class P_AUTOTRAIN:
    """
    The interval between sending out training packets, allowing a switch to learn
    the port's MAC address. Layer-2 switches configure themselves automatically by
    detecting the source MAC addresses of packets received on each port. If a port
    only receives, and does not itself transmit test traffic, then the switch will
    never learn its MAC address. Also, if transmission is very rare the switch will
    age-out the learned MAC address. By setting the auto-train interval you instruct
    the port to send switch training packets, independent of whether the port is
    transmitting test traffic.
    """

    code: typing.ClassVar[int] = 129
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        interval: int = field(XmpInt())
        """integer, specifying the number of seconds between training packets. 0, disable training packets."""

    class SetDataAttr(RequestBodyStruct):
        interval: int = field(XmpInt())
        """integer, specifying the number of seconds between training packets. 0, disable training packets."""

    def get(self) -> Token[GetDataAttr]:
        """Get the interval between sending out training packets of the port in seconds.

        :return: the interval between sending out training packets of the port.
        :rtype: P_AUTOTRAIN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, interval: int) -> Token[None]:
        """Set the interval between sending out training packets of the port in seconds.

        :param interval: the interval between sending out training packets of the port
        :type interval: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, interval=interval))


@register_command
@dataclass
class P_UAT_MODE:
    """
    This command defines if a port is currently used by test suite Valkyrie1564, which
    means that UAT (UnAvailable Time) will be detected for the port.
    """

    code: typing.ClassVar[int] = 138
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: OnOff = field(XmpByte())
        """specifies the state of the affected stream counters"""
        delay: int = field(XmpInt())
        """integer,time in milliseconds to wait before detection of UAT is started. Default value: 500. This parameter is ignored when state is set to OFF."""

    class SetDataAttr(RequestBodyStruct):
        mode: OnOff = field(XmpByte())
        """specifies the state of the affected stream counters"""
        delay: int = field(XmpInt())
        """integer, time in milliseconds to wait before detection of UAT is started. Default value: 500. This parameter is ignored when state is set to OFF."""

    def get(self) -> Token[GetDataAttr]:
        """Get the state of the affected stream counters and time in milliseconds to wait before detection of UAT is started. Default value: 500.
        This command is ignored when state is set to OFF.

        :return: the state of the affected stream counters and time in milliseconds to wait before detection of UAT is started. Default value: 500.
            This command is ignored when state is set to OFF.
        :rtype: P_UAT_MODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: OnOff, delay: int) -> Token[None]:
        """Set the UAT mode of the port.

        :param mode: the state of the affected stream counters
        :type mode: OnOff
        :param delay: time in milliseconds to wait before detection of UAT is started. Default value: 500. This command is ignored when state is set to OFF
        :type delay: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode, delay=delay))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable UAT on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable UAT on the port.
    """


@register_command
@dataclass
class P_UAT_FLR:
    """
    This command defines the threshold for the Frame Loss Ratio, where a second is
    declared as a Severely Errored Second (SES). In Valkyrie1564 UnAvailable Time
    (UAT) is declared after 10 consecutive SES has been detected
    """

    code: typing.ClassVar[int] = 139
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        frame_loss_ratio: int = field(XmpByte())
        """byte, specifies the Frame Loss Ratio threshold for SES as a fraction of 1 * 100 (i.e. if the threshold is 0.50, value is 50)"""

    class SetDataAttr(RequestBodyStruct):
        frame_loss_ratio: int = field(XmpByte())
        """byte, Frame Loss Ratio specified as a number times 1/100, 0..100"""

    def get(self) -> Token[GetDataAttr]:
        """Get the the threshold for the Frame Loss Ratio, where a second is declared as a Severely Errored Second (SES).

        :return: specifies the Frame Loss Ratio threshold for SES as a fraction of 1 * 100 (i.e. if the threshold is 0.50, value is 50)
        :rtype: P_UAT_FLR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, frame_loss_ratio: int) -> Token[None]:
        """Set the the threshold for the Frame Loss Ratio, where a second is declared as a Severely Errored Second (SES).

        :param frame_loss_ratio: Frame Loss Ratio specified as a number times 1/100, 0..100
        :type frame_loss_ratio: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, frame_loss_ratio=frame_loss_ratio))


@register_command
@dataclass
class P_MIXWEIGHTS:
    """
    Allow changing the distribution of the MIX packet length by specifying the
    percentage of each of the 16 possible frame sizes used in the MIX.  The sum of the percentage values specified must be 100. The command will affect the mix-distribution for all streams on the port. The possible 16 frame sizes are: 56 (not valid for 40G/100G), 60, 64, 70, 78, 92, 256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.
    """

    code: typing.ClassVar[int] = 192
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        weight_56_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 56-byte frame sizes."""
        weight_60_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 60-byte frame sizes."""
        weight_64_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 64-byte frame sizes."""
        weight_70_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 70-byte frame sizes."""
        weight_78_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 78-byte frame sizes."""
        weight_92_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 92-byte frame sizes."""
        weight_256_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 256-byte frame sizes."""
        weight_496_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 496-byte frame sizes."""
        weight_512_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 512-byte frame sizes."""
        weight_570_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 570-byte frame sizes."""
        weight_576_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 576-byte frame sizes."""
        weight_594_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 594-byte frame sizes."""
        weight_1438_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 1438-byte frame sizes."""
        weight_1518_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 1518-byte frame sizes."""
        weight_9216_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 9216-byte frame sizes."""
        weight_16360_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 16360-byte frame sizes."""

    class SetDataAttr(RequestBodyStruct):
        weight_56_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 56-byte frame sizes."""
        weight_60_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 60-byte frame sizes."""
        weight_64_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 64-byte frame sizes."""
        weight_70_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 70-byte frame sizes."""
        weight_78_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 78-byte frame sizes."""
        weight_92_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 92-byte frame sizes."""
        weight_256_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 256-byte frame sizes."""
        weight_496_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 496-byte frame sizes."""
        weight_512_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 512-byte frame sizes."""
        weight_570_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 570-byte frame sizes."""
        weight_576_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 576-byte frame sizes."""
        weight_594_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 594-byte frame sizes."""
        weight_1438_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 1438-byte frame sizes."""
        weight_1518_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 1518-byte frame sizes."""
        weight_9216_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 9216-byte frame sizes."""
        weight_16360_bytes: int = field(XmpInt())
        """integer, specifying the percentage of 16360-byte frame sizes."""

    def get(self) -> Token[GetDataAttr]:
        """Get the percentage of each of the
        16 possible frame sizes used in the MIX. The sum of the percentage values specified must
        be 100. The command will affect the mix-distribution for all streams on the port.
        The possible 16 frame sizes are: 56 (not valid for 40G and above), 60, 64, 70, 78, 92,
        256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.

        :return: the percentage of each of the 16 possible frame sizes used in the MIX.
        :rtype: P_MIXWEIGHTS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(
        self,
        weight_56_bytes: int,
        weight_60_bytes: int,
        weight_64_bytes: int,
        weight_70_bytes: int,
        weight_78_bytes: int,
        weight_92_bytes: int,
        weight_256_bytes: int,
        weight_496_bytes: int,
        weight_512_bytes: int,
        weight_570_bytes: int,
        weight_576_bytes: int,
        weight_594_bytes: int,
        weight_1438_bytes: int,
        weight_1518_bytes: int,
        weight_9216_bytes: int,
        weight_16360_bytes: int
    ) -> Token[None]:
        """Set the percentage of each of the
        16 possible frame sizes used in the MIX. The sum of the percentage values specified must
        be 100. The command will affect the mix-distribution for all streams on the port.
        The possible 16 frame sizes are: 56 (not valid for 40G and above), 60, 64, 70, 78, 92,
        256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.

        :param weight_56_bytes: specifying the percentage of 56-byte frame sizes
        :type weight_56_bytes: int
        :param weight_60_bytes: specifying the percentage of 60-byte frame sizes
        :type weight_60_bytes: int
        :param weight_64_bytes: specifying the percentage of 64-byte frame sizes
        :type weight_64_bytes: int
        :param weight_70_bytes: specifying the percentage of 70-byte frame sizes
        :type weight_70_bytes: int
        :param weight_78_bytes: specifying the percentage of 78-byte frame sizes
        :type weight_78_bytes: int
        :param weight_92_bytes: specifying the percentage of 92-byte frame sizes
        :type weight_92_bytes: int
        :param weight_256_bytes: specifying the percentage of 256-byte frame sizes
        :type weight_256_bytes: int
        :param weight_496_bytes: specifying the percentage of 496-byte frame sizes
        :type weight_496_bytes: int
        :param weight_512_bytes: specifying the percentage of 512-byte frame sizes
        :type weight_512_bytes: int
        :param weight_570_bytes: specifying the percentage of 570-byte frame sizes
        :type weight_570_bytes: int
        :param weight_576_bytes: specifying the percentage of 576-byte frame sizes
        :type weight_576_bytes: int
        :param weight_594_bytes: specifying the percentage of 594-byte frame sizes
        :type weight_594_bytes: int
        :param weight_1438_bytes: specifying the percentage of 1438-byte frame sizes
        :type weight_1438_bytes: int
        :param weight_1518_bytes: specifying the percentage of 1518-byte frame sizes
        :type weight_1518_bytes: int
        :param weight_9216_bytes: specifying the percentage of 9216-byte frame sizes
        :type weight_9216_bytes: int
        :param weight_16360_bytes: specifying the percentage of 16360-byte frame sizes
        :type weight_16360_bytes: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                weight_56_bytes=weight_56_bytes,
                weight_60_bytes=weight_60_bytes,
                weight_64_bytes=weight_64_bytes,
                weight_70_bytes=weight_70_bytes,
                weight_78_bytes=weight_78_bytes,
                weight_92_bytes=weight_92_bytes,
                weight_256_bytes=weight_256_bytes,
                weight_496_bytes=weight_496_bytes,
                weight_512_bytes=weight_512_bytes,
                weight_570_bytes=weight_570_bytes,
                weight_576_bytes=weight_576_bytes,
                weight_594_bytes=weight_594_bytes,
                weight_1438_bytes=weight_1438_bytes,
                weight_1518_bytes=weight_1518_bytes,
                weight_9216_bytes=weight_9216_bytes,
                weight_16360_bytes=weight_16360_bytes
            )
        )


@register_command
@dataclass
class P_MDIXMODE:
    """
    Selects the MDI/MDIX behavior of copper interfaces (Currently supported on
    M6SFP and M2SFPT).
    """

    code: typing.ClassVar[int] = 194
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: MDIXMode = field(XmpByte())
        """coded byte, containing the MDI/MDIX mode for the port."""

    class SetDataAttr(RequestBodyStruct):
        mode: MDIXMode = field(XmpByte())
        """coded byte, containing the MDI/MDIX mode for the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the MDI/MDIX mode of the port.

        :return: the MDI/MDIX mode of the port.
        :rtype: P_MDIXMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: MDIXMode) -> Token[None]:
        """Set the MDI/MDIX mode of the port.

        :param mode: the MDI/MDIX mode of the port.
        :type mode: MDIXMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_auto = functools.partialmethod(set, MDIXMode.AUTO)
    """Set the MDI/MDIX mode of the port to Auto.
    """

    set_mdi = functools.partialmethod(set, MDIXMode.MDI)
    """Set the MDI/MDIX mode of the port to MDI.
    """

    set_mdix = functools.partialmethod(set, MDIXMode.MDIX)
    """Set the MDI/MDIX mode of the port to MDIX.
    """


@register_command
@dataclass
class P_TRAFFICERR:
    """
    Obtain the traffic error which has occurred in the last ``*_TRAFFIC`` or ``C_TRAFFICSYNC`` command.

    """

    code: typing.ClassVar[int] = 198
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        error: TrafficError = field(XmpInt())
        """coded byte, specifies the port traffic error."""

    def get(self) -> Token[GetDataAttr]:
        """Get traffic error which has occurred in the last ``*_TRAFFIC`` or ``C_TRAFFICSYNC`` command.

        :return: traffic error which has occurred in the last ``*_TRAFFIC`` or ``C_TRAFFICSYNC`` command
        :rtype: P_TRAFFICERR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_GAPMONITOR:
    """
    The gap-start and gap-stop criteria for the port's gap monitor. The gap monitor
    expects a steady stream of incoming packets, and detects larger-than-allowed
    gaps between them. Once a gap event is encountered it requires a certain number
    of consecutive packets below the threshold to end the event.
    """

    code: typing.ClassVar[int] = 301
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        start: int = field(XmpInt())
        """integer, the maximum allowed gap between packets, in microseconds. (0 to 134.000 microseconds) 0 = disable gap monitor."""
        stop: int = field(XmpInt())
        """integer, the minimum number of good packets required. (0 to 1024 packets) 0 = disable gap monitor."""

    class SetDataAttr(RequestBodyStruct):
        start: int = field(XmpInt())
        """integer, the maximum allowed gap between packets, in microseconds. (0 to 134.000 microseconds) 0 = disable gap monitor."""
        stop: int = field(XmpInt())
        """integer, the minimum number of good packets required. (0 to 1024 packets) 0 = disable gap monitor."""

    def get(self) -> Token[GetDataAttr]:
        """Get the gap-start and gap-stop criteria for the port's gap monitor.

        :return: the gap-start and gap-stop criteria for the port's gap monitor
        :rtype: P_GAPMONITOR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, start: int, stop: int) -> Token[None]:
        """Set the gap-start and gap-stop criteria for the port's gap monitor.
        :param start: the maximum allowed gap between packets, in microseconds. (0 to 134.000 microseconds) 0 = disable gap monitor
        :type start: int
        :param stop: the minimum number of good packets required. (0 to 1024 packets) 0 = disable gap monitor
        :type stop: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, start=start, stop=stop))


@register_command
@dataclass
class P_CHECKSUM:
    """
    Controls an extra payload integrity checksum, which also covers the header
    protocols following the Ethernet header. It will therefore catch any
    modifications to the protocol fields (which should therefore not have modifiers on them).
    """

    code: typing.ClassVar[int] = 302
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        offset: int = field(XmpByte())
        """byte, the offset in the packet where the calculation of the extra checksum is started from. Set to OFF or 0 to disable.
        Valid enable range is [8 .. 127, ON].
        Please observe that ON equals the value 14.
        Please also observe that P_CHECKSUM ? will return OFF if set to 0 (or OFF) and that P_CHECKSUM ? will return ON if set to 14 (or ON).
        """

    class SetDataAttr(RequestBodyStruct):
        offset: int = field(XmpByte())
        """byte, the offset in the packet where the calculation of the extra checksum is started from. Set to OFF or 0 to disable.
        Valid enable range is [8 .. 127].
        Please observe that ON equals the value 14.
        Please also observe that P_CHECKSUM ? will return OFF if set to 0 (or OFF) and that P_CHECKSUM ? will return ON if set to 14 (or ON).
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the offset in the packet where the calculation of the extra checksum is started from. Set to OFF or 0 to disable.
        Valid enable range is [8 .. 127, ON].
        Please observe that ON equals the value 14.
        Please also observe that P_CHECKSUM ? will return OFF if set to 0 (or OFF) and that P_CHECKSUM ? will return ON if set to 14 (or ON).

        :return: the offset in the packet where the calculation of the extra checksum is started from
        :rtype: P_CHECKSUM.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, offset: int) -> Token[None]:
        """Set the offset in the packet where the calculation of the extra checksum is started from.
        Set to OFF or 0 to disable. Valid enable range is [8 .. 127, ON].
        Please observe that ON equals the value 14.
        Please also observe that P_CHECKSUM ? will return OFF if set to 0 (or OFF) and that P_CHECKSUM ? will return ON if set to 14 (or ON).

        :param offset:  the offset in the packet where the calculation of the extra checksum is started from
        :type offset: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, offset=offset))

    set_off = functools.partialmethod(set, 0)
    """Set port's payload checksum off (offset = 0).
    """

    set_on = functools.partialmethod(set, 14)
    """Set port's payload checksum on (offset = 14).
    """


@register_command
@dataclass
class P_STATUS:
    """
    Get the received signal level for optical ports.
    """

    code: typing.ClassVar[int] = 303
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        optical_power: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, received signal level for optical ports, in nanowatts, -1 when not available."""

    def get(self) -> Token[GetDataAttr]:
        """Get the received signal level for optical ports, in nanowatts, -1 when not available.

        :return: the received signal level for optical ports, in nanowatts, -1 when not available
        :rtype: P_STATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_AUTONEGSELECTION:
    """
    Whether the port responds to incoming auto-negotiation requests. Only applicable
    to electrical ports (RJ45).
    """

    code: typing.ClassVar[int] = 304
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to auto-neg requests."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to auto-neg requests."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the port responds to incoming auto-negotiation requests.

        :return: whether the port responds to incoming auto-negotiation requests
        :rtype: P_AUTONEGSELECTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether the port responds to incoming auto-negotiation requests.

        :param on_off: whether the port responds to incoming auto-negotiation requests
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)

    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class P_MIXLENGTH:
    """
    Allows inspecting the frame sizes defined for each position of the P_MIXWEIGHTS command.  By default, the 16 frame sizes are: 56 (not valid for 40G/100G), 60, 64, 70, 78, 92, 256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.  In addition to inspecting these sizes one by one, it also allows changing frame size for positions 0, 1, 14 and 15 (default values 56, 60, 9216 and 16360).
    """

    code: typing.ClassVar[int] = 305
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _position_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        frame_size: int = field(XmpInt())
        """integer, frame size of the position"""

    class SetDataAttr(RequestBodyStruct):
        frame_size: int = field(XmpInt())
        """integer, frame size of the position"""

    def get(self) -> Token[GetDataAttr]:
        """Get frame sizes defined for each position of the P_MIXWEIGHTS command.
        By default, the 16 frame sizes are: 56 (not valid for 40G/100G), 60,
        64, 70, 78, 92, 256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.

        :return: frame sizes defined for each position of the P_MIXWEIGHTS command
        :rtype: P_MIXLENGTH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._position_xindex]))

    def set(self, frame_size: int) -> Token[None]:
        """Set the frame size defined for positions 0, 1, 14 and 15 (default values 56, 60, 9216 and 16360), in bytes.

        :param frame_size: the frame size for the position.
        :type frame_size: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._position_xindex], frame_size=frame_size))


@register_command
@dataclass
class P_ARPRXTABLE:
    """
    Port ARP table used to reply to incoming ARP requests.
    """

    code: typing.ClassVar[int] = 308
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        chunks: typing.List[ArpChunk] = field(XmpSequence(types_chunk=[XmpIPv4Address(), XmpShort(), XmpByte(), XmpMacAddress()]))

    class SetDataAttr(RequestBodyStruct):
        chunks: typing.List[ArpChunk] = field(XmpSequence(types_chunk=[XmpIPv4Address(), XmpShort(), XmpByte(), XmpMacAddress()]))

    def get(self) -> Token[GetDataAttr]:
        """Get the port's ARP table used to reply to incoming ARP requests.

        :return: the port's ARP table used to reply to incoming ARP requests.
            * IP address to match to the Target IP address in the ARP requests,
            * The prefix used for address matching,
            * Whether the target MAC address will be patched with the part of the IP address that is not masked by the prefix,
            * The target MAC address to return in the ARP reply
        :rtype: P_ARPRXTABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, chunks: typing.List[ArpChunk]) -> Token[None]:
        """Set the port's ARP table used to reply to incoming ARP requests.

        :param chunks:
            * IP address to match to the Target IP address in the ARP requests
            * The prefix used for address matching
            * Whether the target MAC address will be patched with the part of the IP address that is not masked by the prefix
            * The target MAC address to return in the ARP reply
        :type chunks: typing.List[subtypes.ArpChunkList]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, chunks=chunks))


@register_command
@dataclass
class P_NDPRXTABLE:
    """
    Port NDP table used to reply to incoming NDP Neighbor Solicitation.
    """

    code: typing.ClassVar[int] = 309
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        chunks: typing.List[NdpChunk] = field(XmpSequence(types_chunk=[XmpIPv6Address(), XmpShort(), XmpByte(), XmpMacAddress()]))

    class SetDataAttr(RequestBodyStruct):
        chunks: typing.List[NdpChunk] = field(XmpSequence(types_chunk=[XmpIPv6Address(), XmpShort(), XmpByte(), XmpMacAddress()]))

    def get(self) -> Token[GetDataAttr]:
        """Get the port's NDP table used to reply to incoming NDP Neighbor Solicitation.

        :return: the port's NDP table used to reply to incoming NDP Neighbor Solicitation.
            * IP address to match to the Target IP address in the NDP Neighbor Solicitation
            * The prefix used for address matching
            * Whether the target MAC address will be patched with the part of the IP address that is not masked by the prefix
            * The target MAC address to return in the NDP Neighbor Advertisement
        :rtype: P_NDPRXTABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, chunks: typing.List[NdpChunk]) -> Token[None]:
        """Set the port's NDP table used to reply to incoming NDP Neighbor Solicitation.

        :param chunks:
            * IP address to match to the Target IP address in the NDP Neighbor Solicitation
            * The prefix used for address matching
            * Whether the target MAC address will be patched with the part of the IP address that is not masked by the prefix
            * The target MAC address to return in the NDP Neighbor Advertisement
        :type chunks: typing.List[subtypes.NdpChunkList]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, chunks=chunks))


@register_command
@dataclass
class P_MULTICAST:
    """
    A multicast mode for a port. Ports can use the IGMPv2 protocol to join or leave multicast groups, either on an on-off basis or repeatedly.
    """

    code: typing.ClassVar[int] = 311
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address] = field(XmpSequence(types_chunk=[XmpIPv4Address()]))
        """a multicast group address to join or leave"""
        operation: MulticastOperation = field(XmpByte())
        """coded byte, specifying the operation."""
        second_count: int = field(XmpByte())
        """the interval between repeated joins in seconds."""

    class SetDataAttr(RequestBodyStruct):
        ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address] = field(XmpSequence(types_chunk=[XmpIPv4Address()]))
        """a multicast group address to join or leave"""
        operation: MulticastOperation = field(XmpByte())
        """coded byte, specifying the operation."""
        second_count: int = field(XmpByte())
        """the interval between repeated joins in seconds."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port's multicast information (IGMPv2).

        :return: the port's multicast information (IGMPv2)
        :rtype: P_MULTICAST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address], operation: MulticastOperation, second_count: int) -> Token[None]:
        """Set the port's multicast information (IGMPv2).

        :param ipv4_multicast_addresses: a multicast group address to join or leave
        :type ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address]
        :param operation: the operation
        :type operation: MulticastOperation
        :param second_count: the interval between repeated joins in seconds.
        :type second_count: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                ipv4_multicast_addresses=ipv4_multicast_addresses,
                operation=operation,
                second_count=second_count
            )
        )

    set_off = functools.partialmethod(set, operation=MulticastOperation.OFF)
    """Set port's multicast operation to Off.
    """

    set_on = functools.partialmethod(set, operation=MulticastOperation.ON)
    """Set port's multicast operation to On.
    """

    set_join = functools.partialmethod(set, operation=MulticastOperation.JOIN)
    """Set port's multicast operation to Join.
    """

    set_leave = functools.partialmethod(set, operation=MulticastOperation.LEAVE)
    """Set port's multicast operation to Join.
    """


@register_command
@dataclass
class P_MULTICASTEXT:
    """
    A multicast mode for a port. Ports can use the IGMPv2/IGMPv3 protocol to join or leave multicast groups, either on an on-off basis or repeatedly. 
    """

    code: typing.ClassVar[int] = 312
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address] = field(XmpSequence(types_chunk=[XmpIPv4Address()]))
        """list of addresses, up to 8 multicast group addresses to receive an operation"""
        operation: MulticastExtOperation = field(XmpByte())
        """coded byte, specifying the operation."""
        second_count: int = field(XmpByte())
        """byte, the interval between repeated joins/excludes in seconds."""
        igmp_version: IGMPVersion = field(XmpByte())
        """coded byte, specifying the IGMP version."""

    class SetDataAttr(RequestBodyStruct):
        ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address] = field(XmpSequence(types_chunk=[XmpIPv4Address()]))
        """list of addresses, up to 8 multicast group addresses to receive an operation"""
        operation: MulticastExtOperation = field(XmpByte())
        """coded byte, specifying the operation."""
        second_count: int = field(XmpByte())
        """byte, the interval between repeated joins/excludes in seconds."""
        igmp_version: IGMPVersion = field(XmpByte())
        """coded byte, specifying the IGMP version."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port's multicast information (IGMPv2/IGMPv3).

        :return: the port's multicast information (IGMPv2/IGMPv3)
        :rtype: P_MULTICASTEXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address], operation: MulticastExtOperation, second_count: int, igmp_version: IGMPVersion) -> Token[None]:
        """Set the port's multicast information (IGMPv2/IGMPv3).

        :param ipv4_multicast_addresses: a multicast group address to join or leave
        :type ipv4_multicast_addresses: typing.List[ipaddress.IPv4Address]
        :param operation: the operation
        :type operation: MulticastExtOperation
        :param second_count: the interval between repeated joins in seconds.
        :type second_count: int
        :param igmp_version: IGMP version
        :type igmp_version: IGMPVersion
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                ipv4_multicast_addresses=ipv4_multicast_addresses,
                operation=operation,
                second_count=second_count,
                igmp_version=igmp_version
            )
        )


@register_command
@dataclass
class P_MCSRCLIST:
    """
    Multicast source list of the port. Only valid if the IGMP protocol version is IGMPv3 set by P_MULTICASTEXT.
    """

    code: typing.ClassVar[int] = 313
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ipv4_addresses: typing.List[ipaddress.IPv4Address] = field(XmpSequence(types_chunk=[XmpIPv4Address()]))
        """list of addresses, multicast source list addresses (max 8) in Group Record field of the IGMPv3 membership report packet."""

    class SetDataAttr(RequestBodyStruct):
        ipv4_addresses: typing.List[ipaddress.IPv4Address] = field(XmpSequence(types_chunk=[XmpIPv4Address()]))
        """list of addresses, multicast source list addresses (max 8) in Group Record field of the IGMPv3 membership report packet."""

    def get(self) -> Token[GetDataAttr]:
        """Get the multicast source list of the port. Only valid if the IGMP protocol version is IGMPv3 set by P_MULTICASTEXT.

        :return: the multicast source list of the port
        :rtype: P_MCSRCLIST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, ipv4_addresses: typing.List[ipaddress.IPv4Address]) -> Token[None]:
        """Set the multicast source list of the port.

        :param ipv4_addresses: the multicast source list of the port
        :type ipv4_addresses: typing.List[ipaddress.IPv4Address]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, ipv4_addresses=ipv4_addresses))


@register_command
@dataclass
class P_IGMPV3_GROUP_RECORD_BUNDLE:
    """
    Configure if a single membership report bundles multiple multicast group records to decrease the number of packets sent when using IGMPv3. This command returns <NOTVALID> when the IGMP version is not IGMPv3.
    """

    code: typing.ClassVar[int] = 315
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: OnOff = field(XmpByte())
        """byte, if a single membership report bundles multiple multicast group records to decrease the number of packets sent when using IGMPv3."""

    class SetDataAttr(RequestBodyStruct):
        mode: OnOff = field(XmpByte())
        """byte, if a single membership report bundles multiple multicast group records to decrease the number of packets sent when using IGMPv3."""

    def get(self) -> Token[GetDataAttr]:
        """Get the mode of IGMPV3 group record bundle.

        :return: the mode of IGMPV3 group record bundle.
        :rtype: P_IGMPV3_GROUP_RECORD_BUNDLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: OnOff) -> Token[None]:
        """Set the mode of IGMPV3 group record bundle.

        :param mode: the mode of IGMPV3 group record bundle
        :type: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))
    

@register_command
@dataclass
class P_TXMODE:
    """
    The scheduling mode for outgoing traffic from the port, specifying how multiple
    logical streams are merged onto one physical port. There are four primary modes:
    Normal Interleaved: The streams are treated independently, and are merged into a
    combined traffic pattern for the port, which honors each stream's ideal packet
    placements as well as possible. This is the default mode. Strict Uniform: This
    is a slight variation of normal interleaved scheduling, which emphasizes strict
    uniformity of the inter-packet-gaps as more important than hitting the stream
    rates absolutely precisely. Sequential: Each stream in turn contribute one or
    more packets, before continuing to the next stream, in a cyclical pattern. The
    count of packets for each stream is obtained from the PS_PACKETLIMIT command
    value for the stream. The individual rates for each stream are ignored, and
    instead the overall rate is determined at the port-level. This in turn determines
    the rates for each stream, taking into account their packet lengths and counts.
    The maximum number of packets in a cycle (i.e. the sum of PS_PACKETLIMIT for all
    enabled streams) is 500. If the packet number is larger than 500,  will be returned
    when attempting to start the traffic (P_TRAFFIC ON). Burst*: When this mode is selected,
    frames from the streams on a port are sent as bursts as depicted below:
    The Burst Period is defined in the P_TXBURSTPERIOD command. For the individual streams
    the number of packets in a burst is defined by the PS_BURST command, while the Inter
    Packet Gap and the Inter Burst Gap are defined by the PS_BURSTGAP command.
    """

    code: typing.ClassVar[int] = 320
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: TXMode = field(XmpByte())
        """coded byte, containing the loopback mode for the port:
            NORMAL (interleaved packet scheduling),
            STRICTUNIFORM (strict uniform mode),
            SEQUENTIAL (sequential packet scheduling),
            BURST (burst mode).
        """

    class SetDataAttr(RequestBodyStruct):
        mode: TXMode = field(XmpByte())
        """coded byte, containing the loopback mode for the port:
        NORMAL (interleaved packet scheduling),
        STRICTUNIFORM (strict uniform mode),
        SEQUENTIAL (sequential packet scheduling),
        BURST (burst mode).
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the scheduling mode for outgoing traffic from the port.

        :return: the scheduling mode for outgoing traffic from the port, containing the loopback mode for the port:
            NORMAL (interleaved packet scheduling),
            STRICTUNIFORM (strict uniform mode),
            SEQUENTIAL (sequential packet scheduling),
            BURST (burst mode).
        :rtype: P_TXMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: TXMode) -> Token[None]:
        """Set the the scheduling mode for outgoing traffic from the port.

        :param mode: the scheduling mode for outgoing traffic from the port, containing the loopback mode for the port:
            NORMAL (interleaved packet scheduling),
            STRICTUNIFORM (strict uniform mode),
            SEQUENTIAL (sequential packet scheduling),
            BURST (burst mode).
        :type mode: TXMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_normal = functools.partialmethod(set, TXMode.NORMAL)
    """Set the port scheduling mode to Normal.
    """

    set_strictuniform = functools.partialmethod(set, TXMode.STRICTUNIFORM)
    """Set the port scheduling mode to Strict Uniform.
    """

    set_sequential = functools.partialmethod(set, TXMode.SEQUENTIAL)
    """Set the port scheduling mode to Sequential.
    """

    set_burst = functools.partialmethod(set, TXMode.BURST)
    """Set the port scheduling mode to Burst.
    """


@register_command
@dataclass
class P_MULTICASTHDR:
    """
    Allows addition of a VLAN tag to IGMPv2 and IGPMv3 packets.
    """

    code: typing.ClassVar[int] = 314
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        header_count: int = field(XmpByte())
        """byte, number of additional headers. Currently only 0 or 1 supported."""
        header_format: MulticastHeaderFormat = field(XmpByte())
        """byte, indicates the header format. 0 = no header, 1 = VLAN"""
        tag: int = field(XmpInt())
        """integer, VLAN tag (VID)"""
        pcp: int = field(XmpByte())
        """byte, VLAN Priority code point"""
        dei: OnOff = field(XmpByte())
        """byte, drop-eligible indicator"""

    class SetDataAttr(RequestBodyStruct):
        header_count: int = field(XmpByte())
        """byte, number of additional headers. Currently only 0 or 1 supported."""
        header_format: MulticastHeaderFormat = field(XmpByte())
        """byte, indicates the header format. 0 = no header, 1 = VLAN"""
        tag: int = field(XmpInt())
        """integer, VLAN tag (VID)"""
        pcp: int = field(XmpByte())
        """byte, VLAN Priority code point"""
        dei: OnOff = field(XmpByte())
        """byte, drop-eligible indicator."""

    def get(self) -> Token[GetDataAttr]:
        """Get the VLAN tag to the IGMPv2 and IGMPv3 packets of the port.

        :return: the VLAN tag to the IGMPv2 and IGMPv3 packets of the port
        :rtype: P_MULTICASTHDR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, header_count: int, header_format: MulticastHeaderFormat, tag: int, pcp: int, dei: OnOff) -> Token[None]:
        """Set the VLAN tag to the IGMPv2 and IGMPv3 packets of the port.

        :param header_count: number of additional headers. Currently only 0 or 1 supported
        :type header_count: int
        :param header_format: indicates the header format
        :type header_format: MulticastHeaderFormat
        :param tag: VLAN tag (VID)
        :type tag: int
        :param pcp: VLAN Priority code point
        :type pcp: int
        :param dei: drop-eligible indicator
        :type dei: OnOff
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                header_count=header_count,
                header_format=header_format,
                tag=tag,
                pcp=pcp,
                dei=dei
            )
        )


@register_command
@dataclass
class P_RATEFRACTION:
    """
    The port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in millionths of the effective rate for the port. The bandwidth consumption includes the inter-frame gaps, and does not depend on the length of the packets for the streams.
    """

    code: typing.ClassVar[int] = 321
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        port_rate_ppm: int = field(XmpInt())
        """integer, port rate expressed as a value between 0 and 1,000,000."""

    class SetDataAttr(RequestBodyStruct):
        port_rate_ppm: int = field(XmpInt())
        """integer, port rate expressed as a value between 0 and 1,000,000."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in millionths of the effective rate for the port.

        :return: the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in millionths of the effective rate for the port.
        :rtype: P_RATEFRACTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, port_rate_ppm: int) -> Token[None]:
        """Set the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in millionths of the effective rate for the port.

        :param port_rate_ppm: the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in millionths of the effective rate for the port
        :type port_rate_ppm: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, port_rate_ppm=port_rate_ppm))


@register_command
@dataclass
class P_RATEPPS:
    """
    The port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in packets per second. The bandwidth consumption is heavily dependent on the length of the packets generated for the streams, and also on the inter-frame gap for the port.
    """

    code: typing.ClassVar[int] = 322
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        port_rate_pps: int = field(XmpInt())
        """integer, port rate expressed as packets per second."""

    class SetDataAttr(RequestBodyStruct):
        port_rate_pps: int = field(XmpInt())
        """integer, port rate expressed as packets per second."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in packets per second.

        :return: the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in packets per second
        :rtype: P_RATEPPS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, port_rate_pps: int) -> Token[None]:
        """Set the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in packets per second.

        :param port_rate_pps: the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in packets per second
        :type port_rate_pps: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, port_rate_pps=port_rate_pps))


@register_command
@dataclass
class P_RATEL2BPS:
    """
    The port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in units of bits per-second at layer-2, thus including the Ethernet header but excluding the inter-frame gap. The bandwidth consumption is somewhat dependent on the length of the packets generated for the stream, and also on the inter-frame gap for the port.
    """

    code: typing.ClassVar[int] = 323
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        port_rate_bps: int = field(XmpLong())
        """long integer, port rate expressed as bits-per-second."""

    class SetDataAttr(RequestBodyStruct):
        port_rate_bps: int = field(XmpLong())
        """long integer, port rate expressed as bits-per-second."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port-level rate of the traffic transmitted for a port in sequential tx mode,
        expressed in units of bits per-second at layer-2, thus including the Ethernet header but excluding the inter-frame gap.

        :return: the port-level rate of the traffic transmitted for a port in sequential tx mode,
            expressed in units of bits per-second at layer-2, thus including the Ethernet header but excluding the inter-frame gap
        :rtype: P_RATEL2BPS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, port_rate_bps: int) -> Token[None]:
        """Set the port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in units of bits per-second at layer-2,
        thus including the Ethernet header but excluding the inter-frame gap.

        :param port_rate_bps: the port-level rate of the traffic transmitted for a port in sequential tx mode,
            expressed in units of bits per-second at layer-2, thus including the Ethernet header but excluding the inter-frame gap
        :type port_rate_bps: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, port_rate_bps=port_rate_bps))


@register_command
@dataclass
class P_PAYLOADMODE:
    """
    Set this command to configure the port to use different payload modes, i.e. normal, extend payload, and custom payload field, for ALL streams on this port. The extended payload feature allows the definition of a much larger (up to MTU) payload buffer for each stream. The custom payload field feature allows you to define a sequence of custom data fields for each stream. The data fields will then be used in a round robin fashion when packets are sent based on the stream definition.
    """

    code: typing.ClassVar[int] = 324
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: PayloadMode = field(XmpByte())
        """coded byte, which is the payload mode the port should be set."""

    class SetDataAttr(RequestBodyStruct):
        mode: PayloadMode = field(XmpByte())
        """coded byte, which is the payload mode the port should be set."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port's payload mode, i.e. normal, extend payload, and custom payload field, for ALL streams on this port.

        :return: the port's payload mode, i.e. normal, extend payload, and custom payload field, for ALL streams on this port.
        :rtype: P_PAYLOADMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: PayloadMode) -> Token[None]:
        """Set the port's payload mode, i.e. normal, extend payload, and custom payload field, for ALL streams on this port.

        :param mode: the port's payload mode, i.e. normal, extend payload, and custom payload field, for ALL streams on this port
        :type mode: PayloadMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_normal = functools.partialmethod(set, PayloadMode.NORMAL)
    """Set the port's payload mode to Normal.
    """

    set_extpl = functools.partialmethod(set, PayloadMode.EXTPL)
    """Set the port's payload mode to Extend Payload.
    """

    set_cdf = functools.partialmethod(set, PayloadMode.CDF)
    """Set the port's payload mode to Custom Payload Field.
    """


@register_command
@dataclass
class P_BRRMODE:
    """
    Selects the Master/Slave setting of
    100 Mbit/s, 1000 Mbit/s BroadR-Reach copper interfaces.
    """

    code: typing.ClassVar[int] = 326
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: BRRMode = field(XmpByte())
        """coded byte, containing the Master/Slave mode for the port."""

    class SetDataAttr(RequestBodyStruct):
        mode: BRRMode = field(XmpByte())
        """coded byte, containing the Master/Slave mode for the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port's BroadR-Reach mode.

        :return: the port's BroadR-Reach mode
        :rtype: P_BRRMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: BRRMode) -> Token[None]:
        """Set the port's BroadR-Reach mode.

        :param mode: the port's BroadR-Reach mode
        :type mode: BRRMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_slave = functools.partialmethod(set, BRRMode.SLAVE)
    """Set the port's BRR mode to Slave.
    """

    set_master = functools.partialmethod(set, BRRMode.MASTER)
    """Set the port's BRR mode to Master.
    """


@register_command
@dataclass
class P_TXENABLE:
    """
    Whether a port should enable its transmitter, or keep the outgoing link down.
    """

    code: typing.ClassVar[int] = 327
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the transmitter is enabled or disabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the transmitter is enabled or disabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port's transmitter status.

        :return: the port's transmitter status
        :rtype: P_TXENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the the port's transmitter status.

        :param on_off: the port's transmitter status
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the port's transmitter and keep the outgoing link down.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the port's transmitter.
    """


@register_command
@dataclass
class P_MAXHEADERLENGTH:
    """
    The maximum number of header content bytes that can be freely specified for each generated stream. The remaining payload bytes of the packet are auto-generated.The default is 128 bytes. When a larger number is select there is a corresponding proportional reduction in the number of stream definitions that are available for the port. Possible values: 128 (default), 256, 512, 1024, 2048.
    """

    code: typing.ClassVar[int] = 328
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        max_header_length: int = field(XmpInt())
        """integer, specifying the maximum number of header bytes."""

    class SetDataAttr(RequestBodyStruct):
        max_header_length: int = field(XmpInt())
        """integer, specifying the maximum number of header bytes."""

    def get(self) -> Token[GetDataAttr]:
        """Get the maximum number of header content bytes that can be freely specified for each generated stream on the port.

        :return: the maximum number of header content bytes that can be freely specified for each generated stream on the port
        :rtype: P_MAXHEADERLENGTH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, max_header_length: int) -> Token[None]:
        """Set the maximum number of header content bytes that can be freely specified for each generated stream on the port. Possible values: 128 (default), 256, 512, 1024, 2048.

        :param max_header_length: the maximum number of header content bytes that can be freely specified for each generated stream on the port
        :type max_header_length: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, max_header_length=max_header_length))


@register_command
@dataclass
class P_TXTIMELIMIT:
    """
    A port-level time-limit on how long it keeps transmitting when started. After
    the elapsed time traffic must be stopped and restarted. This complements the
    stream-level PS_PACKETLIMIT function.
    """

    code: typing.ClassVar[int] = 329
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        microseconds: int = field(XmpLong())
        """long integer, time limit after which the port stops transmitting."""

    class SetDataAttr(RequestBodyStruct):
        microseconds: int = field(XmpLong())
        """long integer, time limit after which the port stops transmitting."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port-level time-limit on how long it keeps transmitting when started in microseconds.

        :return: port-level time-limit on how long it keeps transmitting when started in microseconds.
        :rtype: P_TXTIMELIMIT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, microseconds: int) -> Token[None]:
        """Set the port-level time-limit on how long it keeps transmitting when started in microseconds. Maximum can be 2^63.

        :param microseconds: the port-level time-limit on how long it keeps transmitting when started in microseconds. Maximum can be 2^63
        :type microseconds: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, microseconds=microseconds))


@register_command
@dataclass
class P_TXTIME:
    """
    How long the port has been transmitting, the elapsed time since traffic was
    started.
    """

    code: typing.ClassVar[int] = 330
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        microseconds: int = field(XmpLong())
        """long integer, elapsed time since traffic was started."""

    def get(self) -> Token[GetDataAttr]:
        """Get how long the port has been transmitting, the elapsed time since traffic was started in microseconds.

        :return: how long the port has been transmitting, the elapsed time since traffic was started in microseconds
        :rtype: P_TXTIME.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_XMITONETIME:
    """
    The time at which the latest packet was transmitted using the P_XMITONE command. The time reference is the same used by the time stamps of captured packets.
    """

    code: typing.ClassVar[int] = 331
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        nanoseconds: int = field(XmpLong())
        """long integer, the time at which packet was transmitted."""

    def get(self) -> Token[GetDataAttr]:
        """Get the time at which the latest packet was transmitted using the P_XMITONE command in nanoseconds.

        :return: the time at which the latest packet was transmitted using the P_XMITONE command in nanoseconds
        :rtype: P_XMITONETIME.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_IPV6ADDRESS:
    """
    An IPv6 network configuration specified for a port. The address is used as the
    default source address field in the IP header of generated traffic, and the
    configuration is also used for support of the NDP and PINGv6 protocols.
    """

    code: typing.ClassVar[int] = 332
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ipv6_address: ipaddress.IPv6Address = field(XmpIPv6Address())
        """address, the IPv6 address of the port."""
        gateway: ipaddress.IPv6Address = field(XmpIPv6Address())
        """address, the gateway of the local network segment for the port."""
        subnet_prefix: int = field(XmpByte())
        """byte, the subnet prefix of the local network segment for the port."""
        wildcard_prefix: int = field(XmpByte())
        """byte, a prefix that makes the port replies to NDP/PING for the masked addresses, valid value 0-255"""

    class SetDataAttr(RequestBodyStruct):
        ipv6_address: ipaddress.IPv6Address = field(XmpIPv6Address())
        """address, the IPv6 address of the port."""
        gateway: ipaddress.IPv6Address = field(XmpIPv6Address())
        """address, the gateway of the local network segment for the port."""
        subnet_prefix: int = field(XmpByte())
        """byte, the subnet prefix of the local network segment for the port."""
        wildcard_prefix: int = field(XmpByte())
        """byte, a prefix that makes the port replies to NDP/PING for the masked addresses, valid value 0-255"""

    def get(self) -> Token[GetDataAttr]:
        """Get the port's IPv6 address settings.

        :return: the port's IPv6 address settings
        :rtype: P_IPV6ADDRESS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, ipv6_address: ipaddress.IPv6Address, gateway: ipaddress.IPv6Address, subnet_prefix: int, wildcard_prefix: int) -> Token[None]:
        """Set the port's IPv6 settings.

        :param ipv6_address: the IPv6 address of the port
        :type ipv6_address: Union[str, int, ipaddress.IPv6Address]
        :param gateway: the gateway of the local network segment for the port
        :type gateway: Union[str, int, ipaddress.IPv6Address]
        :param subnet_prefix: the subnet prefix of the local network segment for the port
        :type subnet_prefix: int
        :param wildcard_prefix: a prefix that makes the port replies to NDP/PING for the masked addresses, valid value 0-255
        :type wildcard_prefix: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                ipv6_address=ipv6_address,
                gateway=gateway,
                subnet_prefix=subnet_prefix,
                wildcard_prefix=wildcard_prefix
            )
        )


@register_command
@dataclass
class P_ARPV6REPLY:
    """
    Whether the port generates replies using the IPv6 Network Discovery Protocol.
    The port can reply to incoming NDP Neighbor Solicitations by mapping the IPv6 address
    specified for the port to the MAC address specified for the port. NDP reply
    generation is independent of whether traffic and capture is on for the port.
    """

    code: typing.ClassVar[int] = 333
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to NDP Neighbor Solicitations."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to NDP Neighbor Solicitations."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the port replies to NDP Neighbor Solicitations.

        :return: whether the port replies to NDP Neighbor Solicitations.
        :rtype: P_ARPV6REPLY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether the port replies to NDP Neighbor Solicitations.

        :param on_off: whether the port replies to NDP Neighbor Solicitations.
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the port from replying to NDP Neighbor Solicitations.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the port to reply to NDP Neighbor Solicitations.
    """


@register_command
@dataclass
class P_PINGV6REPLY:
    """
    Whether the port generates PINGv6 replies using the ICMP protocol received over
    IPv6. The port can reply to incoming PINGv6 requests to the IPv6 address
    specified for the port. PINGv6 reply generation is independent of whether
    traffic and capture is on for the port.
    """

    code: typing.ClassVar[int] = 334
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to PINGv6 requests."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the port replies to PINGv6 requests."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the port replies to incoming PINGv6.

        :return: whether the port replies to incoming PINGv6
        :rtype: P_PINGV6REPLY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether the port replies to incoming PINGv6.

        :param on_off: whether the port replies to incoming PINGv6.
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the port from replying to PINGv6.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the port to reply to PINGv6.
    """


@register_command
@dataclass
class P_ERRORS:
    """
    Obtains the total number of errors detected across all streams on the port,
    including lost packets, misorder events, and payload errors.

    .. note::

        FCS errors are included, which will typically lead to double-counting of lost packets.

    """

    code: typing.ClassVar[int] = 335
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        error_count: int = field(XmpLong())
        """list of long integers, the total number of errors across all streams, and including FCS errors."""

    def get(self) -> Token[GetDataAttr]:
        """Get the total number of errors detected across all streams on the port, including lost packets, misorder events, and payload errors.

        :return: the total number of errors detected across all streams on the port, including lost packets, misorder events, and payload errors
        :rtype: P_ERRORS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_TXPREPARE:
    """
    Prepare port for transmission
    """

    code: typing.ClassVar[int] = 336
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Set the port to prepare for packet transmission.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_TXDELAY:
    """
    Sets a variable delay from a traffic start command received by the port until
    it starts transmitting. The delay is specified in multiples of 64 microseconds.
    Valid values are 0-31250 (0 to 2,000,000 microseconds).

    .. note::

        You must use C_TRAFFIC instead of P_TRAFFIC to start traffic for P_TXDELAY to take effect.

    """

    code: typing.ClassVar[int] = 337
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        delay_val: int = field(XmpInt())
        """integer, TX delay in multiples of 64 microseconds. (TX delay = delay_val * 64 microseconds)."""

    class SetDataAttr(RequestBodyStruct):
        delay_val: int = field(XmpInt())
        """integer, TX delay in multiples of 64 microseconds. (TX delay = delay_val * 64 microseconds)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the delay from a traffic start command received by the port until the port starts transmitting packets, in microseconds.

        :return: the delay from a traffic start command received by the port until the port starts transmitting packets, in microseconds.
        :rtype: P_TXDELAY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, delay_val: int) -> Token[None]:
        """Set the delay from a traffic start command received by the port until the port starts transmitting packets, in microseconds.

        :param delay_val: the delay specified in multiples of 64 microseconds.
        :type delay_val: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, delay_val=delay_val))


@register_command
@dataclass
class P_LPENABLE:
    """
    Enables/disables Energy Efficient Ethernet (EEE) on the port.
    """

    code: typing.ClassVar[int] = 340
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the EEE feature is activated or not."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether the EEE feature is activated or not."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether Energy Efficient Ethernet (EEE) is enabled on the port.

        :return: whether Energy Efficient Ethernet (EEE) is enabled on the port
        :rtype: P_LPENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether Energy Efficient Ethernet (EEE) is enabled on the port.

        :param on_off: whether Energy Efficient Ethernet (EEE) is enabled on the port
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable Energy Efficient Ethernet (EEE) on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable Energy Efficient Ethernet (EEE) on the port.
    """


@register_command
@dataclass
class P_LPTXMODE:
    """
    Enables/disables the transmission of Low Power Idles (LPIs) on the port. When
    enabled, the transmit side of the port will automatically enter low-power mode
    (and leave) low-power mode in periods of low or no traffic. LPIs will only be
    transmitted if the Link Partner (receiving port) has advertised EEE capability
    for the selected port speed during EEE auto-negotiation.
    """

    code: typing.ClassVar[int] = 341
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether low power idles will be transmitted or not. OFF (0) ON (1)"""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether low power idles will be transmitted or not. OFF (0) ON (1)"""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the transmission of Low Power Idles (LPIs) is enabled on the port.

        :return: whether the transmission of Low Power Idles (LPIs) is enabled on the port
        :rtype: P_LPTXMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether the transmission of Low Power Idles (LPIs) is enabled on the port.

        :param on_off: whether the transmission of Low Power Idles (LPIs) is enabled on the port
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the transmission of Low Power Idles (LPIs) on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the transmission of Low Power Idles (LPIs) on the port.
    """


@register_command
@dataclass
class P_LPSTATUS:
    """
    Displays the Energy Efficient Ethernet (EEE) status as reported by the PHY.
    """

    code: typing.ClassVar[int] = 343
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        txh: TXHState = field(XmpByte())
        """coded bytes, shows if there has been any recent change in the EEE state on the transmission side (either going into low power mode or leaving low power mode."""
        rxh: RXHState = field(XmpByte())
        """shows if there has been any recent change in the EEE state on the receiver side (either going into low power mode or leaving low power mode."""
        txc: TXCState = field(XmpByte())
        """shows the current EEE state of the transmitter (in low power or active)"""
        rxc: RXCState = field(XmpByte())
        """shows the current EEE state of the receiver (in low power or active)."""
        link_up: LinkState = field(XmpByte())
        """shows if the link is up (seen from perspective of the the PHY's PCS)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the the Energy Efficient Ethernet (EEE) status as reported by the PHY.
            * if there has been any recent change in the EEE state on the transmission side
            * if there has been any recent change in the EEE state on the receiver side
            * the current EEE state of the transmitter
            * the current EEE state of the receiver
            * if the link is up

        :return: the the Energy Efficient Ethernet (EEE) status
        :rtype: P_LPSTATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_LPPARTNERAUTONEG:
    """
    Displays the EEE capabilities advertised during auto-negotiation by the far side
    (link partner).
    """

    code: typing.ClassVar[int] = 345
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        cap_100base_tx: YesNo = field(XmpByte())
        """coded byte, specifying whether the link partner is capable of 100BASE-TX."""
        cap_1000base_t: YesNo = field(XmpByte())
        """coded byte. specifying whether the link partner is capable of 1000BASE-T."""
        cap_10gbase_t: YesNo = field(XmpByte())
        """coded byte. specifying whether the link partner is capable of 10GBASE-T."""
        cap_100base_kx: YesNo = field(XmpByte())
        """coded byte. specifying whether the link partner is capable of 100BASE-KX."""
        cap_10gbase_kx4: YesNo = field(XmpByte())
        """coded byte. specifying whether the link partner is capable of 10GBASE-KX4."""
        cap_10gbase_kr: YesNo = field(XmpByte())
        """coded byte. specifying whether the link partner is capable of 10GBASE-KR."""

    def get(self) -> Token[GetDataAttr]:
        """Get the the Energy Efficient Ethernet (EEE) capabilities advertised during auto-negotiation by the far side (link partner).
            * whether the link partner is capable of 100BASE-TX
            * whether the link partner is capable of 1000BASE-T
            * whether the link partner is capable of 10GBASE-T
            * whether the link partner is capable of 100BASE-KX
            * whether the link partner is capable of 10GBASE-KX4
            * whether the link partner is capable of 10GBASE-KR

        :return: the the Energy Efficient Ethernet (EEE) capabilities advertised during auto-negotiation by the far side (link partner)
        :rtype: P_LPPARTNERAUTONEG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_LPSNRMARGIN:
    """
    Displays the SNR margin on the four link channels (Channel A-D) as reported by
    the PHY. It is displayed in units of 0.1dB.
    """

    code: typing.ClassVar[int] = 346
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        channel_a: int = field(XmpInt())
        """integer, the SNR margin on link channel A."""
        channel_b: int = field(XmpInt())
        """integer, the SNR margin on link channel B."""
        channel_c: int = field(XmpInt())
        """integer, the SNR margin on link channel C."""
        channel_d: int = field(XmpInt())
        """integer, the SNR margin on link channel D."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SNR margin on the four link channels (Channel A-D) as reported by the PHY. It is displayed in units of 0.1dB.
            * the SNR margin on link channel A
            * the SNR margin on link channel B
            * the SNR margin on link channel C
            * the SNR margin on link channel D

        :return: the SNR margin on the four link channels (Channel A-D) as reported by the PHY. It is displayed in units of 0.1dB
        :rtype: P_LPSNRMARGIN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_LPRXPOWER:
    """
    Obtain the RX power recorded during training for the four channels.
    """

    code: typing.ClassVar[int] = 347
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        channel_a: int = field(XmpInt())
        """integer, the RX power on link channel A."""
        channel_b: int = field(XmpInt())
        """integer, the RX power on link channel B."""
        channel_c: int = field(XmpInt())
        """integer, the RX power on link channel C."""
        channel_d: int = field(XmpInt())
        """integer, the RX power on link channel D."""

    def get(self) -> Token[GetDataAttr]:
        """Get the the RX power recorded during training for the four channels.

        :return: the the RX power recorded during training for the four channels
            * the RX power on link channel A
            * the RX power on link channel B
            * the RX power on link channel C
            * the RX power on link channel D
        :rtype: P_LPRXPOWER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_FAULTSIGNALING:
    """
    Sets the remote/local fault signaling behavior of the port (performed by the
    Reconciliation Sub-layer). By default, the port acts according to the standard,
    i.e. when receiving a bad signal, it transmits "Remote Fault indications"on the
    output and when receiving a "Remote Fault indication"from the far-side it will
    transmit IDLE sequences.
    """

    code: typing.ClassVar[int] = 348
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        fault_signaling: FaultSignaling = field(XmpByte())
        """coded byte, specifying remote/local fault signaling behavior of the port."""

    class SetDataAttr(RequestBodyStruct):
        fault_signaling: FaultSignaling = field(XmpByte())
        """coded byte, specifying remote/local fault signaling behavior of the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the remote/local fault signaling behavior of the port (performed by the Reconciliation Sub-layer).

        :return: remote/local fault signaling behavior of the port
        :rtype: P_FAULTSIGNALING.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, fault_signaling: FaultSignaling) -> Token[None]:
        """Set the remote/local fault signaling behavior of the port (performed by the Reconciliation Sub-layer).

        :param fault_signaling: remote/local fault signaling behavior of the port
        :type fault_signaling: FaultSignaling
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, fault_signaling=fault_signaling))

    set_normal = functools.partialmethod(set, FaultSignaling.NORMAL)
    """Set the remote/local fault signaling behavior of the port to Normal.
    """

    set_force_local = functools.partialmethod(set, FaultSignaling.FORCE_LOCAL)
    """Set the remote/local fault signaling behavior of the port to Forced Local.
    """

    set_force_remote = functools.partialmethod(set, FaultSignaling.FORCE_REMOTE)
    """Set the remote/local fault signaling behavior of the port to Forced Remote.
    """

    set_disabled = functools.partialmethod(set, FaultSignaling.DISABLED)
    """Disable the remote/local fault signaling behavior of the port.
    """


@register_command
@dataclass
class P_FAULTSTATUS:
    """
    Shows if a local or remote fault is currently being detected by the
    Reconciliation Sub-layer of the port.

    """

    code: typing.ClassVar[int] = 349
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        local_fault_status: LocalFaultStatus = field(XmpByte())
        """coded byte, specifying the local fault."""
        remote_fault_status: RemoteFaultStatus = field(XmpByte())
        """coded byte, specifying the remote fault."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether a local or remote fault is currently being detected by the Reconciliation Sub-layer of the port.

        :return: whether a local or remote fault is currently being detected.
            * specifying the local fault
            * specifying the remote fault
        :rtype: P_FAULTSTATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_TPLDMODE:
    """
    Sets the size of the Xena Test Payload (TPLD) used to track streams, perform
    latency measurements etc. Default is "Normal", which is a 20 byte TPLD. "Micro"
    is a condensed version, which is useful when generating very small packets with
    relatively long headers (like IPv6). It has the following characteristics
    compared to the "normal" TPLD. When the TPLDMODE is changed, it will affect ALL
    streams on the port. 1) Only 6 byte long. 2) Less accurate mechanism to separate
    Xena-generated packets from other packets is the network - it is recommended not
    to have too much other traffic going into the receive Xena port, when micro TPLD
    is used. 3) No sequence checking (packet loss or packet misordering). The number
    of received packets for each stream can still be compared to the number of
    transmitted packets to detect packet loss once traffic has been stopped. Note:
    Currently not available on M6SFP, M2SFPT, M6RJ45+/M2RJ45+, M2CFP40, M1CFP100,
    M2SFP+4SFP
    """

    code: typing.ClassVar[int] = 350
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: TPLDMode = field(XmpByte())
        """coded byte, specifying TPLD's mode."""

    class SetDataAttr(RequestBodyStruct):
        mode: TPLDMode = field(XmpByte())
        """coded byte, specifying TPLD's mode."""

    def get(self) -> Token[GetDataAttr]:
        """Get the Test Payload mode of the port.

        :return: the Test Payload mode of the port
        :rtype: P_TPLDMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: TPLDMode) -> Token[None]:
        """Set the Test Payload mode of the port.

        :param mode: the Test Payload mode of the port.
        :type mode: TPLDMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_normal = functools.partialmethod(set, TPLDMode.NORMAL)
    """Set the Test Payload mode of the port to Normal.
    """

    set_micro = functools.partialmethod(set, TPLDMode.MICRO)
    """Set the Test Payload mode of the port to Micro.
    """


@register_command
@dataclass
class P_LPSUPPORT:
    """
    Read EEE capabilities of the port (variable size, one for each supported speed,
    returns 0s if no EEE).
    """

    code: typing.ClassVar[int] = 351
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        eee_capabilities: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers,EEE capabilities of the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the EEE capabilities of the port (variable size, one for each supported speed, returns 0s if no EEE).

        :return: the EEE capabilities of the port (variable size, one for each supported speed, returns 0s if no EEE).
        :rtype: P_LPSUPPORT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_TXPACKETLIMIT:
    """
    The number of packets that will be transmitted from a port when traffic is
    started on the port. A value of 0 or -1 makes the port transmit continuously.
    Traffic from the streams on the port can however also be set to stop after
    transmitting a number of packets.
    """

    code: typing.ClassVar[int] = 352
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        packet_count_limit: int = field(XmpInt())
        """integer, number of packets that will be transmitted by the port."""

    class SetDataAttr(RequestBodyStruct):
        packet_count_limit: int = field(XmpInt())
        """integer, number of packets that will be transmitted by the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the number of packets that will be transmitted from the port when traffic is started on the port.

        :return: the number of packets that will be transmitted from the port when traffic is started on the port.
        :rtype: P_TXPACKETLIMIT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, packet_count_limit: int) -> Token[None]:
        """Set the number of packets that will be transmitted from the port when traffic is started on the port.
            A value of 0 or -1 makes the port transmit continuously.
            Traffic from the streams on the port can however also be set to stop after transmitting a number of packets.

        :param packet_count_limit: the number of packets that will be transmitted from the port when traffic is started on the port
        :type packet_count_limit: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, packet_count_limit=packet_count_limit))


@register_command
@dataclass
class P_TCVRSTATUS:
    """
    Get various tcvr status information. RX loss status of the individual RX optical lanes (only 4 lanes are supported currently).
    """

    code: typing.ClassVar[int] = 357
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        rx_loss_lane_0: int = field(XmpByte())
        """RX loss of lane 0"""
        rx_loss_lane_1: int = field(XmpByte())
        """RX loss of lane 1"""
        rx_loss_lane_2: int = field(XmpByte())
        """RX loss of lane 2"""
        rx_loss_lane_3: int = field(XmpByte())
        """RX loss of lane 3"""

    def get(self) -> Token[GetDataAttr]:
        """Get various transceiver status information.

        :return: various tcvr status information. RX loss status of the individual RX optical lanes (only 4 lanes are supported currently).
        :rtype: P_TCVRSTATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_DYNAMIC:
    """
    Controls if a >10G port supports dynamic changes when the traffic is
    running. This command is only supported by ports >10G.
    """

    code: typing.ClassVar[int] = 368
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether dynamic traffic change is enabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether dynamic traffic change is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the port should support dynamic changes when the traffic is running.

        :return: whether the port should support dynamic changes when the traffic is running.
        :rtype: P_DYNAMIC.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether the port should support dynamic changes when the traffic is running.

        :param on_off: whether the port should support dynamic changes when the traffic is running
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable dynamic traffic change on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable dynamic traffic change on the port.
    """


@register_command
@dataclass
class P_PFCENABLE:
    """
    This setting control whether a port responds to incoming Ethernet Priority Flow Control (PFC) frames, by holding back outgoing traffic for that priority.
    """

    code: typing.ClassVar[int] = 373
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        cos_0: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 0."""
        cos_1: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 1."""
        cos_2: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 2."""
        cos_3: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 3."""
        cos_4: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 4."""
        cos_5: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 5."""
        cos_6: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 6."""
        cos_7: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 7."""

    class SetDataAttr(RequestBodyStruct):
        cos_0: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 0."""
        cos_1: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 1."""
        cos_2: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 2."""
        cos_3: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 3."""
        cos_4: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 4."""
        cos_5: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 5."""
        cos_6: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 6."""
        cos_7: OnOff = field(XmpByte())
        """coded bytes, indicating whether PFC response is enabled for that CoS 7."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the port responds to incoming Ethernet Priority Flow Control (PFC) frames.

        :return: whether PFC response is enabled for CoS 0, Cos 1, Cos 2, Cos 3, Cos 4, Cos 5, Cos 6, and Cos 7
        :rtype: P_PFCENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, cos_0: OnOff, cos_1: OnOff, cos_2: OnOff, cos_3: OnOff, cos_4: OnOff, cos_5: OnOff, cos_6: OnOff, cos_7: OnOff) -> Token[None]:
        """Set whether the port responds to incoming Ethernet Priority Flow Control (PFC) frames.

        :param cos_0: whether PFC response is enabled for CoS 0
        :type cos_0: OnOff
        :param cos_1: whether PFC response is enabled for CoS 1
        :type cos_1: OnOff
        :param cos_2: whether PFC response is enabled for CoS 2
        :type cos_2: OnOff
        :param cos_3: whether PFC response is enabled for CoS 3
        :type cos_3: OnOff
        :param cos_4: whether PFC response is enabled for CoS 4
        :type cos_4: OnOff
        :param cos_5: whether PFC response is enabled for CoS 5
        :type cos_5: OnOff
        :param cos_6: whether PFC response is enabled for CoS 6
        :type cos_6: OnOff
        :param cos_7: whether PFC response is enabled for CoS 7
        :type cos_7: OnOff
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                cos_0=cos_0,
                cos_1=cos_1,
                cos_2=cos_2,
                cos_3=cos_3,
                cos_4=cos_4,
                cos_5=cos_5,
                cos_6=cos_6,
                cos_7=cos_7
            )
        )


@register_command
@dataclass
class P_TXBURSTPERIOD:
    """
    In Burst TX mode this command defines the time from the start of one sequence of
    bursts (from a number of streams) to the start of next sequence of bursts. NB:
    Only used when Port TX Mode is "BURST".
    """

    code: typing.ClassVar[int] = 377
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        burst_period: int = field(XmpLong())
        """integer, burst period expressed in microseconds."""

    class SetDataAttr(RequestBodyStruct):
        burst_period: int = field(XmpLong())
        """integer, burst period expressed in microseconds."""

    def get(self) -> Token[GetDataAttr]:
        """Get the duration in microseconds from the start of one sequence of bursts (from a number of streams) to the start of next sequence of bursts in Burst TX mode.

        :return: the duration in microseconds from the start of one sequence of bursts (from a number of streams) to the start of next sequence of bursts
        :rtype: P_TXBURSTPERIOD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, burst_period: int) -> Token[None]:
        """Set the duration in microseconds from the start of one sequence of bursts (from a number of streams) to the start of next sequence of bursts in Burst TX mode.

        :param burst_period: the duration in microseconds from the start of one sequence of bursts
            (from a number of streams) to the start of next sequence of bursts in Burst TX mode
        :type burst_period: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, burst_period=burst_period))


@register_command
@dataclass
class P_TXRUNTLENGTH:
    """
    Enable TX runt feature to cut all packets to a number of bytes.
    """

    code: typing.ClassVar[int] = 390
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        runt_length: int = field(XmpInt())
        """integer, enable TX runt feature to cut all packets to I bytes. Set to -1 to disable."""

    class SetDataAttr(RequestBodyStruct):
        runt_length: int = field(XmpInt())
        """integer, enable TX runt feature to cut all packets to I bytes. Set to -1 to disable."""

    def get(self) -> Token[GetDataAttr]:
        """Get the TX runt feature to cut all packets to I bytes. -1 means disabled.

        :return: the TX runt feature to cut all packets to I bytes
        :rtype: P_TXRUNTLENGTH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, runt_length: int) -> Token[None]:
        """Set TX runt feature to cut all packets to I bytes. Set to -1 to disable.

        :param runt_length: enable TX runt feature to cut all packets to I bytes. Set to -1 to disable.
        :type runt_length: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, runt_length=runt_length))


@register_command
@dataclass
class P_RXRUNTLENGTH:
    """
    Enable RX runt length detection to flag if packets are seen with length not being I bytes.
    """

    code: typing.ClassVar[int] = 391
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        runt_length: int = field(XmpInt())
        """integer, enable RX runt length detection to flag if packets are seen with length not being I bytes. Set to -1 to disabled."""

    class SetDataAttr(RequestBodyStruct):
        runt_length: int = field(XmpInt())
        """integer, enable RX runt length detection to flag if packets are seen with length not being I bytes. Set to -1 to disabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get RX runt length detection to flag if packets are seen with length not being I bytes. -1 means disabled.

        :return: RX runt length detection to flag if packets are seen with length not being I bytes. -1 means disabled
        :rtype: P_RXRUNTLENGTH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, runt_length: int) -> Token[None]:
        """Set RX runt length detection to flag if packets are seen with length not being I bytes. Set to -1 to disabled.

        :param runt_length: RX runt length detection to flag if packets are seen with length not being I bytes. Set to -1 to disabled.
        :type runt_length: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, runt_length=runt_length))


@register_command
@dataclass
class P_RXRUNTLEN_ERRS:
    """
    Sticky clear on read: Have packets with wrong runt length been detected since last read?
    """

    code: typing.ClassVar[int] = 392
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        status: YesNo = field(XmpInt())
        """coded integer, have packets with wrong runt length been detected since last read?"""

    def get(self) -> Token[GetDataAttr]:
        """Have packets with wrong runt length been detected since last read?

        :return: whether packets with wrong runt length been detected since last read
        :rtype: P_RXRUNTLEN_ERRS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_TXPREAMBLE_REMOVE:
    """
    Remove preamble from outgoing frames.
    """

    code: typing.ClassVar[int] = 393
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, remove preamble from outgoing frames."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, remove preamble from outgoing frames."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the preambles from outgoing frames are to be removed by the port.

        :return: whether the preambles from outgoing frames are to be removed by the port
        :rtype: P_TXPREAMBLE_REMOVE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether the preambles from outgoing frames are to be removed by the port.

        :param on_off: whether the preambles from outgoing frames are to be removed by the port
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable frame preamble removal on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable frame preamble removal on the port.
    """


@register_command
@dataclass
class P_RXPREAMBLE_INSERT:
    """
    Insert preambles to the incoming frames.
    """

    code: typing.ClassVar[int] = 394
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, insert preamble to incoming frames."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, insert preamble to incoming frames."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the port should insert preambles to the incoming frames.

        :return: whether the port should insert preambles to the incoming frames
        :rtype: P_RXPREAMBLE_INSERT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether the port should insert preambles to the incoming frames.

        :param on_off: whether the port should insert preambles to the incoming frames
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable frame preamble insertion on the port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable frame preamble insertion on the port.
    """


@register_command
@dataclass
class P_LOADMODE:
    """
    The action determines if config load mode is enabled or disabled for the Chimera port.
    """

    code: typing.ClassVar[int] = 395
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, specifying whether the config load function is enabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, specifying whether the config load function is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of config load mode of the Chimera port.

        :return: the status of config load mode on the Chimera port
        :rtype: P_LOADMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the status of config load mode of the Chimera port.

        :param on_off: whether config load is enabled on the Chimera port
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable config load on the Chimera port.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable config load on the Chimera port.
    """


@register_command
@dataclass
class P_SPEEDS_SUPPORTED:
    """
    Read the speeds supported by the port. The speeds supported by a port depends on
    the transceiver inserted into the port. A series of 0/1 values, identifying
    which speeds are supported by the port.

    .. note::

        Ports can support zero (in case of e.g. empty cage), one, or multiple speeds.

    """

    code: typing.ClassVar[int] = 396
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        auto: int = field(XmpByte())
        """auto-negotiated speed, the actual speed depends on the negotiation result."""
        f10M: int = field(XmpByte())
        """10 Mbps."""
        f100M: int = field(XmpByte())
        """100 Mbps."""
        f1G: int = field(XmpByte())
        """1 Gbps."""
        f10G: int = field(XmpByte())
        """10 Gbps."""
        f40G: int = field(XmpByte())
        """40 Gbps."""
        f100G: int = field(XmpByte())
        """100 Gbps."""
        f10MHDX: int = field(XmpByte())
        """10 Mbps half duplex."""
        f100MHDX: int = field(XmpByte())
        """100 Mbps half duplex."""
        f10M100M: int = field(XmpByte())
        """10/100 Mbps."""
        f100M1G: int = field(XmpByte())
        """100/1000 Mbps."""
        f100M1G10G: int = field(XmpByte())
        """100/1000/10000 Mbps."""
        f2500M: int = field(XmpByte())
        """2500 Mbps."""
        f5G: int = field(XmpByte())
        """5 Gbps."""
        f100M1G2500M: int = field(XmpByte())
        """100/1000/2500 Mbps."""
        f25G: int = field(XmpByte())
        """25 Gbps."""
        f50G: int = field(XmpByte())
        """50 Gbps."""
        f200G: int = field(XmpByte())
        """200 Gbps."""
        f400G: int = field(XmpByte())
        """400 Gbps."""
        f800G: int = field(XmpByte())
        """800 Gbps."""
        f1600G: int = field(XmpByte())
        """1600 Gbps."""

    def get(self) -> Token[GetDataAttr]:
        """Get the speeds supported by the port.

        :return: the speeds supported by the port
        :rtype: P_SPEEDS_SUPPORTED.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_BRRSTATUS:
    """
    Get the actual BroadR-Reach status of the port.
    """

    code: typing.ClassVar[int] = 460
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: BRRMode = field(XmpByte())
        """coded byte, the port’s actual BroadR-Reach mode."""

    def get(self) -> Token[GetDataAttr]:
        """Get the actual BroadR-Reach status of the port.

        :return: the actual BroadR-Reach status of the port.
        :rtype: P_BRRSTATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class P_EMULATE:
    """
    The action determines if emulation functionality is enabled or disabled
    """

    code: typing.ClassVar[int] = 1600
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        action: OnOff = field(XmpByte())
        """coded byte, specifying whether the emulate function is enabled."""

    class SetDataAttr(RequestBodyStruct):
        action: OnOff = field(XmpByte())
        """coded byte, specifying whether the emulate function is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the Chimera port's emulation functionality is enabled.

        :return: whether the Chimera port's emulation functionality is enabled
        :rtype: P_EMULATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, action: OnOff) -> Token[None]:
        """Set whether the Chimera port's emulation functionality is enabled.

        :param action: whether the Chimera port's emulation functionality is enabled
        :type action: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, action=action))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the Chimera port's emulation functionality.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the Chimera port's emulation functionality.
    """


@register_command
@dataclass
class P_MACSEC_TXSC_CREATE:
    """
    Create a TX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 505
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Create a TX Secure Channel (SC) on the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))
    

@register_command
@dataclass
class P_MACSEC_TXSC_INDICES:
    """
    Create multiple TX SCs or query the existing TX SCs on the port.
    """

    code: typing.ClassVar[int] = 506
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        txsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of TX SCs on the port."""

    class SetDataAttr(RequestBodyStruct):
        txsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of TX SCs on the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the full list of which TX SCs are defined for a port.

        :return: the sub-indices of TX SCs on the port
        :rtype: P_MACSEC_TXSC_INDICES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, txsc_indices: typing.List[int]) -> Token[None]:
        """Creates a new empty TX SC for each value that is not already in use, and deletes each TX SC that is not mentioned in the list.

        :param txsc_indices: the sub-indices of TX SCs on the port
        :type txsc_indices: typing.List[int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, txsc_indices=txsc_indices))


@register_command
@dataclass
class P_MACSEC_TXSC_DELETE:
    """
    Delete a TX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 530
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Delete a TX Secure Channel (SC) on the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))


@register_command
@dataclass
class P_MACSEC_TXSC_CONF_OFFSET:
    """
    The confidentiality offset of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 510
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        offset: int = field(XmpInt())
        """integer, the TX Secure Channel (SC) offset. Allowed values are 0, 30, and 50"""

    class SetDataAttr(RequestBodyStruct):
        offset: int = field(XmpInt())
        """integer, the TX Secure Channel (SC) offset. Allowed values are 0, 30, and 50"""

    def get(self) -> Token[GetDataAttr]:
        """Get the TX Secure Channel (SC) offset on the port.

        :return: the TX Secure Channel (SC) offset on the port
        :rtype: P_MACSEC_TXSC_CONF_OFFSET.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, offset: int) -> Token[None]:
        """Set the TX Secure Channel (SC) offset on the port.

        :param offset: the TX Secure Channel (SC) offset
        :type offset: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], offset=offset))
    

@register_command
@dataclass
class P_MACSEC_TXSC_DESCR:
    """
    The description of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 507
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the TX Secure Channel (SC)."""

    class SetDataAttr(RequestBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the TX Secure Channel (SC)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the description of the TX Secure Channel (SC) on the port.

        :return: the description of the TX Secure Channel (SC) on the port
        :rtype: P_MACSEC_TXSC_DESCR.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, description: str) -> Token[None]:
        """Set the description of the TX Secure Channel (SC) on the port.

        :param description: the description of the TX Secure Channel (SC)
        :type description: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], description=description))
    

@register_command
@dataclass
class P_MACSEC_TXSC_SCI_MODE:
    """
    The mode of the port’s TX SCI in MACsec.

    """

    code: typing.ClassVar[int] = 513
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        mode: MACSecSCIMode = field(XmpByte())
        """coded byte, the mode of the port’s TX SCI in MACsec."""

    class SetDataAttr(RequestBodyStruct):
        mode: MACSecSCIMode = field(XmpByte())
        """coded byte, the mode of the port’s TX SCI in MACsec."""

    def get(self) -> Token[GetDataAttr]:
        """Get the mode of the port’s TX SCI in MACsec.

        :return: the mode of the port’s TX SCI in MACsec.
        :rtype: P_MACSEC_TXSC_SCI_MODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, mode: MACSecSCIMode) -> Token[None]:
        """Set the mode of the port’s TX SCI in MACsec.

        :param mode: the mode of the port’s TX SCI in MACsec.
        :type mode: MACSecSCIMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode))

    set_no_sci = functools.partialmethod(set, MACSecSCIMode.NO_SCI)
    """Set SCI Mode to NO SCI.
    """

    set_with_sci = functools.partialmethod(set, MACSecSCIMode.WITH_SCI)
    """Set SCI Mode to WITH SCI.
    """


@register_command
@dataclass
class P_MACSEC_TXSC_SCI:
    """
    The SCI of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 508
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s TX SC."""

    class SetDataAttr(RequestBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s TX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SCI of the port’s TX SC.

        :return: the SCI of the port’s TX SC.
        :rtype: P_MACSEC_TXSC_SCI.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, sci: Hex) -> Token[None]:
        """Set the SCI of the port’s TX SC.

        :param sci: The SCI of the port’s TX SC.
        :type sci: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], sci=sci))
    

@register_command
@dataclass
class P_MACSEC_TXSC_CIPHERSUITE:
    """
    The cipher suite of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 509
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s TX SC."""

    class SetDataAttr(RequestBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s TX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the cipher suite of the port’s TX SC.

        :return: the cipher suite of the port’s TX SC.
        :rtype: P_MACSEC_TXSC_CIPHERSUITE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, cipher_suite: MACSecCipherSuite) -> Token[None]:
        """Set the cipher suite of the port’s TX SC.

        :param cipher_suite: the cipher suite of the port’s TX SC.
        :type cipher_suite: MACSecCipherSuite
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], cipher_suite=cipher_suite))

    set_gcm_aes_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_128)
    """Set cipher suite to GCM_AES_128.
    """

    set_gcm_aes_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_256)
    """Set cipher suite to GCM_AES_256.
    """

    set_gcm_aes_xpn_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_128)
    """Set cipher suite to GCM_AES_XPN_128.
    """

    set_gcm_aes_xpn_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_256)
    """Set cipher suite to GCM_AES_XPN_256.
    """


@register_command
@dataclass
class P_MACSEC_TXSC_STARTING_PN:
    """
    The starting PN number of the port’s TX SC uses.
    """

    code: typing.ClassVar[int] = 514
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        start: int = field(XmpLong())
        """integer, the starting PN number. Default to 1, maximum 2^64. Allowed to be 0."""

        mode: MACSecPNMode = field(XmpByte())
        """byte, defining how to continue the TX PN after the start-traffic. Default to CONTINUOUS."""

    class SetDataAttr(RequestBodyStruct):
        start: int = field(XmpLong())
        """integer, the starting PN number. Default to 1, maximum 2^64. Allowed to be 0."""

        mode: MACSecPNMode = field(XmpByte())
        """byte, defining how to continue the TX PN after the start-traffic. Default to CONTINUOUS."""

    def get(self) -> Token[GetDataAttr]:
        """Get the starting PN number. Default to 1, maximum 2^64. Allowed to be 0.

        :return: the starting PN number. Default to 1, maximum 2^64.
        :rtype: P_MACSEC_TXSC_STARTING_PN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, start: int, mode: MACSecPNMode) -> Token[None]:
        """Set the starting PN number. Default to 1, maximum 2^64. Allowed to be 0.

        :param start: the starting PN number. Default to 1, maximum 2^64.
        :type start: int
        :param mode: defining how to continue the TX PN after the start-traffic.
        :type mode: MACSecPNMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], start=start, mode=mode))
    

# @register_command
# @dataclass
# class P_MACSEC_TXSC_VLAN_MODE:
#     """
#     The VLAN mode of the port’s TX SC.
    
#         * VLAN encrypted: The original MACsec header format encoded the 802.1Q tag as part of the encrypted payload, thus hiding it from the public Ethernet transport.
        
#         * VLAN in clear text (WAN MACsec): With 802.1Q tag in the clear, the 802.1Q tag is encoded outside the 802.1AE encryption header, exposing the tag to the private and public Ethernet transport.

#     """

#     code: typing.ClassVar[int] = 511
#     pushed: typing.ClassVar[bool] = False

#     _connection: 'interfaces.IConnection'
#     _module: int
#     _port: int
#     _txsc_index: int

#     class GetDataAttr(ResponseBodyStruct):
#         mode: MACSecVLANMode = field(XmpByte())
#         """integer, the VLAN mode. Default to ENCRYPTED."""

#     class SetDataAttr(RequestBodyStruct):
#         mode: MACSecVLANMode = field(XmpByte())
#         """integer, the VLAN mode. Default to ENCRYPTEDC."""

#     def get(self) -> Token[GetDataAttr]:
#         """Get the VLAN mode.

#         :return: the VLAN mode.
#         :rtype: P_MACSEC_TXSC_VLAN_MODE.GetDataAttr
#         """
#         return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

#     def set(self, mode: MACSecVLANMode) -> Token[None]:
#         """Set the VLAN mode.

#         :param mode: the VLAN mode.
#         :type mode: MACSecVLANMode
#         """
#         return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode))
    
#     set_encrypted = functools.partialmethod(set, MACSecVLANMode.ENCRYPTED)
#     """Set VLAN mode to ENCRYPTED.
#     """

#     set_clear_text = functools.partialmethod(set, MACSecVLANMode.CLEAR_TEXT)
#     """Set VLAN mode to CLEAR_TEXT.
#     """


@register_command
@dataclass
class P_MACSEC_TXSC_REKEY_MODE:
    """
    The rekey mode of the port’s TX SC defines when to switch to the next SAK.
    """

    code: typing.ClassVar[int] = 515
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        mode: MACSecRekeyMode = field(XmpByte())
        """byte, the rekey mode of the port’s TX SC"""

        value: int = field(XmpInt())
        """integer, defines the packet count. This value will be ignored if the mode is set to PN_EXHAUSTION"""

    class SetDataAttr(RequestBodyStruct):
        mode: MACSecRekeyMode = field(XmpByte())
        """byte, the rekey mode of the port’s TX SC"""

        value: int = field(XmpInt())
        """integer, defines the packet count. This value will be ignored if the mode is set to PN_EXHAUSTION"""

    def get(self) -> Token[GetDataAttr]:
        """Get the rekey mode of the port’s TX SC

        :return: the rekey mode of the port’s TX SC
        :rtype: P_MACSEC_TXSC_REKEY_MODE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, mode: MACSecRekeyMode, value: int) -> Token[None]:
        """Set the rekey mode.

        :param mode: the rekey mode.
        :type mode: MACSecRekeyMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode, value=value))


@register_command
@dataclass
class P_MACSEC_TXSC_ENCRYPT:
    """
    The encryption mode of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 512
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        mode: MACSecEncryptionMode = field(XmpByte())
        """byte, the encryption mode of the port’s TX SC"""

    class SetDataAttr(RequestBodyStruct):
        mode: MACSecEncryptionMode = field(XmpByte())
        """byte, the encryption mode of the port’s TX SC"""

    def get(self) -> Token[GetDataAttr]:
        """Get the encryption mode of the port’s TX SC

        :return: the encryption mode of the port’s TX SC
        :rtype: P_MACSEC_TXSC_ENCRYPT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, mode: MACSecEncryptionMode) -> Token[None]:
        """Set the encryption mode.

        :param mode: the encryption mode.
        :type mode: MACSecEncryptionMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode))
    
    set_encrypt_integrity = functools.partialmethod(set, MACSecEncryptionMode.ENCRYPT_INTEGRITY)
    """Set encryption mode to encryption and integrity.
    """

    set_integrity_only = functools.partialmethod(set, MACSecEncryptionMode.INTEGRITY_ONLY)
    """Set encryption mode to integrity only.
    """

@register_command
@dataclass
class P_MACSEC_TXSC_SAK_VALUE:
    """
    Configure the value of a SAK key on the port’s TX SC.
    """

    code: typing.ClassVar[int] = 534
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int
    _sak_key_index: int

    class GetDataAttr(ResponseBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    class SetDataAttr(RequestBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SAK key.

        :return: the the SAK key.
        :rtype: P_MACSEC_TXSC_SAK_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index, self._sak_key_index]))

    def set(self, sak_key_value: Hex) -> Token[None]:
        """Set the SAK key.

        :param sak_key_value: the SAK key.
        :type sak_key_value: Hex
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index, self._sak_key_index], sak_key_value=sak_key_value))
    


@register_command
@dataclass
class P_MACSEC_RXSC_CREATE:
    """
    Create a RX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 518
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Create a RX Secure Channel (SC) on the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))
    

@register_command
@dataclass
class P_MACSEC_RXSC_INDICES:
    """
    Create multiple RX SCs or query the existing RX SCs on the port.
    """

    code: typing.ClassVar[int] = 519
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        rxsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of RX SCs on the port."""

    class SetDataAttr(RequestBodyStruct):
        rxsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of RX SCs on the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the full list of which RX SCs are defined for a port.

        :return: the sub-indices of RX SCs on the port
        :rtype: P_MACSEC_RXSC_INDICES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, rxsc_indices: typing.List[int]) -> Token[None]:
        """Creates a new empty RX SC for each value that is not already in use, and deletes each RX SC that is not mentioned in the list.

        :param rxsc_indices: the sub-indices of RX SCs on the port
        :type rxsc_indices: typing.List[int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, rxsc_indices=rxsc_indices))
    

@register_command
@dataclass
class P_MACSEC_RXSC_DELETE:
    """
    Delete a RX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 531
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Delete a RX Secure Channel (SC) on the port.
        """
        
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))
    

@register_command
@dataclass
class P_MACSEC_RXSC_DESCR:
    """
    The description of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 520
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the RX Secure Channel (SC)."""

    class SetDataAttr(RequestBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the RX Secure Channel (SC)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the description of the RX Secure Channel (SC) on the port.

        :return: the description of the RX Secure Channel (SC) on the port
        :rtype: P_MACSEC_RXSC_DESCR.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, description: str) -> Token[None]:
        """Set the description of the RX Secure Channel (SC) on the port.

        :param description: the description of the RX Secure Channel (SC)
        :type description: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], description=description))
    

@register_command
@dataclass
class P_MACSEC_RXSC_SCI:
    """
    The SCI of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 523
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s RX SC."""

    class SetDataAttr(RequestBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s RX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SCI of the port’s RX SC.

        :return: the SCI of the port’s RX SC.
        :rtype: P_MACSEC_RXSC_SCI.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, sci: Hex) -> Token[None]:
        """Set the SCI of the port’s RX SC.

        :param sci: The SCI of the port’s RX SC.
        :type sci: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], sci=sci))
    

@register_command
@dataclass
class P_MACSEC_RXSC_CONF_OFFSET:
    """
    The confidentiality offset of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 522
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        offset: int = field(XmpInt())
        """integer, the RX Secure Channel (SC) offset. Allowed values are 0, 30, and 50."""

    class SetDataAttr(RequestBodyStruct):
        offset: int = field(XmpInt())
        """integer, the RX Secure Channel (SC) offset. Allowed values are 0, 30, and 50"""

    def get(self) -> Token[GetDataAttr]:
        """Get the RX Secure Channel (SC) offset on the port.

        :return: the RX Secure Channel (SC) offset on the port
        :rtype: P_MACSEC_RXSC_CONF_OFFSET.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, offset: int) -> Token[None]:
        """Set the RX Secure Channel (SC) offset on the port.

        :param offset: the RX Secure Channel (SC) offset
        :type offset: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], offset=offset))
    

@register_command
@dataclass
class P_MACSEC_RXSC_CIPHERSUITE:
    """
    The cipher suite of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 521
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s RX SC."""

    class SetDataAttr(RequestBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s RX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the cipher suite of the port’s RX SC.

        :return: the cipher suite of the port’s RX SC.
        :rtype: P_MACSEC_RXSC_CIPHERSUITE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, cipher_suite: MACSecCipherSuite) -> Token[None]:
        """Set the cipher suite of the port’s RX SC.

        :param cipher_suite: the cipher suite of the port’s RX SC.
        :type cipher_suite: MACSecCipherSuite
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], cipher_suite=cipher_suite))

    set_gcm_aes_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_128)
    """Set cipher suite to GCM_AES_128.
    """

    set_gcm_aes_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_256)
    """Set cipher suite to GCM_AES_256.
    """

    set_gcm_aes_xpn_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_128)
    """Set cipher suite to GCM_AES_XPN_128.
    """

    set_gcm_aes_xpn_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_256)
    """Set cipher suite to GCM_AES_XPN_256.
    """

@register_command
@dataclass
class P_MACSEC_RXSC_STARTING_PN:
    """
    The first PN number of the port’s RX SC expects to receive.
    """

    code: typing.ClassVar[int] = 511
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        value: int = field(XmpLong())
        """integer, The first PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""

    class SetDataAttr(RequestBodyStruct):
        value: int = field(XmpLong())
        """integer, The first PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""

    def get(self) -> Token[GetDataAttr]:
        """Get the first PN number of the port’s RX SC expects to receive

        :return: the first PN number of the port’s RX SC expects to receive
        :rtype: P_MACSEC_RXSC_STARTING_PN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, value: int) -> Token[None]:
        """Set the first PN number of the port’s RX SC expects to receive

        :param start: The first PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64.
        :type start: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], value=value))


@register_command
@dataclass
class P_MACSEC_RXSC_TPLDID:
    """
    Associate a TPLD ID with the RX SC.
    """

    code: typing.ClassVar[int] = 535
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        tpld_id: int = field(XmpInt())
        """integer, the TPLD ID to associate with the RX SC."""

    class SetDataAttr(RequestBodyStruct):
        tpld_id: int = field(XmpInt())
        """integer, the TPLD ID to associate with the RX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the TPLD ID to associate with the RX SC.

        :return: the TPLD ID to associate with the RX SC.
        :rtype: P_MACSEC_RXSC_TPLDID.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, tpld_id: int) -> Token[None]:
        """Set the TPLD ID to associate with the RX SC.

        :param tpld_id: the TPLD ID to associate with the RX SC.
        :type tpld_id: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], tpld_id=tpld_id))
    

@register_command
@dataclass
class P_MACSEC_RXSC_SAK_VALUE:
    """
    Configure the value of a SAK key on the port’s RX SC.
    """

    code: typing.ClassVar[int] = 542
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int
    _sak_key_index: int

    class GetDataAttr(ResponseBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    class SetDataAttr(RequestBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SAK key.

        :return: the the SAK key.
        :rtype: P_MACSEC_RXSC_SAK_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index, self._sak_key_index]))

    def set(self, sak_key_value: Hex) -> Token[None]:
        """Set the SAK key.

        :param sak_key_value: the SAK key.
        :type sak_key_value: Hex
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index, self._sak_key_index], sak_key_value=sak_key_value))
    


@register_command
@dataclass
class P_MACSEC_TX_STATS:
    """
    Port-level MACsec TX counters
    """

    code: typing.ClassVar[int] = 517
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted since last cleared."""
        total_protected_only_bits: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bits transmitted by the port since cleared."""
        total_protected_only_bytes: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bytes transmitted by the port since cleared."""
        total_encrypted_bits: int = field(XmpLong())
        """long integer, the number of encrypted bits transmitted by the port since cleared, excluding the bytes in the Confidentiality Offset."""
        total_encrypted_bytes: int = field(XmpLong())
        """long integer, the number of encrypted bytes transmitted by the port since cleared, excluding the bytes in the Confidentiality Offset."""


    def get(self) -> Token[GetDataAttr]:
        """Get port-level MACsec TX counters

        :return: port-level MACsec TX counters
        :rtype: P_MACSEC_TX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class P_MACSEC_TXSC_STATS:
    """
    SC/stream-level MACsec TX counters.
    """

    code: typing.ClassVar[int] = 528
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted since last cleared."""
        total_protected_only_bits: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bits transmitted since cleared."""
        total_protected_only_bytes: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bytes transmitted since cleared."""
        total_encrypted_bits: int = field(XmpLong())
        """long integer, the number of encrypted bits transmitted since cleared, excluding the bytes in the Confidentiality Offset."""
        total_encrypted_bytes: int = field(XmpLong())
        """long integer, the number of encrypted bytes transmitted since cleared, excluding the bytes in the Confidentiality Offset."""


    def get(self) -> Token[GetDataAttr]:
        """Get SC/stream-level MACsec TX counters.

        :return: SC/stream-level MACsec TX counters.
        :rtype: P_MACSEC_TXSC_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))
    

@register_command
@dataclass
class P_MACSEC_TX_CLEAR:
    """
    Clear the MACsec TX counters of the port.
    """

    code: typing.ClassVar[int] = 516
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Clear the MACsec TX counters of the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))
    


@register_command
@dataclass
class P_MACSEC_RX_STATS:
    """
    Port-level MACsec RX counters
    """

    code: typing.ClassVar[int] = 525
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, number of MACsec frames received of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, number of MACsec frames received since last cleared."""
        total_ok_frames: int = field(XmpLong())
        """long integer, the number of good MACsec frames received since cleared."""
        total_delayed_frames: int = field(XmpLong())
        """long integer, the number of frames with the PN lower than the minmum expected since cleared."""
        total_icv_check_failed_frames: int = field(XmpLong())
        """long integer, the number of frames with ICV check failed recevied since cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get port-level MACsec RX counters

        :return: port-level MACsec RX counters
        :rtype: P_MACSEC_RX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class P_MACSEC_RXSC_STATS:
    """
    SC/stream-level MACsec RX counters
    """

    code: typing.ClassVar[int] = 529
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, number of MACsec frames received of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, number of MACsec frames received since last cleared."""
        total_ok_frames: int = field(XmpLong())
        """long integer, the number of good MACsec frames received since cleared."""
        total_delayed_frames: int = field(XmpLong())
        """long integer, the number of frames with the PN lower than the minmum expected since cleared."""
        total_icv_check_failed_frames: int = field(XmpLong())
        """long integer, the number of frames with ICV check failed recevied since cleared."""


    def get(self) -> Token[GetDataAttr]:
        """Get port-level MACsec RX counters

        :return: port-level MACsec RX counters
        :rtype: P_MACSEC_RX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))
    

@register_command
@dataclass
class P_MACSEC_RX_CLEAR:
    """
    Clear the MACsec RX counters of the port.
    """

    code: typing.ClassVar[int] = 524
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Clear the MACsec RX counters of the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class P_MACSEC_RX_ENABLE:
    """
    This will enable/disable the MACSec functionality on the RX side. With it ON, the RX port will try to decode the received packets. If it is OFF, the port will not try to decode any received packets.
    """

    code: typing.ClassVar[int] = 545
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, enable or disable MACsec on the RX port."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, enable or disable MACsec on the RX port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the RX port MACSec state.

        :return: the RX port MACSec stat
        :rtype: PS_MACSEC_ENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the RX port MACSec stat.

        :param on_off: the RX port MACSec stat
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the RX port MACSec.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the RX port MACSec.
    """