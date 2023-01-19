from __future__ import annotations
from enum import Enum
from functools import partial
from ipaddress import IPv4Address, IPv6Address
import struct
from typing import (
    Any,
    Callable,
    Iterable,
    List,
    Tuple,
    Type,
    get_args,
)
from dataclasses import (
    is_dataclass,
    astuple,
)
from itertools import islice

from .utils import flatten
from .types import (
    XmpType,
    FMT_ORDER_NETWORK,
    # Numerical
    XmpInt,
    XmpLong,
    XmpByte,
    XmpShort,
    # Preconverted
    XmpHex,
    XmpIPv4Address,
    XmpIPv6Address,
    XmpMacAddress,
    # Preconverted Dynamic
    XmpStr,
    XmpSequence,
)


TYPES_FIXED = (XmpInt, XmpLong, XmpByte, XmpShort, XmpHex, XmpIPv4Address, XmpIPv6Address, XmpMacAddress,)
TYPES_DYNAMIC = (XmpStr,)
TYPES_COMPOSED = (XmpSequence,)


class FieldSpecs:
    """Executed at initialization time"""
    __slots__ = ("xmp_type", "format", "min_version", "max_version", "deprecated", "deprecation_reason", "bsize", "offset")

    bsize: int
    """bytes size"""

    def __init__(
        self,
        xmp_type: XmpType,
        min_version: int | None = None,
        max_version: int | None = None,
        deprecated: bool = False,
        deprecation_reason: str | None = None,
    ) -> None:
        self.xmp_type = xmp_type
        self.min_version = min_version
        self.max_version = max_version
        self.deprecated = deprecated
        self.deprecation_reason = deprecation_reason
        self.offset = 0
        self.format = self.__build_format(
            xmp_type.repetitions,
            xmp_type.data_format
        )
        self.bsize = struct.calcsize(self.format)

    @property
    def is_dynamic(self) -> bool:
        return False

    def __build_format(self, repetition: int | None, format_letter: str) -> str:
        return f"{FMT_ORDER_NETWORK}{repetition or ''}{format_letter}"

    def get_format_method(self, client_type: Type[Any], is_response: bool) -> Callable[[Any], Any]:
        if not isinstance(client_type, (int, IPv4Address, IPv6Address)):
            if is_response:
                return lambda v: client_type(self.xmp_type.client_format(v))
            return lambda v: self.xmp_type.server_format(client_type(v))
        if is_response:
            return self.xmp_type.client_format
        return self.xmp_type.server_format

    def calc_bsize(self, buff: memoryview) -> None:
        return None

    def pack(self, val: Any) -> bytes:
        return struct.pack(self.format, val)

    def unpack(self, buffer: memoryview) -> Any:
        return next(iter(struct.unpack_from(self.format, buffer, self.offset)), b"")


class StrSpec(FieldSpecs):
    def __init__(self, xmp_type: XmpStr,) -> None:
        self.xmp_type = xmp_type
        self.bsize = 0

    def calc_bsize(self, buff: memoryview) -> None:
        in_memory_slice = buff[self.offset:]
        current_size = next(
            (
                idx
                for idx, ord_n in enumerate(in_memory_slice)
                if ord_n == 0 and not bool(idx % 4)
            ),
            in_memory_slice.nbytes
        )
        self.bsize = max(self.xmp_type.min_len or 0, current_size)
        self.format = f"{self.bsize}{self.xmp_type.data_format}"

    @property
    def is_dynamic(self) -> bool:
        return True

    def get_format_method(self, client_type: Type[Any], is_response: bool) -> Callable[[Any], Any]:
        if is_response:
            return self.xmp_type.client_format
        return self.xmp_type.server_format

    def pack(self, val: bytes) -> bytes:
        return val


# class LimitedSequence:
#     ...

# class UnlimitedSequence:
#     @staticmethod
#     def pack(self, val: list[Any]) -> bytes:
#         pack_fmt = f"{FMT_ORDER_NETWORK}{len(val)}{xmp_type.data_format}"
#         return struct.pack(self.pack_fmt, *map(self.xmp_type.types_chunk[0].server_format, val))

# class SequenceChunk:
#     def __init__(self, ) -> None:

def prepare_client_chunks(values_list: List[Tuple[Any, ...]], client_type: Type[Any], xmp_types_chunks: tuple) -> List[Any]:
    if is_dataclass(client_type):
        type_paired = (zip(chunk, xmp_types_chunks) for chunk in values_list)
        converted = (map(lambda v: v[1].client_format(v[0]), pair) for pair in type_paired)
    else:
        converted = map(xmp_types_chunks[0].client_format, values_list)
    return [client_type(*vals) for vals in converted]


def prepare_serv_chunks(values_list: List[Any], client_type: Type[Any], xmp_types_chunks: tuple) -> List[Tuple[Any, ...]]:
    if is_dataclass(client_type):
        return [
            map(lambda v: v[1].server_format(v[0]), zip(chunk, xmp_types_chunks))
            for chunk in map(astuple, values_list)
        ]
    return list(map(xmp_types_chunks[0].server_format, values_list))


class SequenceSpec(FieldSpecs):
    def __init__(
        self,
        xmp_type: XmpSequence,
    ) -> None:
        self.xmp_type = xmp_type
        self.format = f"{FMT_ORDER_NETWORK}{xmp_type.data_format}"
        self.pack_fmt = self.format
        self.bsize = struct.calcsize(self.format) * (xmp_type.length or 1)

    @property
    def is_dynamic(self) -> bool:
        return self.xmp_type.length is None

    def calc_bsize(self, buff: memoryview) -> None:
        return None

    def get_format_method(self, client_type: Type[Any], is_response: bool) -> Callable[[Any], Any]:
        if is_response:
            return partial(prepare_client_chunks, client_type=get_args(client_type)[0], xmp_types_chunks=self.xmp_type.types_chunk)
        return partial(prepare_serv_chunks, client_type=get_args(client_type)[0], xmp_types_chunks=self.xmp_type.types_chunk)
        # chunk_client_type = next(iter(get_args(client_type)), None)
        # def convert(chunk) -> List[chunk_client_type]:
        #     [chunk_client_type(*vals) for vals in chunk] 
        # if is_response:
        #     return self.xmp_type.client_format
        # return self.xmp_type.server_format

    def pack(self, val: list[Any]) -> bytes:
        length = self.xmp_type.length or len(val)
        pack_fmt = f"{FMT_ORDER_NETWORK}{self.xmp_type.data_format * length}"
        return struct.pack(pack_fmt, *flatten(val))

    def unpack(self, buffer: memoryview) -> list[Any]:
        buff_ = buffer[self.offset:]
        buff_ = buff_[:-(len(buff_) % self.bsize)]
        raw_sequence = islice(struct.iter_unpack(self.format, buff_), self.xmp_type.length)
        return list(raw_sequence)


def field(
    xmp_type: XmpType,
    *,
    min_version: int | None = None,
    max_version: int | None = None,
    deprecated: bool = False,
    deprecation_reason: str | None = None
) -> Any:
    if isinstance(xmp_type, TYPES_COMPOSED):
        return SequenceSpec(xmp_type=xmp_type,)
    elif isinstance(xmp_type, TYPES_DYNAMIC):
        return StrSpec(xmp_type=xmp_type,)
    elif isinstance(xmp_type, TYPES_FIXED):
        return FieldSpecs(
            xmp_type=xmp_type,
            min_version=min_version,
            max_version=max_version,
            deprecated=deprecated,
            deprecation_reason=deprecation_reason,
        )
