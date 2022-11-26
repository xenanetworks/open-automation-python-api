import asyncio

from xoa_driver import testers
from xoa_driver import modules

async def my_awesome_func():
    tester = await testers.L23Tester("192.168.1.200", "xoa") # create tester instance and establish connection

    my_module = tester.modules.obtain(0)

    if isinstance(my_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module

    print(await my_module.media.get()) # Querying module current media configuration

    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0, 1)

    for port in resources:
        print(await port.speed.mode.supported.get()) # Querying port supported speed modes
        print(await port.speed.mode.selection.get()) # Querying port current speed mode

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