
import functools
from typing import TYPE_CHECKING, Tuple
from typing_extensions import Self
from xoa_driver.internals.commands import (
    P_DYNAMIC,
)
from xoa_driver import enums
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .bases.port_l23_genuine import BasePortL23Genuine
from .pcs_pma_ijkl_chimera import PcsPma as PcsPma1
from .pcs_pma_ghijkl import (
    PcsPma as PcsPma2,
    SerDes,
)
from .pcs_pma_l import PcsPma as PcsPma3  
from .freya_l1 import Layer1

class PcsPma(PcsPma1, PcsPma2, PcsPma3):
    """Freya PCS/PMA
    """
    def __init__(self, conn: "itf.IConnection", port) -> None:
        PcsPma1.__init__(self, conn, port)
        PcsPma2.__init__(self, conn, port)
        PcsPma3.__init__(self, conn, port)

class L1(Layer1):
    """Freya L1
    """
    def __init__(self, conn: "itf.IConnection", port) -> None:
        Layer1.__init__(self, conn, port)


class FamilyFreya(BasePortL23Genuine):
    pcs_pma: PcsPma
    """PCS/PMA layer

    :type: PcsPma
    """
    
    serdes: Tuple[SerDes, ...]
    """SerDes index

    :type: Tuple[SerDes, ...]
    """

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """

        # self.fault = Fault(conn, module_id, port_id)

    async def _setup(self) -> Self:
        await super()._setup()
        self.pcs_pma = PcsPma(self._conn, self)
        self.serdes = tuple(
            SerDes(self._conn, *self.kind, serdes_xindex=serdes_xindex)
            for serdes_xindex in range(self.info.capabilities.serdes_count)
        )
        self.l1 = L1(self._conn, self)
        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


class PFreya800G1S1P_a(FamilyFreya):
    """L23 port on Freya-800G-1S-1P[a] module.
    """
    ...


class PFreya800G1S1P_b(FamilyFreya):
    """L23 port on Freya-800G-1S-1P[b] module.
    """
    ...


class PFreya800G1S1POSFP_a(FamilyFreya):
    """L23 port on Freya-800G-1S-1P-OSFP[a] module.
    """
    ...

class PFreya800G1S1POSFP_b(FamilyFreya):
    """L23 port on Freya-800G-1S-1P-OSFP[b] module.
    """
    ...


class PFreya800G4S1P_a(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[a] module.
    """
    ...


class PFreya800G4S1P_b(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[b] module.
    """
    ...


class PFreya800G4S1P_c(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[c] module.
    """
    ...


class PFreya800G4S1P_d(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[d] module.
    """
    ...


class PFreya800G4S1P_e(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[e] module.
    """
    ...


class PFreya800G4S1P_f(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[f] module.
    """
    ...


class PFreya800G4S1POSFP_a(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[a] module.
    """
    ...


class PFreya800G4S1POSFP_b(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[b] module.
    """
    ...


class PFreya800G4S1POSFP_c(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[c] module.
    """
    ...


class PFreya800G4S1POSFP_d(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[d] module.
    """
    ...


class PFreya800G4S1POSFP_e(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[e] module.
    """
    ...


class PFreya800G4S1POSFP_f(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[f] module.
    """
    ...