from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    PT_FLOWTOTAL,
    PT_FLOWCLEAR,
)

class TransmissionStatistics:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_idx: int) -> None:
        self.total = PT_FLOWTOTAL(conn, module_id, port_id, flow_idx)
        self.clear = PT_FLOWCLEAR(conn, module_id, port_id, flow_idx)