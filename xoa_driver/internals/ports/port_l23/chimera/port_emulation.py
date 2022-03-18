from typing import (
    TYPE_CHECKING,
    Tuple,
)
from dataclasses import astuple
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.core.commands.enums import FilterType
from xoa_driver.internals.core.commands import (
    PE_FCSDROP,
    PE_TPLDMODE,
    PE_COMMENT,
    PE_INDICES,
    PE_LATENCYRANGE,
    PE_CORRUPT,
    PE_MISORDER,
    PE_BANDPOLICER,
    PE_BANDSHAPER,
    PE_DROPTOTAL,
    PE_LATENCYTOTAL,
    PE_DUPTOTAL,
    PE_MISTOTAL,
    PE_CORTOTAL,
    PE_JITTERTOTAL,
    PE_CLEAR,
    PE_FLOWDROPTOTAL,
    PE_FLOWLATENCYTOTAL,
    PE_FLOWDUPTOTAL,
    PE_FLOWMISTOTAL,
    PE_FLOWCORTOTAL,
    PE_FLOWJITTERTOTAL,
    PE_FLOWCLEAR,
)

from .reception_statistics import ReceptionStatistics
from .transmission_statistics import TransmissionStatistics
from .pe_distribution import PEDistribution
from .pe_filter_definition import FilterDefinition

class CTotalFlow:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_idx: int) -> None:
        self.drop_packets = PE_FLOWDROPTOTAL(conn, module_id, port_id, flow_idx)
        self.latency_packets = PE_FLOWLATENCYTOTAL(conn, module_id, port_id, flow_idx)
        self.duplicated_packets = PE_FLOWDUPTOTAL(conn, module_id, port_id, flow_idx)
        self.mis_ordered_packets = PE_FLOWMISTOTAL(conn, module_id, port_id, flow_idx)
        self.corrupted_packets = PE_FLOWCORTOTAL(conn, module_id, port_id, flow_idx)
        self.jittered_packets = PE_FLOWJITTERTOTAL(conn, module_id, port_id, flow_idx)

class StatisticsTotals:
    def __init__(self, conn, module_id, port_id) -> None:
        self.drop = PE_DROPTOTAL(conn, module_id, port_id)
        self.latency = PE_LATENCYTOTAL(conn, module_id, port_id)
        self.duplicated = PE_DUPTOTAL(conn, module_id, port_id)
        self.mis_ordered = PE_MISTOTAL(conn, module_id, port_id)
        self.corrupted = PE_CORTOTAL(conn, module_id, port_id)
        self.jittered = PE_JITTERTOTAL(conn, module_id, port_id)

class CFlowStatistics:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_idx: int) -> None:
        self.rx = ReceptionStatistics(conn, module_id, port_id, flow_idx)
        self.tx = TransmissionStatistics(conn, module_id, port_id, flow_idx)
        self.total = CTotalFlow(conn, module_id, port_id, flow_idx)
        self.clear = PE_FLOWCLEAR(conn, module_id, port_id, flow_idx)

class CBandwidth:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_idx: int) -> None:
        self.policer = PE_BANDPOLICER(conn, module_id, port_id, flow_idx)
        self.shaper = PE_BANDSHAPER(conn, module_id, port_id, flow_idx)


class CFlow:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_idx: int) -> None:
        self.comment = PE_COMMENT(conn, module_id, port_id, flow_idx)
        self.latency_range = PE_LATENCYRANGE(conn, module_id, port_id, flow_idx)
        self.impairment_corruption = PE_CORRUPT(conn, module_id, port_id, flow_idx)
        self.misordering_depth = PE_MISORDER(conn, module_id, port_id, flow_idx)
        self.bandwidth = CBandwidth(conn, module_id, port_id, flow_idx)
        self.statistics = CFlowStatistics(conn, module_id, port_id, flow_idx)
        self.distribution = PEDistribution(conn, module_id, port_id, flow_idx)
        
        self.shadow_copy = FilterDefinition(conn, module_id, port_id, flow_idx, FilterType.SHADOWN)
        self.working_copy = FilterDefinition(conn, module_id, port_id, flow_idx, FilterType.WORKING)
        
        

class ChimeraPE:
    """Port Emulation"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self._conn = conn
        self.module_id = module_id
        self.port_id = port_id
        self.drop_fcs_errors = PE_FCSDROP(conn, module_id, port_id)
        self.clear = PE_CLEAR(conn, module_id, port_id)
        self.statistics = StatisticsTotals(conn, module_id, port_id)
        self.tpld_mode = PE_TPLDMODE(conn, module_id, port_id)
        
        self.flows: Tuple["CFlow", ...] = tuple()
    
    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> None:
        indices = astuple(await PE_INDICES(self._conn, self.module_id, self.port_id).get())
        self.flows = tuple(
            CFlow(self._conn, self.module_id, self.port_id, idx)
            for idx in indices
        )
