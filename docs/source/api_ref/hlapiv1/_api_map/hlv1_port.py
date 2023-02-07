import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import utils, enums
from xoa_driver import misc


async def my_awesome_func() -> None:

    tester = await testers.L23Tester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)
    port = module.ports.obtain(0)

    #---------------------------------------#
    #                                       #
    #           Valkyrie Port               #
    #                                       #
    #---------------------------------------#
    if isinstance(port, ports.GenericL23Port):

        port.reservation
        port.reserved_by
        port.reset

        port.comment
        port.capabilities
        port.interface

        port.speed.mode.selection
        port.speed.mode.supported
        port.speed.current
        port.speed.reduction

        port.interframe_gap
        port.pause
        port.autotrain
        port.gap_monitor
        port.pfc_enable
        port.random_seed
        port.loop_back
        port.flash
        port.sync_status
        port.autoneg_selection
        port.checksum
        port.fec_mode
        port.tpld_mode
        port.dynamic
        port.tcvr_status

        port.preamble.rx_insert
        port.preamble.tx_remove

        port.net_config.mac_address
        port.net_config.ipv4.address
        port.net_config.ipv4.arp_reply
        port.net_config.ipv4.ping_reply
        port.net_config.ipv6.address
        port.net_config.ipv6.arp_reply
        port.net_config.ipv6.ping_reply

        port.arp_rx_table
        port.ndp_rx_table

        port.rate.fraction
        port.rate.l2_bps
        port.rate.pps

        port.latency_config.mode
        port.latency_config.offset

        port.multicast.header
        port.multicast.mode
        port.multicast.mode_extended
        port.multicast.source_list
        
        port.tx_config.mode
        port.tx_config.burst_period
        port.tx_config.delay
        port.tx_config.enable
        port.tx_config.packet_limit
        port.tx_config.time
        port.tx_config.time_limit
        port.tx_config.prepare

        port.traffic.state
        port.traffic.error

        port.capturer.state
        port.capturer.stats
        port.capturer.trigger
        port.capturer.keep

        port.tx_single_pkt.send
        port.tx_single_pkt.time

        port.mix.weights
        port.mix.lengths        

        port.uat.frame_loss_ratio
        port.uat.mode

        port.mdix_mode
        port.brr_mode
        
        port.runt.has_length_errors
        port.runt.rx_length
        port.runt.tx_length
        
        port.errors_count
        
        port.eee.capabilities
        port.eee.enable
        port.eee.mode
        port.eee.partner_capabilities
        port.eee.rx_power
        port.eee.snr_margin
        port.eee.status

        port.fault.status
        port.fault.signaling

        port.transceiver.access_mii
        port.transceiver.access_rw
        port.transceiver.access_rw_seq
        port.transceiver.access_temperature

        port.pcs_pma.alarms.errors
        port.pcs_pma.auto_neg.settings
        port.pcs_pma.auto_neg.status
        port.pcs_pma.error_gen.error_rate
        port.pcs_pma.error_gen.inject_one
        port.pcs_pma.lanes[0].lane_rx.errors
        port.pcs_pma.lanes[0].lane_rx.lock
        port.pcs_pma.lanes[0].lane_rx.status
        port.pcs_pma.lanes[0].tx_config
        port.pcs_pma.lanes[0].tx_error_inject
        port.pcs_pma.link_flap.enable.set()
        port.pcs_pma.link_flap.params
        port.pcs_pma.link_training.per_lane_status[0]
        port.pcs_pma.link_training.settings
        port.pcs_pma.phy.settings
        port.pcs_pma.phy.autoneg
        port.pcs_pma.phy.signal_status
        port.pcs_pma.pma_pulse_err_inj.enable
        port.pcs_pma.pma_pulse_err_inj.params
        port.pcs_pma.power_level.rx
        port.pcs_pma.power_level.tx
        port.pcs_pma.rx.clear
        port.pcs_pma.rx.fec
        port.pcs_pma.rx.total

        port.serdes[0].eye_diagram.ber
        port.serdes[0].eye_diagram.dwell_bits
        port.serdes[0].eye_diagram.info
        port.serdes[0].eye_diagram.measure
        port.serdes[0].eye_diagram.read_column
        port.serdes[0].eye_diagram.resolution
        port.serdes[0].phy.autotune
        port.serdes[0].phy.retune
        port.serdes[0].phy.rx_equalizer
        port.serdes[0].phy.tx_equalizer
        port.serdes[0].prbs.config
        port.serdes[0].prbs.status

        port.statistics.rx.clear
        port.statistics.rx.calibrate
        port.statistics.rx.extra
        port.statistics.rx.no_tpld
        port.statistics.rx.pfc_stats
        port.statistics.rx.total
        port.statistics.rx.uat.status
        port.statistics.rx.uat.time
        port.statistics.rx.access_tpld(tpld_id=1).errors
        port.statistics.rx.access_tpld(tpld_id=1).jitter
        port.statistics.rx.access_tpld(tpld_id=1).latency
        port.statistics.rx.access_tpld(tpld_id=1).traffic
        port.statistics.rx.obtain_filter_statistics(filter=1)
        port.statistics.rx.obtain_available_tplds()
        
        port.statistics.tx.clear
        port.statistics.tx.extra
        port.statistics.tx.no_tpld
        port.statistics.tx.total
        port.statistics.tx.obtain_from_stream(stream=1)

        port.is_released
        port.is_reserved_by_me
        port.is_reserved_by_others

        port.on_dynamic_change
        port.on_interface_change
        port.on_receive_sync_change
        port.on_reservation_change
        port.on_reserved_by_change
        port.on_speed_change
        port.on_traffic_change
        port.on_speed_selection_change

        port.streams.create()
        stream = port.streams.obtain(0)
        stream.comment
        stream.tpld_id
        stream.enable

        stream.rate.fraction
        stream.rate.l2bps
        stream.rate.pps

        stream.burst.burstiness
        stream.burst.gap

        stream.cdf.offset
        stream.cdf.count
        
        stream.inject_err.frame_checksum
        stream.inject_err.misorder
        stream.inject_err.payload_integrity
        stream.inject_err.sequence
        stream.inject_err.test_payload
        stream.insert_packets_checksum

        stream.request.arp
        stream.request.ping
        
        stream.payload.content
        stream.payload.extended
        
        stream.priority_flow

        stream.packet.header.data
        stream.packet.header.protocol
        stream.packet.length
        stream.packet.limit
        stream.gateway.ipv4
        stream.gateway.ipv6

        stream.packet.header.modifiers.configure(1)
        stream.packet.header.modifiers.clear()
        modifier = stream.packet.header.modifiers.index(0)
        modifier.range
        modifier.specification

        stream.packet.header.modifiers_extended.configure(1)
        stream.packet.header.modifiers_extended.clear()
        modifier_ex = stream.packet.header.modifiers_extended.index(0)
        modifier_ex.range
        modifier_ex.specification

        port.datasets.create()
        dataset = port.datasets.obtain(0)
        dataset.enable
        dataset.source
        dataset.range
        dataset.samples
        dataset.kind

        port.filters.create()
        filter = port.filters.obtain(0)
        filter.comment
        filter.condition
        filter.enable
        filter.string
        filter.kind

        port.length_terms.create()
        length_term = port.length_terms.obtain(0)
        length_term.length

        port.match_terms.create()
        match_term = port.match_terms.obtain(0)
        match_term.match
        match_term.position
        match_term.protocol.set()

    #---------------------------------------#
    #                                       #
    #            Chimera Port               #
    #                                       #
    #---------------------------------------#
    if isinstance(port, ports.PortChimera):      

        port.reservation
        port.reserved_by
        port.reset

        port.comment
        port.capabilities
        port.interface
        port.sync_status

        port.pcs_pma.link_flap.params
        port.pcs_pma.link_flap.enable
        port.pcs_pma.pma_pulse_err_inj.enable
        port.pcs_pma.pma_pulse_err_inj.params

        port.emulate
        port.emulation.clear
        port.emulation.drop_fcs_errors

        port.emulation.statistics.corrupted
        port.emulation.statistics.drop
        port.emulation.statistics.duplicated
        port.emulation.statistics.jittered
        port.emulation.statistics.latency
        port.emulation.statistics.mis_ordered
        port.emulation.tpld_mode

        port.is_released
        port.is_reserved_by_me
        port.is_reserved_by_others

        port.on_emulate_change
        port.on_reserved_by_change
        port.on_interface_change
        port.on_receive_sync_change
        port.on_reservation_change

        port.emulation.flows[0].impairment_distribution.corruption_type_config.off

        port.emulation.flows[0].impairment_distribution.drop_type_config.accumulate_and_burst
        port.emulation.flows[0].impairment_distribution.drop_type_config.bit_error_rate
        port.emulation.flows[0].impairment_distribution.drop_type_config.constant_delay
        port.emulation.flows[0].impairment_distribution.drop_type_config.custom
        port.emulation.flows[0].impairment_distribution.drop_type_config.enable
        port.emulation.flows[0].impairment_distribution.drop_type_config.fixed_burst
        port.emulation.flows[0].impairment_distribution.drop_type_config.fixed
        port.emulation.flows[0].impairment_distribution.drop_type_config.gamma
        port.emulation.flows[0].impairment_distribution.drop_type_config.gaussian
        port.emulation.flows[0].impairment_distribution.drop_type_config.ge
        port.emulation.flows[0].impairment_distribution.drop_type_config.off
        port.emulation.flows[0].impairment_distribution.drop_type_config.one_shot_status
        port.emulation.flows[0].impairment_distribution.drop_type_config.poison
        port.emulation.flows[0].impairment_distribution.drop_type_config.random
        port.emulation.flows[0].impairment_distribution.drop_type_config.uniform
        port.emulation.flows[0].impairment_distribution.drop_type_config.step
        port.emulation.flows[0].impairment_distribution.drop_type_config.schedule

        port.emulation.flows[0].impairment_distribution.duplication_type_config.accumulate_and_burst
        port.emulation.flows[0].impairment_distribution.duplication_type_config.bit_error_rate
        port.emulation.flows[0].impairment_distribution.duplication_type_config.constant_delay
        port.emulation.flows[0].impairment_distribution.duplication_type_config.custom
        port.emulation.flows[0].impairment_distribution.duplication_type_config.enable
        port.emulation.flows[0].impairment_distribution.duplication_type_config.fixed_burst
        port.emulation.flows[0].impairment_distribution.duplication_type_config.fixed
        port.emulation.flows[0].impairment_distribution.duplication_type_config.gamma
        port.emulation.flows[0].impairment_distribution.duplication_type_config.gaussian
        port.emulation.flows[0].impairment_distribution.duplication_type_config.ge
        port.emulation.flows[0].impairment_distribution.duplication_type_config.off
        port.emulation.flows[0].impairment_distribution.duplication_type_config.one_shot_status
        port.emulation.flows[0].impairment_distribution.duplication_type_config.poison
        port.emulation.flows[0].impairment_distribution.duplication_type_config.random
        port.emulation.flows[0].impairment_distribution.duplication_type_config.uniform
        port.emulation.flows[0].impairment_distribution.duplication_type_config.step
        port.emulation.flows[0].impairment_distribution.duplication_type_config.schedule

        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.accumulate_and_burst
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.bit_error_rate
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.constant_delay
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.custom
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.enable
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.fixed_burst
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.fixed
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.gamma
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.gaussian
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.ge
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.off
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.one_shot_status
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.poison
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.random
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.uniform
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.step
        port.emulation.flows[0].impairment_distribution.latency_jitter_type_config.schedule

        port.emulation.flows[0].impairment_distribution.misorder_type_config.accumulate_and_burst
        port.emulation.flows[0].impairment_distribution.misorder_type_config.bit_error_rate
        port.emulation.flows[0].impairment_distribution.misorder_type_config.constant_delay
        port.emulation.flows[0].impairment_distribution.misorder_type_config.custom
        port.emulation.flows[0].impairment_distribution.misorder_type_config.enable
        port.emulation.flows[0].impairment_distribution.misorder_type_config.fixed_burst
        port.emulation.flows[0].impairment_distribution.misorder_type_config.fixed
        port.emulation.flows[0].impairment_distribution.misorder_type_config.gamma
        port.emulation.flows[0].impairment_distribution.misorder_type_config.gaussian
        port.emulation.flows[0].impairment_distribution.misorder_type_config.ge
        port.emulation.flows[0].impairment_distribution.misorder_type_config.off
        port.emulation.flows[0].impairment_distribution.misorder_type_config.one_shot_status
        port.emulation.flows[0].impairment_distribution.misorder_type_config.poison
        port.emulation.flows[0].impairment_distribution.misorder_type_config.random
        port.emulation.flows[0].impairment_distribution.misorder_type_config.uniform
        port.emulation.flows[0].impairment_distribution.misorder_type_config.step
        port.emulation.flows[0].impairment_distribution.misorder_type_config.schedule

        port.emulation.flows[0].impairment_distribution.policer_type_config.accumulate_and_burst
        port.emulation.flows[0].impairment_distribution.policer_type_config.bit_error_rate
        port.emulation.flows[0].impairment_distribution.policer_type_config.constant_delay
        port.emulation.flows[0].impairment_distribution.policer_type_config.custom
        port.emulation.flows[0].impairment_distribution.policer_type_config.enable
        port.emulation.flows[0].impairment_distribution.policer_type_config.fixed_burst
        port.emulation.flows[0].impairment_distribution.policer_type_config.fixed
        port.emulation.flows[0].impairment_distribution.policer_type_config.gamma
        port.emulation.flows[0].impairment_distribution.policer_type_config.gaussian
        port.emulation.flows[0].impairment_distribution.policer_type_config.ge
        port.emulation.flows[0].impairment_distribution.policer_type_config.off
        port.emulation.flows[0].impairment_distribution.policer_type_config.one_shot_status
        port.emulation.flows[0].impairment_distribution.policer_type_config.poison
        port.emulation.flows[0].impairment_distribution.policer_type_config.random
        port.emulation.flows[0].impairment_distribution.policer_type_config.uniform
        port.emulation.flows[0].impairment_distribution.policer_type_config.step
        port.emulation.flows[0].impairment_distribution.policer_type_config.schedule

        port.emulation.flows[0].impairment_distribution.shaper_type_config.accumulate_and_burst
        port.emulation.flows[0].impairment_distribution.shaper_type_config.bit_error_rate
        port.emulation.flows[0].impairment_distribution.shaper_type_config.constant_delay
        port.emulation.flows[0].impairment_distribution.shaper_type_config.custom
        port.emulation.flows[0].impairment_distribution.shaper_type_config.enable
        port.emulation.flows[0].impairment_distribution.shaper_type_config.fixed_burst
        port.emulation.flows[0].impairment_distribution.shaper_type_config.fixed
        port.emulation.flows[0].impairment_distribution.shaper_type_config.gamma
        port.emulation.flows[0].impairment_distribution.shaper_type_config.gaussian
        port.emulation.flows[0].impairment_distribution.shaper_type_config.ge
        port.emulation.flows[0].impairment_distribution.shaper_type_config.off
        port.emulation.flows[0].impairment_distribution.shaper_type_config.one_shot_status
        port.emulation.flows[0].impairment_distribution.shaper_type_config.poison
        port.emulation.flows[0].impairment_distribution.shaper_type_config.random
        port.emulation.flows[0].impairment_distribution.shaper_type_config.uniform
        port.emulation.flows[0].impairment_distribution.shaper_type_config.step
        port.emulation.flows[0].impairment_distribution.shaper_type_config.schedule
        
        port.emulation.flows[0].shadow_filter.apply
        port.emulation.flows[0].shadow_filter.enable
        port.emulation.flows[0].shadow_filter.initiating

        port.emulation.flows[0].shadow_filter.use_basic_mode()
        port.emulation.flows[0].shadow_filter.use_extended_mode()

        filter = port.emulation.flows[0].working_filter.get_mode()
        if isinstance(filter, misc.BasicImpairmentFlowFilter):
            filter.ethernet.dest_address
            filter.ethernet.src_address
            filter.ethernet.settings
            filter.ip.v4.settings
            filter.ip.v4.dest_address
            filter.ip.v4.src_address
            filter.ip.v4.dscp
            filter.ip.v6.settings
            filter.ip.v6.dest_address
            filter.ip.v6.src_address
            filter.ip.v6.traffic_class
            filter.l2plus_use
            filter.l3_use
            filter.mpls.label
            filter.mpls.settings
            filter.mpls.toc
            filter.any.config
            filter.any.settings
            filter.tcp.settings
            filter.tcp.dest_port
            filter.tcp.src_port
            filter.udp.src_port
            filter.udp.dest_port
            filter.udp.settings
            filter.vlan.settings
            filter.vlan.inner
            filter.vlan.outer
            filter.tpld.settings
            filter.tpld.test_payload_filters_config

        if isinstance(filter, misc.ExtendedImpairmentFlowFilter):
            p = filter.get_protocol_segments(0)


