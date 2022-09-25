import functools
from abc import (
    ABC, 
    abstractmethod,
)
from typing import (
    TYPE_CHECKING,
    TypeVar,
    Generic,
)
from xoa_driver.internals.core.commands import enums
from xoa_driver.internals.core.commands import (
    P_RESERVATION,
    P_RESERVEDBY,
    P_RESET,
    P_COMMENT,
    P_INTERFACE,
    P_RECEIVESYNC,
)
from xoa_driver.internals.state_storage import ports_state
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils import kind

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


PortStateStorage = TypeVar('PortStateStorage', bound="ports_state.PortLocalState")

class BasePort(ABC, Generic[PortStateStorage]):
    """Layout which is relevant to all ports."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self._conn = conn
        self.kind = kind.PortKind(module_id, port_id)
        self.sync_status = P_RECEIVESYNC(conn, module_id, port_id)
        """Port sync status.
        Representation of P_RECEIVESYNC
        """
        self.interface = P_INTERFACE(conn, module_id, port_id)
        """Physical interface type of the port.
        Representation of P_INTERFACE
        """
        self.reservation = P_RESERVATION(self._conn, *self.kind)
        """Port reservation action.
        Representation of P_RESERVATION
        """
        self.reserved_by = P_RESERVEDBY(self._conn, *self.kind)
        """Port reservation status.
        Representation of P_RESERVEDBY
        """
        self.reset = P_RESET(self._conn, *self.kind)
        """Port reset action.
        Representation of P_RESET
        """
        self.comment = P_COMMENT(self._conn, *self.kind)
        """Port description.
        Representation of P_COMMENT
        """
    
    def __await__(self):
        return self._setup().__await__()

    @abstractmethod
    async def _setup(self):
        return self
    
    def _check_identity(self, request) -> bool:
        validators = (
            self.kind.module_id == request.header.module_index,
            self.kind.port_id == request.header.port_index
        )
        return all(validators)


    def __is_reservation(self, reserved_status: enums.ReservedStatus) -> bool:
        return self.info.reservation == reserved_status

    is_released = functools.partialmethod(__is_reservation, enums.ReservedStatus.RELEASED)
    """Check if port is released"""

    is_reserved_by_me = functools.partialmethod(__is_reservation, enums.ReservedStatus.RESERVED_BY_YOU)
    """Check if port is released by me"""

    is_reserved_by_others = functools.partialmethod(__is_reservation, enums.ReservedStatus.RESERVED_BY_OTHER)
    """Check if port is released by others"""
    
    @property
    @abstractmethod
    def info(self) -> PortStateStorage:
        """Module info"""
        raise NotImplementedError()
    
    
    on_reservation_change = functools.partialmethod(utils.on_event, P_RESERVATION)
    """Register a callback to the event that the port's reservation status changes."""

    on_receive_sync_change = functools.partialmethod(utils.on_event, P_RECEIVESYNC)
    """Register a callback to the event that the port's SYNC status changes."""

    on_reserved_by_change = functools.partialmethod(utils.on_event, P_RESERVEDBY)
    """Register a callback to the event that the port's reservation ownership changes."""

    on_interface_change = functools.partialmethod(utils.on_event, P_INTERFACE)
    """Register a callback to the event that the port's physical interface type changes."""

