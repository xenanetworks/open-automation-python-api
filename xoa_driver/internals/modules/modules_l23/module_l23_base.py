import asyncio
import functools
from typing import (
    TYPE_CHECKING,
    Optional,
)
from xoa_driver.internals.core.commands import (
    M_STATUS,
    M_UPGRADE,
    M_UPGRADEPROGRESS,
    M_TIMESYNC,
    M_CFPTYPE,
    M_CFPCONFIG,
    M_COMMENT,
    M_TIMEADJUSTMENT,
    M_CAPABILITIES,
    M_MEDIASUPPORT,
    M_FPGAREIMAGE,
    M_MULTIUSER,
    M_CFPCONFIGEXT,
    M_CLOCKPPB,
    M_SMAINPUT,
    M_SMAOUTPUT,
    M_SMASTATUS,
    M_NAME,
    M_REVISION,
    M_MEDIA,
    M_CLOCKSYNCSTATUS,
    M_TXCLOCKSOURCE_NEW,
    M_TXCLOCKSTATUS_NEW,
    M_TXCLOCKFILTER_NEW,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.utils import ports_manager as pm

from .. import base_module as bm
from .. import __interfaces as m_itf
from xoa_driver.internals.state_storage import modules_state

class TXClock:
    """Advanced timing clock"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.source = M_TXCLOCKSOURCE_NEW(conn, module_id)
        """The source that drives the TX clock rate of the ports on the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_TXCLOCKSOURCE_NEW`
        """

        self.status = M_TXCLOCKSTATUS_NEW(conn, module_id)
        """TX clock status of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_TXCLOCKSTATUS_NEW`
        """

        self.filter = M_TXCLOCKFILTER_NEW(conn, module_id)
        """Loop bandwidth on the TX clock filter of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_TXCLOCKFILTER_NEW`
        """


class SMA:
    """SMA connector"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.input = M_SMAINPUT(conn, module_id)
        """SMA input of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_SMAINPUT`
        """

        self.output = M_SMAOUTPUT(conn, module_id)
        """SMA output of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_SMAOUTPUT`
        """

        self.status = M_SMASTATUS(conn, module_id)
        """SMA input status of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_SMASTATUS`
        """


class CFP:
    """Test module CFP"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.type = M_CFPTYPE(conn, module_id)
        """The transceiver's CFP type currently inserted.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPTYPE`
        """
        self.config = M_CFPCONFIG(conn, module_id)
        """The CFP configuration of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIG`
        """
        self.config_extended = M_CFPCONFIGEXT(conn, module_id)
        """The extended CFP configuration of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIGEXT`
        """


class MTime:
    """Test module time"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.sync = M_TIMESYNC(conn, module_id)
        """Time sync controlling of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_TIMESYNC`
        """
        self.adjustment = M_TIMEADJUSTMENT(conn, module_id)
        """Time adjustment controlling of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_TIMEADJUSTMENT`
        """

class MUpgrade:
    """Test module upgrade"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M_UPGRADE(conn, module_id)
        """Start the upgrade progress of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_UPGRADE`
        """
        self.progress = M_UPGRADEPROGRESS(conn, module_id)
        """Upgrade progress status of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_UPGRADEPROGRESS`
        """

class ModuleL23(bm.BaseModule["modules_state.ModuleL23LocalState"]):
    """
    Representation of a L23 test module on a physical tester.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.name = M_NAME(conn, self.module_id)
        """Test module's name.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_NAME`
        """

        self.comment = M_COMMENT(conn, self.module_id)
        """Test module's description.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_COMMENT`
        """

        self.status = M_STATUS(conn, self.module_id)
        """Test module's status.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_STATUS`
        """

        self.media = M_MEDIA(conn, self.module_id)
        """Test module's media configuration.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_MEDIA`
        """

        self.revision = M_REVISION(conn, self.module_id)
        """Test module's model P/N name.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_REVISION`
        """

        self.clock_ppb = M_CLOCKPPB(conn, self.module_id)
        """Small adjustment to the local clock of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CLOCKPPB`
        """

        self.multiuser = M_MULTIUSER(conn, self.module_id)
        """If multiple users are allowed to control the same test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_MULTIUSER`
        """

        self.reload_fpga_image = M_FPGAREIMAGE(conn, self.module_id)
        """Reload the FPGA image of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_FPGAREIMAGE`
        """

        self.capabilities = M_CAPABILITIES(conn, self.module_id)
        """Test module's capabilities.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CAPABILITIES`
        """

        self.clock_sync_status = M_CLOCKSYNCSTATUS(conn, self.module_id)
        """Test module's clock sync status.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CLOCKSYNCSTATUS`
        """

        self.time = MTime(conn, self.module_id)
        """Test module's time settings."""

        self.tx_clock = TXClock(conn, self.module_id)
        """Test module's advanced timing clock."""

        self.sma = SMA(conn, self.module_id)
        """Test module's SMA connector."""

        self.cfp = CFP(conn, self.module_id)
        """Test module's CFP """

        self.upgrade = MUpgrade(conn, self.module_id)
        """Test module's upgrade."""

        self._local_states = modules_state.ModuleL23LocalState()
        self.ports: Optional[pm.PortsManager] = None
        """L23 port index manager of the test module."""

    async def _setup(self):
        m_support_resp, *_ = await asyncio.gather(
            M_MEDIASUPPORT(self._conn, self.module_id).get(),
            super()._setup(),
        )
        self._local_states.media_info_list = m_support_resp.media_info_list # type: ignore
        if self.ports is None:
            raise NotImplementedError("Ports manager type are not defined.") # Maybe can be better solution then this...
        await self.ports.fill()
        return self

    def _register_subscriptions(self) -> None:
        super()._register_subscriptions()
        self._conn.subscribe(M_MEDIASUPPORT, utils.Update(self._local_states, "media_info_list", "media_info_list", self._check_identity))

    on_cfp_type_change = functools.partialmethod(utils.on_event, M_CFPTYPE)
    """Register a callback to the event that the module's CFP type changes."""

    on_cfp_config_change = functools.partialmethod(utils.on_event, M_CFPCONFIG)
    """Register a callback to the event that the module's CFP configuration changes."""

    on_cfp_config_extended_change = functools.partialmethod(utils.on_event, M_CFPCONFIGEXT)
    """Register a callback to the event that the module's CFP extended configuration changes."""

    on_tx_clock_status_change = functools.partialmethod(utils.on_event, M_TXCLOCKSTATUS_NEW)
    """Register a callback to the event that the module's TX clock status changes."""

    on_status_change = functools.partialmethod(utils.on_event, M_STATUS)
    """Register a callback to the event that the module's status changes."""

    on_revision_change = functools.partialmethod(utils.on_event, M_REVISION)
    """Register a callback to the event that the module's model type changes."""

    on_name_change = functools.partialmethod(utils.on_event, M_NAME)
    """Register a callback to the event that the module's name changes."""

    on_sma_status_change = functools.partialmethod(utils.on_event, M_SMASTATUS)
    """Register a callback to the event that the module's SMA status changes."""

    on_media_support_change = functools.partialmethod(utils.on_event, M_MEDIASUPPORT)
    """Register a callback to the event that the module's supported media changes."""

    on_media_change = functools.partialmethod(utils.on_event, M_MEDIA)
    """Register a callback to the event that the module's media and available speeds change."""

    on_comment_change = functools.partialmethod(utils.on_event, M_COMMENT)
    """Register a callback to the event that the module's description changes."""

    on_time_sync_change = functools.partialmethod(utils.on_event, M_TIMESYNC)
    """Register a callback to the event that the module's timesync mode changes."""

    on_clock_ppb_change = functools.partialmethod(utils.on_event, M_CLOCKPPB)
    """Register a callback to the event that the module's clock adjustment ppb changes."""

    on_sma_input_change = functools.partialmethod(utils.on_event, M_SMAINPUT)
    """Register a callback to the event that the module's SMA input function changes."""

    on_sma_output_change = functools.partialmethod(utils.on_event, M_SMAOUTPUT)
    """Register a callback to the event that the module's SMA output function changes."""

    on_tx_clock_source_change = functools.partialmethod(utils.on_event, M_TXCLOCKSOURCE_NEW)
    """Register a callback to the event that the module's clock that drives the port TX rates changes."""

    on_tx_clock_sfilter_change = functools.partialmethod(utils.on_event, M_TXCLOCKFILTER_NEW)
    """Register a callback to the event that the module's loop bandwidth on the TX clock filter changes."""

