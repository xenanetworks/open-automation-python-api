import asyncio
from typing import (
    TYPE_CHECKING, 
    Tuple
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.transporter import funcs
from xoa_driver.internals.core.transporter.exceptions import BadStatus
from xoa_driver.internals.exceptions.testers import WrongTesterPasswordError
from xoa_driver import enums
from xoa_driver.internals.core.commands import (
    C_LOGON, 
    C_LOGOFF,
    C_OWNER,
    C_TIMEOUT,
    C_KEEPALIVE,
    C_INDICES,
    C_STATSESSION,
)

class TesterSession:
    """
    Establishing communication session through connection with ester unit.
    """
    
    __slots__ = ("_conn", "owner_name", "pwd", "timeout", "keepalive")
    
    def __init__(self, conn: "itf.IConnection", owner_name: str, password: str = "xena", timeout_seconds: int = 130, keepalive: bool = False) -> None:
        self._conn = conn
        self.owner_name = owner_name
        self.pwd = password
        self.timeout = timeout_seconds
        self.keepalive = keepalive

    def __await__(self):
        return self.__setup().__await__()

    async def __setup(self) -> "TesterSession":
        try:
            await funcs.apply(
                C_LOGON(self._conn).set(self.pwd),
                C_OWNER(self._conn).set(self.owner_name),
                C_TIMEOUT(self._conn).set(self.timeout),
            )
        except BadStatus as e:
            if e.response.class_name == "C_LOGON" and e.response.command_status == enums.CommandStatus.BADVALUE:
                raise WrongTesterPasswordError(self.pwd) from None
            raise e
        if self.keepalive:
            asyncio.create_task(self.__do_keepalive(), name="keepalive") # TODO: need to handle this task on interuption
        return self

    async def __do_keepalive(self) -> None:
        while self._conn.is_connected:
            await C_KEEPALIVE(self._conn).get()
            await asyncio.sleep(max(0, self.timeout-5))

    @property
    def is_online(self) -> bool:
        """
        Check if connection is still active.
        """
        return self._conn.is_connected

    async def logoff(self) -> None:
        """
        Gracefull logoff from the tester.
        """
        await C_LOGOFF(self._conn).set()
        self._conn.close()

    async def sessions_info(self) -> Tuple[C_STATSESSION.GetDataAttr, ...]:
        """
        Return information about all active sessions on the tester.
        """
        sessions = await C_INDICES(self._conn).get()
        session_ids = sessions.session_ids
        query_sessions = [
            C_STATSESSION(self._conn, session_xindex=sid).get()
            for sid in session_ids
        ]
        return tuple(await funcs.apply(*query_sessions))
