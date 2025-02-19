from typing import (
    TYPE_CHECKING,
    Dict,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.commands import (
    PR_TPLDJITTER,
    PR_TOTAL,
    PR_NOTPLD,
    PR_EXTRA,
    PR_TPLDS,
    PR_TPLDTRAFFIC,
    PR_TPLDERRORS,
    PR_TPLDLATENCY,
    PR_FILTER,
    PR_CLEAR,
    PR_PFCSTATS,
    PR_TOTALEXT,
    PR_NOTPLDEXT,
    PR_TPLDTRAFFICEXT,
    PR_FILTEREXT,
    # genuine only
    PR_CALIBRATE,
    PR_UAT_STATUS,
    PR_UAT_TIME,
    P_MACSEC_RX_STATS,
    P_MACSEC_RX_CLEAR

)


# region All Ports

class PrsTPLD:
    """L23 port's TPLD traffic statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, tpld_idx: int) -> None:
        self.traffic = PR_TPLDTRAFFIC(conn, module_id, port_id, tpld_idx)
        """L23 port's statistics of traffic with TPLD.

        :type: PR_TPLDTRAFFIC
        """

        self.traffic_ext = PR_TPLDTRAFFICEXT(conn, module_id, port_id, tpld_idx)
        """L23 port's statistics of traffic with TPLD. (extended)
        
        :type: PR_TPLDTRAFFICEXT
        """

        self.errors = PR_TPLDERRORS(conn, module_id, port_id, tpld_idx)
        """L23 port's error statistics of traffic with TPLD.

        :type: PR_TPLDERRORS
        """

        self.latency = PR_TPLDLATENCY(conn, module_id, port_id, tpld_idx)
        """L23 port's latency statistics of traffic with TPLD.

        :type: PR_TPLDLATENCY
        """

        self.jitter = PR_TPLDJITTER(conn, module_id, port_id, tpld_idx)
        """L23 port's jitter statistics of traffic with TPLD.

        :type: PR_TPLDJITTER
        """


class PortReceptionStatistics:
    """Port RX statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id

        self.__tpld_ids = PR_TPLDS(conn, module_id, port_id)

        self.total = PR_TOTAL(conn, module_id, port_id)
        """L23 port's total traffic statistics.

        :type: PR_TOTAL
        """

        self.total_ext = PR_TOTALEXT(conn, module_id, port_id)
        """L23 port's total traffic statistics. (extended)
        
        :type: PR_TOTALEXT
        """

        self.no_tpld = PR_NOTPLD(conn, module_id, port_id)
        """L23 port's statistics of traffic without TPLD.

        :type: PR_NOTPLD
        """

        self.no_tpld_ext = PR_NOTPLDEXT(conn, module_id, port_id)
        """L23 port's statistics of traffic without TPLD. (extended)
        
        :type: PR_NOTPLDEXT
        """

        self.extra = PR_EXTRA(conn, module_id, port_id)
        """L23 port's extra traffic statistics.

        :type: PR_EXTRA
        """
        self.pfc_stats = PR_PFCSTATS(conn, module_id, port_id)
        """L23 port's statistics of received PFC packets.

        :type: PR_PFCSTATS
        """
        self.clear = PR_CLEAR(conn, module_id, port_id)
        """Clear all RX statistics on the L23 port.

        :type: PR_CLEAR
        """

    def obtain_filter_statistics(self, filter: int) -> "PR_FILTER":
        """Obtain L23 port filtered traffic statistics.

        :param filter: index of the filter
        :type filter: int
        :return: filtered traffic statistics
        :rtype: PR_FILTER
        """

        return PR_FILTER(
            self.__conn,
            self.__module_id,
            self.__port_id,
            filter
        )

    def obtain_filter_statistics_ext(self, filter: int) -> "PR_FILTEREXT":
        """Obtain L23 port filtered traffic statistics. (extended)

        :param filter: index of the filter
        :type filter: int
        :return: filtered traffic statistics
        :rtype: PR_FILTEREXT
        """

        return PR_FILTEREXT(
            self.__conn,
            self.__module_id,
            self.__port_id,
            filter
        )

    def access_tpld(self, tpld_id: int) -> "PrsTPLD":
        """Access a certain TPLD value on a L23 port.

        :param tpld_id: TPLD value.
        :type tpld_id: int
        :return: L23 port's TPLD traffic statistics
        :rtype: PrsTPLD
        """
        return PrsTPLD(self.__conn, self.__module_id, self.__port_id, tpld_id)

    async def obtain_available_tplds(self) -> Dict[int, "PrsTPLD"]:
        #TODO: need to check use case if this is enough, otherwise to extend by give possibility manually specify indices
        tplds = await self.__tpld_ids.get()
        return {
            idx:
            PrsTPLD(self.__conn, self.__module_id, self.__port_id, idx)
            for idx in tplds.test_payload_identifiers
        }


# endregion

# region Genuine Ports
class GPrsUat():
    """L23 port UAT info."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PR_UAT_STATUS(conn, module_id, port_id)
        """L23 port UAT status.

        :type: PR_UAT_STATUS
        """

        self.time = PR_UAT_TIME(conn, module_id, port_id)
        """L23 port number of unavailable seconds.

        :type: PR_UAT_TIME
        """


class MACSecRxStats:
    """MACSec RX SC Statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.total = P_MACSEC_RX_STATS(conn, module_id, port_id)
        """Port's total MACsec RX statistics

        :type: P_MACSEC_RX_STATS
        """

        self.clear = P_MACSEC_RX_CLEAR(conn, module_id, port_id)
        """Clear Port's MACsec RX statistics

        :type: P_MACSEC_RX_CLEAR
        """


class GenuinePortReceptionStatistics(PortReceptionStatistics):
    """L23 port RX statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.calibrate = PR_CALIBRATE(conn, module_id, port_id)
        """L23 port calibration of latency for received packets.

        :type: PR_CALIBRATE
        """

        self.uat = GPrsUat(conn, module_id, port_id)
        """L23 port UAT info.

        :type: GPrsUat
        """

        self.macsec = MACSecRxStats(conn, module_id, port_id)
        """L23 port's MACsec RX statistics.
        """

# endregion
