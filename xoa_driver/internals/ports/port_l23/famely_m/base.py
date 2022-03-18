import functools
from typing import TYPE_CHECKING

from xoa_driver.internals.core.commands import P_BRRMODE
from xoa_driver.internals.utils import attributes as utils

from ..bases.port_l23_genuine import BasePortL23Genuine

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class FamelyM(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.brr_mode = P_BRRMODE(conn, module_id, port_id)

    on_brr_mode_change = functools.partialmethod(utils.on_event, P_BRRMODE)

class POdin1G3S6PT1RJ45(FamelyM):
    ...
