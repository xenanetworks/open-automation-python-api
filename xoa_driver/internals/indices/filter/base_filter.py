from typing import (
    TYPE_CHECKING,
    List,
    Type,
    TypeVar,
)
from xoa_driver.internals.core.commands import (
    PF_INDICES,
    PF_CREATE,
    PF_DELETE,
    PF_ENABLE,
    PF_COMMENT,
    PF_CONDITION,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
from xoa_driver.internals.utils.indices import observer as idx_obs
from ..base_index import BaseIndex


FT = TypeVar("FT")
class BaseFilterIdx(BaseIndex):
    """Base L23 Filter Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        
        self.comment = PF_COMMENT(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pf_commands.PF_COMMENT`"""
        self.enable = PF_ENABLE(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pf_commands.PF_ENABLE`"""
        self.condition = PF_CONDITION(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pf_commands.PF_CONDITION`"""
    
    async def delete(self):
        """Representation of :class:`~xoa_driver.internals.core.commands.pf_commands.PF_DELETE`"""
        await PF_DELETE(self._conn, *self.kind).set()
        self._observer.notify(idx_obs.IndexEvents.DEL, self)
    
    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await PF_INDICES(conn, module_id, port_id).get()
        return list(resp.filter_xindices)
    
    @classmethod
    async def _new(cls: Type[FT], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> FT:
        await PF_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)