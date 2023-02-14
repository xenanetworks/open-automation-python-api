from __future__ import annotations
import typing as t
from .transporter.token import Token
from .protocol.payload.base_struct import RequestBodyStruct, ResponseBodyStruct
if t.TYPE_CHECKING:
    from .protocol.struct_request import Request
    from asyncio import Future


class IsDataclass(t.Protocol):
    __dataclass_fields__: t.Dict[str, t.Any]
    def __init__(self, *args, **kwargs) -> None: ...  # noqa: E704


class ICommand(t.Protocol):
    code: t.ClassVar[int]
    pushed: t.ClassVar[bool]


SetStructType = t.TypeVar("SetStructType", bound="RequestBodyStruct", covariant=True)
GetStructType = t.TypeVar("GetStructType", bound="ResponseBodyStruct", covariant=True)


class ICmdOnlySet(ICommand, t.Protocol):
    """A template class which provide only <cmd_set> method."""

    SetDataAttr: t.Type[SetStructType]  # type: ignore
    set: t.Callable[..., Token[None]]


class ICmdOnlyGet(ICommand, t.Protocol):
    """A template class which provide only <cmd_get> method."""
    GetDataAttr: t.Type[GetStructType]  # type: ignore
    get: t.Callable[[], Token[GetStructType]]  # type: ignore


CMD_TYPE = t.Union[ICmdOnlySet, ICmdOnlyGet]


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

    def subscribe(self, xmc_cls: "CMD_TYPE", callback: "t.Callable") -> None:
        ...

    def on_disconnected(self, callback: "t.Callable") -> None:
        ...
