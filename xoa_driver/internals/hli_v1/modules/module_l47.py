import asyncio
import functools
import typing
from typing_extensions import Self
from xoa_driver.internals.commands import (
    M_LICENSE_DEMO_INFO,
    M_LICENSE_MAINTENANCE_INFO,
    M_LICENSE_CWB_DETECTED,
    M_LICENSE_UPDATE,
    M_LICENSE_UPDATE_STATUS,
    M_LICENSE_LIST_BSON,
    M_LICENSE_ONLINE,
    # M4_INT, #TODO: need to implement
    # M4_STRING, #TODO: need to implement
    # M4_HEX, #TODO: need to implement
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
    # M4_REPLAY_FILE_INFO_BSON, #TODO: need to implement
    M4_REPLAY_FILE_DELETE,
    M4_CAPTURE_FILE_DELETE,
    M4E_MODE,
    M4E_RESERVE,
    M4_TLS_CIPHER_SUITES,
)
from xoa_driver.internals.hli_v1 import revisions
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.managers import ports_manager as pm
from xoa_driver.internals.state_storage import modules_state
from xoa_driver import ports
from . import base_module as bm
if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from . import __interfaces as m_itf


class License:
    """
    License management of a Vulcan tester.
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.demo_info = M_LICENSE_DEMO_INFO(conn, module_id)
        """
        Returns info about the demo status of the module.

        :type: M_LICENSE_DEMO_INFO
        """

        self.management_info = M_LICENSE_MAINTENANCE_INFO(conn, module_id)
        """
        Returns info about the maintenance license status for the module.

        :type: M_LICENSE_MAINTENANCE_INFO
        """

        self.clock_windback = M_LICENSE_CWB_DETECTED(conn, module_id)
        """
        Returns if clock-windback is detected. If clock-windback has been detected the chassis is locked and no reservations of ports can be performed.

        :type: M_LICENSE_CWB_DETECTED
        """

        self.update = M_LICENSE_UPDATE(conn, module_id)
        """
        Instructs the chassis to update its local license information.

        :type: M_LICENSE_UPDATE
        """

        self.update_status = M_LICENSE_UPDATE_STATUS(conn, module_id)
        """
        Returns the status of the latest license update operations.

        :type: M_LICENSE_UPDATE_STATUS
        """

        self.list_bson = M_LICENSE_LIST_BSON(conn, module_id)
        """
        Returns a list of locally stored licenses - formatted as a BSON document.

        :type: M_LICENSE_LIST_BSON
        """

        self.online_mode = M_LICENSE_ONLINE(conn, module_id)
        """
        Configures the chassis in online or offline mode.

        :type: M_LICENSE_ONLINE
        """


class CaptureParse:
    """
    Parse a captured pcap file.
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M4_REPLAY_PARSE_START(conn, module_id)
        """
        To start parsing an uploaded Capture File (in PCAP format) intended for use in a replay test scenario.

        :type: M4_REPLAY_PARSE_START
        """

        self.stop = M4_REPLAY_PARSE_STOP(conn, module_id)
        """
        To stop parsing an uploaded Capture File (in PCAP format) intended for use in a replay test scenario.

        :type: M4_REPLAY_PARSE_STOP
        """

        self.state = M4_REPLAY_PARSE_STATE(conn, module_id)
        """
        Returns the state of the parser.

        :type: M4_REPLAY_PARSE_STATE
        """

        self.parser_params = M4_REPLAY_PARSER_PARAMS(conn, module_id)
        """
        Configuration of parameters for the parsing of pcap files.

        :type: M4_REPLAY_PARSER_PARAMS
        """


class ReplayFile:
    """
    The pcap files to replay.
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.list_bson = M4_REPLAY_FILE_LIST_BSON(conn, module_id)
        """
        Returns a list of replay files formatted in BSON.

        :type: M4_REPLAY_FILE_LIST_BSON
        """
        self.list = M4_REPLAY_FILE_LIST(conn, module_id)
        """
        Returns a list of replay files.

        :type: M4_REPLAY_FILE_LIST
        """
        # self.info_bson = M4_REPLAY_FILE_INFO_BSON(conn, module_id)  # TODO: need to implement

        self.delete = M4_REPLAY_FILE_DELETE(conn, module_id)
        """
        Delete a replay file.

        :type: M4_REPLAY_FILE_DELETE
        """


class Replay:
    """
    PCAP replay settings and control.
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.file = ReplayFile(conn, module_id)
        """
        Replay file settings and control.

        :type: ReplayFile
        """


