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
    """Chimera port for traffic impairment."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        """Chimera port capabilities.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_CAPABILITIES`
        """
        self.interface = P_INTERFACE(conn, module_id, port_id)
        """Physical interface type of the Chimera port.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_INTERFACE`
        """
        self.status = P_STATUS(conn, module_id, port_id)
        """Chimera port's received optical signal level'.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_STATUS`
        """
        self.tx_enable = P_TXENABLE(conn, module_id, port_id)
        """Enabling Chimera port TX.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXENABLE`
        """
        self.load_mode = P_LOADMODE(conn, module_id, port_id)
        """Load mode of the Chimera port.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LOADMODE`
        """
        self.emulate = P_EMULATE(conn, module_id, port_id)
        """Chimera port emulation control.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_EMULATE`
        """
        self.custom_distributions = CustomDistributions(conn, module_id, port_id)
        """Custom distributions."""
        self.pcs_pma = PcsPma(conn, self)
        """"PCS/PMA settings."""
        
        self.local_states = ports_state.PortChimeraLocalState()
        """Local states of the Chimera port."""
    
    
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
    """Register a callback to the event that the port's interface type changes."""
    on_status_change = functools.partialmethod(utils.on_event, P_STATUS)
    """Register a callback to the event that the port's optical signal level changes."""
    on_emulate_change = functools.partialmethod(utils.on_event, P_EMULATE)
    """Register a callback to the event that the port's emulation state changes."""
    on_tx_enable_change = functools.partialmethod(utils.on_event, P_TXENABLE)
    """Register a callback to the event that the port's TX status changes."""