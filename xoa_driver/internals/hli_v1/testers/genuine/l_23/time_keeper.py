from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    C_TKLICFILE,
    C_TKLICSTATE,
    C_TKSTATUS,
    C_TKSTATUSEXT,
    C_TKSVCSTATE,
    C_TKGPSSTATE,
    C_TKCONFIG,
)


class TimeKeeper:
    """TimeKeeper of Valkyrie."""

    def __init__(self, conn: "itf.IConnection") -> None:
        self.license_file = C_TKLICFILE(conn)
        """TimeKeeper license file content.
                
        :type: C_TKLICFILE
        """

        self.license_state = C_TKLICSTATE(conn)
        """State of TimeKeeper license file content.
                
        :type: C_TKLICSTATE
        """

        self.status = C_TKSTATUS(conn)
        """Version and status of TimeKeeper.
                
        :type: C_TKSTATUS
        """

        self.status_extended = C_TKSTATUSEXT(conn)
        """Version and status of TimeKeeper (extended).
                
        :type: C_TKSTATUSEXT
        """

        self.svc_state = C_TKSVCSTATE(conn)
        """TimeKeeper service state.
                
        :type: C_TKSVCSTATE
        """

        self.gps_state = C_TKGPSSTATE(conn)
        """TimeKeeper GPS state.
                
        :type: C_TKGPSSTATE
        """

        self.config_file = C_TKCONFIG(conn)
        """TimeKeeper configuration file content.
                
        :type: C_TKCONFIG
        """
