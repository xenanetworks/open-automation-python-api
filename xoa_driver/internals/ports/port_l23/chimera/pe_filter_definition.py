from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands.enums import (
    FilterType, 
    VlanType,
)
from xoa_driver.internals.core.commands import (
    PEF_INIT,
    PEF_APPLY,
    PEF_ENABLE,
    PEF_ETHSETTINGS,
    PEF_ETHSRCADDR,
    PEF_ETHDESTADDR,
    PEF_L2PUSE,
    PEF_VLANSETTINGS,
    PEF_VLANTAG,
    PEF_VLANPCP,
    PEF_MPLSSETTINGS,
    PEF_MPLSLABEL,
    PEF_MPLSTOC,
    PEF_L3USE,
    PEF_IPV4SETTINGS,
    PEF_IPV4SRCADDR,
    PEF_IPV4DESTADDR,
    PEF_IPV4DSCP,
    PEF_IPV6SETTINGS,
    PEF_IPV6SRCADDR,
    PEF_IPV6DESTADDR,
    PEF_IPV6TC,
    PEF_UDPSETTINGS,
    PEF_UDPSRCPORT,
    PEF_UDPDESTPORT,
    PEF_TCPSETTINGS,
    PEF_TCPSRCPORT,
    PEF_TCPDESTPORT,
    PEF_ANYSETTINGS,
    PEF_ANYCONFIG,
    PEF_TPLDSETTINGS,
    PEF_TPLDCONFIG,
    # PEF_ISSHADOWDIRTY, # TODO: need to implment
    # PEF_CANCEL, # TODO: need to implment
    PEF_VALUE,
    PEF_MASK,
    PEF_PROTOCOL,
    PEF_MODE,
)

class FEthernet:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_ETHSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.src_address = PEF_ETHSRCADDR(conn, module_id, port_id, flow_index, filter_type)
        self.dest_address = PEF_ETHDESTADDR(conn, module_id, port_id, flow_index, filter_type)



class FPerVlanType:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType, vlan_type: VlanType ) -> None:
        self.tag = PEF_VLANTAG(conn, module_id, port_id, flow_index, filter_type, vlan_type)
        self.pcp = PEF_VLANPCP(conn, module_id, port_id, flow_index, filter_type, vlan_type)
        
class FVlan:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_VLANSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.inner = FPerVlanType(conn, module_id, port_id, flow_index, filter_type, VlanType.INNER)
        self.outer = FPerVlanType(conn, module_id, port_id, flow_index, filter_type, VlanType.OUTER)
        
class FUdp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_UDPSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.src_port = PEF_UDPSRCPORT(conn, module_id, port_id, flow_index, filter_type)
        self.dest_port = PEF_UDPDESTPORT(conn, module_id, port_id, flow_index, filter_type)

class FTcp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_TCPSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.src_port = PEF_TCPSRCPORT(conn, module_id, port_id, flow_index, filter_type)
        self.dest_port = PEF_TCPDESTPORT(conn, module_id, port_id, flow_index, filter_type)

class FIPv4:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_IPV4SETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.src_address = PEF_IPV4SRCADDR(conn, module_id, port_id, flow_index, filter_type)
        self.dest_address = PEF_IPV4DESTADDR(conn, module_id, port_id, flow_index, filter_type)
        self.dscp = PEF_IPV4DSCP(conn, module_id, port_id, flow_index, filter_type)
        
class FIPv6:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_IPV6SETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.src_address = PEF_IPV6SRCADDR(conn, module_id, port_id, flow_index, filter_type)
        self.dest_address = PEF_IPV6DESTADDR(conn, module_id, port_id, flow_index, filter_type)
        self.traffic_class = PEF_IPV6TC(conn, module_id, port_id, flow_index, filter_type)
        

class FIp:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.v4 = FIPv4(conn, module_id, port_id, flow_index, filter_type)
        self.v6 = FIPv6(conn, module_id, port_id, flow_index, filter_type)

class FMpls:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_MPLSSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.label = PEF_MPLSLABEL(conn, module_id, port_id, flow_index, filter_type)
        self.toc = PEF_MPLSTOC(conn, module_id, port_id, flow_index, filter_type)

class FTpld:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_TPLDSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.test_payload_filters_config = tuple( 
            PEF_TPLDCONFIG(conn, module_id, port_id, flow_index, filter_type, test_payload_filter_index) 
            for test_payload_filter_index in range(16) # range need to put to the constants place
        )


class FAny:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_ANYSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        self.config = PEF_ANYCONFIG(conn, module_id, port_id, flow_index, filter_type)

class FilterDefinition:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        # TODO: check if possible to make an transparent way of setting values base on <mode> and <fid_type>
        self.initiating = PEF_INIT(conn, module_id, port_id, flow_index)
        self.apply = PEF_APPLY(conn, module_id, port_id, flow_index)
        self.protocol = PEF_PROTOCOL(conn, module_id, port_id, flow_index)
        self.mode = PEF_MODE(conn, module_id, port_id, flow_index)
        
        self.enable = PEF_ENABLE(conn, module_id, port_id, flow_index, filter_type)
        self.l2plus_use = PEF_L2PUSE(conn, module_id, port_id, flow_index, filter_type)
        self.l3_use = PEF_L3USE(conn, module_id, port_id, flow_index, filter_type)
        self.value = PEF_VALUE(conn, module_id, port_id, flow_index, filter_type)
        self.mask = PEF_MASK(conn, module_id, port_id, flow_index, filter_type)
        
        self.any = FAny(conn, module_id, port_id, flow_index, filter_type)
        self.tpld = FTpld(conn, module_id, port_id, flow_index, filter_type)
        self.mpls = FMpls(conn, module_id, port_id, flow_index, filter_type)
        self.ip = FIp(conn, module_id, port_id, flow_index, filter_type)
        self.tcp = FTcp(conn, module_id, port_id, flow_index, filter_type)
        self.udp = FUdp(conn, module_id, port_id, flow_index, filter_type)
        self.vlan = FVlan(conn, module_id, port_id, flow_index, filter_type)
        self.ethernet = FEthernet(conn, module_id, port_id, flow_index, filter_type)