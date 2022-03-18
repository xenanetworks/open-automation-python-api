from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    PP_AUTONEG,
    PP_AUTONEGSTATUS,
    PP_LINKTRAIN,
    PP_LINKTRAINSTATUS,
)


class AutoNeg:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.settings = PP_AUTONEG(conn, module_id, port_id)
        self.status = PP_AUTONEGSTATUS(conn, module_id, port_id)


class LinkTrain:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.settings = PP_LINKTRAIN(conn, *port.kind)
        self.pir_lane_status: Tuple[PP_LINKTRAINSTATUS, ...] = tuple(
            PP_LINKTRAINSTATUS(conn, *port.kind, _lane_xindex=idx)
            for idx in range(port.info.capabilities.lane_count) # TODO: need to fix, currently port.info.capabilities must be none coz virtual_lanes created before awaiting the port
        )


class PcsPma:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.auto_neg = AutoNeg(conn, *port.kind)
        self.link_training = LinkTrain(conn, port)