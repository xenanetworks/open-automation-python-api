import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils
import time

async def my_awesome_script():
    # Establish connection to a Valkyrie tester
    async with testers.L23Tester("192.168.1.200", "xoa") as tester:

        my_module = tester.modules.obtain(2)

        if isinstance(my_module, modules.ModuleChimera):
            return None # commands which used in this example are not supported by Chimera Module

        # Get the port 2/2 (module 2)
        port = my_module.ports.obtain(2)

        # Reserve the port
        if port.is_released():
            await port.reservation.set_reserve()
        elif port.is_reserved_by_others():
            await port.reservation.set_relinquish()
            await asyncio.sleep(1)
            await port.reservation.set_reserve()

        # Reset the port
        await port.reset.set()

        await asyncio.sleep(10)

        # Read transceiver's temperature
        temperature = await port.transceiver.access_temperature.get()
        print(f"Transceiver temperature: {temperature.integral_part + temperature.fractional_part/256} degrees Celsius.")
        
        # Read transceiver's register value (single read)
        rx_power_lsb = await port.transceiver.access_rw(page_address=0xA2, register_address=0x69).get()
        print(rx_power_lsb)

        # Write transceiver's register value (single write)
        await port.transceiver.access_rw(page_address=0xA2, register_address=0x69).set("0xFFFF")

        # Read MII transceiver's register value (single operation)
        rx_power_lsb = await port.transceiver.access_mii(register_address=0x69).get()
        print(rx_power_lsb)

        # Write MII transceiver's register value (single operation)
        await port.transceiver.access_mii(register_address=0x69).set("0xFFFF")

        # Read transceiver's register value (sequential read)
        i2c_read = await port.transceiver.access_rw_seq(page_address=0xA2, register_address=0x69, byte_count=16).get()
        print(i2c_read)

        # Write transceiver's register value (sequential write)
        await port.transceiver.access_rw_seq(page_address=0xA2, register_address=0x69, byte_count=16).set("0xFFFF")

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
