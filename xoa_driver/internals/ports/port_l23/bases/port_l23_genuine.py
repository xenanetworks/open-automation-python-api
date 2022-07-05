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
from .port_reception_statistics import GenuinePortReceptionStatistics
from .port_transmission_statistics import PortTransmissionStatistics

StreamIndices = idx_mgr.IndexManager[GenuineStreamIdx]
FilterIndices = idx_mgr.IndexManager[GenuineFilterIdx]
PortDatasetIndices = idx_mgr.IndexManager[PortDatasetIdx]


class SpeedMode:
    """L23 port's speed mode"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.selection = P_SPEEDSELECTION(conn, module_id, port_id)
        """L23 port speed mode selection.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_SPEEDSELECTION`
        """
        self.supported = P_SPEEDS_SUPPORTED(conn, module_id, port_id)
        """L23 port's supported speed modes.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_SPEEDS_SUPPORTED`
        """

class GenuineSpeed(Speed):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.mode = SpeedMode(conn, module_id, port_id)
        """L23 port's speed mode."""

class UnAvailableTime:
    """UnAvailable Time"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_UAT_MODE(conn, module_id, port_id)
        """L23 port's Unvailable Time mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_UAT_MODE`
        """
        self.frame_loss_ratio = P_UAT_FLR(conn, module_id, port_id)
        """L23 port's Frame Loss Ratio for UAT.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_UAT_FLR`
        """


class GenuineTxConfiguration(TxConfiguration):
    """L23 port's TX configuration."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.runt_length = P_TXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's TX runt length.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXRUNTLENGTH`
        """
        self.preamble_remove = P_TXPREAMBLE_REMOVE(conn, module_id, port_id)
        """L23 port's removal of preamble from outgoing packets.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXPREAMBLE_REMOVE`
        """


class GenuineRx:
    """L23 port's RX configuration."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.runt_length = P_RXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's RX runt length.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RXRUNTLENGTH`
        """
        self.preamble_insert = P_RXPREAMBLE_INSERT(conn, module_id, port_id)
        """L23 port's insertion of preamble into incoming packets.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RXPREAMBLE_INSERT`
        """
        self.runt_length_errors = P_RXRUNTLEN_ERRS(conn, module_id, port_id)
        """L23 port's RX runt length errors..
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RXRUNTLEN_ERRS`
        """


class PortStatistics:
    """L23 port statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = GenuinePortReceptionStatistics(conn, module_id, port_id)
        """L23 port's RX statistics."""
        self.tx = PortTransmissionStatistics(conn, module_id, port_id)
        """L23 port's TX statistics."""


class BasePortL23Genuine(BasePortL23):
    """L23 port basic configuration."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.flash = P_FLASH(conn, module_id, port_id)
        """L23 port flashes.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_FLASH`
        """
        self.status = P_STATUS(conn, module_id, port_id)
        """L23 port's received optical signal level'.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_STATUS`
        """
        self.config_load_mode = P_LOADMODE(conn, module_id, port_id)
        """Chimera Port loading mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LOADMODE`
        """
        self.lp_support = P_LPSUPPORT(conn, module_id, port_id)
        """L23 port EEE capabilities.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LPSUPPORT`
        """
        self.tcvr_status = P_TCVRSTATUS(conn, module_id, port_id)
        """L23 port transceiver status information.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TCVRSTATUS`
        """
        self.fec_mode = PP_FECMODE(conn, module_id, port_id)
        """L23 port FEC mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.PP_FECMODE`
        """

        self.speed = GenuineSpeed(conn, module_id, port_id)
        """L23 port speed configuration.
        """
        self.uat = UnAvailableTime(conn, module_id, port_id)
        """L23 port UnAvailable Time configuration.
        """
        self.tx_config = GenuineTxConfiguration(conn, module_id, port_id)
        """L23 port TX configuration.
        """

        self.transceiver = PortTransceiver(conn, module_id, port_id)
        """L23 port transceiver configuration.
        """
    
        self.statistics = PortStatistics(conn, module_id, port_id)
        """L23 port statistics.
        """

        self.streams: StreamIndices = idx_mgr.IndexManager(
            conn,
            GenuineStreamIdx,
            module_id,
            port_id
        )
        """L23 port stream index manager.
        """
        self.filters: FilterIndices = idx_mgr.IndexManager(
            conn,
            GenuineFilterIdx,
            module_id,
            port_id
        )
        """L23 port filter index manager.
        """
        self.datasets: PortDatasetIndices = idx_mgr.IndexManager(
            conn,
            PortDatasetIdx,
            module_id,
            port_id
        )
        """L23 port histogram index manager.
        """

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
        """Whether this L23 port supports BRR mode.

        :return: whether this port supports BRR mode.
        :rtype: bool
        """
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