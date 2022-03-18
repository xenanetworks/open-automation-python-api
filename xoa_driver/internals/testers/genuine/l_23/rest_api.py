from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    C_RESTPORT,
    C_RESTENABLE,
    C_RESTSTATUS,
    C_RESTCONTROL,
)


class RestApiServer:
    """
    Controll Rest API server for L23 Tester
    """
    def __init__(self, conn: "itf.IConnection") -> None:
        self.port = C_RESTPORT(conn)
        self.enable = C_RESTENABLE(conn)
        self.status = C_RESTSTATUS(conn)
        self.control = C_RESTCONTROL(conn)
