from __future__ import annotations
import os
import sys
from typing import List
from ipaddress import (
    IPv4Address,
    IPv6Address,
)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver.internals.core.transporter.protocol.payload.exceptions import FirmwareVersionError
from xoa_driver.internals.core.transporter.protocol.payload import (
    ResponseBodyStruct,
    field,
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


# region TypeTesting

def test_byte() -> None:
    data = b"\xff\xff"
    assert len(data) == 2, "for current test case the data must be of 2 bytes long"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: int = field(XmpByte())
        custom_field2: int = field(XmpByte(signed=True))
        custom_field3: int = field(XmpByte())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, int)
    assert obj.custom_field == 255
    assert obj.custom_field != 65535
    assert obj.custom_field2 == -1
    try:
        obj.custom_field3
    except FirmwareVersionError:
        pass
    else:
        assert False, "Suppose to break on not suficient amount of bytes"


def test_short() -> None:
    data = b"\x02\x05"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: int = field(XmpShort())
        custom_field2: int = field(XmpByte(signed=False))

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, int)
    assert obj.custom_field != 2
    assert obj.custom_field != 255
    assert obj.custom_field == 517


def test_int() -> None:
    data = b"\x00\x00\x00\xff"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: int = field(XmpInt())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, int)
    assert obj.custom_field != 0
    assert obj.custom_field == 255


def test_long() -> None:
    data = b"\x00\x00\x00\xff\x00\x00\x00\xff"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: int = field(XmpLong())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, int)
    assert obj.custom_field == 1095216660735


def test_hex() -> None:
    data = b"\x00\x00\x00\xff\x00\x00\x00\xff"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: Hex = field(XmpHex())
        custom_field2: Hex = field(XmpHex(size=3))

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, str)
    assert obj.custom_field == "00"
    assert obj.custom_field == Hex("00")
    assert obj.custom_field2 == "0000ff"
    assert obj.custom_field2 == Hex("0000ff")


def test_ip_v4() -> None:
    data = b'\x7f\x00\x00\x01'

    class GetDataAttr(ResponseBodyStruct):
        custom_field: IPv4Address = field(XmpIPv4Address())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, IPv4Address)
    assert obj.custom_field == IPv4Address("127.0.0.1")
    assert obj.custom_field != "127.0.0.1"


def test_ip_v6() -> None:
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xab'

    class GetDataAttr(ResponseBodyStruct):
        custom_field: IPv6Address = field(XmpIPv6Address())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, IPv6Address)
    assert obj.custom_field == IPv6Address("::ab")
    assert obj.custom_field != "::ab"


def test_mac() -> None:
    data = b'\xf4\xd4\x88\x67\xc5\xda'

    class GetDataAttr(ResponseBodyStruct):
        custom_field: Hex = field(XmpMacAddress())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, str)
    assert obj.custom_field == "f4d48867c5da"
    assert obj.custom_field != "f4:d4:88:67:c5:da"


def test_string() -> None:
    data = b'Xena Networks\x00\x00\x07\xe7'

    class GetDataAttr(ResponseBodyStruct):
        custom_field: str = field(XmpStr())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, str)
    assert obj.custom_field == "Xena Networks"


def test_unlimited_list() -> None:
    data = b'\x00\x02\x00\x06\x00\x06\x00\x06'

    class GetDataAttr(ResponseBodyStruct):
        port_counts: List[int] = field(XmpSequence(types_chunk=[XmpByte()]))

    obj = GetDataAttr(data)
    assert hasattr(obj, "port_counts")
    assert obj.port_counts == [0, 2, 0, 6, 0, 6, 0, 6]


def test_limited_list() -> None:
    data = b'\x00\x02\x00\x06\x00\x06\x00\x06'
    MAX_LEN = 2

    class GetDataAttr(ResponseBodyStruct):
        custom_field: List[int] = field(XmpSequence(types_chunk=[XmpByte()], length=MAX_LEN))

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, list)
    assert len(obj.custom_field) == MAX_LEN
    assert obj.custom_field == [0, 2]

# endregion

# region TypeCombinations

# endregion