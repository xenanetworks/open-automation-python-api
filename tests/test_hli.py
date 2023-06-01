from __future__ import annotations

import timeit
import pstats
import cProfile
import pytest
import asyncio
import os
import sys
import logging
from typing import Coroutine, List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loguru import logger  # noqa: E402
from xoa_driver.testers import L23Tester  # noqa: E402



@pytest.mark.asyncio
async def test_hli() -> None:
    # logger.add(
    #     "./app.log",
    #     rotation="10 MB",
    #     retention=5,
    #     enqueue=True,
    #     compression="zip",
    #     level=0,
    #     serialize=True
    # )

    async with L23Tester("192.168.1.198", "ACO", enable_logging=True, custom_logger=logger) as tester:
        module = tester.modules.obtain(1)
        port1 = module.ports.obtain(0)
        port2 = module.ports.obtain(1)
        print(port1, port2)
        # print(port1.info.reservation)
        # print(port1.info.reserved_by)
        # await port1.reservation.set_reserve()



def run(method: Coroutine) -> None:
    import platform

    if platform.system() == "Windows":
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
