import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils
from xoa_driver import misc
from xoa_driver.hlfuncs import mgmt
from xoa_driver.misc import Hex
from xoa_driver.lli import commands
import ipaddress


async def my_awesome_func(stop_event: asyncio.Event):

# region Tester
    #################################################
    #                   Tester                      #
    #################################################
    tester = await testers.L23Tester(
        host="10.10.10.10",
        username="my_name",
        password="xena",
        enable_logging=False)
    
    # Shutdown/Restart
    await tester.down.set(operation=enums.ChassisShutdownAction.POWER_OFF)
    await tester.down.set_poweroff()
    await tester.down.set(operation=enums.ChassisShutdownAction.RESTART)
    await tester.down.set_restart()

    # Flash
    await tester.flash.set(on_off=enums.OnOff.OFF)
    await tester.flash.set_off()
    await tester.flash.set(on_off=enums.OnOff.ON)
    await tester.flash.set_on()

    resp = await tester.flash.get()
    resp.on_off

    # Debug Log
    resp = await tester.debug_log.get()
    resp.data
    resp.message_length

    # IP Address
    await tester.management_interface.ip_address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.10.1"))
    
    resp = await tester.management_interface.ip_address.get()
    resp.ipv4_address
    resp.subnet_mask
    resp.gateway

    # MAC Address
    resp = await tester.management_interface.macaddress.get()
    resp.mac_address

    # Hostname
    await tester.management_interface.hostname.set(hostname="name")

    resp = await tester.management_interface.hostname.get()
    resp.hostname

    # DHCP
    await tester.management_interface.dhcp.set(on_off=enums.OnOff.ON)
    await tester.management_interface.dhcp.set_on()
    await tester.management_interface.dhcp.set(on_off=enums.OnOff.OFF)
    await tester.management_interface.dhcp.set_off()

    resp = await tester.management_interface.dhcp.get()
    resp.on_off

    # Capabilities
    resp = await tester.capabilities.get()
    resp.version
    resp.max_name_len
    resp.max_comment_len
    resp.max_password_len
    resp.max_ext_rate
    resp.max_session_count
    resp.max_chain_depth
    resp.max_module_count
    resp.max_protocol_count
    resp.can_stream_based_arp
    resp.can_sync_traffic_start
    resp.can_read_log_files
    resp.can_par_module_upgrade
    resp.can_upgrade_timekeeper
    resp.can_custom_defaults
    resp.max_owner_name_length
    resp.can_read_temperatures
    resp.can_latency_f2f

    # Name
    await tester.name.set(chassis_name="name")

    resp = await tester.name.get()
    resp.chassis_name

    # Password
    await tester.password.set(password="xena")

    resp = await tester.password.get()
    resp.password

    # Description
    await tester.comment.set(comment="description")
    
    resp = await tester.comment.get()
    resp.comment

    # Model
    resp = await tester.model.get()
    resp.model

    # Serial Number
    resp = await tester.serial_no.get()
    resp.serial_number

    # Firmware Version
    resp = await tester.version_no.get()
    resp.chassis_major_version
    resp.pci_driver_version

    resp = await tester.version_no_minor.get()
    resp.chassis_minor_version
    resp.reserved_1
    resp.reserved_2

    # Build String
    resp = await tester.build_string.get()
    resp.build_string

    # Reservation
    await tester.reservation.set(operation=enums.ReservedAction.RELEASE)
    await tester.reservation.set_release()
    await tester.reservation.set(operation=enums.ReservedAction.RELINQUISH)
    await tester.reservation.set_relinquish()
    await tester.reservation.set(operation=enums.ReservedAction.RESERVE)
    await tester.reservation.set_reserve()

    resp = await tester.reservation.get()
    resp.operation

    # Reserved By
    resp = await tester.reserved_by.get()
    resp.username

    # Information
    # The following are pre-fetched in cache when connection is established, thus no need to use await

    tester.session.owner_name
    tester.session.keepalive
    tester.session.pwd
    tester.session.is_online
    tester.session.sessions_info
    tester.session.timeout
    tester.is_released()
    tester.is_reserved_by_me()

    # Logoff
    await tester.session.logoff()

    # Time
    resp = await tester.time.get()
    resp.local_time

    # TimeKeeper Configuration
    await tester.time_keeper.config_file.set(config_file="filename")
    
    resp = await tester.time_keeper.config_file.get()
    resp.config_file

    # TimeKeeper GPS State
    resp = await tester.time_keeper.gps_state.get()
    resp.status

    # TimeKeeper License File
    await tester.time_keeper.license_file.set(license_content="")
    
    resp = await tester.time_keeper.license_file.get()
    resp.license_content

    # TimeKeeper License State
    resp = await tester.time_keeper.license_state.get()
    resp.license_errors
    resp.license_file_state
    resp.license_type

    # TimeKeeper Status
    resp = await tester.time_keeper.status.get()
    resp.status_string

    resp = await tester.time_keeper.status_extended.get()
    resp.status_string

    # Chassis Traffic
    await tester.traffic.set(on_off=enums.OnOff.ON, module_ports=[0,0,0,1])
    await tester.traffic.set(on_off=enums.OnOff.OFF, module_ports=[0,0,0,1])
    await tester.traffic.set_on(module_ports=[0,0,0,1])
    await tester.traffic.set_off(module_ports=[0,0,0,1])

    # Synchronized Chassis Traffic
    await tester.traffic_sync.set(on_off=enums.OnOff.ON, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set(on_off=enums.OnOff.OFF, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_on(timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_off(timestamp=1234567, module_ports=[0,0,0,1])

# endregion

# region Module
    #################################################
    #                   Module                      #
    #################################################

    # Access module index 0 on the tester
    module = tester.modules.obtain(0)

    # Capabilities
    resp = await module.capabilities.get()
    resp.can_advanced_timing
    resp.can_local_time_adjust
    resp.can_media_config
    resp.can_ppm_sweep
    resp.can_tsn
    resp.is_chimera
    resp.max_clock_ppm

    # Name
    resp = await module.name.get()
    resp.name

    # Description
    await module.comment.set(comment="description")
    
    resp = await module.comment.get()
    resp.comment

    # Legacy Model
    resp = await module.model.get()
    resp.model

    # Model
    resp = await module.revision.get()
    resp.revision

    # Serial Number
    resp = await module.serial_number.get()
    resp.serial_number

    # Firmware Version
    resp = await module.version_number.get()
    resp.version

    # Port Count
    resp = await module.port_count.get()
    resp.port_count

    # Status
    resp = await module.status.get()
    resp.temperature

    # Media Configuration
    await module.media.set(media_config=enums.MediaConfigurationType.BASE_T1)
    await module.media.set(media_config=enums.MediaConfigurationType.BASE_T1S)
    await module.media.set(media_config=enums.MediaConfigurationType.CFP)
    await module.media.set(media_config=enums.MediaConfigurationType.CFP4)
    await module.media.set(media_config=enums.MediaConfigurationType.CXP)
    await module.media.set(media_config=enums.MediaConfigurationType.OSFP800)
    await module.media.set(media_config=enums.MediaConfigurationType.OSFP800_ANLT)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP112)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP112_ANLT)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP28_NRZ)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP28_PAM4)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP56_PAM4)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD_NRZ)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD_PAM4)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD800)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD800_ANLT)
    await module.media.set(media_config=enums.MediaConfigurationType.SFP112)
    await module.media.set(media_config=enums.MediaConfigurationType.SFP28)
    await module.media.set(media_config=enums.MediaConfigurationType.SFP56)
    await module.media.set(media_config=enums.MediaConfigurationType.SFPDD)

    resp = await module.media.get()
    resp.media_config
    
    # Supported Media
    resp = await module.available_speeds.get()
    resp.media_info_list

    # Port Configuration
    await module.cfp.config.set(portspeed_list=[1, 800000])
    await module.cfp.config.set(portspeed_list=[2, 400000, 400000])
    await module.cfp.config.set(portspeed_list=[4, 200000, 200000, 200000, 200000])
    await module.cfp.config.set(portspeed_list=[8, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])

    resp = await module.cfp.config.get()
    resp.portspeed_list

    # Reservation
    await module.reservation.set(operation=enums.ReservedAction.RELEASE)
    await module.reservation.set_release()
    await module.reservation.set(operation=enums.ReservedAction.RELINQUISH)
    await module.reservation.set_relinquish()
    await module.reservation.set(operation=enums.ReservedAction.RESERVE)
    await module.reservation.set_reserve()

    resp = await module.reservation.get()
    resp.operation
    
    # Reserved By
    resp = await module.reserved_by.get()
    resp.username

    # TX Clock Filter Loop Bandwidth
    if not isinstance(module, modules.ModuleChimera):
        await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW103HZ)
        await module.advanced_timing.clock_tx.filter.set_bw103hz()
        await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW1683HZ)
        await module.advanced_timing.clock_tx.filter.set_bw1683hz()
        await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW207HZ)
        await module.advanced_timing.clock_tx.filter.set_bw207hz()
        await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW416HZ)
        await module.advanced_timing.clock_tx.filter.set_bw416hz()
        await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW7019HZ)
        await module.advanced_timing.clock_tx.filter.set_bw7019hz()

        resp = await module.advanced_timing.clock_tx.filter.get()
        resp.filter_bandwidth

    # TX Clock Source
    if not isinstance(module, modules.ModuleChimera):
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.MODULELOCALCLOCK)
        await module.advanced_timing.clock_tx.source.set_modulelocalclock()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P0RXCLK)
        await module.advanced_timing.clock_tx.source.set_p0rxclk()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P1RXCLK)
        await module.advanced_timing.clock_tx.source.set_p1rxclk()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P2RXCLK)
        await module.advanced_timing.clock_tx.source.set_p2rxclk()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P3RXCLK)
        await module.advanced_timing.clock_tx.source.set_p3rxclk()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P4RXCLK)
        await module.advanced_timing.clock_tx.source.set_p4rxclk()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P5RXCLK)
        await module.advanced_timing.clock_tx.source.set_p5rxclk()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P6RXCLK)
        await module.advanced_timing.clock_tx.source.set_p6rxclk()
        await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P7RXCLK)
        await module.advanced_timing.clock_tx.source.set_p7rxclk()

        resp = await module.advanced_timing.clock_tx.source.get()
        resp.tx_clock

    # TX Clock Status
    if not isinstance(module, modules.ModuleChimera):
        resp = await module.advanced_timing.clock_tx.status.get()
        resp.status

    # SMA Status
    if not isinstance(module, modules.ModuleChimera):
        resp = await module.advanced_timing.sma.status.get()
        resp.status

    # SMA Input
    if not isinstance(module, modules.ModuleChimera):
        await module.advanced_timing.sma.input.set(sma_in=enums.SMAInputFunction.NOT_USED)
        await module.advanced_timing.sma.input.set_notused()
        await module.advanced_timing.sma.input.set(sma_in=enums.SMAInputFunction.TX10MHZ)
        await module.advanced_timing.sma.input.set_tx10mhz()
        await module.advanced_timing.sma.input.set(sma_in=enums.SMAInputFunction.TX2MHZ)
        await module.advanced_timing.sma.input.set_tx2mhz()

        resp = await module.advanced_timing.sma.input.get()
        resp.sma_in

    # SMA Output
    if not isinstance(module, modules.ModuleChimera):
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.DISABLED)
        await module.advanced_timing.sma.output.set_disabled()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P0RXCLK)
        await module.advanced_timing.sma.output.set_p0rxclk()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P0RXCLK2MHZ)
        await module.advanced_timing.sma.output.set_p0rxclk2mhz()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P0SOF)
        await module.advanced_timing.sma.output.set_p0sof()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P1RXCLK)
        await module.advanced_timing.sma.output.set_p1rxclk()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P1RXCLK2MHZ)
        await module.advanced_timing.sma.output.set_p1rxclk2mhz()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P1SOF)
        await module.advanced_timing.sma.output.set_p1sof()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.PASSTHROUGH)
        await module.advanced_timing.sma.output.set_passthrough()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF10MHZ)
        await module.advanced_timing.sma.output.set_ref10mhz()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF125MHZ)
        await module.advanced_timing.sma.output.set_ref125mhz()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF156MHZ)
        await module.advanced_timing.sma.output.set_ref156mhz()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF2MHZ)
        await module.advanced_timing.sma.output.set_ref2mhz()
        await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.TS_PPS)
        await module.advanced_timing.sma.output.set_ts_pps()

        resp = await module.advanced_timing.sma.output.get()
        resp.sma_out

    # Local Clock Adjust
    await module.timing.clock_local_adjust.set(ppb=10)
    
    resp = await module.timing.clock_local_adjust.get()
    resp.ppb

    # Clock Sync Status
    resp = await module.timing.clock_sync_status.get()
    resp.m_clock_diff
    resp.m_correction
    resp.m_is_steady_state
    resp.m_tune_is_increase
    resp.m_tune_value

    # Clock Source
    await module.timing.source.set(source=enums.TimingSource.CHASSIS)
    await module.timing.source.set_chassis()
    await module.timing.source.set(source=enums.TimingSource.EXTERNAL)
    await module.timing.source.set_external()
    await module.timing.source.set(source=enums.TimingSource.MODULE)
    await module.timing.source.set_module()

    resp = await module.timing.source.get()
    resp.source

    # Clock PPM Sweep Configuration
    FREYA_MODULES = (modules.MFreya800G4S1P_a, modules.MFreya800G4S1P_b, modules.MFreya800G4S1POSFP_a, modules.MFreya800G4S1POSFP_b)
    if isinstance(module, FREYA_MODULES):
        await module.clock_sweep.config.set(mode=enums.PPMSweepMode.OFF, ppb_step=10, step_delay=10, max_ppb=10, loops=1)
        await module.clock_sweep.config.set(mode=enums.PPMSweepMode.TRIANGLE, ppb_step=10, step_delay=10, max_ppb=10, loops=1)

        resp = await module.clock_sweep.config.get()
        resp.mode
        resp.ppb_step
        resp.step_delay
        resp.max_ppb
        resp.loops

    # Clock PPM Sweep Status
    if isinstance(module, FREYA_MODULES):
        resp = await module.clock_sweep.status.get()
        resp.curr_step
        resp.curr_sweep
        resp.max_steps

    
    # Chimera - Bypass Mode
    if isinstance(module, modules.ModuleChimera):
        await module.emulator_bypass_mode.set(on_off=enums.OnOff.ON)
        await module.emulator_bypass_mode.set_on()
        await module.emulator_bypass_mode.set(on_off=enums.OnOff.OFF)
        await module.emulator_bypass_mode.set_off()

        resp = await module.emulator_bypass_mode.get()
        resp.on_off

    # Chimera - Latency Mode
    if isinstance(module, modules.ModuleChimera):
        await module.latency_mode.set(mode=enums.ImpairmentLatencyMode.NORMAL)
        await module.latency_mode.set_normal()
        await module.latency_mode.set(mode=enums.ImpairmentLatencyMode.EXTENDED)
        await module.latency_mode.set_extended()

        resp = await module.latency_mode.get()
        resp.mode

    # Chimera - TX Clock Source
    if isinstance(module, modules.ModuleChimera):
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.MODULELOCALCLOCK)
        await module.tx_clock.source.set_modulelocalclock()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P0RXCLK)
        await module.tx_clock.source.set_p0rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P1RXCLK)
        await module.tx_clock.source.set_p1rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P2RXCLK)
        await module.tx_clock.source.set_p2rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P3RXCLK)
        await module.tx_clock.source.set_p3rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P4RXCLK)
        await module.tx_clock.source.set_p4rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P5RXCLK)
        await module.tx_clock.source.set_p5rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P6RXCLK)
        await module.tx_clock.source.set_p6rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P7RXCLK)
        await module.tx_clock.source.set_p7rxclk()

        resp = await module.tx_clock.source.get()
        resp.tx_clock

    # Chimera - TX Clock Status
    if isinstance(module, modules.ModuleChimera):
        resp = await module.tx_clock.status.get()
        resp.status
