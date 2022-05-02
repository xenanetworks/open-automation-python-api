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
    """IPV4 statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_IPV4_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_IPV4_RX_COUNTERS`"""
        self.tx = P4_IPV4_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_IPV4_TX_COUNTERS`"""
        self.total = P4_IPV4_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_IPV4_COUNTERS`"""


class PCountersIPv6:
    """IPV6 statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_IPV6_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_IPV6_RX_COUNTERS`"""
        self.tx = P4_IPV6_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_IPV6_TX_COUNTERS`"""
        self.total = P4_IPV6_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_IPV6_COUNTERS`"""

class PCountersICMP:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_ICMP_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ICMP_RX_COUNTERS`"""
        self.tx = P4_ICMP_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ICMP_TX_COUNTERS`"""
        self.total = P4_ICMP_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ICMP_COUNTERS`"""

class PCountersTCP:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_TCP_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_TCP_RX_COUNTERS`"""
        self.tx = P4_TCP_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_TCP_TX_COUNTERS`"""
        self.total = P4_TCP_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_TCP_COUNTERS`"""
        
class PCountersUDP:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_UDP_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_UDP_RX_COUNTERS`"""
        self.tx = P4_UDP_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_UDP_TX_COUNTERS`"""
        self.total = P4_UDP_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_UDP_COUNTERS`"""

class PCountersETH:
    """ICMP statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_ETH_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ETH_RX_COUNTERS`"""
        self.tx = P4_ETH_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ETH_TX_COUNTERS`"""
        self.total = P4_ETH_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ETH_COUNTERS`"""


class PCountersARP:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_ARP_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ARP_RX_COUNTERS`"""
        self.tx = P4_ARP_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ARP_TX_COUNTERS`"""
        self.total = P4_ARP_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_ARP_COUNTERS`"""


class PCountersNDP:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = P4_NDP_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_NDP_RX_COUNTERS`"""
        self.tx = P4_NDP_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_NDP_TX_COUNTERS`"""
        self.total = P4_NDP_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_NDP_COUNTERS`"""


class PCounters:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.clear = P4_CLEAR_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_CLEAR_COUNTERS`"""
        self.total_tx = P4_PORT_TX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_PORT_TX_COUNTERS`"""
        self.total_rx = P4_PORT_RX_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_PORT_RX_COUNTERS`"""
        self.total = P4_PORT_COUNTERS(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4_commands.P4_PORT_COUNTERS`"""
        
        self.ipv4 = PCountersIPv4(conn, module_id, port_id)
        """L47 port IPv4 counters."""
        self.ipv6 = PCountersIPv6(conn, module_id, port_id)
        """L47 port IPv6 counters."""
        self.icmp = PCountersICMP(conn, module_id, port_id)
        """L47 port ICMP counters."""
        self.tcp = PCountersTCP(conn, module_id, port_id)
        """L47 port TCP counters."""
        self.udp = PCountersUDP(conn, module_id, port_id)
        """L47 port UDP counters."""
        self.eth = PCountersETH(conn, module_id, port_id)
        """L47 port Ethernet counters."""
        self.arp = PCountersARP(conn, module_id, port_id)
        """L47 port ARP counters."""
        self.ndp = PCountersNDP(conn, module_id, port_id)
        """L47 port NDP counters."""