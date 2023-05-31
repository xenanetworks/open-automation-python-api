from typing import (
    TYPE_CHECKING,
    Dict,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PEC_INDICES,
    PEC_VAL,
    PEC_COMMENT,
    PEC_DELETE,
    PEC_DISTTYPE,
)

from xoa_driver.internals.utils.indices import observer
from xoa_driver.enums import (
    OnOff,
)


class CustomDistribution:
    """Custom distribution"""

    def __init__(self, observer: "observer.IndicesObserver", conn: "itf.IConnection", module_id: int, port_id: int, cust_id: int) -> None:
        self.__observer = observer
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.cust_id = cust_id
        self.definition = PEC_VAL(conn, module_id, port_id, cust_id)
        """Custom distribution definition.
        Representation of PEC_VAL
        """

        self.comment = PEC_COMMENT(conn, module_id, port_id, cust_id)
        """Custom distribution description.
        Representation of PEC_COMMENT
        """

        self.type = PEC_DISTTYPE(conn, module_id, port_id, cust_id)
        """Custom distribution type.
        Representation of PEC_DISTTYPE
        """

    async def delete(self) -> None:
        """
        Deleting an existing Custom Distribution
        """

        await PEC_DELETE(
            self.__conn,
            self.__module_id,
            self.__port_id,
            self.cust_id
        ).set()
        self.__observer.notify(observer.IndexEvents.DEL, self)


class CustomDistributions:
    """Custom distributions"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__items: Dict[int, CustomDistribution] = {}
        self.__observer = observer.IndicesObserver()
        self.__observer.subscribe(
            observer.IndexEvents.DEL,
            self.__remove_from_slot
        )

    async def server_sync(self) -> None:
        """Sync the indices with xenaserver"""

        _resp = await PEC_INDICES(self.__conn, self.__module_id, self.__port_id).get()
        self.__items = {
            idx: CustomDistribution(
                self.__observer,
                self.__conn,
                self.__module_id,
                self.__port_id,
                idx
            )
            for idx in _resp.indexations
        }

    def __len__(self) -> int:
        """Return the number of existing indices"""
        return len(self.__items)

    def items(self):
        return self.__items.items()

    def keys(self):
        return self.__items.keys()

    def values(self):
        return self.__items.values()

    def __getitem__(self, key: int):
        return self.__items[key]

    def __setitem__(self, key: int, cd_inst: "CustomDistribution"):
        self.__items[key] = cd_inst

    def __remove_from_slot(self, index_inst: "CustomDistribution") -> None:
        # throws ValueError if element is not exists in list of indices
        del self.__items[index_inst.cust_id]

    async def add(self, cust_id: int, linear: OnOff, entry_count: int, data_x: List[int], comment: str) -> "CustomDistribution":
        cd = CustomDistribution(
            self.__observer,
            self.__conn,
            self.__module_id,
            self.__port_id,
            cust_id,
        )
        await cd.definition.set(linear=linear, symmetric=OnOff.OFF, entry_count=entry_count, data_x=data_x)
        await cd.comment.set(comment)
        self[cust_id] = cd
        return cd

    async def remove(self, position_idx: int) -> None:
        """Remove a index from port"""
        await self.__items[position_idx].delete()
