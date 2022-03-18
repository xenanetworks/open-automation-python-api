import asyncio
import sys
import os
import timeit
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver import testers
from xoa_driver import utils


async def make_requests(tester):
    c_name = (await tester.name.get()).chassis_name
    p = tester.modules.obtain(0).ports.obtain(0)
    tokens = [ 
        p.capabilities.get()
        for _ in range(1000)
    ]
    print("Process:", len(tokens), "requests on:", c_name )
    start = timeit.default_timer()
    async for cap in utils.apply_iter(*tokens): 
        pass
    stop = timeit.default_timer()
    elapsed = stop - start
    print("Finished in: ", elapsed)

async def script():
    tester1 = testers.L23Tester("192.168.1.198", "xena_test")
    tester2 = testers.L23Tester("87.61.110.118", "xena_test")
    await asyncio.gather(tester1, tester2)
    await asyncio.gather(
        make_requests(tester1),
        make_requests(tester2),
    )


def main():
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(script())
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()