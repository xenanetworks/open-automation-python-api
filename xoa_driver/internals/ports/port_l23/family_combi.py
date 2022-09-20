import functools
from typing import TYPE_CHECKING
from .bases.port_l23_genuine import BasePortL23Genuine
from . import family_f
from xoa_driver.internals.core.commands import P_AUTONEGSELECTION
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class POdin1G4S4PCombi(BasePortL23Genuine):
    """L23 ports that supports MDI/MDIX and """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        
        self.autoneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)
        """L23 port's auto-negotiation selection.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_AUTONEGSELECTION`
        """

    on_autoneg_selection = functools.partialmethod(utils.on_event, P_AUTONEGSELECTION)
    """Register a callback to the event that the L23 port's auto-negotiation selection changes."""

class POdin1G4S4PCombi_b(POdin1G4S4PCombi):
    """L23 port on Odin-1G-4S-2P-Combi_b module.
    """
    ...


class POdin10G4S2PCombi(family_f.FamilyF):
    """L23 port on Odin-10G-4S-2P-Combi module.
    """
    ...

class POdin10G4S2PCombi_b(family_f.FamilyF):
    """L23 port on Odin-10G-4S-2P-Combi_b module.
    """
    ...