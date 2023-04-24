import typing
from xoa_driver.v2 import ports
from xoa_driver.internals.hli_v2 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P-T1-RJ45")
class MOdin1G3S6PT1RJ45(ModuleL23):
    """Test module Odin-1G-3S-6P-T1-RJ45"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6PT1RJ45] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6PT1RJ45,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-1G-3S-6P-T1-RJ45"""
