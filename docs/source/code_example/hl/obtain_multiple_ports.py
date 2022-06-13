# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

async def my_awesome_script():
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_test_module = tester.modules.obtain(0)
    ( tx_port, rx_port ) = resources = my_test_module.ports.obtain_multiple(0, 1)
    # other code ...