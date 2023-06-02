import functools
from typing import TYPE_CHECKING
from typing_extensions import Self
from xoa_driver.internals.commands import (
    P_DYNAMIC,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .bases.port_l23_genuine import BasePortL23Genuine
from .pcs_pma_ghijkl import (
    PcsPma,
    SerDes,
)


class FamilyH(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        Representation of P_DYNAMIC
        """

    async def _setup(self) -> Self:
        await super()._setup()
        self.serdes = tuple(
            SerDes(self._conn, *self.kind, serdes_xindex=serdes_xindex)
            for serdes_xindex in range(self.info.capabilities.serdes_count)
        )
        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


class PLoki100G5S1P(FamilyH):
    """L23 port on Loki-100G-5S-1P module.
    """

    pcs_pma: PcsPma
    """PCS/PMA settings.
        
    :type: ~xoa_driver.internals.hli_v1.ports.port_l23.pcs_pma_ghijkl.PcsPma
    """

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

    async def _setup(self) -> Self:
        await super()._setup()
        self.pcs_pma = PcsPma(self._conn, self)
        return self


class POdin100G3S1P(FamilyH):
    """L23 port on Odin-100G-3S-1P module.
    """
    ...
