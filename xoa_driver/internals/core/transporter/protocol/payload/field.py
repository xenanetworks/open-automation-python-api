from __future__ import annotations

from ipaddress import (
    IPv4Address,
    IPv6Address,
)
import struct
from typing import (
    Any,
    Callable,
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


TYPES_FIXED = (
    XmpInt,
    XmpLong,
    XmpByte,
    XmpShort,
    XmpHex,
    XmpIPv4Address,
    XmpIPv6Address,
    XmpMacAddress,
)
TYPES_DYNAMIC = (XmpStr,)
TYPES_COMPOSED = (XmpSequence,)

# Important: The instances of the FieldSpecs will live as a class variables
# which mean wea are not able to update its attributes during runtime.
# Instead it suppose to provide values or methods which return an value under the instance of Pkt Body struct


class FieldSpecs:
    """Executed at initialization time"""
    __slots__ = ("xmp_type", "format", "min_version", "max_version", "deprecated", "deprecation_reason", "bsize",)

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
        # self.format = self._build_format(
        #     xmp_type.data_format
        #     xmp_type.repetitions,
        # )
        # self.bsize = struct.calcsize(self.format)

    @property
    def is_dynamic(self) -> bool:
        return False

    def _build_format(self, format_letter: str, repetition: int | None = None) -> str:
        return f"{FMT_ORDER_NETWORK}{repetition or ''}{format_letter}"

    def get_context_formatter(self, client_type: Type[Any], is_response: bool) -> Callable[[Any], Any]:
        if not isinstance(client_type, (int, IPv4Address, IPv6Address)):
            if is_response:
                return lambda v: client_type(self.xmp_type.client_format(v))
            return lambda v: self.xmp_type.server_format(client_type(v))
        if is_response:
            return self.xmp_type.client_format
        return self.xmp_type.server_format

    def calc_bsize(self, buff: memoryview, left_offset: int = 0) -> None:
        return None

    def pack(self, val: Any) -> bytes:
        return struct.pack(self.format, val)

    def unpack(self, format: str, buffer: memoryview, offset: int) -> Any:
        return next(iter(struct.unpack_from(format, buffer, offset)), b"")


class StrSpec(FieldSpecs):
    def __init__(self, xmp_type: XmpStr,) -> None:
        self.xmp_type = xmp_type
        # self.bsize = None

    @property
    def is_dynamic(self) -> bool:
        return True

    def calc_bsize(self, buff: memoryview, left_offset: int = 0) -> None:
        in_memory_slice = buff[left_offset:]
        current_size = next(
            (
                idx
                for idx, ord_n in enumerate(in_memory_slice)
                if ord_n == 0 and not bool(idx % 4)
            ),
            in_memory_slice.nbytes
        )
        bsize = max(self.xmp_type.min_len or 0, current_size)
        self.format = self._build_format(self.xmp_type.data_format, bsize,)

    def get_context_formatter(self, client_type: Type[Any], is_response: bool) -> Callable[[Any], Any]:
        if is_response:
            return self.xmp_type.client_format
        return self.xmp_type.server_format

    def pack(self, val: bytes) -> bytes:
        return val

    def unpack(self, format: str, buffer: memoryview, offset: int) -> bytes:
        return next(iter(struct.unpack_from(format, buffer, offset)), b"")


def _prepare_client_chunks(client_type: Type[Any], xmp_types_chunks: tuple) -> Callable[[Any], List[Tuple[Any, ...]]]:
    """Selecting the function for parsing data chunks from XMP types to Python types"""
    def converted_dcls(val_):
        type_paired = (zip(chunk, xmp_types_chunks) for chunk in val_)
        return (map(lambda v: v[1].client_format(v[0]), pair) for pair in type_paired)

    def converted_val(val_):
        return map(xmp_types_chunks[0].client_format, val_)

    converted = converted_dcls if is_dataclass(client_type) else converted_val
    return lambda val: [client_type(*vals) for vals in converted(val)]


def _prepare_serv_chunks(client_type: Type[Any], xmp_types_chunks: tuple) -> Callable[[Any], List[Tuple[Any, ...]]]:
    """Selecting the function for parsing data chunks from Python types to XMP types"""
    if is_dataclass(client_type):
        return lambda val: [
            tuple(map(lambda v: v[1].server_format(v[0]), zip(chunk, xmp_types_chunks)))
            for chunk in map(astuple, val)
        ]
    return lambda val: list(map(xmp_types_chunks[0].server_format, val))


class SequenceSpec(FieldSpecs):
    def __init__(self, xmp_type: XmpSequence,) -> None:
        self.xmp_type = xmp_type
        # self.format = f"{FMT_ORDER_NETWORK}{xmp_type.data_format}"
        # self.bsize = struct.calcsize(self.format) * (xmp_type.length or 1)

    @property
    def is_dynamic(self) -> bool:
        return self.xmp_type.length is None

    def calc_bsize(self, buff: memoryview, left_offset: int = 0) -> None:
        return None

    def get_context_formatter(self, client_type: Type[Any], is_response: bool) -> Callable[[Any], List[Tuple[Any, ...]]]:
        try:
            client_type = get_args(client_type)[0]
        except IndexError as e:
            raise e
        if is_response:
            return _prepare_client_chunks(
                client_type=client_type,
                xmp_types_chunks=self.xmp_type.types_chunk
            )
        return _prepare_serv_chunks(
            client_type=client_type,
            xmp_types_chunks=self.xmp_type.types_chunk
        )

    def pack(self, val: list[Any]) -> bytes:
        length = self.xmp_type.length or len(val)
        pack_fmt = f"{FMT_ORDER_NETWORK}{self.xmp_type.data_format * length}"
        return struct.pack(pack_fmt, *flatten(val))

    def unpack(self, format: str, buffer: memoryview, offset: int) -> list[Any]:
        buff_ = buffer[offset:]
        limit = len(buff_) % self.bsize
        buff_ = buff_[:-limit] if limit else buff_
        raw_sequence = islice(struct.iter_unpack(format, buff_), self.xmp_type.length)
        return list(raw_sequence)


def field(
    xmp_type: XmpType,
    *,
    min_version: int | None = None,
    max_version: int | None = None,
    deprecated: bool = False,
    deprecation_reason: str | None = None
) -> Any:
    """Method used for describe field parameters of an XMP packet structure"""
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
    return None
