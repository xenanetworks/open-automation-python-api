from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4G_RAW_TEST_SCENARIO,
    P4G_RAW_PAYLOAD_TYPE,
    P4G_RAW_PAYLOAD_TOTAL_LEN,
    P4G_RAW_PAYLOAD,
    P4G_RAW_PAYLOAD_REPEAT_LEN,
    P4G_RAW_HAS_DOWNLOAD_REQ,
    P4G_RAW_CLOSE_CONN,
    P4G_RAW_UTILIZATION,
    P4G_RAW_DOWNLOAD_REQUEST,
    P4G_RAW_TX_DURING_RAMP,
    P4G_RAW_TX_TIME_OFFSET,
    P4G_RAW_BURSTY_TX,
    P4G_RAW_BURSTY_CONF,
    P4G_RAW_RX_PAYLOAD_LEN,
    P4G_RAW_REQUEST_REPEAT,
    P4G_RAW_CONN_INCARNATION,
    P4G_RAW_CONN_REPETITIONS,
    P4G_RAW_CONN_LIFETIME,
    P4G_APP_TRANSACTION_COUNTERS,
)


class GPayloadRaw:
    """Payload settings of Raw type of test application"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.type = P4G_RAW_PAYLOAD_TYPE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_TYPE`
        """
        self.total_length = P4G_RAW_PAYLOAD_TOTAL_LEN(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_TOTAL_LEN`
        """
        self.rx_length = P4G_RAW_RX_PAYLOAD_LEN(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_RX_PAYLOAD_LEN`
        """
        self.content = P4G_RAW_PAYLOAD(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD`
        """
        self.repeat_length = P4G_RAW_PAYLOAD_REPEAT_LEN(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_REPEAT_LEN`
        """


class GConnectionRaw:
    """Connection settings of Raw type of test application"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.incarnation = P4G_RAW_CONN_INCARNATION(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_INCARNATION`
        """
        self.repetitions = P4G_RAW_CONN_REPETITIONS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_REPETITIONS`
        """
        self.lifetime = P4G_RAW_CONN_LIFETIME(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_LIFETIME`
        """
        self.close_condition = P4G_RAW_CLOSE_CONN(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CLOSE_CONN`
        """


class GBurstyRaw:
    """Burst settings of Raw type of test application"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.transmission = P4G_RAW_BURSTY_TX(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_BURSTY_TX`
        """
        self.config = P4G_RAW_BURSTY_CONF(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_BURSTY_CONF`
        """


class GTransmitRaw:
    """Tranmission settings of Raw type of test application"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.during_ramp = P4G_RAW_TX_DURING_RAMP(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_TX_DURING_RAMP`
        """
        self.time_offset = P4G_RAW_TX_TIME_OFFSET(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_TX_TIME_OFFSET`
        """

class GDownloadRequestRaw:
    """Download request settings."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.server_must_wait = P4G_RAW_HAS_DOWNLOAD_REQ(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_HAS_DOWNLOAD_REQ`
        """
        self.transactions_number = P4G_RAW_REQUEST_REPEAT(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_REQUEST_REPEAT`
        """
        self.content = P4G_RAW_DOWNLOAD_REQUEST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_DOWNLOAD_REQUEST`
        """


class GCountersTransaction:
    """Transaction counters."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.transaction = P4G_APP_TRANSACTION_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_APP_TRANSACTION_COUNTERS`
        """


class GRaw:
    """Raw test application configuration."""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.test_scenario = P4G_RAW_TEST_SCENARIO(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_TEST_SCENARIO`
        """
        self.utilization = P4G_RAW_UTILIZATION(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_UTILIZATION`
        """
        
        self.download_request = GDownloadRequestRaw(conn, module_id, port_id, group_idx)
        """Download request."""
        self.payload = GPayloadRaw(conn, module_id, port_id, group_idx)
        """Payload configuration."""
        self.connection = GConnectionRaw(conn, module_id, port_id, group_idx)
        """Connection configuration."""
        self.bursty = GBurstyRaw(conn, module_id, port_id, group_idx)
        """Burst configuration."""
        self.tx = GTransmitRaw(conn, module_id, port_id, group_idx)
        """Transmit configuration."""

        self.transaction_counter = GCountersTransaction(conn, module_id, port_id, group_idx)
        """Transaction counters"""