# endregion

# region Port
    #################################################
    #                    Port                       #
    #################################################

    port = module.ports.obtain(0)

    # Reset
    await port.reset.set()

    if isinstance(port, ports.PortChimera):
        return

    # Flash
    await port.flash.set(on_off=enums.OnOff.ON)
    await port.flash.set_on()
    await port.flash.set(on_off=enums.OnOff.OFF)
    await port.flash.set_off()

    resp = await port.flash.get()
    resp.on_off


    # MAC Address
    await port.net_config.mac_address.set(mac_address=Hex("000000000000"))
    
    resp = await port.net_config.mac_address.get()
    resp.mac_address

    # IPv4 Address
    await port.net_config.ipv4.address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.1.1"),
        wild=ipaddress.IPv4Address("0.0.0.0"))
    
    resp = await port.net_config.ipv4.address.get()
    resp.ipv4_address
    resp.gateway
    resp.subnet_mask
    resp.wild

    # ARP Reply
    await port.net_config.ipv4.arp_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv4.arp_reply.set(on_off=enums.OnOff.OFF)
    
    resp = await port.net_config.ipv4.arp_reply.get()
    resp.on_off

    # Ping Reply
    await port.net_config.ipv4.ping_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv4.ping_reply.set(on_off=enums.OnOff.OFF)

    resp = await port.net_config.ipv4.ping_reply.get()
    resp.on_off

    # IPv6 Address
    await port.net_config.ipv6.address.set(
        ipv6_address=ipaddress.IPv6Address("fc00::0002"),
        gateway=ipaddress.IPv6Address("fc00::0001"),
        subnet_prefix=7,
        wildcard_prefix=0
    )
    
    resp = await port.net_config.ipv6.address.get()
    resp.ipv6_address
    resp.gateway
    resp.subnet_prefix
    resp.wildcard_prefix

    # NDP Reply
    await port.net_config.ipv6.arp_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv6.arp_reply.set(on_off=enums.OnOff.OFF)

    resp = await port.net_config.ipv6.arp_reply.get()
    resp.on_off

    # IPv6 Ping Reply
    await port.net_config.ipv6.ping_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv6.ping_reply.set(on_off=enums.OnOff.OFF)

    resp = await port.net_config.ipv6.ping_reply.get()
    resp.on_off

    # ARP Table, https://github.com/xenanetworks/open-automation-script-library/tree/main/ip_streams_arp_table
    await port.arp_rx_table.set(chunks=[])
    
    resp = await port.arp_rx_table.get()
    resp.chunks

    # NDP Table, https://github.com/xenanetworks/open-automation-script-library/tree/main/ip_streams_arp_table
    await port.ndp_rx_table.set(chunks=[])
    
    resp = await port.ndp_rx_table.get()
    resp.chunks

    # Capture Trigger Criteria, https://github.com/xenanetworks/open-automation-script-library/blob/main/packet_capture/packet_capture.py
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.ON, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FULL, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.ON, start_criteria_filter=0, stop_criteria=enums.StopTrigger.USERSTOP, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.FCSERR, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FCSERR, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.PLDERR, start_criteria_filter=0, stop_criteria=enums.StopTrigger.PLDERR, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.FILTER, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FILTER, stop_criteria_filter=0)

    resp = await port.capturer.trigger.get()
    resp.start_criteria
    resp.start_criteria_filter
    resp.stop_criteria
    resp.stop_criteria_filter

    # Capture - Frame to Keep, https://github.com/xenanetworks/open-automation-script-library/blob/main/packet_capture/packet_capture.py
    await port.capturer.keep.set(kind=enums.PacketType.ALL, index=0, byte_count=0)
    await port.capturer.keep.set_all()
    await port.capturer.keep.set(kind=enums.PacketType.FCSERR, index=0, byte_count=0)
    await port.capturer.keep.set_fcserr()
    await port.capturer.keep.set(kind=enums.PacketType.FILTER, index=0, byte_count=0)
    await port.capturer.keep.set_filter()
    await port.capturer.keep.set(kind=enums.PacketType.NOTPLD, index=0, byte_count=0)
    await port.capturer.keep.set_notpld()
    await port.capturer.keep.set(kind=enums.PacketType.PLDERR, index=0, byte_count=0)
    await port.capturer.keep.set_plderr()
    await port.capturer.keep.set(kind=enums.PacketType.TPLD, index=0, byte_count=0)
    await port.capturer.keep.set_tpld()

    resp = await port.capturer.keep.get()
    resp.kind
    resp.index
    resp.byte_count

    # Capture - State
    await port.capturer.state.set(on_off=enums.StartOrStop.START)
    await port.capturer.state.set_start()
    await port.capturer.state.set(on_off=enums.StartOrStop.STOP)
    await port.capturer.state.set_stop()

    resp = await port.capturer.state.get()
    resp.on_off

    # Capture - Statistics
    resp = await port.capturer.stats.get()
    resp.start_time
    resp.status

    # Read Captured Packets
    pkts = await port.capturer.obtain_captured()
    for i in range(len(pkts)):
        resp = await pkts[i].packet.get()
        print(f"Packet content # {i}: {resp.hex_data}")

    # Inter-frame Gap
    await port.interframe_gap.set(min_byte_count=20)

    resp = await port.interframe_gap.get()
    resp.min_byte_count

    # PAUSE Frames
    await port.pause.set(on_off=enums.OnOff.ON)
    await port.pause.set_on()
    await port.pause.set(on_off=enums.OnOff.OFF)
    await port.pause.set_off()

    resp = await port.pause.get()
    resp.on_off

    # Auto-Train
    await port.autotrain.set(interval=1)

    resp = await port.autotrain.get()
    resp.interval

    # Gap Monitor
    await port.gap_monitor.set(start=100, stop=10)
    
    resp = await port.gap_monitor.get()
    resp.start
    resp.stop

    # Priority Flow Control
    await port.pfc_enable.set(
        cos_0=enums.OnOff.ON,
        cos_1=enums.OnOff.OFF,
        cos_2=enums.OnOff.ON,
        cos_3=enums.OnOff.OFF,
        cos_4=enums.OnOff.ON,
        cos_5=enums.OnOff.OFF,
        cos_6=enums.OnOff.ON,
        cos_7=enums.OnOff.OFF,
        )
    
    resp = await port.pfc_enable.get()
    resp.cos_0
    resp.cos_1
    resp.cos_2
    resp.cos_3
    resp.cos_4
    resp.cos_5
    resp.cos_6
    resp.cos_7

    # Loopback
    await port.loop_back.set(mode=enums.LoopbackMode.L1RX2TX)
    await port.loop_back.set_l1rx2tx()
    await port.loop_back.set(mode=enums.LoopbackMode.L2RX2TX)
    await port.loop_back.set_l2rx2tx()
    await port.loop_back.set(mode=enums.LoopbackMode.L3RX2TX)
    await port.loop_back.set_l3rx2tx()
    await port.loop_back.set(mode=enums.LoopbackMode.NONE)
    await port.loop_back.set_none()
    await port.loop_back.set(mode=enums.LoopbackMode.PORT2PORT)
    await port.loop_back.set_port2port()
    await port.loop_back.set(mode=enums.LoopbackMode.TXOFF2RX)
    await port.loop_back.set_txoff2rx()
    await port.loop_back.set(mode=enums.LoopbackMode.TXON2RX)
    await port.loop_back.set_txon2rx()

    resp = await port.loop_back.get()
    resp.mode

    # BRR Mode
    await port.brr_mode.set(mode=enums.BRRMode.MASTER)
    await port.brr_mode.set_master()
    await port.brr_mode.set(mode=enums.BRRMode.SLAVE)
    await port.brr_mode.set_slave()

    resp = await port.brr_mode.get()
    resp.mode

    # MDI/MDIX Mode
    await port.mdix_mode.set(mode=enums.MDIXMode.AUTO)
    await port.mdix_mode.set_auto()
    await port.mdix_mode.set(mode=enums.MDIXMode.MDI)
    await port.mdix_mode.set_mdi()
    await port.mdix_mode.set(mode=enums.MDIXMode.MDIX)
    await port.mdix_mode.set_mdix()

    resp = await port.mdix_mode.get()
    resp.mode

    # EEE- Capabilities
    resp = await port.eee.capabilities.get()
    resp.eee_capabilities

    # EEE - Partner Capabilities
    resp = await port.eee.partner_capabilities.get()
    resp.cap_1000base_t
    resp.cap_100base_kx
    resp.cap_10gbase_kr
    resp.cap_10gbase_kx4
    resp.cap_10gbase_t

    # EEE - Control
    await port.eee.enable.set(on_off=enums.OnOff.OFF)
    await port.eee.enable.set_off()
    await port.eee.enable.set(on_off=enums.OnOff.ON)
    await port.eee.enable.set_on()

    resp = await port.eee.enable.get()
    resp.on_off

    # EEE - Low Power TX Mode
    await port.eee.mode.set(on_off=enums.OnOff.ON)
    await port.eee.mode.set_off()
    await port.eee.mode.set(on_off=enums.OnOff.OFF)
    await port.eee.mode.set_on()

    resp = await port.eee.mode.get()
    resp.on_off

    # EEE - RX Power
    resp = await port.eee.rx_power.get()
    resp.channel_a
    resp.channel_b
    resp.channel_c
    resp.channel_d

    # EEE - SNR Margin
    resp = await port.eee.snr_margin.get()
    resp.channel_a
    resp.channel_b
    resp.channel_c
    resp.channel_d

    # EEE - Status
    resp = await port.eee.status.get()
    resp.link_up
    resp.rxc
    resp.rxh
    resp.txc
    resp.txh

    # Fault - Signaling
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.DISABLED)
    await port.fault.signaling.set_disabled()
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.FORCE_LOCAL)
    await port.fault.signaling.set_force_local()
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.FORCE_REMOTE)
    await port.fault.signaling.set_force_remote()
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.NORMAL)
    await port.fault.signaling.set_normal()

    resp = await port.fault.signaling.get()
    resp.fault_signaling

    # Fault - Status
    resp = await port.fault.status.get()
    resp.local_fault_status
    resp.remote_fault_status

    # Interface
    resp = await port.interface.get()
    resp.interface

    # Description
    await port.comment.set(comment="description")
    
    resp = await port.comment.get()
    resp.comment

    # Status
    resp = await port.status.get()
    resp.optical_power

    # Latency Mode
    if not isinstance(port, ports.PortChimera):
        await port.latency_config.mode.set(mode=enums.LatencyMode.FIRST2FIRST)
        await port.latency_config.mode.set_first2first()
        await port.latency_config.mode.set(mode=enums.LatencyMode.FIRST2LAST)
        await port.latency_config.mode.set_first2last()
        await port.latency_config.mode.set(mode=enums.LatencyMode.LAST2FIRST)
        await port.latency_config.mode.set_last2first()
        await port.latency_config.mode.set(mode=enums.LatencyMode.LAST2LAST)
        await port.latency_config.mode.set_last2last()

        resp = await port.latency_config.mode.get()
        resp.mode

    # Latency Offset
    if not isinstance(port, ports.PortChimera):
        await port.latency_config.offset.set(offset=5)

        resp = await port.latency_config.offset.get()
        resp.offset
    
    # Link Flap - Control
    await port.pcs_pma.link_flap.enable.set(on_off=enums.OnOff.ON)
    await port.pcs_pma.link_flap.enable.set_on()
    await port.pcs_pma.link_flap.enable.set(on_off=enums.OnOff.OFF)
    await port.pcs_pma.link_flap.enable.set_off()

    resp = await port.pcs_pma.link_flap.enable.get()
    resp.on_off

    # Link Flap - Configuration
    await port.pcs_pma.link_flap.params.set(duration=10, period=20, repetition=0)
    
    resp = await port.pcs_pma.link_flap.params.get()
    resp.duration
    resp.period
    resp.repetition

    # Multicast Mode
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.JOIN,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.JOIN,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.LEAVE,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.OFF,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.ON,
        second_count=10)

    resp = await port.multicast.mode.get()
    resp.ipv4_multicast_addresses
    resp.operation
    resp.second_count

    # Multicast Extended Mode
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.EXCLUDE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV3
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.INCLUDE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV3
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.JOIN,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.LEAVE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.LEAVE_TO_ALL,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.GENERAL_QUERY,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.GROUP_QUERY,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.ON,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.OFF,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )

    resp = await port.multicast.mode_extended.get()
    resp.ipv4_multicast_addresses
    resp.operation
    resp.second_count
    resp.igmp_version

    # Multicast Source List
    await port.multicast.source_list.set(ipv4_addresses=[])
    
    resp = await port.multicast.source_list.get()
    resp.ipv4_addresses


    # Multicast Header
    await port.multicast.header.set(header_count=1, header_format=enums.MulticastHeaderFormat.VLAN, tag=10, pcp=0, dei=0)
    await port.multicast.header.set(header_count=0, header_format=enums.MulticastHeaderFormat.NOHDR, tag=10, pcp=0, dei=0)
    
    resp = await port.multicast.header.get()
    resp.header_count
    resp.header_format
    resp.tag
    resp.pcp
    resp.dei

    # Random Seed
    await port.random_seed.set(seed=1)

    resp = await port.random_seed.get()
    resp.seed

    # Checksum Offset
    await port.checksum.set(offset=14)

    resp = await port.checksum.get()
    resp.offset

    # Maximum Header Length
    await port.max_header_length.set(max_header_length=56)

    resp = await port.max_header_length.get()
    resp.max_header_length

    # MIX Weights
    await port.mix.weights.set(
        weight_56_bytes:=0,
        weight_60_bytes:=0,
        weight_64_bytes:=70,
        weight_70_bytes:=15,
        weight_78_bytes:=15,
        weight_92_bytes:=0,
        weight_256_bytes:=0,
        weight_496_bytes:=0,
        weight_512_bytes:=0,
        weight_570_bytes:=0,
        weight_576_bytes:=0,
        weight_594_bytes:=0,
        weight_1438_bytes:=0,
        weight_1518_bytes:=0,
        weight_9216_bytes:=0,
        weight_16360_bytes:=0)
    
    resp = await port.mix.weights.get()
    resp.weight_56_bytes
    resp.weight_60_bytes
    resp.weight_64_bytes
    resp.weight_70_bytes
    resp.weight_78_bytes
    resp.weight_92_bytes
    resp.weight_256_bytes
    resp.weight_496_bytes
    resp.weight_512_bytes
    resp.weight_570_bytes
    resp.weight_576_bytes
    resp.weight_594_bytes
    resp.weight_1438_bytes
    resp.weight_1518_bytes
    resp.weight_9216_bytes
    resp.weight_16360_bytes

    # MIX Lengths
    await port.mix.lengths[0].set(frame_size=56)
    await port.mix.lengths[1].set(frame_size=60)
    await port.mix.lengths[14].set(frame_size=9216)
    await port.mix.lengths[15].set(frame_size=16360)

    resp = await port.mix.lengths[0].get()
    resp.frame_size
    resp = await port.mix.lengths[1].get()
    resp.frame_size
    resp = await port.mix.lengths[14].get()
    resp.frame_size
    resp = await port.mix.lengths[15].get()
    resp.frame_size

    # Payload Mode
    await port.payload_mode.set(mode=enums.PayloadMode.NORMAL)
    await port.payload_mode.set_normal()
    await port.payload_mode.set(mode=enums.PayloadMode.EXTPL)
    await port.payload_mode.set_extpl()
    await port.payload_mode.set(mode=enums.PayloadMode.CDF)
    await port.payload_mode.set_cdf()

    resp = await port.payload_mode.get()
    resp.mode

    # RX Preamble Insert
    await port.preamble.rx_insert.set(on_off=enums.OnOff.ON)
    await port.preamble.rx_insert.set(on_off=enums.OnOff.OFF)

    resp = await port.preamble.rx_insert.get()
    resp.on_off

    # TX Preamble Removal   
    await port.preamble.tx_remove.set(on_off=enums.OnOff.ON)
    await port.preamble.tx_remove.set(on_off=enums.OnOff.OFF)

    resp = await port.preamble.tx_remove.get()
    resp.on_off

    # Reservation
    await port.reservation.set(operation=enums.ReservedAction.RELEASE)
    await port.reservation.set_release()
    await port.reservation.set(operation=enums.ReservedAction.RELINQUISH)
    await port.reservation.set_relinquish()
    await port.reservation.set(operation=enums.ReservedAction.RESERVE)
    await port.reservation.set_reserve()

    resp = await port.reservation.get()
    resp.status
    
    # Reserved By
    resp = await port.reserved_by.get()
    resp.username

    # Runt - RX Length
    await port.runt.rx_length.set(runt_length=40)
    
    resp = await port.runt.rx_length.get()
    resp.runt_length

    # Runt - TX Length
    await port.runt.tx_length.set(runt_length=40)

    resp = await port.runt.tx_length.get()
    resp.runt_length

    # Runt - Length Error
    resp = await port.runt.has_length_errors.get()
    resp.status

    # Speed Mode Selection
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.AUTO)
    await port.speed.mode.selection.set_auto()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10M)
    await port.speed.mode.selection.set_f10m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10M100M)
    await port.speed.mode.selection.set_f10m100m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10MHDX)
    await port.speed.mode.selection.set_f10mhdx()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M)
    await port.speed.mode.selection.set_f100m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M1G)
    await port.speed.mode.selection.set_f100m1g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M1G10G)
    await port.speed.mode.selection.set_f100m1g10g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100M1G2500M)
    await port.speed.mode.selection.set_f100m1g2500m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100MHDX)
    await port.speed.mode.selection.set_f100mhdx()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F1G)
    await port.speed.mode.selection.set_f1g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F2500M)
    await port.speed.mode.selection.set_f2500m()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F5G)
    await port.speed.mode.selection.set_f5g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F10G)
    await port.speed.mode.selection.set_f10g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F40G)
    await port.speed.mode.selection.set_f40g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F100G)
    await port.speed.mode.selection.set_f100g()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.UNKNOWN)
    await port.speed.mode.selection.set_unknown()
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F200G)
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F400G)
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F800G)
    await port.speed.mode.selection.set(mode=enums.PortSpeedMode.F1600G)

    resp = await port.speed.mode.selection.get()
    resp.mode

    # Supported Speed Modes
    resp = await port.speed.mode.supported.get()
    resp.auto
    resp.f10M
    resp.f100M
    resp.f1G
    resp.f10G
    resp.f40G
    resp.f100G
    resp.f10MHDX
    resp.f100MHDX
    resp.f10M100M
    resp.f100M1G
    resp.f100M1G10G
    resp.f2500M
    resp.f5G
    resp.f100M1G2500M
    resp.f25G
    resp.f50G
    resp.f200G
    resp.f400G
    resp.f800G
    resp.f1600G

    # Current Speed
    resp = await port.speed.current.get()
    resp.port_speed

    # Speed Reduction
    await port.speed.reduction.set(ppm=100)
    
    resp = await port.speed.reduction.get()
    resp.ppm

    # Sync Status
    resp = await port.sync_status.get()
    resp.sync_status == enums.SyncStatus.IN_SYNC
    resp.sync_status == enums.SyncStatus.NO_SYNC

    # Transceiver Status
    resp = await port.tcvr_status.get()
    resp.rx_loss_lane_0
    resp.rx_loss_lane_1
    resp.rx_loss_lane_2
    resp.rx_loss_lane_3

    # Transceiver Read & Write
    await port.transceiver.access_rw(page_address=0, register_address=0).set(value=Hex("00"))
    
    resp = await port.transceiver.access_rw(page_address=0, register_address=0).get()
    resp.value

    # Transceiver Sequential Read & Write
    await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).set(value=Hex("00FF00FF"))
    
    resp = await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).get()
    resp.value

    # Transceiver MII
    await port.transceiver.access_mii(register_address=0).set(value=Hex("00"))
    
    resp = await port.transceiver.access_mii(register_address=0).get()
    resp.value

    # Transceiver Temperature
    resp = await port.transceiver.access_temperature().get()
    resp.integral_part
    resp.fractional_part

    # Transceiver RX Laser Power
    resp = await port.pcs_pma.transceiver.rx_laser_power.get()
    resp.nanowatts

    # Transceiver TX Laser Power
    resp = await port.pcs_pma.transceiver.tx_laser_power.get()
    resp.nanowatts

    # Traffic Control - Rate Percent
    await port.rate.fraction.set(port_rate_ppm=1_000_000)
    
    resp = await port.rate.fraction.get()
    resp.port_rate_ppm

    # Traffic Control - Rate L2 Bits Per Second
    await port.rate.l2_bps.set(port_rate_bps=1_000_000)

    resp = await port.rate.l2_bps.get()
    resp.port_rate_bps

    # Traffic Control - Rate Frames Per Second
    await port.rate.pps.set(port_rate_pps=10_000)
    
    resp = await port.rate.pps.get()
    resp.port_rate_pps

    # Traffic Control - Start and Stop
    await port.traffic.state.set(on_off=enums.StartOrStop.START)
    await port.traffic.state.set_start()
    await port.traffic.state.set(on_off=enums.StartOrStop.STOP)
    await port.traffic.state.set_stop()

    resp = await port.traffic.state.get()
    resp.on_off

    # Traffic Control - Traffic Error
    resp = await port.traffic.error.get()
    resp.error

    # Traffic Control - Single Frame TX
    await port.tx_single_pkt.send.set(hex_data=Hex("00000000000102030405060800FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"))

    # Traffic Control - Single Frame Time
    resp = await port.tx_single_pkt.time.get()
    resp.nanoseconds

    # TPLD Mode
    await port.tpld_mode.set(mode=enums.TPLDMode.NORMAL)
    await port.tpld_mode.set_normal()
    await port.tpld_mode.set(mode=enums.TPLDMode.MICRO)
    await port.tpld_mode.set_micro()

    resp = await port.tpld_mode.get()
    resp.mode

    # TX Mode
    await port.tx_config.mode.set(mode=enums.TXMode.NORMAL)
    await port.tx_config.mode.set_normal()
    await port.tx_config.mode.set(mode=enums.TXMode.BURST)
    await port.tx_config.mode.set_burst()
    await port.tx_config.mode.set(mode=enums.TXMode.SEQUENTIAL)
    await port.tx_config.mode.set_sequential()
    await port.tx_config.mode.set(mode=enums.TXMode.STRICTUNIFORM)
    await port.tx_config.mode.set_strictuniform()

    resp = await port.tx_config.mode.get()
    resp.mode

    # Burst Period
    await port.tx_config.burst_period.set(burst_period=100)
    
    resp = await port.tx_config.burst_period.get()
    resp.burst_period

    # TX Delay
    await port.tx_config.delay.set(delay_val=100)

    resp = await port.tx_config.delay.get()
    resp.delay_val

    # TX Enable
    await port.tx_config.enable.set(on_off=enums.OnOff.ON)
    await port.tx_config.enable.set(on_off=enums.OnOff.OFF)
    
    resp = await port.tx_config.enable.get()
    resp.on_off

    # Packet Limit
    await port.tx_config.packet_limit.set(packet_count_limit=1_000_000)
    
    resp = await port.tx_config.packet_limit.get()
    resp.packet_count_limit

    # Time Limit
    await port.tx_config.time_limit.set(microseconds=1_000_000)
    
    resp = await port.tx_config.time_limit.get()
    resp.microseconds

    # TX Time Elapsed
    resp = await port.tx_config.time.get()
    resp.microseconds

    # Prepare TX
    await port.tx_config.prepare.set()

    # Dynamic Traffic Rate
    await port.dynamic.set(on_off=enums.OnOff.OFF)
    await port.dynamic.set_off()
    await port.dynamic.set(on_off=enums.OnOff.ON)
    await port.dynamic.set_on()
    
    resp = await port.dynamic.get()
    resp.on_off

    #################################################
    #                 Port Filter                   #
    #################################################
    
    # Create and Obtain
    # Create a filter on the port, and obtain the filter object. The filter index is automatically assigned by the port.
    filter = await port.filters.create()

    # Obtain One or Multiple
    filter = port.filters.obtain(position_idx=0)
    filter_list = port.filters.obtain_multiple(*[0,1,2])

    # Remove
    # Remove a filter on the port with an explicit filter index by the index manager of the port.
    await port.filters.remove(position_idx=0)

    # Filter - Enable
    await filter.enable.set(on_off=enums.OnOff.ON)
    await filter.enable.set_on()
    await filter.enable.set(on_off=enums.OnOff.OFF)
    await filter.enable.set_off()

    resp = await filter.enable.get()
    resp.on_off

    # Filter - Description
    await filter.comment.set(comment="this is a comment")

    resp = await filter.comment.get()
    resp.comment

    # Filter - Condition
    await filter.condition.set(and_expression_0=0, and_not_expression_0=0, and_expression_1=1, and_not_expression_1=0, and_expression_2=0, and_expression_3=0)
    
    resp = await filter.condition.get()
    resp.and_expression_0
    resp.and_not_expression_0
    resp.and_expression_1
    resp.and_not_expression_1
    resp.and_expression_2
    resp.and_expression_3

    # Filter - String Representation
    await filter.string.set(string_name="this is name")

    resp = await filter.string.get()
    resp.string_name

    #################################################
    #               Port Length Term                #
    #################################################

    # Create and Obtain
    # Create a length term on the port, and obtain the length term object. The length term index is automatically assigned by the port.
    length_term = await port.length_terms.create()
    
    # Obtain One or Multiple
    length_term = port.length_terms.obtain(key=0)
    length_term_list = port.length_terms.obtain_multiple(*[0,1,2])

    # Remove
    # Remove a length term on the port with an explicit length term index by the index manager of the port.
    await port.length_terms.remove(position_idx=0)

    #################################################
    #               Port Match Term                 #
    #################################################

    # Create and Obtain
    # Create a match term on the port, and obtain the match term object. The match term index is automatically assigned by the port.
    match_term = await port.match_terms.create()
    
    # Obtain One or Multiple
    length_term = port.match_terms.obtain(key=0)
    length_term_list = port.match_terms.obtain_multiple(*[0,1,2])

    # Remove
    # Remove a match term on the port with an explicit match term index by the index manager of the port.
    await port.match_terms.remove(position_idx=0)

    #################################################
    #               Port Histogram                  #
    #################################################

    # Create and Obtain
    # Create a histogram on the port, and obtain the histogram object. The histogram index is automatically assigned by the port.
    dataset = await port.datasets.create()
    
    # Obtain One or Multiple
    length_term = port.datasets.obtain(key=0)
    length_term_list = port.datasets.obtain_multiple(*[0,1,2])

    # Remove
    # Remove a histogram on the port with an explicit histogram index by the index manager of the port.
    await port.datasets.remove(position_idx=0)

    #################################################
    #               Port PCS/PMA                   #
    #################################################

    # Auto-Negotiation Settings
    resp = await port.pcs_pma.auto_neg.settings.get()
    resp.tec_ability
    resp.fec_capable
    resp.fec_requested
    resp.pause_mode

    # Auto-Negotiation Status
    resp = await port.pcs_pma.auto_neg.status.get()
    resp.mode
    resp.auto_state
    resp.tec_ability
    resp.fec_capable
    resp.fec_requested
    resp.fec
    resp.pause_mode

    # Auto-Negotiation Selection
    # Only applicable to RJ45 ports
    await port.autoneg_selection.set(on_off=enums.OnOff.ON)
    await port.autoneg_selection.set_on()
    await port.autoneg_selection.set(on_off=enums.OnOff.OFF)
    await port.autoneg_selection.set_off()

    resp = await port.autoneg_selection.get()
    resp.on_off

    # FEC Mode
    await port.pcs_pma.phy.auto_neg.set(fec_mode=enums.OnOff.ON,reserved_1=0, reserved_2=0, reserved_3=0, reserved_4=0)

    await port.fec_mode.set(mode=enums.FECMode.RS_FEC)
    await port.fec_mode.set(mode=enums.FECMode.RS_FEC_KP)
    await port.fec_mode.set(mode=enums.FECMode.RS_FEC_KR)
    await port.fec_mode.set(mode=enums.FECMode.FC_FEC)
    await port.fec_mode.set(mode=enums.FECMode.OFF)
    await port.fec_mode.set(mode=enums.FECMode.ON)

    resp = await port.fec_mode.get()
    resp.mode

    # Link Training Settings
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.DISABLED, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.STANDALONE, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.INTERACTIVE, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DISABLED)
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.START_AFTER_AUTONEG, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DEFAULT)

    resp = await port.pcs_pma.link_training.settings.get()
    resp.mode
    resp.pam4_frame_size
    resp.nrz_pam4_init_cond
    resp.nrz_preset
    resp.timeout_mode

    # Link Training Serdes Status
    resp = await port.pcs_pma.link_training.per_lane_status[0].get()
    resp.mode
    resp.failure
    resp.status

    # PMA Pulse Error Inject Control
    await port.pcs_pma.pma_pulse_err_inj.enable.set(on_off=enums.OnOff.ON)
    await port.pcs_pma.pma_pulse_err_inj.enable.set_on()
    await port.pcs_pma.pma_pulse_err_inj.enable.set(on_off=enums.OnOff.OFF)
    await port.pcs_pma.pma_pulse_err_inj.enable.set_off()

    resp = await port.pcs_pma.pma_pulse_err_inj.enable.get()
    resp.on_off

    # PMA Pulse Error Inject Configuration
    await port.pcs_pma.pma_pulse_err_inj.params.set(duration=1000, period=1000, repetition=10, coeff=5, exp=-5)
    
    resp = await port.pcs_pma.pma_pulse_err_inj.params.get()
    resp.duration
    resp.period
    resp.coeff
    resp.exp

    # RX Status - Lane Error Counters
    resp = await port.pcs_pma.lanes[0].rx_status.errors.get()
    resp.alignment_error_count
    resp.corrected_fec_error_count
    resp.header_error_count

    # RX Status - Lock Status
    resp = await port.pcs_pma.lanes[0].rx_status.lock.get()
    resp.align_lock
    resp.header_lock

    # RX Status - Lane Status
    resp = await port.pcs_pma.lanes[0].rx_status.status.get()
    resp.skew
    resp.virtual_lane

    # RX Status - Clear Counters
    await port.pcs_pma.rx.clear.set()

    # RX Status - RX FEC Stats
    resp = await port.pcs_pma.rx.fec_status.get()
    resp.stats_type
    resp.value_count
    resp.correction_stats
    resp.rx_uncorrectable_code_word_count

    # RX Status - RX Total Stats
    resp = await port.pcs_pma.rx.total_status.get()
    resp.total_corrected_codeword_count
    resp.total_corrected_symbol_count
    resp.total_post_fec_ber
    resp.total_pre_fec_ber
    resp.total_rx_bit_count
    resp.total_rx_codeword_count
    resp.total_uncorrectable_codeword_count

    # TX Configuration - Error Counters
    resp = await port.pcs_pma.alarms.errors.get()
    resp.total_alarms
    resp.los_error_count
    resp.total_align_error_count
    resp.total_bip_error_count
    resp.total_fec_error_count
    resp.total_header_error_count
    resp.total_higher_error_count
    resp.total_pcs_error_count
    resp.valid_mask

    # TX Configuration - Error Generation Rate
    resp = await port.pcs_pma.error_gen.error_rate.get()
    resp.rate

    # TX Configuration - Error Generation Inject
    await port.pcs_pma.error_gen.inject_one.set()

    # TX Configuration - Error Injection
    await port.pcs_pma.lanes[0].tx_error_inject.set_alignerror()
    await port.pcs_pma.lanes[0].tx_error_inject.set_bip8error()
    await port.pcs_pma.lanes[0].tx_error_inject.set_headererror()

    # TX Configuration - Lane Configuration
    await port.pcs_pma.lanes[0].tx_config.set(virt_lane_index=1, skew=10)
    
    resp = await port.pcs_pma.lanes[0].tx_config.get()
    resp.virt_lane_index
    resp.skew

    #################################################
    #               Port Medium                     #
    #################################################

    # Eye Diagram Information
    resp = await port.serdes[0].eye_diagram.info.get()
    resp.width_mui
    resp.height_mv
    resp.h_slope_left
    resp.h_slope_right
    resp.y_intercept_left
    resp.y_intercept_right
    resp.r_squared_fit_left
    resp.r_squared_fit_right
    resp.est_rj_rms_left
    resp.est_rj_rms_right
    resp.est_dj_pp
    resp.v_slope_bottom
    resp.v_slope_top
    resp.x_intercept_bottom
    resp.x_intercept_top
    resp.r_squared_fit_bottom
    resp.r_squared_fit_top
    resp.est_rj_rms_bottom
    resp.est_rj_rms_top
    
    # Eye Diagram Bit Error Rate
    resp = await port.serdes[0].eye_diagram.ber.get()
    resp.eye_ber_estimation

    # Eye Diagram Dwell Bits
    resp = await port.serdes[0].eye_diagram.dwell_bits.get()
    resp.max_dwell_bit_count
    resp.min_dwell_bit_count

    # Eye Diagram Measure
    resp = await port.serdes[0].eye_diagram.measure.get()
    resp.status

    # Eye Diagram Resolution
    resp = await port.serdes[0].eye_diagram.resolution.get()
    resp.x_resolution
    resp.y_resolution

    # Eye Diagram Data Columns
    resp = await port.serdes[0].eye_diagram.read_column[0].get()
    resp.valid_column_count
    resp.values
    resp.x_resolution
    resp.y_resolution

    # PHY - Signal Status
    resp = await port.pcs_pma.phy.signal_status.get()
    resp.phy_signal_status

    # PHY - Settings
    await port.pcs_pma.phy.settings.set(
        link_training_on_off=enums.OnOff.ON, 
        precode_on_off=enums.OnOffDefault.DEFAULT, 
        graycode_on_off=enums.OnOff.OFF, pam4_msb_lsb_swap=enums.OnOff.OFF)
    
    resp = await port.pcs_pma.phy.settings.get()
    resp.link_training_on_off
    resp.precode_on_off
    resp.graycode_on_off
    resp.pam4_msb_lsb_swap

    # TX Tap Autotune
    await port.serdes[0].phy.autotune.set(on_off=enums.OnOff.ON)
    await port.serdes[0].phy.autotune.set_on()
    await port.serdes[0].phy.autotune.set(on_off=enums.OnOff.OFF)
    await port.serdes[0].phy.autotune.set_off()

    resp = await port.serdes[0].phy.autotune.get()
    resp.on_off

    # TX Tap Retune
    await port.serdes[0].phy.retune.set(dummy=1)

    # TX Tap Configuration
    await port.serdes[0].phy.tx_equalizer.set(pre2=0, pre1=0, main=86, post1=0, post2=0, post3=0)
    resp = await port.serdes[0].phy.tx_equalizer.get()
    resp.pre2
    resp.pre1
    resp.main
    resp.post1
    resp.post2
    resp.post3

    # RX Tap Configuration
    await port.serdes[0].phy.rx_equalizer.set(auto=0, ctle=0, reserved=0)
    
    resp = await port.serdes[0].phy.rx_equalizer.get()
    resp.auto
    resp.ctle

    #################################################
    #               Port PRBS                       #
    #################################################

    # PRBS Configuration
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS7, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.CAUI_VIRTUAL, 
        polynomial=enums.PRBSPolynomial.PRBS9, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.PERSECOND)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS10, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS11, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS13, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS15, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS20, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS23, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS31, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS49, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
    await port.serdes[0].prbs.config.type.set(
        prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, 
        polynomial=enums.PRBSPolynomial.PRBS58, 
        invert=enums.PRBSInvertState.NON_INVERTED, 
        statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)

    resp = await port.serdes[0].prbs.config.type.get()
    resp.prbs_inserted_type
    resp.polynomial
    resp.invert
    resp.statistics_mode

    # PRBS Statistics
    resp = await port.serdes[0].prbs.status.get()
    resp.byte_count
    resp.error_count
    resp.lock
