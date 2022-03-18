from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4G_UDP_PACKET_SIZE_TYPE,
    P4G_UDP_PACKET_SIZE_MINMAX,
    P4G_UDP_PACKET_SIZE_VALUE,
    P4G_UDP_STATE_CURRENT,
    P4G_UDP_STATE_TOTAL,
    P4G_UDP_STATE_RATE,
    P4G_UDP_RX_PAYLOAD_COUNTERS,
    P4G_UDP_TX_PAYLOAD_COUNTERS,
    P4G_UDP_RX_BYTES_HIST,
    P4G_UDP_TX_BYTES_HIST,
    P4G_UDP_RX_PACKET_COUNTERS,
    P4G_UDP_TX_PACKET_COUNTERS,
)

class GHistogramUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx_bytes = P4G_UDP_RX_BYTES_HIST(conn, module_id, port_id, group_idx)
        self.tx_bytes = P4G_UDP_TX_BYTES_HIST(conn, module_id, port_id, group_idx)


class GPayloadCountersUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_UDP_RX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)
        self.tx = P4G_UDP_TX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)


class GPacketCountersUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_UDP_RX_PACKET_COUNTERS(conn, module_id, port_id, group_idx)
        self.tx = P4G_UDP_TX_PACKET_COUNTERS(conn, module_id, port_id, group_idx)


class GCountersUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.payload = GPayloadCountersUdp(conn, module_id, port_id, group_idx)
        self.packet = GPacketCountersUdp(conn, module_id, port_id, group_idx)
        self.state = GStateCountersUdp(conn, module_id, port_id, group_idx)


class GPacketSizeUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.type = P4G_UDP_PACKET_SIZE_TYPE(conn, module_id, port_id, group_idx)
        self.range_limits = P4G_UDP_PACKET_SIZE_MINMAX(conn, module_id, port_id, group_idx)
        self.value = P4G_UDP_PACKET_SIZE_VALUE(conn, module_id, port_id, group_idx)


class GStateCountersUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.current = P4G_UDP_STATE_CURRENT(conn, module_id, port_id, group_idx)
        self.total = P4G_UDP_STATE_TOTAL(conn, module_id, port_id, group_idx)
        self.rate = P4G_UDP_STATE_RATE(conn, module_id, port_id, group_idx)


class GUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.packet_size = GPacketSizeUdp(conn, module_id, port_id, group_idx)
        self.counters = GCountersUdp(conn, module_id, port_id, group_idx)
        self.histogram = GHistogramUdp(conn, module_id, port_id, group_idx)