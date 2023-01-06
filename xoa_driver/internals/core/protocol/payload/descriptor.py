
from __future__ import annotations

import struct
from typing import Any, Generic, Type, TypeVar

from typing_extensions import NoReturn, Self

from .types import XmpType

GenericType = TypeVar("GenericType")


class RequestStructField:
    @staticmethod
    def setter(descr: StructField, instance, value: Any) -> None:
        instance._buffer.write(
            struct.pack(
                descr.xmp_type.data_format,
                value
            )
        )

    @staticmethod
    def getter(descr: StructField, instance, cls) -> NoReturn:
        raise AttributeError from None


class ResponseStructField:
    @staticmethod
    def setter(descr: StructField, instance, value: Any) -> NoReturn:
        raise AttributeError from None

    @staticmethod
    def getter(descr: StructField, instance, cls) -> Any:
        r = struct.unpack_from(
            descr.xmp_type.data_format,
            instance._buffer,
            descr.offset
        )
        return r[0] if len(r) == 1 else r


class StructField(Generic[GenericType]):
    '''
    Descriptor representing a simple structure field
    '''

    def __init__(self, xmp_type: XmpType, type_size: int, user_type: Type) -> None:
        self.xmp_type = xmp_type
        self.user_type = user_type
        self.size = type_size

    def __set_name__(self, owner, name: str) -> None:
        if not owner._is_response:
            self.__performer = RequestStructField
        else:
            self.__performer = ResponseStructField

        self.name = name
        self.offset = sum(
            v for _, v in owner._order[:owner._order.index((name, self.size))]
        )

    def __set__(self: Self, instance, value: GenericType) -> None:
        """Executed at the runtimne"""
        self.__performer.setter(
            self,
            instance,
            self.xmp_type.server_format(value)
        )

    def __get__(self: Self, instance, cls) -> GenericType | Self:
        """Executed at the runtimne"""
        if instance is None:
            return self
        try:
            val = self.__performer.getter(self, instance, cls)
        except struct.error:
            raise AttributeError() from None
        else:
            return self.user_type(self.xmp_type.user_format(val))
