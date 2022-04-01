import functools
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P_FLASH,
    P_SPEEDSELECTION,
    P_SPEEDS_SUPPORTED,
    P_UAT_MODE,
    P_UAT_FLR,
    P_STATUS,
    P_LPSUPPORT,
    P_TCVRSTATUS,
    P_TXRUNTLENGTH,
    P_RXRUNTLENGTH,
    P_RXRUNTLEN_ERRS,
    P_TXPREAMBLE_REMOVE,
    P_RXPREAMBLE_INSERT,
    P_LOADMODE,

    PP_FECMODE,
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.indices.streams.genuine_stream import GenuineStreamIdx
from xoa_driver.internals.indices.filter.genuine_filter import GenuineFilterIdx
from xoa_driver.internals.indices.port_dataset import PortDatasetIdx

from .port_l23 import (
    BasePortL23,
    Speed,
    TxConfiguration,
)
from .speed_detector import SpeedDetector
from .port_transceiver import PortTransceiver
from .port_capture import PortCapture
from .port_reception_statistics import GenuinePortReceptionStatistics
from .port_transmission_statistics import PortTransmissionStatistics

StreamIndices = idx_mgr.IndexManager[GenuineStreamIdx]
FilterIndices = idx_mgr.IndexManager[GenuineFilterIdx]
PortDatasetIndices = idx_mgr.IndexManager[PortDatasetIdx]


class SpeedMode:
    """Port's speed mode"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.selection = P_SPEEDSELECTION(conn, module_id, port_id)
        self.supported = P_SPEEDS_SUPPORTED(conn, module_id, port_id)

class GenuineSpeed(Speed):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.mode = SpeedMode(conn, module_id, port_id)

class UnAvailableTime:
    """UnAvailable Time"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_UAT_MODE(conn, module_id, port_id)
        self.frame_loss_ratio = P_UAT_FLR(conn, module_id, port_id)


class GenuineTxConfiguration(TxConfiguration):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.runt_length = P_TXRUNTLENGTH(conn, module_id, port_id)
        self.preamble_remove = P_TXPREAMBLE_REMOVE(conn, module_id, port_id)


class GenuineRx:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.runt_length = P_RXRUNTLENGTH(conn, module_id, port_id)
        self.preamble_insert = P_RXPREAMBLE_INSERT(conn, module_id, port_id)
        self.runt_length_errors = P_RXRUNTLEN_ERRS(conn, module_id, port_id)


class PortStatistics:
    """Port statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = GenuinePortReceptionStatistics(conn, module_id, port_id)
        self.tx = PortTransmissionStatistics(conn, module_id, port_id)


class BasePortL23Genuine(BasePortL23):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.flash = P_FLASH(conn, module_id, port_id)
        self.status = P_STATUS(conn, module_id, port_id)
        self.config_load_mode = P_LOADMODE(conn, module_id, port_id)
        self.lp_support = P_LPSUPPORT(conn, module_id, port_id)
        self.tcvr_status = P_TCVRSTATUS(conn, module_id, port_id)
        self.fec_mode = PP_FECMODE(conn, module_id, port_id)

        self.speed = GenuineSpeed(conn, module_id, port_id)
        self.uat = UnAvailableTime(conn, module_id, port_id)
        self.tx_config = GenuineTxConfiguration(conn, module_id, port_id)

        self.transceiver = PortTransceiver(conn, module_id, port_id)
        self.capture = PortCapture(conn, module_id, port_id)
        self.statistics = PortStatistics(conn, module_id, port_id)

        self.streams: StreamIndices = idx_mgr.IndexManager(
            conn,
            GenuineStreamIdx,
            module_id,
            port_id
        )
        self.filters: FilterIndices = idx_mgr.IndexManager(
            conn,
            GenuineFilterIdx,
            module_id,
            port_id
        )
        self.datasets: PortDatasetIndices = idx_mgr.IndexManager(
            conn,
            PortDatasetIdx,
            module_id,
            port_id
        )

    async def _setup(self):
        await super()._setup()
        speed_detector = SpeedDetector(
            self.local_states.capabilities,
            self.local_states.interface
        )
        self.local_states.port_possible_speed_modes = speed_detector.find_port_possible_speed()
        return self

    @property
    def is_brr_mode_supported(self) -> bool:
        return "T1" in self.local_states.interface

    on_speed_selection_change = functools.partialmethod(utils.on_event, P_SPEEDSELECTION)
    """Register a callback to the event that the port's speed mode changes."""

    on_status_change = functools.partialmethod(utils.on_event, P_STATUS)
    """Register a callback to the event that the port's RX signal level (for optical ports) changes."""

    on_lp_support_change = functools.partialmethod(utils.on_event, P_LPSUPPORT)
    """Register a callback to the event that the port's Energy Efficient Ethernet (EEE) status changes."""

    on_uat_mode_change = functools.partialmethod(utils.on_event, P_UAT_MODE)
    """Register a callback to the event that the port's UnAvailable Time mode changes."""

    on_uat_flr_change = functools.partialmethod(utils.on_event, P_UAT_FLR)
    """Register a callback to the event that the port's threshold for the Frame Loss Ratio changes. Used in connection with UnAvailable Time."""

    on_flash_change = functools.partialmethod(utils.on_event, P_FLASH)
    """Register a callback to the event that the port's flash status changes."""
    
    on_tx_runt_length_change = functools.partialmethod(utils.on_event, P_TXRUNTLENGTH)
    """Register a callback to the event that the port's TX runt length setting changes."""

    on_rx_runt_length_change = functools.partialmethod(utils.on_event, P_RXRUNTLENGTH)
    """Register a callback to the event that the port's RX runt length detection changes."""

    on_tx_preamble_remove_change = functools.partialmethod(utils.on_event, P_TXPREAMBLE_REMOVE)
    """Register a callback to the event that the port's preamble removal status changes."""

    on_rx_preamble_insert_change = functools.partialmethod(utils.on_event, P_RXPREAMBLE_INSERT)
    """Register a callback to the event that the port's preamble insertion status changes."""