from typing import (
    List,
    Type,
    TypeVar,
    TYPE_CHECKING,
)
from xoa_driver.internals.core.commands import (
    PS_INDICES,
    PS_CREATE,
    PS_DELETE,
    
    PS_ENABLE,
    PS_PACKETLIMIT,
    PS_COMMENT,
    PS_TPLDID,
    PS_ARPREQUEST,
    PS_PINGREQUEST,
    PS_MODIFIEREXTRANGE,
    PS_MODIFIERRANGE,
    PS_RATEFRACTION,
    PS_RATEPPS,
    PS_RATEL2BPS,
    PS_BURST,
    PS_PACKETHEADER,
    PS_HEADERPROTOCOL,
    PS_MODIFIERCOUNT,
    PS_MODIFIER,
    PS_PACKETLENGTH,
    PS_PAYLOAD,
    PS_IPV4GATEWAY,
    PS_IPV6GATEWAY,
    PS_BURSTGAP,
    PS_INJECTSEQERR,
    PS_INJECTMISERR,
    PS_INJECTPLDERR,
    PS_INJECTTPLDERR,
    PS_MODIFIEREXT,
    PS_MODIFIEREXTCOUNT,
    PS_CDFOFFSET,
    PS_CDFCOUNT,
    PS_CDFDATA,
    PS_EXTPAYLOAD,
    PS_PFCPRIORITY,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
from xoa_driver.internals.utils.indices import observer as idx_obs
from xoa_driver.internals.utils.indices import header_modifier_manager as hmm
from ..base_index import BaseIndex


class SRate:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.fraction = PS_RATEFRACTION(conn, module_id, port_id, stream_idx)
        self.pps = PS_RATEPPS(conn, module_id, port_id, stream_idx)
        self.l2bps = PS_RATEL2BPS(conn, module_id, port_id, stream_idx)

class HModifierExtended:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int, modifier_idx: int) -> None:
        self.specification = PS_MODIFIEREXT(conn, module_id, port_id, stream_idx, modifier_idx)
        self.range = PS_MODIFIEREXTRANGE(conn, module_id, port_id, stream_idx, modifier_idx)
    
class HModifier:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int, modifier_idx: int) -> None:
        self.specification = PS_MODIFIER(conn, module_id, port_id, stream_idx, modifier_idx)
        self.range = PS_MODIFIERRANGE(conn, module_id, port_id, stream_idx, modifier_idx)

class SCustomDataField:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__stream_idx = stream_idx
        
        self.offset = PS_CDFOFFSET(conn, module_id, port_id, stream_idx)
        self.count = PS_CDFCOUNT(conn, module_id, port_id, stream_idx)
        
    def data(self, cdf_index: int) -> "PS_CDFDATA":
        return PS_CDFDATA(self.__conn, self.__module_id, self.__port_id, self.__stream_idx, cdf_index)

class SInjectError:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.sequence = PS_INJECTSEQERR(conn, module_id, port_id, stream_idx)
        self.misorder = PS_INJECTMISERR(conn, module_id, port_id, stream_idx)
        self.payload_integrity = PS_INJECTPLDERR(conn, module_id, port_id, stream_idx)
        self.test_payload = PS_INJECTTPLDERR(conn, module_id, port_id, stream_idx)


class SRequest:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.arp = PS_ARPREQUEST(conn, module_id, port_id, stream_idx)
        self.ping = PS_PINGREQUEST(conn, module_id, port_id, stream_idx)


class SPayload:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.content = PS_PAYLOAD(conn, module_id, port_id, stream_idx)
        self.extended = PS_EXTPAYLOAD(conn, module_id, port_id, stream_idx)


class SGateway:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.ipv4 = PS_IPV4GATEWAY(conn, module_id, port_id, stream_idx)
        self.ipv6 = PS_IPV6GATEWAY(conn, module_id, port_id, stream_idx)


class SPHeader:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.data = PS_PACKETHEADER(conn, module_id, port_id, stream_idx)
        self.protocol = PS_HEADERPROTOCOL(conn, module_id, port_id, stream_idx)
        self.modifiers: "hmm.ModifiersManager[HModifier]" = hmm.ModifiersManager(
            conn, 
            (module_id, port_id, stream_idx), 
            PS_MODIFIERCOUNT, 
            HModifier
        )
        self.modifiers_extended: "hmm.ModifiersManager[HModifierExtended]" = hmm.ModifiersManager(
            conn, 
            (module_id, port_id, stream_idx), 
            PS_MODIFIEREXTCOUNT, 
            HModifierExtended
        )
        
class SPacket:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.limit = PS_PACKETLIMIT(conn, module_id, port_id, stream_idx)
        self.length = PS_PACKETLENGTH(conn, module_id, port_id, stream_idx)
        self.header = SPHeader(conn, module_id, port_id, stream_idx)


class SBurst:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.burstiness = PS_BURST(conn, module_id, port_id, stream_idx)
        self.gap = PS_BURSTGAP(conn, module_id, port_id, stream_idx)

BS = TypeVar("BS")
class BaseStreamIdx(BaseIndex):
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        
        self.comment = PS_COMMENT(conn, *kind)
        self.enable = PS_ENABLE(conn, *kind)
        self.tpld_id = PS_TPLDID(conn, *kind)
        self.priority_flow = PS_PFCPRIORITY(conn, *kind)
        
        self.payload = SPayload(conn, *kind)
        self.request = SRequest(conn, *kind)
        self.packet = SPacket(conn, *kind)
        self.burst = SBurst(conn, *kind)
        self.gateway = SGateway(conn, *kind)
        self.inject_err = SInjectError(conn, *kind)
        self.cdf = SCustomDataField(conn, *kind)
        self.rate = SRate(conn, *kind)
    
    async def delete(self):
        await PS_DELETE(self._conn, *self.kind).set()
        self._observer.notify(idx_obs.IndexEvents.DEL, self)
    
    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await PS_INDICES(conn, module_id, port_id).get()
        return list(resp.stream_indices)
    
    @classmethod
    async def _new(cls: Type[BS], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> BS:
        await PS_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)