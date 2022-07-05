import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils

async def my_awesome_script():
    # Establish connection to a Valkyrie tester 10.10.10.10 with username JonDoe.
    async with testers.L23Tester("10.10.10.10", "JonDoe") as tester:
        
        # Get the port 0/0 (module 0)
        my_port = await tester.modules.obtain(0).ports.obtain(0)

        # Reserve the port
        if my_port.is_released():
            await my_port.reservation.set_reserve()
        elif my_port.is_reserved_by_others():
            await my_port.reservation.set_relinquish()
            await my_port.reservation.set_reserve()

        # Reset the port
        await my_port.reset.set()

        # Create a stream on the port
        my_stream = await my_port.streams.create()

        # Prepare stream header protocol
        header_protocol = [enums.ProtocolOption.ETHERNET, enums.ProtocolOption.IP]

        # Batch configure the stream
        await utils.apply(
            my_stream.tpld_id.set(0), # Create the TPLD index of stream
            my_stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000), # Configure the packet size to fixed 1000 bytes
            my_stream.packet.header.protocol.set(header_protocol), # Configure the packet type
            my_stream.enable.set_on(), # Enable streams
            my_stream.rate.fraction.set(1000000) # Configure the stream rate 100% (1,000,000 ppm)
        )

        # Batch Ccear statistics
        await utils.apply(
            my_port.statistics.tx.clear.set(),
            my_port.statistics.rx.clear.set()
        )

        # Start traffic on the port
        await my_port.traffic.state.set_start()

        # Test duration 10 seconds
        await asyncio.sleep(10)

        # Stop traffic on the port
        await my_port.traffic.state.set_stop()

        # Query TX statistics
        tx_result = await my_port.statistics.tx.total.get()
        print(f"TX bit count in the last second: {tx_result.bit_count_last_sec}")
        print(f"TX packet count lin the ast second: {tx_result.packet_count_last_sec}")
        print(f"TX byte count since cleared: {tx_result.byte_count_since_cleared}")
        print(f"TX packet count since cleared: {tx_result.packet_count_since_cleared}")

        # Release the port
        await my_port.reservation.set_release()

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_script())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
