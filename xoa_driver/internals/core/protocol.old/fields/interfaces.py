from typing import (
    TypeVar,
    Type,
    Protocol,
    ClassVar,
    Optional,
    Callable,
    Union,
)

XmpGenericType = TypeVar("XmpGenericType", bound="IXmpType")


class IXmpType(Protocol):
    size: ClassVar[int]
    __init__: Callable
    def __bytes__(self) -> bytes: ...  # noqa: E704
    def byte_length(self) -> int: ...  # noqa: E704
    @classmethod
    def from_bytes(cls: Type[XmpGenericType], data: bytes) -> XmpGenericType: ...  # noqa: E704


XmpGenericList = TypeVar("XmpGenericList", bound="IXmpDefaultList")


class IXmpDefaultList(Protocol):
    __init__: Callable
    size: ClassVar[int]
    element_type: ClassVar[Type[IXmpType]]
    fix_length: ClassVar[Optional[int]]
    stop_to_keep: ClassVar[Optional[int]]

    def byte_length(self) -> int: ...  # noqa: E704
    @classmethod
    def from_bytes(cls: Type[XmpGenericType], data: bytes) -> XmpGenericType: ...  # noqa: E704


XmpGenericField = TypeVar("XmpGenericField", bound=Union["IXmpDefaultList", "IXmpType"])
