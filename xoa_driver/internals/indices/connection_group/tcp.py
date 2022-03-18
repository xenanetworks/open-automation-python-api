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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.duplicate_tresholds = P4G_TCP_DUP_THRES(conn, module_id, port_id, group_idx)
        self.frequency = P4G_TCP_ACK_FREQUENCY(conn, module_id, port_id, group_idx) # ToDo: probably need beter name, which more close to cmd description
        self.timeout = P4G_TCP_ACK_TIMEOUT(conn, module_id, port_id, group_idx)

class GRetransmitionTimeoutTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.syn_value = P4G_TCP_SYN_RTO(conn, module_id, port_id, group_idx)
        self.value = P4G_TCP_RTO(conn, module_id, port_id, group_idx)
        self.range_limits = P4G_TCP_RTO_MINMAX(conn, module_id, port_id, group_idx)
        self.prolonged_mode = P4G_TCP_RTO_PROLONGED_MODE(conn, module_id, port_id, group_idx)

class GStateCountersTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.current = P4G_TCP_STATE_CURRENT(conn, module_id, port_id, group_idx)
        self.total = P4G_TCP_STATE_TOTAL(conn, module_id, port_id, group_idx)
        self.rate = P4G_TCP_STATE_RATE(conn, module_id, port_id, group_idx)


class GMaxSegmentSize:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.type = P4G_TCP_MSS_TYPE(conn, module_id, port_id, group_idx)
        self.range_limits = P4G_TCP_MSS_MINMAX(conn, module_id, port_id, group_idx)
        self.fixed_value = P4G_TCP_MSS_VALUE(conn, module_id, port_id, group_idx)


class GPacketCountersTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_TCP_RX_PACKET_COUNTERS(conn, module_id, port_id, group_idx)
        self.tx = P4G_TCP_TX_PACKET_COUNTERS(conn, module_id, port_id, group_idx)


class GPayloadCountersTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_TCP_RX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)
        self.tx = P4G_TCP_TX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)


class GCountersTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.retransmission = P4G_TCP_RETRANSMIT_COUNTERS(conn, module_id, port_id, group_idx)
        self.error = P4G_TCP_ERROR_COUNTERS(conn, module_id, port_id, group_idx)
        self.packet = GPacketCountersTcp(conn, module_id, port_id, group_idx)
        self.payload = GPayloadCountersTcp(conn, module_id, port_id, group_idx)
        self.state = GStateCountersTcp(conn, module_id, port_id, group_idx)


class GRxHistogramTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.total_bytes = P4G_TCP_RX_TOTAL_BYTES_HIST(conn, module_id, port_id, group_idx)
        self.good_bytes = P4G_TCP_RX_GOOD_BYTES_HIST(conn, module_id, port_id, group_idx)


class GTxHistogramTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.total_bytes = P4G_TCP_TX_TOTAL_BYTES_HIST(conn, module_id, port_id, group_idx)
        self.good_bytes = P4G_TCP_TX_GOOD_BYTES_HIST(conn, module_id, port_id, group_idx)


class GConnHistogramTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.establish_times = P4G_TCP_ESTABLISH_HIST(conn, module_id, port_id, group_idx)
        self.close_times = P4G_TCP_CLOSE_HIST(conn, module_id, port_id, group_idx)


class GHistogramTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.connection = GConnHistogramTcp(conn, module_id, port_id, group_idx)
        self.rx = GRxHistogramTcp(conn, module_id, port_id, group_idx)
        self.tx = GTxHistogramTcp(conn, module_id, port_id, group_idx)


class GReceiverWindowTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.size = P4G_TCP_WINDOW_SIZE(conn, module_id, port_id, group_idx)
        self.scaling = P4G_TCP_WINDOW_SCALING(conn, module_id, port_id, group_idx)


class GCongestionWindowTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.congestion_mode = P4G_TCP_CONGESTION_MODE(conn, module_id, port_id, group_idx)
        self.icwnd_calc_method = P4G_TCP_ICWND_CALC_METHOD(conn, module_id, port_id, group_idx)
        

class GTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.clear_post_test_statistics = P4G_CLEAR_POST_STAT(conn, module_id, port_id, group_idx)
        self.rtt_value = P4G_TCP_RTT_VALUE(conn, module_id, port_id, group_idx)
        self.iss_treshold = P4G_TCP_ISSTHRESH(conn, module_id, port_id, group_idx)
        self.mss = GMaxSegmentSize(conn, module_id, port_id, group_idx)
        self.rto = GRetransmitionTimeoutTcp(conn, module_id, port_id, group_idx)
        self.ack = GAckTcp(conn, module_id, port_id, group_idx)
        self.rwnd = GReceiverWindowTcp(conn, module_id, port_id, group_idx)
        self.cwnd = GCongestionWindowTcp(conn, module_id, port_id, group_idx)

        self.counters = GCountersTcp(conn, module_id, port_id, group_idx)
        self.histogram = GHistogramTcp(conn, module_id, port_id, group_idx)