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

LengthTermIndices = idx_mgr.IndexManager[LengthTermIdx]
MatchTermIndices = idx_mgr.IndexManager[MatchTermIdx]

class TxSinglePacket:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.send = P_XMITONE(conn, module_id, port_id)
        self.time = P_XMITONETIME(conn, module_id, port_id)


class TxConfiguration:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_TXMODE(conn, module_id, port_id)
        self.enable = P_TXENABLE(conn, module_id, port_id)
        self.time_limit = P_TXTIMELIMIT(conn, module_id, port_id)
        self.time = P_TXTIME(conn, module_id, port_id)
        self.repare = P_TXPREPARE(conn, module_id, port_id)
        self.delay = P_TXDELAY(conn, module_id, port_id)
        self.packet_limit = P_TXPACKETLIMIT(conn, module_id, port_id)
        self.burst_period = P_TXBURSTPERIOD(conn, module_id, port_id)


class Rate:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.fraction = P_RATEFRACTION(conn, module_id, port_id)
        self.pps = P_RATEPPS(conn, module_id, port_id)
        self.l2_bps = P_RATEL2BPS(conn, module_id, port_id)


class Multicast:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_MULTICAST(conn, module_id, port_id)
        self.mode_extended = P_MULTICASTEXT(conn, module_id, port_id)
        self.source_list = P_MCSRCLIST(conn, module_id, port_id)
        self.header = P_MULTICASTHDR(conn, module_id, port_id)


class IPv4:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPADDRESS(conn, module_id, port_id)
        self.arp_reply = P_ARPREPLY(conn, module_id, port_id)
        self.ping_reply = P_PINGREPLY(conn, module_id, port_id)


class IPv6:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPV6ADDRESS(conn, module_id, port_id)
        self.arp_reply = P_ARPV6REPLY(conn, module_id, port_id)
        self.ping_reply = P_PINGV6REPLY(conn, module_id, port_id)


class NetworkConfiguration: # will be extended in genuine ports
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mac_address = P_MACADDRESS(conn, module_id, port_id)
        self.ipv4 = IPv4(conn, module_id, port_id)
        self.ipv6 = IPv6(conn, module_id, port_id)


class LatencyConfiguration:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.offset = P_LATENCYOFFSET(conn, module_id, port_id)
        self.mode = P_LATENCYMODE(conn, module_id, port_id)

class Mix:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.weights = P_MIXWEIGHTS(conn, module_id, port_id)
        self.lengths = tuple(
            P_MIXLENGTH(conn, module_id, port_id, idx)
            for idx in range(16)
        ) # TODO: need to add manager for handle specific indices only

class Speed:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.current = P_SPEED(conn, module_id, port_id)
        self.reduction = P_SPEEDREDUCTION(conn, module_id, port_id)

class Traffic:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.state = P_TRAFFIC(conn, module_id, port_id)
        self.error = P_TRAFFICERR(conn, module_id, port_id)

