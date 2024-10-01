import typing
from xoa_driver.v2 import ports
from xoa_driver.internals.hli_v2 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23
from xoa_driver.internals.commands import (
    M_CLOCKPPBSWEEP,
    M_CLOCKSWEEPSTATUS,
    M_HEALTH,
)


class MClockSweep:
    """Test module local clock sweep"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.config = M_CLOCKPPBSWEEP(conn, module_id)
        """Configure and control the module local clock sweep.
        Representation of M_CLOCKPPBSWEEP
        """

        self.status = M_CLOCKSWEEPSTATUS(conn, module_id)
        """Status of the module local clock sweep.
        Representation of M_CLOCKSWEEPSTATUS
        """

class MHealth:
    """Test module health"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.all = M_HEALTH(conn, module_id, [])
        """All module health information"""
        self.info = M_HEALTH(conn, module_id, [0])
        """Module identification information"""
        self.cage_insertion = M_HEALTH(conn, module_id, [1])
        """Module cage insertion counter"""

class ModuleFamilyL1(ModuleL23):
    """Test module Freya family"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self.clock_sweep = MClockSweep(conn, self.module_id)
        """Clock ppm sweep control"""

        self.health = MHealth(conn, self.module_id)
        """Module health information"""


#region Freya 1S 1P
        
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[a]")
class MFreya800G1S1P_a(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[a]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[b]")
class MFreya800G1S1P_b(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[a]")
class MFreya800G1S1POSFP_a(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P-OSFP[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[a]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[b]")
class MFreya800G1S1POSFP_b(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P-OSFP[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[b]"""


#endregion

#region Freya 1S 1P G1
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[a] G1")
class MFreya800G1S1P_a_g1(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[b] G1")
class MFreya800G1S1P_b_g1(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[b] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[a] G1")
class MFreya800G1S1POSFP_a_g1(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P-OSFP[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[b] G1")
class MFreya800G1S1POSFP_b_g1(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P-OSFP[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[b] G1"""


#endregion

#region Freya 1S 1P G2
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[a] G2")
class MFreya800G1S1P_a_g2(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[a] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[b] G2")
class MFreya800G1S1P_b_g2(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[b] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[a] G2")
class MFreya800G1S1POSFP_a_g2(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P-OSFP[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[a] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[b] G2")
class MFreya800G1S1POSFP_b_g2(ModuleFamilyL1):
    """Test module Freya-800G-1S-1P-OSFP[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[b] G2"""


#endregion

#region Freya 1S 4P
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[a]")
class MFreya800G4S1P_a(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[a]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[b]")
class MFreya800G4S1P_b(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[c]")
class MFreya800G4S1P_c(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[c]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[d]")
class MFreya800G4S1P_d(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[d]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[d]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[e]")
class MFreya800G4S1P_e(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[e]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[e]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[f]")
class MFreya800G4S1P_f(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[f]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[f]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[a]")
class MFreya800G4S1POSFP_a(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[a]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[b]")
class MFreya800G4S1POSFP_b(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[b]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[c]")
class MFreya800G4S1POSFP_c(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[c]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[d]")
class MFreya800G4S1POSFP_d(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[d]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[d]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[e]")
class MFreya800G4S1POSFP_e(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[e]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[e]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[f]")
class MFreya800G4S1POSFP_f(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[f]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[f]"""


#endregion

#region Freya 1S 4P G1

@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[a] G1")
class MFreya800G4S1P_a_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[b] G1")
class MFreya800G4S1P_b_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[b] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[c] G1")
class MFreya800G4S1P_c_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[c] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[c] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[d] G1")
class MFreya800G4S1P_d_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[d] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[d] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[e] G1")
class MFreya800G4S1P_e_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[e] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[e] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[f] G1")
class MFreya800G4S1P_f_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[f] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[f] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[a] G1")
class MFreya800G4S1POSFP_a_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[b] G1")
class MFreya800G4S1POSFP_b_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[b] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[c] G1")
class MFreya800G4S1POSFP_c_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[c] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[c] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[d] G1")
class MFreya800G4S1POSFP_d_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[d] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[d] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[e] G1")
class MFreya800G4S1POSFP_e_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[e] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[e] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[f] G1")
class MFreya800G4S1POSFP_f_g1(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[f] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[f] G1"""


#endregion

#region Freya 1S 4P G2        

@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[a] G2")
class MFreya800G4S1P_a_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[a] G2"""
        

@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[b] G2")
class MFreya800G4S1P_b_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[b] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[c] G2")
class MFreya800G4S1P_c_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[c] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[c] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[d] G2")
class MFreya800G4S1P_d_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[d] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[d] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[e] G2")
class MFreya800G4S1P_e_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[e] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[e] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[f] G2")
class MFreya800G4S1P_f_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P[f] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[f] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[a] G2")
class MFreya800G4S1POSFP_a_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[a] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[b] G2")
class MFreya800G4S1POSFP_b_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[b] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[c] G2")
class MFreya800G4S1POSFP_c_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[c] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[c] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[d] G2")
class MFreya800G4S1POSFP_d_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[d] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[d] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[e] G2")
class MFreya800G4S1POSFP_e_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[e] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[e] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[f] G2")
class MFreya800G4S1POSFP_f_g2(ModuleFamilyL1):
    """Test module Freya-800G-4S-1P-OSFP[f] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[f] G2"""




#endregion
