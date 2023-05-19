from __future__ import annotations
import typing as t
from .protocol.payload.base_struct import (
    RequestBodyStruct,
    ResponseBodyStruct
)
from .protocol.struct_header import ResponseHeader
from ..token import Token


# The defenition of generic Types

HeaderType = t.TypeVar("HeaderType", bound="ResponseHeader", covariant=True)
T_ = t.TypeVar("T_", covariant=True)


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


XoaCommandType = t.Union[ICmdOnlySet, ICmdOnlyGet]