class BasePortL23(base_port.BasePort[ports_state.PortL23LocalState]):
    """L23 port layout which relevant to all L23 ports."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        self.pause = P_PAUSE(conn, module_id, port_id)
        self.loop_back = P_LOOPBACK(conn, module_id, port_id)
        self.capture = P_CAPTURE(conn, module_id, port_id)
        self.errors_count = P_ERRORS(conn, module_id, port_id)
        

        self.interframe_gap = P_INTERFRAMEGAP(conn, module_id, port_id)
        self.max_header_length = P_MAXHEADERLENGTH(conn, module_id, port_id)
        self.tpld_mode = P_TPLDMODE(conn, module_id, port_id)
        self.pfc_enable = P_PFCENABLE(conn, module_id, port_id)
        self.random_seed = P_RANDOMSEED(conn, module_id, port_id)
        self.payload_mode = P_PAYLOADMODE(conn, module_id, port_id)
        self.autotrain = P_AUTOTRAIN(conn, module_id, port_id)
        self.gap_monitor = P_GAPMONITOR(conn, module_id, port_id)
        self.checksum = P_CHECKSUM(conn, module_id, port_id)

        self.arp_rx_table = P_ARPRXTABLE(conn, module_id, port_id)
        self.ndp_rx_table = P_NDPRXTABLE(conn, module_id, port_id)

        self.speed = Speed(conn, module_id, port_id)
        self.traffic = Traffic(conn, module_id, port_id)
        self.mix = Mix(conn, module_id, port_id)
        self.latency_config = LatencyConfiguration(conn, module_id, port_id)
        self.rate = Rate(conn, module_id, port_id)
        self.tx_config = TxConfiguration(conn, module_id, port_id)
        self.tx_single_pkt = TxSinglePacket(conn, module_id, port_id)
        self.multicast = Multicast(conn, module_id, port_id)
        self.net_config = NetworkConfiguration(conn, module_id, port_id)

        self.local_states = ports_state.PortL23LocalState()

        self.length_term: LengthTermIndices = idx_mgr.IndexManager(
            conn,
            LengthTermIdx,
            module_id,
            port_id
        )
        self.match_term: MatchTermIndices = idx_mgr.IndexManager(
            conn,
            MatchTermIdx,
            module_id,
            port_id
        )

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
    on_speed_reduction_change = functools.partialmethod(utils.on_event, P_SPEEDREDUCTION)
    on_traffic_change = functools.partialmethod(utils.on_event, P_TRAFFIC)
    on_capture_change = functools.partialmethod(utils.on_event, P_CAPTURE)
    on_tx_enable_change = functools.partialmethod(utils.on_event, P_TXENABLE)
    on_interframe_gap_change = functools.partialmethod(utils.on_event, P_INTERFRAMEGAP)
    on_mac_address_change = functools.partialmethod(utils.on_event, P_MACADDRESS)
    on_ipv4_address_change = functools.partialmethod(utils.on_event, P_IPADDRESS)
    on_ipv4_arp_replay_change = functools.partialmethod(utils.on_event, P_ARPREPLY)
    on_ipv4_ping_replay_change = functools.partialmethod(utils.on_event, P_PINGREPLY)
    on_multicast_mode_change = functools.partialmethod(utils.on_event, P_MULTICAST)
    on_multicast_mode_extended_change = functools.partialmethod(utils.on_event, P_MULTICASTEXT)
    on_multicast_header_change = functools.partialmethod(utils.on_event, P_MULTICASTHDR)
    on_multicast_source_list_change = functools.partialmethod(utils.on_event, P_MCSRCLIST)
    on_ipv6_address_change = functools.partialmethod(utils.on_event, P_IPV6ADDRESS)
    on_ipv6_arp_reply_change = functools.partialmethod(utils.on_event, P_ARPV6REPLY)
    on_ipv6_ping_reply_change = functools.partialmethod(utils.on_event, P_PINGV6REPLY)
    on_arp_rx_table_change = functools.partialmethod(utils.on_event, P_ARPRXTABLE)
    on_ndp_rx_table_change = functools.partialmethod(utils.on_event, P_NDPRXTABLE)
    on_pause_change = functools.partialmethod(utils.on_event, P_PAUSE)
    on_pfc_enable_change = functools.partialmethod(utils.on_event, P_PFCENABLE)
    on_random_seed_change = functools.partialmethod(utils.on_event, P_RANDOMSEED)
    on_latency_offset_change = functools.partialmethod(utils.on_event, P_LATENCYOFFSET)
    on_latency_mode_change = functools.partialmethod(utils.on_event, P_LATENCYMODE)
    on_tx_time_limit_change = functools.partialmethod(utils.on_event, P_TXTIMELIMIT)
    on_tx_burst_period_change = functools.partialmethod(utils.on_event, P_TXBURSTPERIOD)
    on_tx_packet_limit_change = functools.partialmethod(utils.on_event, P_TXPACKETLIMIT)
    on_tx_mode_change = functools.partialmethod(utils.on_event, P_TXMODE)
    on_tx_delay_change = functools.partialmethod(utils.on_event, P_TXDELAY)
    on_max_header_length_change = functools.partialmethod(utils.on_event, P_MAXHEADERLENGTH)
    on_auto_train_change = functools.partialmethod(utils.on_event, P_AUTOTRAIN)
    on_loop_back_change = functools.partialmethod(utils.on_event, P_LOOPBACK)
    on_checksum_change = functools.partialmethod(utils.on_event, P_CHECKSUM)
    on_gap_monitor_change = functools.partialmethod(utils.on_event, P_GAPMONITOR)
    on_mix_weights_change = functools.partialmethod(utils.on_event, P_MIXWEIGHTS)
    on_mix_length_change = functools.partialmethod(utils.on_event, P_MIXLENGTH)
    on_tpld_mode_change = functools.partialmethod(utils.on_event, P_TPLDMODE)
    on_payload_mode_change = functools.partialmethod(utils.on_event, P_PAYLOADMODE)
