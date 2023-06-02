from typing import (
    final,
    List,
    Type,
    TypeVar,
    TYPE_CHECKING,
)

from xoa_driver.internals.commands import (
    P4G_INDICES,
    P4G_CREATE,
    P4G_DELETE,
    P4G_ENABLE,
    P4G_COMMENT,
    P4G_CLEAR_COUNTERS,
    P4G_ROLE,
    P4G_LP_TIME_SCALE,
    P4G_LP_SHAPE,
    P4G_TEST_APPLICATION,
    P4G_L4_PROTOCOL,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
from xoa_driver.internals.utils.indices import observer as idx_obs
from .tls import GTls
from .l2 import GL2
from .raw import GRaw
from .tcp import GTcp
from .udp import GUdp
from .replay import GReplay
from .l3 import GL3
from .user_state import GUserState
from .histogram import GHistogram

from ..base_index import BaseIndex


class GCounters:
    """Connection Group's counters
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.clear = P4G_CLEAR_COUNTERS(conn, module_id, port_id, group_idx)
        """Clear the counters
        
        :type: P4G_CLEAR_COUNTERS
        """


class GLoadProfile:
    """Connection Group's load profile.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.time_scale = P4G_LP_TIME_SCALE(conn, module_id, port_id, group_idx)
        """Time scale of the load profile
        
        :type: P4G_LP_TIME_SCALE
        """

        self.shape = P4G_LP_SHAPE(conn, module_id, port_id, group_idx)
        """Shape of the load profile.
        
        :type: P4G_LP_SHAPE
        """


CG = TypeVar("CG")


@final
class ConnectionGroupIdx(BaseIndex):
    """L47 Connection Group Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)

        self.comment = P4G_COMMENT(self._conn, *kind)
        """Description of the connection group
        
        :type: P4G_COMMENT
        """

        self.status = P4G_ENABLE(self._conn, *kind)
        """Enable/disable/suppress a previously created connection group
        
        :type: P4G_ENABLE
        """

        self.role = P4G_ROLE(self._conn, *kind)
        """Specifies the client or server role for this Connection Group.
        
        :type: P4G_ROLE
        """

        self.layer4_protocol = P4G_L4_PROTOCOL(self._conn, *kind)
        """Specifies either TCP or UDP as Layer 4 protocol.
        
        :type: P4G_L4_PROTOCOL
        """

        self.test_application = P4G_TEST_APPLICATION(self._conn, *kind)
        """Configure the application layer mode.
        
        :type: P4G_TEST_APPLICATION
        """

        self.tls = GTls(self._conn, *kind)
        """TLS configurations.
        
        :type: GTls
        """

        self.l2 = GL2(self._conn, *kind)
        """L2 configurations.
        
        :type: GL2
        """

        self.raw = GRaw(self._conn, *kind)
        """Raw configurations.
        
        :type: GRaw
        """

        self.tcp = GTcp(self._conn, *kind)
        """TCP configurations.
        
        :type: GTcp
        """

        self.udp = GUdp(self._conn, *kind)
        """UDP configurations.
        
        :type: GUdp
        """

        self.replay = GReplay(self._conn, *kind)
        """Replay configurations.
        
        :type: GReplay
        """

        self.l3 = GL3(self._conn, *kind)
        """L3 configurations.
        
        :type: GL3
        """

        self.user_state = GUserState(self._conn, *kind)
        """User state configurations.
        
        ;type: GUserState
        """

        self.histogram = GHistogram(self._conn, *kind)
        """Histogram configurations.
        
        :type: GHistogram
        """

        self.counters = GCounters(self._conn, *kind)
        """Counters.
        
        :type: GCounters
        """

        self.load_profile = GLoadProfile(self._conn, *kind)
        """Load Profile configurations.
        
        :type: GLoadProfile
        """

    async def delete(self):
        """Delete the Connection Group.
        """
        await P4G_DELETE(self._conn, *self.kind).set()
        self._observer.notify(idx_obs.IndexEvents.DEL, self)

    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await P4G_INDICES(conn, module_id, port_id).get()
        return list(resp.group_identifiers)

    @classmethod
    async def _new(cls: Type[CG], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> CG:
        await P4G_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)