async def my_awesome_func2() -> None:
    tester = await testers.L47Tester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)
    port = module.ports.obtain(0)

    #---------------------------------------#
    #                                       #
    #           Vulcan Port                 #
    #                                       #
    #---------------------------------------#
    if isinstance(port, ports.PortL47):
        port.aptitudes
        port.arp_config
        port.ndp_config
        port.capabilities
        port.capture.get_first_frame
        port.capture.get_next_frame
        port.capture.start
        port.clear
        port.comment
        port.interface

        port.last_state_status
        port.license_info
        port.max_packet_rate
        
        port.nic_firmware_version
        port.nic_name

        port.counters.arp.total
        port.counters.arp.rx
        port.counters.arp.tx
        port.counters.clear
        port.counters.eth.total
        port.counters.eth.rx
        port.counters.eth.tx
        port.counters.icmp.total
        port.counters.icmp.rx
        port.counters.icmp.tx
        port.counters.ipv4.total
        port.counters.ipv4.rx
        port.counters.ipv4.tx
        port.counters.ipv6.total
        port.counters.ipv6.rx
        port.counters.ipv6.tx
        port.counters.ndp.total
        port.counters.ndp.rx
        port.counters.ndp.tx
        port.counters.tcp.total
        port.counters.tcp.rx
        port.counters.tcp.tx
        port.counters.udp.total
        port.counters.udp.rx
        port.counters.udp.tx
        port.counters.total
        port.counters.total_rx
        port.counters.total_tx

        port.connection_groups.create()
        cg = port.connection_groups.obtain(0)

        cg.comment
        cg.counters.clear
        cg.histogram.config.transaction
        cg.histogram.config.payload
        cg.histogram.config.time
        cg.histogram.recalculates.transaction
        cg.histogram.recalculates.payload
        cg.histogram.recalculates.time
        cg.histogram.transaction

        cg.l2.address_resolve
        cg.l2.gateway.ipv4
        cg.l2.gateway.ipv6
        cg.l2.gateway.use
        cg.l2.mac.client
        cg.l2.mac.server
        cg.l2.vlan.enable
        cg.l2.vlan.tci

        cg.l3.ip_version
        cg.l3.ipv4.client_range
        cg.l3.ipv4.server_range
        cg.l3.diffserv.mask
        cg.l3.diffserv.range_limits
        cg.l3.diffserv.step
        cg.l3.diffserv.type
        cg.l3.diffserv.value
        cg.l3.ipv6.client_range
        cg.l3.ipv6.server_range
        cg.l3.ipv6.flow_label
        cg.l3.ipv6.traffic_class
        cg.l3.nat

        cg.layer4_protocol

        cg.tcp.ack.duplicate_thresholds
        cg.tcp.ack.frequency
        cg.tcp.ack.timeout
        
        cg.tcp.counters.error
        cg.tcp.counters.packet.tx
        cg.tcp.counters.packet.rx
        cg.tcp.counters.payload.rx
        cg.tcp.counters.payload.tx
        cg.tcp.counters.retransmission
        cg.tcp.counters.state.current
        cg.tcp.counters.state.rate
        cg.tcp.counters.state.total

        cg.tcp.clear_post_test_statistics

        cg.tcp.cwnd.congestion_mode
        cg.tcp.cwnd.icwnd_calc_method

        cg.tcp.histogram.connection.close_times
        cg.tcp.histogram.connection.establish_times
        cg.tcp.histogram.rx.good_bytes
        cg.tcp.histogram.rx.total_bytes
        cg.tcp.histogram.tx.good_bytes
        cg.tcp.histogram.tx.total_bytes

        cg.tcp.iss_treshold

        cg.tcp.mss.fixed_value
        cg.tcp.mss.range_limits
        cg.tcp.mss.type

        cg.tcp.rwnd.scaling
        cg.tcp.rwnd.size

        cg.tcp.rto.prolonged_mode
        cg.tcp.rto.range_limits
        cg.tcp.rto.syn_value
        cg.tcp.rto.value

        cg.udp.counters.packet.rx
        cg.udp.counters.packet.tx
        cg.udp.counters.payload.rx
        cg.udp.counters.payload.tx
        cg.udp.counters.state.current
        cg.udp.counters.state.rate
        cg.udp.counters.state.total
        cg.udp.histogram.rx_bytes
        cg.udp.histogram.tx_bytes
        cg.udp.packet_size.range_limits
        cg.udp.packet_size.type
        cg.udp.packet_size.value

        cg.raw.bursty.config
        cg.raw.bursty.transmission
        cg.raw.connection.close_condition
        cg.raw.connection.incarnation
        cg.raw.connection.lifetime
        cg.raw.connection.repetitions
        cg.raw.download_request.content
        cg.raw.download_request.server_must_wait
        cg.raw.download_request.transactions_number
        cg.raw.payload.content
        cg.raw.payload.repeat_length
        cg.raw.payload.rx_length
        cg.raw.payload.type
        cg.raw.payload.total_length
        cg.raw.test_scenario
        cg.raw.transaction_counter.transaction
        cg.raw.tx.during_ramp
        cg.raw.tx.time_offset
        cg.raw.utilization

        cg.replay.utilization
        cg.replay.counters.replay
        cg.replay.files.indices
        cg.replay.files.clear_index
        cg.replay.files.name
        cg.replay.user.incarnation
        cg.replay.user.repetitions

        cg.role
        cg.status
        
        cg.test_application
        cg.load_profile.shape
        cg.load_profile.time_scale

        cg.tls.cipher_suites
        cg.tls.close_notify
        cg.tls.counters.alert.fatal
        cg.tls.counters.alert.warning
        cg.tls.counters.payload.rx
        cg.tls.counters.payload.tx
        cg.tls.counters.state.current
        cg.tls.counters.state.rate
        cg.tls.counters.state.total
        cg.tls.enable
        cg.tls.file.certificate_path
        cg.tls.file.dhparams_path
        cg.tls.file.private_key_path
        cg.tls.histogram.handshake
        cg.tls.histogram.payload.rx_bytes
        cg.tls.histogram.payload.tx_bytes
        cg.tls.max_record_size
        cg.tls.protocol.min_required_version
        cg.tls.protocol.version
        cg.tls.server_name

        cg.user_state.current
        cg.user_state.rate
        cg.user_state.total

        port.is_released
        port.is_reserved_by_me
        port.is_reserved_by_others

        port.on_capabilities_change
        port.on_interface_change
        port.on_license_info_change
        port.on_receive_sync_change
        port.on_reservation_change
        port.on_reserved_by_change
        port.on_speed_selection_change
        port.on_state_change


