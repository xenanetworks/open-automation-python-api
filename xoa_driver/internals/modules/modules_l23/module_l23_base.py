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
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.source = M_TXCLOCKSOURCE_NEW(conn, module_id)
        self.status = M_TXCLOCKSTATUS_NEW(conn, module_id)
        self.filter = M_TXCLOCKFILTER_NEW(conn, module_id)


class SMA:
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.input = M_SMAINPUT(conn, module_id)
        self.output = M_SMAOUTPUT(conn, module_id)
        self.status = M_SMASTATUS(conn, module_id)


class CFP:
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.type = M_CFPTYPE(conn, module_id)
        self.config = M_CFPCONFIG(conn, module_id)
        self.config_extended = M_CFPCONFIGEXT(conn, module_id)


class MTime:
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.sync = M_TIMESYNC(conn, module_id)
        self.adjustment = M_TIMEADJUSTMENT(conn, module_id)

class MUpgrade:
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M_UPGRADE(conn, module_id)
        self.progress = M_UPGRADEPROGRESS(conn, module_id)

class ModuleL23(bm.BaseModule["modules_state.ModuleL23LocalState"]):
    """
    Representation of a Level23Module on genuine tester.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.name = M_NAME(conn, self.module_id)
        self.comment = M_COMMENT(conn, self.module_id)
        self.status = M_STATUS(conn, self.module_id)
        self.media = M_MEDIA(conn, self.module_id)
        self.revision = M_REVISION(conn, self.module_id)
        self.clock_ppb = M_CLOCKPPB(conn, self.module_id)
        self.multiuser = M_MULTIUSER(conn, self.module_id)
        self.reload_fpga_image = M_FPGAREIMAGE(conn, self.module_id)
        self.capabilities = M_CAPABILITIES(conn, self.module_id)
        self.clock_sync_status = M_CLOCKSYNCSTATUS(conn, self.module_id)

        self.time = MTime(conn, self.module_id)
        self.tx_clock = TXClock(conn, self.module_id)
        self.sma = SMA(conn, self.module_id)
        self.cfp = CFP(conn, self.module_id)
        self.upgrade = MUpgrade(conn, self.module_id)

        self._local_states = modules_state.ModuleL23LocalState()
        self.ports: Optional[pm.PortsManager] = None
        """Subset of avaliable ports `xoa_driver.internals.utils.ports_manager.PortsManager`"""

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
    on_cfp_config_change = functools.partialmethod(utils.on_event, M_CFPCONFIG)
    on_cfp_config_extended_change = functools.partialmethod(utils.on_event, M_CFPCONFIGEXT)
    on_tx_clock_status_change = functools.partialmethod(utils.on_event, M_TXCLOCKSTATUS_NEW)
    on_status_change = functools.partialmethod(utils.on_event, M_STATUS)
    on_revision_change = functools.partialmethod(utils.on_event, M_REVISION)
    on_name_change = functools.partialmethod(utils.on_event, M_NAME)
    on_sma_status_change = functools.partialmethod(utils.on_event, M_SMASTATUS)
    on_media_support_change = functools.partialmethod(utils.on_event, M_MEDIASUPPORT)
    on_media_change = functools.partialmethod(utils.on_event, M_MEDIA)
    on_comment_change = functools.partialmethod(utils.on_event, M_COMMENT)
    on_time_sync_change = functools.partialmethod(utils.on_event, M_TIMESYNC)
    on_clock_ppb_change = functools.partialmethod(utils.on_event, M_CLOCKPPB)
    on_sma_input_change = functools.partialmethod(utils.on_event, M_SMAINPUT)
    on_sma_output_change = functools.partialmethod(utils.on_event, M_SMAOUTPUT)
    on_tx_clock_source_change = functools.partialmethod(utils.on_event, M_TXCLOCKSOURCE_NEW)
    on_tx_clock_sfilter_change = functools.partialmethod(utils.on_event, M_TXCLOCKFILTER_NEW)

