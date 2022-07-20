import functools
import typing
from xoa_driver.internals.ports import base_port
from xoa_driver.internals.core.commands import (
    P_CAPABILITIES,
    P_SPEED,
    P_SPEEDREDUCTION,
    P_INTERFRAMEGAP,
    P_MACADDRESS,
    P_IPADDRESS,
    P_ARPREPLY,
    P_PINGREPLY,
    P_PAUSE,
    P_RANDOMSEED,
    P_LOOPBACK,
    P_TRAFFIC,
    P_CAPTURE,
    P_XMITONE,
    P_LATENCYOFFSET,
    P_LATENCYMODE,
    P_AUTOTRAIN,
    P_MIXWEIGHTS,
    P_TRAFFICERR,
    P_GAPMONITOR,
    P_CHECKSUM,
    P_MIXLENGTH,
    P_ARPRXTABLE,
    P_NDPRXTABLE,
    P_MULTICAST,
    P_MULTICASTEXT,
    P_MCSRCLIST,
    P_MULTICASTHDR,
    P_TXMODE,
    P_RATEFRACTION,
    P_RATEPPS,
    P_RATEL2BPS,
    P_PAYLOADMODE,
    P_TXENABLE,
    P_MAXHEADERLENGTH,
    P_TXTIMELIMIT,
    P_TXTIME,
    P_XMITONETIME,
    P_IPV6ADDRESS,
    P_ARPV6REPLY,
    P_PINGV6REPLY,
    P_ERRORS,
    P_TXPREPARE,
    P_TXDELAY,
    P_TPLDMODE,
    P_TXPACKETLIMIT,
    P_PFCENABLE,
    P_TXBURSTPERIOD,
)
if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.core.transporter import funcs
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.state_storage import ports_state
from xoa_driver.internals.indices.length_term import LengthTermIdx
from xoa_driver.internals.indices.match_term import MatchTermIdx

from .port_capture import PortCapture

LengthTermIndices = idx_mgr.IndexManager[LengthTermIdx]
MatchTermIndices = idx_mgr.IndexManager[MatchTermIdx]

class TxSinglePacket:
    """L23 port single-packet transmission"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.send = P_XMITONE(conn, module_id, port_id)
        """Send one packet from the L23 port without a stream config.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_XMITONE`
        """
        self.time = P_XMITONETIME(conn, module_id, port_id)
        """The time at which the latest packet was transmitted using the :class:`~xoa_driver.internals.core.commands.p_commands.P_XMITONE` command.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_XMITONETIME`
        """


class TxConfiguration:
    """L23 port TX configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_TXMODE(conn, module_id, port_id)
        """L23 port TX mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXMODE`
        """
        self.enable = P_TXENABLE(conn, module_id, port_id)
        """Enabling L23 port TX.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXENABLE`
        """
        self.time_limit = P_TXTIMELIMIT(conn, module_id, port_id)
        """L23 port TX time limit.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXTIMELIMIT`
        """
        self.time = P_TXTIME(conn, module_id, port_id)
        """L23 port TX time.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXTIME`
        """
        self.repare = P_TXPREPARE(conn, module_id, port_id)
        """Prepare L23 port for transmission.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXPREPARE`
        """
        self.delay = P_TXDELAY(conn, module_id, port_id)
        """L23 port TX delay.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXDELAY`
        """
        self.packet_limit = P_TXPACKETLIMIT(conn, module_id, port_id)
        """L23 port TX packet limit
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXPACKETLIMIT`
        """
        self.burst_period = P_TXBURSTPERIOD(conn, module_id, port_id)
        """L23 port TX burst period.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TXBURSTPERIOD`
        """


