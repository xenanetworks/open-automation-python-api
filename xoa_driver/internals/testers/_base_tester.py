from typing import (
    TypeVar,
    Awaitable,
    Generic,
    Callable,
    Generator,
    Any
)
import functools
from xoa_driver.internals.core.commands import enums
from xoa_driver.internals.core.commands import (
    C_RESERVATION,
    C_DOWN,
    C_PASSWORD,
    C_TIME,
    C_CAPABILITIES,
    C_DEBUGLOGS,
    C_NAME,
    C_MODEL,
    C_COMMENT,
    C_VERSIONNO,
    C_SERIALNO,
    C_RESERVEDBY,
)
from xoa_driver.internals.utils import attributes as utils

import xoa_driver.internals.testers._tester_session as session
from xoa_driver.internals.state_storage import testers_state

from xoa_driver.internals.core.transporter import (
    establish_connection,
    TransportationHandler,
)
from xoa_driver.internals.core.transporter import funcs



T = TypeVar('T', bound="BaseTester")
TesterStateStorage = TypeVar('TesterStateStorage', bound="testers_state.TesterLocalState")

# ToDo: lately update imports to correct style
# min version = 83.2
class BaseTester(Generic[TesterStateStorage]):
    def __init__(self, host: str, username: str, password: str = "xena", port: int = 22606, *, debug: bool = False) -> None:
        self.__host = host
        self.__port = port
        self._conn = TransportationHandler(debug=debug)
        self.session = session.TesterSession(
            self._conn,
            username,
            password=password,
            keepalive=True,
        )
        """
        Current management session
        """

        self.name = C_NAME(self._conn)
        """
        Tester's name.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_NAME`
        """

        self.comment = C_COMMENT(self._conn)
        """Description of the tester.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_COMMENT`
        """

        self.model = C_MODEL(self._conn)
        """Tester's model.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_MODEL`
        """

        self.version_no = C_VERSIONNO(self._conn)
        """Tester's version number.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_VERSIONNO`
        """

        self.serial_no = C_SERIALNO(self._conn)
        """Tester's serial number.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_SERIALNO`
        """

        self.reservation = C_RESERVATION(self._conn)
        """Tester's reservation operation.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_RESERVATION`
        """

        self.reserved_by = C_RESERVEDBY(self._conn)
        """Tester's reservation status.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_RESERVEDBY`
        """

        self.down = C_DOWN(self._conn)
        """Shut down the tester.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_DOWN`
        """

        self.password = C_PASSWORD(self._conn)
        """Tester's password.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_PASSWORD`
        """

        self.time = C_TIME(self._conn)
        """Tester's time in seconds.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_TIME`
        """

        self.capabilities = C_CAPABILITIES(self._conn)
        """Tester's capabilities.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_CAPABILITIES`
        """

        self.debug_log = C_DEBUGLOGS(self._conn)
        """Tester's debug log.
        Representation of :class:`~xoa_driver.internals.core.commands.c_commands.C_DEBUGLOGS`
        """

        self._local_states = testers_state.TesterLocalState(host, port)
        self._register_subscriptions()

    async def __aenter__(self: Awaitable[T]) -> T:
        return await self

    async def __aexit__(self, type, value, traceback) -> None:
        await self.session.logoff()

    def __await__(self: T) -> Generator[Any, None, T]: 
        if self.session.is_online:
            async def skip(): return self
            return skip().__await__()
        return self._setup().__await__()

    async def _setup(self: T) -> T:
        await establish_connection(self._conn, self.__host, self.__port)
        await self.session

        (
            capabilities_resp,
            model_res,
            v_major_res,
            serial_res,
            reserved_by_res,
            reservation_resp,
        ) = await funcs.apply(
            self.capabilities.get(),
            self.model.get(),
            self.version_no.get(),
            self.serial_no.get(),
            self.reserved_by.get(),
            self.reservation.get(),
        )
        self._local_states.reserved_by = reserved_by_res.username
        self._local_states.model = model_res.model
        self._local_states.driver_version = v_major_res.pci_driver_version
        self._local_states.version_major = v_major_res.chassis_major_version
        self._local_states.serial_number = serial_res.serial_number
        self._local_states.reservation = reservation_resp.operation
        self._local_states.capabilities = capabilities_resp
        return self

    def _register_subscriptions(self) -> None:
        self._conn.subscribe(C_RESERVEDBY, utils.Update(self._local_states, "reserved_by", "username"))
        self._conn.subscribe(C_RESERVATION, utils.Update(self._local_states, "reservation", "operation"))


    def __is_reservation(self, reserved_status: enums.ReservedStatus) -> bool:
        return self._local_states.reservation == reserved_status

    is_released = functools.partialmethod(__is_reservation, enums.ReservedStatus.RELEASED)
    """Validate if the tester is released.
    """

    is_reserved_by_me = functools.partialmethod(__is_reservation, enums.ReservedStatus.RESERVED_BY_YOU)
    """Validate if the tester is reserved by my connection.
    """

    @property
    def info(self) -> TesterStateStorage:
        """
        Tester's local information.
        """
        return self._local_states  # type: ignore


    # region Events

    # We are not supporting Subscription on Connection made, coz Connection is happens at Awaiting of instance
    # but subscription only registered after instance is already created, means already connected,
    # means On_connected event will never b called, it's can be twiked, but then Creating process of tester instance
    # will be less intuitive, and in one case subscription will work while in another not.

    def on_disconnected(self, callback: "Callable") -> None:
        """
        Register a callback which will be called at the time when connection will be closed.
        """
        self._conn.on_disconnected(callback)

    def on_reservation_change(self, callback: "Callable") -> None:
        """
        Register an callback function to C_RESERVATION event.
        """
        self._conn.subscribe(C_RESERVATION, callback)

    def on_reserved_by_change(self, callback: "Callable") -> None:
        """
        Register an callback function to C_RESERVEDBY event.
        """
        self._conn.subscribe(C_RESERVEDBY, callback)

    # endregion