import asyncio
from typing import (
    Type, 
    TypeVar,
    Protocol,
    TYPE_CHECKING,
)
from collections import OrderedDict
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from ._base_manager import ResourcesBaseManager

class IPort(Protocol):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        ...


PT = TypeVar("PT", bound=IPort)

class PortsManager(ResourcesBaseManager[PT]):
    
    __slots__ = ("_conn", "_ports_type", "_ports_count", "_module_id", )
    
    def __init__(self, conn: "itf.IConnection", module_id: int, ports_type: Type[PT], ports_count: int) -> None:
        super().__init__()
        self._conn = conn
        self._ports_type = ports_type
        self._ports_count = ports_count
        self._module_id = module_id
        self._items: OrderedDict[int, PT] = OrderedDict(
            (
                port_id,
                self._ports_type(
                    conn=self._conn,
                    module_id=self._module_id,
                    port_id=port_id,
                )
            )
            for port_id in range(self._ports_count)
        )

    async def fill(self) -> None:
        """Method for create and fill in."""
        assert not self._lock, "Method <fill> can be called only once."
        coros = list(self._items.values())
        await asyncio.gather(*coros) # type: ignore
