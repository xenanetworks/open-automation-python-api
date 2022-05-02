from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.core.commands import (
    P4G_TLS_ENABLE,
    P4G_TLS_CIPHER_SUITES,
    P4G_TLS_MAX_RECORD_SIZE,
    P4G_TLS_CERTIFICATE_FILENAME,
    P4G_TLS_PRIVATE_KEY_FILENAME,
    P4G_TLS_DHPARAMS_FILENAME,
    P4G_TLS_CLOSE_NOTIFY,
    P4G_TLS_ALERT_WARNING_COUNTERS,
    P4G_TLS_ALERT_FATAL_COUNTERS,
    P4G_TLS_STATE_CURRENT,
    P4G_TLS_STATE_TOTAL,
    P4G_TLS_STATE_RATE,
    P4G_TLS_RX_PAYLOAD_COUNTERS,
    P4G_TLS_TX_PAYLOAD_COUNTERS,
    P4G_TLS_RX_PAYLOAD_BYTES_HIST,
    P4G_TLS_TX_PAYLOAD_BYTES_HIST,
    P4G_TLS_HANDSHAKE_HIST,
    P4G_TLS_SERVER_NAME,
    P4G_TLS_PROTOCOL_VER,
    P4G_TLS_MIN_REQ_PROTOCOL_VER,
)

class GCountersTlsState:
    """TLS state counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.current = P4G_TLS_STATE_CURRENT(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_STATE_CURRENT`
        """
        self.total = P4G_TLS_STATE_TOTAL(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_STATE_TOTAL`
        """
        self.rate = P4G_TLS_STATE_RATE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_STATE_RATE`
        """


class GCountersTlsAlert:
    """TLS alert counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.warning = P4G_TLS_ALERT_WARNING_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_ALERT_WARNING_COUNTERS`
        """
        self.fatal = P4G_TLS_ALERT_FATAL_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_ALERT_FATAL_COUNTERS`
        """


class GCountersTlsPayload:
    """TLS payload counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_TLS_RX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_RX_PAYLOAD_COUNTERS`
        """
        self.tx = P4G_TLS_TX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_TX_PAYLOAD_COUNTERS`
        """


class GCountersTls:
    """TLS counters"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.alert = GCountersTlsAlert(conn, module_id, port_id, group_idx)
        """TLS alert counters"""
        self.payload = GCountersTlsPayload(conn, module_id, port_id, group_idx)
        """TLS payload counters"""
        self.state = GCountersTlsState(conn, module_id, port_id, group_idx)
        """TLS state counters"""


class GHistogramTlsPayload:
    """TLS payload histogram"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx_bytes = P4G_TLS_RX_PAYLOAD_BYTES_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_RX_PAYLOAD_BYTES_HIST`
        """
        self.tx_bytes = P4G_TLS_TX_PAYLOAD_BYTES_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_TX_PAYLOAD_BYTES_HIST`
        """


class GHistogramTls:
    """TLS histogram"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.handshake = P4G_TLS_HANDSHAKE_HIST(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_HANDSHAKE_HIST`
        """
        self.payload = GHistogramTlsPayload(conn, module_id, port_id, group_idx)
        """TLS payload histogram"""


class GProtocolTls:
    """TLS protocol version"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.version = P4G_TLS_PROTOCOL_VER(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_PROTOCOL_VER`
        """
        self.min_required_version = P4G_TLS_MIN_REQ_PROTOCOL_VER(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_MIN_REQ_PROTOCOL_VER`
        """


class GFileTls:
    """TLS certificate and key files"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.certificate_path = P4G_TLS_CERTIFICATE_FILENAME(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_CERTIFICATE_FILENAME`
        """
        self.private_key_path = P4G_TLS_PRIVATE_KEY_FILENAME(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_PRIVATE_KEY_FILENAME`
        """
        self.dhparams_path = P4G_TLS_DHPARAMS_FILENAME(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_DHPARAMS_FILENAME`
        """


class GTls:
    """TLS configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.enable = P4G_TLS_ENABLE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_ENABLE`
        """
        self.server_name = P4G_TLS_SERVER_NAME(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_SERVER_NAME`
        """
        self.close_notify = P4G_TLS_CLOSE_NOTIFY(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_CLOSE_NOTIFY`
        """
        self.cipher_suites = P4G_TLS_CIPHER_SUITES(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_CIPHER_SUITES`
        """
        self.max_record_size = P4G_TLS_MAX_RECORD_SIZE(conn, module_id, port_id, group_idx)
        """
        Representation of :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TLS_MAX_RECORD_SIZE`
        """
        
        self.file = GFileTls(conn, module_id, port_id, group_idx)
        """Cert and key file"""
        self.protocol = GProtocolTls(conn, module_id, port_id, group_idx)
        """Protocol version"""
        self.counters = GCountersTls(conn, module_id, port_id, group_idx)
        """Counters"""
        self.histogram = GHistogramTls(conn, module_id, port_id, group_idx)
        """Histogram"""
