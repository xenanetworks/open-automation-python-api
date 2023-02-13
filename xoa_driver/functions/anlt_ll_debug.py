from __future__ import annotations
import asyncio
import typing as t
from functools import partial
from xoa_driver.enums import Layer1ConfigType
from xoa_driver.ports import GenericAnyPort
from xoa_driver.lli import commands
from dataclasses import dataclass
from enum import IntEnum

class AnLtD(IntEnum):
    PMD_CONFIG_REGISTER = 0x02
    LT_TX_CONFIG_REGISTER = 0x20
    LT_TX_FRAME_REGISTER = 0x24
    LT_RX_STATUS_REGISTER = 0x29
    LT_RX_CONFIG_REGISTER = 0x28
    LT_RX_FRAME_REGISTER = 0x2C
    LT_RX_ERROR_STAT_0 = 0x2A
    LT_RX_ERROR_STAT_1 = 0x2B
    LT_RX_ANALYZER_CONFIG = 0x38
    LT_RX_ANALYZER_TRIG_MASK = 0x39
    LT_RX_ANALYZER_STATUS = 0x3A
    LT_RX_ANALYZER_RD_ADDR = 0x3B
    LT_RX_ANALYZER_RD_PAGE = 0x3C
    LT_RX_ANALYZER_RD_DATA = 0x3D

@dataclass
class AnLtLowLevelInfo:
    base: int
    rx_gtm_base: int
    rx_serdes: int
    tx_gtm_base: int
    tx_serdes: int


async def init(port: GenericAnyPort, lane: int) -> AnLtLowLevelInfo:
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    inf = await commands.PL1_CFG_TMP(
        conn, mid, pid, lane, Layer1ConfigType.LL_DEBUG_INFO
    ).get()
    values = inf.values[:5]
    inf = AnLtLowLevelInfo(*values)
    return inf


async def lane_reset(
    port: GenericAnyPort, lane: int, inf: t.Optional[AnLtLowLevelInfo] = None
) -> None:
    """Reset the lane (serdes)"""
    GTM_QUAD_GT_CONFIG = 0x102
    if inf is None:
        inf = await init(port, lane)
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id
    addr = inf.rx_gtm_base + GTM_QUAD_GT_CONFIG + (inf.rx_serdes * 0x40)
    r = commands.PX_RW(conn, mid, pid, 2000, addr)
    v = int((await r.get()).value, 16)
    # Set bit 2
    v |= 1 << 2
    await r.set(f"0x{v:08X}")
    # in XOA-Driver V2 `0x` prefix will be drop from the hex strings
    # Clear bit 2
    v &= ~(1 << 2)
    await r.set(f"0x{v:08X}")
    return None


async def __get(
    port: GenericAnyPort,
    lane: int,
    reg: AnLtD,
    inf: t.Optional[AnLtLowLevelInfo] = None,
) -> int:
    if inf is None:
        inf = await init(port, lane)
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id

    addr = inf.base + reg.value + (lane * 0x40)
    r = commands.PX_RW(conn, mid, pid, 2000, addr)
    return int((await r.get()).value, 16)


async def __set(
    port: GenericAnyPort,
    lane: int,
    reg: AnLtD,
    value: int,
    inf: t.Optional[AnLtLowLevelInfo] = None,
) -> None:
    if inf is None:
        inf = await init(port, lane)
    conn, mid, pid = port._conn, port.kind.module_id, port.kind.port_id

    addr = inf.base + reg.value + (lane * 0x40)
    r = commands.PX_RW(conn, mid, pid, 2000, addr)
    await r.set(f"0x{value:08X}")
    return None


mode_get = partial(__get, reg=AnLtD.PMD_CONFIG_REGISTER)
mode_set = partial(__set, reg=AnLtD.PMD_CONFIG_REGISTER)

lt_tx_config_get = partial(__get, reg=AnLtD.LT_TX_CONFIG_REGISTER)
lt_tx_config_set = partial(__set, reg=AnLtD.LT_TX_CONFIG_REGISTER)

lt_rx_config_get = partial(__get, reg=AnLtD.LT_RX_CONFIG_REGISTER)
lt_rx_config_set = partial(__set, reg=AnLtD.LT_RX_CONFIG_REGISTER)

lt_tx_tf_get = partial(__get, reg=AnLtD.LT_TX_FRAME_REGISTER)
lt_tx_tf_set = partial(__set, reg=AnLtD.LT_TX_FRAME_REGISTER)

lt_rx_tf_get = partial(__get, reg=AnLtD.LT_RX_FRAME_REGISTER)

lt_status = partial(__get, reg=AnLtD.LT_RX_STATUS_REGISTER)

lt_rx_error_stat0_get = partial(__get, reg=AnLtD.LT_RX_ERROR_STAT_0)
lt_rx_error_stat1_get = partial(__get, reg=AnLtD.LT_RX_ERROR_STAT_1)

lt_rx_analyzer_config_get = partial(__get, reg=AnLtD.LT_RX_ANALYZER_CONFIG)
lt_rx_analyzer_config_set = partial(__set, reg=AnLtD.LT_RX_ANALYZER_CONFIG)

