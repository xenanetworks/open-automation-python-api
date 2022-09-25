import asyncio

# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

from xoa_driver import utils, enums

async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") 

    # access module 0 on the tester
    my_module = tester.modules.obtain(0)

    if isinstance(my_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module

    # access port 0 on the module as the TX port
    tx_port = my_module.ports.obtain(0)

    # check TX port's reservation's status, and reserve it
    if tx_port.is_released():
        await tx_port.reservation.set_reserve() # set reservation , means port will be controlled by our session
    elif not tx_port.is_reserved_by_me():
        await tx_port.reservation.set_relinquish() # send relinquish the port
        await tx_port.reservation.set_reserve() # set reservation , means port will be controlled by our session
    
    await tx_port.reset.set()

    my_stream = await tx_port.streams.create() # Create one stream on the port
    my_stream_2 = await tx_port.streams.create() # Create one stream on the port

    await utils.apply(
        my_stream.tpld_id.set(0), # Create the TPLD index of stream
        my_stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000), # Configure the packet size
        my_stream.enable.set_on(), # Enable streams
        my_stream.rate.fraction.set(stream_rate_ppm=500000), # Configure the stream rate
        my_stream_2.tpld_id.set(1),
        my_stream_2.packet.length.set(length_type=enums.LengthType.INCREMENTING, min_val=100, max_val=1000), # Configure the packet size
        my_stream_2.enable.set_on(), # Enable streams
        my_stream_2.rate.fraction.set(stream_rate_ppm=500000), # Configure the stream rate
    )

    await my_stream_2.delete() # delete a stream

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