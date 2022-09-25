from typing import (
    Dict,
    Tuple,
    Type,
    TypeVar,
    TYPE_CHECKING
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands.enums import (
    FilterType, 
    FilterVlanType,
    ProtocolOption,
    FilterMode,
)
from xoa_driver.internals.core.commands import (
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
    # PEF_ISSHADOWDIRTY, #TODO: need to implement
    # PEF_CANCEL, #TODO: need to implement
    PEF_VALUE,
    PEF_MASK,
    PEF_PROTOCOL,
    PEF_MODE,
)
from ._utils import prevent_set

class FEthernet:
    """Filter for Ethernet field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_ETHSETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on Ethernet field.
        Representation of PEF_ETHSETTINGS
        """
        self.src_address = prevent_set(PEF_ETHSRCADDR(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Ethernet source address settings for the filter.
        Representation of PEF_ETHSRCADDR
        """
        self.dest_address = prevent_set(PEF_ETHDESTADDR(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Ethernet destination address settings for the filter.
        Representation of PEF_ETHDESTADDR
        """


class FPerVlanType:
    """Filter for VLAN tag."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType, vlan_type: FilterVlanType ) -> None:
        self.tag = prevent_set(PEF_VLANTAG(conn, module_id, port_id, flow_index, filter_type, vlan_type), filter_type)
        """VLAN tag setting for the filter.
        Representation of PEF_VLANTAG
        """
        self.pcp = prevent_set(PEF_VLANPCP(conn, module_id, port_id, flow_index, filter_type, vlan_type), filter_type)
        """VLAN PCP setting for the filter.
        Representation of PEF_VLANPCP
        """


class FVlan:
    """Filter for VLAN field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_VLANSETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on VLAN field.
        Representation of PEF_VLANSETTINGS
        """
        
        self.inner = FPerVlanType(conn, module_id, port_id, flow_index, filter_type, FilterVlanType.INNER)
        """Filter for inner VLAN tag."""
        
        self.outer = FPerVlanType(conn, module_id, port_id, flow_index, filter_type, FilterVlanType.OUTER)
        """Filter for outer VLAN tag."""

class FUdp:
    """Filer for UDP field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_UDPSETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on UDP field.
        Representation of PEF_UDPSETTINGS
        """
        self.src_port = prevent_set(PEF_UDPSRCPORT(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """UDP source port settings for the filter.
        Representation of PEF_UDPSRCPORT
        """
        self.dest_port = prevent_set(PEF_UDPDESTPORT(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """UDP destination port settings for the filter.
        Representation of PEF_UDPDESTPORT
        """

class FTcp:
    """Filter for TCP."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_TCPSETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on TCP field.
        Representation of PEF_TCPSETTINGS
        """
        self.src_port = prevent_set(PEF_TCPSRCPORT(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """TCP source port settings for the filter.
        Representation of PEF_TCPSRCPORT
        """
        self.dest_port = prevent_set(PEF_TCPDESTPORT(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """TCP destination port settings for the filter.
        Representation of PEF_TCPDESTPORT
        """

class FIPv4:
    """Filter for IPv4 field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_IPV4SETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on IPv4 field.
        Representation of PEF_IPV4SETTINGS
        """
        self.src_address = prevent_set(PEF_IPV4SRCADDR(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """IPv4 source address settings for the filter.
        Representation of PEF_IPV4SRCADDR
        """
        self.dest_address = prevent_set(PEF_IPV4DESTADDR(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """IPv4 destination address settings for the filter.
        Representation of PEF_IPV4DESTADDR
        """
        self.dscp = prevent_set(PEF_IPV4DSCP(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """IPv4 DSCP/TOS settings for the filter.
        Representation of PEF_IPV4DSCP
        """

class FIPv6:
    """Filter for IPv6 field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_IPV6SETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on IPv6 field.
        Representation of PEF_IPV6SETTINGS
        """
        self.src_address = prevent_set(PEF_IPV6SRCADDR(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """IPv6 source address settings for the filter.
        Representation of PEF_IPV6SRCADDR
        """
        self.dest_address = prevent_set(PEF_IPV6DESTADDR(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """IPv6 destination address settings for the filter.
        Representation of PEF_IPV6DESTADDR
        """
        self.traffic_class = prevent_set(PEF_IPV6TC(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """IPv6 traffic class settings for the filter.
        Representation of PEF_IPV6TC
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
        self.settings = prevent_set(PEF_MPLSSETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on MPLS field.
        Representation of PEF_MPLSSETTINGS
        """
        self.label = prevent_set(PEF_MPLSLABEL(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """MPLS label settings for the filter.
        Representation of PEF_MPLSLABEL
        """
        self.toc = prevent_set(PEF_MPLSTOC(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """"MPLS TOC settings for the filter.
        Representation of PEF_MPLSTOC
        """

class FTpld:
    """Filter for Xena TPLD field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_TPLDSETTINGS(conn, module_id, port_id, flow_index, filter_type))
        """Filter action on Xena TPLD field.
        Representation of PEF_TPLDSETTINGS
        """
        
        self.test_payload_filters_config = tuple( 
            prevent_set(PEF_TPLDCONFIG(conn, module_id, port_id, flow_index, filter_type, test_payload_filter_index), filter_type) 
            for test_payload_filter_index in range(16) # range need to put to the constants place
        )
        """TPLS filter configurations.
        Representation of PEF_TPLDCONFIG
        """


class FAny:
    """Filter for any field."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.settings = prevent_set(PEF_ANYSETTINGS(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Filter action on any field.
        Representation of PEF_ANYSETTINGS
        """
        self.config = prevent_set(PEF_ANYCONFIG(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """Any field's filter configurations.
        Representation of PEF_ANYCONFIG
        """


class ModeBasic:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self.l2plus_use = prevent_set(PEF_L2PUSE(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """L2 protocol to use.
        Representation of PEF_L2PUSE
        """
        self.l3_use = prevent_set(PEF_L3USE(conn, module_id, port_id, flow_index, filter_type), filter_type)
        """L3 protocol to use.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_L3USE`
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


class ProtocolSegment:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType, protocol_segment_index: int, segment_type: ProtocolOption) -> None:
        self.segment_type = segment_type
        
        self.value = prevent_set(PEF_VALUE(conn, module_id, port_id, flow_index, filter_type, protocol_segment_index), filter_type)
        """Value bytes match for the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_VALUE`
        """
        self.mask = prevent_set(PEF_MASK(conn, module_id, port_id, flow_index, filter_type, protocol_segment_index), filter_type)
        """Mask byte value.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MASK`
        """

class ModeExtended:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType) -> None:
        self._conn = conn
        self._module_id = module_id
        self._port_id = port_id
        self._flow_index = flow_index
        self._filter_type = filter_type
                
        # self.protocol = prevent_set(PEF_PROTOCOL(conn, module_id, port_id, flow_index, filter_type))
        # """Protocol segments match for the filter.
        # Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_PROTOCOL`
        # """
        
    async def get_protocol_segments(self) -> Tuple[ProtocolSegment, ...]:
        segments_raw = (
            await PEF_PROTOCOL(
                self._conn, 
                self._module_id, 
                self._port_id, 
                self._flow_index, 
                self._filter_type
            ).get()
        ).segment_list
        return tuple( 
            ProtocolSegment(
                self._conn, 
                self._module_id, 
                self._port_id, 
                self._flow_index, 
                self._filter_type,
                idx, # TODO: need to discute with Leo
                ProtocolOption(segment_type)
            ) 
            for idx, segment_type in enumerate(segments_raw) 
        )

T = TypeVar("T")
async def get_mode(conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, filter_type: FilterType, mode_types: Dict[FilterMode, Type[T]] ) -> T:
    mode_raw = (
        await PEF_MODE(
            conn, 
            module_id, 
            port_id, 
            flow_index, 
            filter_type,
        ).get()
    ).mode
    mode_type = mode_types[FilterMode(mode_raw)]
    return mode_type(
        conn, 
        module_id, 
        port_id, 
        flow_index, 
        filter_type,
    )

