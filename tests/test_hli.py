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
from xoa_driver.lli import establish_connection  # noqa: E402
from xoa_driver.lli import commands  # noqa: E402
from xoa_driver.lli import TransportationHandler  # noqa: E402
from xoa_driver.utils import apply, apply_iter  # noqa: E402
from xoa_driver.internals.core.transporter.protocol.payload import (
    ResponseBodyStruct,
    field,
    XmpSequence,
    XmpByte,
)
from xoa_driver.functions.config_cli_convert import CLIConverter

# TODO: <GET> response contain more fields then driver can parse
# TODO: <GET> response contains less fields then driver can parse
# TODO: <SET> request require more fields then server expecting
# TODO: <SET> request require less fields then server expects


async def test_command() -> None:
    data = b"\x00\x02\x00\x06\x00\x06\x00\x06"

    class GetDataAttr(ResponseBodyStruct):
        port_counts: List[int] = field(XmpSequence(types_chunk=[XmpByte()]))

    obj = GetDataAttr(data)
    print(obj)


async def test_lli() -> None:
    # logging.basicConfig(
    #     format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s',
    #     level=logging.DEBUG
    # )
    # logger_ = logging.getLogger(__file__)
    ctx = TransportationHandler(enable_logging=True, custom_logger=logger)
    await establish_connection(ctx, "192.168.1.197")
    # # print("Is connected", ctx.is_connected)
    # with cProfile.Profile() as pr:
    *_, pc = await apply(
        commands.C_LOGON(ctx).set("xena"),
        commands.C_OWNER(ctx).set("xoa"),
        commands.C_OWNER(ctx).get(),
        # commands.M_CAPABILITIES(ctx, 1).get(),
        # commands.P_CAPABILITIES(ctx, 1, 1).get(),
        commands.C_PORTCOUNTS(ctx).get(),
    )
    print(pc._order.field_names, pc.to_bytes())
    # req = apply_iter(*[commands.P_CAPABILITIES(ctx, 1, 1).get() for _ in range(1_000)])
    # async for resp in req:
    #     resp.tx_eq_tap_max_val
    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats(20)
    ctx.close()

    # port = PortL23()
    # if isinstance(port, PortL23) and port.is_capable_of(ANLT, PCS_PMA)

    # Testsuite 2544:
    # required_port_type: L23Port
    # required_functionalities:
    # ANLT functionalities:
    # required_port_type: L23Port,
    # required_functionalities:  ANLT


async def test_hli() -> None:
    # async with L23Tester("demo.xenanetworks.com", "ACO") as tester:
    #     t_cap = await tester.capabilities.get()
    #     print(t_cap.can_sync_traffic_start)
    ...


def test_config_cli() -> None:
    for c in CLIConverter.read_commands_from_file(
        "C:/Users/Administrator/Desktop/p_command_example.txt"
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
