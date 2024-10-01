import typing
import asyncio
import functools
from typing_extensions import Self
from xoa_driver.internals.commands import (
    M_STATUS,
    M_UPGRADE,
    M_UPGRADEPROGRESS,
    M_CFPTYPE,
    M_COMMENT,
    M_CAPABILITIES,
    M_CLOCKPPB,
    M_TXCLOCKSOURCE_NEW,
    M_TXCLOCKSTATUS_NEW,
    M_EMULBYPASS,
    M_LATENCYMODE,
    M_REVISION,
    M_MEDIA,
    M_MEDIASUPPORT,
    M_TIMESYNC,
    M_CLOCKSYNCSTATUS,
    M_NAME,
    M_CFPCONFIGEXT,
    M_UPGRADEPAR,
    M_VERSIONSTR,
)

from xoa_driver.internals.hli_v1 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.state_storage import modules_state
from xoa_driver import ports
from xoa_driver.internals.hli_v1.modules.modules_l23.module_l23_base import MediaModule, CfpModule
from . import base_module as bm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli_v1.modules.modules_l23.module_l23_base import ModuleL23
    from . import __interfaces as m_itf


class ChTXClock:
    """
    Advanced timing feature (Chimera).
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.source = M_TXCLOCKSOURCE_NEW(conn, module_id)
        """
        The source that drives the TX clock rate of the ports on the test module.

        :type: M_TXCLOCKSOURCE_NEW
        """
        self.status = M_TXCLOCKSTATUS_NEW(conn, module_id)
        """
        TX clock status of the test module.

        :type: M_TXCLOCKSTATUS_NEW
        """


class ChCFP:
    """
    CFP test module (Chimera).
    """

    def __init__(self, conn: "itf.IConnection", module: typing.Union["ModuleL23", "ModuleChimera"]) -> None:
        self.type = M_CFPTYPE(conn, module.module_id)
        """
        The transceiver's CFP type currently inserted.

        :type: M_CFPTYPE
        """
        self.config = CfpModule(conn, module)
        """
        The CFP configuration of the test module.

        :type: CfpModule
        """


class ChUpgrade:
    """
    Upgrade test module (Chimera).
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M_UPGRADE(conn, module_id)
        """
        Start the upgrade progress of the test module.

        :type: M_UPGRADE
        """
        self.progress = M_UPGRADEPROGRESS(conn, module_id)
        """
        Upgrade progress status of the test module.

        :type: M_UPGRADEPROGRESS
        """
        self.start_parallel = M_UPGRADEPAR(conn, module_id)
        """
        Start the parallel upgrade progress of the test module.

        :type: M_UPGRADEPAR
        """


