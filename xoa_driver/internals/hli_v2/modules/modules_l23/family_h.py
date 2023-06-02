import typing
from xoa_driver.v2 import ports
from xoa_driver.internals.hli_v2 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


@typing.final
@revisions.register_valkyrie_module(rev="Loki-100G-5S-1P")
class MLoki100G5S1P(ModuleL23):
    """Test module Loki-100G-5S-1P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PLoki100G5S1P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PLoki100G5S1P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Loki-100G-5S-1P"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-100G-3S-1P")
class MOdin100G3S1P(ModuleL23):
    """Test module Odin-100G-3S-1P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin100G3S1P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin100G3S1P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-100G-3S-1P"""