async def my_awesome_func3() -> None:
    tester = await testers.L23VeTester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)
    port = module.ports.obtain(0)

    #---------------------------------------#
    #                                       #
    #           Valkyrie Port               #
    #                                       #
    #---------------------------------------#
    if isinstance(port, ports.PortL23VE):

        port.reservation
        port.reserved_by
        port.reset

        port.comment
        port.capabilities
        port.interface

        port.speed
        port.speed.mode.selection
        port.speed.mode.supported
        port.speed.current
        port.speed.reduction

        port.interframe_gap
        port.pause
        port.autotrain
        port.gap_monitor
        port.pfc_enable
        port.random_seed
        port.loop_back
        port.sync_status
        port.checksum
        port.tpld_mode

        port.net_config.mac_address
        port.net_config.ipv4.address
        port.net_config.ipv4.arp_reply
        port.net_config.ipv4.ping_reply
        port.net_config.ipv6.address
        port.net_config.ipv6.arp_reply
        port.net_config.ipv6.ping_reply

        port.arp_rx_table
        port.ndp_rx_table

        port.rate.fraction
        port.rate.l2_bps
        port.rate.pps

        port.latency_config.mode
        port.latency_config.offset

        port.multicast.header
        port.multicast.mode
        port.multicast.mode_extended
        port.multicast.source_list
        
        port.tx_config.mode
        port.tx_config.burst_period
        port.tx_config.delay
        port.tx_config.enable
        port.tx_config.packet_limit
        port.tx_config.time
        port.tx_config.time_limit
        port.tx_config.prepare

        port.traffic.state
        port.traffic.error

        port.capturer.state
        port.capturer.stats
        port.capturer.trigger
        port.capturer.keep

        port.tx_single_pkt.send
        port.tx_single_pkt.time

        port.mix.weights
        port.mix.lengths        

        port.mdix_mode

        port.errors_count

        port.statistics.rx.clear
        port.statistics.rx.calibrate
        port.statistics.rx.extra
        port.statistics.rx.no_tpld
        port.statistics.rx.pfc_stats
        port.statistics.rx.total
        port.statistics.rx.access_tpld(tpld_id=1).errors
        port.statistics.rx.access_tpld(tpld_id=1).jitter
        port.statistics.rx.access_tpld(tpld_id=1).latency
        port.statistics.rx.access_tpld(tpld_id=1).traffic
        port.statistics.rx.obtain_filter_statistics(filter=1)
        port.statistics.rx.obtain_available_tplds()
        
        port.statistics.tx.clear
        port.statistics.tx.extra
        port.statistics.tx.no_tpld
        port.statistics.tx.total
        port.statistics.tx.obtain_from_stream(stream=1)

        port.is_released
        port.is_reserved_by_me
        port.is_reserved_by_others

        port.on_interface_change
        port.on_receive_sync_change
        port.on_reservation_change
        port.on_reserved_by_change
        port.on_speed_change
        port.on_traffic_change

        port.streams.create()
        stream = port.streams.obtain(0)
        stream.comment
        stream.tpld_id
        stream.enable

        stream.rate.fraction
        stream.rate.l2bps
        stream.rate.pps

        stream.burst.burstiness
        stream.burst.gap

        stream.cdf.offset
        stream.cdf.count
        
        stream.inject_err.frame_checksum
        stream.inject_err.misorder
        stream.inject_err.payload_integrity
        stream.inject_err.sequence
        stream.inject_err.test_payload
        stream.insert_packets_checksum

        stream.request.arp
        stream.request.ping
        
        stream.payload.content
        stream.payload.extended
        
        stream.priority_flow

        stream.packet.header.data
        stream.packet.header.protocol
        stream.packet.length
        stream.packet.limit
        stream.gateway.ipv4
        stream.gateway.ipv6

        stream.packet.header.modifiers.configure(1)
        stream.packet.header.modifiers.clear()
        modifier = stream.packet.header.modifiers.index(0)
        modifier.range
        modifier.specification

        stream.packet.header.modifiers_extended.configure(1)
        stream.packet.header.modifiers_extended.clear()
        modifier_ex = stream.packet.header.modifiers_extended.index(0)
        modifier_ex.range
        modifier_ex.specification

        port.filters.create()
        filter = port.filters.obtain(0)
        filter.comment
        filter.condition
        filter.enable
        filter.string
        filter.kind

        port.length_terms.create()
        length_term = port.length_terms.obtain(0)
        length_term.length

        port.match_terms.create()
        match_term = port.match_terms.obtain(0)
        match_term.match
        match_term.position
        match_term.protocol.set()


