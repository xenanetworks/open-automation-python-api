from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    C_HEALTH,
)


class Health:
    """File uploading functions of the Valkyrie tester."""

    def __init__(self, conn: "itf.IConnection") -> None:
        self.all = C_HEALTH(conn, [])
        """All chassis health information"""
        self.info = C_HEALTH(conn, [0])
        """Chassis identification information"""
        self.uptime = C_HEALTH(conn, [1])
        """Chassis system uptime"""
