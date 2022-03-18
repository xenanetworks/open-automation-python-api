from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    C_TKLICFILE,
    C_TKLICSTATE,
    C_TKSTATUS,
    C_TKSTATUSEXT,
    C_TKSVCSTATE,
    C_TKGPSSTATE,
    C_TKCONFIG,
)

class TimeKeeper:
    def __init__(self, conn: "itf.IConnection") -> None:
        self.license_file = C_TKLICFILE(conn)
        self.license_state = C_TKLICSTATE(conn)
        self.status = C_TKSTATUS(conn)
        self.status_extended = C_TKSTATUSEXT(conn)
        self.svc_state = C_TKSVCSTATE(conn)
        self.gps_state = C_TKGPSSTATE(conn)
        self.config_file = C_TKCONFIG(conn)
