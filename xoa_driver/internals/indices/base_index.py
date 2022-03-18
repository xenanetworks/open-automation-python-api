import abc
from typing import (
    List,
    TypeVar,
    Type,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
    from xoa_driver.internals.utils.indices import observer


CT = TypeVar("CT")
class BaseIndex(abc.ABC):
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> None:
        self._observer = observer
        self._conn = conn
        self.kind = kind
    
    @property
    def idx(self) -> int:
        return self.kind.index_id
    
    @abc.abstractmethod
    async def delete(self) -> None: ...
    
    @classmethod
    @abc.abstractmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]: ...
    
    @classmethod
    @abc.abstractmethod
    async def _new(cls: Type[CT], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> CT: ...