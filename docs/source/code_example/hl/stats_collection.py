import asyncio

# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules

from xoa_driver import utils, enums

async def background_task(tx_port: "ports.GenericL23Port", rx_port: "ports.GenericL23Port"):
    while True:
        print(await tx_port.statistics.tx.total.get())
        print(await rx_port.statistics.rx.total.get())
        await asyncio.sleep(1)

async def my_awesome_script():
    # my code ...
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_module = tester.modules.obtain(0)

    if isinstance(my_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module

    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0, 1)

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

    # clear Tx port statistics
    await utils.apply(
        tx_port.statistics.tx.clear(),
        tx_port.statistics.rx.clear()
    )

    # clear Rx port statistics
    await utils.apply(
        rx_port.statistics.tx.clear(),
        rx_port.statistics.rx.clear()
    )
    
    asyncio.create_task(background_task(tx_port, rx_port)) # put function to work in the background
    print("Task working in background")

    # start traffic on the Tx port
    await tx_port.traffic.state.set_start()

    # let traffic runs for 10 seconds
    await asyncio.sleep(10)

    # stop traffic on the Tx port
    await tx_port.traffic.state.set_stop()
