import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils

async def my_awesome_func():
    # Establish connection to a Valkyrie tester 10.10.10.10 with username JonDoe.
    async with testers.L23Tester("10.10.10.10", "JonDoe") as tester:
        
        my_module = tester.modules.obtain(0)

        if isinstance(my_module, modules.ModuleChimera):
            return None # commands which used in this example are not supported by Chimera Module

        # Get the port 0/0 as TX port
        my_tx_port = my_module.ports.obtain(0)
        # Get the port 0/0 as RX port
        my_rx_port = my_module.ports.obtain(1)

        # Reserve the TX port and reset it.
        if my_tx_port.is_reserved_by_me():
            await my_tx_port.reservation.set_release()
        elif not my_tx_port.is_released():
            await my_tx_port.reservation.set_relinquish()
        await utils.apply(
            my_tx_port.reservation.set_reserve(),
            my_tx_port.reset.set()
        )

        # Reserve the RX port and reset it.
        if my_rx_port.is_reserved_by_me():
            await my_rx_port.reservation.set_release()
        elif not my_rx_port.is_released():
            await my_rx_port.reservation.set_relinquish()
        await utils.apply(
            my_rx_port.reservation.set_reserve(),
            my_rx_port.reset.set()
        )

        # Create a stream on the TX port
        my_stream = await my_tx_port.streams.create()
        my_tpld_value = 0

        # Prepare stream header protocol
        header_protocol = [enums.ProtocolOption.ETHERNET, enums.ProtocolOption.IP]

        # Simple batch configure the stream on the TX port
        await utils.apply(
            my_stream.tpld_id.set(my_tpld_value), # Create the TPLD index of stream
            my_stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000), # Configure the packet size to fixed 1000 bytes
            my_stream.packet.header.protocol.set(header_protocol), # Configure the packet type
            my_stream.enable.set_on(), # Enable streams
            my_stream.rate.fraction.set(1000000) # Configure the stream rate 100% (1,000,000 ppm)
        )

        # Batch clear statistics on TX and RX ports
        await asyncio.gather(
            my_tx_port.statistics.tx.clear.set(),
            my_tx_port.statistics.rx.clear.set(),
            my_rx_port.statistics.tx.clear.set(),
            my_rx_port.statistics.rx.clear.set()
        )

        # Start traffic on the TX port
        await my_tx_port.traffic.state.set_start()

        # Test duration 10 seconds
        await asyncio.sleep(10)

        # Stop traffic on the TX port
        await my_tx_port.traffic.state.set_stop()

        # Wait 2 seconds for the counters to finish
        await asyncio.sleep(2)

        # Query TX statistics
        tx_results = list(await utils.apply(
            my_tx_port.statistics.tx.total.get(),

            # let the resource manager tell you the stream index so you don't have to remember it
            my_tx_port.statistics.tx.obtain_from_stream(my_stream).get()
        ))
        print(f"Total TX byte count since cleared: {tx_results[0].byte_count_since_cleared}")
        print(f"Total TX packet count since cleared: {tx_results[0].packet_count_since_cleared}")
        print(f"Stream 0 TX byte count since cleared: {tx_results[1].byte_count_since_cleared}")
        print(f"Stream 0 TX packet count since cleared: {tx_results[1].packet_count_since_cleared}")

        # if you have forgot what TPLD ID assigned to a stream, you can query it 
        tpld_obj = await my_stream.tpld_id.get()
        # then access the RX stat object
        rx_stats_obj = my_rx_port.statistics.rx.access_tpld(tpld_obj.test_payload_identifier)
        # then query each stats of a TPLD ID
        rx_results = list(await utils.apply(
            my_rx_port.statistics.rx.total.get(),
            rx_stats_obj.traffic.get(),
            rx_stats_obj.latency.get(),
            rx_stats_obj.jitter.get(),
            rx_stats_obj.errors.get()
        ))

        print(f"Total RX byte count since cleared: {rx_results[0].byte_count_since_cleared}")
        print(f"Total RX packet count since cleared: {rx_results[0].packet_count_since_cleared}")
        print(f"Stream 0 RX byte count since cleared: {rx_results[1].byte_count_since_cleared}")
        print(f"Stream 0 RX packet count since cleared: {rx_results[1].packet_count_since_cleared}")
        print(f"Stream 0 RX min latency: {rx_results[2].min_val}")
        print(f"Stream 0 RX max latency: {rx_results[2].max_val}")
        print(f"Stream 0 RX avg latency: {rx_results[2].avg_val}")
        print(f"Stream 0 RX min jitter: {rx_results[3].min_val}")
        print(f"Stream 0 RX max jitter: {rx_results[3].max_val}")
        print(f"Stream 0 RX avg jitter: {rx_results[3].avg_val}")
        print(f"Stream 0 RX number of non-incrementing-sequence-number events: {rx_results[4].non_incre_seq_event_count}")
        print(f"Stream 0 RX number of swapped-sequence-number misorder events: {rx_results[4].swapped_seq_misorder_event_count}")
        print(f"Stream 0 RX number of packets with non-incrementing payload content: {rx_results[4].non_incre_payload_packet_count}")

        # Release the ports
        await asyncio.gather(
            my_tx_port.reservation.set_release(),
            my_rx_port.reservation.set_release()
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
