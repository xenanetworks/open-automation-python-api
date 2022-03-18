import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection


async def test_command():
    handler = TransportationHandler(debug=False)
    await establish_connection(handler, "192.168.1.198")
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set("XENA"),
    )
    print(await cmd.M_PORTCOUNT(handler, 0).get())
    many_p_capabilities = [
        cmd.P_CAPABILITIES(handler, 0, 0).get() for _ in range(200)
    ]
    results = await utils.apply(*many_p_capabilities)
    print(results)


# %%
def main():
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(test_command())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
