from enum import IntEnum
import asyncio
class ReservedRequestID(IntEnum):
    PUSH_REQUEST = 0
    
    REQUEST_ID_LIMIT = 0xFFFFFFFF
    
    @classmethod
    def started(cls) -> int:
        return max(list(cls)[:-1]).value


class RequestId:
    """Aggrigator of request ID."""
    
    __slots__ = ("__req_id", "__lock",)
    
    def __init__(self) -> None:
        self.__req_id = ReservedRequestID.started()
        self.__lock = asyncio.Lock()

    async def get_avaliable(self) -> int:
        async with self.__lock:
            if self.__req_id >= ReservedRequestID.REQUEST_ID_LIMIT:
                self.__req_id = ReservedRequestID.started()
            else:
                self.__req_id += 1
            return self.__req_id
