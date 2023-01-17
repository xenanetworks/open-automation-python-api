from __future__ import annotations
from collections import Iterable
import struct
from typing import Any
from dataclasses import (
    is_dataclass,
    astuple,
)
from itertools import islice


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


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


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

    # def calc_offset(self, position_idx: int, order: tuple) -> None:
    #     self.offset = sum(v.bsize for v in order[:position_idx])

    def __build_format(self, repetition: int | None, format_letter: str) -> str:
        return f"{FMT_ORDER_NETWORK}{repetition or ''}{format_letter}"

    def calc_bsize(self, buff: memoryview) -> None:
        return None

    def pack(self, val: str) -> bytes:
        val_ = self.xmp_type.server_format(val)
        return struct.pack(self.format, val_)

    def unpack(self, buffer: memoryview) -> str:
        datum_bytes: bytes = next(iter(struct.unpack_from(self.format, buffer, self.offset)), b"")
        return self.xmp_type.client_format(datum_bytes)


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

    @property
    def is_dynamic(self) -> bool:
        return True

    def pack(self, val: str) -> bytes:
        return self.xmp_type.server_format(val)

    def unpack(self, buffer: memoryview) -> str:
        self.format = f"{self.bsize}{self.xmp_type.data_format}"
        datum_bytes: bytes = next(iter(struct.unpack_from(self.format, buffer, self.offset)), b"")
        return self.xmp_type.client_format(datum_bytes)


class SequenceSpec(FieldSpecs):
    def __init__(
        self,
        xmp_type: XmpSequence,
    ) -> None:
        self.xmp_type = xmp_type
        self.format = f"{FMT_ORDER_NETWORK}{xmp_type.data_format}"
        self.pack_fmt = f"{FMT_ORDER_NETWORK}{xmp_type.length}{xmp_type.data_format}"
        self.bsize = struct.calcsize(self.format) * (xmp_type.length or 1)

    @property
    def is_dynamic(self) -> bool:
        return self.xmp_type.length is None

    def pack(self, val: list[Any]) -> bytes:
        # !!! WARNING !!! can be many errors, coz we are not covering all posible scenarios of how this field can be defined.
        # length = self.xmp_type.length or len(val)
        if is_dataclass(val[0]):
            mapped_vals_ = (
                map(
                    lambda v: v[1].server_format(v[0]),
                    zip(chunk, self.xmp_type.types_chunk)
                )
                for chunk in map(astuple, val)
            )
            return b"".join(struct.pack(self.format, *chunk) for chunk in mapped_vals_)
        else:
            return struct.pack(self.pack_fmt, *map(self.xmp_type.types_chunk[0].server_format, val))

    def unpack(self, buffer: memoryview) -> list[Any]:
        buff_ = buffer[self.offset:]
        buff_ = buff_[:-(len(buff_) % self.bsize)]
        raw_sequence = (val for val in islice(struct.iter_unpack(self.format, buff_), self.xmp_type.length))
        # datum_bytes: bytes = next(iter(struct.unpack_from(self.xmp_type.data_format, buffer, offset)), b"")
        # return self.xmp_type.client_format(datum_bytes)
        return list(flatten(raw_sequence))


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
