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
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.type = P4G_RAW_PAYLOAD_TYPE(conn, module_id, port_id, group_idx)
        self.total_length = P4G_RAW_PAYLOAD_TOTAL_LEN(conn, module_id, port_id, group_idx)
        self.rx_length = P4G_RAW_RX_PAYLOAD_LEN(conn, module_id, port_id, group_idx) # ?
        self.content = P4G_RAW_PAYLOAD(conn, module_id, port_id, group_idx)
        self.repeat_length = P4G_RAW_PAYLOAD_REPEAT_LEN(conn, module_id, port_id, group_idx)


class GConnectionRaw:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.incarnation = P4G_RAW_CONN_INCARNATION(conn, module_id, port_id, group_idx)
        self.repetitions = P4G_RAW_CONN_REPETITIONS(conn, module_id, port_id, group_idx)
        self.lifetime = P4G_RAW_CONN_LIFETIME(conn, module_id, port_id, group_idx)
        self.close_condition = P4G_RAW_CLOSE_CONN(conn, module_id, port_id, group_idx)


class GBurstyRaw:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.transmission = P4G_RAW_BURSTY_TX(conn, module_id, port_id, group_idx)
        self.config = P4G_RAW_BURSTY_CONF(conn, module_id, port_id, group_idx)


class GTransmitRaw:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.during_ramp = P4G_RAW_TX_DURING_RAMP(conn, module_id, port_id, group_idx)
        self.time_offset = P4G_RAW_TX_TIME_OFFSET(conn, module_id, port_id, group_idx)

class GDownloadRequestRaw:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.server_must_wait = P4G_RAW_HAS_DOWNLOAD_REQ(conn, module_id, port_id, group_idx)
        self.transactions_number = P4G_RAW_REQUEST_REPEAT(conn, module_id, port_id, group_idx) # ?
        self.content = P4G_RAW_DOWNLOAD_REQUEST(conn, module_id, port_id, group_idx)


class GCountersTransaction:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.transaction = P4G_APP_TRANSACTION_COUNTERS(conn, module_id, port_id, group_idx)


class GRaw:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, group_idx: int) -> None:
        self.test_scenario = P4G_RAW_TEST_SCENARIO(conn, module_id, port_id, group_idx)
        self.utilization = P4G_RAW_UTILIZATION(conn, module_id, port_id, group_idx)
        
        self.download_request = GDownloadRequestRaw(conn, module_id, port_id, group_idx)
        self.payload = GPayloadRaw(conn, module_id, port_id, group_idx)
        self.connection = GConnectionRaw(conn, module_id, port_id, group_idx)
        self.bursty = GBurstyRaw(conn, module_id, port_id, group_idx)
        self.tx = GTransmitRaw(conn, module_id, port_id, group_idx)

        self.transaction_counter = GCountersTransaction(conn, module_id, port_id, group_idx)