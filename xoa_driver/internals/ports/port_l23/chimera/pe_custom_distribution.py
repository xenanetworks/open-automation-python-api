from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    PEC_INDICES,
    PEC_VAL,
    PEC_COMMENT,
    PEC_DELETE,
    PEC_DISTTYPE,
)

from xoa_driver.internals.utils.indices import observer # import IndicesObserver, IndexEvents
class CustomDistribution:
    """Custom distribution"""
    def __init__(self, observer: "observer.IndicesObserver", conn: "itf.IConnection", module_id: int, port_id: int, custom_distribution_index: int) -> None:
        self.__observer = observer
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__cdi = custom_distribution_index
        self.definition = PEC_VAL(conn, module_id, port_id, custom_distribution_index)
        """Custom distribution defintion.
        Representation of :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_VAL`
        """
        self.comment = PEC_COMMENT(conn, module_id, port_id, custom_distribution_index)
        """Custom distribution description.
        Representation of :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_COMMENT`
        """
        self.type = PEC_DISTTYPE(conn, module_id, port_id, custom_distribution_index)
        """Custom distribution type.
        Representation of :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_DISTTYPE`
        """
    
    async def delete(self) -> None:
        """
        Deleting an existing Custom Distribution
        """
        await PEC_DELETE(
            self.__conn, 
            self.__module_id,
            self.__port_id,
            self.__cdi
        ).set()
        self.__observer.notify(observer.IndexEvents.DEL, self)


class CustomDistributions:
    """Custom distributions"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__items: List[CustomDistribution] = []
        self.__observer = observer.IndicesObserver()
        self.__observer.subscribe(
            observer.IndexEvents.DEL, 
            self.__remove_from_slot
        )
    
    async def server_sync(self) -> None:
        """Sync the indices with xenaserver"""
        _resp = await PEC_INDICES(self.__conn, self.__module_id, self.__port_id).get()
        self.__items = [
            CustomDistribution(
                self.__observer,
                self.__conn, 
                self.__module_id, 
                self.__port_id, 
                idx
            )
            for idx in _resp.indices
        ]

    def __len__(self) -> int:
        """Return the number of existing indices"""
        return len(self.__items)

    def __iter__(self):
        self.__k = 0
        return self

    def __next__(self):
        try:
            v = self.__items[self.__k]
        except IndexError:
            raise StopIteration()
        else:
            self.__k += 1
            return v

    def __getitem__(self, key: int):
        return self.__items[key]

    def __remove_from_slot(self, index_inst: "CustomDistribution") -> None:
        # throws ValueError if element is not exists in list of indices 
        self.__items.remove(index_inst)

    async def assign(self, idx_cuantity: int = 0 ) -> None:
        """
        Assign Custom distribution indices, all indices which is out of range will be removed.
        ``idx_cuantity`` permitted values is: 0 <= idx_cuantity <= 40
        """
        if not (0 < idx_cuantity < 40):
            raise ValueError("idx_cuantity must be in range of: 0 <= idx_cuantity <= 40")
        await PEC_INDICES(self.__conn, self.__module_id, self.__port_id).set([i for i in range(idx_cuantity) ])
        await self.server_sync()

    async def remove(self, position_idx: int) -> None:
        """Remove a index from port"""
        await self.__items[position_idx].delete()