class Rate:
    """L23 port TX rate"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.fraction = P_RATEFRACTION(conn, module_id, port_id)
        """L23 port rate in ppm.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RATEFRACTION`
        """
        self.pps = P_RATEPPS(conn, module_id, port_id)
        """L23 port rate in packets per second.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RATEPPS`
        """
        self.l2_bps = P_RATEL2BPS(conn, module_id, port_id)
        """L23 port rate in L2 bits per second.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RATEL2BPS`
        """


class Multicast:
    """L23 port multicast configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_MULTICAST(conn, module_id, port_id)
        """L23 port multicast mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MULTICAST`
        """
        self.mode_extended = P_MULTICASTEXT(conn, module_id, port_id)
        """L23 port multicast extended mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MULTICASTEXT`
        """
        self.source_list = P_MCSRCLIST(conn, module_id, port_id)
        """L23 port multicast source list.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MCSRCLIST`
        """
        self.header = P_MULTICASTHDR(conn, module_id, port_id)
        """L23 port multicast IGMP header.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MULTICASTHDR`
        """


class IPv4:
    """L23 port IPv4 configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPADDRESS(conn, module_id, port_id)
        """L23 port IPv4 address.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_IPADDRESS`
        """
        self.arp_reply = P_ARPREPLY(conn, module_id, port_id)
        """L23 port reply to ARP request.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_ARPREPLY`
        """
        self.ping_reply = P_PINGREPLY(conn, module_id, port_id)
        """L23 port reply to PING request.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_PINGREPLY`
        """


class IPv6:
    """L23 port IPv6 configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPV6ADDRESS(conn, module_id, port_id)
        """L23 port IPv6 address.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_IPV6ADDRESS`
        """
        self.arp_reply = P_ARPV6REPLY(conn, module_id, port_id)
        """L23 port reply to NDP Neighbor Solicitation.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_ARPV6REPLY`
        """
        self.ping_reply = P_PINGV6REPLY(conn, module_id, port_id)
        """L23 port reply to PINGv6 request.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_PINGV6REPLY`
        """


