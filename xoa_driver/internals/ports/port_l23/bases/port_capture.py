from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    PC_TRIGGER,
    PC_KEEP,
    PC_STATS,
    PC_EXTRA,
    PC_PACKET,
)

class ObtainCaptured:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, capture_pkt_idx: int) -> None:
        self.extra = PC_EXTRA(conn, module_id, port_id, capture_pkt_idx)
        self.packet = PC_PACKET(conn, module_id, port_id, capture_pkt_idx)

class PortCapture:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        
        self.trigger = PC_TRIGGER(conn, module_id, port_id)
        self.keep = PC_KEEP(conn, module_id, port_id)
        self.stats = PC_STATS(conn, module_id, port_id)
    
    async def obtain_captured(self) -> List[ObtainCaptured]:
        # TODO: check better title for this operation
        stats = await self.stats.get()
        return [
            ObtainCaptured(self.__conn, self.__module_id, self.__port_id, idx)
            for idx in range(stats.packets)
        ]