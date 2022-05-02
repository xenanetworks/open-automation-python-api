from typing import (
    TYPE_CHECKING,
    List,
    TypeVar,
    Type,
)
from xoa_driver.internals.core.commands import (
    PD_INDICES,
    PD_CREATE,
    PD_DELETE,
    PD_ENABLE,
    PD_SOURCE,
    PD_RANGE,
    PD_SAMPLES,
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
from xoa_driver.internals.utils.indices import observer as idx_obs
from .base_index import BaseIndex


PD = TypeVar("PD")

class PortDatasetIdx(BaseIndex):
    """L23 Histogram Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        self.enable = PD_ENABLE(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pd_commands.PD_ENABLE`"""
        self.source = PD_SOURCE(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pd_commands.PD_SOURCE`"""
        self.range = PD_RANGE(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pd_commands.PD_RANGE`"""
        self.samples = PD_SAMPLES(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.pd_commands.PD_SAMPLES`"""
        
    
    async def delete(self):
        await PD_DELETE(self._conn, *self.kind).set()
        """Representation of :class:`~xoa_driver.internals.core.commands.pd_commands.PD_ENABLE`"""
        self._observer.notify(idx_obs.IndexEvents.DEL, self)
    
    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await PD_INDICES(conn, module_id, port_id).get()
        return list(resp.histogram_indices)
    
    @classmethod
    async def _new(cls: Type[PD], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> PD:
        await PD_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)