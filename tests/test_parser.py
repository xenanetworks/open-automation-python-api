from __future__ import annotations

import asyncio
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from xoa_driver.lli import establish_connection  # noqa: E402
from xoa_driver.lli import commands  # noqa: E402
from xoa_driver.lli import TransportationHandler  # noqa: E402
# TODO: <GET> response contain more fields then driver can parse
# TODO: <GET> response contains less fields then driver can parse
# TODO: <SET> request require more fields then server expecting
# TODO: <SET> request require less fields then server expects


async def main() -> None:
    print("start")
    ctx = TransportationHandler(debug=False)
    print("Create handler")
    await establish_connection(ctx, "192.168.1.198")
    print("Is connected", ctx.is_connected)
    await commands.C_LOGON(ctx).set("xena")
    await commands.C_OWNER(ctx).set("xoa")

if __name__ == "__main__":
    asyncio.run(main())
