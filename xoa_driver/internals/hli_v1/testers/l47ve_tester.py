
from xoa_driver.internals.commands import (
    C_BUILDSTRING,
    C_VERSIONNO_MINOR
)
from .l47_tester import L47Tester


class L47VeTester(L47Tester):
    """
    This is a conceptual class of Xena VulcanVE Tester.
    It is essentially an extended :class:`BaseTester`.


    :param host: tester's address/hostname
    :type host: str
    :param username: username of the user
    :type username: str
    :param password: login password of the tester, defaults to "xena"
    :type password: str, optional
    :param port: the port number for connection establishment, default to 22606
    :type port: int, optional
    :param debug: `True` if debug log output from the tester is needed, and `False` otherwise
    :type debug: int, optional
    """

    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, debug: bool = False) -> None:
        super().__init__(host=host, username=username, password=password, port=port, debug=debug)
        self.version_no_minor = C_VERSIONNO_MINOR(self._conn)
        """
        Get the minor version number of the tester firmware.

        :type: C_VERSIONNO_MINOR
        """

        self.build_string = C_BUILDSTRING(self._conn)
        """
        Identify the hostname of the PC that builds the xenaserver. It uniquely identifies the build of a xenaserver.

        :type: C_BUILDSTRING
        """
