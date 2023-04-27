import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import utils, enums
from xoa_driver.hlfuncs import mgmt

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 0
PORT_IDS = [0,1]

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME)

    # access module 0 on the tester
    my_module = my_tester.modules.obtain(MODULE_ID)

    # commands which used in this example are not supported by Chimera Module
    if isinstance(my_module, modules.ModuleChimera):
        return None 

    await mgmt.reserve_module(my_module)

    # set module config
    await my_module.media.set(media_config=enums.MediaConfigurationType.QSFP56_PAM4)

    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(*PORT_IDS)

    # use high-level func to reserve the port
    for port in resources:
        await mgmt.reserve_port(port)
    
    await utils.apply(
        # set latency mode of the Tx port
        tx_port.latency_config.mode.set(mode = enums.LatencyMode.LAST2LAST),
        # set an comment of the Tx port
        tx_port.comment.set("My Tx port") 
        )

    await utils.apply(
        # set latency mode of the Rx port
        rx_port.latency_config.mode.set(mode = enums.LatencyMode.LAST2LAST), 
        # set an comment of the Rx port
        rx_port.comment.set("My Rx port") 
    )

if __name__ == "__main__":
    asyncio.run(main())