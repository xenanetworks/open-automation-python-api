from __future__ import annotations
from xoa_driver.internals.commands import (
    C_BUILDSTRING,
    C_VERSIONNO_MINOR
)
from xoa_driver.internals.core.transporter.logger import CustomLogger
from .l47_tester import L47Tester


class L47VeTester(L47Tester):
    """
    Representation of a virtual Xena Vulcan Tester.
    """

    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, enable_logging: bool = False, custom_logger: CustomLogger | None = None) -> None:
        super().__init__(
            host=host,
            username=username,
            password=password,
            port=port,
            enable_logging=enable_logging,
            custom_logger=custom_logger
        )
        self.version_no_minor = C_VERSIONNO_MINOR(self._conn)
        """
        Representation of C_VERSIONNO_MINOR
        """

        self.build_string = C_BUILDSTRING(self._conn)
        """
        Representation of C_BUILDSTRING
        """
