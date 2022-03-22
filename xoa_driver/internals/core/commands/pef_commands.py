"""
Port Impairment Filter Definition (Chimera only) Commands
"""
from dataclasses import dataclass
import ipaddress
import typing
import functools

from ..protocol.command_builders import (
    build_get_request,
    build_set_request
)
from .. import interfaces
from ..transporter.token import Token
from ..protocol.fields.data_types import *
from ..protocol.fields.field import XmpField
from ..registry import register_command
from .enums import *

@register_command
@dataclass
class PEF_INIT:
    """
    Prepares for setting up a filter definition.  When called, all filter
    definitions in the shadow-set which are not applied are discarded and replaced
    with the default values (DEFAULT).  NOTE: There are 2 register copies used to
    configure the filters:      (1) Shadow copy (type = 0), temporary copy
    configured by SW.          Values stored in "shadow registers" have no immediate
    effect on the flow filters.          "PEF_APPLY" API will pass the values from
    the "shadow copy" to the "working copy".      (2) Working registers (type = 1),
    reflects what is currently used for filtering in the FPGA. Working registers
    cannot be written directly C only using the "shadow copy".      (3) All SETs are
    performed on shadow registers ONLY.      (4) Only when PEF_APPLY is called,
    working registers and FPGA are updated with values from the "shadow copy".
    """

    code: typing.ClassVar[int] = 1700
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex],
            ),
        )


@register_command
@dataclass
class PEF_APPLY:
    """
    Applies filter definitions from "shadow-registers" to "working-registers". This
    also pushes these settings to the FPGA.
    """

    code: typing.ClassVar[int] = 1701
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex],
            ),
        )


@register_command
@dataclass
class PEF_ENABLE:
    """
    Defines if filtering is enabled for the flow.
    """

    code: typing.ClassVar[int] = 1702
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        state: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the state of the filter.

    @dataclass(frozen=True)
    class GetDataAttr:
        state: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the state of the filter.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, state: OnOff) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], state=state))

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_ETHSETTINGS:
    """
    Defines what filter action is performed on the Ethernet header.
    """

    code: typing.ClassVar[int] = 1703
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies if Ethernet information is expected.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of Ethernet information.

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies if Ethernet information is expected.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of Ethernet information.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_ETHSRCADDR:
    """
    Defines the Ethernet Source Address settings for the Ethernet filter. NOTE: For
    SET, only allowed filter_type is "shadow-copy"(0)
    """

    code: typing.ClassVar[int] = 1704
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of Ethernet information.
        value: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000.
        mask: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF.

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of Ethernet information.
        value: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000.
        mask: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: str, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_ETHDESTADDR:
    """
    Defines the Ethernet Destination Address settings for the Ethernet filter. NOTE:
    For SET, only allowed filter_type is "shadow-copy"(0)
    """

    code: typing.ClassVar[int] = 1705
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of Ethernet information:
        value: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000
        mask: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of Ethernet information:
        value: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000
        mask: XmpField[XmpHex6] = XmpField(XmpHex6)  # six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: str, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_L2PUSE:
    """
    Defines what Layer 2+ protocols that are present and may be used for the filter.
    NOTE: For SET, only allowed filter_type is "shadow-copy"(0)
    """

    code: typing.ClassVar[int] = 1706
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=L2PlusPresent)  # coded byte, specifies the presence of Layer 2+ protocols.

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=L2PlusPresent)  # coded byte, specifies the presence of Layer 2+ protocols.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: L2PlusPresent) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use))

    set_na = functools.partialmethod(set, L2PlusPresent.NA)
    set_vlan1 = functools.partialmethod(set, L2PlusPresent.VLAN1)
    set_vlan2 = functools.partialmethod(set, L2PlusPresent.VLAN2)
    set_mpls = functools.partialmethod(set, L2PlusPresent.MPLS)


