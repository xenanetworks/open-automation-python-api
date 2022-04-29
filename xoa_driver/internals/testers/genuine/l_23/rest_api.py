from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    C_RESTPORT,
    C_RESTENABLE,
    C_RESTSTATUS,
    C_RESTCONTROL,
)


class RestApiServer:
    """
    Rest API server for the Valkyrie tester
    """
    def __init__(self, conn: "itf.IConnection") -> None:
        self.port = C_RESTPORT(conn)
        """TCP port for the REST server.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_RESTPORT`
        """
        self.enable = C_RESTENABLE(conn)
        """Enable the REST server.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_RESTENABLE`
        """
        self.status = C_RESTSTATUS(conn)
        """Status of the REST server.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_RESTSTATUS`
        """
        self.control = C_RESTCONTROL(conn)
        """Control the REST server.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_RESTCONTROL`
        """