class ChTiming:
    """Test module timing and clock configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.source = M_TIMESYNC(conn, module_id)
        """Timing source of the test module.

        :type: M_TIMESYNC
        """

        self.clock_local_adjust = M_CLOCKPPB(conn, module_id)
        """Time adjustment controlling of the local clock of the test module, which drives the TX rate of the test ports.

        :type: M_CLOCKPPB
        """

        self.clock_sync_status = M_CLOCKSYNCSTATUS(conn, module_id)
        """Test module's clock sync status.

        :type: M_CLOCKSYNCSTATUS
        """


class ModuleChimera(bm.BaseModule["modules_state.ModuleLocalState"]):
    """
    This is a conceptual class of Chimera module.
    """

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self._local_states = modules_state.ModuleLocalState()

        self.tx_clock = ChTXClock(conn, self.module_id)
        """
        TX clock config (Chimera).

        :type: ChTXClock
        """

        self.timing = ChTiming(conn, self.module_id)
        """
        Timing config (Chimera).

        :type: ChTiming
        """

        self.cfp = ChCFP(conn, self)
        """
        CFP test module (Chimera).

        :type:  ChCFP
        """

        self.upgrade = ChUpgrade(conn, self.module_id)
        """
        Upgrade test module (Chimera).

        :type: ChUpgrade
        """

        self.capabilities = M_CAPABILITIES(conn, self.module_id)
        """
        Test module's capabilities.

        :type: M_CAPABILITIES
        """

        self.comment = M_COMMENT(conn, self.module_id)
        """
        Test module's description.

        :type: M_COMMENT
        """

        self.status = M_STATUS(conn, self.module_id)
        """
        Test module's status.

        :type: M_STATUS
        """

        self.clock_ppb = M_CLOCKPPB(conn, self.module_id)
        """
        Test module's local clock adjustment.

        :type: M_CLOCKPPB
        """

        self.emulator_bypass_mode = M_EMULBYPASS(conn, self.module_id)
        """
        Bypass mode of the Chimera module.

        :type: M_EMULBYPASS
        """

        self.latency_mode = M_LATENCYMODE(conn, self.module_id)
        """
        Latency mode of the Chimera module.

        :type: M_LATENCYMODE
        """

        self.revision = M_REVISION(conn, self.module_id)
        """Test module's model P/N name.

        :type: M_REVISION
        """

        self.version_str = M_VERSIONSTR(conn, self.module_id)
        """Module version number in the new format

        :type: M_VERSIONSTR
        """

        self.media = MediaModule(conn, self)
        """Test module's media type.

        :type: MediaModule
        """

        self.available_speeds = M_MEDIASUPPORT(conn, self.module_id)
        """Test module's available speeds.

        :type: M_MEDIASUPPORT
        """

        self.name = M_NAME(conn, self.module_id)
        """Test module's name.

        :type: M_NAME
        """

        self.ports: pm.PortsManager["ports.PortChimera"] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PortChimera,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """
        Port index manager of the Chimera module.

        :type: PortsManager
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
    Register a callback function to the event that the module's CFP type changes.
    """

    on_cfp_config_change = functools.partialmethod(utils.on_event, M_CFPCONFIGEXT)
    """
    Register a callback function to the event that the module's CFP configuration changes.
    """

    on_status_change = functools.partialmethod(utils.on_event, M_STATUS)
    """
    Register a callback function to the event that the module's model changes.
    """

    on_latency_mode_change = functools.partialmethod(utils.on_event, M_LATENCYMODE)
    """
    Register a callback function to the event that the module's latency mode changes.
    """

    on_media_change = functools.partialmethod(utils.on_event, M_MEDIA)
    """
    Register a callback to the event that the module's media and available speeds change.
    """

    on_media_support_change = functools.partialmethod(utils.on_event, M_MEDIASUPPORT)
    """
    Register a callback to the event that the module's supported media changes.
    """

    on_timing_source_change = functools.partialmethod(utils.on_event, M_TIMESYNC)
    """
    Register a callback to the event that the module's timesync mode changes.
    """

    on_timing_clock_local_adjust_change = functools.partialmethod(utils.on_event, M_CLOCKPPB)
    """
    Register a callback to the event that the module's clock adjustment ppb changes.
    """

    on_adv_timing_clock_tx_status_change = functools.partialmethod(utils.on_event, M_TXCLOCKSTATUS_NEW)
    """Register a callback to the event that the module's TX clock status changes."""

    on_adv_timing_clock_tx_source_change = functools.partialmethod(utils.on_event, M_TXCLOCKSOURCE_NEW)
    """Register a callback to the event that the module's clock that drives the port TX rates changes."""


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
        """Port index manager of Chi-100G-5S-2P

        :type: PortsManager
        """


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
        """Port index manager of Chi-100G-5S-2P[b]

        :type: PortsManager
        """


@typing.final
@revisions.register_chimera_module(rev="Chimera-40G-5S-2P")
class MChi40G2S2P(ModuleChimera):
    """Chimera module Chi-40G-2S-2P"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PChi40G2S2P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PChi40G2S2P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Chi-40G-2S-2P

        :type: PortsManager
        """
