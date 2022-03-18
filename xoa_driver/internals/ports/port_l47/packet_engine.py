from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4E_ASSIGN,
    P4E_AVAILABLE,
    P4E_ALLOCATE,
    P4E_ALLOCATION_INFO,
)

class PacketEngine:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.assign = P4E_ASSIGN(conn, module_id, port_id)
        self.avaliable = P4E_AVAILABLE(conn, module_id, port_id)
        self.allocate = P4E_ALLOCATE(conn, module_id, port_id)
        self.allocation_info = P4E_ALLOCATION_INFO(conn, module_id, port_id)