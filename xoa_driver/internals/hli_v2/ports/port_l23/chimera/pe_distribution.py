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


class ImpairmentDistribution:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int, impairment_type_index: "ImpairmentTypeIndex") -> None:
        self.off = PED_OFF(conn, module_id, port_id, flow_index, impairment_type_index)
        """Impairments Distribution to OFF.
        Representation of PED_OFF
        """

        self.fixed_rate = PED_FIXED(conn, module_id, port_id, flow_index, impairment_type_index)
        """Fixed Rate distribution configuration.
        Representation of PED_FIXED
        """

        self.random_rate = PED_RANDOM(conn, module_id, port_id, flow_index, impairment_type_index)
        """Random Rate distribution configuration.
        Representation of PED_RANDOM
        """

        self.bit_error_rate = PED_BER(conn, module_id, port_id, flow_index, impairment_type_index)
        """Bit Error Rate distribution configuration.
        Representation of PED_BER
        """

        self.random_burst = PED_RANDOMBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Random Burst configuration.
        Representation of PED_RANDOMBURST
        """

        self.ge = PED_GE(conn, module_id, port_id, flow_index, impairment_type_index)
        """Gilbert-Elliot distribution configuration.
        Representation of PED_GE
        """

        self.uniform = PED_UNI(conn, module_id, port_id, flow_index, impairment_type_index)
        """Uniform distribution configuration.
        Representation of PED_UNI
        """

        self.gaussian = PED_GAUSS(conn, module_id, port_id, flow_index, impairment_type_index)
        """Gaussian distribution configuration.
        Representation of PED_GAUSS
        """

        self.poisson = PED_POISSON(conn, module_id, port_id, flow_index, impairment_type_index)
        """Poisson distribution configuration.
        Representation of PED_POISSON
        """

        self.gamma = PED_GAMMA(conn, module_id, port_id, flow_index, impairment_type_index)
        """Gamma distribution configuration.
        Representation of PED_GAMMA
        """

        self.custom = PED_CUST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Associate a custom distribution to a flow and impairment type.
        Representation of PED_CUST
        """

        self.constant_delay = PED_CONST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Constant Delay distribution configuration.
        Representation of PED_CONST
        """

        self.accumulate_and_burst = PED_ACCBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Accumulate & Burst distribution configuration.
        Representation of PED_ACCBURST
        """

        self.step = PED_STEP(conn, module_id, port_id, flow_index, impairment_type_index)
        """Step distribution configuration.
        Representation of PED_STEP
        """

        self.fixed_burst = PED_FIXEDBURST(conn, module_id, port_id, flow_index, impairment_type_index)
        """Fixed Burst distribution configuration.
        Representation of PED_FIXEDBURST
        """
