import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import utils, enums

async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("192.168.1.200", "xoa") 
    my_module = tester.modules.obtain(0)

    # commands which used in this example are not supported by Chimera Module
    if isinstance(my_module, modules.ModuleChimera):
        return None 

    if my_module.is_released():
        # set reservation , means port will be controlled by our session
        await my_module.reservation.set_reserve() 
    elif not my_module.is_reserved_by_me():
        # send relinquish the module
        await my_module.reservation.set_relinquish()
        # set reservation , means module will be controlled by our session
        await my_module.reservation.set_reserve() 

    # set module config
    my_module.media.set(media_type=enums.MediaConfigurationType.QSFP56_PAM4)

    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0, 1)

    for port in resources:
        # check if we can set parameters to selected port
        if port.is_reserved_by_me(): 
            continue
        if not port.is_released():
            # send relinquish the port
            await port.reservation.set_relinquish() 
        # set reservation , means port will be controlled by our session
        await port.reservation.set_reserve() 
    
    await utils.apply(
        # set latency mode of the Tx port
        tx_port.latency_config.mode.set(mode = enums.LatencyMode.LAST2LAST),
        # set an comment of the Tx port
        tx_port.comment.set("My Tx port") 
        )

    await utils.apply(
        # set latency mode of the Rx port
        rx_port.latency_config.mode.set(mode = enums.LatencyMode.LAST2LAST), 
        # set an comment of the Rx port
        rx_port.comment.set("My Rx port") 
    )

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()