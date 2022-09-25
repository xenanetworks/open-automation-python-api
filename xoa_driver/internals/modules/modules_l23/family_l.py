import typing
from xoa_driver import ports
from xoa_driver.internals.utils import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23

@typing.final
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
class MFreya800G1S1P_a(ModuleL23):
    """Test module Freya-800G-1S-1P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_a] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.PFreya800G1S1P_a, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Freya-800G-1S-1P[a]"""

@typing.final
class MFreya800G1S1P_b(ModuleL23):
    """Test module Freya-800G-1S-1P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_b] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.PFreya800G1S1P_b, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Freya-800G-1S-1P[b]"""

@typing.final
class MFreya800G1S1POSFP_a(ModuleL23):
    """Test module Freya-800G-1S-1P-OSFP[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_a] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.PFreya800G1S1POSFP_a, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Freya-800G-1S-1P-OSFP[a]"""


@typing.final
class MFreya800G4S1P_a(ModuleL23):
    """Test module Freya-800G-4S-1P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_a] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.PFreya800G4S1P_a, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Freya-800G-4S-1P[a]"""

@typing.final
class MFreya800G4S1POSFP_a(ModuleL23):
    """Test module Freya-800G-4S-1P-OSFP[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_a] = pm.PortsManager(
            conn=conn, 
            ports_type=ports.PFreya800G4S1POSFP_a, 
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Freya-800G-4S-1P-OSFP[a]"""