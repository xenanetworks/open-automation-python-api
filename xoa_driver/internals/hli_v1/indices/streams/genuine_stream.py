from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PS_INSERTFCS,
    PS_INJECTFCSERR,
    PS_MACSEC_ENABLE,
    PS_MACSEC_ASSIGN,
)
from .base_stream import (
    BaseStreamIdx,
    SInjectError
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
    from xoa_driver.internals.utils.indices import observer as idx_obs


class GSInjectError(SInjectError):
    """Error Injection configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        super().__init__(conn, module_id, port_id, stream_idx)
        self.frame_checksum = PS_INJECTFCSERR(conn, module_id, port_id, stream_idx)
        """Inject FCS error

        :type: PS_INJECTFCSERR
        """

class SMacSec:
    """MACSec configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.enable = PS_MACSEC_ENABLE(conn, module_id, port_id, stream_idx)
        """Enable MACSec

        :type: PS_MACSEC_ENABLE
        """

        self.assign = PS_MACSEC_ASSIGN(conn, module_id, port_id, stream_idx)
        """Assign MACSec

        :type: PS_MACSEC_ASSIGN
        """

class GenuineStreamIdx(BaseStreamIdx):
    """Genuine L23 Stream Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        self.insert_packets_checksum = PS_INSERTFCS(conn, *kind)
        """Whether a valid frame checksum is added to the packets of a stream.

        :type:  PS_INSERTFCS
        """

        self.inject_err = GSInjectError(conn, *kind)
        """Error injection configuration

        :type: GSInjectError
        """

        self.macsec = SMacSec(conn, *kind)
        """MACSec configuration

        :type: SMacSec
        """
