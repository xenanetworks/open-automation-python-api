from typing import (
    Protocol,
    List,
    Type,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import kind
    from . import observer


class IIndexType(Protocol):
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> None: ...
    
    async def delete(self) -> None: ...
    
    @property
    def idx(self) -> int: ...
    
    @classmethod
    async def _fetch(cls, conn, module_id, port_id) -> List[int]: ...
    
    @classmethod
    async def _new(cls, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> Type: ...