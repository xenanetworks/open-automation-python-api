import asyncio

async def background_task(tx_port: "ports.GenericL23Port", rx_port: "ports.GenericL23Port"):
    while True:
        print(await tx_port.statistics.tx.total.get())
        print(await rx_port.statistics.rx.total.get())
        await async.sleep(1)

async def my_awesome_script():
    # my code ...
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0)
    if isinstance(my_test_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module
    ( tx_port, rx_port ) = resources = my_test_module.ports.obtain_multiple(0, 1)
    
    asyncio.create_task(background_task(tx_port, rx_port)) # put function to work in the background
    print("Task working in background")

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_script())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()