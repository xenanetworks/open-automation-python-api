from typing import TYPE_CHECKING
from xoa_driver.internals.core.commands import PF_STRING

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli_v1.utils import kind
    from xoa_driver.internals.hli_v1.utils.indices import observer as idx_obs

from .base_filter import BaseFilterIdx


class GenuineFilterIdx(BaseFilterIdx):
    """Genuine L23 Filter Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        self.string = PF_STRING(conn, *kind)
        """Representation of PF_STRING"""