async def my_awesome_func2() -> None:
    tester = await testers.L47VeTester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)
    port = module.ports.obtain(0)

    #---------------------------------------#
    #                                       #
    #           VulcanVE Port                 #
    #                                       #
    #---------------------------------------#
    if isinstance(port, ports.L):
        port.aptitudes
        port.arp_config
        port.ndp_config
        port.capabilities
        port.capture.get_first_frame
        port.capture.get_next_frame
        port.capture.start
        port.clear
        port.comment
        port.interface

        port.last_state_status
        port.license_info
        port.max_packet_rate
        
        port.nic_firmware_version
        port.nic_name

        port.counters.arp.total
        port.counters.arp.rx
        port.counters.arp.tx
        port.counters.clear
        port.counters.eth.total
        port.counters.eth.rx
        port.counters.eth.tx
        port.counters.icmp.total
        port.counters.icmp.rx
        port.counters.icmp.tx
        port.counters.ipv4.total
        port.counters.ipv4.rx
        port.counters.ipv4.tx
        port.counters.ipv6.total
        port.counters.ipv6.rx
        port.counters.ipv6.tx
        port.counters.ndp.total
        port.counters.ndp.rx
        port.counters.ndp.tx
        port.counters.tcp.total
        port.counters.tcp.rx
        port.counters.tcp.tx
        port.counters.udp.total
        port.counters.udp.rx
        port.counters.udp.tx
        port.counters.total
        port.counters.total_rx
        port.counters.total_tx

        port.connection_groups.create()
        cg = port.connection_groups.obtain(0)

        cg.comment
        cg.counters.clear
        cg.histogram.config.transaction
        cg.histogram.config.payload
        cg.histogram.config.time
        cg.histogram.recalculates.transaction
        cg.histogram.recalculates.payload
        cg.histogram.recalculates.time
        cg.histogram.transaction

        cg.l2.address_resolve
        cg.l2.gateway.ipv4
        cg.l2.gateway.ipv6
        cg.l2.gateway.use
        cg.l2.mac.client
        cg.l2.mac.server
        cg.l2.vlan.enable
        cg.l2.vlan.tci

        cg.l3.ip_version
        cg.l3.ipv4.client_range
        cg.l3.ipv4.server_range
        cg.l3.diffserv.mask
        cg.l3.diffserv.range_limits
        cg.l3.diffserv.step
        cg.l3.diffserv.type
        cg.l3.diffserv.value
        cg.l3.ipv6.client_range
        cg.l3.ipv6.server_range
        cg.l3.ipv6.flow_label
        cg.l3.ipv6.traffic_class
        cg.l3.nat

        cg.layer4_protocol

        cg.tcp.ack.duplicate_thresholds
        cg.tcp.ack.frequency
        cg.tcp.ack.timeout
        
        cg.tcp.counters.error
        cg.tcp.counters.packet.tx
        cg.tcp.counters.packet.rx
        cg.tcp.counters.payload.rx
        cg.tcp.counters.payload.tx
        cg.tcp.counters.retransmission
        cg.tcp.counters.state.current
        cg.tcp.counters.state.rate
        cg.tcp.counters.state.total

        cg.tcp.clear_post_test_statistics

        cg.tcp.cwnd.congestion_mode
        cg.tcp.cwnd.icwnd_calc_method

        cg.tcp.histogram.connection.close_times
        cg.tcp.histogram.connection.establish_times
        cg.tcp.histogram.rx.good_bytes
        cg.tcp.histogram.rx.total_bytes
        cg.tcp.histogram.tx.good_bytes
        cg.tcp.histogram.tx.total_bytes

        cg.tcp.iss_treshold

        cg.tcp.mss.fixed_value
        cg.tcp.mss.range_limits
        cg.tcp.mss.type

        cg.tcp.rwnd.scaling
        cg.tcp.rwnd.size

        cg.tcp.rto.prolonged_mode
        cg.tcp.rto.range_limits
        cg.tcp.rto.syn_value
        cg.tcp.rto.value

        cg.udp.counters.packet.rx
        cg.udp.counters.packet.tx
        cg.udp.counters.payload.rx
        cg.udp.counters.payload.tx
        cg.udp.counters.state.current
        cg.udp.counters.state.rate
        cg.udp.counters.state.total
        cg.udp.histogram.rx_bytes
        cg.udp.histogram.tx_bytes
        cg.udp.packet_size.range_limits
        cg.udp.packet_size.type
        cg.udp.packet_size.value

        cg.raw.bursty.config
        cg.raw.bursty.transmission
        cg.raw.connection.close_condition
        cg.raw.connection.incarnation
        cg.raw.connection.lifetime
        cg.raw.connection.repetitions
        cg.raw.download_request.content
        cg.raw.download_request.server_must_wait
        cg.raw.download_request.transactions_number
        cg.raw.payload.content
        cg.raw.payload.repeat_length
        cg.raw.payload.rx_length
        cg.raw.payload.type
        cg.raw.payload.total_length
        cg.raw.test_scenario
        cg.raw.transaction_counter.transaction
        cg.raw.tx.during_ramp
        cg.raw.tx.time_offset
        cg.raw.utilization

        cg.replay.utilization
        cg.replay.counters.replay
        cg.replay.files.indices
        cg.replay.files.clear_index
        cg.replay.files.name
        cg.replay.user.incarnation
        cg.replay.user.repetitions

        cg.role
        cg.status
        
        cg.test_application
        cg.load_profile.shape
        cg.load_profile.time_scale

        cg.tls.cipher_suites
        cg.tls.close_notify
        cg.tls.counters.alert.fatal
        cg.tls.counters.alert.warning
        cg.tls.counters.payload.rx
        cg.tls.counters.payload.tx
        cg.tls.counters.state.current
        cg.tls.counters.state.rate
        cg.tls.counters.state.total
        cg.tls.enable
        cg.tls.file.certificate_path
        cg.tls.file.dhparams_path
        cg.tls.file.private_key_path
        cg.tls.histogram.handshake
        cg.tls.histogram.payload.rx_bytes
        cg.tls.histogram.payload.tx_bytes
        cg.tls.max_record_size
        cg.tls.protocol.min_required_version
        cg.tls.protocol.version
        cg.tls.server_name

        cg.user_state.current
        cg.user_state.rate
        cg.user_state.total

        port.is_released
        port.is_reserved_by_me
        port.is_reserved_by_others

        port.on_capabilities_change
        port.on_interface_change
        port.on_license_info_change
        port.on_receive_sync_change
        port.on_reservation_change
        port.on_reserved_by_change
        port.on_speed_selection_change
        port.on_state_change

