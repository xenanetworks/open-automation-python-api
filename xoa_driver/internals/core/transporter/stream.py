from __future__ import annotations
import asyncio
from collections import deque
from itertools import islice
from typing import (
    AsyncGenerator,
    ClassVar,
    Generic,
    Protocol,
    Type,
    TypeVar,
)

HeaderType = TypeVar("HeaderType", bound="ResponseHeader")


class ResponseHeader(Protocol):
    size: ClassVar[int]

    @property
    def body_size(self) -> int:
        ...

    @property
    def is_pushed(self) -> bool:
        ...

    @classmethod
    def from_bytes(cls: Type["HeaderType"], buff: bytes) -> "HeaderType" | None:
        ...


class Stream(Generic[HeaderType]):
    __slots__ = ("__queue", "__header_struct", "__wait_data")

    def __init__(self, header_struct: type[HeaderType]) -> None:
        self.__queue: deque[int] = deque(b"")
        self.__header_struct = header_struct

    def __pop_n_bytes(self, n_bytes: int) -> bytes:
        def safe_pop() -> int | None:
            try:
                return self.__queue.popleft()
            except IndexError:
                return None
        return bytes(islice(iter(safe_pop, None), n_bytes))

    def __pop_packet(self) -> tuple[HeaderType, bytes] | None:
        h_buff = self.__pop_n_bytes(self.__header_struct.size)
        if not h_buff:
            return None
        header = self.__header_struct.from_bytes(h_buff)
        if header is None:
            self.__queue.extendleft(h_buff)
            return None
        body_bytes = self.__pop_n_bytes(header.body_size)
        if len(body_bytes) < header.body_size:
            self.__queue.extendleft(body_bytes)
            self.__queue.extendleft(h_buff)
            return None
        return (header, body_bytes)

    def empty(self) -> bool:
        """Return True if the stream is empty, False otherwise."""
        return not self.__queue

    def write(self, data: bytes) -> None:
        self.__queue.extend(data)

    async def read(self) -> AsyncGenerator[tuple[HeaderType, bytes], None]:
        while True:
            await asyncio.sleep(0)
            parsed = self.__pop_packet()
            if not parsed:
                await asyncio.sleep(0)
                continue
            header, body_bytes = parsed
            yield header, body_bytes
