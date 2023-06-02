from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, IntEnum
import os
import sys
from typing import List
from ipaddress import (
    IPv4Address,
    IPv6Address,
)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver.internals.core.transporter.protocol.payload.exceptions import FirmwareVersionError  # noqa: E402
from xoa_driver.internals.core.transporter.protocol.payload import (  # noqa: E402
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

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, int)
    assert obj.custom_field != 2
    assert obj.custom_field != 255
    assert obj.custom_field == 517


def test_int() -> None:
    data = b"\x00\x00\x00\xff"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: int = field(XmpInt(climb=(10, 20)))

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
        custom_field: Hex = field(XmpHex(size=1))
        custom_field2: Hex = field(XmpHex(size=3))

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, str)
    assert obj.custom_field == "00"
    assert obj.custom_field == Hex("00")
    assert obj.custom_field2 == "0000ff"
    assert obj.custom_field2 == Hex("0000ff")


def test_hex_string() -> None:
    data = b'\x04\xf4\xbc\x9cs\xd1\x04\xf4\xbc\x9cs\xd0\xff\xff\x00\x00'

    class SetDataAttr(ResponseBodyStruct):
        hex_data: Hex = field(XmpHex())

    obj = SetDataAttr(data)
    assert obj.hex_data[:-4] == Hex("04F4BC9C73D104F4BC9C73D0FFFF").lower()


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
    data_1 = b"Odin-10G-1S-6P[b]\x00\x00\n"
    data_2 = b"Odin-10G-1S-6P[b]\x00\x00\x0c"
    data_3 = b""

    class GetDataAttr(ResponseBodyStruct):
        custom_field: str = field(XmpStr())

    obj1 = GetDataAttr(data_1)
    obj2 = GetDataAttr(data_2)
    obj3 = GetDataAttr(data_3)

    assert isinstance(obj1.custom_field, str)
    assert isinstance(obj2.custom_field, str)
    assert isinstance(obj3.custom_field, str)
    assert obj1.custom_field == "Odin-10G-1S-6P[b]"
    assert obj2.custom_field == "Odin-10G-1S-6P[b]"
    assert obj3.custom_field == ""


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


# region TypeConversion

class UsersEnum(Enum):
    OPTION_1 = 1
    OPTION_2 = 2
    OPTION_3 = 3
    OPTION_4 = 5


def test_enum_global_def() -> None:
    data = b"\x02\x05"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: UsersEnum = field(XmpByte())
        custom_field2: UsersEnum = field(XmpByte())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, UsersEnum)
    assert isinstance(obj.custom_field2, UsersEnum)
    assert obj.custom_field == UsersEnum.OPTION_2
    assert obj.custom_field2 == UsersEnum.OPTION_4


def test_enum_local_def() -> None:
    """
    At the Moment the defenition of the enum under the local namespace will faile
    """
    data = b"\x02\x05"

    class UsersLocalEnum(Enum):
        OPTION_1 = 1
        OPTION_2 = 2
        OPTION_3 = 3
        OPTION_4 = 5

    class GetDataAttr(ResponseBodyStruct):
        custom_field: UsersLocalEnum = field(XmpByte())
        custom_field2: UsersLocalEnum = field(XmpByte())

    obj = GetDataAttr(data)
    try:
        assert isinstance(obj.custom_field, UsersLocalEnum)
        assert isinstance(obj.custom_field2, UsersLocalEnum)
        assert obj.custom_field == UsersLocalEnum.OPTION_2
        assert obj.custom_field2 == UsersLocalEnum.OPTION_4
    except TypeError as e:
        assert str(e) == "'ForwardRef' object is not callable"
    else:
        assert False, "Magicly it start to works"


def test_bool() -> None:
    data = b"\x01\x00"

    class GetDataAttr(ResponseBodyStruct):
        custom_field: bool = field(XmpByte())
        custom_field2: bool = field(XmpByte())

    obj = GetDataAttr(data)
    assert isinstance(obj.custom_field, bool)
    assert isinstance(obj.custom_field2, bool)
    assert obj.custom_field is True
    assert obj.custom_field2 is False


class OnOff(IntEnum):
    OFF = 0
    ON = 1


@dataclass
class ArpChunk:
    ipv4_address: IPv4Address
    prefix: int
    patched_mac: OnOff
    mac_address: Hex


def test_chunk_type() -> None:
    data = b'\x7f\x00\x00\x01\x02\x05\x01\xf4\xd4\x88\x67\xc5\xda\x7f\x00\x00\x03\x02\x05\x00\xf4\xd4\x88\x55\xc5\xda'

    class GetDataAttr(ResponseBodyStruct):
        custom_field: List[ArpChunk] = field(XmpSequence(types_chunk=[XmpIPv4Address(), XmpShort(), XmpByte(), XmpMacAddress()]))
    obj = GetDataAttr(data)
    assert len(obj.custom_field) == 2
    assert obj.custom_field[0].ipv4_address == IPv4Address("127.0.0.1")
    assert obj.custom_field[0].prefix == 517
    assert obj.custom_field[0].patched_mac == OnOff.ON
    assert obj.custom_field[0].mac_address == "f4d48867c5da"

# endregion


# region TypeCombinations

# endregion
