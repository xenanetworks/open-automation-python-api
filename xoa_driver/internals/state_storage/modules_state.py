from typing import List
from dataclasses import (
    dataclass, 
    field,
)
from xoa_driver.internals.core.commands import enums

@dataclass
class ModuleLocalState:
    reservation: enums.ReservedStatus = enums.ReservedStatus.RELEASED
    reserved_by: str = ""
    model: str = ""



@dataclass(frozen=True)
class ModuleSpeed:
    port_count: int
    port_speed: int

@dataclass(frozen=True)
class MediaInfo:
    cage_type: "enums.MediaType"
    avaliable_speeds: List["ModuleSpeed"] = field(default_factory=list)

@dataclass
class ModuleL23LocalState(ModuleLocalState):
    __media_info_list: List["MediaInfo"] = field(init=False, repr=False, default_factory=list)
    
    @property
    def media_info_list(self) -> List["MediaInfo"]:
        return self.__media_info_list
    
    @media_info_list.setter
    def media_info_list(self, value: List[int]) -> None:
        self.__media_info_list.clear()
        _vs = value[:]
        while _vs:
            cage_type = enums.MediaType(_vs.pop(0))
            available_speeds_count = _vs.pop(0)
            mi = MediaInfo(
                cage_type,
                [ 
                    ModuleSpeed(_vs.pop(0), _vs.pop(0))
                    for _ in range(available_speeds_count)
                ]
            )
            self.__media_info_list.append(mi)