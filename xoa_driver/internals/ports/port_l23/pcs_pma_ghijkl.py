from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    PP_ALARMS_ERRORS,
    PP_ALARMS_ERRORS_CLEAR,
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






class PcsPmaAlarms:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.errors = PP_ALARMS_ERRORS(conn, module_id, port_id)
        self.clear = PP_ALARMS_ERRORS_CLEAR(conn, module_id, port_id)

class PcsPmaTransceiver:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_laser_power = PP_TXLASERPOWER(conn, module_id, port_id)
        self.rx_laser_power = PP_RXLASERPOWER(conn, module_id, port_id)


class PcsPmaRxLaneStatus:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.lane_errors = PP_RXLANEERRORS(conn, module_id, port_id, lane_idx)
        self.lock = PP_RXLANELOCK(conn, module_id, port_id, lane_idx)
        self.status = PP_RXLANESTATUS(conn, module_id, port_id, lane_idx)
        self.prbs_status = PP_RXPRBSSTATUS(conn, module_id, port_id, lane_idx)


class PcsPmaTxLaneErrorInjection:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.inject = PP_TXLANEINJECT(conn, module_id, port_id, lane_idx)


class PcsPmaTxErrorGeneration:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.error_rate = PP_TXERRORRATE(conn, module_id, port_id)
        self.inject_one = PP_TXINJECTONE(conn, module_id, port_id)

class PcsPmaTxLaneConfig:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.config = PP_TXLANECONFIG(conn, module_id, port_id, lane_idx)
        self.tx_config = PP_TXPRBSCONFIG(conn, module_id, port_id, lane_idx)

class PcsPmaRx:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.total_status = PP_RXTOTALSTATS(conn, module_id, port_id)
        self.fec_status = PP_RXFECSTATS(conn, module_id, port_id)
        self.clear = PP_RXCLEAR(conn, module_id, port_id)

class PcsPmaPhy:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.auto_neg = PP_PHYAUTONEG(conn, module_id, port_id)
        self.signal_status = PP_PHYSIGNALSTATUS(conn, module_id, port_id)
        self.settings = PP_PHYSETTINGS(conn, module_id, port_id)


class Lane:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.rx_status = PcsPmaRxLaneStatus(conn, module_id, port_id, lane_idx)
        self.tx_error_inject = PcsPmaTxLaneErrorInjection(conn, module_id, port_id, lane_idx)
        self.tx_config = PcsPmaTxLaneConfig(conn, module_id, port_id, lane_idx)

class PcsPma:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self._conn = conn
        self.__port = port
        
        self.alarms = PcsPmaAlarms(conn, *port.kind)
        self.transceiver = PcsPmaTransceiver(conn, *port.kind)
        self.error_gen = PcsPmaTxErrorGeneration(conn, *port.kind)
        self.rx = PcsPmaRx(conn, *port.kind)
        self.phy = PcsPmaPhy(conn, *port.kind)

        self.lanes: Tuple["Lane", ...] = tuple(
            Lane(self._conn, *self.__port.kind, lane_idx=idx) 
            for idx in range(self.__port.info.capabilities.lane_count) # TODO: need to fix, currently port.info.capabilities must be none coz lanes created before awaiting the port
        )

class PRBSConfig:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.type = PP_PRBSTYPE(conn, module_id, port_id)
        self.tx_type = PP_TXPRBSTYPE(conn, module_id, port_id)
        self.rx_type = PP_RXPRBSTYPE(conn, module_id, port_id)

class SDEyeDiagram:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__serdes_index = serdes_xindex
        self.measure = PP_EYEMEASURE(conn, module_id, port_id, serdes_xindex)
        self.resolution = PP_EYERESOLUTION(conn, module_id, port_id, serdes_xindex)
        self.info = PP_EYEINFO(conn, module_id, port_id, serdes_xindex)
        self.ber = PP_EYEBER(conn, module_id, port_id, serdes_xindex)
        self.dwell_bits = PP_EYEDWELLBITS(conn, module_id, port_id, serdes_xindex)
        
    def __await__(self):
        return self._setup().__await__()
    
    async def _setup(self):
        resolution = await self.resolution.get()
        self.read_column = tuple(
            PP_EYEREAD(
                self.__conn, 
                self.__module_id, 
                self.__port_id, 
                self.__serdes_index, 
                colum_xindex=x
            )
            for x in range(resolution.x_resolution)
        )
        return self

class SDPhy:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx_equalizer = PP_PHYTXEQ(conn, module_id, port_id, serdes_xindex)
        self.rx_equalizer = PP_PHYRXEQ(conn, module_id, port_id, serdes_xindex)
        self.retune = PP_PHYRETUNE(conn, module_id, port_id, serdes_xindex)
        self.autotune = PP_PHYAUTOTUNE(conn, module_id, port_id, serdes_xindex)

class SerDes:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.phy = SDPhy(conn, module_id, port_id, serdes_xindex)
        self.eye_diagram = SDEyeDiagram(conn, module_id, port_id, serdes_xindex)
    
    def __await__(self):
        return self._setup().__await__()
    
    async def _setup(self):
        await self.eye_diagram
        return self