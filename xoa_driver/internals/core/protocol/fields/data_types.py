import re
import struct
from abc import ABCMeta
from collections import UserList
from ipaddress import IPv4Address, IPv6Address
from typing import (
    Any,
    List,
    Optional,
    Type,
    Union,
    Generic,
)
from . import exceptions as excp
from . import interfaces as itf
class XmpEmpty:
    size: int = 0

    def byte_length(self) -> int:
        return self.size


class XmpIPV6Address(IPv6Address):
    """Type for representing Ipv6 addresses"""

    size: int = 16
    # format: str = "q"

    def __bytes__(self) -> bytes:
        return self.packed

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(data)


class XmpIPV4Address(IPv4Address):
    """Type for representing Ipv4 addresses"""

    size: int = 4
    # format: str = "I"

    def __bytes__(self) -> bytes:
        return self.packed

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(data)


class XmpByte(int):
    size: int = 1
    # format: str = "b"
    _max_val = 0xFF
    _max_length = _max_val.bit_length()
    
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        if not value.bit_length() <= cls._max_length:
            raise excp.NumberRangeError(value, cls._max_val)
        return value

    def __bytes__(self) -> bytes:
        return self.to_bytes(self.size, "big", signed=False)

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(int.from_bytes(data, "big", signed=False))

class XmpLong(int):
    size: int = 8
    # format: str = "q"
    _max_val = 0xFFFFFFFFFFFFFFFF
    _max_length = _max_val.bit_length()
    
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        if not value.bit_length() <= cls._max_length:
            raise excp.NumberRangeError(value, cls._max_val)
        return value

    def __bytes__(self) -> bytes:
        return self.to_bytes(self.size, "big", signed=True)

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(int.from_bytes(data, "big", signed=True))



class XmpInt(int):
    size: int = 4
    # format: str = "i"
    _max_val = 0xFFFFFFFF
    _max_length = _max_val.bit_length()
    
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        if not value.bit_length() <= cls._max_length:
            raise excp.NumberRangeError(value, cls._max_val)
        return value

    def __bytes__(self) -> bytes:
        # return pack("!i", self)
        return self.to_bytes(self.size, "big", signed=True)

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(int.from_bytes(data, "big", signed=True))
        # return cls(struct.unpack("!i", data)[0])
        # return cls(ResponseConverter.to_py_signed_int(data))


class XmpUnsignedInt(int):
    size: int = 4
    # format: str = "i"
    _max_val = 0xFFFFFFFF
    _max_length = _max_val.bit_length()
    
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        if not value.bit_length() <= cls._max_length:
            raise excp.NumberRangeError(value, cls._max_val)
        return value

    def __bytes__(self) -> bytes:
        # return pack("!i", self)
        return self.to_bytes(self.size, "big", signed=False)

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(int.from_bytes(data, "big", signed=False))


class XmpShort(int):
    size: int = 2
    # format: str = "h"
    _max_val = 0xFFFF
    _max_length = _max_val.bit_length()
    
    def __new__(cls, *args, **kwargs):
        value = super().__new__(cls, *args, **kwargs)
        if not value.bit_length() <= cls._max_length:
            raise excp.NumberRangeError(value, cls._max_val)
        return value

    def __bytes__(self) -> bytes:
        return self.to_bytes(self.size, "big", signed=True)

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(int.from_bytes(data, "big", signed=True))


class XmpStr(str):
    size: int = 0
    # format: str = "${size}s"
    
    def __bytes__(self) -> bytes:
        return struct.pack(f"!{len(self)}s", self.encode())

    def byte_length(self) -> int:
        return self.__len__()

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(data.decode())


class XmpMacAddress(str):
    size: int = 6
    # format: str = "6s"

    def __new__(cls, val: Union[int, str]):
        _val = f"{val:012x}" if isinstance(val, int) else val
        tbl = _val.maketrans("", "", ":.- ")
        clean_val = _val.translate(tbl)

        if len(clean_val) != 12 or any(
            (i not in "1234567890ABCDEFabcdef" for i in clean_val)
        ):
            raise excp.InvalidMacAddressError(val)
        return super().__new__(cls, clean_val.upper())

    def __bytes__(self) -> bytes:
        return bytes.fromhex(self)

    def __str__(self) -> str:
        return bytes.fromhex(self).hex(":")

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(data.hex(":"))

    def byte_length(self) -> int:
        return self.size


