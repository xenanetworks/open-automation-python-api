from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4G_USER_STATE_CURRENT,
    P4G_USER_STATE_TOTAL,
    P4G_USER_STATE_RATE,
)

class GUserState:
    """User state counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.current = P4G_USER_STATE_CURRENT(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_USER_STATE_CURRENT`
        """
        self.total = P4G_USER_STATE_TOTAL(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_USER_STATE_TOTAL`
        """
        self.rate = P4G_USER_STATE_RATE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_USER_STATE_RATE`
        """