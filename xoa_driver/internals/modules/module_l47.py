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
        self.management_info = M_LICENSE_MAINTENANCE_INFO(conn, module_id)
        self.clock_windback = M_LICENSE_CWB_DETECTED(conn, module_id)
        self.update = M_LICENSE_UPDATE(conn, module_id)
        self.update_status = M_LICENSE_UPDATE_STATUS(conn, module_id)
        self.list_bson = M_LICENSE_LIST_BSON(conn, module_id)
        self.online_mode = M_LICENSE_ONLINE(conn, module_id)


class CaptureParse:
    """Parse a captured pcap file"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M4_REPLAY_PARSE_START(conn, module_id)
        self.stop = M4_REPLAY_PARSE_STOP(conn, module_id)
        self.state = M4_REPLAY_PARSE_STATE(conn, module_id)
        self.parser_params = M4_REPLAY_PARSER_PARAMS(conn, module_id)


class ReplayFile:
    """The pcap files to replay"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.list_bson = M4_REPLAY_FILE_LIST_BSON(conn, module_id)
        self.list = M4_REPLAY_FILE_LIST(conn, module_id)
        # self.info_bson = M4_REPLAY_FILE_INFO_BSON(conn, module_id) # TODO: need to implement
        self.delete = M4_REPLAY_FILE_DELETE(conn, module_id)


class Replay:
    """PCAP replay"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.file = ReplayFile(conn, module_id)


class Capture:
    """Captured pcap file"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.size = M4_CAPTURE_SIZE(conn, module_id)
        self.file_list_bson = M4_CAPTURE_FILE_LIST_BSON(conn, module_id)
        self.file_list = M4_CAPTURE_FILE_LIST(conn, module_id)
        self.file_delete = M4_CAPTURE_FILE_DELETE(conn, module_id)
        self.parse = CaptureParse(conn, module_id)


class PacketEngine:
    """Packet engine"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.license_info = M4_LICENSE_INFO(conn, module_id)
        self.reserve = M4E_RESERVE(conn, module_id)
        self.mode = M4E_MODE(conn, module_id)


class ModuleSystem:
    """L47 module info"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.id = M4_SYSTEMID(conn, module_id)
        self.status = M4_SYSTEM_STATUS(conn, module_id)
        self.time = M4_SYSTEM_TIME(conn, module_id)

class ModuleL47(bm.BaseModule):
    """
    Representation of a Vulcan module on physical tester.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self.version_number = M4_VERSIONNO(conn, self.module_id)
        self.compatible_client_version = M4_COMPATIBLE_CLIENT_VERSION(conn, self.module_id)
        self.time = M4_TIME(conn, self.module_id)
        self.tls_chiper = M4_TLS_CIPHER_SUITES(conn, self.module_id)
        self.memory_info = M4_MEM_INFO(conn, self.module_id) # Not sure if suppose to be here, maybe under ModuleSystem

        self.module_system = ModuleSystem(conn, self.module_id)
        self.license = License(conn, self.module_id)
        self.replay = Replay(conn, self.module_id)
        self.capture = Capture(conn, self.module_id)
        self.packet_engine = PacketEngine(conn, self.module_id)

        self.ports: pm.PortsManager[PortL47] = pm.PortsManager(
            conn=conn,
            ports_type=PortL47,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Subset of avaliable ports `xoa_driver.internals.utils.ports_manager.PortsManager`"""

    async def _setup(self):
        await asyncio.gather(
            super()._setup(),
            self.ports.fill()
        )
        return self

    on_license_demo_info_change = functools.partialmethod(utils.on_event, M_LICENSE_DEMO_INFO)
    """Demo license info change event."""

    on_license_maintenance_info_change = functools.partialmethod(utils.on_event, M_LICENSE_MAINTENANCE_INFO)
    """Maintenane license info change event."""

    on_replay_parse_state_change = functools.partialmethod(utils.on_event, M4_REPLAY_PARSE_STATE)
    """Parse state of a captured pcap file change event."""

    on_license_info_change = functools.partialmethod(utils.on_event, M4_LICENSE_INFO)
    """L47 license info change event."""