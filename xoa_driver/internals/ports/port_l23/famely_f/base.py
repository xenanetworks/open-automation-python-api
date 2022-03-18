import functools
from typing import TYPE_CHECKING
from ..bases.port_l23_genuine import BasePortL23Genuine
from xoa_driver.internals.core.commands import (
    P_DYNAMIC,
    P_TXRUNTLENGTH,
    P_RXRUNTLENGTH,
    P_RXRUNTLEN_ERRS,
    P_TXPREAMBLE_REMOVE,
    P_RXPREAMBLE_INSERT,

)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class FamelyF(BasePortL23Genuine):
    ...


class POdin10G1S2P(FamelyF):
    ...

class POdin10G1S2P_b(FamelyF):
    ...

class POdin10G1S2P_c(FamelyF):
    ...

class POdin10G1S6P(FamelyF):
    ...


class Runt:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_length = P_TXRUNTLENGTH(conn, module_id, port_id)
        self.rx_length = P_RXRUNTLENGTH(conn, module_id, port_id)
        self.rx_errors = P_RXRUNTLEN_ERRS(conn, module_id, port_id)

class Preamble:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_remove = P_TXPREAMBLE_REMOVE(conn, module_id, port_id)
        self.rx_insert = P_RXPREAMBLE_INSERT(conn, module_id, port_id)

class POdin10G1S6P_b(FamelyF):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.runt = Runt(conn, module_id, port_id)
        self.preamble = Preamble(conn, module_id, port_id)
        
    on_runt_tx_length_change = functools.partialmethod(utils.on_event, P_TXRUNTLENGTH)
    on_runt_rx_length_change = functools.partialmethod(utils.on_event, P_RXRUNTLENGTH)
    on_preamble_tx_remove_change = functools.partialmethod(utils.on_event, P_TXPREAMBLE_REMOVE)
    on_preamble_rx_insert_change = functools.partialmethod(utils.on_event, P_RXPREAMBLE_INSERT)

class POdin10G1S2PT(FamelyF):
    ...

class POdin10G1S2P_d(FamelyF):
    ...

class POdin10G1S12P(FamelyF):
    ...

class POdin40G2S2P(FamelyF):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)

