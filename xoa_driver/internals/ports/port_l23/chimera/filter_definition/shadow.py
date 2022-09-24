from typing import (
    TYPE_CHECKING,
    Dict,
    Type,
    Union
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands.enums import (
    FilterType, 
    ProtocolOption,
    FilterMode,
)
from xoa_driver.internals.core.commands import (
    PEF_INIT,
    PEF_APPLY,
    PEF_ENABLE,
    PEF_PROTOCOL,
    PEF_MODE,
)
from . import general

class ModeExtendedS(general.ModeExtended):
    async def use_segments(self, *segments: ProtocolOption) -> None:
        segments_payload = [ 
            ProtocolOption.ETHERNET, 
            *segments
        ]
        await PEF_PROTOCOL(
            self._conn, 
            self._module_id, 
            self._port_id, 
            self._flow_index, 
            self._filter_type
        ).set(segments_payload)


class FilterDefinitionShadow:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self._conn = conn
        self._module_id = module_id
        self._port_id = port_id
        self._flow_index = flow_index
        self._filter_type = FilterType.SHADOW
        
        
        self.initiating = PEF_INIT(conn, module_id, port_id, flow_index)
        """Preparing filter definition.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_INIT`
        """
        self.apply = PEF_APPLY(conn, module_id, port_id, flow_index)
        """Apply filter defintion.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_APPLY`
        """
        self.enable = PEF_ENABLE(conn, module_id, port_id, flow_index, self._filter_type)
        """Enabling the filter.
        Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_ENABLE`
        """
        # self.mode = PEF_MODE(conn, module_id, port_id, flow_index, self._filter_type)
        # """Filter mode.
        # Representation of :class:`~xoa_driver.internals.core.commands.pef_commands.PEF_MODE`
        # """
    
    async def get_mode(self) -> Union[general.ModeBasic, ModeExtendedS]:
        mode_types: Dict[FilterMode, Type[Union[general.ModeBasic, ModeExtendedS]]] = {
            FilterMode.BASIC: general.ModeBasic,
            FilterMode.EXTENDED: ModeExtendedS,
        }
        return await general.get_mode(
            self._conn, 
            self._module_id, 
            self._port_id, 
            self._flow_index, 
            self._filter_type,
            mode_types
        )
    
    async def use_basic_mode(self) -> None:
        await PEF_MODE(
            self._conn, 
            self._module_id, 
            self._port_id, 
            self._flow_index, 
            self._filter_type,
        ).set_basic()

    async def use_extended_mode(self) -> None:
        await PEF_MODE(
            self._conn, 
            self._module_id, 
            self._port_id, 
            self._flow_index, 
            self._filter_type,
        ).set_extended()