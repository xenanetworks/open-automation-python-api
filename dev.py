
from __future__ import annotations
from dataclasses import dataclass
from enum import IntEnum
from ipaddress import IPv4Address
import os
import sys
from typing import List, NewType
from xoa_driver.internals.core.protocol.payload import (
    field,
    ResponseBodyStruct,
    RequestBodyStruct,
    XmpByte,
    XmpHex,
    XmpInt,
    XmpIPv4Address,
    XmpIPv6Address,
    XmpLong,
    XmpMacAddress,
    XmpSequence,
    XmpShort,
    XmpStr
)

sys.path.insert(0, os.path.abspath("."))

# Conditions
# 1) Request payload structure can be set only once
# 2) Responce values structure is read only
# 3) Command suppose to have a deprication warnings
# 4) XmpType defenition suppose to be generic and simple
# 5) Field declaration suppose to define specifications as: ( signed/unsigned, is it a list, list size, )
# 6) Set command also suppose to handle future compatable fields


DATA = b'\x00\x01\x86\xa0\x00\x00\x03\xe8\x00\x00\x00\x10\x00\x00\x00?\x00\x00\x00\x0c\x00\x00\x01\x00\x00\x00\x00\xc8\x12\xa0_ \x00\x03\r@;\x9a\xca\x00\x7f\xff\xff\xffw5\x94\x00\x00\x00\x00<\x00\x000\x00\x00\x00\x08\x00\x00\x00\x00\x1e\x00\x00\x00\x12\x00\x00\x00\x08\x00\x00\x00\x02\x00\x00\x10\x00\x00\x00\x07\xdf\x00\x00\x00\n\x00\x00\x00\x06\x00\x00\x00\x06\x00\x00\x00\x04\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x10\x00\x00\x00\x07\xdf\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x14\x00\x00\x00\x03\x00\x00\x00d\x00\x00\x00d\x00\x00\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'


class TrafficEngine(IntEnum):
    """Traffic Engine"""
    TGA = 1
    """Normal TGA"""
    MICRO_TGA = 2
    """Micro TGA"""
    OTHER = 100000


Hex = NewType('Hex', str)


def string_test() -> None:
    OWNER = "XenaNetwork"
    DATA_C_STATSESSION = b'\x00\x00\x00\x01\xc0\xa8\x01\x1bACO\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb3\x00\x00\x00\x00\x00\x00\x0bX\x00\x00\x00\x00\x00\x005\xd8'

    class StringTestSet(RequestBodyStruct):
        session_type: int = field(XmpInt())
        ipv4_address: IPv4Address = field(XmpIPv4Address())
        owner: str = field(XmpStr())
        operation_count: int = field(XmpLong(signed=True))
        requested_byte_count: int = field(XmpLong(signed=True))
        responded_byte_count: int = field(XmpLong(signed=True))

    class StringTestGet(ResponseBodyStruct):
        session_type: int = field(XmpInt())
        ipv4_address: IPv4Address = field(XmpIPv4Address())
        owner: str = field(XmpStr(min_len=8))
        operation_count: int = field(XmpLong(signed=True))
        requested_byte_count: int = field(XmpLong(signed=True))
        responded_byte_count: int = field(XmpLong(signed=True))

    d = StringTestSet(
        session_type=1,
        ipv4_address=IPv4Address("192.168.1.198"),
        owner=OWNER,
        operation_count=42999,
        requested_byte_count=691808,
        responded_byte_count=3975772
    )
    print(d.to_bytes())

    d1 = StringTestGet(DATA_C_STATSESSION)
    print(d1.session_type)
    print(d1.ipv4_address)
    print(d1.owner)
    print(d1.operation_count)
    print(d1.requested_byte_count)
    print(d1.responded_byte_count)


@dataclass
class ArpChunk:
    ipv4_address: IPv4Address
    prefix: int
    patched_mac: int
    mac_address: Hex


class ProtoSetDataAttr(RequestBodyStruct):
    """Set Only"""
    max_speed: TrafficEngine = field(XmpInt())
    max_speed_reduction: int = field(XmpInt())
    min_interframe_gap: int = field(XmpInt(signed=True))
    max_interframe_gap: Hex = field(XmpHex(size=2))
    some_iterable: List[int] = field(XmpSequence(types_chunk=[XmpInt()], length=2))
    # some_iterable: List[ArpChunk] = field(
    #     XmpSequence(
    #         types_chunk=[XmpIPv4Address(), XmpInt(), XmpInt(), XmpHex(size=2)],
    #         # length=5
    #     )
    # )
#     # max_preamble: IPv4Address = field(XmpIPv4Address())


class ProtoGetDataAttr(ResponseBodyStruct):
    """Get Only"""
    max_speed: TrafficEngine = field(XmpInt())
    max_speed_reduction: int = field(XmpInt())
    min_interframe_gap: int = field(XmpInt())
    max_interframe_gap: Hex = field(XmpHex(size=2))
    some_iterable: List[TrafficEngine] = field(XmpSequence(types_chunk=[XmpInt()], length=2))
    # some_iterable: List[ArpChunk] = field(
    #     XmpSequence(
    #         types_chunk=[XmpIPv4Address(), XmpInt(), XmpInt(), XmpHex(size=2)],
    #         # length=5
    #     )
    # )
    # max_preamble: IPv4Address = field(XmpIPv4Address())


def main() -> None:
    ...
    # string_test()


    # some_iterable: list[int] = field(XmpSequence(types_chunk=[XmpInt()],))
    # some_iterable: list[TrafficEngine] = field(XmpSequence(types_chunk=[XmpInt()],))
    # some_iterable: list[TrafficEngine] = field(XmpSequence(types_chunk=[XmpInt()], length=5))
    # some_iterable: list[ArpChunk] = field(
    #     XmpSequence(
    #         types_chunk=[XmpIPv4Address(), XmpInt(), XmpInt(), XmpHex(size=2)],
    #         length=5
    #     )
    # )

    for _ in range(3_000_000):
        req = ProtoSetDataAttr(
            max_speed=TrafficEngine.MICRO_TGA,
            max_speed_reduction=10,
            min_interframe_gap=-2,
            max_interframe_gap=Hex("05ff"),
            some_iterable=[1, 2,],
            # some_iterable=[
            #     ArpChunk(IPv4Address("127.0.0.1"), 2, 10, Hex("05ff")),
            #     ArpChunk(IPv4Address("127.0.0.11"), 2, 10, Hex("98ff")),
            # ]
            # max_preamble=IPv4Address("127.0.0.1")
        )
        (req.to_bytes())
        # print(req.to_hex())
        res = ProtoGetDataAttr(req.to_bytes())
        # (res.max_speed)
        # # print(res.max_speed_reduction)
        # # print(res.min_interframe_gap)
        # (res.max_interframe_gap)
        # (res.some_iterable)
        # print(res.max_preamble)
        # # a = res.max_interframe_gap + 1

        # # d = GetDataAttr(data)
        # # print(d.max_speed)
        # # print(d.tx_eq_tap_max_val)

        # # a = memoryview(data).toreadonly()
        # # b = bytearray(data)
        # # print(a.hex(" "))
        # print(b'\x00\x00\x00\x0c\x00\x00\x01\x00\x00\x00\x00\xc8\x12\xa0_ '.hex(" "))


if __name__ == '__main__':
    # run code
    # main()

    # Performance Test
    import cProfile
    import pstats
    import timeit
    with cProfile.Profile() as pr:
        main()
        # result = timeit.timeit(
        #     "main()",
        #     setup="from __main__ import main",
        #     number=100000
        # )
        # print(result)
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    stats.print_stats(20)
