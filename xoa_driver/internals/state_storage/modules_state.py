import asyncio
from typing import List
from dataclasses import (
    dataclass, 
    field,
)

from xoa_driver.internals.core.commands import (
    M_MODEL, 
    M_RESERVATION,
    M_RESERVEDBY, 
    M_MEDIASUPPORT,
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.core.transporter import funcs
from xoa_driver.internals.core.commands import enums


class ModuleLocalState:
    __slots__ = (
        "reservation",
        "reserved_by",
        "model",
    )
    def __init__(self) -> None:
        self.reservation: enums.ReservedStatus = enums.ReservedStatus.RELEASED
        self.reserved_by: str = ""
        self.model: str = ""

    async def initiate(self, module) -> None:
        (
            reservation_r,
            reserved_by_r,
            model_r,
        ) = await funcs.apply(
            module.reservation.get(),
            module.reserved_by.get(),
            module.model.get(),
        )
        self.reservation = reservation_r.operation
        self.reserved_by = reserved_by_r.username
        self.model = model_r.model
    
    def register_subscriptions(self, module) -> None:
        module._conn.subscribe(M_RESERVEDBY, utils.Update(self, "reserved_by", "username", module._check_identity))
        module._conn.subscribe(M_RESERVATION, utils.Update(self, "reservation", "operation", module._check_identity, format=lambda a: enums.ReservedStatus(a)))
        module._conn.subscribe(M_MODEL, utils.Update(self, "model", "model", module._check_identity))


@dataclass(frozen=True)
class ModuleSpeed:
    port_count: int
    port_speed: int

@dataclass(frozen=True)
class MediaInfo:
    cage_type: "enums.MediaConfigurationType"
    avaliable_speeds: List["ModuleSpeed"] = field(default_factory=list)


class ModuleL23LocalState(ModuleLocalState):
    __slots__ = ("__media_info_list",)
    
    def __init__(self) -> None:
        self.__media_info_list: List["MediaInfo"] = []
    
    @property
    def media_info_list(self) -> List["MediaInfo"]:
        return self.__media_info_list
    
    @media_info_list.setter
    def media_info_list(self, value: List[int]) -> None:
        self.__media_info_list.clear()
        _vs = value[:]
        while _vs:
            cage_type = enums.MediaConfigurationType(_vs.pop(0))
            available_speeds_count = _vs.pop(0)
            mi = MediaInfo(
                cage_type,
                [ 
                    ModuleSpeed(_vs.pop(0), _vs.pop(0))
                    for _ in range(available_speeds_count)
                ]
            )
            self.__media_info_list.append(mi)
    
    async def initiate(self, module) -> None:
        m_support_resp, _ = await asyncio.gather(
            M_MEDIASUPPORT(module._conn, module.module_id).get(),
            super().initiate(module)
        )
        self.media_info_list = m_support_resp.media_info_list # type: ignore
    
    def register_subscriptions(self, module) -> None:
        super().register_subscriptions(module)
        module._conn.subscribe(M_MEDIASUPPORT, utils.Update(self, "media_info_list", "media_info_list", module._check_identity))