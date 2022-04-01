from typing import List
from dataclasses import (
    dataclass, 
    field,
)
from xoa_driver.internals.core.commands import enums
from xoa_driver.internals.core.commands import (
    P_CAPABILITIES,
    P4_CAPABILITIES,
) 

@dataclass
class PortLocalState:
    model: str = ""
    serial_number: int = 0
    interface: str = ""
    reservation: "enums.ReservedStatus" = enums.ReservedStatus.RELEASED
    reserved_by: str = ""
    sync_status: "enums.SyncStatus" = enums.SyncStatus.NO_SYNC

@dataclass
class PortChimeraLocalState(PortLocalState):
    capabilities: "P_CAPABILITIES.GetDataAttr" = field(init=False)

@dataclass
class PortL23LocalState(PortLocalState):
    capabilities: "P_CAPABILITIES.GetDataAttr" = field(init=False)
    port_possible_speed_modes: List["enums.PortSpeedMode"] = field(default_factory=list)
    traffic_state: "enums.TrafficOnOff" = enums.TrafficOnOff.OFF

@dataclass
class PortL47LocalState(PortLocalState):
    capabilities: "P4_CAPABILITIES.GetDataAttr" = field(init=False)
    traffic_state: "enums.L47PortState" = enums.L47PortState.OFF