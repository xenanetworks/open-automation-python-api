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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.current = P4G_TLS_STATE_CURRENT(conn, module_id, port_id, group_idx)
        self.total = P4G_TLS_STATE_TOTAL(conn, module_id, port_id, group_idx)
        self.rate = P4G_TLS_STATE_RATE(conn, module_id, port_id, group_idx)


class GCountersTlsAlert:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.warning = P4G_TLS_ALERT_WARNING_COUNTERS(conn, module_id, port_id, group_idx)
        self.fatal = P4G_TLS_ALERT_FATAL_COUNTERS(conn, module_id, port_id, group_idx)


class GCountersTlsPayload:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx = P4G_TLS_RX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)
        self.tx = P4G_TLS_TX_PAYLOAD_COUNTERS(conn, module_id, port_id, group_idx)


class GCountersTls:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.alert = GCountersTlsAlert(conn, module_id, port_id, group_idx)
        self.payload = GCountersTlsPayload(conn, module_id, port_id, group_idx)
        self.state = GCountersTlsState(conn, module_id, port_id, group_idx)


class GHistogramtlsPayload:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.rx_bytes = P4G_TLS_RX_PAYLOAD_BYTES_HIST(conn, module_id, port_id, group_idx)
        self.tx_bytes = P4G_TLS_TX_PAYLOAD_BYTES_HIST(conn, module_id, port_id, group_idx)


class GHistogramTls:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.handshake = P4G_TLS_HANDSHAKE_HIST(conn, module_id, port_id, group_idx)
        self.payload = GHistogramtlsPayload(conn, module_id, port_id, group_idx)


class GProtocolTls:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.version = P4G_TLS_PROTOCOL_VER(conn, module_id, port_id, group_idx)
        self.min_required_version = P4G_TLS_MIN_REQ_PROTOCOL_VER(conn, module_id, port_id, group_idx)


class GFileTls:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.certificate_path = P4G_TLS_CERTIFICATE_FILENAME(conn, module_id, port_id, group_idx)
        self.private_key_path = P4G_TLS_PRIVATE_KEY_FILENAME(conn, module_id, port_id, group_idx)
        self.dhparams_path = P4G_TLS_DHPARAMS_FILENAME(conn, module_id, port_id, group_idx)


class GTls:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.enable = P4G_TLS_ENABLE(conn, module_id, port_id, group_idx)
        self.server_name = P4G_TLS_SERVER_NAME(conn, module_id, port_id, group_idx)
        self.close_notify = P4G_TLS_CLOSE_NOTIFY(conn, module_id, port_id, group_idx)
        self.cipher_suites = P4G_TLS_CIPHER_SUITES(conn, module_id, port_id, group_idx)
        self.max_record_size = P4G_TLS_MAX_RECORD_SIZE(conn, module_id, port_id, group_idx)
        
        self.file = GFileTls(conn, module_id, port_id, group_idx)
        self.protocol = GProtocolTls(conn, module_id, port_id, group_idx)
        self.counters = GCountersTls(conn, module_id, port_id, group_idx)
        self.histogram = GHistogramTls(conn, module_id, port_id, group_idx)
