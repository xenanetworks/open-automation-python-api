from typing import (
    TYPE_CHECKING,
    Tuple,
)
from xoa_driver.internals.commands.enums import ImpairmentTypeIndex
from xoa_driver.internals.commands.ped_commands import PED_ENABLE, PED_ONESHOTSTATUS, PED_SCHEDULE

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.commands import (
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
from .pe_distribution import ImpairmentDistribution
from .filter_definition import (
    shadow,
    working,
)


class CTotalFlow:
    """Total flow statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.dropped = PE_FLOWDROPTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets dropped in a flow.
        Representation of PE_FLOWDROPTOTAL
        """

        self.delayed = PE_FLOWLATENCYTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets delayed in a flow.
        Representation of PE_FLOWLATENCYTOTAL
        """

        self.duplicated = PE_FLOWDUPTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets duplicate in a flow.
        Representation of PE_FLOWDUPTOTAL
        """

        self.misordered = PE_FLOWMISTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets misordered in a flow.
        Representation of PE_FLOWMISTOTAL
        """

        self.corrupted = PE_FLOWCORTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets corrupted in a flow.
        Representation of PE_FLOWCORTOTAL
        """

        self.jittered = PE_FLOWJITTERTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets jittered in a flow.
        Representation of PE_FLOWJITTERTOTAL
        """


class StatisticsTotals:
    """Total port statistics."""

    def __init__(self, conn, module_id, port_id) -> None:
        self.dropped = PE_DROPTOTAL(conn, module_id, port_id)
        """Statistics of all packets dropped on the port.
        Representation of PE_DROPTOTAL
        """

        self.delayed = PE_LATENCYTOTAL(conn, module_id, port_id)
        """Statistics of all packets delayed on the port.
        Representation of PE_LATENCYTOTAL
        """

        self.duplicated = PE_DUPTOTAL(conn, module_id, port_id)
        """Statistics of all packets duplicated on the port.
        Representation of PE_DUPTOTAL
        """

        self.misordered = PE_MISTOTAL(conn, module_id, port_id)
        """Statistics of all packets mirordered on the port.
        Representation of PE_MISTOTAL
        """

        self.corrupted = PE_CORTOTAL(conn, module_id, port_id)
        """Statistics of all packets corrupted on the port.
        Representation of PE_CORTOTAL
        """

        self.jittered = PE_JITTERTOTAL(conn, module_id, port_id)
        """Statistics of all packets jittered on the port.
        Representation of PE_JITTERTOTAL
        """

        self.fcs_errors = PE_FCSDROP(conn, module_id, port_id)
        """Action on FCS errors.
        Representation of PE_FCSDROP
        """

        self.clear = PE_CLEAR(conn, module_id, port_id)
        """Clear impairment statistics.
        Representation of PE_CLEAR
        """


class CFlowStatistics:
    """Per flow statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.rx = ReceptionStatistics(conn, module_id, port_id, flow_index)
        """RX statistics."""

        self.tx = TransmissionStatistics(conn, module_id, port_id, flow_index)
        """TX statistics."""

        self.total = CTotalFlow(conn, module_id, port_id, flow_index)
        """Total flow statistics."""

        self.clear = PE_FLOWCLEAR(conn, module_id, port_id, flow_index)
        """Clear the impairment statistics on a flow.
        Representation of PE_FLOWCLEAR
        """


class CBandwidth:
    """Bandwidth configuration."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.policer = PE_BANDPOLICER(conn, module_id, port_id, flow_index)
        """Bandwidth policer configuration.
        Representation of PE_BANDPOLICER
        """

        self.shaper = PE_BANDSHAPER(conn, module_id, port_id, flow_index)
        """Bandwidth shaper configuration.
        Representation of PE_BANDSHAPER
        """


class ChimeraPE:
    """Port Emulation"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self._conn = conn
        self.module_id = module_id
        self.port_id = port_id
        self.drop_fcs_errors = PE_FCSDROP(conn, module_id, port_id)
        """Action on FCS errors.
        Representation of PE_FCSDROP
        """

        self.clear = PE_CLEAR(conn, module_id, port_id)
        """Clear impairment statistics.
        Representation of PE_CLEAR
        """

        self.statistics = StatisticsTotals(conn, module_id, port_id)
        """Total port statistics."""

        self.tpld_mode = PE_TPLDMODE(conn, module_id, port_id)
        """TPLD mode.
        Representation of PE_TPLDMODE
        """

        self.flow: Tuple["CFlow", ...] = tuple()

    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> None:
        indices = await PE_INDICES(self._conn, self.module_id, self.port_id).get()
        self.flow = tuple(
            CFlow(self._conn, self.module_id, self.port_id, idx)
            for idx in indices.to_tuple()
        )


class CTotalFlowStats:
    """Total flow statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.dropped = PE_FLOWDROPTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets dropped in a flow.
        Representation of PE_FLOWDROPTOTAL
        """

        self.delayed = PE_FLOWLATENCYTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets delayed in a flow.
        Representation of PE_FLOWLATENCYTOTAL
        """

        self.duplicated = PE_FLOWDUPTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets duplicate in a flow.
        Representation of PE_FLOWDUPTOTAL
        """

        self.misordered = PE_FLOWMISTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets misordered in a flow.
        Representation of PE_FLOWMISTOTAL
        """

        self.corrupted = PE_FLOWCORTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets corrupted in a flow.
        Representation of PE_FLOWCORTOTAL
        """

        self.jittered = PE_FLOWJITTERTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets jittered in a flow.
        Representation of PE_FLOWJITTERTOTAL
        """


class CPerFlowStats:
    """Per flow statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.rx = ReceptionStatistics(conn, module_id, port_id, flow_index)
        """RX statistics."""

        self.tx = TransmissionStatistics(conn, module_id, port_id, flow_index)
        """TX statistics."""

        self.total = CTotalFlowStats(conn, module_id, port_id, flow_index)
        """Total flow statistics."""

        self.clear = PE_FLOWCLEAR(conn, module_id, port_id, flow_index)
        """Clear the impairment statistics on a flow.
        Representation of PE_FLOWCLEAR
        """


class CDropImpairment:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.distribution = ImpairmentDistribution(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DROP)

        self.schedule = PED_SCHEDULE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DROP)
        """Impairment scheduling configuration.
        Representation of PED_SCHEDULE
        """

        self.one_shot_status = PED_ONESHOTSTATUS(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DROP)
        """One-shot status.
        Representation of PED_ONESHOTSTATUS
        """

        self.enable = PED_ENABLE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DROP)
        """Impairment distribution control.
        Representation of PED_ENABLE
        """


