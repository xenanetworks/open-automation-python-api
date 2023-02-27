from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P4G_CLIENT_RANGE,
    P4G_SERVER_RANGE,
    P4G_IP_DS_TYPE,
    P4G_IP_DS_VALUE,
    P4G_IP_DS_MASK,
    P4G_IP_DS_MINMAX,
    P4G_IP_DS_STEP,
    P4G_IP_VERSION,
    P4G_IPV6_CLIENT_RANGE,
    P4G_IPV6_SERVER_RANGE,
    P4G_IPV6_TRAFFIC_CLASS,
    P4G_IPV6_FLOW_LABEL,
    P4G_NAT,
)


class GIPv4L3:
    """L3 IPv4"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.client_range = P4G_CLIENT_RANGE(conn, module_id, port_id, group_idx)
        """Specifies a number of client sockets
        
        :type: P4G_CLIENT_RANGE
        """

        self.server_range = P4G_SERVER_RANGE(conn, module_id, port_id, group_idx)
        """Specifies a number of server sockets
        
        :type: P4G_SERVER_RANGE
        """


class GIPv6L3:
    """L3 IPv6"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.client_range = P4G_IPV6_CLIENT_RANGE(conn, module_id, port_id, group_idx)
        """Specifies the number of client sockets
        
        :type: P4G_IPV6_CLIENT_RANGE
        """

        self.server_range = P4G_IPV6_SERVER_RANGE(conn, module_id, port_id, group_idx)
        """Specifies the number of server sockets
        
        :type: P4G_IPV6_SERVER_RANGE
        """

        self.traffic_class = P4G_IPV6_TRAFFIC_CLASS(conn, module_id, port_id, group_idx)
        """Configure the value of the traffic class field of the IPv6 header.
        
        :type: P4G_IPV6_TRAFFIC_CLASS
        """

        self.flow_label = P4G_IPV6_FLOW_LABEL(conn, module_id, port_id, group_idx)
        """Configure the value of the flow label field of the IPv6 header.
        
        :type: P4G_IPV6_FLOW_LABEL
        """


class GDifferentialServiceL3:
    """L3 Differential Service"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.type = P4G_IP_DS_TYPE(conn, module_id, port_id, group_idx)
        """Configure the mode of the DS field of the IP header of this Connection Group.
        
        :type: P4G_IP_DS_TYPE
        """

        self.value = P4G_IP_DS_VALUE(conn, module_id, port_id, group_idx)
        """Specify the (FIXED) value used for DS.
        
        :type: P4G_IP_DS_VALUE
        """

        self.mask = P4G_IP_DS_MASK(conn, module_id, port_id, group_idx)
        """Specify a bit mask to be applied to the DS field.
        
        :type: P4G_IP_DS_MASK
        """

        self.range_limits = P4G_IP_DS_MINMAX(conn, module_id, port_id, group_idx)
        """Configure the min and max values of the range for the calculated part of the DS value.
        
        :type: P4G_IP_DS_MINMAX
        """

        self.step = P4G_IP_DS_STEP(conn, module_id, port_id, group_idx)
        """Specifies the incrementing step size for the calculated part of the DS value.
        
        :type: P4G_IP_DS_STEP
        """


class GL3:
    """L3 Configurations"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.ip_version = P4G_IP_VERSION(conn, module_id, port_id, group_idx)
        """Specifies either IPv4 or IPv6.
        
        :type: P4G_IP_VERSION
        """

        self.ipv4 = GIPv4L3(conn, module_id, port_id, group_idx)
        """L3 IPv4 Configurations
        
        :type: GIPv4L3
        """

        self.ipv6 = GIPv6L3(conn, module_id, port_id, group_idx)
        """L3 IPv6 Configurations
        
        :type: GIPv6L3
        """

        self.diffserv = GDifferentialServiceL3(conn, module_id, port_id, group_idx)
        """L3 IPv6 DS Configurations
        
        :type: GDifferentialServiceL3
        """

        self.nat = P4G_NAT(conn, module_id, port_id, group_idx)  # TODO: maybe to add extra logic for this command based on the description
        """Specify whether to support DUT Source NAT functionality.
        
        :type: P4G_NAT
        """
