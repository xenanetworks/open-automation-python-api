# The defenition of generic Types
from __future__ import annotations
import typing as t
from .payload.base_struct import (
    RequestBodyStruct,
    ResponseBodyStruct
)

T_ = t.TypeVar("T_", covariant=True)


class Token(t.Protocol[T_]):
    def __await__(self) -> t.Generator[t.Any, None, T_]:
        ...


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
