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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.time = P4G_TIME_HIST_CONF(conn, module_id, port_id, group_idx)
        self.payload = P4G_PAYLOAD_HIST_CONF(conn, module_id, port_id, group_idx)
        self.transaction = P4G_TRANSACTION_HIST_CONF(conn, module_id, port_id, group_idx)


class GRecalculatesHistogram:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.time = P4G_RECALC_TIME_HIST(conn, module_id, port_id, group_idx)
        self.payload = P4G_RECALC_PAYLOAD_HIST(conn, module_id, port_id, group_idx)
        self.transaction = P4G_RECALC_TRANSACTION_HIST(conn, module_id, port_id, group_idx)


class GHistogram:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.transaction = P4G_APP_TRANSACTION_HIST(conn, module_id, port_id, group_idx)
        self.recalculates = GRecalculatesHistogram(conn, module_id, port_id, group_idx)
        self.config = GConfigHistogram(conn, module_id, port_id, group_idx)