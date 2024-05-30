import typing
from xoa_driver import ports
from xoa_driver.internals.hli_v1 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


@typing.final
@revisions.register_valkyrie_module(rev="Thor-400G-7S-1P")
class MThor400G7S1P(ModuleL23):
    """Test module Thor-400G-7S-1P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PThor400G7S1P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PThor400G7S1P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index of Thor-400G-7S-1P"""

@typing.final
@revisions.register_valkyrie_module(rev="Thor-400G-7S-1P LE")
class MThor400G7S1PLE(ModuleL23):
    """Test module Thor-400G-7S-1P LE"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PThor400G7S1PLE] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PThor400G7S1PLE,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index of Thor-400G-7S-1P LE"""
