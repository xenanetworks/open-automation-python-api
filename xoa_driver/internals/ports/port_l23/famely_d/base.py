import functools
from typing import TYPE_CHECKING
from ..bases.port_l23_genuine import BasePortL23Genuine
from xoa_driver.internals.core.commands import (
    P_MDIXMODE,
    P_AUTONEGSELECTION,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class FamelyD(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.mdix_mode = P_MDIXMODE(conn, module_id, port_id)
        self.autonneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)

    on_autoneg_selection = functools.partialmethod(utils.on_event, P_AUTONEGSELECTION)


class POdin1G3S6P(FamelyD):
    ...
class POdin1G3S6P_b(FamelyD):
    ...
class POdin1G3S6PE(FamelyD):
    ...
class POdin1G3S2PT(FamelyD):
    ...
