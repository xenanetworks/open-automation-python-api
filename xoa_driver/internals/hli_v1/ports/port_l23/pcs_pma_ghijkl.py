from typing import (
    TYPE_CHECKING,
    Tuple,
)
from typing_extensions import Self
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_ALARMS_ERRORS,
    PP_TXLANECONFIG,
    PP_TXLANEINJECT,
    PP_TXPRBSCONFIG,
    PP_TXERRORRATE,
    PP_TXINJECTONE,
    PP_RXTOTALSTATS,
    PP_RXFECSTATS,
    PP_RXLANELOCK,
    PP_RXLANESTATUS,
    PP_RXLANEERRORS,
    PP_RXPRBSSTATUS,
    PP_RXCLEAR,
    PP_RXLASERPOWER,
    PP_TXLASERPOWER,
    PP_EYEMEASURE,
    PP_EYERESOLUTION,
    PP_EYEREAD,
    PP_EYEINFO,
    PP_PHYTXEQ,
    PP_PHYRETUNE,
    PP_PHYAUTOTUNE,
    PP_EYEBER,
    PP_PHYAUTONEG,
    PP_TXPRBSTYPE,
    PP_RXPRBSTYPE,
    # PP_FECMODE, # moved to all genuine ports
    PP_EYEDWELLBITS,
    PP_PHYSIGNALSTATUS,
    PP_PRBSTYPE,
    PP_PHYSETTINGS,
    PP_PHYRXEQ,
)
from xoa_driver import enums


class PcsPmaAlarms:
    """L23 high-speed port PCS/PMA alarms"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.errors = PP_ALARMS_ERRORS(conn, module_id, port_id)
        """Error count of each alarm on a L23 high-speed port.

        :type: PP_ALARMS_ERRORS
        """


class PcsPmaTransceiver:
    """L23 high-speed port PCS/PMA transceivers"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_laser_power = PP_TXLASERPOWER(conn, module_id, port_id)
        """Power of TX laser.

        :type: PP_TXLASERPOWER
        """

        self.rx_laser_power = PP_RXLASERPOWER(conn, module_id, port_id)
        """Power of RX laser.

        :type: PP_RXLASERPOWER
        """


class PcsPmaRxLaneStatus:
    """L23 high-speed port PCS/PMA lane status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.errors = PP_RXLANEERRORS(conn, module_id, port_id, lane_idx)
        """RX lane error statistics.

        :type: PP_RXLANEERRORS
        """

        self.lock = PP_RXLANELOCK(conn, module_id, port_id, lane_idx)
        """RX lane lock.

        :type: PP_RXLANELOCK
        """

        self.status = PP_RXLANESTATUS(conn, module_id, port_id, lane_idx)
        """RX lane status

        :type: PP_RXLANESTATUS
        """


class PcsPmaTxErrorGeneration:
    """L23 high-speed port PCS/PMA TX error generation."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.error_rate = PP_TXERRORRATE(conn, module_id, port_id)
        """The rate of continuous bit-level error injection.

        :type: PP_TXERRORRATE
        """

        self.inject_one = PP_TXINJECTONE(conn, module_id, port_id)
        """Inject a single bit-level error.

        :type: PP_TXINJECTONE
        """


class PcsPmaRx:
    """L23 high-speed port PCS/PMA RX"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.total_status = PP_RXTOTALSTATS(conn, module_id, port_id)
        """RX FEC total counters.

        :type: PP_RXTOTALSTATS
        """

        self.fec_status = PP_RXFECSTATS(conn, module_id, port_id)
        """RX FEC statistics.

        :type: PP_RXFECSTATS
        """

        self.clear = PP_RXCLEAR(conn, module_id, port_id)
        """Clear all the PCS/PMA receiver statistics.

        :type: PP_RXCLEAR
        """


class PcsPmaPhy:
    """L23 high-speed port PCS/PMA PHY settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.auto_neg = PP_PHYAUTONEG(conn, module_id, port_id)
        """ Auto-negotiation settings of the PHY.

        :type: PP_PHYAUTONEG
        """

        self.signal_status = PP_PHYSIGNALSTATUS(conn, module_id, port_id)
        """The PHY signal status.

        :type: PP_PHYSIGNALSTATUS
        """

        self.settings = PP_PHYSETTINGS(conn, module_id, port_id)
        """Low-level PHY settings

        :type: PP_PHYSETTINGS
        """


