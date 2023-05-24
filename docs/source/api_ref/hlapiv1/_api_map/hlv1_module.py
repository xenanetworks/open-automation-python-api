import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import utils, enums
from xoa_driver import misc


async def my_awesome_func() -> None:

    tester = await testers.L23Tester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)

    #---------------------------------------#
    #                                       #
    #           Valkyrie Module             #
    #                                       #
    #---------------------------------------#
    if isinstance(module, modules.ModuleL23):

        module.ports.obtain

        module.name
        module.capabilities
        module.comment
        module.status
        module.port_count

        module.reservation
        module.reserved_by

        module.model
        module.revision

        module.media
        module.available_speeds
        
        module.serial_number
        module.version_number

        module.timing.clock_local_adjust
        module.timing.clock_sync_status
        module.timing.source

        module.advanced_timing.clock_tx.filter
        module.advanced_timing.clock_tx.source
        module.advanced_timing.clock_tx.status
        module.advanced_timing.sma.status
        module.advanced_timing.sma.input
        module.advanced_timing.sma.output
        
        module.cfp.config
        module.cfp.type

        module.clock_sweep.config
        module.clock_sweep.status

        module.upgrade.progress
        module.upgrade.reload_image
        module.upgrade.start

        module.is_released()
        module.is_reserved_by_me()

    #---------------------------------------#
    #                                       #
    #           Chimera Module              #
    #                                       #
    #---------------------------------------# 
    if isinstance(module, modules.ModuleChimera):

        module.ports.obtain

        module.emulator_bypass_mode
        module.latency_mode
        
        module.name
        module.capabilities
        module.comment
        module.status
        module.port_count

        module.reservation
        module.reserved_by

        module.model
        module.revision

        module.media
        module.available_speeds
        
        module.serial_number
        module.version_number

        module.timing.clock_local_adjust
        module.timing.clock_sync_status
        module.timing.source
        
        module.cfp.config
        module.cfp.type

        module.upgrade.progress
        module.upgrade.start

        module.tx_clock.source
        module.tx_clock.status

        module.is_released()
        module.is_reserved_by_me()


    #---------------------------------------#
    #                                       #
    #           Vulcan Module               #
    #                                       #
    #---------------------------------------#
    tester = await testers.L47Tester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)

    if isinstance(module, modules.ModuleL47):

        module.ports.obtain

        module.port_count

        module.reservation
        module.reserved_by

        module.model
        module.time
        module.memory_info

        module.module_system.id
        module.module_system.status
        module.module_system.time
        
        module.serial_number
        module.version_number

        module.capture.file_delete
        module.capture.file_list
        module.capture.file_list_bson
        module.capture.parse.parser_params
        module.capture.parse.start
        module.capture.parse.state
        module.capture.parse.stop
        module.capture.size

        module.compatible_client_version

        module.license.clock_windback
        module.license.demo_info
        module.license.list_bson
        module.license.management_info
        module.license.online_mode
        module.license.update
        module.license.update_status

        module.packet_engine.license_info
        module.packet_engine.mode
        module.packet_engine.reserve
        
        module.replay.file.delete
        module.replay.file.list
        module.replay.file.list_bson

        module.tls_cipher

        module.is_released()
        module.is_reserved_by_me()


    #---------------------------------------#
    #                                       #
    #           ValkyrieVE Module           #
    #                                       #
    #---------------------------------------#
    tester = await testers.L23VeTester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)

    if isinstance(module, modules.ModuleL23VE):

        module.ports.obtain


        module.capabilities
        module.comment

        module.port_count

        module.reservation
        module.reserved_by

        module.model

        module.serial_number
        module.version_number

        module.is_released()
        module.is_reserved_by_me()


    #---------------------------------------#
    #                                       #
    #           VulcanVEModule              #
    #                                       #
    #---------------------------------------#
    tester = await testers.L47VeTester("0.0.0.0", "xoa") 
    module = tester.modules.obtain(0)

    if isinstance(module, modules.ModuleL47VE):

        module.ports.obtain

        module.port_count

        module.reservation
        module.reserved_by

        module.model
        module.time
        module.memory_info

        module.module_system.id
        module.module_system.status
        module.module_system.time
        
        module.serial_number
        module.version_number

        module.capture.file_delete
        module.capture.file_list
        module.capture.file_list_bson
        module.capture.parse.parser_params
        module.capture.parse.start
        module.capture.parse.state
        module.capture.parse.stop
        module.capture.size

        module.compatible_client_version

        module.license.clock_windback
        module.license.demo_info
        module.license.list_bson
        module.license.management_info
        module.license.online_mode
        module.license.update
        module.license.update_status

        module.packet_engine.license_info
        module.packet_engine.mode
        module.packet_engine.reserve
        
        module.replay.file.delete
        module.replay.file.list
        module.replay.file.list_bson

        module.tls_cipher

        module.is_released()
        module.is_reserved_by_me()
    