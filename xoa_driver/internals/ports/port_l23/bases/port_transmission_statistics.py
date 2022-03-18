from typing import (
    TYPE_CHECKING,
    Union,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.indices.streams.genuine_stream import GenuineStreamIdx
from xoa_driver.internals.core.commands import (
    PT_TOTAL,
    PT_NOTPLD,
    PT_STREAM,
    PT_CLEAR,
    PT_EXTRA,
)

class PortTransmissionStatistics:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.total = PT_TOTAL(conn, module_id, port_id)
        self.extra = PT_EXTRA(conn, module_id, port_id)
        self.no_tpld = PT_NOTPLD(conn, module_id, port_id)
        self.clear = PT_CLEAR(conn, module_id, port_id)

    def obtain_from_stream(self, stream: Union[int, "GenuineStreamIdx"]) -> "PT_STREAM":
        stream_idx = stream if isinstance(stream, int) else stream.kind.index_id
        return PT_STREAM(
            self.__conn,
            self.__module_id,
            self.__port_id,
            stream_idx
        )
