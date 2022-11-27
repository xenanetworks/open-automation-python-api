import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("192.168.1.200", "xoa") 
    my_module = tester.modules.obtain(0)

    # commands which used in this example are not supported by Chimera Module
    if isinstance(my_module, modules.ModuleChimera):
        return None 

    # Querying module current media configuration
    print(await my_module.media.get()) 

    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0, 1)

    for port in resources:
        # Querying port supported speed modes
        print(await port.speed.mode.supported.get()) 
        # Querying port current speed mode
        print(await port.speed.mode.selection.get()) 

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()