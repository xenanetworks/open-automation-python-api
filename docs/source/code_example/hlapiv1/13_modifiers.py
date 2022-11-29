import asyncio

import socket
from binascii import hexlify

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import utils, enums


async def my_awesome_func():
    # create tester instance and establish connection
    tester = await testers.L23Tester("192.168.1.200", "xoa") 

    # access module 0 on the tester
    my_module = tester.modules.obtain(0)

    if isinstance(my_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module

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

    SMAC = '000000000001'
    DMAC = '000000000002'
    ETHERTYPE = '0800'
    header_data = f'0x{DMAC}{SMAC}{ETHERTYPE}'

    await utils.apply(
        # Create the TPLD index of stream
        my_stream.tpld_id.set(0), 
        # Configure the packet size
        my_stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000),
        # Enable stream
        my_stream.enable.set_on(), 
        # Configure the stream rate
        my_stream.rate.fraction.set(stream_rate_ppm=500000), 

        # Configure the packet type
        my_stream.packet.header.protocol.set(segments=[enums.ProtocolOption.ETHERNET, enums.ProtocolOption.IP]),
        # Configure the packet header data
        my_stream.packet.header.data.set(hex_data = header_data) 
    )

    # create one modifier and configure
    await my_stream.packet.header.modifiers.configure(1)
    # access the created modifier
    my_modifier = my_stream.packet.header.modifiers.index(0)
    # configure the modifier
    # place the modifier on header position 0
    await my_modifier.specification.set(position=0, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier.range.set(min_val=0, step=1, max_val=65535)

    # to create another modifier, you need to re-configure all modifiers again
    await my_stream.packet.header.modifiers.configure(2)

    my_modifier = my_stream.packet.header.modifiers.index(0)
    # place the first modifier on header position 0
    await my_modifier.specification.set(position=0, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier.range.set(min_val=0, step=1, max_val=65535)

    my_modifier_2 = my_stream.packet.header.modifiers.index(1)
    # place the second modifier on header position 6
    await my_modifier_2.specification.set(position=6, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier_2.range.set(min_val=0, step=1, max_val=65535)

    # to delete the first modifier, you need to re-configure all modifiers again
    await my_stream.packet.header.modifiers.configure(1)
    
    my_modifier = my_stream.packet.header.modifiers.index(0)
    # place the modifier on header position 0
    await my_modifier.specification.set(position=6, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier.range.set(min_val=0, step=1, max_val=65535)

    # to delete all modifiers
    await my_stream.packet.header.modifiers.configure(0)

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_func())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()