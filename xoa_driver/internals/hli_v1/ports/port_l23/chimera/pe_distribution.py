from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands.enums import ImpairmentTypeIndex
from xoa_driver.internals.commands import (
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


class ImpairmentDistributionConfig:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, impairment_type_index: "ImpairmentTypeIndex") -> None:
        self.enable = PED_ENABLE(conn, module_id, port_id, flow_index, impairment_type_index)
        """Impairment distribution control.

        :type: PED_ENABLE
        """

        self.schedule = PED_SCHEDULE(conn, module_id, port_id, flow_index, impairment_type_index)
        """Impairment scheduling configuration.

        :type: PED_SCHEDULE
        """

        self.one_shot_status = PED_ONESHOTSTATUS(conn, module_id, port_id, flow_index, impairment_type_index)
        """One-shot status.

        :type: PED_ONESHOTSTATUS
        """

        self.off = PED_OFF(conn, module_id, port_id, flow_index, impairment_type_index)
        """Impairments Distribution to OFF.

        :type: PED_OFF
        """

        self.fixed_rate = PED_FIXED(conn, module_id, port_id, flow_index, impairment_type_index)
        """Fixed Rate distribution configuration.

        :type: PED_FIXED
        """

        self.random_rate = PED_RANDOM(conn, module_id, port_id, flow_index, impairment_type_index)
        """Random Rate distribution configuration.

        :type: PED_RANDOM
        """

        self.bit_error_rate = PED_BER(conn, module_id, port_id, flow_index, impairment_type_index)
        """Bit Error Rate distribution configuration.

        :type: PED_BER
        """

        self.random_burst = PED_RANDOMBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Random Burst configuration.

        :type: PED_RANDOMBURST
        """

        self.ge = PED_GE(conn, module_id, port_id, flow_index, impairment_type_index)
        """Gilbert-Elliot distribution configuration.

        :type: PED_GE
        """

        self.uniform = PED_UNI(conn, module_id, port_id, flow_index, impairment_type_index)
        """Uniform distribution configuration.

        :type: PED_UNI
        """

        self.gaussian = PED_GAUSS(conn, module_id, port_id, flow_index, impairment_type_index)
        """Gaussian distribution configuration.

        :type: PED_GAUSS
        """

        self.poisson = PED_POISSON(conn, module_id, port_id, flow_index, impairment_type_index)
        """Poisson distribution configuration.

        :type: PED_POISSON
        """

        self.gamma = PED_GAMMA(conn, module_id, port_id, flow_index, impairment_type_index)
        """Gamma distribution configuration.

        :type: PED_GAMMA
        """

        self.custom = PED_CUST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Associate a custom distribution to a flow and impairment type.

        :type: PED_CUST
        """

        self.constant_delay = PED_CONST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Constant Delay distribution configuration.

        :type: PED_CONST
        """

        self.accumulate_and_burst = PED_ACCBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Accumulate & Burst distribution configuration.

        :type: PED_ACCBURST
        """

        self.step = PED_STEP(conn, module_id, port_id, flow_index, impairment_type_index)
        """Step distribution configuration.

        :type: PED_STEP
        """

        self.fixed_burst = PED_FIXEDBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Fixed Burst distribution configuration.

        :type: PED_FIXEDBURST
        """


class ImpairmentTypeDistribution:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.drop_type_config = ImpairmentDistributionConfig(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DROP)
        """Impairment distribution configuration of impairment type Drop.

        :type: ImpairmentDistributionConfig
        """

        self.misorder_type_config = ImpairmentDistributionConfig(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.MISORDER)
        """Impairment distribution configuration of impairment type Misorder."""

        self.latency_jitter_type_config = ImpairmentDistributionConfig(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.LATENCYJITTER)
        """Impairment distribution configuration of impairment type Delay Jitter."""

        self.duplication_type_config = ImpairmentDistributionConfig(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.DUPLICATION)
        """Impairment distribution configuration of impairment type Duplication.

        :type: ImpairmentDistributionConfig
        """

        self.corruption_type_config = ImpairmentDistributionConfig(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.CORRUPTION)
        """Impairment distribution configuration of impairment type Corruption.

        :type: ImpairmentDistributionConfig
        """

        self.policer_type_config = ImpairmentDistributionConfig(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.POLICER)
        """Impairment distribution configuration of impairment type Policer.

        :type: ImpairmentDistributionConfig
        """

        self.shaper_type_config = ImpairmentDistributionConfig(conn, module_id, port_id, flow_index, ImpairmentTypeIndex.SHAPER)
        """Impairment distribution configuration of impairment type Shaper.

        :type: ImpairmentDistributionConfig
        """