class XmpHex(str):
    size: int = 1
    # format: str = f"{size}s"
    
    def __new__(cls, val: str):
        value = super().__new__(cls, val)
        if not value.startswith(("0x", "0X")):
            raise excp.StartWithError(value, "0x", "0X")
        real_val = value.replace("0X", "").replace("0x", "")
        
        val_value = int.from_bytes(bytes.fromhex(real_val), "big")
        max_val = (1 << (cls.size * 8)) - 1
        if not 0 <= val_value <= max_val:
            raise excp.HexRangeError(value, max_val)
        return value

    def __bytes__(self) -> bytes:
        return bytes.fromhex(self.replace("0X", "").replace("0x", ""))

    def byte_length(self) -> int:
        return self.size

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericType"], data: bytes) -> "itf.XmpGenericType":
        return cls(f"0x{data.hex().upper()}")


class XmpHex1(XmpHex):
    size = 1


class XmpHex2(XmpHex):
    size = 2


class XmpHex3(XmpHex):
    size = 3


class XmpHex4(XmpHex):
    size = 4


class XmpHex6(XmpHex):
    size = 6


class XmpHex8(XmpHex):
    size = 8


class XmpHex16(XmpHex):
    size = 16


class __MegaABCAttrChecking(ABCMeta):
    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls, *args, **kwargs)
        if args[0] != "XmpDefaultList" and issubclass(
            getattr(inst, "element_type", NotImplementedError), NotImplementedError
        ):
            raise excp.ElementTypeError(args[0])
        return inst


# Complex types
class XmpDefaultList(UserList, Generic[itf.XmpGenericList], metaclass=__MegaABCAttrChecking):
    element_type: Type[itf.IXmpType]
    fix_length: Optional[int] = None
    stop_to_keep: Optional[int] = None
    size: int = 0

    def __init__(self, data: Optional[List[Any]] = None) -> None:
        if not data:
            self.data = []
        else:
            if getattr(self.element_type, "is_add_on", False):
                self.data = data
            else:
                allowed_types = (list, tuple, XmpDefaultList, str)
                if not isinstance(data, allowed_types):
                    raise excp.NotAllowedTypeError(data, allowed_types)
                
                if isinstance(data, str):
                    data = [
                        "0x" + i
                        for i in re.findall(
                            r".{2}", data.replace("0x", "").replace("0x", "")
                        )
                    ]
                self.data = [self.element_type(el) for el in data]
        if (
            self.fix_length
            and self.fix_length > 0
            and len(self.data) != self.fix_length
        ):
            raise excp.FixedLenghtError(self.data, self.fix_length)

    def __setitem__(self, idx: int, val: Any) -> None:
        self.data[idx] = self.element_type(val)

    def __bytes__(self) -> bytes:
        return b"".join(bytes(el) for el in self.data)

    def insert(self, idx, val) -> None:
        super().insert(idx, self.element_type(val))

    def append(self, val) -> None:
        super().append(self.element_type(val))

    @classmethod
    def from_bytes(cls: Type["itf.XmpGenericList"], data: bytes) -> "itf.XmpGenericList":
        pointer = 0
        each_size = cls.element_type.size
        times: int = (
            cls.fix_length
            if cls.fix_length and cls.fix_length > 0
            else len(data) // cls.element_type.size
        )
        result = []
        for _ in range(times):
            each_ele = cls.element_type.from_bytes(data[pointer : pointer + each_size])
            result.append(each_ele)
            pointer += each_size

        return cls(result) # type: ignore

    def byte_length(self) -> int:
        return self.__len__() * self.element_type.size


class XmpByteList(XmpDefaultList):
    element_type = XmpByte


class XmpIntList(XmpDefaultList):
    element_type = XmpInt


class XmpIPV4AddressList(XmpDefaultList):
    element_type = XmpIPV4Address


class XmpLongList(XmpDefaultList):
    element_type = XmpLong


class XmpShortList(XmpDefaultList):
    element_type = XmpShort


class XmpHexList(XmpDefaultList):
    element_type = XmpHex


class XmpIntList5(XmpIntList):
    fix_length = 5


class XmpIntList10(XmpIntList):
    fix_length = 10


class XmpLongListStopToKeep8(XmpLongList):
    stop_to_keep = XmpLong.size


class XmpIPV4AddressListStopToKeep4(XmpIPV4AddressList):
    stop_to_keep = 4