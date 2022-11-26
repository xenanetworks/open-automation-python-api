import asyncio
from contextlib import suppress
import ipaddress

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils
from xoa_driver import exceptions


async def my_awesome_func(stop_event: asyncio.Event):
    # create tester instance and establish connection
    tester = await testers.L23Tester("10.10.10.10", "xoa")

    # access module 0 on the tester
    my_module = tester.modules.obtain(0)

    if isinstance(my_module, modules.ModuleChimera):
        return None # commands which used in this example are not supported by Chimera Module

    # access port 0 on the module as the TX port
    my_port = my_module.ports.obtain(0)

    #---------------------------
    # Port reservation
    #---------------------------
    if my_port.is_released():
        print(f"The port is released (not owned by anyone). Will reserve the port to continue port configuration.")
        await my_port.reservation.set_reserve() # set reservation , means port will be controlled by our session
    elif not my_port.is_reserved_by_me():
        print(f"The port is reserved by others. Will relinquish and reserve the port to continue port configuration.")
        await my_port.reservation.set_relinquish() # send relinquish the port
        await my_port.reservation.set_reserve() # set reservation , means port will be controlled by our session

    #---------------------------
    # Start conversion
    #---------------------------
    with suppress(exceptions.BadStatus):

        await my_port.reset.set()

        await utils.apply(
            my_port.speed.mode.selection.set(mode=enums.PortSpeedMode.AUTO),
            my_port.comment.set(comment="Port number 0"),
            my_port.tx_config.enable.set_on(),
            my_port.interframe_gap.set(min_byte_count=20),
            my_port.flash.set_off(),
            my_port.speed.reduction.set(ppm=-1),
            my_port.net_config.mac_address.set(mac_address="04F4BCA53E60"),
            my_port.net_config.ipv4.address.set(ipv4_address=ipaddress.IPv4Address('0.0.0.0'), subnet_mask=ipaddress.IPv4Address('0.0.0.0'), gateway=ipaddress.IPv4Address('0.0.0.0'), wild=ipaddress.IPv4Address('0.0.0.0')),
            my_port.multicast.header.set(header_count=0, header_format=enums.MulticastHeaderFormat.NOHDR, tag=0, pcp=0, dei=enums.OnOff.OFF),
            my_port.multicast.mode.set(ipv4_multicast_addresses=[ipaddress.IPv4Address('0.0.0.0')], operation=enums.MulticastOperation.OFF, second_count=25),
            my_port.multicast.mode_extended.set(ipv4_multicast_addresses=[ipaddress.IPv4Address('0.0.0.0')], operation=enums.MulticastExtOperation.OFF, second_count=25, igmp_version=enums.IGMPVersion.IGMPV2),
            my_port.multicast.source_list.set(ipv4_addresses=[ipaddress.IPv4Address('0.0.0.0')]),
            my_port.net_config.ipv4.arp_reply.set_off(),
            my_port.net_config.ipv4.ping_reply.set_off(),
            my_port.net_config.ipv6.address.set(ipv6_address=ipaddress.IPv6Address('::'), gateway=ipaddress.IPv6Address('::'), subnet_prefix=128, wildcard_prefix=128),
            my_port.net_config.ipv6.arp_reply.set_off(),
            my_port.net_config.ipv6.ping_reply.set_off(),
            my_port.arp_rx_table.set(chunks=[]),
            my_port.ndp_rx_table.set(chunks=[]),
            my_port.pause.set_off(),
            my_port.pfc_enable.set(cos_0=enums.OnOff.OFF, cos_1=enums.OnOff.OFF, cos_2=enums.OnOff.OFF, cos_3=enums.OnOff.OFF, cos_4=enums.OnOff.OFF, cos_5=enums.OnOff.OFF, cos_6=enums.OnOff.OFF, cos_7=enums.OnOff.OFF),
            my_port.random_seed.set(seed=0),
            my_port.latency_config.offset.set(offset=0),
            my_port.latency_config.mode.set(mode=enums.LatencyMode.LAST2LAST),
            my_port.tx_config.time_limit.set(microseconds=0),
            my_port.tx_config.burst_period.set(burst_period=0),
            my_port.tx_config.packet_limit.set(packet_count_limit=0),
            my_port.tx_config.mode.set_normal(),
            my_port.max_header_length.set(max_header_length=128),
            my_port.autotrain.set(interval=0),
            my_port.loop_back.set_none(),
            my_port.checksum.set(offset=0),
            my_port.gap_monitor.set(start=0, stop=0),
            my_port.mix.weights.set(weight_56_bytes=0, weight_60_bytes=0, weight_64_bytes=0, weight_70_bytes=0,weight_78_bytes=57,
        weight_92_bytes=3, weight_256_bytes=5, weight_496_bytes=1, weight_512_bytes=2, weight_570_bytes=5, weight_576_bytes=1,
        weight_594_bytes=4, weight_1438_bytes=4, weight_1518_bytes=18, weight_9216_bytes=0, weight_16360_bytes=0),
            my_port.tx_config.delay.set(delay_val=0),
            my_port.tpld_mode.set_normal(),
        # await my_port.dynamic.set_off(), this dynamic traffic rate feature is not supported by the module. Even though it appears in the xpc file, we don't necessarily need to configure it.
            my_port.payload_mode.set_normal()
        )
        if isinstance(my_port, ports.POdin10G5S6PCU_b):
            # M6RJ45N[b]'s name is Odin-10G-5S-6P-CU[b]. Only CU ports support autoneg_selection. So I added an if clause here.
            await my_port.autoneg_selection.set_on()
        if isinstance(my_port, ports.POdin1G3S6PT1RJ45):
            await my_port.brr_mode.set(mode=enums.BRRMode.MASTER)
        if isinstance(my_port, ports.POdin10G5S6PCU):
            # M6RJ45N[b]'s name is Odin-10G-5S-6P-CU[b], which supports EEE, so I added an if clause here.
            await my_port.eee.enable.set_off()
            await my_port.eee.mode.set_off()
        
        # Create a stream on the port and configure the stream
        stream =await my_port.streams.create()
        await utils.apply(
            stream.enable.set_on(),
            stream.packet.limit.set(packet_count=-1),
            stream.comment.set("Stream number 0"),
            stream.rate.fraction.set(stream_rate_ppm=500000),
            stream.burst.burstiness.set(size=-1, density=100),
            stream.burst.gap.set(inter_packet_gap=0, inter_burst_gap=0),
            stream.packet.header.protocol.set(segments=[enums.ProtocolOption.ETHERNET]),
            stream.packet.header.data.set(hex_data="0x00000000000004F4BCA53E60FFFF"), # for string type, we need to quote it.
            stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=64, max_val=1518),
            stream.payload.content.set(payload_type=enums.PayloadType.INCREMENTING, hex_data="0x00"), # same as line 87
            stream.tpld_id.set(test_payload_identifier=0),
            stream.insert_packets_checksum.set_on(),
            stream.gateway.ipv4.set(gateway=ipaddress.IPv4Address('0.0.0.0')),
            stream.gateway.ipv6.set(gateway=ipaddress.IPv6Address('::')),
            stream.priority_flow.set(pcp=enums.PFCMode.VLAN_PCP),
            my_port.capturer.trigger.set(start_criteria=enums.StartTrigger.ON, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FULL, stop_criteria_filter=0),
            my_port.capturer.keep.set(kind=enums.PacketType.ALL, index=0, byte_count=-1)
        )
        # Configure a modifier on the stream (Enabled Line 113-116 if modifier is needed.)
        # await stream.packet.header.modifiers.configure(1)
        # modifier = stream.packet.header.modifiers.obtain(0)
        # await modifier.specification.set(position=0, mask="0xFFFF", action=enums.ModifierAction.INC, repetition=1)
        # await modifier.range.set(min_val=0, step=1, max_val=65535)


async def main():
    stop_event = asyncio.Event()
    try:
        await my_awesome_func(stop_event)
    except KeyboardInterrupt:
        stop_event.set()


if __name__ == "__main__":
    asyncio.run(main())