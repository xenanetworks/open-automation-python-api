from __future__ import annotations
import typing as t
if t.TYPE_CHECKING:
    from asyncio import Future
    from .transporter._typings import ICommand
    from .transporter.protocol.struct_request import Request


# The defenition of generic Types


T_ = t.TypeVar("T_", covariant=True)


class IsDataclass(t.Protocol):
    __dataclass_fields__: t.Dict[str, t.Any]
    def __init__(self, *args, **kwargs) -> None: ...  # noqa: E704


Inst = t.TypeVar('Inst')
CallbackType = t.Callable[[Inst, t.Optional[IsDataclass]], t.Awaitable[None]]


class IConnection(t.Protocol):
    """Representation of TransportationHandler"""

    @property
    def is_connected(self) -> bool:
        ...

    def send(self, data: bytes | bytearray | memoryview) -> None:
        ...

    def close(self) -> None:
        ...

    async def prepare_data(self, request: "Request") -> t.Tuple[bytes, "Future"]:
        ...

    def subscribe(self, xmc_cls: "ICommand", callback: "t.Callable") -> None:
        ...

    def on_disconnected(self, callback: "t.Callable") -> None:
        ...

    def set_outdated(self) -> None:
        ...