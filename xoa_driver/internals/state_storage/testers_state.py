from dataclasses import dataclass
from typing import (
    Optional,
    TYPE_CHECKING,
    Final,
)
from xoa_driver.internals.core.commands import enums
if TYPE_CHECKING:
    from xoa_driver.internals.core.commands import C_CAPABILITIES

@dataclass
class TesterLocalState:
    host: Final[str]
    port: Final[int]
    model: str = ""
    capabilities: Optional["C_CAPABILITIES.GetDataAttr"] = None
    serial_number: int = 0
    version_major: int = 0
    driver_version: int = 0
    reservation: enums.ReservedStatus = enums.ReservedStatus.RELEASED
    reserved_by: str = ""

@dataclass
class GenuineTesterLocalState(TesterLocalState):
    buildstring: str = ""