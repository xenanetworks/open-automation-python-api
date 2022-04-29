from typing import (
    TYPE_CHECKING,
    List,
    TypeVar,
    Type,
)
from xoa_driver.internals.core.commands import (
    PL_INDICES,
    PL_CREATE,
    PL_DELETE,
    PL_LENGTH,
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
from xoa_driver.internals.utils.indices import observer as idx_obs
from .base_index import BaseIndex


LT = TypeVar("LT")
class LengthTermIdx(BaseIndex):
    """L23 Length Term Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        self.length = PL_LENGTH(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pl_commands.PL_LENGTH`"""
    
    async def delete(self):
        await PL_DELETE(self._conn, *self.kind).set()
        """Representation of :class:`~xoa_driver.internals.core.commands.pl_commands.PL_DELETE`"""
        self._observer.notify(idx_obs.IndexEvents.DEL, self)
    
    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await PL_INDICES(conn, module_id, port_id).get()
        return list(resp.length_term_xindices)
    
    @classmethod
    async def _new(cls: Type[LT], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> LT:
        await PL_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)