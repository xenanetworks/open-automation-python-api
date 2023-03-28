
from __future__ import annotations
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

GenericType = TypeVar("GenericType")


class SetInstance(Protocol):
    _buffer: BytesIO


class GetInstance(Protocol):
    _buffer: memoryview


class RequestFieldState:
    @staticmethod
    def setter(descr: FieldDescriptor, instance: SetInstance, value: Any) -> None:
        """Transform values from Python to Bxmp and store them in to the buffer"""
        val_ = descr.format_method(value)
        instance._buffer.write(descr.specs.pack(val=val_))

    @staticmethod
    def getter(descr: FieldDescriptor, instance: SetInstance, cls) -> NoReturn:
        raise AttributeError from None


class ResponseFieldState:
    @staticmethod
    def setter(descr: FieldDescriptor, instance: GetInstance, value: Any) -> NoReturn:
        raise AttributeError from None

    @staticmethod
    def getter(descr: FieldDescriptor, instance: GetInstance, cls) -> Any:
        """Unpack values from the buffer and converting to expected type if required"""
        try:
            val_ = descr.specs.unpack(instance._buffer)
        except struct.error:
            raise FirmwareVersionError(
                cmd_name=instance.__class__.__qualname__,
                field_name=descr.public_name,
                min_version=descr.specs.min_version,
            ) from None
        else:
            return descr.format_method(val_)


class FieldDescriptor(Generic[GenericType]):
    '''
    Descriptor representing getter and setter of the field
    '''
    __slots__ = ("specs", "format_method", "state", "public_name", "value_cache")

    def __init__(self: Self, specs: FieldSpecs, user_type: Type[Any], is_response: bool) -> None:
        # Will be called from the Meta class
        self.specs = specs
        self.format_method: Callable[[Any], Any] = self.specs.get_format_method(user_type, is_response)
        self.state = RequestFieldState if not is_response else ResponseFieldState

    def __set_name__(self, owner, name: str) -> None:
        self.public_name = name

    def __set__(self: Self, instance, value: GenericType) -> None:
        # Executed at the runtimne
        self.state.setter(self, instance, value)

    def __get__(self: Self, instance, cls) -> GenericType | Self:
        # Executed at the runtimne
        if instance is None:
            return self
        return self.state.getter(self, instance, cls)
