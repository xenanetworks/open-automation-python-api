import typing
if typing.TYPE_CHECKING:
    from .protocol.struct_request import Request
    from asyncio import Future


class IsDataclass(typing.Protocol):
    __dataclass_fields__: typing.Dict[str, typing.Any]
    def __init__(self, *args, **kwargs) -> None: ...  # noqa: E704


DC = typing.TypeVar("DC", bound=IsDataclass)


class ICommand(typing.Protocol):
    code: typing.ClassVar[int]
    pushed: typing.ClassVar[bool]


class ICmdOnlySet(ICommand, typing.Protocol):
    """A template class which provide only <cmd_set> method."""
    SetDataAttr: typing.Type[DC]  # type: ignore
    set: typing.Callable


class ICmdOnlyGet(ICommand, typing.Protocol):
    """A template class which provide only <cmd_get> method."""
    GetDataAttr: typing.Type[DC]  # type: ignore
    get: typing.Callable


CMD_TYPE = typing.Union[ICmdOnlySet, ICmdOnlyGet]


Inst = typing.TypeVar('Inst')
CallbackType = typing.Callable[[Inst, typing.Optional[IsDataclass]], typing.Awaitable[None]]


class IConnection(typing.Protocol):
    """Representation of TransportationHandler"""
    is_connected: bool

    def send(self, requests: bytes) -> None:
        ...

    def close(self) -> None:
        ...

    async def prepare_data(self, request: "Request") -> typing.Tuple[bytes, "Future"]:
        ...

    def subscribe(self, xmc_cls: "CMD_TYPE", callback: "typing.Callable") -> None:
        ...