class Capture:
    """
    Captured pcap file settings and control.
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.size = M4_CAPTURE_SIZE(conn, module_id)
        """
        Specify whether to capture whole packets(large) or truncated packets.

        :type: M4_CAPTURE_SIZE
        """

        self.file_list_bson = M4_CAPTURE_FILE_LIST_BSON(conn, module_id)
        """
        Returns a list of captured files formatted as a BSON.

        :type: M4_CAPTURE_FILE_LIST_BSON
        """

        self.file_list = M4_CAPTURE_FILE_LIST(conn, module_id)
        """
        Returns a list of captured files.

        :type: M4_CAPTURE_FILE_LIST
        """

        self.file_delete = M4_CAPTURE_FILE_DELETE(conn, module_id)
        """
        Delete a captured file.

        :type: M4_CAPTURE_FILE_DELETE
        """

        self.parse = CaptureParse(conn, module_id)
        """
        Capture file parser settings.

        :type: CaptureParse
        """


class PacketEngine:
    """
    Packet engine.
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.license_info = M4_LICENSE_INFO(conn, module_id)
        """
        Returns the number of available and free PE licenses.

        :type: M4_LICENSE_INFO
        """

        self.reserve = M4E_RESERVE(conn, module_id)
        """
        Reserve a number of PEs so they later can be assigned to specific ports.

        :type: M4E_RESERVE
        """

        self.mode = M4E_MODE(conn, module_id)
        """
        Select resource allocation mode.

        :type: M4E_MODE
        """


class ModuleSystem:
    """
    L47 module info.
    """

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.id = M4_SYSTEMID(conn, module_id)
        """
        The system identifier of the module.

        :type: M4_SYSTEMID
        """

        self.status = M4_SYSTEM_STATUS(conn, module_id)
        """
        The module system status in a text string.

        :type: M4_SYSTEM_STATUS
        """

        self.time = M4_SYSTEM_TIME(conn, module_id)
        """
        The module system time in UTC.
        :type: M4_SYSTEM_TIME
        """


@revisions.register_vulcan_module(rev="Xena L47 Module")
class ModuleL47(bm.BaseModule["modules_state.ModuleLocalState"]):
    """
    This is a conceptual class of L47 test module on a Vulcan tester.
    """

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self._local_states = modules_state.ModuleLocalState()

        self.version_number = M4_VERSIONNO(conn, self.module_id)
        """
        Version string containing a combination of information regarding the software version and the build environment. The first part of the string is the software build version.

        :type: M4_VERSIONNO
        """

        self.compatible_client_version = M4_COMPATIBLE_CLIENT_VERSION(conn, self.module_id)
        """
        The recommended and required VulcanMananger client version.

        :type: M4_COMPATIBLE_CLIENT_VERSION
        """

        self.time = M4_TIME(conn, self.module_id)
        """
        The module time in millisecond.

        :type: M4_TIME
        """

        self.tls_cipher = M4_TLS_CIPHER_SUITES(conn, self.module_id)
        """
        The list of supported TLS Cipher Suites.

        :type: M4_TLS_CIPHER_SUITES
        """

        self.memory_info = M4_MEM_INFO(conn, self.module_id)  # Not sure if suppose to be here, maybe under ModuleSystem
        """
        The system memory information.

        :type: M4_MEM_INFO
        """

        self.module_system = ModuleSystem(conn, self.module_id)
        """L47 module info.

        :type: ModuleSystem
        """

        self.license = License(conn, self.module_id)
        """L47 license management.

        :type: License
        """

        self.replay = Replay(conn, self.module_id)
        """L47 pcap replay.

        :type: Replay
        """

        self.capture = Capture(conn, self.module_id)
        """L47 capture to pcap files.

        :type: Capture
        """

        self.packet_engine = PacketEngine(conn, self.module_id)
        """L47 packet engine.

        :type: ~xoa_driver.internals.hli_v1.modules.module_l47.PacketEngine
        """

        self.ports: pm.PortsManager[ports.PortL47] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PortL47,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """
        L47 Port index manager of this test module.

        :type: PortsManager
        """

    @property
    def info(self) -> modules_state.ModuleLocalState:
        """Return the module's local state

        :return: the module's local state
        :rtype: ModuleLocalState
        """

        return self._local_states

    async def _setup(self) -> Self:
        await asyncio.gather(
            self._local_states.initiate(self),
            self.ports.fill()
        )
        self._local_states.register_subscriptions(self)
        return self

    on_license_demo_info_change = functools.partialmethod(utils.on_event, M_LICENSE_DEMO_INFO)
    """Register a callback to the event that the module's demo license info changes."""

    on_license_maintenance_info_change = functools.partialmethod(utils.on_event, M_LICENSE_MAINTENANCE_INFO)
    """Register a callback to the event that the module's maintenance license info changes."""

    on_replay_parse_state_change = functools.partialmethod(utils.on_event, M4_REPLAY_PARSE_STATE)
    """Register a callback to the event that the module's parsing state of a captured pcap file changes."""

    on_license_info_change = functools.partialmethod(utils.on_event, M4_LICENSE_INFO)
    """Register a callback to the event that the module's L47 license info changes."""
