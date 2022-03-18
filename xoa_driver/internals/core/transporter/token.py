from typing import (
    TYPE_CHECKING,
    TypeVar,
    Generic,
)
from dataclasses import dataclass
if TYPE_CHECKING:
    from .. import interfaces
    from .. import protocol


AwaitableDataType = TypeVar("AwaitableDataType") 
@dataclass(frozen=True)
class Token(Generic[AwaitableDataType]):
    """
    A wrapper of connection and request. 
    Which can be used for await an single command or organized in to the ordered 
    sequence of the commands which will be send to the server in single request.
    """
    __slots__ = ('connection', 'request')
    connection: "interfaces.IConnection"
    request: "protocol.Request"

    def __await__(self):
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