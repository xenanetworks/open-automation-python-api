from __future__ import annotations
import asyncio
import ctypes as c
from typing import (
    AsyncGenerator,
    Generic,
    # Protocol,
    TypeVar,
)

# StructType = TypeVar("StructType", bound="c.BigEndianStructure", covariant=True)


# class PacketHeader(Protocol["c.BigEndianStructure"]):
#     @property
#     def body_size(self) -> int:
#         ...


HeaderType = TypeVar("HeaderType", bound="c.BigEndianStructure")


def _calc_body_position(header_pos: slice, body_size: int) -> slice:
    return slice(
        header_pos.stop,
        header_pos.stop + body_size
    )


def _header_bytes_is_valid(header_bytes: bytearray, expected_size: int, magic_wrd: bytes) -> bool:
    is_correct_size = len(header_bytes) == expected_size
    start_with_mw = header_bytes.startswith(magic_wrd)
    return is_correct_size and start_with_mw


class Stream(Generic[HeaderType]):
    def __init__(self, header_struct: type[HeaderType], magic_wrd: bytes) -> None:
        self.__buffer = bytearray()
        self.__magic_wrd = magic_wrd
        self.__header_struct = header_struct
        self.__header_pos = slice(c.sizeof(header_struct))
        self.__wait_data = asyncio.Event()

    def __pop(self) -> tuple[HeaderType, bytearray] | None:
        # need to manage of the data copying
        buff = self.__buffer
        header_bytes = buff[self.__header_pos]
        if not _header_bytes_is_valid(header_bytes, self.__header_pos.stop, self.__magic_wrd):
            return None
        header = self.__header_struct.from_buffer_copy(header_bytes)
        BODY_POS = _calc_body_position(
            self.__header_pos,
            header.body_size
        )
        body_bytes = buff[BODY_POS]
        if len(body_bytes) < header.body_size:
            return None
        try:
            return (header, body_bytes)
        finally:
            del self.__buffer[slice(BODY_POS.stop)]
            if len(self.__buffer) == 0:
                self.__wait_data.clear()

    def write(self, data: bytes) -> None:
        self.__buffer.extend(data)
        if not self.__wait_data.is_set():
            self.__wait_data.set()

    async def read(self) -> AsyncGenerator[tuple[HeaderType, bytearray], None]:
        while True:
            await self.__wait_data.wait()
            if resp := self.__pop():
                yield resp
