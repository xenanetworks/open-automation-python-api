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
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> None: ...  # noqa: E704

    async def delete(self) -> None: ...  # noqa: E704

    @property
    def idx(self) -> int: ...  # noqa: E704

    @classmethod
    async def _fetch(cls, conn, module_id, port_id) -> List[int]: ...  # noqa: E704

    @classmethod
    async def _new(cls, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> Type: ...  # noqa: E704