class Lane:
    """L23 high-speed port lane configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.rx_status = PcsPmaRxLaneStatus(conn, module_id, port_id, lane_idx)
        """PCS/PMA RX lane status.
        """

        self.tx_error_inject = PP_TXLANEINJECT(conn, module_id, port_id, lane_idx)
        """Inject CAUI error into a TX lane.

        :type: PP_TXLANEINJECT
        """

        self.tx_config = PP_TXLANECONFIG(conn, module_id, port_id, lane_idx)
        """TX lane configuration.

        :type: PP_TXLANECONFIG
        """


class PcsPma:
    """L23 high-speed port PCS/PMA"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self._conn = conn
        self.__port = port

        self.alarms = PcsPmaAlarms(conn, *port.kind)
        """PCS/PMA alarms

        :type: PcsPmaAlarms
        """

        self.transceiver = PcsPmaTransceiver(conn, *port.kind)
        """PCS/PMA transceiver

        :type: PcsPmaTransceiver
        """

        self.error_gen = PcsPmaTxErrorGeneration(conn, *port.kind)
        """PCS/PMA error generation

        :type: PcsPmaTxErrorGeneration
        """

        self.rx = PcsPmaRx(conn, *port.kind)
        """PCS/PMA RX

        :type: PcsPmaRx
        """

        self.phy = PcsPmaPhy(conn, *port.kind)
        """PCS/PMA PHY

        :type: PcsPmaPhy
        """

        self.prbs_config = PRBSConfig(conn, *port.kind)
        """PCS/PMA PRBS Configuration
        
        :type: PRBSConfig
        """

        self.lanes: Tuple["Lane", ...] = tuple(
            Lane(self._conn, *self.__port.kind, lane_idx=idx)
            for idx in range(self.__port.info.capabilities.lane_count)
        )  # TODO: need to fix, currently port.info.capabilities must be none because lanes are created before awaiting the port


class PRBSConfig:
    """L23 high-speed port PRBS configuration."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.type = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS type used when in PRBS mode.

        :type: PP_PRBSTYPE
        """


class SDEyeDiagram:
    """L23 high-speed port SerDes eye diagram."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__serdes_index = serdes_xindex
        self.measure = PP_EYEMEASURE(conn, module_id, port_id, serdes_xindex)
        """BER eye measurement.

        :type: PP_EYEMEASURE
        """

        self.resolution = PP_EYERESOLUTION(conn, module_id, port_id, serdes_xindex)
        """Resolution for BER eye measurement.

        :type: PP_EYERESOLUTION
        """

        self.info = PP_EYEINFO(conn, module_id, port_id, serdes_xindex)
        """Information of BER eye measurement.

        :type: PP_EYEINFO
        """

        self.ber = PP_EYEBER(conn, module_id, port_id, serdes_xindex)
        """BER estimation of an eye diagram.

        :type: PP_EYEBER
        """

        self.dwell_bits = PP_EYEDWELLBITS(conn, module_id, port_id, serdes_xindex)
        """Dwell bits for an eye capture.

        :type: PP_EYEDWELLBITS
        """

    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> Self:
        resolution = await self.resolution.get()
        self.read_column = tuple(
            PP_EYEREAD(
                self.__conn,
                self.__module_id,
                self.__port_id,
                self.__serdes_index,
                _colum_xindex=x
            )
            for x in range(resolution.x_resolution)
        )
        return self


class SDPhy:
    """L23 high-speed port SerDes PHY configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx_equalizer = PP_PHYTXEQ(conn, module_id, port_id, serdes_xindex)
        """Equalizer settings of the on-board PHY in the TX direction.

        :type: PP_PHYTXEQ
        """

        self.rx_equalizer = PP_PHYRXEQ(conn, module_id, port_id, serdes_xindex)
        """Equalizer settings of the on-board PHY in the RX direction.

        :type: PP_PHYRXEQ
        """

        self.retune = PP_PHYRETUNE(conn, module_id, port_id, serdes_xindex)
        """Retuning of the PHY.

        :type: PP_PHYRETUNE
        """

        self.autotune = PP_PHYAUTOTUNE(conn, module_id, port_id, serdes_xindex)
        """Autotune of the PHY.

        :type: PP_PHYAUTOTUNE
        """

class Prbs:
    """L23 high-speed port SerDes PRBS configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx_config = PP_TXPRBSCONFIG(conn, module_id, port_id, serdes_xindex)
        """TX PRBS configuration of a SerDes.

        :type: PP_TXPRBSCONFIG
        """

        self.status = PP_RXPRBSSTATUS(conn, module_id, port_id, serdes_xindex)
        """RX PRBS status on a SerDes

        :type: PP_RXPRBSSTATUS
        """



class SerDes:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS configuration

        :type: Prbs
        """

        self.phy = SDPhy(conn, module_id, port_id, serdes_xindex)
        """PHY configuration

        :type: SDPhy
        """

        self.eye_diagram = SDEyeDiagram(conn, module_id, port_id, serdes_xindex)
        """Eye diagram

        :type: SDEyeDiagram
        """

    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> Self:
        await self.eye_diagram
        return self
