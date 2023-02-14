import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import utils, enums
from xoa_driver import misc


async def my_awesome_func1() -> None:

    #---------------------------------------#
    #                                       #
    #           Valkyrie Tester             #
    #                                       #
    #---------------------------------------#

    tester = await testers.L23Tester("0.0.0.0", "xoa") 
    
    tester.modules.obtain
    tester.modules.obtain_multiple

    tester.name
    tester.password
    tester.comment
    tester.capabilities
    tester.debug_log
    tester.build_string
    tester.down
    tester.model
    tester.multiuser
    tester.session.owner_name
    tester.session.keepalive
    tester.session.pwd
    tester.session.logoff
    tester.session.is_online
    tester.session.sessions_info
    tester.session.timeout
    tester.flash
    
    tester.management_interface.dhcp
    tester.management_interface.hostname
    tester.management_interface.ip_address
    tester.management_interface.macaddress
    
    tester.reservation
    tester.reserved_by

    tester.serial_no
    tester.version_no
    tester.version_no_minor
    
    tester.time
    tester.time_keeper.config_file
    tester.time_keeper.gps_state
    tester.time_keeper.license_file
    tester.time_keeper.license_state
    tester.time_keeper.status
    tester.time_keeper.status_extended
    tester.time_keeper.status

    tester.rest_api_server.status
    tester.rest_api_server.control
    tester.rest_api_server.enable
    tester.rest_api_server.port

    tester.traffic
    tester.traffic_sync
    
    tester.upload_file.data
    tester.upload_file.finish
    tester.upload_file.start

    tester.is_released()
    tester.is_reserved_by_me()
    tester.on_disconnected(my_callback_func())
    tester.on_reservation_change(my_callback_func())
    tester.on_disconnected(my_callback_func())


    #---------------------------------------#
    #                                       #
    #           Vulcan Tester               #
    #                                       #
    #---------------------------------------#

    tester = await testers.L47Tester("0.0.0.0", "xoa") 

    tester.modules.obtain
    tester.modules.obtain_multiple

    tester.name
    tester.password
    tester.comment
    tester.capabilities
    tester.debug_log
    tester.build_string
    tester.down
    tester.model
    tester.session.owner_name
    tester.session.keepalive
    tester.session.pwd
    tester.session.logoff
    tester.session.is_online
    tester.session.sessions_info
    tester.session.timeout
    tester.flash
    
    tester.management_interface.dhcp
    tester.management_interface.hostname
    tester.management_interface.ip_address
    tester.management_interface.macaddress
    
    tester.reservation
    tester.reserved_by

    tester.serial_no
    tester.version_no
    
    tester.time

    tester.is_released()
    tester.is_reserved_by_me()
    tester.on_disconnected(my_callback_func())
    tester.on_reservation_change(my_callback_func())
    tester.on_disconnected(my_callback_func())


    #---------------------------------------#
    #                                       #
    #           ValkyrieVE Tester           #
    #                                       #
    #---------------------------------------#

    tester = await testers.L23VeTester("0.0.0.0", "xoa") 

    tester.modules.obtain
    tester.modules.obtain_multiple

    tester.name
    tester.password
    tester.comment
    tester.capabilities
    tester.debug_log
    tester.down
    tester.model
    tester.multiuser
    tester.session.owner_name
    tester.session.keepalive
    tester.session.pwd
    tester.session.logoff
    tester.session.is_online
    tester.session.sessions_info
    tester.session.timeout
    tester.flash
    
    tester.reservation
    tester.reserved_by

    tester.serial_no
    tester.version_no
    tester.version_no_minor
    
    tester.time

    tester.traffic
    tester.traffic_sync

    tester.is_released()
    tester.is_reserved_by_me()
    tester.on_disconnected(my_callback_func())
    tester.on_reservation_change(my_callback_func())
    tester.on_disconnected(my_callback_func())


    #---------------------------------------#
    #                                       #
    #           VulcanVE Tester             #
    #                                       #
    #---------------------------------------#

    tester = await testers.L47VeTester("0.0.0.0", "xoa") 

    tester.modules.obtain
    tester.modules.obtain_multiple

    tester.name
    tester.password
    tester.comment
    tester.capabilities
    tester.debug_log
    tester.build_string
    tester.down
    tester.model
    tester.session.owner_name
    tester.session.keepalive
    tester.session.pwd
    tester.session.logoff
    tester.session.is_online
    tester.session.sessions_info
    tester.session.timeout
    tester.flash
    
    tester.management_interface.dhcp
    tester.management_interface.hostname
    tester.management_interface.ip_address
    tester.management_interface.macaddress
    
    tester.reservation
    tester.reserved_by

    tester.serial_no
    tester.version_no
    tester.version_no_minor
    
    tester.time

    tester.is_released()
    tester.is_reserved_by_me()
    tester.on_disconnected(my_callback_func())
    tester.on_reservation_change(my_callback_func())
    tester.on_disconnected(my_callback_func())
    