lt_rx_analyzer_trig_mask_get = partial(__get, reg=AnLtD.LT_RX_ANALYZER_TRIG_MASK)
lt_rx_analyzer_trig_mask_set = partial(__set, reg=AnLtD.LT_RX_ANALYZER_TRIG_MASK)

lt_rx_analyzer_status_get = partial(__get, reg=AnLtD.LT_RX_ANALYZER_STATUS)

lt_rx_analyzer_rd_addr_get = partial(__get, reg=AnLtD.LT_RX_ANALYZER_RD_ADDR)
lt_rx_analyzer_rd_addr_set = partial(__set, reg=AnLtD.LT_RX_ANALYZER_RD_ADDR)

lt_rx_analyzer_rd_page_get = partial(__get, reg=AnLtD.LT_RX_ANALYZER_RD_PAGE)
lt_rx_analyzer_rd_page_set = partial(__set, reg=AnLtD.LT_RX_ANALYZER_RD_PAGE)

lt_rx_analyzer_rd_data_get = partial(__get, reg=AnLtD.LT_RX_ANALYZER_RD_DATA)


async def lt_prbs(
    port: GenericAnyPort,
    lane: int,
    inf: t.Optional[AnLtLowLevelInfo] = None,
) -> dict[str, float]:
    if inf is None:
        inf = await init(port, lane)

    cfg = await lt_rx_config_get(port, lane, inf=inf)
    cfg &= ~(3 << 21)  # Clear bit 22-21
    cfg |= 1 << 20  # Set bit 20
    await lt_rx_config_set(port, lane, inf=inf, value=cfg)  # Trigger PRBS read
    cfg &= ~(1 << 20)  # Clear bit 20
    await lt_rx_config_set(port, lane, inf=inf, value=cfg)

    # Read the total # bits
    cfg &= ~(3 << 21)  # Clear bit 22-21
    cfg |= 1 << 21
    await lt_rx_config_set(port, lane, inf=inf, value=cfg)
    v = await lt_rx_error_stat0_get(port, lane, inf=inf)
    total_bits = v
    v = await lt_rx_error_stat1_get(port, lane, inf=inf)
    total_bits |= v << 32

    # Read the total # error bits
    cfg &= ~(3 << 21)  # Clear bit 22-21
    cfg |= 2 << 21
    await lt_rx_config_set(port, lane, inf=inf, value=cfg)
    v = await lt_rx_error_stat0_get(port, lane, inf=inf)
    error_bits = v
    v = await lt_rx_error_stat1_get(port, lane, inf=inf)
    error_bits |= v << 32
    error_bits &= 0x0000FFFFFFFFFFFF
    ber = (error_bits) / (total_bits) if total_bits > 0 else float("nan")
    return {"total_bits": total_bits, "error_bits": error_bits, "ber": float(ber)}


async def lt_rx_analyzer_dump(
    port: GenericAnyPort, lane: int, inf: t.Optional[AnLtLowLevelInfo] = None
) -> str:
    """This will dump the 320bit words in the capture buffer"""
    if inf is None:
        inf = await init(port, lane)
    string = []
    trigger_pos, capture_done = await asyncio.gather(
        lt_rx_analyzer_config_get(port, lane, inf=inf),
        lt_rx_analyzer_status_get(port, lane, inf=inf),
    )
    string.append(f"Trigger position: {trigger_pos}\n")
    string.append(f"Analyzer status: : {capture_done}\n")
    if not capture_done:
        string.append("No capture\n")
        result = "".join(string)
        return result
    string.append("Capture:")
    for r in range(256):
        # Set the read address
        await lt_rx_analyzer_rd_addr_set(port, lane, inf=inf, value=r)
        string.append(f"{r:02X}: ")
        for p in range(10):
            # Read the data
            await lt_rx_analyzer_rd_page_set(port, lane, inf=inf, value=p)
            d = await lt_rx_analyzer_rd_data_get(port, lane, inf=inf)
            string.append(f"{d:08X} ")
        string.append("\n")
    string.append("Done\n")
    result = "".join(string)
    return result



__all__ = (
    "init",
    "lane_reset",
    "mode_get",
    "mode_set",
    "lt_prbs",
    "lt_rx_analyzer_config_get",
    "lt_rx_analyzer_config_set",
    "lt_rx_analyzer_dump",
    "lt_rx_analyzer_rd_addr_get",
    "lt_rx_analyzer_rd_addr_set",
    "lt_rx_analyzer_rd_data_get",
    "lt_rx_analyzer_rd_page_get",
    "lt_rx_analyzer_rd_page_set",
    "lt_tx_config_get",
    "lt_tx_config_set",
    "lt_rx_analyzer_status_get",
    "lt_rx_analyzer_trig_mask_get",
    "lt_rx_analyzer_trig_mask_set",
    "lt_rx_config_get",
    "lt_rx_config_set",
    "lt_rx_error_stat0_get",
    "lt_tx_tf_get",
    "lt_rx_error_stat1_get",
    "lt_rx_tf_get",
    "lt_status",
    "lt_tx_tf_set",
)