# endregion

# region Statistics 
    #################################################
    #               Statistics                      #
    #################################################

    # Error Counter
    resp = await port.errors_count.get()
    resp.error_count

    # RX Statistics - Clear Counter
    await port.statistics.rx.clear.set()

    # RX Statistics - Calibrate
    await port.statistics.rx.calibrate.set()

    # RX Statistics - Total Counter
    resp = await port.statistics.rx.total.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

    # RX Statistics - Non-TPLD Counter
    resp = await port.statistics.rx.no_tpld.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

    # RX Statistics - PFC Counter
    resp = await port.statistics.rx.pfc_stats.get()
    resp.packet_count
    resp.quanta_pri_0
    resp.quanta_pri_1
    resp.quanta_pri_2
    resp.quanta_pri_3
    resp.quanta_pri_4
    resp.quanta_pri_5
    resp.quanta_pri_6
    resp.quanta_pri_7

    # RX Statistics - Extra Counter
    resp = await port.statistics.rx.extra.get()
    resp.fcs_error_count
    resp.pause_frame_count
    resp.gap_count
    resp.gap_duration
    resp.pause_frame_count
    resp.rx_arp_reply_count
    resp.rx_arp_request_count
    resp.rx_ping_reply_count
    resp.rx_ping_request_count

    # RX Statistics - Received TPLDs
    await port.statistics.rx.obtain_available_tplds()

    # RX Statistics - TPLD - Error Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).errors.get()
    resp.non_incre_payload_packet_count
    resp.non_incre_seq_event_count
    resp.swapped_seq_misorder_event_count

    # RX Statistics - TPLD - Latency Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).latency.get()
    resp.avg_last_sec
    resp.max_last_sec
    resp.min_last_sec
    resp.avg_val
    resp.max_val
    resp.min_val

    # RX Statistics - TPLD - Jitter Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).jitter.get()
    resp.avg_last_sec
    resp.max_last_sec
    resp.min_last_sec
    resp.avg_val
    resp.max_val
    resp.min_val

    # RX Statistics - TPLD - Traffic Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).traffic.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

    # RX Statistics - Filter Statistics
    resp = await port.statistics.rx.obtain_filter_statistics(filter=0).get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

    # TX Statistics - Clear Counter
    await port.statistics.tx.clear.set()

    # TX Statistics - Total Counter
    resp = await port.statistics.tx.total.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

    # TX Statistics - Non-TPLD Counter
    resp = await port.statistics.tx.no_tpld.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

    # TX Statistics - Extra Counter
    resp = await port.statistics.tx.extra.get()
    resp.tx_arp_req_count

    # TX Statistics - Stream Counter
    resp = await port.statistics.tx.obtain_from_stream(stream=0).get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec
