from __future__ import annotations
import asyncio
import functools
from typing import (
    TYPE_CHECKING,
    Awaitable,
    Iterable,
    NamedTuple,
    Type,
    TypeVar,
    Callable,
    Union,
    cast,
)
from collections import OrderedDict

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    M_REVISION,
    M_MODEL,
    M_VERSIONSTR,
)
from .abc import AbcResourcesManager
from .exceptions import (
    NoSuchModuleError,
    WrongTesterError
)

# region Module Init dataset


class ModuleData(NamedTuple):
    """Base module data."""
    module_id: int
    ports_count: int
    revision: str


class L23ModuleData(ModuleData):
    """L23 module data"""
    @classmethod
    async def create(cls, conn, mid: int, p_cnt: int) -> "L23ModuleData":
        """Return the module name of the L23 module."""
        r = await M_REVISION(conn, mid).get()
        return cls(
            module_id=mid,
            ports_count=p_cnt,
            revision=r.revision
        )


class L47ModuleData(ModuleData):
    """L47 module data"""
    @classmethod
    async def create(cls, conn, mid: int, p_cnt: int) -> "L47ModuleData":
        """Return the module name of the L47 module."""
        r = await M_MODEL(conn, mid).get()
        return cls(
            module_id=mid,
            ports_count=p_cnt,
            revision=r.model
        )

# endregion


MT = TypeVar("MT")
MTypeObtainer = Callable[[str], Type]
ModuleDataType = Union[Type["L23ModuleData"], Type["L47ModuleData"]]


class ModulesManager(AbcResourcesManager[MT]):
    """Modules Manager"""

    __slots__ = ("_conn", "__m_types_obtainer")

    def __init__(self, conn: "itf.IConnection", m_types_obtainer: MTypeObtainer) -> None:
        super().__init__()
        self._conn = conn
        self.__m_types_obtainer = m_types_obtainer

    def obtain(self, key: int) -> MT:
        try:
            return super().obtain(key)
        except KeyError:
            raise NoSuchModuleError(key)

    def obtain_multiple(self, *keys: int) -> tuple[MT, ...]:
        try:
            return super().obtain_multiple(*keys)
        except KeyError as err:
            raise NoSuchModuleError(err.args[0])

    async def fill(self, ports_count: list[int], module_type: ModuleDataType) -> None:
        """Method for create and fill in."""
        assert not self._lock, "Method <fill> can be called only once."
        module_builder = (
            module_type.create(self._conn, slot_id, p_count)
            for slot_id, p_count in enumerate(ports_count)
            if p_count > 0
        )
        identities: Iterable[ModuleData] = await asyncio.gather(*module_builder)

        self._items = OrderedDict(
            (
                idnt.module_id,
                self.__m_types_obtainer(idnt.revision)(self._conn, idnt)
            )
            for idnt in identities
        )
        if len(self) == 0:
            raise WrongTesterError()
        coros = cast(Iterable[Awaitable], self._items.values())
        await asyncio.gather(*coros)

    fill_l23 = functools.partialmethod(fill, module_type=L23ModuleData)
    fill_l47 = functools.partialmethod(fill, module_type=L47ModuleData)
