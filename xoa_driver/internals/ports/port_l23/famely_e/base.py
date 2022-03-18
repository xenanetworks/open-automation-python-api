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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.enable = P_LPENABLE(conn, module_id, port_id)
        self.mode = P_LPTXMODE(conn, module_id, port_id)
        self.status = P_LPSTATUS(conn, module_id, port_id)
        self.partner_autonegotiation = P_LPPARTNERAUTONEG(conn, module_id, port_id)
        self.snr_margin = P_LPSNRMARGIN(conn, module_id, port_id)
        self.rx_power = P_LPRXPOWER(conn, module_id, port_id)


class FamelyE(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.autonneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)
        self.eee = LowPowerMode(conn, module_id, port_id)


    on_autoneg_selection_change = functools.partialmethod(utils.on_event, P_AUTONEGSELECTION)
    on_Low_power_mode_enable_change = functools.partialmethod(utils.on_event, P_LPENABLE)
    on_Low_power_mode_change = functools.partialmethod(utils.on_event, P_LPTXMODE)



class POdin5G4S6PCU(FamelyE):
    ...

class POdin10G5S6PCU(FamelyE):
    ...

class POdin10G5S6PCU_b(FamelyE):
    ...

class POdin10G3S6PCU(FamelyE):
    ...

class POdin10G3S2PCU(FamelyE):
    ...
