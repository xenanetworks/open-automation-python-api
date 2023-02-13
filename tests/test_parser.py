from __future__ import annotations
import timeit
import pstats
import cProfile

import asyncio
import os
import sys
from typing import Coroutine
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver.lli import establish_connection  # noqa: E402
from xoa_driver.lli import commands  # noqa: E402
from xoa_driver.lli import TransportationHandler  # noqa: E402
from xoa_driver.utils import apply, apply_iter  # noqa: E402
# TODO: <GET> response contain more fields then driver can parse
# TODO: <GET> response contains less fields then driver can parse
# TODO: <SET> request require more fields then server expecting
# TODO: <SET> request require less fields then server expects

# async def connect() -> TransportationHandler:
#     ctx = TransportationHandler()
#     # print("Create handler")
#     await establish_connection(ctx, "192.168.1.198")
#     # print("Is connected", ctx.is_connected)
#     # with cProfile.Profile() as pr:
#     await apply(
#         commands.C_LOGON(ctx).set("xena"),
#         commands.C_OWNER(ctx).set("xoa")
#     )

async def main() -> None:
    # print("start")
    ctx = TransportationHandler(debug=False)
    # print("Create handler")
    await establish_connection(ctx, "192.168.1.198")
    # print("Is connected", ctx.is_connected)
    # with cProfile.Profile() as pr:

    await apply(
        commands.C_LOGON(ctx).set("xena"),
        commands.C_OWNER(ctx).set("xoa"),
        commands.M_CAPABILITIES(ctx, 1).get(),
        commands.P_CAPABILITIES(ctx, 0, 1).get(),
    )
        # print(resp)
        # ccp = await commands.C_CAPABILITIES(ctx).get()
        # print(ccp.version)
        # req = apply_iter(*[commands.P_CAPABILITIES(ctx, 1, 1).get() for _ in range(100_000)])
        # async for resp in req:
        #     resp.tx_eq_tap_max_val
    # stats = pstats.Stats(pr)
    # stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats(20)

    # port = PortL23()
    # if isinstance(port, PortL23) and port.is_capable_of(ANLT, PCS_PMA)


    # Testsuite 2544:
        # required_port_type: L23Port
        # required_functionalities: 
    # ANLT functionalities:
        # required_port_type: L23Port,
        # required_functionalities:  ANLT

def run(method: Coroutine) -> None:
    import platform
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(method)


if __name__ == "__main__":
    run(main())
    # result = timeit.timeit(
    #     "run(main())",
    #     setup="from __main__ import run, main",
    #     number=1
    # )
    # print(result)
