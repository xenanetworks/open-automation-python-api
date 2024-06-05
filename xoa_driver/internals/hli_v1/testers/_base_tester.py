from __future__ import annotations
from typing import (
    TypeVar,
    Awaitable,
    Generic,
    Callable,
    Generator,
    Any
)
from abc import (
    ABC,
    abstractmethod,
)
import functools
from xoa_driver.internals.commands import enums
from xoa_driver.internals.commands import (
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
    C_FLASH,
    C_MODEL_NAME,
    C_MODEL_NUMBER,
)
from xoa_driver.internals.core.funcs import establish_connection
from xoa_driver.internals.core.transporter.handler import TransportationHandler
from xoa_driver.internals.core.transporter.logger import CustomLogger
from xoa_driver.internals.utils import session
from xoa_driver.internals.state_storage import testers_state


T = TypeVar('T', bound="BaseTester")
TesterStateStorage = TypeVar('TesterStateStorage', bound="testers_state.TesterLocalState")


# min version = 83.2
class BaseTester(ABC, Generic[TesterStateStorage]):
    """
    Basic Tester class.

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
        self.__host = host
        self.__port = port
        self._conn = TransportationHandler(
            enable_logging=enable_logging,
            custom_logger=custom_logger
        )
        self.session = session.TesterSession(
            self._conn,
            username,
            password=password,
            timeout_seconds=session_timeout,
            keepalive=True,
        )
        """
        Current management session

        :type: TesterSession
        """

        self.name = C_NAME(self._conn)
        """
        Get and set the name of the tester

        :type: C_NAME
        """

        self.comment = C_COMMENT(self._conn)
        """Description of the tester.

        :type: C_COMMENT
        """

        self.model = C_MODEL(self._conn)
        """Specifies tester's model.

        :type: C_MODEL
        """

        self.model_name = C_MODEL_NAME(self._conn)
        """Specifies tester's model name.

        :type: C_MODEL_NAME
        """

        self.model_number = C_MODEL_NUMBER(self._conn)
        """Specifies tester's model number.

        :type: C_MODEL_NUMBER
        """

        self.version_no = C_VERSIONNO(self._conn)
        """Tester's version number.

        :type: C_VERSIONNO
        """

        self.serial_no = C_SERIALNO(self._conn)
        """Tester's serial number.

        :type: C_SERIALNO
        """

        self.reservation = C_RESERVATION(self._conn)
        """Tester's reservation operation.

        :type: C_RESERVATION
        """

        self.reserved_by = C_RESERVEDBY(self._conn)
        """Tester's reservation status.

        :type: C_RESERVEDBY
        """

        self.down = C_DOWN(self._conn)
        """Shutdown/reboot the tester.

        :type: C_DOWN
        """

        self.password = C_PASSWORD(self._conn)
        """Specifies tester's password.

        :type: C_PASSWORD
        """

        self.time = C_TIME(self._conn)
        """Tester's time in seconds.

        :type: C_TIME
        """

        self.capabilities = C_CAPABILITIES(self._conn)
        """Tester's capabilities.

        :type: C_CAPABILITIES
        """

        self.debug_log = C_DEBUGLOGS(self._conn)
        """Tester's debug log.

        :type: C_DEBUGLOGS
        """

        self.flash = C_FLASH(self._conn)
        """Specifies tester's flash LEDs status.

        :type: C_FLASH
        """

    async def __aenter__(self: Awaitable[T]) -> T:
        return await self

    async def __aexit__(self, type, value, traceback) -> None:
        await self.session.logoff()

    def __await__(self: T) -> Generator[Any, None, T]:
        if self.session.is_online:
            async def skip():
                return self
            return skip().__await__()
        return self._setup().__await__()

    async def _setup(self: T) -> T:
        await establish_connection(self._conn, self.__host, self.__port)
        await self.session.logon()
        return self

    def __is_reservation(self, reserved_status: enums.ReservedStatus) -> bool:
        return self.info.reservation == reserved_status

    is_released = functools.partialmethod(__is_reservation, enums.ReservedStatus.RELEASED)
    """Validate if the tester is released.

    :return: whether the tester is released.
    :rtype: bool
    """

    is_reserved_by_me = functools.partialmethod(__is_reservation, enums.ReservedStatus.RESERVED_BY_YOU)
    """Validate if the tester is reserved by your connection under the username used when logging in.

    :return: whether the tester is reserved by your connection under the username used when logging in.
    :rtype: bool
    """

    @property
    @abstractmethod
    def info(self) -> TesterStateStorage:
        """
        Tester's local information.

        :type: TesterStateStorage
        """

        raise NotImplementedError()

    # region Events

    # We are not supporting Subscription on Connection made, coz Connection is happens at Awaiting of instance
    # but subscription only registered after instance is already created, means already connected,
    # means On_connected event will never b called, it's can be tweaked, but then Creating process of tester instance
    # will be less intuitive, and in one case subscription will work while in another not.

    def on_disconnected(self, callback: "Callable") -> None:
        """
        Register a callback function that will be called at the time when connection will be closed.

        :param callback: the callback function that can be called when the event happens.
        :type callback: Callable
        """

        self._conn.on_disconnected(callback)

    def on_reservation_change(self, callback: "Callable") -> None:
        """
        Register an callback function that will be called when tester's reservation status is changed.

        :param callback: the callback function that can be called when the event happens.
        :type callback: Callable
        """

        self._conn.subscribe(C_RESERVATION, callback)

    def on_reserved_by_change(self, callback: "Callable") -> None:
        """
        Register an callback function that will be called when tester's owner is changed.

        :param callback: the callback function that can be called when the event happens.
        :type callback: Callable
        """

        self._conn.subscribe(C_RESERVEDBY, callback)

    # endregion
