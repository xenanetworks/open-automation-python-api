from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    C_FILESTART,
    C_FILEDATA,
    C_FILEFINISH
)


class UploadFile:
    def __init__(self, conn: "itf.IConnection") -> None:
        self.start = C_FILESTART(conn)
        self.data = C_FILEDATA(conn)
        self.finish = C_FILEFINISH(conn)