import asyncio
from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import utils
from xoa_driver import misc
from xoa_driver.enums import *
from xoa_driver.hlfuncs import mgmt

CHASSIS_IP = "87.61.110.118"
USERNAME = "xoa"
MODULE_ID = 10
PORT_ID = 0

# --------------------------------------------------------------------------------------#
# function name: collect_statistics                                                     #
# This function collect Chimera's statistics on-the-fly.                                #
#                                                                                       #
# --------------------------------------------------------------------------------------#

async def collect_statistics(flow: misc.ImpairmentFlow, stop_event: asyncio.Event) -> None:
    print(f"Start collecting statistics by Chimera...")
    count = 0
    while not stop_event.is_set():
        (rx, total_drop) = await utils.apply(
            flow.statistics.rx.total.get(),
            flow.statistics.total.drop_packets.get()
        )
        print(f"{count}\t\t\tChimera total received frames: {rx.packet_count},\t\ttotal dropped: {total_drop.pkt_drop_count_total}")
        count+=1
        await asyncio.sleep(1.0)


async def my_awesome_func(stop_event: asyncio.Event) -> None:
    
    # Access to the chassis that has a Chimera module in
    async with testers.L23Tester(CHASSIS_IP, USERNAME) as tester:
        # Access the module #10
        my_module = tester.modules.obtain(MODULE_ID)

        # Check whether the module is a Chimera module
        if not isinstance(my_module, modules.ModuleChimera):
            print("Selected not a Chimera module.", "Exiting.")
            return None
        
        # Use port #0
        my_port = my_module.ports.obtain(PORT_ID)
        
        # use high-level func to reserve the port
        await mgmt.reserve_port(my_port)

        # Enable impairment on the port. If you don't do this, the port won't impair the incoming traffic.
        await my_port.emulate.set_on()
        
        # Use Flow #1 on this port. We will define a filter and configure impairment functions on it.
        flow_1 = my_port.emulation.flows[1]

        # Initializing the shadow copy of the filter. (If you don't know how Chimera impairment works, please read the Chimera's user manual)
        await flow_1.shadow_filter.initiating.set()
        # Enable the filter
        await flow_1.shadow_filter.enable.set_on()
        # Basic mode
        await flow_1.shadow_filter.use_basic_mode()
        # Description of the flow
        await flow_1.comment.set("On VLAN 20")

        # Query the mode of the filter (either basic or extended)
        filter = await flow_1.shadow_filter.get_mode()

        # Set up the filter to impair frames with VLAN Tag = 20 (using command grouping)
        if isinstance(filter, misc.BasicImpairmentFlowFilter):
            await utils.apply(
                # filter.ethernet.settings.set(use=FilterUse.OFF, action=InfoAction.INCLUDE),
                # filter.ethernet.src_address.set(use=OnOff.OFF, value="0x000000000000", mask="0xFFFFFFFFFFFF"),
                # filter.ethernet.dest_address.set(use=OnOff.OFF, value="0x000000000000", mask="0xFFFFFFFFFFFF"),
                filter.l2plus_use.set(use=L2PlusPresent.VLAN1),
                filter.vlan.settings.set(use=FilterUse.AND, action=InfoAction.INCLUDE),
                filter.vlan.inner.tag.set(use=OnOff.ON, value=20, mask="0x0FFF"),
                filter.vlan.inner.pcp.set(use=OnOff.OFF, value=0, mask="0x07"),
                # filter.vlan.outer.tag.set(use=OnOff.OFF, value=20, mask="0x0FFF"),
                # filter.vlan.outer.pcp.set(use=OnOff.OFF, value=0, mask="0x07"),
            )

        # Apply the filter so the configuration data in the shadow copy is committed to the working copy automatically.
        await flow_1.shadow_filter.apply.set()
        
        # Start configuring the impairment for the filter. (using command grouping)
        await utils.apply(
            # Latency/Jitter impairment (distribution: constant)
            flow_1.impairment_distribution.latency_jitter_type_config.constant_delay.set(20000), # 20,000 ns, must be multiples of 100
            flow_1.impairment_distribution.latency_jitter_type_config.schedule.set(1, 0), # continuously increase the latency 

            # Drop impairment (distribution: fixed burst)
            flow_1.impairment_distribution.drop_type_config.fixed_burst.set(burst_size=5), # drop a fixed burst size 5 frames
            flow_1.impairment_distribution.drop_type_config.schedule.set(1, 5), # drop is on for 10ms and pause for 40ms (total=50ms) (100 drops per second)
        )

        await asyncio.sleep(1)

        # start latency & jitter impairment
        await flow_1.impairment_distribution.latency_jitter_type_config.enable.set_on() 

        # start frame drop impairment
        # await flow_1.impairment_distribution.drop_type_config.enable.set(action=OnOff.ON) 

        asyncio.create_task(collect_statistics(flow_1, stop_event))
        await stop_event.wait()
        await asyncio.sleep(1)


async def main():
    stop_event = asyncio.Event()
    try:
        await my_awesome_func(stop_event)
    except KeyboardInterrupt:
        stop_event.set()


if __name__ == "__main__":
    asyncio.run(main())