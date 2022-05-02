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
    """L23 Stream Rate Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.fraction = PS_RATEFRACTION(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_RATEFRACTION`"""
        self.pps = PS_RATEPPS(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_RATEPPS`"""
        self.l2bps = PS_RATEL2BPS(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_RATEL2BPS`"""

class HModifierExtended:
    """L23 Extended Modifier Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int, modifier_idx: int) -> None:
        self.specification = PS_MODIFIEREXT(conn, module_id, port_id, stream_idx, modifier_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_MODIFIEREXT`"""
        self.range = PS_MODIFIEREXTRANGE(conn, module_id, port_id, stream_idx, modifier_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_MODIFIEREXTRANGE`"""
    
class HModifier:
    """L23 Modifier Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int, modifier_idx: int) -> None:
        self.specification = PS_MODIFIER(conn, module_id, port_id, stream_idx, modifier_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_MODIFIEREXTRANGE`"""
        self.range = PS_MODIFIERRANGE(conn, module_id, port_id, stream_idx, modifier_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_MODIFIERRANGE`"""

class SCustomDataField:
    """L23 Custom Data Field Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__stream_idx = stream_idx
        
        self.offset = PS_CDFOFFSET(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_CDFOFFSET`"""
        self.count = PS_CDFCOUNT(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_CDFCOUNT`"""
        
    def data(self, cdf_index: int) -> "PS_CDFDATA":
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_CDFDATA`"""
        return PS_CDFDATA(self.__conn, self.__module_id, self.__port_id, self.__stream_idx, cdf_index)

class SInjectError:
    """L23 Error Injection Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.sequence = PS_INJECTSEQERR(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_INJECTSEQERR`"""
        self.misorder = PS_INJECTMISERR(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_INJECTMISERR`"""
        self.payload_integrity = PS_INJECTPLDERR(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_INJECTPLDERR`"""
        self.test_payload = PS_INJECTTPLDERR(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_INJECTTPLDERR`"""


class SRequest:
    """L23 Request Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.arp = PS_ARPREQUEST(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_ARPREQUEST`"""
        self.ping = PS_PINGREQUEST(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_PINGREQUEST`"""


class SPayload:
    """L23 Payload Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.content = PS_PAYLOAD(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_PAYLOAD`"""
        self.extended = PS_EXTPAYLOAD(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_EXTPAYLOAD`"""


class SGateway:
    """L23 Gateway Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.ipv4 = PS_IPV4GATEWAY(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_IPV4GATEWAY`"""
        self.ipv6 = PS_IPV6GATEWAY(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_IPV6GATEWAY`"""


class SPHeader:
    """L23 Stream Header Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.data = PS_PACKETHEADER(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_PACKETHEADER`"""
        self.protocol = PS_HEADERPROTOCOL(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_HEADERPROTOCOL`"""
        self.modifiers: "hmm.ModifiersManager[HModifier]" = hmm.ModifiersManager(
            conn, 
            (module_id, port_id, stream_idx), 
            PS_MODIFIERCOUNT, 
            HModifier
        )
        """L23 stream modifier index manager"""
        self.modifiers_extended: "hmm.ModifiersManager[HModifierExtended]" = hmm.ModifiersManager(
            conn, 
            (module_id, port_id, stream_idx), 
            PS_MODIFIEREXTCOUNT, 
            HModifierExtended
        )
        """L23 stream extended modifier index manager"""
        
class SPacket:
    """L23 Packet Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.limit = PS_PACKETLIMIT(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_PACKETLIMIT`"""
        self.length = PS_PACKETLENGTH(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_PACKETLENGTH`"""
        self.header = SPHeader(conn, module_id, port_id, stream_idx)
        """Packet header config"""


class SBurst:
    """L23 Stream Burst Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.burstiness = PS_BURST(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_BURST`"""
        self.gap = PS_BURSTGAP(conn, module_id, port_id, stream_idx)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_BURSTGAP`"""

BS = TypeVar("BS")
class BaseStreamIdx(BaseIndex):
    """Base L23 Stream Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        
        self.comment = PS_COMMENT(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_COMMENT`"""
        self.enable = PS_ENABLE(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_ENABLE`"""
        self.tpld_id = PS_TPLDID(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_TPLDID`"""
        self.priority_flow = PS_PFCPRIORITY(conn, *kind)
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_PFCPRIORITY`"""
        
        self.payload = SPayload(conn, *kind)
        """L23 stream payload config"""
        self.request = SRequest(conn, *kind)
        """L23 stream request config"""
        self.packet = SPacket(conn, *kind)
        """L23 stream packet config"""
        self.burst = SBurst(conn, *kind)
        """L23 stream burst config"""
        self.gateway = SGateway(conn, *kind)
        """L23 stream gateway config"""
        self.inject_err = SInjectError(conn, *kind)
        """L23 stream error injections config"""
        self.cdf = SCustomDataField(conn, *kind)
        """L23 stream custom data field config"""
        self.rate = SRate(conn, *kind)
        """L23 stream rate config"""
    
    async def delete(self):
        """Representation of :class:`~xoa_driver.internals.core.commands.ps_commands.PS_DELETE`"""
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