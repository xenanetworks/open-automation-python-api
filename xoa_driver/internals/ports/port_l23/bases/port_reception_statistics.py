from typing import (
    TYPE_CHECKING,
    Dict,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.core.commands import (
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
    # genuine only
    PR_CALIBRATE,
    PR_UAT_STATUS,
    PR_UAT_TIME,

)

# region All Ports
class PrsTPLD:
    """L23 port's TPLD traffic statisttics."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, tpld_idx: int) -> None:
        self.traffic = PR_TPLDTRAFFIC(conn, module_id, port_id, tpld_idx)
        """L23 port's statistics of traffic with TPLD.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_TPLDTRAFFIC`
        """
        self.errors = PR_TPLDERRORS(conn, module_id, port_id, tpld_idx)
        """L23 port's error statistics of traffic with TPLD.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_TPLDERRORS`
        """
        self.latency= PR_TPLDLATENCY(conn, module_id, port_id, tpld_idx)
        """L23 port's latency statistics of traffic with TPLD.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_TPLDLATENCY`
        """
        self.jitter = PR_TPLDJITTER(conn, module_id, port_id, tpld_idx)
        """L23 port's jitter statistics of traffic with TPLD.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_TPLDJITTER`
        """


class PortReceptionStatistics:
    """Port RX statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        
        self.__tpld_ids = PR_TPLDS(conn, module_id, module_id)
        
        self.total = PR_TOTAL(conn, module_id, port_id)
        """L23 port's total traffic statistics.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_TOTAL`
        """
        self.no_tpld = PR_NOTPLD(conn, module_id, port_id)
        """L23 port's statistics of traffic without TPLD.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_NOTPLD`
        """
        self.extra = PR_EXTRA(conn, module_id, port_id)
        """L23 port's extra traffic statistics.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_EXTRA`
        """
        self.pfc_packets = PR_PFCSTATS(conn, module_id, port_id)
        """L23 port's statistics of received PFC packets.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_PFCSTATS`
        """
        self.clear = PR_CLEAR(conn, module_id, port_id)
        """Clear all RX statistics on the L23 port.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_CLEAR`
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
    
    def access_tpld(self, tpld_id: int) -> "PrsTPLD":
        """Access a certain TPLD value on a L23 port.

        :param tpld_id: TPLD value.
        :type tpld_id: int
        :return: L23 port's TPLD traffic statisttics
        :rtype: PrsTPLD
        """
        return PrsTPLD(self.__conn, self.__module_id, self.__port_id, tpld_id)
    
    async def obtain_available_tplds(self) -> Dict[int, "PrsTPLD"]:
        # TODO: need to check usecase if this is enaough, otherwise to extend by give possibility manually specify indices
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
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_UAT_STATUS`
        """
        self.time = PR_UAT_TIME(conn, module_id, port_id)
        """L23 port number of unavailable seconds.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_UAT_TIME`
        """

class GenuinePortReceptionStatistics(PortReceptionStatistics):
    """L23 port RX statistics."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.calibrate = PR_CALIBRATE(conn, module_id, port_id)
        """L23 port calibration of latency for received packets.
        Representation of :class:`~xoa_driver.internals.core.commands.pr_commands.PR_CALIBRATE`
        """
        self.uat = GPrsUat(conn, module_id, port_id)
        """L23 port UAT info.
        """

# endregion