from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P4G_L2_CLIENT_MAC,
    P4G_L2_SERVER_MAC,
    P4G_L2_USE_ADDRESS_RES,
    P4G_L2_USE_GW,
    P4G_L2_GW,
    P4G_L2_IPV6_GW,
    P4G_VLAN_ENABLE,
    P4G_VLAN_TCI,
)


class GMacL2:
    """L2 MAC"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.client = P4G_L2_CLIENT_MAC(conn, module_id, port_id, group_idx)
        """Configure the client MAC address.
        
        :type: P4G_L2_CLIENT_MAC
        """

        self.server = P4G_L2_SERVER_MAC(conn, module_id, port_id, group_idx)
        """Configure the server MAC address.
        
        :type: P4G_L2_SERVER_MAC
        """


class GGatewayL2:
    """L2 Gateway"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.use = P4G_L2_USE_GW(conn, module_id, port_id, group_idx)
        """Specify whether to use the resolved default gateway's MAC address as the destination MAC address in the packets.
        
        :type: P4G_L2_USE_GW
        """

        self.ipv4 = P4G_L2_GW(conn, module_id, port_id, group_idx)
        """Specify a default gateway for IPv4.
        
        :type: P4G_L2_GW
        """

        self.ipv6 = P4G_L2_IPV6_GW(conn, module_id, port_id, group_idx)
        """Specify a default gateway for IPv6.
        
        :type: P4G_L2_IPV6_GW
        """


class GVlanL2:
    """L2 VLAN"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.enable = P4G_VLAN_ENABLE(conn, module_id, port_id, group_idx)
        """Specify whether to insert a VLAN tag header upon transmit.
        
        :type: P4G_VLAN_ENABLE
        """

        self.tci = P4G_VLAN_TCI(conn, module_id, port_id, group_idx)
        """Specify the VLAN TCI.
        
        :type: P4G_VLAN_TCI
        """


class GL2:
    """L2 Configurations"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.address_resolve = P4G_L2_USE_ADDRESS_RES(conn, module_id, port_id, group_idx)
        """
        
        :type: P4G_L2_USE_ADDRESS_RES
        """
        self.mac = GMacL2(conn, module_id, port_id, group_idx)
        """L2 MAC
        
        :type: GMacL2
        """

        self.gateway = GGatewayL2(conn, module_id, port_id, group_idx)
        """L2 Gateway
        
        :type: GGatewayL2
        """
        
        self.vlan = GVlanL2(conn, module_id, port_id, group_idx)
        """L2 VLAN
        
        :type: GVlanL2
        """
