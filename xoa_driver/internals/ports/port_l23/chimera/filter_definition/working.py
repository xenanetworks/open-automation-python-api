from typing import (
    Dict,
    Type,
    Union, 
    TYPE_CHECKING
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands.enums import (
    FilterType, 
    FilterMode,
)
from . import general


class FilterDefinitionWorking:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self._conn = conn
        self._module_id = module_id
        self._port_id = port_id
        self._flow_index = flow_index
        self._filter_type = FilterType.WORKING
    
    async def get_mode(self) -> Union[general.ModeBasic, general.ModeExtended]:
        mode_types: Dict[FilterMode ,Type[Union[general.ModeBasic, general.ModeExtended]]] = {
            FilterMode.BASIC: general.ModeBasic,
            FilterMode.EXTENDED: general.ModeExtended,
        }
        return await general.get_mode(
            self._conn, 
            self._module_id, 
            self._port_id, 
            self._flow_index, 
            self._filter_type,
            mode_types
        )
