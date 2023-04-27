import asyncio

from xoa_driver import testers
from xoa_driver import modules

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 0
PORT_IDS =[0,1]

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME) 
    my_module = my_tester.modules.obtain(MODULE_ID)
    
    # get access to port 0 and 1
    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(*PORT_IDS)

if __name__ == "__main__":
    asyncio.run(main())