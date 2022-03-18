import asyncio
import functools
from typing import (
    TYPE_CHECKING,
    Type, 
    TypeVar,
    List,
    Callable,
    Union,

)
from collections import OrderedDict
from dataclasses import dataclass

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    M_REVISION, 
    M_MODEL
)
from ._base_manager import ResourcesBaseManager
from xoa_driver.internals import exceptions

@dataclass
class ModuleData:
    module_id: int
    ports_count: int
    revision: str = ""


class L23ModuleData(ModuleData):
    async def get_revision(self, conn) -> None:
        r = await M_REVISION(conn, self.module_id).get()
        self.revision = r.revision

class L47ModuleData(ModuleData):
    async def get_revision(self, conn) -> None:
        r = await M_MODEL(conn, self.module_id).get()
        self.revision = r.model


MT = TypeVar("MT")
MTypeObtainer = Callable[[str], Type]
ModuleDataType = Union[Type["L23ModuleData"], Type["L47ModuleData"]]

class ModulesManager(ResourcesBaseManager[MT]):
    
    __slots__ = ("_conn", "__m_types_obtainer")
    
    def __init__(self, conn: "itf.IConnection", m_types_obtainer: MTypeObtainer) -> None:
        super().__init__()
        self._conn = conn
        self.__m_types_obtainer = m_types_obtainer

    async def fill(self, ports_count: List[int], module_type: ModuleDataType) -> None:
        """Method for create and fill in."""
        assert not self._lock, "Method <fill> can be called only once."
        identities = [
            module_type(
                module_id=slot_id, 
                ports_count=p_count
            ) 
            for slot_id, p_count in enumerate(ports_count)
            if p_count > 0
        ]
        await asyncio.gather( *[ mi.get_revision(self._conn) for mi in identities ] )
        self._items = OrderedDict(
            (
                idnt.module_id,
                self.__m_types_obtainer(idnt.revision)(self._conn, idnt)
            ) 
            for idnt in identities
        )
        if len(self) == 0:
            raise exceptions.WrongTesterError()
        coros = list(self._items.values())
        await asyncio.gather(*coros) # type: ignore
    
    fill_l23 = functools.partialmethod(fill, module_type=L23ModuleData)
    fill_l47 = functools.partialmethod(fill, module_type=L47ModuleData)

