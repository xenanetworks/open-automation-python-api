from typing import (
    List,
    Type,
    TypeVar,
    TYPE_CHECKING,
)
from xoa_driver.internals.commands import (
    P_MACSEC_TXSC_INDICES,
    P_MACSEC_TXSC_CREATE,
    P_MACSEC_TXSC_DELETE,
    P_MACSEC_TXSC_DESCR,
    P_MACSEC_TXSC_SCI_MODE,
    P_MACSEC_TXSC_SCI,
    P_MACSEC_TXSC_CONF_OFFSET,
    P_MACSEC_TXSC_CIPHERSUITE,
    P_MACSEC_TXSC_STARTING_PN,
    P_MACSEC_TXSC_VLAN_MODE,
    P_MACSEC_TXSC_REKEY_MODE,
    P_MACSEC_TXSC_ENCRYPT,
    P_MACSEC_RXSC_INDICES,
    P_MACSEC_RXSC_CREATE,
    P_MACSEC_RXSC_DELETE,
    P_MACSEC_RXSC_DESCR,
    P_MACSEC_RXSC_SCI,
    P_MACSEC_RXSC_CONF_OFFSET,
    P_MACSEC_RXSC_CIPHERSUITE,
    P_MACSEC_RXSC_TPLDID,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
from xoa_driver.internals.utils.indices import observer as idx_obs
from xoa_driver.internals.utils.indices import header_modifier_manager as hmm
from ..base_index import BaseIndex


class MACSecTxScConfig:
    """MACSec TX SC Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, txsc_idx: int) -> None:
        
        self.description = P_MACSEC_TXSC_DESCR(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's description

        :type: P_MACSEC_TXSC_DESCR
        """

        self.sci_mode = P_MACSEC_TXSC_SCI_MODE(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's SCI mode

        :type: P_MACSEC_TXSC_SCI_MODE
        """

        self.sci = P_MACSEC_TXSC_SCI(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's SCI value

        :type: P_MACSEC_TXSC_SCI
        """

        self.confidentiality_offset = P_MACSEC_TXSC_CONF_OFFSET(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's confidentiality offset

        :type: P_MACSEC_TXSC_CONF_OFFSET
        """

        self.cipher_suite = P_MACSEC_TXSC_CIPHERSUITE(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's cipher suite

        :type: P_MACSEC_TXSC_CIPHERSUITE
        """

        self.starting_pn = P_MACSEC_TXSC_STARTING_PN(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's starting PN

        :type: P_MACSEC_TXSC_STARTING_PN
        """

        self.vlan_mode = P_MACSEC_TXSC_VLAN_MODE(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's VLAN mode

        :type: P_MACSEC_TXSC_VLAN_MODE
        """

        self.rekey_mode = P_MACSEC_TXSC_REKEY_MODE(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's rekey mode

        :type: P_MACSEC_TXSC_REKEY_MODE
        """

        self.encryption_mode = P_MACSEC_TXSC_ENCRYPT(conn, module_id, port_id, txsc_idx)
        """Configure TX SC's encryption mode

        :type: P_MACSEC_TXSC_ENCRYPT
        """

class MACSecRxScConfig:
    """MACSec RX SC Configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, rxsc_idx: int) -> None:
        
        self.description = P_MACSEC_RXSC_DESCR(conn, module_id, port_id, rxsc_idx)
        """Configure RX SC's description

        :type: P_MACSEC_RXSC_DESCR
        """

        self.sci = P_MACSEC_RXSC_SCI(conn, module_id, port_id, rxsc_idx)
        """Configure RX SC's SCI value

        :type: P_MACSEC_RXSC_SCI
        """

        self.confidentiality_offset = P_MACSEC_RXSC_CONF_OFFSET(conn, module_id, port_id, rxsc_idx)
        """Configure RX SC's confidentiality offset

        :type: P_MACSEC_RXSC_CONF_OFFSET
        """

        self.cipher_suite = P_MACSEC_RXSC_CIPHERSUITE(conn, module_id, port_id, rxsc_idx)
        """Configure RX SC's cipher suite

        :type: P_MACSEC_RXSC_CIPHERSUITE
        """

        self.tpld_id = P_MACSEC_RXSC_TPLDID(conn, module_id, port_id, rxsc_idx)
        """Configure RX SC's TPLD ID value

        :type: P_MACSEC_RXSC_TPLDID
        """


# class MACSecTxStats:
#     """MACSec TX SC Statistics"""
#     def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, txsc_idx: int) -> None:

#         self.total = P_MACSEC_TX_STATS(conn, module_id, port_id)
#         """Port's total MACsec TX statistics

#         :type: P_MACSEC_TX_STATS
#         """

#         self.clear = P_MACSEC_TX_CLEAR(conn, module_id, port_id)
#         """Clear Port's MACsec TX statistics

#         :type: P_MACSEC_TX_CLEAR
#         """


# class MACSecRxStats:
#     """MACSec RX SC Statistics"""
#     def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, rxsc_idx: int) -> None:

#         self.total = P_MACSEC_RX_STATS(conn, module_id, port_id)
#         """Port's total MACsec RX statistics

#         :type: P_MACSEC_RX_STATS
#         """

#         self.clear = P_MACSEC_RX_CLEAR(conn, module_id, port_id)
#         """Clear Port's MACsec RX statistics

#         :type: P_MACSEC_RX_CLEAR
#         """



BS = TypeVar("BS")


class BaseMacSecTxScIdx(BaseIndex):
    """Base MACSec TX SC Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)

        self.config = MACSecTxScConfig(conn, *kind)
        """MACSec TX SC Configuration
        
        :type: MACSecTxScConfig
        """

    async def delete(self):
        """Delete the TX SC

        :type: P_MACSEC_TXSC_DELETE
        """

        await P_MACSEC_TXSC_DELETE(self._conn, *self.kind).set()
        self._observer.notify(idx_obs.IndexEvents.DEL, self)

    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await P_MACSEC_TXSC_INDICES(conn, module_id, port_id).get()
        return list(resp.txsc_indices)

    @classmethod
    async def _new(cls: Type[BS], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> BS:
        await P_MACSEC_TXSC_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)


class BaseMacSecRxScIdx(BaseIndex):
    """Base MACSec RX SC Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)

        self.config = MACSecRxScConfig(conn, *kind)
        """MACSec RX SC Configuration
        
        :type: MACSecRxScConfig
        """

    async def delete(self):
        """Delete the RX SC

        :type: P_MACSEC_RXSC_DELETE
        """

        await P_MACSEC_RXSC_DELETE(self._conn, *self.kind).set()
        self._observer.notify(idx_obs.IndexEvents.DEL, self)

    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await P_MACSEC_RXSC_INDICES(conn, module_id, port_id).get()
        return list(resp.rxsc_indices)

    @classmethod
    async def _new(cls: Type[BS], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> BS:
        await P_MACSEC_RXSC_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)