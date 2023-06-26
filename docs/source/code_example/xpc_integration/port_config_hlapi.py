import asyncio
from contextlib import suppress
import ipaddress

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils
from xoa_driver import exceptions
from xoa_driver.hlfuncs import mgmt, cli

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 0
PORT_ID = 0

async def main():
    # create tester instance and establish connection
    async with testers.L23Tester(CHASSIS_IP, USERNAME) as tester:

        # access module 0 on the tester
        module = tester.modules.obtain(MODULE_ID)

        if isinstance(module, modules.ModuleChimera):
            return None # commands which used in this example are not supported by Chimera Module

        # access port 0 on the module as the TX port
        port = module.ports.obtain(PORT_ID)

        #---------------------------
        # Port reservation
        #---------------------------
        # use high-level func to reserve the port
        await mgmt.reserve_port(port)

        await cli.port_config_from_file(port, "port_config.xpc")

        # use high-level func to reserve the port
        await mgmt.free_port(port)


if __name__ == "__main__":
    asyncio.run(main())