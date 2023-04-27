from __future__ import annotations
import asyncio
import typing as t
from functools import partial
from xoa_driver import enums
from xoa_driver.ports import GenericL23Port
from xoa_driver.lli import commands
from dataclasses import dataclass
from enum import IntEnum
from .tools import get_ctx


class AnLtD(IntEnum):
    PMD_CONFIG_REGISTER = 0x02
    AN_TX_CONFIG_REGISTER = 0x10
    AN_RX_CONFIG_REGISTER = 0x18
    AN_RX_STATUS_REGISTER = 0x19
    AN_TX_PAGE_0_REGISTER = 0x14
    AN_TX_PAGE_1_REGISTER = 0x15
    AN_RX_DME_MV_RANGE    = 0x1A
    AN_RX_DME_BIT_RANGE   = 0x1B
    AN_RX_PAGE_0_REGISTER = 0x1C
    AN_RX_PAGE_1_REGISTER = 0x1D

    LT_TX_CONFIG_REGISTER = 0x20
    LT_TX_FRAME_REGISTER = 0x24
    LT_RX_STATUS_REGISTER = 0x29
    LT_RX_CONFIG_REGISTER = 0x28
    LT_RX_FRAME_REGISTER = 0x2C
    LT_RX_ERROR_STAT_0 = 0x2A
    LT_RX_ERROR_STAT_1 = 0x2B
    XLA_CONFIG = 0x38
    XLA_TRIG_MASK = 0x39
    XLA_STATUS = 0x3A
    XLA_RD_ADDR = 0x3B
    XLA_RD_PAGE = 0x3C
    XLA_RD_DATA = 0x3D


@dataclass
class AnLtLowLevelInfo:
    base: int
    rx_gtm_base: int
    rx_serdes: int
    tx_gtm_base: int
    tx_serdes: int


async def init(port: GenericL23Port, serdes: int) -> AnLtLowLevelInfo:
    conn, mid, pid = get_ctx(port)
    inf = await commands.PL1_CFG_TMP(
        conn, mid, pid, serdes, enums.Layer1ConfigType.LL_DEBUG_INFO
    ).get()
    values = inf.values[:5]
    inf = AnLtLowLevelInfo(*values)
    return inf


async def serdes_reset(
    port: GenericL23Port, serdes: int, inf: t.Optional[AnLtLowLevelInfo] = None
) -> None:
    GTM_QUAD_GT_CONFIG = 0x102
    if inf is None:
        inf = await init(port, serdes)
    conn, mid, pid = get_ctx(port)
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
    port: GenericL23Port,
    serdes: int,
    reg: AnLtD,
    inf: t.Optional[AnLtLowLevelInfo] = None,
) -> int:
    if inf is None:
        inf = await init(port, serdes)
    conn, mid, pid = get_ctx(port)
    addr = inf.base + reg.value + (serdes * 0x40)
    r = commands.PX_RW(conn, mid, pid, 2000, addr)
    return int((await r.get()).value, 16)


async def __set(
    port: GenericL23Port,
    serdes: int,
    reg: AnLtD,
    value: int,
    inf: t.Optional[AnLtLowLevelInfo] = None,
) -> None:
    if inf is None:
        inf = await init(port, serdes)
    conn, mid, pid = get_ctx(port)
    addr = inf.base + reg.value + (serdes * 0x40)
    r = commands.PX_RW(conn, mid, pid, 2000, addr)
    await r.set(f"0x{value:08X}")
    return None


mode_get = partial(__get, reg=AnLtD.PMD_CONFIG_REGISTER)
mode_set = partial(__set, reg=AnLtD.PMD_CONFIG_REGISTER)

an_status = partial(__get, reg=AnLtD.AN_RX_STATUS_REGISTER)

an_tx_config_get = partial(__get, reg=AnLtD.AN_TX_CONFIG_REGISTER)
an_tx_config_set = partial(__set, reg=AnLtD.AN_TX_CONFIG_REGISTER)

an_rx_config_get = partial(__get, reg=AnLtD.AN_RX_CONFIG_REGISTER)
an_rx_config_set = partial(__set, reg=AnLtD.AN_RX_CONFIG_REGISTER)

an_rx_dme_mv_range_get = partial(__get, reg=AnLtD.AN_RX_DME_MV_RANGE)
an_rx_dme_mv_range_set = partial(__set, reg=AnLtD.AN_RX_DME_MV_RANGE)

an_rx_dme_bit_range_get = partial(__get, reg=AnLtD.AN_RX_DME_BIT_RANGE)
an_rx_dme_bit_range_set = partial(__set, reg=AnLtD.AN_RX_DME_BIT_RANGE)

an_rx_page0_get = partial(__get, reg=AnLtD.AN_RX_PAGE_0_REGISTER)
an_rx_page1_get = partial(__get, reg=AnLtD.AN_RX_PAGE_1_REGISTER)

an_tx_page0_get = partial(__get, reg=AnLtD.AN_TX_PAGE_0_REGISTER)
an_tx_page0_set = partial(__set, reg=AnLtD.AN_TX_PAGE_0_REGISTER)
an_tx_page1_get = partial(__get, reg=AnLtD.AN_TX_PAGE_1_REGISTER)
an_tx_page1_set = partial(__set, reg=AnLtD.AN_TX_PAGE_1_REGISTER)

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

xla_config_get = partial(__get, reg=AnLtD.XLA_CONFIG)
xla_config_set = partial(__set, reg=AnLtD.XLA_CONFIG)

xla_trig_mask_get = partial(__get, reg=AnLtD.XLA_TRIG_MASK)
xla_trig_mask_set = partial(__set, reg=AnLtD.XLA_TRIG_MASK)

