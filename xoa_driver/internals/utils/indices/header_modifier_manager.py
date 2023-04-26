from typing import (
    List,
    Type,
    Union,
    Generic,
    TypeVar,
    TYPE_CHECKING,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.commands import (
        PS_MODIFIERCOUNT,
        PS_MODIFIEREXTCOUNT
    )
    CT = Union[Type[PS_MODIFIERCOUNT], Type[PS_MODIFIEREXTCOUNT]]

MT = TypeVar("MT")


class ModifiersManager(Generic[MT]):
    def __init__(self, conn: "itf.IConnection", kind, count_type: "CT", modifier_type: Type[MT]) -> None:
        self.__conn = conn
        self.__kind = kind
        self.__modifier_type = modifier_type

        self._count = count_type(self.__conn, *kind)
        self.__items: List[MT] = []

    async def _populate(self) -> None:
        count = (await self._count.get()).to_tuple()[0]  # modifier_count or ext_modifier_count
        self.__items = [
            self.__modifier_type(
                self.__conn,
                *self.__kind,
                idx
            )
            for idx in range(count)
        ]

    async def configure(self, number: int) -> None:
        await self._count.set(number)
        await self._populate()

    async def clear(self) -> None:
        await self._count.set(0)
        self.__items.clear()

    def __len__(self) -> int:
        return len(self.__items)

    def __iter__(self):
        return iter(self.__items)

    def obtain(self, idx: int) -> MT:
        """Access modifier of the index value"""
        return self.__items[idx]
