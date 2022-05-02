import typing
from xoa_driver import ports
from xoa_driver.internals.utils import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23

@typing.final
class MLoki100G5S2P(ModuleL23):
    """Test module Loki-100G-5S-2P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PLoki100G5S2P] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.PLoki100G5S2P, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Loki-100G-5S-2P"""
