from typing import TYPE_CHECKING
from .bases.port_l23 import BasePortL23
from .bases.port_reception_statistics import PortReceptionStatistics
from .bases.port_transmission_statistics import PortTransmissionStatistics

from xoa_driver.internals.commands import (
    P_MDIXMODE,
    # P_ENGINENAMES, # TODO: need to implement
    # P_ENGINELOAD, # TODO: need to implement
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.hli_v1.indices.streams.base_stream import BaseStreamIdx
from xoa_driver.internals.hli_v1.indices.filter.base_filter import BaseFilterIdx
from xoa_driver.internals.state_storage import ports_state

VEStreamIndices = idx_mgr.IndexManager[BaseStreamIdx]
VEFilterIndices = idx_mgr.IndexManager[BaseFilterIdx]


class Engine:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        # self.names = P_ENGINENAMES(conn, module_id, port_id)
        # self.load = P_ENGINELOAD(conn, module_id, port_id)
        ...


class L23VEPortStatistics:
    """L23 VE port statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = PortReceptionStatistics(conn, module_id, port_id)
        """L23 VE port's RX statistics.
        
        :type: PortReceptionStatistics
        """

        self.tx = PortTransmissionStatistics(conn, module_id, port_id)
        """L23 VE port's TX statistics.
        
        :type: PortTransmissionStatistics
        """


class PortL23VE(BasePortL23):
    """L23 VE port"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

        self._local_states = ports_state.PortL23LocalState()

        self.mdix_mode = P_MDIXMODE(conn, module_id, port_id)
        """MDI/MDIX mode.
        
        :type: P_MDIXMODE
        """

        self.engine = Engine(conn, module_id, port_id)
        """Engine is not supported yet.
        
        :type: Engine
        """

        self.statistics = L23VEPortStatistics(conn, module_id, port_id)
        """Port statistics.

        :type: L23VEPortStatistics
        """

        self.streams: VEStreamIndices = idx_mgr.IndexManager(
            conn,
            BaseStreamIdx,
            module_id,
            port_id
        )
        """L23 VE port's stream index manager.
        
        :type: VEStreamIndices
        """

        self.filters: VEFilterIndices = idx_mgr.IndexManager(
            conn,
            BaseFilterIdx,
            module_id,
            port_id
        )
        """L23 VE port's filter index manager.
        
        :type: VEFilterIndices
        """

    @property
    def info(self) -> ports_state.PortL23LocalState:
        return self._local_states

    async def _setup(self):
        await self._local_states.initiate(self)
        self._local_states.register_subscriptions(self)
        return self
