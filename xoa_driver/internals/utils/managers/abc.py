from abc import (
    ABC,
    abstractmethod
)
from typing import (
    Generic,
    TypeVar,
    Tuple,
)
from collections import OrderedDict


T = TypeVar("T")


class AbcResourcesManager(ABC, Generic[T]):
    """Resource Base Manager
    """
    __slots__ = ("_items", "_lock", )

    def __init__(self) -> None:
        self._items: OrderedDict[int, T] = OrderedDict()
        self._lock: bool = False

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items.values())

    def obtain(self, key: int) -> T:
        """Obtain a single resource.
        """
        return self._items[key]

    def obtain_multiple(self, *keys: int) -> Tuple[T, ...]:
        """Obtain multiple resources as a tuple of resources.
        """
        return tuple(self._items[k] for k in keys)

    @abstractmethod
    async def fill(self, *args, **kwargs) -> None:
        """Method for create and fill in."""
        raise NotImplementedError()
