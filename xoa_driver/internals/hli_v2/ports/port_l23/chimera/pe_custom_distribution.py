from typing import (
    TYPE_CHECKING,
    Dict,
    List,
)
from collections import UserDict
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
from xoa_driver.enums import OnOff


class CustomDistribution:
    """Custom distribution"""

    def __init__(self, observer: "observer.IndicesObserver", conn: "itf.IConnection", module_id: int, port_id: int, custom_distribution_index: int) -> None:
        self.__observer = observer
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.custom_distribution_index = custom_distribution_index
        self.definition = PEC_VAL(conn, module_id, port_id, custom_distribution_index)
        """Custom distribution definition.
        Representation of PEC_VAL
        """

        self.comment = PEC_COMMENT(conn, module_id, port_id, custom_distribution_index)
        """Custom distribution description.
        Representation of PEC_COMMENT
        """

        self.type = PEC_DISTTYPE(conn, module_id, port_id, custom_distribution_index)
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
            self.custom_distribution_index
        ).set()
        self.__observer.notify(observer.IndexEvents.DEL, self)


class CustomDistributions(UserDict):
    """Custom distributions"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.data: Dict[int, CustomDistribution] = {}
        self.__observer = observer.IndicesObserver()
        self.__observer.subscribe(
            observer.IndexEvents.DEL,
            self.__remove_from_slot
        )

    async def server_sync(self) -> None:
        """Sync the indices with xenaserver"""
        _resp = await PEC_INDICES(self.__conn, self.__module_id, self.__port_id).get()
        self.data = {
            idx: CustomDistribution(
                self.__observer,
                self.__conn,
                self.__module_id,
                self.__port_id,
                idx
            )
            for idx in _resp.indexations
        }

    def __remove_from_slot(self, index_inst: "CustomDistribution") -> None:
        # throws ValueError if element is not exists in list of indices
        del self.data[index_inst.custom_distribution_index]

    def __setitem__(self, key, value):
        raise NotImplementedError("Only support assign item by 'add' method")

    async def remove(self, custom_distribution_index: int) -> None:
        """Remove a index from port"""
        await self.data[custom_distribution_index].delete()

    async def __get_available_custom_distribution_index(self) -> int:
        await self.server_sync()
        if len(self.keys()) == 40:
            raise ValueError("The server was full of custom distributions.")
        return next(i for i in range(1, 41) if i not in self.keys())

    async def add(self, linear: OnOff, entry_count: int, data_x: List[int], comment: str) -> "CustomDistribution":
        cdi = await self.__get_available_custom_distribution_index()
        cd = CustomDistribution(
            self.__observer,
            self.__conn,
            self.__module_id,
            self.__port_id,
            custom_distribution_index=cdi,
        )
        await cd.definition.set(linear=linear, symmetric=OnOff.OFF, entry_count=entry_count, data_x=data_x)
        await cd.comment.set(comment)
        self.data[cdi] = cd
        return cd
