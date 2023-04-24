import typing
from xoa_driver.v2 import ports
from xoa_driver.internals.hli_v2 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


@typing.final
@revisions.register_valkyrie_module(rev="Thor-400G-7S-1P[b]")
class MThor400G7S1P_b(ModuleL23):
    """Test module Thor-400G-7S-1P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PThor400G7S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PThor400G7S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Thor-400G-7S-1P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Thor-400G-7S-1P[c]")
class MThor400G7S1P_c(ModuleL23):
    """Test module Thor-400G-7S-1P[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PThor400G7S1P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PThor400G7S1P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Thor-400G-7S-1P[c]"""


@typing.final
@revisions.register_valkyrie_module(rev="Thor-400G-7S-1P[d]")
class MThor400G7S1P_d(ModuleL23):
    """Test module Thor-400G-7S-1P[d]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PThor400G7S1P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PThor400G7S1P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Thor-400G-7S-1P[d]"""