class CCorruptionImpairment:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:

        self.type = PE_CORRUPT(conn, module_id, port_id, flow_index)
        """Bandwidth policer configuration.
        Representation of PE_BANDPOLICER
        """

        self.distribution = ImpairmentDistribution(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.CORRUPTION)

        self.schedule = PED_SCHEDULE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.CORRUPTION)
        """Impairment scheduling configuration.
        Representation of PED_SCHEDULE
        """

        self.one_shot_status = PED_ONESHOTSTATUS(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.CORRUPTION)
        """One-shot status.
        Representation of PED_ONESHOTSTATUS
        """

        self.enable = PED_ENABLE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.CORRUPTION)
        """Impairment distribution control.
        Representation of PED_ENABLE
        """


class CMisorderingImpairment:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.depth = PE_MISORDER(conn, module_id, port_id, flow_index)
        """Misordering depth
        Representation of PE_MISORDER
        """

        self.distribution = ImpairmentDistribution(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.MISORDER)

        self.schedule = PED_SCHEDULE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.MISORDER)
        """Impairment scheduling configuration.
        Representation of PED_SCHEDULE
        """

        self.one_shot_status = PED_ONESHOTSTATUS(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.MISORDER)
        """One-shot status.
        Representation of PED_ONESHOTSTATUS
        """

        self.enable = PED_ENABLE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.MISORDER)
        """Impairment distribution control.
        Representation of PED_ENABLE
        """


class CLatencyJitterImpairment:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:

        self.range = PE_LATENCYRANGE(conn, module_id, port_id, flow_index)
        """Flow latency range.
        Representation of PE_LATENCYRANGE
        """

        self.distribution = ImpairmentDistribution(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.LATENCYJITTER)

        self.schedule = PED_SCHEDULE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.LATENCYJITTER)
        """Impairment scheduling configuration.
        Representation of PED_SCHEDULE
        """

        self.one_shot_status = PED_ONESHOTSTATUS(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.LATENCYJITTER)
        """One-shot status.
        Representation of PED_ONESHOTSTATUS
        """

        self.enable = PED_ENABLE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.LATENCYJITTER)
        """Impairment distribution control.
        Representation of PED_ENABLE
        """


class CDuplicationImpairment:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:

        self.distribution = ImpairmentDistribution(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DUPLICATION)

        self.schedule = PED_SCHEDULE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DUPLICATION)
        """Impairment scheduling configuration.
        Representation of PED_SCHEDULE
        """

        self.one_shot_status = PED_ONESHOTSTATUS(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DUPLICATION)
        """One-shot status.
        Representation of PED_ONESHOTSTATUS
        """

        self.enable = PED_ENABLE(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DUPLICATION)
        """Impairment distribution control.
        Representation of PED_ENABLE
        """


class CShaperImpairment:
    """Bandwidth shaper impairment configuration."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.config = PE_BANDSHAPER(conn, module_id, port_id, flow_index)
        """Bandwidth shaper configuration.
        Representation of PE_BANDSHAPER
        """


class CPolicerImpairment:
    """Bandwidth policer impairment configuration."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.config = PE_BANDPOLICER(conn, module_id, port_id, flow_index)
        """Bandwidth policer configuration.
        Representation of PE_BANDPOLICER
        """


class CFlow:
    """Flow settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.comment = PE_COMMENT(conn, module_id, port_id, flow_index)
        """Flow description.
        Representation of PE_COMMENT
        """

        self.statistics = CPerFlowStats(conn, module_id, port_id, flow_index)
        """Flow statistics."""

        self.shadow_filter = shadow.FilterDefinitionShadow(conn, module_id, port_id, flow_index)
        """Shadow copy."""

        self.working_filter = working.FilterDefinitionWorking(conn, module_id, port_id, flow_index)
        """Working copy."""

        self.drop = CDropImpairment(conn, module_id, port_id, flow_index)

        self.misordering = CMisorderingImpairment(conn, module_id, port_id, flow_index)

        self.latency_jitter = CLatencyJitterImpairment(conn, module_id, port_id, flow_index)

        self.duplication = CDuplicationImpairment(conn, module_id, port_id, flow_index)

        self.corruption = CCorruptionImpairment(conn, module_id, port_id, flow_index)

        self.policer = CPolicerImpairment(conn, module_id, port_id, flow_index)

        self.shaper = CShaperImpairment(conn, module_id, port_id, flow_index)
