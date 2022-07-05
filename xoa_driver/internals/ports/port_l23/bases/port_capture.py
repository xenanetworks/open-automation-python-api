from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P_CAPTURE,
    PC_TRIGGER,
    PC_KEEP,
    PC_STATS,
    PC_EXTRA,
    PC_PACKET,
)

class ObtainCaptured:
    """Obtain info of captured packets.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, capture_pkt_idx: int) -> None:
        self.extra = PC_EXTRA(conn, module_id, port_id, capture_pkt_idx)
        """Obtains extra information about a captured packet on a L23 port.
        Representation of :class:`~xoa_driver.internals.core.commands.pc_commands.PC_EXTRA`
        """
        self.packet = PC_PACKET(conn, module_id, port_id, capture_pkt_idx)
        """Obtains raw bytes of a captured packet on a L23 port.
        Representation of :class:`~xoa_driver.internals.core.commands.pc_commands.PC_PACKET`
        """

class PortCapture:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.state = P_CAPTURE(conn, module_id, port_id)
        """L23 port traffic capture.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_CAPTURE`
        """
        self.trigger = PC_TRIGGER(conn, module_id, port_id)
        """L23 port packet capture triggering criteria.
        Representation of :class:`~xoa_driver.internals.core.commands.pc_commands.PC_TRIGGER`
        """
        self.keep = PC_KEEP(conn, module_id, port_id)
        """Keeping captured packets on a L23 port.
        Representation of :class:`~xoa_driver.internals.core.commands.pc_commands.PC_KEEP`
        """
        self.stats = PC_STATS(conn, module_id, port_id)
        """L23 port's number of packets in the capture buffer.
        Representation of :class:`~xoa_driver.internals.core.commands.pc_commands.PC_STATS`
        """
    
    async def obtain_captured(self) -> List[ObtainCaptured]:
        # TODO: check better title for this operation
        stats = await self.stats.get()
        return [
            ObtainCaptured(self.__conn, self.__module_id, self.__port_id, idx)
            for idx in range(stats.packets)
        ]