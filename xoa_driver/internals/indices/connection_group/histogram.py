from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4G_TIME_HIST_CONF,
    P4G_PAYLOAD_HIST_CONF,
    P4G_TRANSACTION_HIST_CONF,
    P4G_APP_TRANSACTION_HIST,
    P4G_RECALC_TIME_HIST,
    P4G_RECALC_PAYLOAD_HIST,
    P4G_RECALC_TRANSACTION_HIST,
)


class GConfigHistogram:
    """L47 Histogram Config"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.time = P4G_TIME_HIST_CONF(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TIME_HIST_CONF`
        """
        self.payload = P4G_PAYLOAD_HIST_CONF(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`
        """
        self.transaction = P4G_TRANSACTION_HIST_CONF(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TRANSACTION_HIST_CONF`
        """


class GRecalculatesHistogram:
    """L47 Histogram Recalculation."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.time = P4G_RECALC_TIME_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RECALC_TIME_HIST`
        """
        self.payload = P4G_RECALC_PAYLOAD_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RECALC_PAYLOAD_HIST`
        """
        self.transaction = P4G_RECALC_TRANSACTION_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RECALC_TRANSACTION_HIST`
        """


class GHistogram:
    """L47 Histogram."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.transaction = P4G_APP_TRANSACTION_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_APP_TRANSACTION_HIST`
        """
        self.recalculates = GRecalculatesHistogram(conn, module_id, port_id, group_idx)
        """L47 Histogram Recalculation."""
        self.config = GConfigHistogram(conn, module_id, port_id, group_idx)
        """L47 Histogram Config"""