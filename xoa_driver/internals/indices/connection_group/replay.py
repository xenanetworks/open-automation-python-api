from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4G_REPLAY_FILE_INDICES,
    P4G_REPLAY_FILE_NAME,
    P4G_REPLAY_FILE_CLEAR,
    P4G_REPLAY_UTILIZATION,
    P4G_REPLAY_USER_INCARNATION,
    P4G_REPLAY_USER_REPETITIONS,
    P4G_APP_REPLAY_COUNTERS,
    # P4G_REPLAY_SCHEDULING, # TODO: need to implment
    # P4G_REPLAY_SYNCHRONIZATION, # TODO: need to implment
)

class GFilesReplay:
    """PCAP replay file configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__group_idx = group_idx
        self.indices = P4G_REPLAY_FILE_INDICES(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_FILE_INDICES`
        """

    def name(self, replay_file_idx: int) -> "P4G_REPLAY_FILE_NAME": # TODO: Not sure about function name
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_FILE_NAME`
        """
        return P4G_REPLAY_FILE_NAME(
            self.__conn, 
            self.__module_id, 
            self.__port_id, 
            self.__group_idx,
            replay_file_idx
        )

    async def clear_index(self, replay_file_idx: int) -> None:
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_FILE_CLEAR`
        """
        await P4G_REPLAY_FILE_CLEAR(
            self.__conn, 
            self.__module_id, 
            self.__port_id,
            replay_file_idx
        ).set()

class GUserReplay:
    """PCAP replay user configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.incarnation = P4G_REPLAY_USER_INCARNATION(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_USER_INCARNATION`
        """
        self.repetitions = P4G_REPLAY_USER_REPETITIONS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_USER_REPETITIONS`
        """


class GCounters:
    """PCAP replay counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.replay = P4G_APP_REPLAY_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_APP_REPLAY_COUNTERS`
        """


class GReplay:
    """PCAP replay configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.utilization = P4G_REPLAY_UTILIZATION(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_UTILIZATION`
        """
        # self.scheduling = P4G_REPLAY_SCHEDULING(conn, module_id, port_id, group_idx)
        # self.synchronization = P4G_REPLAY_SYNCHRONIZATION(conn, module_id, port_id, group_idx)
        self.files = GFilesReplay(conn, module_id, port_id, group_idx)
        """PCAP replay file configuration"""
        self.user = GUserReplay(conn, module_id, port_id, group_idx)
        """PCAP replay user configuration"""
        self.counters = GCounters(conn, module_id, port_id, group_idx)
        """PCAP replay counters"""

