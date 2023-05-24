import asyncio
from xoa_driver import testers
from xoa_driver import modules
from xoa_driver.enums import *
from xoa_driver.hlfuncs import mgmt

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 0
PORT1_ID = 1
PORT2_ID = 3

TRAFFIC_DURATION = 180  # Three minutes

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
    print(f"Connecting to chassis: {CHASSIS_IP}, username: {USERNAME}")
    my_tester = await testers.L23Tester(CHASSIS_IP, USERNAME)


    my_module = my_tester.modules.obtain(MODULE_ID)

    # commands which used in this example are not supported by Chimera Module
    if isinstance(my_module, modules.ModuleChimera):
        return None

    ( port1, port2 ) = resources = my_module.ports.obtain_multiple(PORT1_ID, PORT2_ID)

    print(f"Reserve and reset port {MODULE_ID}/{PORT1_ID}")
    print(f"Reserve and reset port {MODULE_ID}/{PORT2_ID}")
    for port in resources:
        await mgmt.reserve_port(port)
        await mgmt.reset_port(port)


    # Create one stream on the port
    print(f"Creating a stream on port {MODULE_ID}/{PORT1_ID}")
    my_stream1 = await port1.streams.create()
    # Create one stream on the port
    print(f"Creating a stream on port {MODULE_ID}/{PORT2_ID}")
    my_stream2 = await port2.streams.create()


    print(f"Configuring streams..")

    header_data1 = f'0x{DESTINATION_MAC}{SOURCE_MAC}{ETHERNET_TYPE}{VLAN}'
    header_data2 = f'0x{DESTINATION_MAC2}{SOURCE_MAC2}{ETHERNET_TYPE2}{VLAN2}'

    await asyncio.gather(
        # Create the TPLD index of stream
        my_stream1.tpld_id.set(0),
        # Configure the packet size
        my_stream1.packet.length.set(length_type=LengthType.FIXED, min_val=1000, max_val=1000),
        my_stream1.packet.header.protocol.set(segments=[
                ProtocolOption.ETHERNET,
                ProtocolOption.VLAN
                ]),
        # Enable streams
        my_stream1.enable.set_on(),
        # Configure the stream rate
        # my_stream1.rate.fraction.set(stream_rate_ppm=100000),
        # my_stream1.rate.l2bps.set(l2_bps=1e9),
        my_stream1.rate.pps.set(stream_rate_pps=1000),
        # my_stream.packet.limit.set(packet_count=10000),
        my_stream1.packet.header.data.set(hex_data=header_data1),

        my_stream2.tpld_id.set(1),
        # Configure the packet size
        my_stream2.packet.length.set(length_type=LengthType.INCREMENTING, min_val=100, max_val=1000),
        my_stream2.packet.header.protocol.set(segments=[
                ProtocolOption.ETHERNET,
                ProtocolOption.VLAN
                ]),
        # Enable streams
        my_stream2.enable.set_on(),
        # Configure the stream rate
        # my_stream2.rate.fraction.set(stream_rate_ppm=100000),
        # my_stream2.rate.l2bps.set(l2_bps=1e9),
        my_stream2.rate.pps.set(stream_rate_pps=1000),
        # my_stream2.packet.limit.set(packet_count=10000),
        my_stream2.packet.header.data.set(hex_data=header_data2),
    )

    # clear port statistics
    print(f"Clearing statistics")
    await asyncio.gather(
        port1.statistics.tx.clear.set(),
        port1.statistics.rx.clear.set(),
        port2.statistics.tx.clear.set(),
        port2.statistics.rx.clear.set()
    )

    # start traffic on the ports
    print(f"Starting traffic")
    await asyncio.gather(
        port1.traffic.state.set_start(),
        port2.traffic.state.set_start()
    )

    # # let traffic runs for 10 seconds
    print(f"Wait for {TRAFFIC_DURATION} seconds...")
    await asyncio.sleep(TRAFFIC_DURATION)

    # # stop traffic on the Tx port
    print(f"Stopping traffic..")
    await asyncio.gather(
        port1.traffic.state.set_stop(),
        port2.traffic.state.set_stop()
    )
    await asyncio.sleep(2)

    # collect statistics
    print(f"Collecting statistics..")

    (p1_tx, p1_rx, p2_tx, p2_rx) = await asyncio.gather(
        port1.statistics.tx.obtain_from_stream(0).get(),
        port1.statistics.rx.access_tpld(1).traffic.get(),
        port2.statistics.tx.obtain_from_stream(0).get(),
        port2.statistics.rx.access_tpld(0).traffic.get(),
    )
    print(f"Port 1")
    print(f"  TX(tid=0).Byte_Count: {p1_tx.byte_count_since_cleared}")
    print(f"  TX(tid=0).Packet_Count: {p1_tx.packet_count_since_cleared}")
    print(f"  RX(tid=1).Byte_Count: {p1_rx.byte_count_since_cleared}")
    print(f"  RX(tid=1).Packet_Count: {p1_rx.packet_count_since_cleared}")

    print(f"Port 2")
    print(f"  TX(tid=1).Byte_Count: {p2_tx.byte_count_since_cleared}")
    print(f"  TX(tid=1).Packet_Count: {p2_tx.packet_count_since_cleared}")
    print(f"  RX(tid=0).Byte_Count: {p2_rx.byte_count_since_cleared}")
    print(f"  RX(tid=0).Packet_Count: {p2_rx.packet_count_since_cleared}")

    print(f"Frame Loss (TX-RX)")
    print(f"  Port 1->Port 2 (tid=0): {p1_tx.packet_count_since_cleared - p2_rx.packet_count_since_cleared}")
    print(f"  Port 2->Port 1 (tid=1): {p2_tx.packet_count_since_cleared - p1_rx.packet_count_since_cleared}")

    # free ports
    print(f"Free ports")
    for port in resources:
        await mgmt.free_port(port)

    # done
    print(f"Test done")

if __name__ == "__main__":
    asyncio.run(main())