xla_status_get = partial(__get, reg=AnLtD.XLA_STATUS)

xla_rd_addr_get = partial(__get, reg=AnLtD.XLA_RD_ADDR)
xla_rd_addr_set = partial(__set, reg=AnLtD.XLA_RD_ADDR)

xla_rd_page_get = partial(__get, reg=AnLtD.XLA_RD_PAGE)
xla_rd_page_set = partial(__set, reg=AnLtD.XLA_RD_PAGE)

xla_rd_data_get = partial(__get, reg=AnLtD.XLA_RD_DATA)



async def lt_prbs(
    port: GenericL23Port,
    serdes: int,
    inf: t.Optional[AnLtLowLevelInfo] = None,
) -> dict[str, float]:
    if inf is None:
        inf = await init(port, serdes)

    cfg = await lt_rx_config_get(port, serdes, inf=inf)
    cfg &= ~(3 << 21)  # Clear bit 22-21
    cfg |= 1 << 20  # Set bit 20
    await lt_rx_config_set(port, serdes, inf=inf, value=cfg)  # Trigger PRBS read
    cfg &= ~(1 << 20)  # Clear bit 20
    await lt_rx_config_set(port, serdes, inf=inf, value=cfg)

    # Read the total # bits
    cfg &= ~(3 << 21)  # Clear bit 22-21
    cfg |= 1 << 21
    await lt_rx_config_set(port, serdes, inf=inf, value=cfg)
    v = await lt_rx_error_stat0_get(port, serdes, inf=inf)
    total_bits = v
    v = await lt_rx_error_stat1_get(port, serdes, inf=inf)
    total_bits |= v << 32

    # Read the total # error bits
    cfg &= ~(3 << 21)  # Clear bit 22-21
    cfg |= 2 << 21
    await lt_rx_config_set(port, serdes, inf=inf, value=cfg)
    v = await lt_rx_error_stat0_get(port, serdes, inf=inf)
    error_bits = v
    v = await lt_rx_error_stat1_get(port, serdes, inf=inf)
    error_bits |= v << 32
    error_bits &= 0x0000FFFFFFFFFFFF
    ber = (error_bits) / (total_bits) if total_bits > 0 else float("nan")
    return {"total_bits": total_bits, "error_bits": error_bits, "ber": float(ber)}


async def xla_dump(
    port: GenericL23Port,
    serdes: int,
    inf: t.Optional[AnLtLowLevelInfo] = None
) -> t.Dict[str, str]:
    """This will dump the 320bit words in the capture buffer"""
    if inf is None:
        inf = await init(port, serdes)
    result = {}
    trigger_pos, capture_done = await asyncio.gather(
        xla_config_get(port, serdes, inf=inf),
        xla_status_get(port, serdes, inf=inf),
    )
    result["Trigger Position"] = str(trigger_pos)
    result["Analyzer Status"] = str(capture_done)
    if not capture_done:
        result["Data"] = ""
        return result
    data_list = []
    for r in range(256):
        # Set the read address
        await xla_rd_addr_set(port, serdes, inf=inf, value=r)
        for p in range(10):
            # Read the data
            await xla_rd_page_set(port, serdes, inf=inf, value=9-p)
            d = await xla_rd_data_get(port, serdes, inf=inf)
            data_list.append(f"{d:08X}")
        data_list.append("\n")
    result["Data"] = "".join(data_list)
    return result


async def px_get(
    port: GenericL23Port,
    page_address: int,
    register_address: int
) -> t.Tuple[bool, str]:
    resp = await port.transceiver.access_rw(page_address, register_address).get()

    if resp.value.lower().find("dead") != -1:
        return (False, resp.value)
    else:
        return (True, resp.value)
    
async def px_set(
    port: GenericL23Port,
    page_address: int,
    register_address: int,
    value: int
) -> None:
    value_hexstr = hex(value)
    await port.transceiver.access_rw(page_address, register_address).set(value_hexstr)


async def xla_dump_ctrl(
    port: GenericL23Port,
    on: bool
) -> None:
    conn, mid, pid = get_ctx(port)
    await commands.PL1_CFG_TMP(conn, mid, pid, 0, enums.Layer1ConfigType.AN_LT_XLA_MODE).set(values=[int(on)])
    


__all__ = (
    "init",
    "serdes_reset",
    "mode_get",
    "mode_set",
    "lt_prbs",
    "xla_config_get",
    "xla_config_set",
    "xla_dump",
    "xla_rd_addr_get",
    "xla_rd_addr_set",
    "xla_rd_data_get",
    "xla_rd_page_get",
    "xla_rd_page_set",
    "lt_tx_config_get",
    "lt_tx_config_set",
    "xla_status_get",
    "xla_trig_mask_get",
    "xla_trig_mask_set",
    "lt_rx_config_get",
    "lt_rx_config_set",
    "lt_rx_error_stat0_get",
    "lt_tx_tf_get",
    "lt_rx_error_stat1_get",
    "lt_rx_tf_get",
    "lt_status",
    "lt_tx_tf_set",
    "px_get",
    "px_set",
    "xla_dump_ctrl",
    "an_tx_config_get",
    "an_tx_config_set",
    "an_rx_dme_bit_range_get",
    "an_rx_dme_bit_range_set",
    "an_rx_dme_mv_range_get",
    "an_rx_dme_mv_range_set",
    "an_rx_page0_get",
    "an_rx_page1_get",
    "an_status",
    "an_tx_config_get",
    "an_tx_config_set",
    "an_tx_page0_get",
    "an_tx_page0_set",
    "an_tx_page1_get",
    "an_tx_page1_set",
)