@register_command
@dataclass
class PEF_VLANSETTINGS:
    """
    Defines what filter action is performed on the VLAN header. NOTE: For SET, only
    allowed filter_type is "shadow-copy"(0)
    """

    code: typing.ClassVar[int] = 1707
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies if VLAN information is expected.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of VLAN information.

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies if VLAN information is expected.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of VLAN information.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_VLANTAG:
    """
    Basic mode only.  Defines the VLAN TAG settings for the VLAN filter.  NOTE: For
    SET, only allowed filter_type is "shadow-copy"(0)
    """

    code: typing.ClassVar[int] = 1708
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).
    vlan_type: VlanType # coded byte, the sub-index value specifies the VLAN type. VLAN1 (0) (INNER VLAN Tag is specified for the filter – used also when only 1 VLAN) indicates single/inner VLAN-TPID = 0x8100. VLAN2 (1) (OUTER VLAN Tag is specified for the filter) indicates outer VLAN-TPID=0x88A8

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of VLAN information:
        value: XmpField[XmpInt] = XmpField(XmpInt)  # decimal digits, specifying the 12 bit value of the tag. Default value: 0.
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex digits, specifying the 12 bit value of the tag. Default value: 0x0FFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of VLAN information:
        value: XmpField[XmpInt] = XmpField(XmpInt)  # decimal digits, specifying the 12 bit value of the tag. Default value: 0.
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex digits, specifying the 12 bit value of the tag. Default value: 0x0FFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type, self.vlan_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type, self.vlan_type], use=use, value=value, mask=mask
            ),
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_VLANPCP:
    """
    Basic mode only. Defines the VLAN PCP settings for the VLAN filter.
    """

    code: typing.ClassVar[int] = 1709
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).
    vlan_type: VlanType # coded byte, the sub-index value specifies the VLAN type. VLAN1 (0) (INNER VLAN Tag is specified for the filter – used also when only 1 VLAN) indicates single/inner VLAN-TPID = 0x8100. VLAN2 (1) (OUTER VLAN Tag is specified for the filter) indicates outer VLAN-TPID=0x88A8

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of VLAN information:
        value: XmpField[XmpByte] = XmpField(XmpByte)  # byte, specifying the value of the PCP. Default value: 0 (Range: 0 to 7)
        mask: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, specifying the 8 bit value mask. Default value: 0x07

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of VLAN information:
        value: XmpField[XmpByte] = XmpField(XmpByte)  # byte, specifying the value of the PCP. Default value: 0 (Range: 0 to 7)
        mask: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, specifying the 8 bit value mask. Default value: 0x07

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type, self.vlan_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type, self.vlan_type], use=use, value=value, mask=mask
            ),
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_MPLSSETTINGS:
    """
    Basic mode only. Defines what filter action is performed on the MPLS header.
    NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1710
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of MPLS information:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of MPLS information:

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of MPLS information:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of MPLS information:

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_MPLSLABEL:
    """
    Basic mode only. Defines the MPLS label settings for the filter. NOTE: For SET,
    only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1711
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of MPLS information.
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying the 20 bit value of the label. Default value: 0.
        mask: XmpField[XmpHex3] = XmpField(XmpHex3)  # three hex bytes, specifying the 20 bit value of the label. Default value: 0x0FFFFF,

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of MPLS information.
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying the 20 bit value of the label. Default value: 0.
        mask: XmpField[XmpHex3] = XmpField(XmpHex3)  # three hex bytes, specifying the 20 bit value of the label. Default value: 0x0FFFFF,

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_MPLSTOC:
    """
    Basic mode only. Defines the MPLS TOC settings for the filter. NOTE: For SET,
    only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1712
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1). 

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of MPLS TOC information.
        value: XmpField[XmpByte] = XmpField(XmpByte)  # byte, specifying the value of the MPLS TOC. Default value: 0 (Range: 0 to 7).
        mask: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, specifying the filter mask for the value of the MPLS TOC. Default value: 0x07

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of MPLS TOC information.
        value: XmpField[XmpByte] = XmpField(XmpByte)  # byte, specifying the value of the MPLS TOC. Default value: 0 (Range: 0 to 7).
        mask: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, specifying the filter mask for the value of the MPLS TOC. Default value: 0x07

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_L3USE:
    """
    Basic mode only. Defines what Layer 3 protocols that are present and may be used
    for the filter. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1713
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=L3PlusPresent)  # coded byte, specifies the presence of Layer 3 protocols:

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=L3PlusPresent)  # coded byte, specifies the presence of Layer 3 protocols:

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: L3PlusPresent) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use))

    set_na = functools.partialmethod(set, L3PlusPresent.NA)
    set_ip4 = functools.partialmethod(set, L3PlusPresent.IP4)
    set_ip6 = functools.partialmethod(set, L3PlusPresent.IP6)


