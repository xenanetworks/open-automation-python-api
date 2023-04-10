import asyncio

from xoa_driver import testers
from xoa_driver import modules

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 0
PORT_IDS = [0,1]

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME) 
    my_module = my_tester.modules.obtain(MODULE_ID)

    # commands which used in this example are not supported by Chimera Module
    if isinstance(my_module, modules.ModuleChimera):
        return None 

    # Querying module current media configuration
    print(await my_module.media.get()) 

    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(*PORT_IDS)

    for port in resources:
        # Querying port supported speed modes
        print(await port.speed.mode.supported.get()) 
        # Querying port current speed mode
        print(await port.speed.mode.selection.get()) 

if __name__ == "__main__":
    asyncio.run(main())