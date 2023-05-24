import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver.hlfuncs import mgmt

CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "xoa"
MODULE_ID = 2
PORT_ID = 2

async def main():
    # Establish connection to a Valkyrie tester
    async with testers.L23Tester(CHASSIS_IP, USERNAME) as my_tester:
        my_module = my_tester.modules.obtain(MODULE_ID)

        # commands which used in this example are not supported by Chimera Module
        if isinstance(my_module, modules.ModuleChimera):
            return None 

        # Get the port 2/2 (module 2)
        my_port = my_module.ports.obtain(PORT_ID)

        # use high-level func to reserve the port
        await mgmt.reserve_port(my_port)

        # Reset the port
        await my_port.reset.set()

        await asyncio.sleep(10)

        # Read transceiver's temperature
        temperature = await my_port.transceiver.access_temperature.get()
        print(f"Transceiver temperature: {temperature.integral_part + temperature.fractional_part/256} degrees Celsius.")
        
        # Read transceiver's register value (single read)
        rx_power_lsb = await my_port.transceiver.access_rw(page_address=0xA2, register_address=0x69).get()
        print(rx_power_lsb)

        # Write transceiver's register value (single write)
        await my_port.transceiver.access_rw(page_address=0xA2, register_address=0x69).set("0xFFFF")

        # Read MII transceiver's register value (single operation)
        rx_power_lsb = await my_port.transceiver.access_mii(register_address=0x69).get()
        print(rx_power_lsb)

        # Write MII transceiver's register value (single operation)
        await my_port.transceiver.access_mii(register_address=0x69).set("0xFFFF")

        # Read transceiver's register value (sequential read)
        i2c_read = await my_port.transceiver.access_rw_seq(page_address=0xA2, register_address=0x69, byte_count=16).get()
        print(i2c_read)

        # Write transceiver's register value (sequential write)
        await my_port.transceiver.access_rw_seq(page_address=0xA2, register_address=0x69, byte_count=16).set("0xFFFF")

        # Release the port
        await my_port.reservation.set_release()

if __name__ == "__main__":
    asyncio.run(main())
