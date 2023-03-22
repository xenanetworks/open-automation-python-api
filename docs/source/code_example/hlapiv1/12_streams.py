import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import utils, enums
from xoa_driver.hlfuncs import mgmt

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 0
PORT_ID = 0

DESTINATION_MAC =   "AAAAAAAAAAAA"
SOURCE_MAC =        "BBBBBBBBBBBB"
ETHERNET_TYPE =     "8100"
VLAN = "0000FFFF"

DESTINATION_MAC2 =   "BBBBBBBBBBBB"
SOURCE_MAC2 =        "AAAAAAAAAAAA"
ETHERNET_TYPE2 =     "8100"
VLAN2 = "0010FFFF"

async def main():
    # create tester instance and establish connection
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME)

    # access module 0 on the tester
    my_module = my_tester.modules.obtain(MODULE_ID)

    # commands which used in this example are not supported by Chimera Module
    if isinstance(my_module, modules.ModuleChimera):
        return None 

    # access port 0 on the module as the TX port
    tx_port = my_module.ports.obtain(PORT_ID)

    # use high-level func to reserve the port
    await mgmt.reserve_port(tx_port)
    
    # reset the port
    await mgmt.reset_port(tx_port)

    # create one stream on the port
    my_stream1 = await tx_port.streams.create()
    # create one stream on the port
    my_stream2 = await tx_port.streams.create() 

    header_data1 = f'0x{DESTINATION_MAC}{SOURCE_MAC}{ETHERNET_TYPE}{VLAN}'
    header_data2 = f'0x{DESTINATION_MAC2}{SOURCE_MAC2}{ETHERNET_TYPE2}{VLAN2}'

    await utils.apply(
        # Create the TPLD index of stream
        my_stream1.tpld_id.set(0), 
        # Configure the packet size
        my_stream1.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000), 
        # Enable streams
        my_stream1.enable.set_on(), 
        # Configure the stream rate
        my_stream1.rate.fraction.set(stream_rate_ppm=500000),
        # Configure the stream packet header protocol
        my_stream1.packet.header.protocol.set(segments=[enums.ProtocolOption.ETHERNET, enums.ProtocolOption.VLAN]),
        # Configure the stream packet header value
        my_stream1.packet.header.data.set(hex_data=header_data1),

        # Configure TPLD ID
        my_stream2.tpld_id.set(1),
        # Configure the packet size
        my_stream2.packet.length.set(length_type=enums.LengthType.INCREMENTING, min_val=100, max_val=1000), 
        # Enable streams
        my_stream2.enable.set_on(), 
        # Configure the stream rate
        my_stream2.rate.fraction.set(stream_rate_ppm=500000), 
        # Configure the stream packet header protocol
        my_stream2.packet.header.protocol.set(segments=[enums.ProtocolOption.ETHERNET, enums.ProtocolOption.VLAN]),
        # Configure the stream packet header value
        my_stream2.packet.header.data.set(hex_data=header_data2)
    )

if __name__ == "__main__":
    asyncio.run(main())