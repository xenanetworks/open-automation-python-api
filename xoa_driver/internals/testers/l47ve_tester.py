
from xoa_driver.internals.core.commands import (
    C_BUILDSTRING,
    C_VERSIONNO_MINOR
)




from .l47_tester import L47Tester
class L47VeTester(L47Tester):
    """
    Representation of a virtual Xena Vulcan Tester.
    """
    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, debug: bool = False ) -> None:
        super().__init__(host=host, username=username, password=password, port=port, debug=debug)
        self.version_no_minor = C_VERSIONNO_MINOR(self._conn)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_VERSIONNO_MINOR`
        """

        self.build_string = C_BUILDSTRING(self._conn)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_BUILDSTRING`
        """
