import asyncio
from loguru import logger
import functools
from typing import TYPE_CHECKING
from xoa_driver.internals.ports import base_port

from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.core.commands import (
    P_CAPABILITIES,
    P_INTERFACE,
    P_STATUS,
    P_TXENABLE,
    P_LOADMODE,
    P_EMULATE,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    
from xoa_driver.internals.state_storage import ports_state
from ..pcs_pma_ijkl_chimera import PcsPma
from .pe_custom_distribution import CustomDistributions

from .port_emulation import ChimeraPE
class PortChimera(base_port.BasePort[ports_state.PortChimeraLocalState]):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        self.interface = P_INTERFACE(conn, module_id, port_id)
        self.status = P_STATUS(conn, module_id, port_id)
        self.tx_enable = P_TXENABLE(conn, module_id, port_id)
        self.load_mode = P_LOADMODE(conn, module_id, port_id)
        self.emulate = P_EMULATE(conn, module_id, port_id)
        self.custom_distributions = CustomDistributions(conn, module_id, port_id)
        self.pcs_pma = PcsPma(conn, self)
        
        self.local_states = ports_state.PortChimeraLocalState()
    
    
    async def _setup(self):
        *_, capabilities, emulation =  await asyncio.gather(
            super()._setup(),
            self.custom_distributions.server_sync(),
            self.capabilities.get(),
            ChimeraPE(self._conn, *self.kind),
        )
        self.local_states.capabilities = capabilities # type: ignore
        self.emulation = emulation
        return self
    
    on_interface_change = functools.partialmethod(utils.on_event, P_INTERFACE)
    on_status_change = functools.partialmethod(utils.on_event, P_STATUS)
    on_emulate_change = functools.partialmethod(utils.on_event, P_EMULATE)
    on_tx_enable_change = functools.partialmethod(utils.on_event, P_TXENABLE)