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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, tpld_idx: int) -> None:
        self.traffic = PR_TPLDTRAFFIC(conn, module_id, port_id, tpld_idx)
        self.errors = PR_TPLDERRORS(conn, module_id, port_id, tpld_idx)
        self.latency= PR_TPLDLATENCY(conn, module_id, port_id, tpld_idx)
        self.jitter = PR_TPLDJITTER(conn, module_id, port_id, tpld_idx)


class PortReceptionStatistics:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        
        self.__tpld_ids = PR_TPLDS(conn, module_id, module_id)
        
        self.totatl = PR_TOTAL(conn, module_id, port_id)
        self.no_tpld = PR_NOTPLD(conn, module_id, port_id)
        self.extra = PR_EXTRA(conn, module_id, port_id)
        self.pfc_packets = PR_PFCSTATS(conn, module_id, port_id)
        self.clear = PR_CLEAR(conn, module_id, port_id)
    
    def obtain_filter_statistics(self, filter: int) -> "PR_FILTER":
        return PR_FILTER(
            self.__conn, 
            self.__module_id, 
            self.__port_id, 
            filter
        )
    
    def access_tpld(self, tpld_id: int) -> "PrsTPLD":
        return PrsTPLD(self.__conn, self.__module_id, self.__port_id, tpld_id)
    
    async def obtain_avliable_tplds(self) -> Dict[int, "PrsTPLD"]:
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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PR_UAT_STATUS(conn, module_id, port_id)
        self.time = PR_UAT_TIME(conn, module_id, port_id)

class GenuinePortReceptionStatistics(PortReceptionStatistics):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.calibrate = PR_CALIBRATE(conn, module_id, port_id)
        self.uat = GPrsUat(conn, module_id, port_id)

# endregion