@register_command
@dataclass
class PEF_IPV4SETTINGS:
    """
    Basic mode only. Defines what filter action is performed on the IPv4
    information. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1714
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of IPv4 information.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the action of IPv4 information.

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of IPv4 information.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the action of IPv4 information.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_IPV4SRCADDR:
    """
    Basic mode only. Defines the IPv4 Source Address settings for the IPv4 filter.
    NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1715
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv4 information:
        value: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, specifying the four bytes of the address. Default value: 0.0.0.0
        mask: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv4 information:
        value: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, specifying the four bytes of the address. Default value: 0.0.0.0
        mask: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: typing.Union[str, int, ipaddress.IPv4Address], mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_IPV4DESTADDR:
    """
    Basic mode only. Defines the IPv4 Destination Address settings for the IPv4
    filter. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1716
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv4 information:
        value: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, specifying the four bytes of the address. Default value: 0.0.0.0
        mask: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv4 information:
        value: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, specifying the four bytes of the address. Default value: 0.0.0.0
        mask: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: typing.Union[str, int, ipaddress.IPv4Address], mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_IPV4DSCP:
    """
    Basic mode only. Defines if IPv4 DSCP/TOS settings used for the filter. NOTE:
    For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1717
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv4 information:
        value: XmpField[XmpByte] = XmpField(
            XmpByte
        )  # byte, specifying the value of the IPv4 DSCP/TOS in the upper 6 bits. value[7:2] = DSCP/TOS, value[1:0] = reserved (must be zero). Default vaule: 0
        mask: XmpField[XmpHex1] = XmpField(
            XmpHex1
        )  # hex byte, specifying the filter mask of the value in the upper 6 bits. mask[7:2] = DSCP/TOS mask, mask[1:0] = reserved (must be zero). Default value: 0xFC

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv4 information:
        value: XmpField[XmpByte] = XmpField(
            XmpByte
        )  # byte, specifying the value of the IPv4 DSCP/TOS in the upper 6 bits. value[7:2] = DSCP/TOS, value[1:0] = reserved (must be zero). Default vaule: 0
        mask: XmpField[XmpHex1] = XmpField(
            XmpHex1
        )  # hex byte, specifying the filter mask of the value in the upper 6 bits. mask[7:2] = DSCP/TOS mask, mask[1:0] = reserved (must be zero). Default value: 0xFC

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_IPV6SETTINGS:
    """
    DBasic mode only. Defines what filter action is performed on the IPv6
    information. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1718
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of IPv6 information:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of IPv6 information:

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of IPv6 information:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of IPv6 information:

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_IPV6SRCADDR:
    """
    Basic mode only. Defines the IPv6 Source Address settings for the IPv4 filter.
    NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1719
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv6 information:
        value: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000
        mask: XmpField[XmpHex16] = XmpField(XmpHex16)  # 16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv6 information:
        value: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000
        mask: XmpField[XmpHex16] = XmpField(XmpHex16)  # 16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: str, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_IPV6DESTADDR:
    """
    Basic mode only. Defines the IPv6 Destination Address settings for the IPv6
    filter. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1720
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv6 information:
        value: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000
        mask: XmpField[XmpHex16] = XmpField(XmpHex16)  # 16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv6 information:
        value: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000
        mask: XmpField[XmpHex16] = XmpField(XmpHex16)  # 16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: str, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_IPV6TC:
    """
    Basic mode only. Defines the IPv6 Traffic Class settings used for the filter.
    NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1721
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv6 information:
        value: XmpField[XmpIPV6Address] = XmpField(
            XmpIPV6Address
        )  # byte, specifying the value of the IPv6 Traffic Class in the upper 6 bits. value[7:2] = IPv6 Traffic Class. value[1:0] = reserved (must be zero). Default value: 0
        mask: XmpField[XmpHex1] = XmpField(
            XmpHex1
        )  # hex byte, specifying the filter mask for the value in the upper 6 bits. mask[7:2] = IPv6 Traffic Class mask. mask[1:0] = reserved (must be zero). Default value: 0xFC

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of IPv6 information:
        value: XmpField[XmpIPV6Address] = XmpField(
            XmpIPV6Address
        )  # byte, specifying the value of the IPv6 Traffic Class in the upper 6 bits. value[7:2] = IPv6 Traffic Class. value[1:0] = reserved (must be zero). Default value: 0
        mask: XmpField[XmpHex1] = XmpField(
            XmpHex1
        )  # hex byte, specifying the filter mask for the value in the upper 6 bits. mask[7:2] = IPv6 Traffic Class mask. mask[1:0] = reserved (must be zero). Default value: 0xFC

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_UDPSETTINGS:
    """
    Basic mode only. Controls if UDP packet information is used for flow filtering.
    NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1722
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of UDP information:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of UDP information:

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of UDP information:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of UDP information:

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_UDPSRCPORT:
    """
    Basic mode only. Defines UDP Source Port settings used for the filter. NOTE: For
    SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1723
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of UDP Source Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the UDP Source Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of UDP Source Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the UDP Source Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_UDPDESTPORT:
    """
    Basic mode only. Defines UDP Destination Port settings used for the filter.NOTE:
    For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1724
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of UDP Destination Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the UDP Destination Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of UDP Destination Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the UDP Destination Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_TCPSETTINGS:
    """
    Basic mode only. Defines if filtering on TCP information is used for flow
    filtering. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1725
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of TCP information.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of TCP information.

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of TCP information.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of TCP information.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_TCPSRCPORT:
    """
    Basic mode only. Defines TCP Source Port settings used for the filter. NOTE: For
    SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1726
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of TCP Source Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the TCP Source Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of TCP Source Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the TCP Source Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_TCPDESTPORT:
    """
    Basic mode only. Defines TCP Destination Port settings used for the filter.
    NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1727
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of TCP Destination Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the TCP Destination Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        use: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of TCP Destination Port information
        value: XmpField[XmpInt] = XmpField(XmpInt)  # integer , specifying the value of the TCP Destination Port. Default value: 0
        mask: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, use: OnOff, value: int, mask: str) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], use=use, value=value, mask=mask)
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_ANYSETTINGS:
    """
    Basic mode only. Defines if filtering on ANY field in a packet is used for flow
    filtering. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1728
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of ANY field information.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of IPv6 information.

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=EthernetInfo)  # coded byte, specifies the usage of ANY field information.
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of IPv6 information.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, usage: EthernetInfo, action: Clude) -> "Token":
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], usage=usage, action=action)
        )


@register_command
@dataclass
class PEF_ANYCONFIG:
    """
    Basic mode only. Defines the ANY field filter configuration. The "ANY field"
    filter will match 6 consecutive bytes in the incoming packets at a programmable
    offset. Applying a mask, allows to only filter based on selected bits within the
    6 bytes. NOTE: For SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1729
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        position: XmpField[XmpByte] = XmpField(XmpByte)  # byte, specifies the start position of the ANY field. Default value: 0, Range:0-127
        value: XmpField[XmpHex8] = XmpField(XmpHex8)  # 8 hex bytes, specifying the six bytes of the field. Default value: 0x000000000000
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # 8 hex bytes, specifying the six bytes of the field. Default value: 0xFFFFFFFFFFFF

    @dataclass(frozen=True)
    class GetDataAttr:
        position: XmpField[XmpByte] = XmpField(XmpByte)  # byte, specifies the start position of the ANY field. Default value: 0, Range:0-127
        value: XmpField[XmpHex8] = XmpField(XmpHex8)  # 8 hex bytes, specifying the six bytes of the field. Default value: 0x000000000000
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # 8 hex bytes, specifying the six bytes of the field. Default value: 0xFFFFFFFFFFFF

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, position: int, value: str, mask: str) -> "Token":
        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], position=position, value=value, mask=mask),
        )


