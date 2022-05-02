from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4E_ASSIGN,
    P4E_AVAILABLE,
    P4E_ALLOCATE,
    P4E_ALLOCATION_INFO,
)

class PacketEngine:
    """L47 port's packet engine."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.assign = P4E_ASSIGN(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4e_commands.P4E_ASSIGN`"""
        self.avaliable = P4E_AVAILABLE(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4e_commands.P4E_AVAILABLE`"""
        self.allocate = P4E_ALLOCATE(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4e_commands.P4E_ALLOCATE`"""
        self.allocation_info = P4E_ALLOCATION_INFO(conn, module_id, port_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.p4e_commands.P4E_ALLOCATION_INFO`"""