from __future__ import annotations
from asyncio import Future
from typing import ClassVar, Generic, Protocol, Type, TypeVar


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


class StreamReader(Generic[HeaderType]):
    __slots__ = ("_buffer", "_eof", "_waiter", "__header_struct")

    def __init__(self, header_struct: type[HeaderType]) -> None:
        self._buffer = bytearray()
        self._eof = False    # Whether we're done.
        self._waiter = None  # A future used by _wait_for_data()
        self.__header_struct = header_struct

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.read_pkt()
        if val == b'':
            raise StopAsyncIteration
        return val

    def _wakeup_waiter(self) -> None:
        """Wakeup read*() functions waiting for data or EOF."""
        waiter = self._waiter
        if waiter is not None:
            self._waiter = None
            if not waiter.cancelled():
                waiter.set_result(None)

    async def _wait_for_data(self, func_name: str) -> None:
        """Wait until feed_data() or feed_eof() is called.
        If stream was paused, automatically resume it.
        """
        # StreamReader uses a future to link the protocol feed_data() method
        # to a read coroutine. Running two read coroutines at the same time
        # would have an unexpected behaviour. It would not possible to know
        # which coroutine would get the next data.
        if self._waiter is not None:
            raise RuntimeError(
                f'{func_name}() called while another coroutine is '
                f'already waiting for incoming data'
            )

        assert not self._eof, '_wait_for_data after EOF'

        self._waiter = Future()
        try:
            await self._waiter
        finally:
            self._waiter = None

    def feed_eof(self) -> None:
        self._eof = True
        self._wakeup_waiter()

    def at_eof(self) -> bool:
        """Return True if the buffer is empty and 'feed_eof' was called."""
        return self._eof and not self._buffer

    def feed_data(self, data: bytes) -> None:
        assert not self._eof, 'feed_data after feed_eof'

        if not data:
            return None

        self._buffer.extend(data)
        self._wakeup_waiter()

    # async def read(self, n: int = -1) -> bytes:
    #     if n <= 0:
    #         return b''

    #     if not self._buffer and not self._eof:
    #         await self._wait_for_data('read')

    #     # This will work right even if buffer is less than n bytes
    #     data = bytes(self._buffer[:n])
    #     del self._buffer[:n]
    #     return data

    async def readexactly(self, n: int) -> bytes:
        if n < 0:
            raise ValueError('readexactly size can not be less than zero')

        if n == 0:
            return b''

        while len(self._buffer) < n:
            if self._eof:
                incomplete = bytes(self._buffer)
                self._buffer.clear()
                raise Exception(incomplete, n)

            await self._wait_for_data('readexactly')

        if len(self._buffer) == n:
            data = bytes(self._buffer)
            self._buffer.clear()
        else:
            data = bytes(self._buffer[:n])
            del self._buffer[:n]
        return data

    async def read_pkt(self) -> tuple[HeaderType, bytes]:
        h_buff = await self.readexactly(self.__header_struct.size)
        header = self.__header_struct.from_bytes(h_buff)
        if not header:
            raise Exception("Invalid Header")
        body_bytes = await self.readexactly(header.body_size)
        return (header, body_bytes)
