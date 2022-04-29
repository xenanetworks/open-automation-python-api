import asyncio
import functools
from typing import TYPE_CHECKING
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
    # M_LATENCYMODE, # TODO: wait for val-90 to assign the correct command code
)

from xoa_driver.internals.utils import ports_manager as pm
from xoa_driver.internals.utils import attributes as utils
from xoa_driver import ports
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
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_TXCLOCKSOURCE_NEW`
        """
        self.status = M_TXCLOCKSTATUS_NEW(conn, module_id)
        """
        TX clock status of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_TXCLOCKSTATUS_NEW`
        """


class ChCFP:
    """
    CFP test module (Chimera).
    """
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.type = M_CFPTYPE(conn, module_id)
        """
        The transceiver's CFP type currently inserted.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPTYPE`
        """
        self.config = M_CFPCONFIG(conn, module_id)
        """
        The CFP configuration of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIG`
        """


class ChUpgrade:
    """
    Upgrade test module (Chimera).
    """
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M_UPGRADE(conn, module_id)
        """
        Start the upgrade progress of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_UPGRADE`
        """
        self.progress = M_UPGRADEPROGRESS(conn, module_id)
        """
        Upgrade progress status of the test module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_UPGRADEPROGRESS`
        """

class ModuleChimera(bm.BaseModule):
    """
    Representation of a Chimera module on physical tester.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
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
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CAPABILITIES`
        """

        self.comment = M_COMMENT(conn, self.module_id)
        """
        Test module's description.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_COMMENT`
        """

        self.status = M_STATUS(conn, self.module_id)
        """
        Test module's status.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_STATUS`
        """

        self.clock_ppb = M_CLOCKPPB(conn, self.module_id)
        """
        Test module's local clock adjustment.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_CLOCKPPB`
        """

        self.emulator_bypass_mode = M_EMULBYPASS(conn, self.module_id)
        """
        Bypass mode of the Chimera module.
        Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_EMULBYPASS`
        """

        self.ports: pm.PortsManager["ports.PortChimera"] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PortChimera,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """
        Port index manager of the Chimera module.
        """

    on_cfp_type_change = functools.partialmethod(utils.on_event, M_CFPTYPE)
    """
    Register a callback to the event that the module's CFP type changes.
    """

    on_cfp_config_change = functools.partialmethod(utils.on_event, M_CFPCONFIG)
    """
    Register a callback to the event that the module's CFP configuration changes.
    """

    on_model_change = functools.partialmethod(utils.on_event, M_STATUS)
    """
    Register a callback to the event that the module's model changes.
    """

    # on_latency_mode_change = functools.partialmethod(utils.on_event, M_LATENCYMODE)

    async def _setup(self):
        await asyncio.gather(
            super()._setup(),
            self.ports.fill()
        )
        return self