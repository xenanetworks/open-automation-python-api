
from __future__ import annotations
from abc import (
    abstractmethod,
    ABC
)
from io import BytesIO
import struct

from typing import (
    Any,
    Callable,
    Generic,
    Protocol,
    Type,
    TypeVar,
)

from typing_extensions import (
    NoReturn,
    Self,
)

from .field import FieldSpecs
from .exceptions import FirmwareVersionError

# region Types

GenericType = TypeVar("GenericType")


class SetInstance(Protocol):
    _buffer: BytesIO


class GetInstance(Protocol):
    _buffer: memoryview
    _stencil: tuple[tuple[str, int], ...]

# endregion


class FieldDescriptor(ABC, Generic[GenericType]):
    '''
    Descriptor representing getter and setter of the field
    '''
    __slots__ = ("idx", "specs", "public_name",)

    def __init__(self: Self, idx: int, specs: FieldSpecs) -> None:
        # Will be called from the Meta class
        self.idx = idx
        self.specs = specs

    def __set_name__(self, owner, name: str) -> None:
        self.public_name = name

    @abstractmethod
    def __set__(self: Self, instance, value: GenericType) -> None:
        # Executed at the runtimne
        raise NotImplementedError()

    @abstractmethod
    def __get__(self: Self, instance, cls) -> GenericType | Self:
        # Executed at the runtimne
        raise NotImplementedError()


class RequestFieldDescr(FieldDescriptor[GenericType]):
    __slots__ = ("to_xmp_context", "fmt")

    def __init__(self: Self, idx: int, specs: FieldSpecs, user_type: Type[Any]) -> None:
        super().__init__(idx, specs)
        self.fmt = self.specs.format()
        self.to_xmp_context: Callable[[Any], Any] = self.specs.get_context_formatter(user_type, False)

    def __set__(self: Self, instance: SetInstance, value: GenericType) -> None:
        """Transform values from Python to Bxmp and store them in to the buffer"""
        # Executed at the runtimne
        val_ = self.to_xmp_context(value)
        instance._buffer.write(self.specs.pack(self.fmt, val=val_))

    def __get__(self: Self, instance: SetInstance, cls) -> NoReturn | Self:
        # Executed at the runtimne
        if instance is None:
            return self
        raise RuntimeError from None


class ResponseFieldDescr(FieldDescriptor[GenericType]):
    __slots__ = ("to_py_context",)

    def __init__(self: Self, idx: int, specs: FieldSpecs, user_type: Type[Any]) -> None:
        super().__init__(idx, specs)
        self.to_py_context: Callable[[Any], Any] = self.specs.get_context_formatter(user_type, True)

    def __set__(self: Self, instance: GetInstance, value: GenericType) -> NoReturn:
        # Executed at the runtimne
        raise RuntimeError from None

    def __get__(self: Self, instance: GetInstance, cls) -> GenericType | Self:
        """Unpack values from the buffer and converting to expected type if required"""
        # Executed at the runtimne
        if instance is None:
            return self
        format_, offset_ = instance._stencil[self.idx]
        try:
            val_ = self.specs.unpack(
                format=format_,
                buffer=instance._buffer,
                offset=offset_,
            )
        except struct.error:
            raise FirmwareVersionError(
                cmd_name=instance.__class__.__qualname__,
                field_name=self.public_name,
                min_version=self.specs.min_version,
            ) from None
        else:
            return self.to_py_context(val_)
