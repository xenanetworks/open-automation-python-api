import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("192.168.1.200", "xoa") 
    my_module = tester.modules.obtain(0)
    
    # get access to port 0 and 1
    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0, 1)

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()