class NetworkConfiguration: # will be extended in genuine ports
    """L23 port networking configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mac_address = P_MACADDRESS(conn, module_id, port_id)
        """L23 port MAC address.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MACADDRESS`
        """
        self.ipv4 = IPv4(conn, module_id, port_id)
        """L23 port IPv4 address configuration.
        """
        self.ipv6 = IPv6(conn, module_id, port_id)
        """L23 port IPv6 address configuration.
        """


class LatencyConfiguration:
    """L23 port latency configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.offset = P_LATENCYOFFSET(conn, module_id, port_id)
        """L23 port latency offset.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LATENCYOFFSET`
        """
        self.mode = P_LATENCYMODE(conn, module_id, port_id)
        """L23 port latency measurement mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LATENCYMODE`
        """

class Mix:
    """L23 port IMIX configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.weights = P_MIXWEIGHTS(conn, module_id, port_id)
        """L23 port IMIX weights
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MIXWEIGHTS`
        """
        self.lengths = tuple(
            P_MIXLENGTH(conn, module_id, port_id, idx)
            for idx in range(16)
        ) # TODO: need to add manager for handle specific indices only
        """L23 port IMIX lengths.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MIXLENGTH`
        """

class Speed:
    """L23 port speed configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.current = P_SPEED(conn, module_id, port_id)
        """L23 port current speed in units of Mbps.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_SPEED`
        """
        self.reduction = P_SPEEDREDUCTION(conn, module_id, port_id)
        """L23 port speed reduction in ppm.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_SPEEDREDUCTION`
        """

class Traffic:
    """L23 port traffic generation"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.state = P_TRAFFIC(conn, module_id, port_id)
        """L23 port traffic status and action.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TRAFFIC`
        """
        self.error = P_TRAFFICERR(conn, module_id, port_id)
        """L23 port traffic error.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TRAFFICERR`
        """

class BasePortL23(base_port.BasePort[ports_state.PortL23LocalState]):
    """L23 port layout which is relevant to all L23 ports."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        """L23 port capabilities.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_CAPABILITIES`
        """
        self.pause = P_PAUSE(conn, module_id, port_id)
        """L23 port response to Ethernet PAUSE frames.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_PAUSE`
        """
        self.loop_back = P_LOOPBACK(conn, module_id, port_id)
        """L23 port loopback mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_LOOPBACK`
        """
        
        self.errors_count = P_ERRORS(conn, module_id, port_id)
        """L23 port errors.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_ERRORS`
        """

        self.interframe_gap = P_INTERFRAMEGAP(conn, module_id, port_id)
        """L23 port interframe gap.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_INTERFRAMEGAP`
        """
        self.max_header_length = P_MAXHEADERLENGTH(conn, module_id, port_id)
        """L23 port maximum header length.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_MAXHEADERLENGTH`
        """
        self.tpld_mode = P_TPLDMODE(conn, module_id, port_id)
        """L23 port test payload mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_TPLDMODE`
        """
        self.pfc_enable = P_PFCENABLE(conn, module_id, port_id)
        """L23 port Ethernet Priority Flow Control (PFC).
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_PFCENABLE`
        """
        self.random_seed = P_RANDOMSEED(conn, module_id, port_id)
        """L23 port seed value.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RANDOMSEED`
        """
        self.payload_mode = P_PAYLOADMODE(conn, module_id, port_id)
        """L23 port payload mode.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_PAYLOADMODE`
        """
        self.autotrain = P_AUTOTRAIN(conn, module_id, port_id)
        """L23 port interval between auto training packets.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_AUTOTRAIN`
        """
        self.gap_monitor = P_GAPMONITOR(conn, module_id, port_id)
        """L23 port gap monitor.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_GAPMONITOR`
        """
        self.checksum = P_CHECKSUM(conn, module_id, port_id)
        """L23 port extra payload integrity checksum.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_CHECKSUM`
        """

        self.arp_rx_table = P_ARPRXTABLE(conn, module_id, port_id)
        """L23 port ARP table.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_ARPRXTABLE`
        """
        self.ndp_rx_table = P_NDPRXTABLE(conn, module_id, port_id)
        """L23 port NDP table.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_NDPRXTABLE`
        """

        self.capturer = PortCapture(conn, module_id, port_id)
        """L23 port capturer configuration."""
        self.speed = Speed(conn, module_id, port_id)
        """L23 port speed configuration."""
        self.traffic = Traffic(conn, module_id, port_id)
        """L23 port traffic configuration."""
        self.mix = Mix(conn, module_id, port_id)
        """L23 port IMIX configuration."""
        self.latency_config = LatencyConfiguration(conn, module_id, port_id)
        """L23 port latency configuration."""
        self.rate = Rate(conn, module_id, port_id)
        """L23 port rate."""
        self.tx_config = TxConfiguration(conn, module_id, port_id)
        """L23 port TX configuration."""
        self.tx_single_pkt = TxSinglePacket(conn, module_id, port_id)
        """L23 port single-packet TX configuration."""
        self.multicast = Multicast(conn, module_id, port_id)
        """L23 port multicast configuration."""
        self.net_config = NetworkConfiguration(conn, module_id, port_id)
        """L23 port network configuration."""

        self.local_states = ports_state.PortL23LocalState()
        """L23 port local states."""

        self.length_terms: LengthTermIndices = idx_mgr.IndexManager(
            conn,
            LengthTermIdx,
            module_id,
            port_id
        )
        """L23 port's length term index manager."""

        self.match_terms: MatchTermIndices = idx_mgr.IndexManager(
            conn,
            MatchTermIdx,
            module_id,
            port_id
        )
        """L23 port's match term index manager."""

    async def _setup(self):
        await super()._setup()
        (
            capabilities_r,
            traffic_state_r,
        ) = await funcs.apply(
            self.capabilities.get(),
            self.traffic.state.get()
        )
        self.local_states.capabilities = capabilities_r
        self.local_states.traffic_state = traffic_state_r.on_off
        return self

    def _register_subscriptions(self) -> None:
        super()._register_subscriptions()
        self._conn.subscribe(P_TRAFFIC, utils.Update(self.local_states, "traffic_state", "on_off", self._check_identity))

    on_speed_change = functools.partialmethod(utils.on_event, P_SPEED)
    """Register a callback to the event that the port's speed changes."""

    on_speed_reduction_change = functools.partialmethod(utils.on_event, P_SPEEDREDUCTION)
    """Register a callback to the event that the port's speed reduction changes."""

    on_traffic_change = functools.partialmethod(utils.on_event, P_TRAFFIC)
    """Register a callback to the event that the port's traffic status changes."""

    on_capturer_state_change = functools.partialmethod(utils.on_event, P_CAPTURE)
    """Register a callback to the event that the port's capturer state changes."""

    on_tx_enable_change = functools.partialmethod(utils.on_event, P_TXENABLE)
    """Register a callback to the event that the port's TX status changes."""

    on_interframe_gap_change = functools.partialmethod(utils.on_event, P_INTERFRAMEGAP)
    """Register a callback to the event that the port's interframe gap configuration changes."""

    on_mac_address_change = functools.partialmethod(utils.on_event, P_MACADDRESS)
    """Register a callback to the event that the port's MAC address changes."""

    on_ipv4_address_change = functools.partialmethod(utils.on_event, P_IPADDRESS)
    """Register a callback to the event that the port's IPv4 address changes."""

    on_ipv4_arp_reply_change = functools.partialmethod(utils.on_event, P_ARPREPLY)
    """Register a callback to the event that the port's ARP reply setting changes."""

    on_ipv4_ping_reply_change = functools.partialmethod(utils.on_event, P_PINGREPLY)
    """Register a callback to the event that the port's PING reply setting changes."""

    on_multicast_mode_change = functools.partialmethod(utils.on_event, P_MULTICAST)
    """Register a callback to the event that the port's multicast configuration changes."""

    on_multicast_mode_extended_change = functools.partialmethod(utils.on_event, P_MULTICASTEXT)
    """Register a callback to the event that the port's extended multicast configuration changes."""

    on_multicast_header_change = functools.partialmethod(utils.on_event, P_MULTICASTHDR)
    """Register a callback to the event that the port's multicast packet header changes."""

    on_multicast_source_list_change = functools.partialmethod(utils.on_event, P_MCSRCLIST)
    """Register a callback to the event that the port's multicast source list changes."""

    on_ipv6_address_change = functools.partialmethod(utils.on_event, P_IPV6ADDRESS)
    """Register a callback to the event that the port's IPv6 address setting changes."""

    on_ipv6_arp_reply_change = functools.partialmethod(utils.on_event, P_ARPV6REPLY)
    """Register a callback to the event that the port's NDP reply setting changes."""

    on_ipv6_ping_reply_change = functools.partialmethod(utils.on_event, P_PINGV6REPLY)
    """Register a callback to the event that the port's PINGv6 reply setting changes."""

    on_arp_rx_table_change = functools.partialmethod(utils.on_event, P_ARPRXTABLE)
    """Register a callback to the event that the port's ARP table changes."""

    on_ndp_rx_table_change = functools.partialmethod(utils.on_event, P_NDPRXTABLE)
    """Register a callback to the event that the port's NDP table changes."""

    on_pause_change = functools.partialmethod(utils.on_event, P_PAUSE)
    """Register a callback to the event that the port's response to pause frame setting changes."""

    on_pfc_enable_change = functools.partialmethod(utils.on_event, P_PFCENABLE)
    """Register a callback to the event that the port's response to PFC setting changes."""

    on_random_seed_change = functools.partialmethod(utils.on_event, P_RANDOMSEED)
    """Register a callback to the event that the port's random seed changes."""

    on_latency_offset_change = functools.partialmethod(utils.on_event, P_LATENCYOFFSET)
    """Register a callback to the event that the port's latency offset changes."""

    on_latency_mode_change = functools.partialmethod(utils.on_event, P_LATENCYMODE)
    """Register a callback to the event that the port's latency measurement mode changes."""

    on_tx_time_limit_change = functools.partialmethod(utils.on_event, P_TXTIMELIMIT)
    """Register a callback to the event that the port's TX time limit changes."""

    on_tx_burst_period_change = functools.partialmethod(utils.on_event, P_TXBURSTPERIOD)
    """Register a callback to the event that the port's TX burst period changes."""

    on_tx_packet_limit_change = functools.partialmethod(utils.on_event, P_TXPACKETLIMIT)
    """Register a callback to the event that the port's TX packet count limit changes."""

    on_tx_mode_change = functools.partialmethod(utils.on_event, P_TXMODE)
    """Register a callback to the event that the port's TX mode changes."""

    on_tx_delay_change = functools.partialmethod(utils.on_event, P_TXDELAY)
    """Register a callback to the event that the port's TX deplay changes."""

    on_max_header_length_change = functools.partialmethod(utils.on_event, P_MAXHEADERLENGTH)
    """Register a callback to the event that the port's maximum packet header length changes."""

    on_auto_train_change = functools.partialmethod(utils.on_event, P_AUTOTRAIN)
    """Register a callback to the event that the port's auto training setting changes."""

    on_loop_back_change = functools.partialmethod(utils.on_event, P_LOOPBACK)
    """Register a callback to the event that the port's loopback mode changes."""

    on_checksum_change = functools.partialmethod(utils.on_event, P_CHECKSUM)
    """Register a callback to the event that the port's extra payload integrity checksum changes."""

    on_gap_monitor_change = functools.partialmethod(utils.on_event, P_GAPMONITOR)
    """Register a callback to the event that the port's gap-start and gap-stop settings change."""

    on_mix_weights_change = functools.partialmethod(utils.on_event, P_MIXWEIGHTS)
    """Register a callback to the event that the port's distribution of the MIX packet length changes."""

    on_mix_length_change = functools.partialmethod(utils.on_event, P_MIXLENGTH)
    """Register a callback to the event that the port's frame sizes defined for each mix weight changes."""

    on_tpld_mode_change = functools.partialmethod(utils.on_event, P_TPLDMODE)
    """Register a callback to the event that the port's TPLD mode changes."""

    on_payload_mode_change = functools.partialmethod(utils.on_event, P_PAYLOADMODE)
    """Register a callback to the event that the port's payload mode changes."""
