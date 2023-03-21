import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester("192.168.1.200", "xoa") 
    my_module = my_tester.modules.obtain(0)
    
    # get access to port 0 and 1
    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0, 1)

if __name__ == "__main__":
    asyncio.run(main())