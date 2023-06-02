import functools
from typing import TYPE_CHECKING
from typing_extensions import Self

from xoa_driver.internals.commands import (
    P4_TRAFFIC,
    P4_STATE,
    P4_CAPABILITIES,
    P4_STATE_STATUS,
    P4_VLAN_OFFLOAD,
    P4_ARP_CONFIG,
    P4_NDP_CONFIG,
    P4_CAPTURE,
    P4_CAPTURE_GET_FIRST,
    P4_CAPTURE_GET_NEXT,
    P4_TX_PACKET_SIZE,
    P4_RX_PACKET_SIZE,
    P4_TX_MTU,
    P4_RX_MTU,
    P4_CLEAR,
    P4_SPEEDSELECTION,
    P4_MAX_PACKET_RATE,
    P4_PCI_INFO,
    P4_FW_VER,
    P4_DEV_NAME,
    P4_PORT_TYPE,
    P4_LICENSE_INFO,
    P4_APTITUDES,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.hli_v1.ports import base_port
from xoa_driver.internals.state_storage import ports_state
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as im
from xoa_driver.internals.hli_v1.indices.connection_group.cg import ConnectionGroupIdx

from .counters import PCounters
from .packet_engine import PacketEngine


class PCapture:
    """Packet capture
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.start = P4_CAPTURE(conn, module_id, port_id)
        """Control L47 packet capture.

        :type: P4_CAPTURE
        """

        self.get_first_frame = P4_CAPTURE_GET_FIRST(conn, module_id, port_id)
        """Get the first captured packet.

        :type: P4_CAPTURE_GET_FIRST
        """

        self.get_next_frame = P4_CAPTURE_GET_NEXT(conn, module_id, port_id)
        """Get the next captured packet.

        :type: P4_CAPTURE_GET_NEXT
        """


class PortL47(base_port.BasePort["ports_state.PortL47LocalState"]):
    """L47 Port"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

        self._local_states = ports_state.PortL47LocalState()

        self.traffic = P4_TRAFFIC(self._conn, module_id, port_id)
        """
        Control L47 traffic.

        :type: P4_TRAFFIC
        """

        self.clear = P4_CLEAR(self._conn, module_id, port_id)
        """
        Clear all the connection groups on the port and set the port state to OFF.

        :type: P4_CLEAR
        """

        self.state = P4_STATE(self._conn, module_id, port_id)
        """
        :type: P4_STATE
        """

        self.type = P4_PORT_TYPE(self._conn, module_id, port_id)
        """
        :type: P4_PORT_TYPE
        """

        self.aptitudes = P4_APTITUDES(self._conn, module_id, port_id)
        """
        :type: P4_APTITUDES
        """

        self.last_state_status = P4_STATE_STATUS(self._conn, module_id, port_id)
        """
        :type: P4_STATE_STATUS
        """

        self.nic_name = P4_DEV_NAME(self._conn, module_id, port_id)
        """
        :type: P4_DEV_NAME
        """

        self.nic_firmware_version = P4_FW_VER(self._conn, module_id, port_id)
        """
        :type: P4_FW_VER
        """

        self.vlan_offload = P4_VLAN_OFFLOAD(self._conn, module_id, port_id)
        """
        :type: P4_VLAN_OFFLOAD
        """

        self.max_packet_rate = P4_MAX_PACKET_RATE(self._conn, module_id, port_id)
        """
        :type: P4_MAX_PACKET_RATE
        """

        self.capabilities = P4_CAPABILITIES(self._conn, module_id, port_id)
        """
        :type: P4_CAPABILITIES
        """

        self.speed_selection = P4_SPEEDSELECTION(self._conn, module_id, port_id)
        """
        :type: P4_SPEEDSELECTION
        """

        # region Not sure if this commands must be at this level
        self.tx_packet_size = P4_TX_PACKET_SIZE(self._conn, module_id, port_id)
        """
        :type: P4_TX_PACKET_SIZE
        """

        self.rx_packet_size = P4_RX_PACKET_SIZE(self._conn, module_id, port_id)
        """
        :type: P4_RX_PACKET_SIZE
        """

        self.tx_mtu = P4_TX_MTU(self._conn, module_id, port_id)
        """
        :type: P4_TX_MTU
        """

        self.rx_mtu = P4_RX_MTU(self._conn, module_id, port_id)
        """
        :type: P4_RX_MTU
        """
        # endregion

        self.pci_info = P4_PCI_INFO(self._conn, module_id, port_id)
        """
        :type: P4_PCI_INFO
        """

        self.license_info = P4_LICENSE_INFO(self._conn, module_id, port_id)
        """
        :type: P4_LICENSE_INFO
        """

        self.arp_config = P4_ARP_CONFIG(self._conn, module_id, port_id)
        """
        :type: P4_ARP_CONFIG
        """

        self.ndp_config = P4_NDP_CONFIG(self._conn, module_id, port_id)
        """
        :type: P4_NDP_CONFIG
        """

        self.capture = PCapture(self._conn, module_id, port_id)
        """L47 packet capture
        
        :type: PCapture
        """

        self.counters = PCounters(self._conn, module_id, port_id)
        """L47 counters
        
        :type: PCounters
        """

        self.packet_engine = PacketEngine(self._conn, module_id, port_id)
        """L47 packet engine.
        
        :type: ~xoa_driver.internals.hli_v1.ports.port_l47.packet_engine.PacketEngine
        """

        self.connection_groups: "im.IndexManager[ConnectionGroupIdx]" = im.IndexManager(
            self._conn,
            ConnectionGroupIdx,
            module_id,
            port_id
        )
        """L47 connection group index manager.
        
        :type: IndexManager
        """

    @property
    def info(self) -> ports_state.PortL47LocalState:
        return self._local_states

    async def _setup(self) -> Self:
        await self._local_states.initiate(self)
        self._local_states.register_subscriptions(self)
        return self

    on_capabilities_change = functools.partialmethod(utils.on_event, P4_CAPABILITIES)
    """Register a callback to the event that the L47 port's capabilities change."""

    on_speed_selection_change = functools.partialmethod(utils.on_event, P4_SPEEDSELECTION)
    """Register a callback to the event that the L47 port's speed mode changes."""

    on_state_change = functools.partialmethod(utils.on_event, P4_STATE)
    """Register a callback to the event that the L47 port's state changes."""
    
    on_license_info_change = functools.partialmethod(utils.on_event, P4_LICENSE_INFO)
    """Register a callback to the event that the L47 port's license information changes."""
