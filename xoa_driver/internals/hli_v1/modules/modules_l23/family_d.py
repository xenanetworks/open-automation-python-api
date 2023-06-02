import typing
from xoa_driver import ports
from xoa_driver.internals.hli_v1 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm


if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P")
class MOdin1G3S6P(ModuleL23):
    """Test module Odin-1G-3S-6P"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-6P"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P[b]")
class MOdin1G3S6P_b(ModuleL23):
    """Test module Odin-1G-3S-6P[b]"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-6P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P-E")
class MOdin1G3S6PE(ModuleL23):
    """Test module Odin-1G-3S-6P-E"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6PE] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6PE,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-6P-E"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-2P-T")
class MOdin1G3S2PT(ModuleL23):
    """Test module Odin-1G-3S-2P-T"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S2PT] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S2PT,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-2P-T"""
