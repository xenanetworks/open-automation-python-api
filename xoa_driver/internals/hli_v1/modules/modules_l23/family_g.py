import typing
from xoa_driver import ports
from xoa_driver.internals.hli_v1 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


@typing.final
@revisions.register_valkyrie_module(rev="Loki-100G-3S-1P")
class MLoki100G3S1P(ModuleL23):
    """Test module Loki-100G-3S-1P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PLoki100G3S1P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PLoki100G3S1P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Loki-100G-3S-1P"""


@typing.final
@revisions.register_valkyrie_module(rev="Loki-100G-3S-1P[b]")
class MLoki100G3S1P_b(ModuleL23):
    """Test module Loki-100G-3S-1P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PLoki100G3S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PLoki100G3S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Loki-100G-3S-1P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Loki-100G-3S-1P-SE")
class MLoki100G3S1PSE(ModuleL23):
    """Test module Loki-100G-3S-1P-SE"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PLoki100G3S1PSE] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PLoki100G3S1PSE,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Loki-100G-3S-1P-SE"""


@typing.final
@revisions.register_valkyrie_module(rev="Loki-100G-3S-1P-B")
class MLoki100G3S1PB(ModuleL23):
    """Test module Loki-100G-3S-1P-B"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PLoki100G3S1PB] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PLoki100G3S1PB,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Loki-100G-3S-1P-B"""

@typing.final
@revisions.register_valkyrie_module(rev="Loki-100G-3S-1P-B[b]")
class MLoki100G3S1PB_b(ModuleL23):
    """Test module Loki-100G-3S-1P-B[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PLoki100G3S1PB_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PLoki100G3S1PB_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Loki-100G-3S-1P-B[b]"""