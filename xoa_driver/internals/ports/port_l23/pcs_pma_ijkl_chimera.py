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
    """L23 high-speed port link flap."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.params = PP_LINKFLAP_PARAMS(conn, module_id, port_id)
        """Link flap parameters.
        Representation of :class:`~xoa_driver.internals.core.commands.pp_commands.PP_LINKFLAP_PARAMS`
        """
        self.enable = PP_LINKFLAP_ENABLE(conn, module_id, port_id)
        """Link flap control.
        Representation of :class:`~xoa_driver.internals.core.commands.pp_commands.PP_LINKFLAP_ENABLE`
        """

class PmaPulseErrInj:
    """L23 high-speed port PMA pulse error injection."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.params = PP_PMAERRPUL_PARAMS(conn, module_id, port_id)
        """PMA pulse error injection parameters.
        Representation of :class:`~xoa_driver.internals.core.commands.pp_commands.PP_PMAERRPUL_PARAMS`
        """
        self.enable = PP_PMAERRPUL_ENABLE(conn, module_id, port_id)
        """PMA pulse error injection control.
        Representation of :class:`~xoa_driver.internals.core.commands.pp_commands.PP_PMAERRPUL_ENABLE`
        """

class PcsPma:
    """PCS/PMA settings"""
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.link_flap = LinkFlap(conn, *port.kind)
        """Link flap settings."""
        self.pma_pulse_err_inj = PmaPulseErrInj(conn, *port.kind)
        """PMA pulse error injection settings."""