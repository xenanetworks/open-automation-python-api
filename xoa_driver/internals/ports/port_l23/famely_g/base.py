import functools
from typing import TYPE_CHECKING
from ..bases.port_l23_genuine import BasePortL23Genuine

from xoa_driver.internals.core.commands import (
    P_FAULTSIGNALING,
    P_FAULTSTATUS,
    P_DYNAMIC,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from ..pcs_pma_ghijkl import (
    PcsPma,
    SerDes,
)
class Fault:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.signaling = P_FAULTSIGNALING(conn, module_id, port_id)
        self.status = P_FAULTSTATUS(conn, module_id, port_id)


class FamelyG(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        self.pcs_pma = PcsPma(conn, self)

    async def _setup(self):
        await super()._setup()
        self.ser_des = tuple(
            SerDes(self._conn, *self.kind, serdes_xindex=serdes_xindex)
            for serdes_xindex in range(self.info.capabilities.serdes_count)
        )
        return self

    on_fault_signaling_change = functools.partialmethod(utils.on_event, P_FAULTSIGNALING)
    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)



class PLoki100G3S1P(FamelyG):
    ...

class PLoki100G3S1P_b(FamelyG):
    ...

class PLoki100G3S1PSE(FamelyG):
    ...

