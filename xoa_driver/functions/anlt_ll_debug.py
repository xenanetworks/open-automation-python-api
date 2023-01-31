from __future__ import annotations

from typing import Dict
from xoa_driver.enums import (
    Layer1ConfigType
)
from xoa_driver.ports import GenericAnyPort
from xoa_driver.lli import commands


class anlt_ll_debug:
    PMD_CONFIG_REGISTER = 0x02
    LT_TX_CONFIG_REGISTER = 0x20
    LT_TX_FRAME_REGISTER = 0x24
    LT_RX_STATUS_REGISTER = 0x29
    LT_RX_CONFIG_REGISTER = 0x28
    LT_RX_FRAME_REGISTER = 0x2C
    LT_RX_ERROR_STAT_0 = 0x2A
    LT_RX_ERROR_STAT_1 = 0x2B

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
        ll_info = await commands.PL1_CFG_TMP(self.conn, self.mid, self.pid, self.lane, Layer1ConfigType.LL_DEBUG_INFO).get()
        self.ll_info = {
            "base": ll_info.value[0],
            "rx_gtm_base": ll_info.value[1],
            "rx_serdes": ll_info.value[2],
            "tx_gtm_base": ll_info.value[3],
            "tx_serdes": ll_info.value[4],
        }

    async def lane_reset(self) -> None:
        """Reset the lane (serdes)"""
        GTM_QUAD_GT_CONFIG = 0x102
        addr = self.ll_info.get('rx_gtm_base') + GTM_QUAD_GT_CONFIG + (self.ll_info.get('rx_serdes') * 0x40)
        r = commands.PX_RW(self.conn, self.mid, self.pid, 2000, addr)
        v = int((await r.get()).value, 16)
        # Set bit 2
        v |= 1 << 2
        await r.set('0x{0:08X}'.format(v))
        # Clear bit 2
        v &= ~(1 << 2)
        await r.set('0x{0:08X}'.format(v))

    async def __get(self, reg) -> int:
        addr = self.ll_info.get('base') + reg + (self.lane * 0x40)
        r = commands.PX_RW(self.conn, self.mid, self.pid, 2000, addr)
        return int((await r.get()).value, 16)

    async def __set(self, reg, value) -> None:
        addr = self.ll_info.get('base') + reg + (self.lane * 0x40)
        r = commands.PX_RW(self.conn, self.mid, self.pid, 2000, addr)
        await r.set('0x{0:08X}'.format(value))

    async def mode_get(self) -> int:
        return await self.__get(self.PMD_CONFIG_REGISTER)

    async def mode_set(self, value) -> None:
        await self.__set(self.PMD_CONFIG_REGISTER, value)

    async def lt_tx_config_get(self) -> int:
        return await self.__get(self.LT_TX_CONFIG_REGISTER)

    async def lt_tx_config_set(self, value) -> None:
        await self.__set(self.LT_TX_CONFIG_REGISTER, value)

    async def lt_rx_config_get(self) -> int:
        return await self.__get(self.LT_RX_CONFIG_REGISTER)

    async def lt_rx_config_set(self, value) -> None:
        await self.__set(self.LT_RX_CONFIG_REGISTER, value)

    async def lt_tx_tf_get(self) -> int:
        return await self.__get(self.LT_TX_FRAME_REGISTER)

    async def lt_tx_tf_set(self, value) -> None:
        await self.__set(self.LT_TX_FRAME_REGISTER, value)

    async def lt_rx_tf_get(self) -> int:
        return await self.__get(self.LT_RX_FRAME_REGISTER)

    async def lt_status(self) -> int:
        return await self.__get(self.LT_RX_STATUS_REGISTER)

    async def lt_prbs(self) -> Dict[str, int]:
        cfg = await self.__get(self.LT_RX_CONFIG_REGISTER)
        cfg &= ~(3 << 21)  # Clear bit 22-21
        cfg |= (1 << 20)  # Set bit 20
        await self.__set(self.LT_RX_CONFIG_REGISTER, cfg)  # Trigger PRBS read
        cfg &= ~(1 << 20)  # Clear bit 20
        await self.__set(self.LT_RX_CONFIG_REGISTER, cfg)

        # Read the total # bits
        cfg &= ~(3 << 21)  # Clear bit 22-21
        cfg |= (1 << 21)
        await self.__set(self.LT_RX_CONFIG_REGISTER, cfg)
        v = await self.__get(self.LT_RX_ERROR_STAT_0)
        total_bits = v
        v = await self.__get(self.LT_RX_ERROR_STAT_1)
        total_bits |= (v << 32)

        # Read the total # error bits
        cfg &= ~(3 << 21)  # Clear bit 22-21
        cfg |= (2 << 21)
        await self.__set(self.LT_RX_CONFIG_REGISTER, cfg)
        v = await self.__get(self.LT_RX_ERROR_STAT_0)
        error_bits = v
        v = await self.__get(self.LT_RX_ERROR_STAT_1)
        error_bits |= (v << 32)
        error_bits &= 0x0000ffffffffffff
        return {
            "total_bits": total_bits,
            "error_bits": error_bits
        }
