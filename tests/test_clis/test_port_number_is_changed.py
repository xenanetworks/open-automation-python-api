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
from xoa_driver.internals.utils.managers.exceptions import NoSuchPortError  # noqa: E402


async def test_using_a_outdated_port():
    # Module 7 of destination chassis is supposed to have two modes: BASE-T1(7 ports), BASE-T1S(2 ports), switch to BASE-T1 to start this test.
    t = await L23Tester("192.168.1.198", "Ron", enable_logging=False)

    m1 = t.modules.obtain(7)
    p1 = m1.ports.obtain(3)
    print(await p1.interface.get())
    print('success1')
    await set_module_media_config(m1, MediaConfigurationType.BASE_T1S)
    try:
        print(await p1.interface.get())
        print('success2')
    except ConnectionRefusedError as e:
        print(e)
    try:
        p2 = m1.ports.obtain(3)
        print(await p2.interface.get())
        print('success3')
    except NoSuchPortError as e:
        print(e)


async def test_getting_a_removed_port():
    # Module 7 of destination chassis is supposed to have two modes: BASE-T1(7 ports), BASE-T1S(2 ports), switch to BASE-T1 to start this test.
    t = await L23Tester("192.168.1.198", "Ron", enable_logging=False)
    m1 = t.modules.obtain(7)
    print(len(m1.ports))

    p1 = m1.ports.obtain(1)
    print('success1', await p1.interface.get())

    await set_module_media_config(m1, MediaConfigurationType.BASE_T1S)

    print(len(m1.ports))
    try:
        print('success2', await p1.interface.get())
    except ConnectionRefusedError as e:
        print(e)
    # This will raise Exceptions.

    p2 = m1.ports.obtain(1)
    print('success3', await p2.interface.get())
    # This line should do fine.


async def test_getting_stream_under_a_removed_port():
    # Module 7 of destination chassis is supposed to have two modes: BASE-T1(7 ports), BASE-T1S(2 ports), switch to BASE-T1 to start this test.
    t = await L23Tester("192.168.1.198", "Ron", enable_logging=False)
    m1 = t.modules.obtain(7)
    p1 = m1.ports.obtain(3)
    await p1.reservation.set_reserve()
    s = await p1.streams.create()
    b = s.comment
    await set_module_media_config(m1, MediaConfigurationType.BASE_T1S)

    print(await b.get())


def run(method: Coroutine) -> None:
    import platform

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(method)


if __name__ == "__main__":
    run(test_getting_stream_under_a_removed_port())
