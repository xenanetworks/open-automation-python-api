from __future__ import annotations

import timeit
import pstats
import cProfile

import asyncio
import os
import sys
import logging
from typing import Coroutine, List
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loguru import logger  # noqa: E402
from xoa_driver.v2.testers import L23Tester  # noqa: E402
from xoa_driver.internals.core.transporter.protocol.payload import ResponseBodyStruct, field, XmpSequence, XmpByte
# TODO: <GET> response contain more fields then driver can parse
# TODO: <GET> response contains less fields then driver can parse
# TODO: <SET> request require more fields then server expecting
# TODO: <SET> request require less fields then server expects


async def test_hli() -> None:
    async with L23Tester("192.168.1.197", "ACO") as tester:
        # t_cap = await tester.capabilities.get()
        # print(t_cap.can_sync_traffic_start)
        print(await tester.model.get())


def run(method: Coroutine) -> None:
    import platform
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(method)


if __name__ == "__main__":
    run(test_hli())
    # result = timeit.timeit(
    #     "run(main())",
    #     setup="from __main__ import run, main",
    #     number=10
    # )
    # print(result)
