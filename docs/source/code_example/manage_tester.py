import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils

async def my_awesome_script():
    # Establish connection to a Valkyrie tester
    async with testers.L23Tester("10.10.10.10", "JonDoe") as tester:
        # Get the port 0/0 (module 0)
        port = await tester.modules.obtain(0).ports.obtain(0)

        # Reserve the port
        await port.reservation.set_reserve()

        # Reset the port
        await port.reset.set()

        # Create a stream on the port
        stream = await port.streams.create()

        # Prepare stream header protocol
        header_protocol = [enums.ProtocolOption.ETHERNET, enums.ProtocolOption.IP]

        # Batch configure the stream
        await utils.apply(
            stream.tpld_id.set(0), # Create the TPLD index of stream
            stream.packet.length.set(*size), # Configure the packet size
            stream.packet.header.protocol.set(header_protocol), # Configure the packet type
            stream.packet.header.data.set(header), # Configure the packet header
            stream.enable.set_on(), # Enable streams
            stream.rate.fraction.set(1000000) # Configure the stream rate 100%
        )

        # Clear statistics
        await utils.apply(
            port.statistics.tx.clear.set(),
            port.statistics.rx.clear.set()
        )

        # Start traffic on the port
        await port.traffic.state.set_start()

        # Test duration 10 seconds
        await asyncio.sleep(10)

        # Query TX statistics
        tx_result = await port.statistics.tx.total.get()
        print(f"bit count last second: {tx_result.bit_count_last_sec}")
        print(f"packet count last second: {tx_result.packet_count_last_sec}")
        print(f"byte count since cleared: {tx_result.byte_count_since_cleared}")
        print(f"packet count since cleared: {tx_result.packet_count_since_cleared}")

        # Stop traffic on the port
        await port.traffic.state.set_stop()

        # Release the port
        await port.reservation.set_release()

def main():
    try:
        loop = asyncio.get_event_loop()
        loop.create_task(my_awesome_script())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    if __name__ == "__main__":
        main()
