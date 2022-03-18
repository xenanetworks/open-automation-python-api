import functools
from typing import TYPE_CHECKING
from .bases.port_l23 import BasePortL23
from .bases.port_reception_statistics import PortReceptionStatistics

from xoa_driver.internals.core.commands import (
    P_MDIXMODE,
    # P_ENGINENAMES, # TODO: need to implment
    # P_ENGINELOAD, # TODO: need to implment
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.indices.streams.base_stream import BaseStreamIdx
from xoa_driver.internals.indices.filter.base_filter import BaseFilterIdx

VEStreamIndices = idx_mgr.IndexManager[BaseStreamIdx]
VEFilterIndices = idx_mgr.IndexManager[BaseFilterIdx]

class Engine:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        # self.names = P_ENGINENAMES(conn, module_id, port_id)
        # self.load = P_ENGINELOAD(conn, module_id, port_id)
        ...

class PortL23VE(BasePortL23):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.mdix_mode = P_MDIXMODE(conn, module_id, port_id)
        self.engine = Engine(conn, module_id, port_id)
        self.prs = PortReceptionStatistics(conn, module_id, port_id)
        
        self.streams: VEStreamIndices = idx_mgr.IndexManager(
            conn, 
            BaseStreamIdx, 
            module_id, 
            port_id
        )
        self.filters: VEFilterIndices = idx_mgr.IndexManager(
            conn, 
            BaseFilterIdx, 
            module_id, 
            port_id
        )
    
    on_mdix_mode_change = functools.partialmethod(utils.on_event, P_MDIXMODE)