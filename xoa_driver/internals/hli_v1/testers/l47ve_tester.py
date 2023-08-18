from __future__ import annotations
from xoa_driver.internals.commands import (
    C_BUILDSTRING,
    C_VERSIONNO_MINOR
)
from xoa_driver.internals.core.transporter.logger import CustomLogger
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
    :param enable_logging: `True` if debug log output from the tester is needed, and `False` otherwise
    :type enable_logging: bool
    :param custom_logger: `None` allow to specify logger with custom configurations
    :type enable_logging: CustomLogger | None
    :param session_timeout: `130` Session timeout in seconds
    :type session_timeout: int
    """

    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, enable_logging: bool = False, custom_logger: CustomLogger | None = None, session_timeout: int = 130) -> None:
        super().__init__(
            host=host,
            username=username,
            password=password,
            port=port,
            enable_logging=enable_logging,
            custom_logger=custom_logger,
            session_timeout=session_timeout
        )
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
