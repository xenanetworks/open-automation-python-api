from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    P_MACSEC_TXSC_SAK_INDICES,
    P_MACSEC_TXSC_SAK_TYPE,
    P_MACSEC_TXSC_SAK_VALUE,
    P_MACSEC_RXSC_SAK_INDICES,
    P_MACSEC_RXSC_SAK_TYPE,
    P_MACSEC_RXSC_SAK_VALUE,
)
from .base_macsecsc import (
    BaseMacSecTxScIdx,
    BaseMacSecRxScIdx
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
    from xoa_driver.internals.utils.indices import observer as idx_obs



class GenuineMacSecTxScIdx(BaseMacSecTxScIdx):
    """Genuine MACSec TX SC Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)

        self.sak_indices = P_MACSEC_TXSC_SAK_INDICES(conn, *kind)
        """SAK indices of the TX SC.

        :type:  P_MACSEC_TXSC_SAK_INDICES
        """

        self.sak_type = P_MACSEC_TXSC_SAK_TYPE(conn, *kind)
        """SAK type of the TX SC.

        :type:  P_MACSEC_TXSC_SAK_TYPE
        """

    def access_sak_value(self, sak_index: int) -> "P_MACSEC_TXSC_SAK_VALUE":
        """Access SAK value

        :param sak_index: SAK key index
        :type sak_index: int
        :rtype: P_MACSEC_TXSC_SAK_VALUE
        """

        return P_MACSEC_TXSC_SAK_VALUE(
            self._conn,
            self.kind.module_id,
            self.kind.port_id,
            self.kind.index_id,
            sak_index
        )

class GenuineMacSecRxScIdx(BaseMacSecRxScIdx):
    """Genuine MACSec RX SC Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)

        self.sak_indices = P_MACSEC_RXSC_SAK_INDICES(conn, *kind)
        """SAK indices of the RX SC.

        :type:  P_MACSEC_RXSC_SAK_INDICES
        """

        self.sak_type = P_MACSEC_RXSC_SAK_TYPE(conn, *kind)
        """SAK type of the RX SC.

        :type:  P_MACSEC_RXSC_SAK_TYPE
        """

    def access_sak_value(self, sak_index: int) -> "P_MACSEC_RXSC_SAK_VALUE":
        """Access SAK value

        :param sak_index: SAK key index
        :type sak_index: int
        :rtype: P_MACSEC_RXSC_SAK_VALUE
        """

        return P_MACSEC_RXSC_SAK_VALUE(
            self._conn,
            self.kind.module_id,
            self.kind.port_id,
            self.kind.index_id,
            sak_index
        )