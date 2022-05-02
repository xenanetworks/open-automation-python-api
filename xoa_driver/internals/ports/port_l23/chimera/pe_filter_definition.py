from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands.enums import (
    FilterType, 
    FilterVlanType,
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
    """Filter for Ethernet field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_ETHSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on Ethernet field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_ETHSETTINGS`
        """
        self.src_address = PEF_ETHSRCADDR(conn, module_id, port_id, flow_index, filter_type)
        """Ethernet source address settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_ETHSRCADDR`
        """
        self.dest_address = PEF_ETHDESTADDR(conn, module_id, port_id, flow_index, filter_type)
        """Ethernet destination address settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_ETHDESTADDR`
        """



class FPerVlanType:
    """Filter for VLAN tag."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType, vlan_type: FilterVlanType ) -> None:
        self.tag = PEF_VLANTAG(conn, module_id, port_id, flow_index, filter_type, vlan_type)
        """VLAN tag setting for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VLANTAG`
        """
        self.pcp = PEF_VLANPCP(conn, module_id, port_id, flow_index, filter_type, vlan_type)
        """VLAN PCP setting for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VLANPCP`
        """
        
class FVlan:
    """Filter for VLAN field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_VLANSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on VLAN field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VLANSETTINGS`
        """
        self.inner = FPerVlanType(conn, module_id, port_id, flow_index, filter_type, FilterVlanType.INNER)
        """Filter for inner VLAN tag."""
        self.outer = FPerVlanType(conn, module_id, port_id, flow_index, filter_type, FilterVlanType.OUTER)
        """Filter for outer VLAN tag."""
        
class FUdp:
    """Filer for UDP field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_UDPSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on UDP field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_UDPSETTINGS`
        """
        self.src_port = PEF_UDPSRCPORT(conn, module_id, port_id, flow_index, filter_type)
        """UDP source port settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_UDPSRCPORT`
        """
        self.dest_port = PEF_UDPDESTPORT(conn, module_id, port_id, flow_index, filter_type)
        """UDP destination port settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_UDPDESTPORT`
        """

class FTcp:
    """Filter for TCP."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_TCPSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on TCP field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_TCPSETTINGS`
        """
        self.src_port = PEF_TCPSRCPORT(conn, module_id, port_id, flow_index, filter_type)
        """TCP source port settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_TCPSRCPORT`
        """
        self.dest_port = PEF_TCPDESTPORT(conn, module_id, port_id, flow_index, filter_type)
        """TCP destination port settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_TCPDESTPORT`
        """

class FIPv4:
    """Filter for IPv4 field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_IPV4SETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on IPv4 field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV4SETTINGS`
        """
        self.src_address = PEF_IPV4SRCADDR(conn, module_id, port_id, flow_index, filter_type)
        """IPv4 source address settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV4SRCADDR`
        """
        self.dest_address = PEF_IPV4DESTADDR(conn, module_id, port_id, flow_index, filter_type)
        """IPv4 destination address settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV4DESTADDR`
        """
        self.dscp = PEF_IPV4DSCP(conn, module_id, port_id, flow_index, filter_type)
        """IPv4 DSCP/TOS settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV4DSCP`
        """
        
class FIPv6:
    """Filter for IPv6 field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_IPV6SETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on IPv6 field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV6SETTINGS`
        """
        self.src_address = PEF_IPV6SRCADDR(conn, module_id, port_id, flow_index, filter_type)
        """IPv6 source address settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV6SRCADDR`
        """
        self.dest_address = PEF_IPV6DESTADDR(conn, module_id, port_id, flow_index, filter_type)
        """IPv6 destination address settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV6DESTADDR`
        """
        self.traffic_class = PEF_IPV6TC(conn, module_id, port_id, flow_index, filter_type)
        """IPv6 traffic class settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_IPV6TC`
        """
        

class FIp:
    """Filter for IP field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.v4 = FIPv4(conn, module_id, port_id, flow_index, filter_type)
        """Filter for IPv4 field."""
        self.v6 = FIPv6(conn, module_id, port_id, flow_index, filter_type)
        """Filter for IPv6 field."""

class FMpls:
    """Filter for MPLS field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_MPLSSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on MPLS field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MPLSSETTINGS`
        """
        self.label = PEF_MPLSLABEL(conn, module_id, port_id, flow_index, filter_type)
        """MPLS label settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MPLSLABEL`
        """
        self.toc = PEF_MPLSTOC(conn, module_id, port_id, flow_index, filter_type)
        """"MPLS TOC settings for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MPLSTOC`
        """

class FTpld:
    """Filter for Xena TPLD field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_TPLDSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on Xena TPLD field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_TPLDSETTINGS`
        """
        self.test_payload_filters_config = tuple( 
            PEF_TPLDCONFIG(conn, module_id, port_id, flow_index, filter_type, test_payload_filter_index) 
            for test_payload_filter_index in range(16) # range need to put to the constants place
        )
        """TPLS filter configurations.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_TPLDCONFIG`
        """


class FAny:
    """Filter for any field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = PEF_ANYSETTINGS(conn, module_id, port_id, flow_index, filter_type)
        """Filter action on any field.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_ANYSETTINGS`
        """
        self.config = PEF_ANYCONFIG(conn, module_id, port_id, flow_index, filter_type)
        """Any field's filter configurations.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_ANYCONFIG`
        """

class FilterDefinition:
    """Filter definition."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        # TODO: check if possible to make an transparent way of setting values base on <mode> and <fid_type>
        self.initiating = PEF_INIT(conn, module_id, port_id, flow_index)
        """Preparing filter definition.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_INIT`
        """
        self.apply = PEF_APPLY(conn, module_id, port_id, flow_index)
        """Apply filter defintion.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_APPLY`
        """
        self.protocol = PEF_PROTOCOL(conn, module_id, port_id, flow_index)
        """Protocol segments match for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_PROTOCOL`
        """
        self.mode = PEF_MODE(conn, module_id, port_id, flow_index)
        """Filter mode.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MODE`
        """
        
        self.enable = PEF_ENABLE(conn, module_id, port_id, flow_index, filter_type)
        """Enabling the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_ENABLE`
        """
        self.l2plus_use = PEF_L2PUSE(conn, module_id, port_id, flow_index, filter_type)
        """L2 protocol to use.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_L2PUSE`
        """
        self.l3_use = PEF_L3USE(conn, module_id, port_id, flow_index, filter_type)
        """L3 protocol to use.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_L3USE`
        """
        self.value = PEF_VALUE(conn, module_id, port_id, flow_index, filter_type)
        """Value bytes match for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VALUE`
        """
        self.mask = PEF_MASK(conn, module_id, port_id, flow_index, filter_type)
        """Mask byte value.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MASK`
        """
        
        self.any = FAny(conn, module_id, port_id, flow_index, filter_type)
        """Filter for any field."""
        self.tpld = FTpld(conn, module_id, port_id, flow_index, filter_type)
        """Filter for Xena TPLD field."""
        self.mpls = FMpls(conn, module_id, port_id, flow_index, filter_type)
        """Filter for MPLS field."""
        self.ip = FIp(conn, module_id, port_id, flow_index, filter_type)
        """Filter for IP field."""
        self.tcp = FTcp(conn, module_id, port_id, flow_index, filter_type)
        """Filter for TCP ield."""
        self.udp = FUdp(conn, module_id, port_id, flow_index, filter_type)
        """Filter for UDP field."""
        self.vlan = FVlan(conn, module_id, port_id, flow_index, filter_type)
        """Filter for VLAN field."""
        self.ethernet = FEthernet(conn, module_id, port_id, flow_index, filter_type)
        """Filter for Ethernet field."""