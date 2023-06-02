from __future__ import annotations
from asyncio import Future
from typing import Generic
from typing_extensions import Self
from ._typings import HeaderType


class StreamReader(Generic[HeaderType]):
    __slots__ = ("_buffer", "_eof", "_waiter", "__header_struct")

    def __init__(self, header_struct: type[HeaderType]) -> None:
        self._buffer = bytearray()
        self._eof = False  # Whether we're done.
        self._waiter = None  # A future used by _wait_for_data()
        self.__header_struct = header_struct

    def __aiter__(self) -> Self:
        return self

    async def __anext__(self) -> tuple[HeaderType, bytes]:
        try:
            val = await self.read_pkt()
        except EOFError:
            raise StopAsyncIteration
        else:
            return val

    def _wakeup_waiter(self) -> None:
        waiter = self._waiter
        if waiter is not None:
            self._waiter = None
            if not waiter.cancelled():
                waiter.set_result(None)

    async def _wait_for_data(self, func_name: str) -> None:
        """Wait until feed_data() or feed_eof() is called.
        If stream was paused, automatically resume it.
        """
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

    async def readexactly(self, n: int) -> bytes:
        if n < 0:
            raise ValueError('readexactly size can not be less than zero')

        if n == 0:
            return b''

        while len(self._buffer) < n:
            if self._eof:
                incomplete = bytes(self._buffer)
                self._buffer.clear()
                raise EOFError(incomplete, n)

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
            raise ValueError("Invalid Header")
        body_bytes = await self.readexactly(header.body_size)
        return (header, body_bytes)
