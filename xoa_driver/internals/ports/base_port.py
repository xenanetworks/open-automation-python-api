import functools
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
from xoa_driver.internals.core.transporter import funcs
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils import kind

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


PortStateStorage = TypeVar('PortStateStorage', bound="ports_state.PortLocalState")

class BasePort(Generic[PortStateStorage]):
    """Layout which is relevant to all ports."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self._conn = conn
        self.kind = kind.PortKind(module_id, port_id)
        self.sync_status = P_RECEIVESYNC(conn, module_id, port_id)
        """Port sync status.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RECEIVESYNC`
        """
        self.interface = P_INTERFACE(conn, module_id, port_id)
        """Physical interface type of the port.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_INTERFACE`
        """
        self.reservation = P_RESERVATION(self._conn, *self.kind)
        """Port reservation action.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RESERVATION`
        """
        self.reserved_by = P_RESERVEDBY(self._conn, *self.kind)
        """Port reservation status.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RESERVEDBY`
        """
        self.reset = P_RESET(self._conn, *self.kind)
        """Port reset action.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_RESET`
        """
        self.comment = P_COMMENT(self._conn, *self.kind)
        """Port description.
        Representation of :class:`~xoa_driver.internals.core.commands.p_commands.P_COMMENT`
        """
        
        self.local_states = ports_state.PortLocalState()
        self._register_subscriptions()
        
    def __await__(self):
        return self._setup().__await__()

    async def _setup(self):
        (
            sync_status_r,
            interface_r,
            reservation_r,
            reserved_by_r,
        ) = await funcs.apply(
            self.sync_status.get(),
            self.interface.get(),
            self.reservation.get(),
            self.reserved_by.get(),
        )
        self.local_states.sync_status = sync_status_r.sync_status
        self.local_states.interface = interface_r.interface
        self.local_states.reservation = reservation_r.status
        self.local_states.reserved_by = reserved_by_r.username
        return self
    
    def _check_identity(self, request) -> bool:
        return (
            self.kind.module_id == request.header.module_index 
            and
            self.kind.port_id == request.header.port_index
        )
    
    def _register_subscriptions(self) -> None:
        self._conn.subscribe(P_RECEIVESYNC, utils.Update(self.local_states, "sync_status", "sync_status", self._check_identity))
        self._conn.subscribe(P_RESERVEDBY, utils.Update(self.local_states, "reserved_by", "username", self._check_identity))
        self._conn.subscribe(P_RESERVATION, utils.Update(self.local_states, "reservation", "status", self._check_identity))
        self._conn.subscribe(P_INTERFACE, utils.Update(self.local_states, "interface", "interface", self._check_identity))

    def __is_reservation(self, reserved_status: enums.ReservedStatus) -> bool:
        return self.local_states.reservation == reserved_status

    is_released = functools.partialmethod(__is_reservation, enums.ReservedStatus.RELEASED)
    """Check if port is released"""
    is_reserved_by_me = functools.partialmethod(__is_reservation, enums.ReservedStatus.RESERVED_BY_YOU)
    """Check if port is released by me"""
    is_reserved_by_others = functools.partialmethod(__is_reservation, enums.ReservedStatus.RESERVED_BY_OTHER)
    """Check if port is released by others"""
    
    @property
    def info(self) -> PortStateStorage:
        """Module info"""
        return self.local_states  # type: ignore
    
    
    on_reservation_change = functools.partialmethod(utils.on_event, P_RESERVATION)
    """Register a callback to the event that the port's reservation status changes."""

    on_receive_sync_change = functools.partialmethod(utils.on_event, P_RECEIVESYNC)
    """Register a callback to the event that the port's SYNC status changes."""

    on_reserved_by_change = functools.partialmethod(utils.on_event, P_RESERVEDBY)
    """Register a callback to the event that the port's reservation ownership changes."""

    on_interface_change = functools.partialmethod(utils.on_event, P_INTERFACE)
    """Register a callback to the event that the port's physical interface type changes."""

