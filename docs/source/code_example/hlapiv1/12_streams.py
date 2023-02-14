import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import utils, enums

async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("10.20.1.170", "xoa") 

    # access module 0 on the tester
    my_module = tester.modules.obtain(0)

    # commands which used in this example are not supported by Chimera Module
    if isinstance(my_module, modules.ModuleChimera):
        return None 

    # access port 0 on the module as the TX port
    tx_port = my_module.ports.obtain(0)

    # check TX port's reservation's status, and reserve it
    if tx_port.is_released():
        # set reservation , means port will be controlled by our session
        await tx_port.reservation.set_reserve() 
    elif not tx_port.is_reserved_by_me():
        # send relinquish the port
        await tx_port.reservation.set_relinquish()
        # set reservation , means port will be controlled by our session
        await tx_port.reservation.set_reserve() 
    
    # reset the port
    await tx_port.reset.set()

    # create one stream on the port
    my_stream = await tx_port.streams.create()
    # create one stream on the port
    my_stream_2 = await tx_port.streams.create() 

    await utils.apply(
        # Create the TPLD index of stream
        my_stream.tpld_id.set(0), 
        # Configure the packet size
        my_stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000), 
        # Enable streams
        my_stream.enable.set_on(), 
        # Configure the stream rate
        my_stream.rate.fraction.set(stream_rate_ppm=500000),

        # Configure TPLD ID
        my_stream_2.tpld_id.set(1),
        # Configure the packet size
        my_stream_2.packet.length.set(length_type=enums.LengthType.INCREMENTING, min_val=100, max_val=1000), 
        # Enable streams
        my_stream_2.enable.set_on(), 
        # Configure the stream rate
        my_stream_2.rate.fraction.set(stream_rate_ppm=500000), 
        # Configure the stream packet header protocol
        my_stream_2.packet.header.protocol.set(segments=[enums.ProtocolOption.ETHERNET, enums.ProtocolOption.VLAN, enums.ProtocolOption.UDP]),
        # Configure the stream packet header value
        my_stream_2.packet.header.data.set(hex_data="0x00000000000004F4BC94DAE081000000FFFF00000000002A0000")
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