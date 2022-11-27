import typing
import asyncio
import functools
from typing import TYPE_CHECKING
from typing_extensions import Self
from xoa_driver.internals.core.commands import (
    M_STATUS,
    M_UPGRADE,
    M_UPGRADEPROGRESS,
    M_CFPTYPE,
    M_CFPCONFIG,
    M_COMMENT,
    M_CAPABILITIES,
    M_CLOCKPPB,
    M_TXCLOCKSOURCE_NEW,
    M_TXCLOCKSTATUS_NEW,
    M_EMULBYPASS,
    M_LATENCYMODE,
)

from xoa_driver.internals.hli_v2 import revisions
from xoa_driver.internals.utils import ports_manager as pm
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.state_storage import modules_state
from xoa_driver.v2 import ports
from . import base_module as bm
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from . import __interfaces as m_itf


class ChTXClock:
    """
    Advanced timing feature (Chimera).
    """
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.source = M_TXCLOCKSOURCE_NEW(conn, module_id)
        """
        The source that drives the TX clock rate of the ports on the test module.
        Representation of M_TXCLOCKSOURCE_NEW
        """
        self.status = M_TXCLOCKSTATUS_NEW(conn, module_id)
        """
        TX clock status of the test module.
        Representation of M_TXCLOCKSTATUS_NEW
        """


class ChCFP:
    """
    CFP test module (Chimera).
    """
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.type = M_CFPTYPE(conn, module_id)
        """
        The transceiver's CFP type currently inserted.
        Representation of M_CFPTYPE
        """
        self.config = M_CFPCONFIG(conn, module_id)
        """
        The CFP configuration of the test module.
        Representation of M_CFPCONFIG
        """


class ChUpgrade:
    """
    Upgrade test module (Chimera).
    """
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M_UPGRADE(conn, module_id)
        """
        Start the upgrade progress of the test module.
        Representation of M_UPGRADE
        """
        self.progress = M_UPGRADEPROGRESS(conn, module_id)
        """
        Upgrade progress status of the test module.
        Representation of M_UPGRADEPROGRESS
        """


class ChTiming:
    """Test module timing and clock configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:

        self.clock_local_adjust = M_CLOCKPPB(conn, module_id)
        """Time adjustment controlling of the local clock of the test module, which drives the TX rate of the test ports.
        Representation of M_CLOCKPPB
        """


class ChAdvancedTiming:
    """Advanced Timing config and control"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.clock = ChTXClock(conn, module_id)
        """Advanced timing clock config and status
        """


class ModuleChimera(bm.BaseModule["modules_state.ModuleLocalState"]):
    """
    Representation of a Chimera module on physical tester.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self._local_states = modules_state.ModuleLocalState()

        self.tx_clock = ChTXClock(conn, self.module_id)
        """
        Advanced timing feature (Chimera).
        """

        self.cfp = ChCFP(conn, self.module_id)
        """
        CFP test module (Chimera).
        """

        self.upgrade = ChUpgrade(conn, self.module_id)
        """
        Upgrade test module (Chimera).
        """

        self.capabilities = M_CAPABILITIES(conn, self.module_id)
        """
        Test module's capabilities.
        Representation of M_CAPABILITIES
        """

        self.comment = M_COMMENT(conn, self.module_id)
        """
        Test module's description.
        Representation of M_COMMENT
        """

        self.status = M_STATUS(conn, self.module_id)
        """
        Test module's status.
        Representation of M_STATUS
        """

        self.clock_ppb = M_CLOCKPPB(conn, self.module_id)
        """
        Test module's local clock adjustment.
        Representation of M_CLOCKPPB
        """

        self.emulator_bypass_mode = M_EMULBYPASS(conn, self.module_id)
        """
        Bypass mode of the Chimera module.
        Representation of M_EMULBYPASS
        """

        self.latency_mode = M_LATENCYMODE(conn, self.module_id)
        """
        Latency mode of the Chimera module.
        Representation of M_LATENCYMODE
        """

        self.timing = ChTiming(conn, self.module_id)
        """Test module's timing configuration."""

        self.bypass_mode = M_EMULBYPASS(conn, self.module_id)
        """
        Bypass mode of the Chimera module.
        Representation of M_EMULBYPASS
        """

        self.adv_timing = ChAdvancedTiming(conn, self.module_id)

        self.ports: pm.PortsManager["ports.PortChimera"] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PortChimera,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """
        Port index manager of the Chimera module.
        """

    @property
    def info(self) -> modules_state.ModuleLocalState:
        return self._local_states

    async def _setup(self) -> Self:
        await asyncio.gather(
            self._local_states.initiate(self),
            self.ports.fill()
        )
        self._local_states.register_subscriptions(self)
        return self

    on_cfp_type_change = functools.partialmethod(utils.on_event, M_CFPTYPE)
    """
    Register a callback to the event that the module's CFP type changes.
    """

    on_cfp_config_change = functools.partialmethod(utils.on_event, M_CFPCONFIG)
    """
    Register a callback to the event that the module's CFP configuration changes.
    """

    on_status_change = functools.partialmethod(utils.on_event, M_STATUS)
    """
    Register a callback to the event that the module's model changes.
    """

    on_latency_mode_change = functools.partialmethod(utils.on_event, M_LATENCYMODE)
    """
    Register a callback to the event that the module's latency mode changes.
    """


@typing.final
@revisions.register_chimera_module(rev="Chimera-100G-5S-2P")
class MChi100G5S2P(ModuleChimera):
    """Chimera module Chi-100G-5S-2P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PChi100G5S2P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PChi100G5S2P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Chi-100G-5S-2P"""


@typing.final
@revisions.register_chimera_module(rev="Chimera-100G-5S-2P[b]")
class MChi100G5S2P_b(ModuleChimera):
    """Chimera module Chi-100G-5S-2P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PChi100G5S2P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PChi100G5S2P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Chi-100G-5S-2P[b]"""


@typing.final
@revisions.register_chimera_module(rev="Chimera-40G-5S-2P")
class MChi40G5S2P(ModuleChimera):
    """Chimera module Chi-40G-5S-2P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PChi40G5S2P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PChi40G5S2P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Chi-40G-5S-2P"""