@register_command
@dataclass
class PEF_TPLDSETTINGS:
    """
    Defines if filtering on TPLD field in a packet is used for flow filtering. The
    TPLD filter allows filtering based on the Xena Testpayload ID. The Testpayload
    ID is meta data, which can be inserted into the Ethernet packets by Xena traffic
    generators. Each flow filter, can filter based on 16 TPLD ID values. NOTE: For
    SET, only allowed filter_type is "shadow-copy"(0).
    """

    code: typing.ClassVar[int] = 1730
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of TPLD information.

    @dataclass(frozen=True)
    class GetDataAttr:
        action: XmpField[XmpByte] = XmpField(XmpByte, choices=Clude)  # coded byte, specifies the usage of TPLD information.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, action: Clude) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], action=action))

    set_exclude = functools.partialmethod(set, Clude.EXCLUDE)
    set_include = functools.partialmethod(set, Clude.INCLUDE)


@register_command
@dataclass
class PEF_TPLDCONFIG:
    """
    Defines the TPLD filter configuration. NOTE: For SET, only allowed filter_type is
    "shadow-copy"(0). There are only 16 TPLD filter, thus the index values are from 0 to 15.
    """

    code: typing.ClassVar[int] = 1731
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).
    test_payload_filter_index: int # integer, the sub-index value which indicates the tpld filter index (range 0 to 15)

    @dataclass(frozen=True)
    class SetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of TPLD field information.
        id: XmpField[XmpInt] = XmpField(XmpInt)  # int, specifies the TPLD ID. Range: 0-2015, Default value: 0

    @dataclass(frozen=True)
    class GetDataAttr:
        usage: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifies the usage of TPLD field information.
        id: XmpField[XmpInt] = XmpField(XmpInt)  # int, specifies the TPLD ID. Range: 0-2015, Default value: 0

    def get(self) -> "Token[GetDataAttr]":
        """Get the TPLD filter configuration.

        :return: the usage of TPLD field information, and the TPLD ID. Range: 0-2015, Default value: 0
        :rtype: PEF_TPLDCONFIG.GetDataAttr
        """
        return Token(
            self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type, self.test_payload_filter_index])
        )

    def set(self, usage: OnOff, id: int) -> "Token":
        """Set the TPLD filter configuration.

        :param usage: specifies the usage of TPLD field information
        :type usage: OnOff
        :param id: specifies the TPLD ID. Range: 0-2015, Default value: 0
        :type id: int
        """
        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type, self.test_payload_filter_index], usage=usage, id=id),
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    set_on = functools.partialmethod(set, OnOff.ON)


