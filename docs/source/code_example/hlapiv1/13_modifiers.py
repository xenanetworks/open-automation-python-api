import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import utils, enums
from xoa_driver.hlfuncs import mgmt

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 0
PORT_ID = 0

SMAC = '000000000001'
DMAC = '000000000002'
ETHERTYPE = '0800'

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME) 

    # access module 0 on the tester
    my_module = my_tester.modules.obtain(MODULE_ID)

    if isinstance(my_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module

    # access port 0 on the module as the TX port
    tx_port = my_module.ports.obtain(PORT_ID)

    # use high-level func to reserve the port
    await mgmt.reserve_port(tx_port)
    
    # reset the port
    await tx_port.reset.set()

    # create one stream on the port
    my_stream = await tx_port.streams.create() 

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
    my_modifier = my_stream.packet.header.modifiers.obtain(0)
    # configure the modifier
    # place the modifier on header position 0
    await my_modifier.specification.set(position=0, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier.range.set(min_val=0, step=1, max_val=65535)

    # to create another modifier, you need to re-configure all modifiers again
    await my_stream.packet.header.modifiers.configure(2)

    my_modifier = my_stream.packet.header.modifiers.obtain(0)
    # place the first modifier on header position 0
    await my_modifier.specification.set(position=0, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier.range.set(min_val=0, step=1, max_val=65535)

    my_modifier_2 = my_stream.packet.header.modifiers.obtain(1)
    # place the second modifier on header position 6
    await my_modifier_2.specification.set(position=6, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier_2.range.set(min_val=0, step=1, max_val=65535)

    # to delete the first modifier, you need to re-configure all modifiers again
    await my_stream.packet.header.modifiers.configure(1)
    
    my_modifier = my_stream.packet.header.modifiers.obtain(0)
    # place the modifier on header position 0
    await my_modifier.specification.set(position=6, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1) 
    await my_modifier.range.set(min_val=0, step=1, max_val=65535)

    # to delete all modifiers
    await my_stream.packet.header.modifiers.configure(0)

if __name__ == "__main__":
    asyncio.run(main())