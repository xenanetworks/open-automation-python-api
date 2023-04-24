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
from xoa_driver.testers import L23Tester  # noqa: E402

from xoa_driver.functions.config_cli_convert import CLIConverter # noqa: E402



async def test_hli() -> None:
    async with L23Tester("192.168.1.198", "ACO") as tester:
        # t_cap = await tester.capabilities.get()
        # print(t_cap.can_sync_traffic_start)
        module = tester.modules.obtain(1)
        port1 = module.ports.obtain(0)
        port2 = module.ports.obtain(1)
        print(port1, port2)
        print(port1.info.reservation)
        print(port1.info.reserved_by)
        await port1.reservation.set_reserve()
        # print(m1)


def test_config_cli() -> None:
    for c in CLIConverter.read_commands_from_file(
        "C:/Users/Administrator/Desktop/m_command_example.txt"
    ):
        print(c)
        # print(c.as_request())


def run(method: Coroutine) -> None:
    import platform

    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(method)


if __name__ == "__main__":
    # run(test_hli())
    test_config_cli()
    # result = timeit.timeit(
    #     "run(main())",
    #     setup="from __main__ import run, main",
    #     number=10
    # )
    # print(result)