@register_command
@dataclass
class PEF_VALUE:
    """
    Extended mode only. Defines byte values that can be matched if selected by the
    mask; see PEF_MASK. If segment_index is zero, the maximum number of match value
    bytes that can be set is determined by the total length of the segments
    specified with PEF_PROTOCOL. E.g. if PEF_PROTOCOL is set to ETHERNET then only
    12 bytes can be set. In order to set the full 128 bytes, either specify a
    detailed segment list, or use the raw segment type, e.g. 0/0 PEF_PROTOCOL [5,0]
    ETHERNET -116. This specifies 12 + 116 = 128 bytes. If segment_index is non-
    zero, only the bytes covered by that segment are manipulated, so if PEF_PROTOCOL
    is set to ETHERNET VLAN ETHERTYPE ECPRI, then segment_index = 4 selects the 8
    bytes of the eCPRI header starting at byte position (12 + 2 + 4) = 18. For "set"
    commands where fewer value bytes are provided than specified by the protocol
    segment, those unspecified bytes are set to zero. "get" commands always returns
    the number of bytes specified by the segment.
    """

    code: typing.ClassVar[int] = 1777
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        value: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, the raw bytes comprising the packet header.

    @dataclass(frozen=True)
    class GetDataAttr:
        value: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, the raw bytes comprising the packet header.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, pid: int, value: str) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], pid=pid, value=value))


