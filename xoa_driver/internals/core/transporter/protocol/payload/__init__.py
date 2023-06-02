from .field import field
from .base_struct import (
    RequestBodyStruct,
    ResponseBodyStruct,
)
from .types import (
    XmpByte,
    XmpHex,
    XmpInt,
    XmpIPv4Address,
    XmpIPv6Address,
    XmpLong,
    XmpMacAddress,
    XmpSequence,
    XmpShort,
    XmpStr,
    Hex
)

__all__ = (
    "field",
    "RequestBodyStruct",
    "ResponseBodyStruct",
    "XmpByte",
    "XmpHex",
    "XmpInt",
    "XmpIPv4Address",
    "XmpIPv6Address",
    "XmpLong",
    "XmpMacAddress",
    "XmpSequence",
    "XmpShort",
    "XmpStr",
    "Hex",
)


"""
Commands with non fixed size attributes will work slower

!!!NOT PERMITED STRUCTURES!!!


# 2 strings with undefined size in one packet, seporated or not with other attributes

class BadClass1:
    attr1: str = field(XmpStr())
    attr2: str = field(XmpStr())


# Strings and arrays with undefined size

class BadClass2:
    attr1: str = field(XmpStr())
    attr2: list[int] = field(XmpSequence(XmpInt()))


# List of strings

class BadClass3:
    attr1: list[str] = field(XmpSequence(XmpStr()))


# Multiple lists of unfixed sizes

class BadClass3:
    attr1: list[int] = field(XmpSequence(XmpInt()))
    attr2: list[int] = field(XmpSequence(XmpInt()))

"""
