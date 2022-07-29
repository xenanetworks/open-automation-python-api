import asyncio
from typing import List

from xoa_driver.internals.core.commands import (
    P_CAPABILITIES,
    P4_CAPABILITIES,
    P_RECEIVESYNC,
    P_RESERVEDBY,
    P_RESERVATION,
    P_INTERFACE,
    P_TRAFFIC,
    P4_STATE,
) 
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.core.transporter import funcs
from xoa_driver.internals.core.commands import enums

from ._speed_detector import SpeedDetector
class PortLocalState:
    __slots__ = (
        "model",
        "serial_number",
        "interface",
        "reservation",
        "reserved_by",
        "sync_status"
    )
    def __init__(self) -> None:
        self.model: str = ""
        self.serial_number: int = 0
        self.interface: str = ""
        self.reservation: "enums.ReservedStatus" = enums.ReservedStatus.RELEASED
        self.reserved_by: str = ""
        self.sync_status: "enums.SyncStatus" = enums.SyncStatus.NO_SYNC
    
    async def initiate(self, port) -> None:
        (
            sync_status_r,
            interface_r,
            reservation_r,
            reserved_by_r,
        ) = await funcs.apply(
            port.sync_status.get(),
            port.interface.get(),
            port.reservation.get(),
            port.reserved_by.get(),
        )
        self.sync_status = enums.SyncStatus(sync_status_r.sync_status)
        self.interface = interface_r.interface
        self.reservation = enums.ReservedStatus(reservation_r.status)
        self.reserved_by = reserved_by_r.username
    
    def register_subscriptions(self, port) -> None:
        port._conn.subscribe(P_RECEIVESYNC, utils.Update(self, "sync_status", "sync_status", port._check_identity, format=lambda a: enums.SyncStatus(a)))
        port._conn.subscribe(P_RESERVEDBY, utils.Update(self, "reserved_by", "username", port._check_identity))
        port._conn.subscribe(P_RESERVATION, utils.Update(self, "reservation", "status", port._check_identity, format=lambda a: enums.ReservedStatus(a)))
        port._conn.subscribe(P_INTERFACE, utils.Update(self, "interface", "interface", port._check_identity))


class PortChimeraLocalState(PortLocalState):
    __slots__ = ("capabilities",)
    capabilities: "P_CAPABILITIES.GetDataAttr"

    async def initiate(self, port) -> None:
        capabilities, _ = await asyncio.gather(
            port.capabilities.get(),
            super().initiate(port)
        )
        self.capabilities = capabilities

class PortL23LocalState(PortLocalState):
    __slots__ = (
        "capabilities", 
        "traffic_state"
    )
    capabilities: "P_CAPABILITIES.GetDataAttr"
    
    def __init__(self) -> None:
        self.traffic_state: "enums.TrafficOnOff" = enums.TrafficOnOff.OFF
        
    
    async def initiate(self, port) -> None:
        capabilities, traffic_state_r, _ = await asyncio.gather(
            port.capabilities.get(),
            port.traffic.state.get(),
            super().initiate(port)
        )
        self.capabilities = capabilities
        self.traffic_state = enums.TrafficOnOff(traffic_state_r.on_off)
    
    def register_subscriptions(self, port) -> None:
        super().register_subscriptions(port)
        port._conn.subscribe(P_TRAFFIC, utils.Update(self, "traffic_state", "on_off", port._check_identity, format=lambda a: enums.TrafficOnOff(a)))

class PortL23GenuineLocalState(PortL23LocalState):
    __slots__ = ("port_possible_speed_modes",)
    
    def __init__(self) -> None:
        self.port_possible_speed_modes: List["enums.PortSpeedMode"] = []
    
    async def initiate(self, port) -> None:
        await super().initiate(port)
        speed_detector = SpeedDetector(
            self.capabilities,
            self.interface
        )
        self.port_possible_speed_modes = speed_detector.find_port_possible_speed()
    
    @property
    def is_brr_mode_supported(self) -> bool:
        """Whether this L23 port supports BRR mode.

        :return: whether this port supports BRR mode.
        :rtype: bool
        """
        return "T1" in self.interface



class PortL47LocalState(PortLocalState):
    __slots__ = (
        "capabilities",
        "traffic_state",
    )
    capabilities: "P4_CAPABILITIES.GetDataAttr"
    
    def __init__(self) -> None:
        self.traffic_state: "enums.L47PortState" = enums.L47PortState.OFF
    
    async def initiate(self, port) -> None:
        capabilities, traffic_state_r, _ = await asyncio.gather(
            port.capabilities.get(),
            port.state.get(),
            super().initiate(port)
        )
        self.capabilities = capabilities
        self.traffic_state = enums.L47PortState(traffic_state_r.state)
    
    def register_subscriptions(self, port) -> None:
        super().register_subscriptions(port)
        port._conn.subscribe(P4_STATE, utils.Update(self, "traffic_state", "state", port._check_identity, format=lambda a: enums.L47PortState(a)))