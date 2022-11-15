import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def my_awesome_func():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    
    my_module = tester.modules.obtain(0)
    
    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0, 1)
    # other code ...


def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()