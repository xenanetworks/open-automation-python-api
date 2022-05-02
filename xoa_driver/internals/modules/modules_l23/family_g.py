import typing
from xoa_driver import ports
from xoa_driver.internals.utils import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23

@typing.final
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
        """Port index manager of Loki-100G-3S-1P"""

@typing.final
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
        """Port index manager of Loki-100G-3S-1P[b]"""

@typing.final
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
        """Port index manager of Loki-100G-3S-1P-SE"""
