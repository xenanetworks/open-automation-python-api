import typing
from xoa_driver import ports
from xoa_driver.internals.utils import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23

@typing.final
class MOdin5G4S6PCU(ModuleL23):
    """Test module Odin-5G-4S-6P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin5G4S6PCU] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.POdin5G4S6PCU, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-5G-4S-6P-CU"""

@typing.final
class MOdin10G5S6PCU(ModuleL23):
    """Test module Odin-10G-5S-6P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G5S6PCU] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.POdin10G5S6PCU, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-5S-6P-CU"""

@typing.final
class MOdin10G5S6PCU_b(ModuleL23):
    """Test module Odin-10G-5S-6P-CU[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G5S6PCU_b] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.POdin10G5S6PCU_b, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-5S-6P-CU[b]"""

@typing.final
class MOdin10G3S6PCU(ModuleL23):
    """Test module Odin-10G-3S-6P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G3S6PCU] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.POdin10G3S6PCU, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-3S-6P-CU"""

@typing.final
class MOdin10G3S2PCU(ModuleL23):
    """Test module Odin-10G-3S-2P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G3S2PCU] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.POdin10G3S2PCU, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-3S-2P-CU"""
