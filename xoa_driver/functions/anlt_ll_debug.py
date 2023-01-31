from __future__ import annotations

from functools import partialmethod
from typing import Dict
from xoa_driver.enums import (
    Layer1ConfigType
)
from xoa_driver.ports import GenericAnyPort
from xoa_driver.lli import commands
from dataclasses import dataclass


@dataclass
class AnLtLowLevelInfo:
    base: int
    rx_gtm_base: int
    rx_serdes: int
    tx_gtm_base: int
    tx_serdes: int


class AnLtLowLevelDebug:
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

    def __init__(self, port: GenericAnyPort, lane: int):
        """
        :param port: port to select
        :type port: :class:`~xoa_driver.ports.GenericAnyPort`
        :param lane: lane index, starting from 0. The lane to reset
        :type lane: int
        """
        self.port = port
        self.conn = port._conn
        self.mid = port.kind.module_id
        self.pid = port.kind.port_id
        self.lane = lane

    async def init(self) -> None:
        inf = await commands.PL1_CFG_TMP(self.conn, self.mid, self.pid, self.lane, Layer1ConfigType.LL_DEBUG_INFO).get()
        self.inf = AnLtLowLevelInfo(
            base=inf.value[0],
            rx_gtm_base=inf.value[1],
            rx_serdes=inf.value[2],
            tx_gtm_base=inf.value[3],
            tx_serdes=inf.value[4]
        )

    async def lane_reset(self) -> None:
        """Reset the lane (serdes)"""
        GTM_QUAD_GT_CONFIG = 0x102
        addr = self.inf.rx_gtm_base + GTM_QUAD_GT_CONFIG + (self.inf.rx_serdes * 0x40)
        r = commands.PX_RW(self.conn, self.mid, self.pid, 2000, addr)
        v = int((await r.get()).value, 16)
        # Set bit 2
        v |= 1 << 2
        await r.set('0x{0:08X}'.format(v))
        # Clear bit 2
        v &= ~(1 << 2)
        await r.set('0x{0:08X}'.format(v))

    async def __get(self, reg) -> int:
        addr = self.inf.base + reg + (self.lane * 0x40)
        r = commands.PX_RW(self.conn, self.mid, self.pid, 2000, addr)
        return int((await r.get()).value, 16)

    async def __set(self, reg, value) -> None:
        addr = self.inf.base + reg + (self.lane * 0x40)
        r = commands.PX_RW(self.conn, self.mid, self.pid, 2000, addr)
        await r.set('0x{0:08X}'.format(value))

    mode_get = partialmethod(__get, reg=PMD_CONFIG_REGISTER)
    mode_set = partialmethod(__set, reg=PMD_CONFIG_REGISTER)

    lt_tx_config_get = partialmethod(__get, reg=LT_TX_CONFIG_REGISTER)
    lt_tx_config_set = partialmethod(__get, reg=LT_TX_CONFIG_REGISTER)

    lt_rx_config_get = partialmethod(__get, reg=LT_RX_CONFIG_REGISTER)
    lt_rx_config_set = partialmethod(__set, reg=LT_RX_CONFIG_REGISTER)

    lt_tx_tf_get = partialmethod(__get, reg=LT_TX_FRAME_REGISTER)
    lt_tx_tf_set = partialmethod(__set, reg=LT_TX_FRAME_REGISTER)

    lt_rx_tf_get = partialmethod(__get, reg=LT_RX_FRAME_REGISTER)

    lt_status = partialmethod(__get, reg=LT_RX_STATUS_REGISTER)

    lt_rx_error_stat0_get = partialmethod(__get, reg=LT_RX_ERROR_STAT_0)
    lt_rx_error_stat1_get = partialmethod(__get, reg=LT_RX_ERROR_STAT_1)

    lt_rx_analyzer_config_get = partialmethod(__get, reg=LT_RX_ANALYZER_CONFIG)
    lt_rx_analyzer_config_set = partialmethod(__set, reg=LT_RX_ANALYZER_CONFIG)

    lt_rx_analyzer_trig_mask_get = partialmethod(__get, reg=LT_RX_ANALYZER_TRIG_MASK)
    lt_rx_analyzer_trig_mask_set = partialmethod(__set, reg=LT_RX_ANALYZER_TRIG_MASK)

    lt_rx_analyzer_status_get = partialmethod(__get, reg=LT_RX_ANALYZER_STATUS)

    lt_rx_analyzer_rd_addr_get= partialmethod(__get, reg=LT_RX_ANALYZER_RD_ADDR)
    lt_rx_analyzer_rd_addr_set= partialmethod(__set, reg=LT_RX_ANALYZER_RD_ADDR)

    lt_rx_analyzer_rd_page_get = partialmethod(__get, reg=LT_RX_ANALYZER_RD_PAGE)
    lt_rx_analyzer_rd_page_set = partialmethod(__set, reg=LT_RX_ANALYZER_RD_PAGE)

    lt_rx_analyzer_rd_data_get = partialmethod(__get, reg=LT_RX_ANALYZER_RD_DATA)

    async def lt_prbs(self) -> Dict[str, int]:
        cfg = await self.lt_rx_config_get()
        cfg &= ~(3 << 21)  # Clear bit 22-21
        cfg |= (1 << 20)  # Set bit 20
        await self.lt_rx_config_set(value=cfg)  # Trigger PRBS read
        cfg &= ~(1 << 20)  # Clear bit 20
        await self.lt_rx_config_set(value=cfg)

        # Read the total # bits
        cfg &= ~(3 << 21)  # Clear bit 22-21
        cfg |= (1 << 21)
        await self.lt_rx_config_set(value=cfg)
        v = await self.lt_rx_error_stat0_get()
        total_bits = v
        v = await self.lt_rx_error_stat1_get()
        total_bits |= (v << 32)

        # Read the total # error bits
        cfg &= ~(3 << 21)  # Clear bit 22-21
        cfg |= (2 << 21)
        await self.lt_rx_config_set(value=cfg)
        v = await self.lt_rx_error_stat0_get()
        error_bits = v
        v = await self.lt_rx_error_stat1_get()
        error_bits |= (v << 32)
        error_bits &= 0x0000ffffffffffff
        return {
            "total_bits": total_bits,
            "error_bits": error_bits,
            "ber": error_bits/total_bits
        }

    async def lt_rx_analyzer_dump(self):
        """This will dump the 320bit words in the capture buffer"""
        trigger_pos = await self.lt_rx_analyzer_config_get()
        print("Trigger position: %d" % trigger_pos)
        capture_done = await self.lt_rx_analyzer_status_get()
        print("Analyzer status: %d" % capture_done)
        if capture_done:
            print("Capture:")
            for r in range(0, 256):
                # Set the read address
                await self.lt_rx_analyzer_rd_addr_set(value=r)
                print('{0:02X}'.format(r), end=': ')
                for p in range(0, 10):
                    # Read the data
                    await self.lt_rx_analyzer_rd_page_set(value=p)
                    d = await self.lt_rx_analyzer_rd_data_get()
                    print('{0:08X}'.format(d), end=' ')
                print("")
        else:
            print("No capture")
            return
        print("Done")
