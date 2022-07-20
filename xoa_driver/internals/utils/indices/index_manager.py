import asyncio
from typing import (
    List,
    Type,
    Generic, 
    TypeVar,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ._interfaces import IIndexType

from . import observer
from .. import kind


IT = TypeVar("IT", bound="IIndexType")

class IndexManager(Generic[IT]):
    __slots__ = ("_conn", "_idx_type", "_module_id", "_port_id", "_indices", "_lock", "_observer")
    
    def __init__(self, conn: "itf.IConnection", idx_type: Type[IT], module_id: int, port_id: int) -> None:
        self._conn = conn
        self._idx_type = idx_type
        self._module_id = module_id
        self._port_id = port_id
        self._indices: List[IT] = []
        self._lock = asyncio.Lock()
        self._observer: "observer.IndicesObserver" = observer.IndicesObserver()
        self._observer.subscribe(
            observer.IndexEvents.DEL, 
            self.__remove_from_slot
        )
    
    async def server_sync(self) -> None:
        """Sync the indices with xenaserver"""
        self._indices.clear()
        idxs: List[int] = await self._idx_type._fetch(self._conn, self._module_id, self._port_id)
        for idx_id in idxs:
            index_kind = kind.IndicesKind(
                self._module_id, 
                self._port_id, 
                idx_id
            )
            idx_instance = self._idx_type(self._conn, index_kind, self._observer)
            self._indices.append(idx_instance)

    def __str__(self) -> str:
        return f"Iterable[{self._idx_type.__name__}]({self._indices!s})"

    def __len__(self) -> int:
        """Return the number of existing indices"""
        return len(self._indices)

    def __iter__(self):
        return iter(self._indices)

    def obtain(self, key: int):
        return self._indices[key]
    
    def obtain_multiple(self, *keys: int):
        """Obtain multiple resources as a tuple of indices"""
        return tuple(self._indices[k] for k in keys)

    def __detect_empty_idx_slot(self) -> int:
        if len(self._indices) == 0:
            return 0
        existing_indices = [i.idx for i in self._indices]
        l = [
            ele
            for ele in range(max(existing_indices) + 1)
            if ele not in existing_indices
        ]
        return min(l) if l else len(existing_indices)

    def __remove_from_slot(self, index_inst: Type) -> None:
        # throws ValueError if element is not exists in list of indices 
        self._indices.remove(index_inst)

    async def create(self):
        async with self._lock:
            index_kind = kind.IndicesKind(
                self._module_id, 
                self._port_id, 
                self.__detect_empty_idx_slot()
            )
            index_inst: IT = await self._idx_type._new(self._conn, index_kind, self._observer)
            assert index_inst, f"Failed to create Index: {len(self)}"
            self._indices.append(index_inst)
            return index_inst

    async def remove(self, position_idx: int) -> None:
        """Remove an index from the port"""
        await self._indices[position_idx].delete()
