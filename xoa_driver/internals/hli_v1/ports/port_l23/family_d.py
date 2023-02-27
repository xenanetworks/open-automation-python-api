from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    P_MDIXMODE,
    P_AUTONEGSELECTION,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .bases.port_l23_genuine import BasePortL23Genuine


class FamilyD(BasePortL23Genuine):
    """L23 ports that supports MDI/MDIX and """

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.mdix_mode = P_MDIXMODE(conn, module_id, port_id)
        """L23 port's MDI/MDIX mode.
        
        :type: P_MDIXMODE
        """

        self.autoneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)
        """L23 port's auto-negotiation selection.
        
        :type: P_AUTONEGSELECTION
        """


class POdin1G3S6P(FamilyD):
    """L23 port on Odin-1G-3S-6P module.
    """
    ...


class POdin1G3S6P_b(FamilyD):
    """L23 port on Odin-1G-3S-6P[b] module.
    """
    ...


class POdin1G3S6PE(FamilyD):
    """L23 port on Odin-1G-3S-6P-E module.
    """
    ...


class POdin1G3S2PT(FamilyD):
    """L23 port on Odin-1G-3S-2P-T module.
    """
    ...
