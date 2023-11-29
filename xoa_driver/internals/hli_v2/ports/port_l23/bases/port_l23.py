import functools
import typing
from xoa_driver.internals.commands import (
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
    # P_CAPTURE,
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
    P_CAPABILITIES_EXT,
)
if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.hli_v2.ports import base_port
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.state_storage import ports_state
from xoa_driver.internals.hli_v2.indices.length_term import LengthTermIdx
from xoa_driver.internals.hli_v2.indices.match_term import MatchTermIdx

from .port_capture import PortCapture

LengthTermIndices = idx_mgr.IndexManager[LengthTermIdx]
MatchTermIndices = idx_mgr.IndexManager[MatchTermIdx]


class TxSinglePacket:
    """L23 port single-packet transmission"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.send = P_XMITONE(conn, module_id, port_id)
        """Send one packet from the L23 port without a stream config.
        Representation of P_XMITONE
        """

        self.time = P_XMITONETIME(conn, module_id, port_id)
        """The time at which the latest packet was transmitted using the P_XMITONE` command.
        Representation of P_XMITONETIME
        """


class TxConfiguration:
    """L23 port TX configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_TXMODE(conn, module_id, port_id)
        """L23 port TX mode.
        Representation of P_TXMODE
        """

        self.enable = P_TXENABLE(conn, module_id, port_id)
        """Enabling L23 port TX.
        Representation of P_TXENABLE
        """

        self.time_limit = P_TXTIMELIMIT(conn, module_id, port_id)
        """L23 port TX time limit.
        Representation of P_TXTIMELIMIT
        """

        self.time = P_TXTIME(conn, module_id, port_id)
        """L23 port TX time.
        Representation of P_TXTIME
        """

        self.prepare = P_TXPREPARE(conn, module_id, port_id)
        """Prepare L23 port for transmission.
        Representation of P_TXPREPARE
        """

        self.delay = P_TXDELAY(conn, module_id, port_id)
        """L23 port TX delay.
        Representation of P_TXDELAY
        """

        self.packet_limit = P_TXPACKETLIMIT(conn, module_id, port_id)
        """L23 port TX packet limit
        Representation of P_TXPACKETLIMIT
        """

        self.burst_period = P_TXBURSTPERIOD(conn, module_id, port_id)
        """L23 port TX burst period.
        Representation of P_TXBURSTPERIOD
        """


class Rate:
    """L23 port TX rate"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.fraction = P_RATEFRACTION(conn, module_id, port_id)
        """L23 port rate in ppm.
        Representation of P_RATEFRACTION
        """

        self.pps = P_RATEPPS(conn, module_id, port_id)
        """L23 port rate in packets per second.
        Representation of P_RATEPPS
        """

        self.l2_bps = P_RATEL2BPS(conn, module_id, port_id)
        """L23 port rate in L2 bits per second.
        Representation of P_RATEL2BPS
        """


class Multicast:
    """L23 port multicast configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_MULTICAST(conn, module_id, port_id)
        """L23 port multicast mode.
        Representation of P_MULTICAST
        """

        self.mode_extended = P_MULTICASTEXT(conn, module_id, port_id)
        """L23 port multicast extended mode.
        Representation of P_MULTICASTEXT
        """

        self.source_list = P_MCSRCLIST(conn, module_id, port_id)
        """L23 port multicast source list.
        Representation of P_MCSRCLIST
        """

        self.header = P_MULTICASTHDR(conn, module_id, port_id)
        """L23 port multicast IGMP header.
        Representation of P_MULTICASTHDR
        """


class IPv4:
    """L23 port IPv4 configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPADDRESS(conn, module_id, port_id)
        """L23 port IPv4 address.
        Representation of P_IPADDRESS
        """

        self.arp_reply = P_ARPREPLY(conn, module_id, port_id)
        """L23 port reply to ARP request.
        Representation of P_ARPREPLY
        """

        self.ping_reply = P_PINGREPLY(conn, module_id, port_id)
        """L23 port reply to PING request.
        Representation of P_PINGREPLY
        """


class IPv6:
    """L23 port IPv6 configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPV6ADDRESS(conn, module_id, port_id)
        """L23 port IPv6 address.
        Representation of P_IPV6ADDRESS
        """

        self.arp_reply = P_ARPV6REPLY(conn, module_id, port_id)
        """L23 port reply to NDP Neighbor Solicitation.
        Representation of P_ARPV6REPLY
        """

        self.ping_reply = P_PINGV6REPLY(conn, module_id, port_id)
        """L23 port reply to PINGv6 request.
        Representation of P_PINGV6REPLY
        """


class NetworkConfiguration:  # will be extended in genuine ports
    """L23 port networking configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mac_address = P_MACADDRESS(conn, module_id, port_id)
        """L23 port MAC address.
        Representation of P_MACADDRESS
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
        Representation of P_LATENCYOFFSET
        """

        self.mode = P_LATENCYMODE(conn, module_id, port_id)
        """L23 port latency measurement mode.
        Representation of P_LATENCYMODE
        """


class Mix:
    """L23 port IMIX configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.weights = P_MIXWEIGHTS(conn, module_id, port_id)
        """L23 port IMIX weights
        Representation of P_MIXWEIGHTS
        """

        self.lengths = tuple(
            P_MIXLENGTH(conn, module_id, port_id, idx)
            for idx in range(16)
        )  # TODO: need to add manager for handle specific indices only
        """L23 port IMIX lengths.
        Representation of P_MIXLENGTH
        """


class Speed:
    """L23 port speed configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.current = P_SPEED(conn, module_id, port_id)
        """L23 port current speed in units of Mbps.
        Representation of P_SPEED
        """

        self.reduction = P_SPEEDREDUCTION(conn, module_id, port_id)
        """L23 port speed reduction in ppm.
        Representation of P_SPEEDREDUCTION
        """


class Traffic:
    """L23 port traffic generation"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.state = P_TRAFFIC(conn, module_id, port_id)
        """L23 port traffic status and action.
        Representation of P_TRAFFIC
        """

        self.error = P_TRAFFICERR(conn, module_id, port_id)
        """L23 port traffic error.
        Representation of P_TRAFFICERR
        """


class BasePortL23(base_port.BasePort[ports_state.PortL23LocalState]):
    """L23 port layout which is relevant to all L23 ports."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        """L23 port capabilities.
        Representation of P_CAPABILITIES
        """
        
        self.capabilities_ext = P_CAPABILITIES_EXT(conn, module_id, port_id)
        """L23 port capabilities ext.

        Representation of P_CAPABILITIES_EXT
        """

        self.pause = P_PAUSE(conn, module_id, port_id)
        """L23 port response to Ethernet PAUSE frames.
        Representation of P_PAUSE
        """

        self.loop_back = P_LOOPBACK(conn, module_id, port_id)
        """L23 port loopback mode.
        Representation of P_LOOPBACK
        """

        self.errors_count = P_ERRORS(conn, module_id, port_id)
        """L23 port errors.
        Representation of P_ERRORS
        """

        self.interframe_gap = P_INTERFRAMEGAP(conn, module_id, port_id)
        """L23 port interframe gap.
        Representation of P_INTERFRAMEGAP
        """

        self.max_header_length = P_MAXHEADERLENGTH(conn, module_id, port_id)
        """L23 port maximum header length.
        Representation of P_MAXHEADERLENGTH
        """

        self.tpld_mode = P_TPLDMODE(conn, module_id, port_id)
        """L23 port test payload mode.
        Representation of P_TPLDMODE
        """

        self.pfc_enable = P_PFCENABLE(conn, module_id, port_id)
        """L23 port Ethernet Priority Flow Control (PFC).
        Representation of P_PFCENABLE
        """

        self.random_seed = P_RANDOMSEED(conn, module_id, port_id)
        """L23 port seed value.
        Representation of P_RANDOMSEED
        """

        self.payload_mode = P_PAYLOADMODE(conn, module_id, port_id)
        """L23 port payload mode.
        Representation of P_PAYLOADMODE
        """

        self.autotrain = P_AUTOTRAIN(conn, module_id, port_id)
        """L23 port interval between auto training packets.
        Representation of P_AUTOTRAIN
        """

        self.gap_monitor = P_GAPMONITOR(conn, module_id, port_id)
        """L23 port gap monitor.
        Representation of P_GAPMONITOR
        """

        self.checksum = P_CHECKSUM(conn, module_id, port_id)
        """L23 port extra payload integrity checksum.
        Representation of P_CHECKSUM
        """

        self.arp_rx_table = P_ARPRXTABLE(conn, module_id, port_id)
        """L23 port ARP table.
        Representation of P_ARPRXTABLE
        """

        self.ndp_rx_table = P_NDPRXTABLE(conn, module_id, port_id)
        """L23 port NDP table.
        Representation of P_NDPRXTABLE
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

    on_speed_change = functools.partialmethod(utils.on_event, P_SPEED)
    """Register a callback to the event that the port's speed changes."""

    on_traffic_change = functools.partialmethod(utils.on_event, P_TRAFFIC)
    """Register a callback to the event that the port's traffic status changes."""
