import asyncio
import functools
import typing
from xoa_driver.internals.core.commands import (
    M_LICENSE_DEMO_INFO,
    M_LICENSE_MAINTENANCE_INFO,
    M_LICENSE_CWB_DETECTED,
    M_LICENSE_UPDATE,
    M_LICENSE_UPDATE_STATUS,
    M_LICENSE_LIST_BSON,
    M_LICENSE_ONLINE,
    # M4_INT, # TODO: need to implment
    # M4_STRING, # TODO: need to implment
    # M4_HEX, # TODO: need to implment
    M4_SYSTEMID,
    M4_VERSIONNO,
    M4_SYSTEM_STATUS,
    M4_COMPATIBLE_CLIENT_VERSION,
    M4_TIME,
    M4_SYSTEM_TIME,
    M4_MEM_INFO,
    M4_CAPTURE_SIZE,
    M4_LICENSE_INFO,
    M4_REPLAY_PARSE_START,
    M4_REPLAY_PARSE_STOP,
    M4_REPLAY_PARSE_STATE,
    M4_REPLAY_PARSER_PARAMS,
    M4_REPLAY_FILE_LIST_BSON,
    M4_REPLAY_FILE_LIST,
    M4_CAPTURE_FILE_LIST_BSON,
    M4_CAPTURE_FILE_LIST,
    # M4_REPLAY_FILE_INFO_BSON, # TODO: need to implment
    M4_REPLAY_FILE_DELETE,
    M4_CAPTURE_FILE_DELETE,
    M4E_MODE,
    M4E_RESERVE,
    M4_TLS_CIPHER_SUITES,
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils import ports_manager as pm
from xoa_driver.ports import PortL47
from . import base_module as bm
if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from . import __interfaces as m_itf


class License:
    """License management for Vulcan"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.demo_info = M_LICENSE_DEMO_INFO(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_LICENSE_DEMO_INFO`
        """
        self.management_info = M_LICENSE_MAINTENANCE_INFO(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_LICENSE_MAINTENANCE_INFO`
        """
        self.clock_windback = M_LICENSE_CWB_DETECTED(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_LICENSE_CWB_DETECTED`
        """
        self.update = M_LICENSE_UPDATE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_LICENSE_UPDATE`
        """
        self.update_status = M_LICENSE_UPDATE_STATUS(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_LICENSE_UPDATE_STATUS`
        """
        self.list_bson = M_LICENSE_LIST_BSON(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_LICENSE_LIST_BSON`
        """
        self.online_mode = M_LICENSE_ONLINE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m_commands.M_LICENSE_ONLINE`
        """


class CaptureParse:
    """Parse a captured pcap file"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M4_REPLAY_PARSE_START(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_REPLAY_PARSE_START`
        """
        self.stop = M4_REPLAY_PARSE_STOP(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_REPLAY_PARSE_STOP`
        """
        self.state = M4_REPLAY_PARSE_STATE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_REPLAY_PARSE_STATE`
        """
        self.parser_params = M4_REPLAY_PARSER_PARAMS(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_REPLAY_PARSER_PARAMS`
        """


class ReplayFile:
    """The pcap files to replay"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.list_bson = M4_REPLAY_FILE_LIST_BSON(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_REPLAY_FILE_LIST_BSON`
        """
        self.list = M4_REPLAY_FILE_LIST(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_REPLAY_FILE_LIST`
        """
        # self.info_bson = M4_REPLAY_FILE_INFO_BSON(conn, module_id) # TODO: need to implement
        self.delete = M4_REPLAY_FILE_DELETE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_REPLAY_FILE_DELETE`
        """


class Replay:
    """PCAP replay"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.file = ReplayFile(conn, module_id)
        """The pcap file to replay."""


class Capture:
    """Captured pcap file"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.size = M4_CAPTURE_SIZE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_CAPTURE_SIZE`
        """
        self.file_list_bson = M4_CAPTURE_FILE_LIST_BSON(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_CAPTURE_FILE_LIST_BSON`
        """
        self.file_list = M4_CAPTURE_FILE_LIST(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_CAPTURE_FILE_LIST`
        """
        self.file_delete = M4_CAPTURE_FILE_DELETE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_CAPTURE_FILE_DELETE`
        """
        self.parse = CaptureParse(conn, module_id)
        """Parse a captured pcap file."""


class PacketEngine:
    """Packet engine"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.license_info = M4_LICENSE_INFO(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_LICENSE_INFO`
        """
        self.reserve = M4E_RESERVE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4e_commands.M4E_RESERVE`
        """
        self.mode = M4E_MODE(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4e_commands.M4E_MODE`
        """


class ModuleSystem:
    """L47 module info"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.id = M4_SYSTEMID(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M_COMMEM4_SYSTEMIDNT`
        """
        self.status = M4_SYSTEM_STATUS(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_SYSTEM_STATUS`
        """
        self.time = M4_SYSTEM_TIME(conn, module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_SYSTEM_TIME`
        """

class ModuleL47(bm.BaseModule):
    """
    Representation of a L47 test module on a physical tester.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self.version_number = M4_VERSIONNO(conn, self.module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_VERSIONNO`
        """
        self.compatible_client_version = M4_COMPATIBLE_CLIENT_VERSION(conn, self.module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_COMPATIBLE_CLIENT_VERSION`
        """
        self.time = M4_TIME(conn, self.module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_TIME`
        """
        self.tls_chiper = M4_TLS_CIPHER_SUITES(conn, self.module_id)
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_TLS_CIPHER_SUITES`
        """
        self.memory_info = M4_MEM_INFO(conn, self.module_id) # Not sure if suppose to be here, maybe under ModuleSystem
        """Representation of :class:`~xoa_driver.internals.core.commands.m4_commands.M4_MEM_INFO`
        """

        self.module_system = ModuleSystem(conn, self.module_id)
        """L47 module info."""
        self.license = License(conn, self.module_id)
        """L47 license management."""
        self.replay = Replay(conn, self.module_id)
        """L47 pcap replay."""
        self.capture = Capture(conn, self.module_id)
        """L47 capture to pcap files."""
        self.packet_engine = PacketEngine(conn, self.module_id)
        """L47 packet engine."""

        self.ports: pm.PortsManager[PortL47] = pm.PortsManager(
            conn=conn,
            ports_type=PortL47,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """L47 Port index manager of this test module."""

    async def _setup(self):
        await asyncio.gather(
            super()._setup(),
            self.ports.fill()
        )
        return self

    on_license_demo_info_change = functools.partialmethod(utils.on_event, M_LICENSE_DEMO_INFO)
    """Register a callback to the event that the module's demo license info changes."""

    on_license_maintenance_info_change = functools.partialmethod(utils.on_event, M_LICENSE_MAINTENANCE_INFO)
    """Register a callback to the event that the module's maintenane license info changes."""

    on_replay_parse_state_change = functools.partialmethod(utils.on_event, M4_REPLAY_PARSE_STATE)
    """Register a callback to the event that the module's parsing state of a captured pcap file changes."""

    on_license_info_change = functools.partialmethod(utils.on_event, M4_LICENSE_INFO)
    """Register a callback to the event that the module's L47 license info changes."""