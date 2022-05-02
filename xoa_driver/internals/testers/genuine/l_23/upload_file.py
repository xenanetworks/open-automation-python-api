from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    C_FILESTART,
    C_FILEDATA,
    C_FILEFINISH
)


class UploadFile:
    """File uploading functions of the Valkyrie tester."""
    def __init__(self, conn: "itf.IConnection") -> None:
        self.start = C_FILESTART(conn)
        """Start uploading file.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_FILESTART`
        """
        self.data = C_FILEDATA(conn)
        """Uploading a file fragment.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_FILEDATA`
        """
        self.finish = C_FILEFINISH(conn)
        """Finish uploading file.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_FILEFINISH`
        """