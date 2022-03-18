from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands.enums import ImpairmentTypeIndex
from xoa_driver.internals.core.commands import (
    PED_SCHEDULE,
    PED_ONESHOTSTATUS,
    PED_OFF,
    PED_FIXED,
    PED_RANDOM,
    PED_BER,
    PED_FIXEDBURST,
    PED_RANDOMBURST,
    PED_GE,
    PED_UNI,
    PED_GAUSS,
    PED_POISSON,
    PED_GAMMA,
    PED_CUST,
    PED_CONST,
    PED_ACCBURST,
    PED_STEP,
    PED_ENABLE,
)

class Impairment:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, impairment_type_index: "ImpairmentTypeIndex") -> None:
        self.enable = PED_ENABLE(conn, module_id, port_id, flow_index, impairment_type_index)
        self.fixed_burst = PED_FIXEDBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        self.schedule = PED_SCHEDULE(conn, module_id, port_id, flow_index, impairment_type_index)
        self.one_shot_status = PED_ONESHOTSTATUS(conn, module_id, port_id, flow_index, impairment_type_index)
        self.off = PED_OFF(conn, module_id, port_id, flow_index, impairment_type_index)
        self.ge = PED_GE(conn, module_id, port_id, flow_index, impairment_type_index)
        self.uniform = PED_UNI(conn, module_id, port_id, flow_index, impairment_type_index)
        self.gausian = PED_GAUSS(conn, module_id, port_id, flow_index, impairment_type_index)
        self.poison = PED_POISSON(conn, module_id, port_id, flow_index, impairment_type_index)
        self.gamma = PED_GAMMA(conn, module_id, port_id, flow_index, impairment_type_index)
        self.custom = PED_CUST(conn, module_id, port_id, flow_index, impairment_type_index)
        self.constant_delay = PED_CONST(conn, module_id, port_id, flow_index, impairment_type_index)
        self.accumulate_and_burst = PED_ACCBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        self.step = PED_STEP(conn, module_id, port_id, flow_index, impairment_type_index)


class PEDistribution:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.fixed = PED_FIXED(conn, module_id, port_id, flow_index)
        self.random = PED_RANDOM(conn, module_id, port_id, flow_index)
        self.bit_error_rate = PED_BER(conn, module_id, port_id, flow_index)
        self.random = PED_RANDOMBURST(conn, module_id, port_id, flow_index)
        
        self.drop_impairment = Impairment(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DROP)
        self.misorder_impairment = Impairment(conn, module_id, port_id, flow_index,ImpairmentTypeIndex.MISORDER)
        self.delayjitter_impairment = Impairment(conn, module_id, port_id, flow_index,ImpairmentTypeIndex.DELAYJITTER)
        self.duplication_impairment = Impairment(conn, module_id, port_id, flow_index,ImpairmentTypeIndex.DUPLICATION)
        self.corruption_impairment = Impairment(conn, module_id, port_id, flow_index,ImpairmentTypeIndex.CORRUPTION)
        self.policer_impairment = Impairment(conn, module_id, port_id, flow_index,ImpairmentTypeIndex.POLICER)
        self.shaper_impairment = Impairment(conn, module_id, port_id, flow_index,ImpairmentTypeIndex.SHAPER)
