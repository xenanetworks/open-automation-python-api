from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    PP_LINKFLAP_PARAMS,
    PP_LINKFLAP_ENABLE,
    PP_PMAERRPUL_PARAMS,
    PP_PMAERRPUL_ENABLE,
)

class LinkFlap:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.params = PP_LINKFLAP_PARAMS(conn, module_id, port_id)
        self.enable = PP_LINKFLAP_ENABLE(conn, module_id, port_id)

class PmaPulseErrInj:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.params = PP_PMAERRPUL_PARAMS(conn, module_id, port_id)
        self.enable = PP_PMAERRPUL_ENABLE(conn, module_id, port_id)

class PcsPma:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.link_flap = LinkFlap(conn, *port.kind)
        self.pma_pulse_err_inj = PmaPulseErrInj(conn, *port.kind)