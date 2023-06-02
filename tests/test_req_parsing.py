from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum
import os
import sys
from typing import List
from ipaddress import (
    IPv4Address,
    IPv6Address,
)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver.internals.core.transporter.protocol.payload import (  # noqa: E402
    RequestBodyStruct,
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
    data = b"\xff\xff\x00\x00"
    assert len(data) == 4, "for current test case the data must be of 2 bytes long"

    class SetDataAttr(RequestBodyStruct):
        custom_field: int = field(XmpByte())
        custom_field2: int = field(XmpByte(signed=True))

    obj = SetDataAttr(
        custom_field=255,
        custom_field2=-1
    )
    assert obj.to_bytes() == data


def test_short() -> None:
    data = b"\x02\x05\x00\x00"

    class SetDataAttr(RequestBodyStruct):
        custom_field: int = field(XmpShort())

    obj = SetDataAttr(custom_field=517)
    assert obj.to_bytes() == data


def test_int() -> None:
    data = b"\x00\x00\x00\xff"

    class SetDataAttr(RequestBodyStruct):
        custom_field: int = field(XmpInt(climb=(10, 20)))

    obj = SetDataAttr(custom_field=255)
    assert obj.to_bytes() == data


def test_long() -> None:
    data = b"\x00\x00\x00\xff\x00\x00\x00\xff"

    class SetDataAttr(RequestBodyStruct):
        custom_field: int = field(XmpLong())

    obj = SetDataAttr(custom_field=1095216660735)
    assert obj.to_bytes() == data


def test_hex() -> None:
    data = b"\x00\x00\x00\xff"

    class SetDataAttr(RequestBodyStruct):
        custom_field: Hex = field(XmpHex(size=1))
        custom_field2: Hex = field(XmpHex(size=3))

    obj = SetDataAttr(
        custom_field=Hex("00"),
        custom_field2=Hex("ff")
    )
    assert obj.to_bytes() == data


def test_hex_string() -> None:
    data = b'\x04\xf4\xbc\x9cs\xd1\x04\xf4\xbc\x9cs\xd0\xff\xff\x00\x00'

    class SetDataAttr(RequestBodyStruct):
        hex_data: Hex = field(XmpHex())

    obj = SetDataAttr(hex_data=Hex("04F4BC9C73D104F4BC9C73D0FFFF"))
    assert data == obj.to_bytes()


def test_ip_v4() -> None:
    data = b'\x7f\x00\x00\x01'

    class SetDataAttr(RequestBodyStruct):
        custom_field: IPv4Address = field(XmpIPv4Address())

    obj = SetDataAttr(custom_field=IPv4Address("127.0.0.1"))
    assert obj.to_bytes() == data


def test_ip_v6() -> None:
    data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xab'

    class SetDataAttr(RequestBodyStruct):
        custom_field: IPv6Address = field(XmpIPv6Address())

    obj = SetDataAttr(custom_field=IPv6Address("::ab"))
    assert obj.to_bytes() == data


def test_mac() -> None:
    data = b'\xf4\xd4\x88\x67\xc5\xda\x00\x00'

    class SetDataAttr(RequestBodyStruct):
        custom_field: Hex = field(XmpMacAddress())

    obj = SetDataAttr(custom_field=Hex("f4d48867c5da"))
    assert obj.to_bytes() == data


def test_string() -> None:
    data1 = b'Odin-10G-1S-6P[b]\x00\x00\x00'
    data2 = b"Xena"
    data3 = b""

    class SetDataAttr(RequestBodyStruct):
        custom_field: str = field(XmpStr())

    obj1 = SetDataAttr(custom_field="Odin-10G-1S-6P[b]")
    obj2 = SetDataAttr(custom_field="Xena")
    obj3 = SetDataAttr(custom_field="")

    assert obj1.to_bytes() == data1
    assert obj2.to_bytes() == data2
    assert obj3.to_bytes() == data3


def test_unlimited_list() -> None:
    data = b'\x00\x02\x00\x06\x00\x06\x00\x06'

    class SetDataAttr(RequestBodyStruct):
        port_counts: List[int] = field(XmpSequence(types_chunk=[XmpByte()]))

    obj = SetDataAttr(
        port_counts=[0, 2, 0, 6, 0, 6, 0, 6]
    )
    assert obj.to_bytes() == data


def test_limited_list() -> None:
    data = b'\x00\x02\x00\x00'
    MAX_LEN = 2

    class SetDataAttr(RequestBodyStruct):
        custom_field: List[int] = field(XmpSequence(types_chunk=[XmpByte()], length=MAX_LEN))

    try:
        SetDataAttr(
            custom_field=[0, 2, 0, 6, 0, 6, 0, 6]
        )
    except Exception:
        pass
    else:
        assert False, "Some how passed longer list then expected"

    obj = SetDataAttr(
        custom_field=[0, 2]
    )

    assert obj.to_bytes() == data


# endregion


# region TypeConversion

class UsersEnum(IntEnum):
    OPTION_1 = 1
    OPTION_2 = 2
    OPTION_3 = 3
    OPTION_4 = 5


def test_enum_global_def() -> None:
    data = b"\x02\x05\x00\x00"

    class SetDataAttr(RequestBodyStruct):
        custom_field: UsersEnum = field(XmpByte())
        custom_field2: UsersEnum = field(XmpByte())

    obj = SetDataAttr(
        custom_field=UsersEnum.OPTION_2,
        custom_field2=UsersEnum.OPTION_4
    )
    assert obj.to_bytes() == data


def test_enum_local_def() -> None:
    """
    At the Moment the defenition of the enum under the local namespace will faile
    """

    class UsersLocalEnum(IntEnum):
        OPTION_1 = 1
        OPTION_2 = 2
        OPTION_3 = 3
        OPTION_4 = 5

    class SetDataAttr(RequestBodyStruct):
        custom_field: UsersLocalEnum = field(XmpByte())
        custom_field2: UsersLocalEnum = field(XmpByte())

    try:
        SetDataAttr(
            custom_field=UsersLocalEnum.OPTION_2,
            custom_field2=UsersLocalEnum.OPTION_4
        )
    except TypeError as e:
        assert str(e) == "'ForwardRef' object is not callable"
    else:
        assert False, "Magicly it start to works"


def test_bool() -> None:
    data = b"\x01\x00\x00\x00"

    class SetDataAttr(RequestBodyStruct):
        custom_field: bool = field(XmpByte())
        custom_field2: bool = field(XmpByte())

    obj = SetDataAttr(
        custom_field=True,
        custom_field2=False
    )
    assert obj.to_bytes() == data


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
    data = b'\x7f\x00\x00\x01\x02\x05\x01\xf4\xd4\x88\x67\xc5\xda\x7f\x00\x00\x03\x02\x05\x00\xf4\xd4\x88\x55\xc5\xda\x00\x00'

    class SetDataAttr(RequestBodyStruct):
        custom_field: List[ArpChunk] = field(XmpSequence(types_chunk=[XmpIPv4Address(), XmpShort(), XmpByte(), XmpMacAddress()]))

    obj = SetDataAttr(
        custom_field=[
            ArpChunk(
                ipv4_address=IPv4Address("127.0.0.1"),
                prefix=517,
                patched_mac=OnOff.ON,
                mac_address=Hex("f4d48867c5da")
            ),
            ArpChunk(
                ipv4_address=IPv4Address("127.0.0.3"),
                prefix=517,
                patched_mac=OnOff.OFF,
                mac_address=Hex("f4d48855c5da")
            )
        ]
    )
    assert obj.to_bytes() == data

# endregion
