# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0)
    if isinstance(my_test_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module
    ( tx_port, rx_port ) = resources = my_test_module.ports.obtain_multiple(0, 1)
    for port in resources:
        print(await port.speed.supported.get()) # Querying port supported speeds
    # other code ...