@register_command
@dataclass
class PEF_MASK:
    """
    Extended mode only. Defines mask byte values that select the values specified by
    PEF_VALUE. For a chosen segment_index the first byte in the value masks the
    first byte of the corresponding PEF_VALUE, and so on. Get/set semantics are
    similar to PEF_VALUE; please see description there for details.
    """

    code: typing.ClassVar[int] = 1778
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int
    filter_type: FilterType # integer, the sub-index value which indicates the filter type - “shadow-copy”(0) or “working-copy”(1).

    @dataclass(frozen=True)
    class SetDataAttr:
        masks: XmpField[XmpHexList] = XmpField(XmpHexList)  #

    @dataclass(frozen=True)
    class GetDataAttr:
        masks: XmpField[XmpHexList] = XmpField(XmpHexList)  #

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type]))

    def set(self, pid: int, masks: str) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self.filter_type], pid=pid, masks=masks))


@register_command
@dataclass
class PEF_PROTOCOL:
    """
    Extended mode only. Defines the sequence of protocol segments that can be
    matched. The total length of the specified segments cannot exceed 128 bytes. If
    an existing sequence of segments is changed (using PEF_PROTOCOL) the underlying
    value and mask bytes remain unchanged, even though the semantics of those bytes
    may have changed. However, if the total length, in bytes, of the segments is
    reduced, then the excess bytes of value and mask are set to zero. I.e. to update
    an existing filter, you must first correct the list of segments (using
    PEF_PROTOCOL) and subsequently update the filtering value (using PEF_VALUE) and
    filtering mask (PEF_MASK).
    """

    code: typing.ClassVar[int] = 1779
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        segment_list: XmpField[XmpByteList] = XmpField(
            XmpByteList, choices=ProtocolOption
        )  # list of bytes, specifying the list of protocol segment types in the order they are expected in a frame. First segment type must be ETHERNET; the following can be chosen freely.

    @dataclass(frozen=True)
    class GetDataAttr:
        segment_list: XmpField[XmpByteList] = XmpField(
            XmpByteList, choices=ProtocolOption
        )  # list of bytes, specifying the list of protocol segment types in the order they are expected in a frame. First segment type must be ETHERNET; the following can be chosen freely.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))

    def set(self, segment_list: typing.List[ProtocolOption]) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex], segment_list=segment_list))


@register_command
@dataclass
class PEF_MODE:
    """ """

    code: typing.ClassVar[int] = 1780
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        sid: XmpField[XmpByte] = XmpField(XmpByte, choices=Flow)  # integer, the sub-index value of the flow definition.

    @dataclass(frozen=True)
    class GetDataAttr:
        sid: XmpField[XmpByte] = XmpField(XmpByte, choices=Flow)  # integer, the sub-index value of the flow definition.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))

    def set(self, sid: Flow) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex], sid=sid))

    set_basic = functools.partialmethod(set, Flow.BASIC)
    set_extended = functools.partialmethod(set, Flow.EXTENDED)


