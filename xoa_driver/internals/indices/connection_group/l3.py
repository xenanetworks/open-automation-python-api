from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.client_range = P4G_CLIENT_RANGE(conn, module_id, port_id, group_idx)
        self.server_range = P4G_SERVER_RANGE(conn, module_id, port_id, group_idx)


class GIPv6L3:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.client_range = P4G_IPV6_CLIENT_RANGE(conn, module_id, port_id, group_idx)
        self.server_range = P4G_IPV6_SERVER_RANGE(conn, module_id, port_id, group_idx)
        self.traffic_class = P4G_IPV6_TRAFFIC_CLASS(conn, module_id, port_id, group_idx)
        self.flow_label = P4G_IPV6_FLOW_LABEL(conn, module_id, port_id, group_idx)


class GDifferentialServiceL3:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.type = P4G_IP_DS_TYPE(conn, module_id, port_id, group_idx)
        self.value = P4G_IP_DS_VALUE(conn, module_id, port_id, group_idx)
        self.mask = P4G_IP_DS_MASK(conn, module_id, port_id, group_idx)
        self.range_limits = P4G_IP_DS_MINMAX(conn, module_id, port_id, group_idx)
        self.step = P4G_IP_DS_STEP(conn, module_id, port_id, group_idx)


class GL3:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.ip_version = P4G_IP_VERSION(conn, module_id, port_id, group_idx)
        self.ipv4 = GIPv4L3(conn, module_id, port_id, group_idx)
        self.ipv6 = GIPv6L3(conn, module_id, port_id, group_idx)
        self.diffserv = GDifferentialServiceL3(conn, module_id, port_id, group_idx)
        self.nat = P4G_NAT(conn, module_id, port_id, group_idx) # ToDo: maybe to add extra logic for this command based on the description