import asyncio
from contextlib import suppress
from typing import (
    TYPE_CHECKING,
    Tuple
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core import funcs
from xoa_driver.internals.core.exceptions import XmpBadValueError
from xoa_driver.internals import exceptions
from xoa_driver.internals.commands import (
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
    Establishing communication session through connection with the tester.

    :param conn: connection handler
    :type host: itf.IConnection
    :param owner_name: username of the user
    :type username: str
    :param password: login password of the tester, defaults to "xena"
    :type password: str, optional
    :param timeout_seconds: the timeout to close idle connection
    :type port: int, optional
    :param keepalive: `True` if keepalive signal is needed, and `False` otherwise, defaults to `False`.
    :type keepalive: bool, optional
    """

    __slots__ = ("_conn", "owner_name", "pwd", "timeout", "keepalive")

    def __init__(self, conn: "itf.IConnection", owner_name: str, password: str = "xena", timeout_seconds: int = 130, keepalive: bool = False) -> None:
        self._conn = conn
        self.owner_name = owner_name
        self.pwd = password
        self.timeout = timeout_seconds
        self.keepalive = keepalive

    async def logon(self) -> "TesterSession":
        logon, *_ = await funcs.apply(
            C_LOGON(self._conn).set(self.pwd),
            C_OWNER(self._conn).set(self.owner_name),
            C_TIMEOUT(self._conn).set(self.timeout),
            return_exceptions=True,
            token_timeout_sec=1.0
        )
        if isinstance(logon, XmpBadValueError):
            raise exceptions.WrongTesterPasswordError(self.pwd) from None

        if self.keepalive:
            asyncio.create_task(self.__do_keepalive(), name="keepalive").add_done_callback(
                self.__handle_exceptions
            )
        return self

    async def chang_timeout(self, seconds: int = 130) -> None:
        """Modify session timeout, """
        if not self.is_online:
            raise RuntimeError("Timeout can be changet only after connection is established.")
        self.timeout = seconds
        await C_TIMEOUT(self._conn).set(self.timeout)

    def __handle_exceptions(self, fut: asyncio.Future) -> None:
        if fut.cancelled():
            return None
        elif e := fut.exception():
            raise e

    async def __do_keepalive(self) -> None:
        while self._conn.is_connected:
            with suppress(Exception):
                await C_KEEPALIVE(self._conn).get()
            await asyncio.sleep(max(0, self.timeout - 5))

    @property
    def is_online(self) -> bool:
        """
        Check if connection is still active.

        :return: connection is still on or not.
        :rtype: bool
        """

        return self._conn.is_connected

    async def logoff(self) -> None:
        """
        Gracefully log off from the tester.
        """

        await C_LOGOFF(self._conn).set()
        self._conn.close()

    async def sessions_info(self) -> Tuple[C_STATSESSION.GetDataAttr, ...]:
        """
        Return information about all active sessions on the tester.

        :return: a list of session information
        :rtype: List[C_STATSESSION]
        """

        sessions = await C_INDICES(self._conn).get()
        session_ids = sessions.session_ids
        query_sessions = (
            C_STATSESSION(self._conn, _session_xindex=sid).get()
            for sid in session_ids
        )
        return tuple(await funcs.apply(*query_sessions))
