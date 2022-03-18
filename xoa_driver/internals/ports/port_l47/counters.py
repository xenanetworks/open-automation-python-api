from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4_ETH_TX_COUNTERS,
    P4_ETH_RX_COUNTERS,
    P4_PORT_TX_COUNTERS,
    P4_PORT_RX_COUNTERS,
    P4_PORT_COUNTERS,
    P4_IPV4_RX_COUNTERS,
    P4_IPV4_TX_COUNTERS,
    P4_IPV4_COUNTERS,
    P4_IPV6_RX_COUNTERS,
    P4_IPV6_TX_COUNTERS,
    P4_IPV6_COUNTERS,
    P4_ARP_RX_COUNTERS,
    P4_ARP_TX_COUNTERS,
    P4_ARP_COUNTERS,
    P4_NDP_RX_COUNTERS,
    P4_NDP_TX_COUNTERS,
    P4_NDP_COUNTERS,
    P4_ICMP_RX_COUNTERS,
    P4_ICMP_TX_COUNTERS,
    P4_ICMP_COUNTERS,
    P4_TCP_RX_COUNTERS,
    P4_TCP_TX_COUNTERS,
    P4_TCP_COUNTERS,
    P4_UDP_RX_COUNTERS,
    P4_UDP_TX_COUNTERS,
    P4_UDP_COUNTERS,
    P4_CLEAR_COUNTERS,
    P4_ETH_COUNTERS,
)

class PCountersIPv4:
    """IpV4 statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_IPV4_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_IPV4_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_IPV4_COUNTERS(conn, module_id, port_id)


class PCountersIPv6:
    """IpV6 statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_IPV6_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_IPV6_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_IPV6_COUNTERS(conn, module_id, port_id)

class PCountersICMP:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_ICMP_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_ICMP_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_ICMP_COUNTERS(conn, module_id, port_id)

class PCountersTCP:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_TCP_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_TCP_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_TCP_COUNTERS(conn, module_id, port_id)
        
class PCountersUDP:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_UDP_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_UDP_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_UDP_COUNTERS(conn, module_id, port_id)

class PCountersETH:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_ETH_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_ETH_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_ETH_COUNTERS(conn, module_id, port_id)


class PCountersARP:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_ARP_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_ARP_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_ARP_COUNTERS(conn, module_id, port_id)


class PCountersNDP:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_NDP_RX_COUNTERS(conn, module_id, port_id)
        self.tx = P4_NDP_TX_COUNTERS(conn, module_id, port_id)
        self.total = P4_NDP_COUNTERS(conn, module_id, port_id)


class PCounters:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.clear = P4_CLEAR_COUNTERS(conn, module_id, port_id)
        self.total_tx = P4_PORT_TX_COUNTERS(conn, module_id, port_id)
        self.total_rx = P4_PORT_RX_COUNTERS(conn, module_id, port_id)
        self.totatl = P4_PORT_COUNTERS(conn, module_id, port_id)
        
        self.ipv4 = PCountersIPv4(conn, module_id, port_id)
        self.ipv6 = PCountersIPv6(conn, module_id, port_id)
        self.icmp = PCountersICMP(conn, module_id, port_id)
        self.tcp = PCountersTCP(conn, module_id, port_id)
        self.udp = PCountersUDP(conn, module_id, port_id)
        self.eth = PCountersETH(conn, module_id, port_id)
        self.arp = PCountersARP(conn, module_id, port_id)
        self.ndp = PCountersNDP(conn, module_id, port_id)