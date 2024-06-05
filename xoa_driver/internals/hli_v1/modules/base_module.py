
import functools
from typing import (
    TYPE_CHECKING,
    TypeVar,
    Generic
)
from abc import (
    ABC,
    abstractmethod,
)
from typing_extensions import Self
from xoa_driver.internals.commands import enums
from xoa_driver.internals.commands import (
    M_MODEL,
    M_PORTCOUNT,
    M_RESERVATION,
    M_RESERVEDBY,
    M_SERIALNO,
    M_VERSIONNO,
    M_MODEL_NAME,
)
from xoa_driver.internals.utils import attributes as utils

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from . import __interfaces as m_itf
    from xoa_driver.internals.state_storage import modules_state


T = TypeVar('T', bound="modules_state.ModuleLocalState")


class BaseModule(ABC, Generic[T]):
    """Basic Module class.
    """

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        self._conn = conn
        self.module_id = init_data.module_id
        self.ports_count = init_data.ports_count
        self.reservation = M_RESERVATION(self._conn, self.module_id)
        """Test module's reservation action.

        :type: M_RESERVATION
        """

        self.reserved_by = M_RESERVEDBY(self._conn, self.module_id)
        """Test module's reservation status.

        :type: M_RESERVEDBY
        """

        self.model = M_MODEL(self._conn, self.module_id)
        """Test module's model.

        :type: M_MODEL
        """

        self.model_name = M_MODEL_NAME(self._conn, self.module_id)
        """Test module's model name.

        :type: M_MODEL_NAME
        """

        self.serial_number = M_SERIALNO(self._conn, self.module_id)
        """Test module's serial number.

        :type: M_SERIALNO
        """

        self.version_number = M_VERSIONNO(self._conn, self.module_id)
        """Test module's version number.

        :type: M_VERSIONNO
        """

        self.port_count = M_PORTCOUNT(self._conn, self.module_id)
        """Max port count of the test module.

        :type: M_PORTCOUNT
        """

    @property
    @abstractmethod
    def info(self) -> T:
        """
        Module local info.
        """
        raise NotImplementedError()

    def __await__(self):
        return self._setup().__await__()

    @abstractmethod
    async def _setup(self) -> Self:
        raise NotImplementedError()

    def _check_identity(self, request) -> bool:
        return self.module_id == request.header.module_index

    def __is_reservation(self, reserved_status: enums.ReservedStatus) -> bool:
        return self.info.reservation == reserved_status

    is_released = functools.partialmethod(__is_reservation, enums.ReservedStatus.RELEASED)
    """
    Validate if the module is released.
    """

    is_reserved_by_me = functools.partialmethod(__is_reservation, enums.ReservedStatus.RESERVED_BY_YOU)
    """
    Validate if the module is reserved by me.
    """

    on_reservation_change = functools.partialmethod(utils.on_event, M_RESERVATION)
    """
    Register a callback to the event that the module's reservation status changes.
    """

    on_reserved_by_change = functools.partialmethod(utils.on_event, M_RESERVEDBY)
    """
    Register a callback to the event that the module's ownership status changes.
    """

    on_model_change = functools.partialmethod(utils.on_event, M_MODEL)
    """
    Register a callback to the event that the module's legacy model changes.
    """

    on_serial_number_change = functools.partialmethod(utils.on_event, M_SERIALNO)
    """
    Register a callback to the event that the module's serial number status changes.
    """

    on_version_number_change = functools.partialmethod(utils.on_event, M_VERSIONNO)
    """
    Register a callback to the event that the module's version number status changes.
    """
