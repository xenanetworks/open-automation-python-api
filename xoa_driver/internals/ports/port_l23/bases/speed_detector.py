from typing import (
    TYPE_CHECKING,
    List,
)
from enum import (
    Enum,
    auto
)
from xoa_driver.internals.core.commands import enums
if TYPE_CHECKING:
    from xoa_driver.internals.core.commands import P_CAPABILITIES

class EPortInterfaceSubtype(Enum):
    Unspecified = auto()
    Single = auto()
    Dual = auto()
    Triple = auto()
    Quint = auto()


class SpeedDetector:
    """
    Work around of ports speed detection. Only for Genuine L23 ports.
    Keep it as a class for not couple all logic under one function.
    """
    __slots__ = ("capabilities", "interface")
    def __init__(self, capabilities: "P_CAPABILITIES.GetDataAttr", interface: str) -> None:
        self.capabilities = capabilities
        self.interface = interface
    
    @property
    def __determinate_interface_subtype(self) -> EPortInterfaceSubtype:
        if "[Triple]" in self.interface:
            return EPortInterfaceSubtype.Triple
        elif "[Quint]" in self.interface:
            return EPortInterfaceSubtype.Quint
        elif "[Dual]" in self.interface:
            return EPortInterfaceSubtype.Dual
        elif "[Single]" in self.interface:
            return EPortInterfaceSubtype.Single
        return EPortInterfaceSubtype.Unspecified
    
    @property
    def can_set_port_speed(self) -> bool:
        return self.__determinate_interface_subtype in {
            EPortInterfaceSubtype.Triple,
            EPortInterfaceSubtype.Quint,
            EPortInterfaceSubtype.Dual,
            EPortInterfaceSubtype.Single
        }
    
    def __define_single(self) -> List[enums.PortSpeedMode]:
        if "T1S" in self.interface:
            return [
                enums.PortSpeedMode.AUTO,
                enums.PortSpeedMode.F100M,
                enums.PortSpeedMode.F1G,
            ]
        return []
    
    def __define_dual(self) -> List[enums.PortSpeedMode]:
        if "T1" in self.interface:
            return [enums.PortSpeedMode.F10MHDX,]
        return []

    def __define_triple(self) -> List[enums.PortSpeedMode]:
        if self.interface.startswith("SFP"):
            if self.capabilities.max_speed == 1_000:
                return [
                    enums.PortSpeedMode.AUTO,
                    enums.PortSpeedMode.F10M,
                    enums.PortSpeedMode.F100M,
                    enums.PortSpeedMode.F1G,
                    enums.PortSpeedMode.F10M100M,
                    enums.PortSpeedMode.F100M1G,
                    enums.PortSpeedMode.F10MHDX,
                    enums.PortSpeedMode.F100MHDX,
                ]
            elif self.capabilities.max_speed == 10_000:
                return [
                    enums.PortSpeedMode.AUTO,
                    enums.PortSpeedMode.F100M,
                    enums.PortSpeedMode.F1G,
                    enums.PortSpeedMode.F10G,
                    enums.PortSpeedMode.F100M1G,
                ]
        elif self.interface.startswith("10GBASE-T"):
            return [
                enums.PortSpeedMode.AUTO,
                enums.PortSpeedMode.F100M,
                enums.PortSpeedMode.F1G,
                enums.PortSpeedMode.F10G,
                enums.PortSpeedMode.F100M1G,
            ]
        return []

    def __define_quint(self) -> List[enums.PortSpeedMode]:
        speeds =  [
            enums.PortSpeedMode.AUTO,
            enums.PortSpeedMode.F100M,              
            enums.PortSpeedMode.F1G,                 
            enums.PortSpeedMode.F2500M,         
            enums.PortSpeedMode.F5G,           
            enums.PortSpeedMode.F100M1G,
            enums.PortSpeedMode.F100M1G2500M,
        ]
        if self.interface.startswith("10GBASE-T"):
            speeds.append(enums.PortSpeedMode.F10G)
        return speeds
    
    def find_port_possible_speed(self) -> List[enums.PortSpeedMode]:
        if not self.can_set_port_speed:
            return []
        define_func = {
            EPortInterfaceSubtype.Single: self.__define_single,
            EPortInterfaceSubtype.Dual: self.__define_dual,
            EPortInterfaceSubtype.Triple: self.__define_triple,
            EPortInterfaceSubtype.Quint: self.__define_quint
        }.get(self.__determinate_interface_subtype, lambda: [])
        return define_func()