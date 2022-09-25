from typing import TYPE_CHECKING
from xoa_driver.internals.core.commands import (
    P_FAULTSIGNALING,
    P_FAULTSTATUS,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    
class Fault:
    """L23 port fault settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.signaling = P_FAULTSIGNALING(conn, module_id, port_id)
        """L23 port fault signaling.
        Representation ofP_FAULTSIGNALING
        """
        
        self.status = P_FAULTSTATUS(conn, module_id, port_id)
        """L23 port fault status.
        Representation of P_FAULTSTATUS
        """