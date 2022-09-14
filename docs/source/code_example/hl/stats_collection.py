import asyncio

# import available testers
from xoa_driver import testers
# import available modules type
from xoa_driver import modules
# import available port type
from xoa_driver import ports

from xoa_driver import utils, enums

async def my_awesome_script():
    # my code ...
    tester = await testers.L23Tester("192.168.1.200", "JonDoe") # create tester instance and establish connection
    my_module = tester.modules.obtain(0)

    if isinstance(my_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module

    ( tx_port, rx_port ) = resources = my_module.ports.obtain_multiple(0,1)

    for port in resources:
        if port.is_reserved_by_me(): # check if we can set parameters to selected port
            continue
        if not port.is_released():
            await port.reservation.set_relinquish() # send relinquish the port
        await port.reservation.set_reserve() # set reservation , means port will be controlled by our session

    my_stream = await tx_port.streams.create() # Create one stream on the port
    my_stream_2 = await tx_port.streams.create() # Create one stream on the port

    await utils.apply(
        my_stream.tpld_id.set(0), # Create the TPLD index of stream
        my_stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000), # Configure the packet size
        my_stream.enable.set_on(), # Enable streams
        my_stream.rate.fraction.set(stream_rate_ppm=500000), # Configure the stream rate
        my_stream.packet.limit.set(packet_count=10000),
        my_stream_2.tpld_id.set(1),
        my_stream_2.packet.length.set(length_type=enums.LengthType.INCREMENTING, min_val=100, max_val=1000), # Configure the packet size
        my_stream_2.enable.set_on(), # Enable streams
        my_stream_2.rate.fraction.set(stream_rate_ppm=500000), # Configure the stream rate
        my_stream_2.packet.limit.set(packet_count=10000)
    )

    # clear Tx port statistics
    await utils.apply(
        tx_port.statistics.tx.clear.set(),
        tx_port.statistics.rx.clear.set()
    )

    # clear Rx port statistics
    await utils.apply(
        rx_port.statistics.tx.clear.set(),
        rx_port.statistics.rx.clear.set()
    )
    
    # start traffic on the Tx port
    await tx_port.traffic.state.set_start()

    # let traffic runs for 10 seconds
    await asyncio.sleep(10)

    # stop traffic on the Tx port
    await tx_port.traffic.state.set_stop()

    # collect statistics
    print("------------------------------------------------------------")

    # port level TX stats
    tx_port_stats =  await tx_port.statistics.tx.total.get()

    # # let the resource manager tell you the stream index so you don't have to remember it:
    tx_stream0_stats = await tx_port.statistics.tx.obtain_from_stream(my_stream).get()
    tx_stream1_stats = await tx_port.statistics.tx.obtain_from_stream(my_stream_2).get()

    # if you want, you can also simply use the index value as shown below:
    # tx_stream0_stats = await tx_port.statistics.tx.obtain_from_stream(0).get()
    # tx_stream1_stats = await tx_port.statistics.tx.obtain_from_stream(1).get()

    print(f"TX Port.Byte_Count: {tx_port_stats.byte_count_since_cleared}")
    print(f"TX Port.Packet_Count: {tx_port_stats.packet_count_since_cleared}")
    print(f"TX Stream[0].Byte_Count: {tx_stream0_stats.byte_count_since_cleared}")
    print(f"TX Stream[0].Packet_Count: {tx_stream0_stats.packet_count_since_cleared}")
    print(f"TX Stream[1].Byte_Count: {tx_stream1_stats.byte_count_since_cleared}")
    print(f"TX Stream[1].Packet_Count: {tx_stream1_stats.packet_count_since_cleared}")

    rx_port_stats = await rx_port.statistics.rx.total.get()
    
    # if you have forgot what TPLD ID assigned to a stream, you can query it 
    rx_stream0_tpld_obj = await my_stream.tpld_id.get()
    rx_stream1_tpld_obj = await my_stream_2.tpld_id.get()

    # after fetching the TPLD object of the stream, you can access it value and use it to query the port's RX counter of that stream.
    rx_stream0_stats = await rx_port.statistics.rx.access_tpld(rx_stream0_tpld_obj.test_payload_identifier).traffic.get()
    rx_stream1_stats = await rx_port.statistics.rx.access_tpld(rx_stream1_tpld_obj.test_payload_identifier).traffic.get()

    # if you know the TPLD ID of the stream that you want to get the RX counters, you can also simply provide the TPLD ID value: 
    # rx_stream0_stats = await rx_port.statistics.rx.access_tpld(0).traffic.get()
    # rx_stream1_stats = await rx_port.statistics.rx.access_tpld(1).traffic.get()

    print(f"RX Port.Byte_Count: {rx_port_stats.byte_count_since_cleared}")
    print(f"RX Port.Packet_Count: {rx_port_stats.packet_count_since_cleared}")
    print(f"RX Stream[0].Byte_Count: {rx_stream0_stats.byte_count_since_cleared}")
    print(f"RX Stream[0].Packet_Count: {rx_stream0_stats.packet_count_since_cleared}")
    print(f"RX Stream[1].Byte_Count: {rx_stream1_stats.byte_count_since_cleared}")
    print(f"RX Stream[1].Packet_Count: {rx_stream1_stats.packet_count_since_cleared}")
    print("------------------------------------------------------------")


def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_script())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()