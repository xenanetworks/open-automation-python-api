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
        if port.is_reserved_by_me(): # check if we can set parameters to selected port
            continue
        if not port.is_released():
            await port.reservation.set_relinquish() # send relinquish the port
        await port.reservation.set_reserve() # set reservation , means port will be controlled by our session
    await tx_port.comment.set("My Tx port") # set an comment to the Tx port
    await rx_port.comment.set("My Rx port") # set an comment to the Rx port
    # other code ...