import functools
from typing import TYPE_CHECKING
from ..bases.port_l23_genuine import BasePortL23Genuine
from xoa_driver.internals.core.commands import (
    P_AUTONEGSELECTION, # questinable which ports are electrical
    P_LPENABLE,
    P_LPTXMODE,
    P_LPSTATUS,
    P_LPPARTNERAUTONEG,
    P_LPSNRMARGIN,
    P_LPRXPOWER,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class LowPowerMode:
    """L23 port low power mode."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.enable = P_LPENABLE(conn, module_id, port_id)
        """Energy Efficiency Ethernet.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LPENABLE`
        """
        self.mode = P_LPTXMODE(conn, module_id, port_id)
        """Low power TX mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LPTXMODE`
        """
        self.status = P_LPSTATUS(conn, module_id, port_id)
        """Low power status.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LPSTATUS`
        """
        self.partner_autonegotiation = P_LPPARTNERAUTONEG(conn, module_id, port_id)
        """EEE capabilities advertised during autonegotiation by the far side.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LPPARTNERAUTONEG`
        """
        self.snr_margin = P_LPSNRMARGIN(conn, module_id, port_id)
        """SNR margin on the four link channels by the PHY.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LPSNRMARGIN`
        """
        self.rx_power = P_LPRXPOWER(conn, module_id, port_id)
        """RX power recorded during training for the four channels.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LPRXPOWER`
        """


class FamilyE(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.autoneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)
        """L23 port's auto-negotiation selection.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_AUTONEGSELECTION`
        """
        self.eee = LowPowerMode(conn, module_id, port_id)
        """L23 port Low Power mode settings."""


    on_autoneg_selection_change = functools.partialmethod(utils.on_event, P_AUTONEGSELECTION)
    """Register a callback to the event that the L23 port's auto-negotiation selection changes."""
    on_low_power_mode_enable_change = functools.partialmethod(utils.on_event, P_LPENABLE)
    """Register a callback to the event that the L23 port's low power status changes."""
    on_low_power_mode_change = functools.partialmethod(utils.on_event, P_LPTXMODE)
    """Register a callback to the event that the L23 port's low power mode changes."""



class POdin5G4S6PCU(FamilyE):
    """L23 port on Odin-5G-4S-6P-CU module.
    """
    ...

class POdin10G5S6PCU(FamilyE):
    """L23 port on Odin-10G-5S-6P-CU module.
    """
    ...

class POdin10G5S6PCU_b(FamilyE):
    """L23 port on Odin-10G-5S-6P-CU[b] module.
    """
    ...

class POdin10G3S6PCU(FamilyE):
    """L23 port on Odin-10G-3S-6P-CU module.
    """
    ...

class POdin10G3S2PCU(FamilyE):
    """L23 port on Odin-10G-3S-2P-CU module.
    """
    ...
