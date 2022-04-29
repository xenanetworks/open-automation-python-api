from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4G_CLEAR_POST_STAT,
    P4G_TCP_RTT_VALUE,
    P4G_TCP_STATE_CURRENT,
    P4G_TCP_STATE_TOTAL,
    P4G_TCP_STATE_RATE,
    P4G_TCP_RX_PAYLOAD_COUNTERS,
    P4G_TCP_TX_PAYLOAD_COUNTERS,
    P4G_TCP_RETRANSMIT_COUNTERS,
    P4G_TCP_ERROR_COUNTERS,
    P4G_TCP_MSS_TYPE,
    P4G_TCP_MSS_MINMAX,
    P4G_TCP_MSS_VALUE,
    P4G_TCP_WINDOW_SIZE,
    P4G_TCP_DUP_THRES,
    P4G_TCP_SYN_RTO,
    P4G_TCP_RTO,
    P4G_TCP_CONGESTION_MODE,
    P4G_TCP_WINDOW_SCALING,
    P4G_TCP_RTO_MINMAX,
    P4G_TCP_RTO_PROLONGED_MODE,
    P4G_TCP_ICWND_CALC_METHOD,
    P4G_TCP_ISSTHRESH,
    P4G_TCP_ACK_FREQUENCY,
    P4G_TCP_ACK_TIMEOUT,
    P4G_TCP_ESTABLISH_HIST,
    P4G_TCP_CLOSE_HIST,
    P4G_TCP_RX_TOTAL_BYTES_HIST,
    P4G_TCP_RX_GOOD_BYTES_HIST,
    P4G_TCP_TX_TOTAL_BYTES_HIST,
    P4G_TCP_TX_GOOD_BYTES_HIST,
    P4G_TCP_RX_PACKET_COUNTERS,
    P4G_TCP_TX_PACKET_COUNTERS,
)

class GAckTcp:
    """TCP ACK configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.duplicate_tresholds = P4G_TCP_DUP_THRES(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_DUP_THRES`
        """
        self.frequency = P4G_TCP_ACK_FREQUENCY(conn, module_id, port_id, group_idx) # TODO: probably need a better name to be closer to cmd description
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ACK_FREQUENCY`
        """
        self.timeout = P4G_TCP_ACK_TIMEOUT(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ACK_TIMEOUT`
        """

class GRetransmitionTimeoutTcp:
    """TCP Retransmition Timeout configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.syn_value = P4G_TCP_SYN_RTO(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_SYN_RTO`
        """
        self.value = P4G_TCP_RTO(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RTO`
        """
        self.range_limits = P4G_TCP_RTO_MINMAX(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RTO_MINMAX`
        """
        self.prolonged_mode = P4G_TCP_RTO_PROLONGED_MODE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RTO_PROLONGED_MODE`
        """

class GStateCountersTcp:
    """TCP State counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.current = P4G_TCP_STATE_CURRENT(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_STATE_CURRENT`
        """
        self.total = P4G_TCP_STATE_TOTAL(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_STATE_TOTAL`
        """
        self.rate = P4G_TCP_STATE_RATE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_STATE_RATE`
        """


class GMaxSegmentSize:
    """TCP Max Segment Size Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.type = P4G_TCP_MSS_TYPE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_MSS_TYPE`
        """
        self.range_limits = P4G_TCP_MSS_MINMAX(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_MSS_MINMAX`
        """
        self.fixed_value = P4G_TCP_MSS_VALUE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_MSS_VALUE`
        """


class GPacketCountersTcp:
    """TCP Packet Counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_TCP_RX_PACKET_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_PACKET_COUNTERS`
        """
        self.tx = P4G_TCP_TX_PACKET_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_PACKET_COUNTERS`
        """


class GPayloadCountersTcp:
    """TCP Payload Counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_TCP_RX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_PAYLOAD_COUNTERS`
        """
        self.tx = P4G_TCP_TX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_PAYLOAD_COUNTERS`
        """


class GCountersTcp:
    """TCP counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.retransmission = P4G_TCP_RETRANSMIT_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RETRANSMIT_COUNTERS`
        """
        self.error = P4G_TCP_ERROR_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ERROR_COUNTERS`
        """
        self.packet = GPacketCountersTcp(conn, module_id, port_id, group_idx)
        """Packet counters"""
        self.payload = GPayloadCountersTcp(conn, module_id, port_id, group_idx)
        """Payload counters"""
        self.state = GStateCountersTcp(conn, module_id, port_id, group_idx)
        """State counters"""


class GRxHistogramTcp:
    """TCP RX Histogram"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.total_bytes = P4G_TCP_RX_TOTAL_BYTES_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_TOTAL_BYTES_HIST`
        """
        self.good_bytes = P4G_TCP_RX_GOOD_BYTES_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_GOOD_BYTES_HIST`
        """


class GTxHistogramTcp:
    """TCP TX Histogram"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.total_bytes = P4G_TCP_TX_TOTAL_BYTES_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_TOTAL_BYTES_HIST`
        """
        self.good_bytes = P4G_TCP_TX_GOOD_BYTES_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_GOOD_BYTES_HIST`
        """


class GConnHistogramTcp:
    """TCP Connection Histogram"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.establish_times = P4G_TCP_ESTABLISH_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ESTABLISH_HIST`
        """
        self.close_times = P4G_TCP_CLOSE_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_CLOSE_HIST`
        """


class GHistogramTcp:
    """TCP histogram"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.connection = GConnHistogramTcp(conn, module_id, port_id, group_idx)
        """TCP Connection Histogram"""
        self.rx = GRxHistogramTcp(conn, module_id, port_id, group_idx)
        """TCP RX Histogram"""
        self.tx = GTxHistogramTcp(conn, module_id, port_id, group_idx)
        """TCP TX Histogram"""


class GReceiverWindowTcp:
    """TCP RWND Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.size = P4G_TCP_WINDOW_SIZE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_WINDOW_SIZE`
        """
        self.scaling = P4G_TCP_WINDOW_SCALING(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_WINDOW_SCALING`
        """


class GCongestionWindowTcp:
    """TCP CWND Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.congestion_mode = P4G_TCP_CONGESTION_MODE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_CONGESTION_MODE`
        """
        self.icwnd_calc_method = P4G_TCP_ICWND_CALC_METHOD(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ICWND_CALC_METHOD`
        """
        

class GTcp:
    """TCP Stack Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.clear_post_test_statistics = P4G_CLEAR_POST_STAT(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_CLEAR_POST_STAT`
        """
        self.rtt_value = P4G_TCP_RTT_VALUE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RTT_VALUE`
        """
        self.iss_treshold = P4G_TCP_ISSTHRESH(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ISSTHRESH`
        """
        self.mss = GMaxSegmentSize(conn, module_id, port_id, group_idx)
        """Max segment size config"""
        self.rto = GRetransmitionTimeoutTcp(conn, module_id, port_id, group_idx)
        """Retransmission timeout config"""
        self.ack = GAckTcp(conn, module_id, port_id, group_idx)
        """ACK config"""
        self.rwnd = GReceiverWindowTcp(conn, module_id, port_id, group_idx)
        """RWND config"""
        self.cwnd = GCongestionWindowTcp(conn, module_id, port_id, group_idx)
        """CWND config"""

        self.counters = GCountersTcp(conn, module_id, port_id, group_idx)
        """Counters"""
        self.histogram = GHistogramTcp(conn, module_id, port_id, group_idx)
        """Histogram"""