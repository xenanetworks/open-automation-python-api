from __future__ import annotations
from xoa_driver.enums import MediaConfigurationType
from xoa_driver.functions.mgmt import (
    get_module_supported_media,
    set_module_media_config,
)

import timeit
import pstats
import cProfile

import asyncio
import os
import sys
import logging
from typing import Coroutine, List, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loguru import logger  # noqa: E402
from xoa_driver.testers import L23Tester  # noqa: E402
from xoa_driver.functions.config_cli_convert import CLIConverter  # noqa: E402
from xoa_driver.internals.utils.artificial_event import ReloadPortResponseLike

async def test_using_a_outdated_port():
    # Module 7 of destination chassis is supposed to have two modes: BASE-T1(7 ports), BASE-T1S(2 ports), switch to BASE-T1 to start this test.
    t = await L23Tester("192.168.1.198", "Ron", enable_logging=False)


    m1 = t.modules.obtain(7)
    print(await m1.port_count.get())
    await set_module_media_config(m1, MediaConfigurationType.BASE_T1S)
    print(await m1.port_count.get())


    # p1 = m1.ports.obtain(3)
    # await p1.capabilities.get()
    # print('success1')
    # await set_module_media_config(m1, MediaConfigurationType.BASE_T1S)
    # await p1.capabilities.get()
    # # print('success2')
    # This line should raise a ValueError: This instance is outdated, please obtain a new instance.
    # p2 = m1.ports.obtain(3)
    # await p2.capabilities.get()


async def test_getting_a_removed_port():
    # Module 7 of destination chassis is supposed to have two modes: BASE-T1(7 ports), BASE-T1S(2 ports), switch to BASE-T1 to start this test.
    t = await L23Tester("192.168.1.198", "Ron", enable_logging=False)
    m1 = t.modules.obtain(7)
    p1 = m1.ports.obtain(1)

    print(len(m1.ports))
    print('success1', await p1.interface.get())
    await set_module_media_config(m1, MediaConfigurationType.BASE_T1S)
    p2 = m1.ports.obtain(1)
    await p2.capabilities.get()
    print('success2', await p2.interface.get())
    await p1.capabilities.get()
    print('success3', await p1.interface.get())
    print(len(m1.ports))
    # This line should do fine.


def run(method: Coroutine) -> None:
    import platform

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(method)


if __name__ == "__main__":
    run(test_using_a_outdated_port())