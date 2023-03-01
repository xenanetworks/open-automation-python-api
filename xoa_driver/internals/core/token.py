from __future__ import annotations
from typing import (
    Any,
    Awaitable,
    TypeVar,
    # Generic,
    Generator
)
from dataclasses import dataclass

from . import interfaces
from .transporter.protocol.struct_request import Request


AwaitableDataType = TypeVar("AwaitableDataType", covariant=True)


@dataclass(frozen=True)
class Token(Awaitable[AwaitableDataType]):
    """
    A wrapper of connection and request.
    Which can be used for await an single command or organized in to the ordered
    sequence of the commands which will be send to the server in single request.
    """
    __slots__ = ('connection', 'request',)

    connection: interfaces.IConnection
    request: Request

    def __await__(self) -> Generator[Any, None, AwaitableDataType]:
        return self.__ask().__await__()

    async def __ask(self) -> AwaitableDataType:
        (
            data,
            fut
        ) = await self.connection.prepare_data(self.request)
        self.connection.send(data)
        try:
            result = await fut
        except Exception as e:
            raise e
        else:
            return result