# endregion

# region Stream
    #################################################
    #                   Stream                      #
    #################################################

    # Create and Obtain
    # Create a stream on the port, and obtain the stream object. The stream index is automatically assigned by the port.
    stream = await port.streams.create()

    # Obtain One or Multiple
    stream = port.streams.obtain(0)
    stream_list = port.streams.obtain_multiple(*[0,1,2])

    # Remove
    # Remove a stream on the port with an explicit stream index.
    await port.streams.remove(position_idx=0)

    # Description
    await stream.comment.set(comment="description")
    
    resp = await stream.comment.get()
    resp.comment

    # Test Payload ID
    await stream.tpld_id.set(test_payload_identifier=0)
    
    resp = await stream.tpld_id.get()
    resp.test_payload_identifier

    # State
    await stream.enable.set(state=enums.OnOffWithSuppress.OFF)
    await stream.enable.set_off()
    await stream.enable.set(state=enums.OnOffWithSuppress.ON)
    await stream.enable.set_on()
    await stream.enable.set(state=enums.OnOffWithSuppress.SUPPRESS)
    await stream.enable.set_suppress()

    resp = await stream.enable.get()
    resp.state

    # Header Protocol Segment
    await stream.packet.header.protocol.set(segments=[
        enums.ProtocolOption.ETHERNET,
        enums.ProtocolOption.VLAN,
        enums.ProtocolOption.IP,
        enums.ProtocolOption.UDP,
    ])

    # ETHERNET = 1
    # """Ethernet II"""
    # VLAN = 2
    # """VLAN"""
    # ARP = 3
    # """Address Resolution Protocol"""
    # IP = 4
    # """IPv4"""
    # IPV6 = 5
    # """IPv6"""
    # UDP = 6
    # """User Datagram Protocol (w/o checksum)"""
    # TCP = 7
    # """Transmission Control Protocol (w/o checksum)"""
    # LLC = 8
    # """Logic Link Control"""
    # SNAP = 9
    # """Subnetwork Access Protocol"""
    # GTP = 10
    # """GPRS Tunnelling Protocol"""
    # ICMP = 11
    # """Internet Control Message Protocol"""
    # RTP = 12
    # """Real-time Transport Protocol"""
    # RTCP = 13
    # """RTP Control Protocol"""
    # STP = 14
    # """Spanning Tree Protocol"""
    # SCTP = 15
    # """Stream Control Transmission Protocol"""
    # MACCTRL = 16
    # """MAC Control"""
    # MPLS = 17
    # """Multiprotocol Label Switching"""
    # PBBTAG = 18
    # """Provider Backbone Bridge tag"""
    # FCOE = 19
    # """Fibre Channel over Ethernet"""
    # FC = 20
    # """Fibre Channel"""
    # FCOETAIL = 21
    # """Fibre Channel over Ethernet (tail)"""
    # IGMPV3L0 = 22
    # """IGMPv3 Membership Query L=0"""
    # IGMPV3L1 = 23
    # """IGMPv3 Membership Query L=1"""
    # UDPCHECK = 24
    # """User Datagram Protocol (w/ checksum)"""
    # IGMPV2 = 25
    # """Internet Group Management Protocol v2"""
    # MPLS_TP_OAM = 26
    # """MPLS-TP, OAM Header"""
    # GRE_NOCHECK = 27
    # """Generic Routing Encapsulation (w/o checksum)"""
    # GRE_CHECK = 28
    # """Generic Routing Encapsulation (w/ checksum)"""
    # TCPCHECK = 29
    # """Transmission Control Protocol (w/ checksum)"""
    # GTPV1L0 = 30
    # """GTPv1 (no options), GPRS Tunneling Protocol v1"""
    # GTPV1L1 = 31
    # """GTPv1 (w/ options), GPRS Tunneling Protocol v1"""
    # GTPV2L0 = 32
    # """GTPv2 (no options), GPRS Tunneling Protocol v2"""
    # GTPV2L1 = 33
    # """GTPv2 (w/ options), GPRS Tunneling Protocol v2"""
    # IGMPV1 = 34
    # """Internet Group Management Protocol v1"""
    # PWETHCTRL = 35
    # """PW Ethernet Control Word"""
    # VXLAN = 36
    # """Virtual eXtensible LAN"""
    # ETHERNET_8023 = 37
    # """Ethernet 802.3"""
    # NVGRE = 38
    # """Generic Routing Encapsulation (Network Virtualization)"""
    # DHCPV4 = 39
    # """Dynamic Host Configuration Protocol (IPv4)"""
    # GENEVE = 40
    # """Generic Network Virtualization Encapsulation"""

    resp = await stream.packet.header.protocol.get()
    resp.segments

    # Header Value
    await stream.packet.header.data.set(
        hex_data=Hex("00000000000004F4BC7FFE908100000008004500002A000000007F113BC400000000000000000000000000160000"))
    
    resp = await stream.packet.header.data.get()
    resp.hex_data

    # Packet Size
    await stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=64, max_val=64)
    await stream.packet.length.set(length_type=enums.LengthType.INCREMENTING, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.BUTTERFLY, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.RANDOM, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.MIX, min_val=64, max_val=64)

    resp = await stream.packet.length.get()
    resp.length_type
    resp.min_val
    resp.max_val

    # Packet Auto Size
    await stream.packet.auto_adjust.set()

    # Payload Type
    # Pattern string in hex, min = 1 byte, max = 18 bytes
    await stream.payload.content.set(payload_type=enums.PayloadType.PATTERN, hex_data=Hex("000102030405060708090A0B0C0D0E0FDEAD"))
    await stream.payload.content.set(payload_type=enums.PayloadType.PATTERN, hex_data=Hex("F5"))
    
    # Patter string ignored for non-pattern types
    await stream.payload.content.set(payload_type=enums.PayloadType.INC16, hex_data=Hex("F5"))
    await stream.payload.content.set_inc_word("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.INC8, hex_data=Hex("F5"))
    await stream.payload.content.set_inc_byte("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.DEC8, hex_data=Hex("F5"))
    await stream.payload.content.set_dec_byte("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.DEC16, hex_data=Hex("F5"))
    await stream.payload.content.set_dec_word("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.PRBS, hex_data=Hex("F5"))
    await stream.payload.content.set_prbs("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.RANDOM, hex_data=Hex("F5"))
    await stream.payload.content.set_random("00")

    resp = await stream.payload.content.get()
    resp.hex_data
    resp.payload_type

    # Extended Payload
    # Use await port.payload_mode.set_extpl() to set the port's payload mode to Extended Payload.
    await stream.payload.extended.set(hex_data=Hex("00110022FF"))
    
    resp = await stream.payload.extended.get()
    resp.hex_data

    # Rate Fraction
    await stream.rate.fraction.set(stream_rate_ppm=1_000_000)

    resp = await stream.rate.fraction.get()
    resp.stream_rate_ppm

    # Packet Rate
    await stream.rate.pps.set(stream_rate_pps=1_000)
    
    resp = await stream.rate.pps.get()
    resp.stream_rate_pps

    # Bit Rate L2
    await stream.rate.l2bps.set(l2_bps=1_000_000)
    
    resp = await stream.rate.l2bps.get()
    resp.l2_bps

    # Packet Limit
    await stream.packet.limit.set(packet_count=1_000)
    
    resp = await stream.packet.limit.get()
    resp.packet_count

    # Burst Size and Density
    await stream.burst.burstiness.set(size=20, density=80)

    resp = await stream.burst.burstiness.get()
    resp.size
    resp.density

    # Inter Burst/Packet Gap
    await stream.burst.gap.set(inter_packet_gap=30, inter_burst_gap=30)
    
    resp = await stream.burst.gap.get()
    resp.inter_packet_gap
    resp.inter_burst_gap

    # Priority Flow
    await stream.priority_flow.set(cos=enums.PFCMode.ZERO)
    await stream.priority_flow.set(cos=enums.PFCMode.ONE)
    await stream.priority_flow.set(cos=enums.PFCMode.TWO)
    await stream.priority_flow.set(cos=enums.PFCMode.THREE)
    await stream.priority_flow.set(cos=enums.PFCMode.FOUR)
    await stream.priority_flow.set(cos=enums.PFCMode.FIVE)
    await stream.priority_flow.set(cos=enums.PFCMode.SIX)
    await stream.priority_flow.set(cos=enums.PFCMode.SEVEN)
    await stream.priority_flow.set(cos=enums.PFCMode.VLAN_PCP)

    resp = await stream.priority_flow.get()
    resp.cos

    # IPv4 Gateway Address
    await stream.gateway.ipv4.set(gateway=ipaddress.IPv4Address("10.10.10.1"))
    
    resp = await stream.gateway.ipv4.get()
    resp.gateway

    # IPv6 Gateway Address
    await stream.gateway.ipv6.set(gateway=ipaddress.IPv6Address("::0001"))
    
    resp = await stream.gateway.ipv6.get()
    resp.gateway

    # ARP Resolve Peer Address
    # You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ARP resolve the MAC address.
    resp = await stream.request.arp.get()
    resp.mac_address

    # PING Check IP Peer
    # You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ping.
    resp = await stream.request.ping.get()
    resp.delay
    resp.time_to_live

    # Custom Data Field
    # Use await port.payload_mode.set_cdf() to set the port's payload mode to Custom Data Field.

    # Field Offset
    await stream.cdf.offset.set(offset=1)
    
    resp = await stream.cdf.offset.get()
    resp.offset

    # Byte Count
    await stream.cdf.count.set(cdf_count=1)
    
    resp = await stream.cdf.count.get()
    resp.cdf_count

    ################################################
    #          Stream Modifier                     #
    ################################################
    
    # Create
    await stream.packet.header.modifiers.configure(number=1)

    # Clear
    await stream.packet.header.modifiers.clear()

    # Obtain
    # Must create modifiers before obtain.
    modifier = stream.packet.header.modifiers.obtain(idx=0)
    
    # Range
    await modifier.range.set(min_val=0, step=10, max_val=9)
    
    resp = await modifier.range.get()
    resp.min_val
    resp.max_val
    resp.step

    # Position, Action, Mask
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.INC, repetition=1)
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.DEC, repetition=1)
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.RANDOM, repetition=1)
    
    resp = await modifier.specification.get()
    resp.action
    resp.mask
    resp.position
    resp.repetition

    # #################################################
    # #           Stream 32-bit Modifier              #
    # #################################################

    # Create
    await stream.packet.header.modifiers_extended.configure(number=1)

    # Clear
    await stream.packet.header.modifiers_extended.clear()

    # Obtain
    # Must create modifiers before obtain.
    modifier_ext = stream.packet.header.modifiers_extended.obtain(idx=0)

    # Range
    await modifier_ext.range.set(min_val=0, step=1, max_val=100)
    
    resp = await modifier_ext.range.get()
    resp.max_val
    resp.min_val
    resp.step

    # Position, Action, Mask
    await modifier_ext.specification.set(position=0, mask=Hex("FFFFFFFF"), action=enums.ModifierAction.INC, repetition=1)
    await modifier_ext.specification.set(position=0, mask=Hex("FFFFFFFF"), action=enums.ModifierAction.DEC, repetition=1)
    await modifier_ext.specification.set(position=0, mask=Hex("FFFFFFFF"), action=enums.ModifierAction.RANDOM, repetition=1)

    resp = await modifier_ext.specification.get()
    resp.action
    resp.mask
    resp.position
    resp.repetition

    # #################################################
    # #           Stream Error Control                #
    # #################################################

    # Misorder Error Injection
    await stream.inject_err.misorder.set()

    # Payload Integrity Error Injection
    await stream.inject_err.payload_integrity.set()

    # Sequence Error Injection
    await stream.inject_err.sequence.set()

    # Test Payload Error Injection
    await stream.inject_err.test_payload.set()

    # Checksum Error Injection
    await stream.inject_err.frame_checksum.set()

    # Insert Frame Checksum
    await stream.insert_packets_checksum.set(on_off=enums.OnOff.ON)
    await stream.insert_packets_checksum.set_on()
    await stream.insert_packets_checksum.set(on_off=enums.OnOff.OFF)
    await stream.insert_packets_checksum.set_off()

    resp = await stream.insert_packets_checksum.get()
    resp.on_off
# endregion

# region Network Emulation
    #################################################
    #              Network Emulation                #
    #################################################

    # Configure Chimera port
    if isinstance(module, modules.ModuleChimera):
        port = module.ports.obtain(0)

        await port.pcs_pma.link_flap.params.set(duration=100, period=1000, repetition=0)
        await port.pcs_pma.link_flap.enable.set_on()
        await port.pcs_pma.link_flap.enable.set_off()

        await port.pcs_pma.pma_pulse_err_inj.params.set(duration=100, period=1000, repetition=0, coeff=100, exp=-4)
        await port.pcs_pma.pma_pulse_err_inj.enable.set_on()
        await port.pcs_pma.pma_pulse_err_inj.enable.set_off()

        # Enable impairment on the port.
        await port.emulate.set_off()
        await port.emulate.set_on()

        resp = await port.emulate.get()
        resp.action

        # Set TPLD mode
        await port.emulation.tpld_mode.set(mode=enums.TPLDMode.NORMAL)
        await port.emulation.tpld_mode.set(mode=enums.TPLDMode.MICRO)

        resp = await port.emulation.tpld_mode.get()
        resp.mode

        # Configure flow's basic filter on a port
        # Configure flow properties
        flow = port.emulation.flows[1]

        await flow.comment.set(comment="Flow description")
        
        resp = await flow.comment.get()
        resp.comment

        # Initializing the shadow copy of the filter.
        await flow.shadow_filter.initiating.set()

        # Configure shadow filter to BASIC mode
        await flow.shadow_filter.use_basic_mode()
        
        # Query the mode of the filter (either basic or extended)
        filter = await flow.shadow_filter.get_mode()

        if isinstance(filter, misc.BasicImpairmentFlowFilter):
            #------------------
            # Ethernet subfilter
            #------------------
            # Use and configure basic-mode shadow filter's Ethernet subfilter
            await utils.apply(
                filter.ethernet.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.ethernet.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.ethernet.src_address.set(use=enums.OnOff.ON, value=Hex("AAAAAAAAAAAA"), mask=Hex("FFFFFFFFFFFF")),
                filter.ethernet.dest_address.set(use=enums.OnOff.ON, value=Hex("BBBBBBBBBBBB"), mask=Hex("FFFFFFFFFFFF"))
            )

            #------------------
            # Layer 2+ subfilter
            #------------------
            # Not use basic-mode shadow filter's Layer 2+ subfilter
            await filter.l2plus_use.set(use=enums.L2PlusPresent.NA)

            # Use and configure basic-mode shadow filter's Layer2+ subfilter (One VLAN tag)
            await utils.apply(
                filter.l2plus_use.set(use=enums.L2PlusPresent.VLAN1),
                filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.vlan.inner.tag.set(use=enums.OnOff.ON, value=1234, mask=Hex("0FFF")),
                filter.vlan.inner.pcp.set(use=enums.OnOff.OFF, value=3, mask=Hex("07")),
            )
            # Use and configure basic-mode shadow filter's Layer2+ subfilter (Two VLAN tag)
            await utils.apply(
                filter.l2plus_use.set(use=enums.L2PlusPresent.VLAN2),
                filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.vlan.inner.tag.set(use=enums.OnOff.ON, value=1234, mask=Hex("0FFF")),
                filter.vlan.inner.pcp.set(use=enums.OnOff.OFF, value=3, mask=Hex("07")),
                filter.vlan.outer.tag.set(use=enums.OnOff.ON, value=2345, mask=Hex("0FFF")),
                filter.vlan.outer.pcp.set(use=enums.OnOff.OFF, value=0, mask=Hex("07")),
            )
            # Use and configure basic-mode shadow filter's Layer2+ subfilter (MPLS)
            await utils.apply(
                filter.l2plus_use.set(use=enums.L2PlusPresent.MPLS),
                filter.mpls.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.mpls.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.mpls.label.set(use=enums.OnOff.ON, value=1000, mask=Hex("FFFFF")),
                filter.mpls.toc.set(use=enums.OnOff.ON, value=0, mask=Hex("07")),
            )

            #------------------
            # Layer 3 subfilter
            #------------------
            # Not use basic-mode shadow filter's Layer 3 subfilter
            await filter.l3_use.set(use=enums.L3Present.NA)
            # Use and configure basic-mode shadow filter's Layer 3 subfilter (IPv4)
            await utils.apply(
                filter.l3_use.set(use=enums.L3Present.IP4),
                filter.ip.v4.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.ip.v4.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.ip.v4.src_address.set(use=enums.OnOff.ON, value=ipaddress.IPv4Address("10.0.0.2"), mask=Hex("FFFFFFFF")),
                filter.ip.v4.dest_address.set(use=enums.OnOff.ON, value=ipaddress.IPv4Address("10.0.0.2"), mask=Hex("FFFFFFFF")),
                filter.ip.v4.dscp.set(use=enums.OnOff.ON, value=0, mask=Hex("FC")),
            )
            # Use and configure basic-mode shadow filter's Layer 3 subfilter (IPv6)
            await utils.apply(
                filter.l3_use.set(use=enums.L3Present.IP6),
                filter.ip.v6.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.ip.v6.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.ip.v6.src_address.set(use=enums.OnOff.ON, value=ipaddress.IPv6Address("2001::2"), mask=Hex("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")),
                filter.ip.v6.dest_address.set(use=enums.OnOff.ON, value=ipaddress.IPv6Address("2002::2"), mask=Hex("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")),
                filter.ip.v6.traffic_class.set(use=enums.OnOff.ON, value=0, mask=Hex("FC")),
            )

            #------------------
            # Layer 4 subfilter
            #------------------
            # Use and configure basic-mode shadow filter's Layer 4 subfilter (TCP)
            await utils.apply(
                filter.tcp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.tcp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.tcp.src_port.set(use=enums.OnOff.ON, value=1234, mask=Hex("FFFF")),
                filter.tcp.dest_port.set(use=enums.OnOff.ON, value=80, mask=Hex("FFFF")),
            )
            # Use and configure basic-mode shadow filter's Layer 4 subfilter (UDP)
            await utils.apply(
                filter.udp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.udp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.udp.src_port.set(use=enums.OnOff.ON, value=1234, mask=Hex("FFFF")),
                filter.udp.dest_port.set(use=enums.OnOff.ON, value=80, mask=Hex("FFFF")),
            )

            #------------------
            # Layer Xena subfilter
            #------------------
            await utils.apply(
                filter.tpld.settings.set(action=enums.InfoAction.EXCLUDE),
                filter.tpld.settings.set(action=enums.InfoAction.INCLUDE),
                filter.tpld.test_payload_filters_config[0].set(use=enums.OnOff.ON, id = 2),
                filter.tpld.test_payload_filters_config[0].set(use=enums.OnOff.OFF, id = 2),
                filter.tpld.test_payload_filters_config[1].set(use=enums.OnOff.ON, id = 4),
                filter.tpld.test_payload_filters_config[1].set(use=enums.OnOff.OFF, id = 4),
                filter.tpld.test_payload_filters_config[2].set(use=enums.OnOff.ON, id = 6),
                filter.tpld.test_payload_filters_config[2].set(use=enums.OnOff.OFF, id = 6),
                filter.tpld.test_payload_filters_config[3].set(use=enums.OnOff.ON, id = 8),
                filter.tpld.test_payload_filters_config[3].set(use=enums.OnOff.OFF, id = 8),
                filter.tpld.test_payload_filters_config[4].set(use=enums.OnOff.ON, id = 10),
                filter.tpld.test_payload_filters_config[4].set(use=enums.OnOff.OFF, id = 10),
                filter.tpld.test_payload_filters_config[5].set(use=enums.OnOff.ON, id = 20),
                filter.tpld.test_payload_filters_config[5].set(use=enums.OnOff.OFF, id = 20),
                filter.tpld.test_payload_filters_config[6].set(use=enums.OnOff.ON, id = 40),
                filter.tpld.test_payload_filters_config[6].set(use=enums.OnOff.OFF, id = 40),
                filter.tpld.test_payload_filters_config[7].set(use=enums.OnOff.ON, id = 60),
                filter.tpld.test_payload_filters_config[7].set(use=enums.OnOff.OFF, id = 60),
                filter.tpld.test_payload_filters_config[8].set(use=enums.OnOff.ON, id = 80),
                filter.tpld.test_payload_filters_config[8].set(use=enums.OnOff.OFF, id = 80),
                filter.tpld.test_payload_filters_config[9].set(use=enums.OnOff.ON, id = 100),
                filter.tpld.test_payload_filters_config[9].set(use=enums.OnOff.OFF, id = 100),
                filter.tpld.test_payload_filters_config[10].set(use=enums.OnOff.ON, id = 102),
                filter.tpld.test_payload_filters_config[10].set(use=enums.OnOff.OFF, id = 102),
                filter.tpld.test_payload_filters_config[11].set(use=enums.OnOff.ON, id = 104),
                filter.tpld.test_payload_filters_config[11].set(use=enums.OnOff.OFF, id = 104),
                filter.tpld.test_payload_filters_config[12].set(use=enums.OnOff.ON, id = 106),
                filter.tpld.test_payload_filters_config[12].set(use=enums.OnOff.OFF, id = 106),
                filter.tpld.test_payload_filters_config[13].set(use=enums.OnOff.ON, id = 108),
                filter.tpld.test_payload_filters_config[13].set(use=enums.OnOff.OFF, id = 108),
                filter.tpld.test_payload_filters_config[14].set(use=enums.OnOff.ON, id = 110),
                filter.tpld.test_payload_filters_config[14].set(use=enums.OnOff.OFF, id = 110),
                filter.tpld.test_payload_filters_config[15].set(use=enums.OnOff.ON, id = 200),
                filter.tpld.test_payload_filters_config[15].set(use=enums.OnOff.OFF, id = 200),
            )

            #------------------
            # Layer Any subfilter
            #------------------
            await utils.apply(
                filter.any.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
                filter.any.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
                filter.any.config.set(position=0, value=Hex("112233445566"), mask=Hex("112233445566"))
            )

        # Apply the filter so the configuration data in the shadow copy is committed to the working copy automatically.
        await flow.shadow_filter.enable.set_off()
        await flow.shadow_filter.enable.set_on()
        await flow.shadow_filter.apply.set()

        # Configure flow's extended filter on a port
        # Configure flow properties
        flow = port.emulation.flows[1]
        await flow.comment.set("Flow description")

        # Initializing the shadow copy of the filter.
        await flow.shadow_filter.initiating.set()

        # Configure shadow filter to EXTENDED mode
        await flow.shadow_filter.use_extended_mode()

        # Query the mode of the filter (either basic or extended)
        filter = await flow.shadow_filter.get_mode()

        if isinstance(filter, misc.ExtendedImpairmentFlowFilter):

            await filter.use_segments(
                enums.ProtocolOption.VLAN)
            protocol_segments = await filter.get_protocol_segments()
            await protocol_segments[0].value.set(value=Hex("AAAAAAAAAAAABBBBBBBBBBBB8100"))
            await protocol_segments[0].mask.set(masks=Hex("0000000000000000000000000000"))
            await protocol_segments[1].value.set(value=Hex("0064FFFF"))
            await protocol_segments[1].mask.set(masks=Hex("00000000"))

        # Configure impairment - Drop
        # Fixed Burst distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.fixed_burst.set(burst_size=5),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=5), #repeat (duration = 1, period = x)
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=0), #one shot
        )

        # Random Burst distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.random_burst.set(minimum=1, maximum=10, probability=10_000),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Fixed Rate distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.fixed_rate.set(probability=10_000),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Bit Error Rate distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.bit_error_rate.set(coef=1, exp=1),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Random Rate distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.random_rate.set(probability=10_000),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gilbert Elliot distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.ge.set(good_state_prob=0, good_state_trans_prob=0, bad_state_prob=0, bad_state_trans_prob=0),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Uniform distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.uniform.set(minimum=1, maximum=1),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gaussian distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.gaussian.set(mean=1, std_deviation=1),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Poisson distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.poison.set(mean=9),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gamma distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.drop_type_config.gamma.set(shape=1, scale=1),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Custom distribution for impairment Drop
        data_x=[0, 1] * 256
        await port.custom_distributions.assign(0)
        await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
        await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
        await utils.apply(
            flow.impairment_distribution.drop_type_config.custom.set(cust_id=0),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),
            flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Set distribution and start impairment Drop
        await flow.impairment_distribution.drop_type_config.enable.set_on()
        await flow.impairment_distribution.drop_type_config.enable.set_off()
        
        # Configure impairment - Misordering

        # Fixed Burst distribution for impairment Misordering
        # dist = distributions.misordering.FixedBurst(burst_size=1)
        # dist.repeat(period=5)
        # dist.one_shot()

        # Fixed Burst distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.misorder_type_config.fixed_burst.set(burst_size=5),
            flow.impairment_distribution.misorder_type_config.schedule.set(duration=1, period=5), #repeat
            flow.impairment_distribution.misorder_type_config.schedule.set(duration=1, period=0), #one shot
        )

        # Fixed Rate distribution for impairment Drop
        await utils.apply(
            flow.impairment_distribution.misorder_type_config.fixed_rate.set(probability=10_000),
            flow.impairment_distribution.misorder_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.misorder_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Set distribution and start impairment Misordering
        await flow.misordering.set(depth=1)
        await flow.impairment_distribution.misorder_type_config.enable.set_on()
        await flow.impairment_distribution.misorder_type_config.enable.set_off()

        # Configure impairment - Latency & Jitter
        # Fixed Burst distribution for impairment Latency & Jitter
        await flow.impairment_distribution.latency_jitter_type_config.constant_delay.set(delay=100)

        # Random Burst distribution for impairment Latency & Jitter
        await utils.apply(
            flow.impairment_distribution.latency_jitter_type_config.accumulate_and_burst.set(delay=1300),
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=1, period=1), #repeat (duration = 1, period = x)
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=1, period=0), #one shot
        )

        # Step distribution for impairment Latency & Jitter
        await utils.apply(
            flow.impairment_distribution.latency_jitter_type_config.step.set(low=1300, high=77000),
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Uniform distribution for impairment Latency & Jitter
        await utils.apply(
            flow.impairment_distribution.latency_jitter_type_config.uniform.set(minimum=1, maximum=1),
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gaussian distribution for impairment Latency & Jitter
        await utils.apply(
            flow.impairment_distribution.latency_jitter_type_config.gaussian.set(mean=1, std_deviation=1),
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Poisson distribution for impairment Latency & Jitter
        await utils.apply(
            flow.impairment_distribution.latency_jitter_type_config.poison.set(mean=1),
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gamma distribution for impairment Latency & Jitter
        await utils.apply(
            flow.impairment_distribution.latency_jitter_type_config.gamma.set(shape=1, scale=1),
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Custom distribution for impairment Latency & Jitter
        data_x=[0, 1] * 256
        await port.custom_distributions.assign(0)
        await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
        await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
        await utils.apply(
            flow.impairment_distribution.latency_jitter_type_config.custom.set(cust_id=0),
            flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Set distribution and start impairment Latency & Jitter
        await flow.impairment_distribution.latency_jitter_type_config.enable.set_on()
        await flow.impairment_distribution.latency_jitter_type_config.enable.set_off()

        # Configure impairment - Duplication

        # Fixed Burst distribution for impairment Duplication
        # dist.one_shot()
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.fixed_burst.set(burst_size=1300),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), #repeat (duration = 1, period = x)
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=0), #one shot
        )

        # Random Burst distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.random_burst.set(minimum=1, maximum=1, probability=10_0000),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Fixed Rate distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.fixed_rate.set(probability=10_000),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Bit Error Rate distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.bit_error_rate.set(coef=1, exp=1),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Random Rate distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.random_rate.set(probability=10_000),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gilbert Elliot distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.ge.set(good_state_prob=0, good_state_trans_prob=0, bad_state_prob=0, bad_state_trans_prob=0),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Uniform distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.uniform.set(minimum=1, maximum=1),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gaussian distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.gaussian.set(mean=1, std_deviation=1),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Poisson distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.poison.set(mean=9),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gamma distribution for impairment Duplication
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.gamma.set(shape=1, scale=1),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Custom distribution for impairment Duplication
        data_x=[0, 1] * 256
        await port.custom_distributions.assign(0)
        await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
        await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
        await utils.apply(
            flow.impairment_distribution.duplication_type_config.custom.set(cust_id=0),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),
            flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Set distribution and start impairment Duplication
        await flow.impairment_distribution.duplication_type_config.enable.set_on()
        await flow.impairment_distribution.duplication_type_config.enable.set_off()

        # Configure impairment - Corruption

        # Fixed Burst distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.fixed_burst.set(burst_size=1300),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), #repeat (duration = 1, period = x)
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=0), #one shot
        )

        # Random Burst distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.random_burst.set(minimum=1, maximum=1, probability=10_0000),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Fixed Rate distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.fixed_rate.set(probability=10_000),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Bit Error Rate distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.bit_error_rate.set(coef=1, exp=1),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Random Rate distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.random_rate.set(probability=10_000),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gilbert Elliot distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.ge.set(good_state_prob=0, good_state_trans_prob=0, bad_state_prob=0, bad_state_trans_prob=0),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Uniform distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.uniform.set(minimum=1, maximum=1),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gaussian distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.gaussian.set(mean=1, std_deviation=1),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Poisson distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.poison.set(mean=9),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Gamma distribution for impairment Corruption
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.gamma.set(shape=1, scale=1),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), # repeat pattern
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )


        # Custom distribution for impairment Corruption
        data_x=[0, 1] * 256
        await port.custom_distributions.assign(0)
        await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
        await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
        await utils.apply(
            flow.impairment_distribution.corruption_type_config.custom.set(cust_id=0),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),
            flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
        )

        # Set distribution and start impairment Corruption
        await flow.corruption.set(corruption_type=enums.CorruptionType.ETH)
        await flow.corruption.set(corruption_type=enums.CorruptionType.IP)
        await flow.corruption.set(corruption_type=enums.CorruptionType.TCP)
        await flow.corruption.set(corruption_type=enums.CorruptionType.UDP)
        await flow.corruption.set(corruption_type=enums.CorruptionType.BER)
        await flow.impairment_distribution.corruption_type_config.enable.set_on()
        await flow.impairment_distribution.corruption_type_config.enable.set_off()


        # Configure bandwidth control - Policer

        await flow.bandwidth_control.policer.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L1, cir=10_000, cbs=1_000)
        await flow.bandwidth_control.policer.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L2, cir=10_000, cbs=1_000)


        # Configure bandwidth control - Shaper

        # Set and start bandwidth control Shaper
        await flow.bandwidth_control.shaper.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L1, cir=10_000, cbs=1_000, buffer_size=1_000)
        await flow.bandwidth_control.shaper.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L2, cir=10_000, cbs=1_000, buffer_size=1_000)

        # Flow statistics

        rx_total = await flow.statistics.rx.total.get()
        rx_total.byte_count
        rx_total.packet_count
        rx_total.l2_bps
        rx_total.pps

        tx_total = await flow.statistics.tx.total.get()
        tx_total.byte_count
        tx_total.packet_count
        tx_total.l2_bps
        tx_total.pps

        flow_drop_total = await flow.statistics.total.drop_packets.get()
        flow_drop_total.pkt_drop_count_total
        flow_drop_total.pkt_drop_count_programmed
        flow_drop_total.pkt_drop_count_bandwidth
        flow_drop_total.pkt_drop_count_other
        flow_drop_total.pkt_drop_ratio_total
        flow_drop_total.pkt_drop_ratio_programmed
        flow_drop_total.pkt_drop_ratio_bandwidth
        flow_drop_total.pkt_drop_ratio_other

        flow_corrupted_total = await flow.statistics.total.corrupted_packets.get()
        flow_corrupted_total.fcs_corrupted_pkt_count
        flow_corrupted_total.fcs_corrupted_pkt_ratio
        flow_corrupted_total.ip_corrupted_pkt_count
        flow_corrupted_total.ip_corrupted_pkt_ratio
        flow_corrupted_total.tcp_corrupted_pkt_count
        flow_corrupted_total.tcp_corrupted_pkt_ratio
        flow_corrupted_total.total_corrupted_pkt_count
        flow_corrupted_total.total_corrupted_pkt_ratio
        flow_corrupted_total.udp_corrupted_pkt_count
        flow_corrupted_total.udp_corrupted_pkt_ratio

        flow_delayed_total = await flow.statistics.total.latency_packets.get()
        flow_delayed_total.pkt_count
        flow_delayed_total.ratio

        flow_jittered_total = await flow.statistics.total.jittered_packets.get()
        flow_jittered_total.pkt_count
        flow_jittered_total.ratio

        flow_duplicated_total = await flow.statistics.total.duplicated_packets.get()
        flow_duplicated_total.pkt_count
        flow_duplicated_total.ratio

        flow_misordered_total = await flow.statistics.total.mis_ordered_packets.get()
        flow_misordered_total.pkt_count
        flow_misordered_total.ratio

        await flow.statistics.tx.clear.set()
        await flow.statistics.rx.clear.set()
        await flow.statistics.clear.set()
        
        # Port statistics
        port_drop = await port.emulation.statistics.drop.get()
        port_drop.pkt_drop_count_total
        port_drop.pkt_drop_count_programmed
        port_drop.pkt_drop_count_bandwidth
        port_drop.pkt_drop_count_other
        port_drop.pkt_drop_ratio_total
        port_drop.pkt_drop_ratio_programmed
        port_drop.pkt_drop_ratio_bandwidth
        port_drop.pkt_drop_ratio_other

        port_corrupted = await port.emulation.statistics.corrupted.get()
        port_corrupted.fcs_corrupted_pkt_count
        port_corrupted.fcs_corrupted_pkt_ratio
        port_corrupted.ip_corrupted_pkt_count
        port_corrupted.ip_corrupted_pkt_ratio
        port_corrupted.tcp_corrupted_pkt_count
        port_corrupted.tcp_corrupted_pkt_ratio
        port_corrupted.total_corrupted_pkt_count
        port_corrupted.total_corrupted_pkt_ratio
        port_corrupted.udp_corrupted_pkt_count
        port_corrupted.udp_corrupted_pkt_ratio

        port_delayed = await port.emulation.statistics.latency.get()
        port_delayed.pkt_count
        port_delayed.ratio

        port_jittered = await port.emulation.statistics.jittered.get()
        port_jittered.pkt_count
        port_jittered.ratio

        port_duplicated = await port.emulation.statistics.duplicated.get()
        port_duplicated.pkt_count
        port_duplicated.ratio

        port_misordered = await port.emulation.statistics.mis_ordered.get()
        port_misordered.pkt_count
        port_misordered.ratio

        await port.emulation.clear.set()
# endregion
