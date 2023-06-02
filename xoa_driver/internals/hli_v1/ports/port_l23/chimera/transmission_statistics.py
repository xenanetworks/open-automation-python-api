from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PT_FLOWTOTAL,
    PT_FLOWCLEAR,
)


class TransmissionStatistics:
    """Chimera TX statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.total = PT_FLOWTOTAL(conn, module_id, port_id, flow_index)
        """TX statistics of a flow.
        
        :type: PT_FLOWTOTAL
        """

        self.clear = PT_FLOWCLEAR(conn, module_id, port_id, flow_index)
        """Clear TX statistics of a flow.
        
        :type: PT_FLOWCLEAR
        """
