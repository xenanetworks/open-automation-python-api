from __future__ import annotations
import struct
from typing import Any, Type
# from typing_extensions import runtime_checkable

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


class FieldSpecs:
    """Executed at initialization time"""
    __slots__ = ("xmp_type", "min_version", "max_version", "deprecated", "deprecation_reason", "bsize")
    
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
        self.bsize = struct.calcsize(xmp_type.data_format) 
        


class StrSpec:
    def __init__(self, xmp_type: XmpStr,) -> None:
        self.xmp_type = xmp_type

    def build_format(self) -> None:
        self.format = ""

    def pack(self, val: str) -> bytes:
        return self.xmp_type.server_format(val)

    def unpack(self, buffer, offset) -> str:
        datum_bytes: bytes = next(iter(struct.unpack_from(self.format, buffer, offset)), b"")
        return self.xmp_type.user_format(datum_bytes)


class NumericalSpec:
    def __init__(
        self,
        xmp_type: Type[XmpInt | XmpLong | XmpByte | XmpShort],
        signed: bool = False
    ) -> None:
        self.xmp_type = xmp_type
        self.signed = signed



class HexSpec:
    def __init__(self, xmp_type: Type[XmpHex],) -> None:
        ...


class SequenceSpec:
    def __init__(
        self,
        xmp_type: XmpSequence,
        list_size: int | None = None,
    ) -> None:
        self.xmp_type = xmp_type
        self.format = f"{FMT_ORDER_NETWORK}{xmp_type.data_format}"

    def pack(self, val: list) -> bytes:
        return self.xmp_type.server_format(val)

    def unpack(self, buffer, offset) -> str:
        datum_bytes: bytes = next(iter(struct.unpack_from(self.xmp_type.data_format, buffer, offset)), b"")
        return self.xmp_type.user_format(datum_bytes)


def field(
    xmp_type: XmpType,
    *,
    min_version: int | None = None,
    max_version: int | None = None,
    deprecated: bool = False,
    deprecation_reason: str | None = None
) -> Any:
    return FieldSpecs(
        xmp_type=xmp_type,
        min_version=min_version,
        max_version=max_version,
        deprecated=deprecated,
        deprecation_reason=deprecation_reason,
    )
