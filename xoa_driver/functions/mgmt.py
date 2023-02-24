from __future__ import annotations
import asyncio
import typing as t
from xoa_driver import enums
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v2.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v2.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.modules import GenericAnyModule, GenericL23Module, ModuleChimera
from xoa_driver.testers import GenericAnyTester
from .exceptions import NoSuchModuleError, NoSuchPortError, NotSupportMedia, NotSupportPortSpeed
from itertools import chain

PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


# region Testers
async def reserve_tester(tester: GenericAnyTester, force: bool = True) -> None:
    """Reserve a tester regardless whether it is owned by others or not.

    :param tester: The tester to reserve
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :param force: Should force reserve the tester
    :type force: boolean
    :return:
    :rtype: None
    """
    r = await tester.reservation.get()
    if force and r.operation == enums.ReservedStatus.RESERVED_BY_OTHER:
        await asyncio.gather(*[free_module(m) for m in tester.modules])
        await tester.reservation.set_reserve()
    elif r.operation == enums.ReservedStatus.RELEASED:
        # can fail in condition if an module or port is reserved by someone else
        await tester.reservation.set_reserve()


async def free_tester(tester: GenericAnyTester) -> None:
    """Free a tester. If the tester is reserved by you, release the tester. If the tester is reserved by others, relinquish the tester. The tester should have no owner afterwards.

    :param tester: The tester to free
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :return:
    :rtype: None
    """
    r = await tester.reservation.get()
    if r.operation == enums.ReservedStatus.RESERVED_BY_OTHER:
        await tester.reservation.set_relinquish()
    elif r.operation == enums.ReservedStatus.RESERVED_BY_YOU:
        await tester.reservation.set_release()
    await asyncio.gather(*[free_module(m) for m in tester.modules])


# endregion


# region Modules


def get_module(tester: GenericAnyTester, module_id: int) -> GenericAnyModule:
    """Get a module object of the tester.

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :param module_id: the index id of the module
    :type module_id: int
    :raises NoSuchModuleError: No such a module index on the tester
    :return: module object
    :rtype: :class:`~xoa_driver.modules.GenericAnyModule`
    """
    try:
        return tester.modules.obtain(module_id)
    except KeyError:
        raise NoSuchModuleError(module_id)


def get_modules(tester: GenericAnyTester) -> tuple[GenericAnyModule, ...]:
    """Get all modules of the tester

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :return: List of module objects
    :rtype: tuple[GenericAnyModule]
    """
    return tuple(tester.modules)


async def reserve_module(module: GenericAnyModule, force: bool = True) -> None:
    """Reserve a module regardless whether it is owned by others or not.

    :param module: The module to reserve
    :type module: :class:`~xoa_driver.modules.GenericAnyModule`
    :param force: Should force reserve the module, defaults to True
    :type force: boolean
    :return:
    :rtype: None
    """
    r = await module.reservation.get()
    if force and r.operation == enums.ReservedStatus.RESERVED_BY_OTHER:
        await free_module(module)
        await module.reservation.set_reserve()
    elif r.operation == enums.ReservedStatus.RELEASED:
        # will fail in condition coz module can be released but port can be occupied by some one else
        await module.reservation.set_reserve()


async def free_module(module: GenericAnyModule) -> None:
    """Free a module. If the module is reserved by you, release the module. If the module is reserved by others, relinquish the module. The module should have no owner afterwards.

    :param module: The module to free
    :type module: :class:`~xoa_driver.modules.GenericAnyModule`
    :return:
    :rtype: None
    """
    r = await module.reservation.get()
    if r.operation == enums.ReservedStatus.RESERVED_BY_OTHER:
        await module.reservation.set_relinquish()
    elif r.operation == enums.ReservedStatus.RESERVED_BY_YOU:
        await module.reservation.set_release()
    await free_ports(*module.ports)


async def get_module_supported_media(module: t.Union[GenericL23Module, ModuleChimera]) -> t.List[dict[str, t.Any]|None]:
    """Get a list of supported media, port speed and count of the module.

    :param module: The module object
    :type module: GenericAnyModule
    :return: List of supported media, port speed and count
    :rtype: t.Union[t.List[t.Dict[str, t.Any]], None]
    """
    supported_media_list = []
    reply = await module.available_speeds.get()
    info_list = reply.media_info_list
    while len(info_list) > 0:
        # print(f"Media: {list[0]}")
        x = {"media": enums.MediaConfigurationType(info_list[0]), "speeds": []}
        sub_list = info_list[2:(2*info_list[1]+2)]
        while len(sub_list) > 0:
            # print(f"       {sub_list[0:2]}")
            x["speeds"].append((sub_list[0], sub_list[1]))
            sub_list = sub_list[2:]
        supported_media_list.append(x)
        info_list = info_list[2*info_list[1]+2:]
    return supported_media_list



async def set_module_media_config(module: t.Union[GenericL23Module, ModuleChimera], media: enums.MediaConfigurationType, force: bool = True) -> None:
    """Set module's media configuration.

    :param module: The module object
    :type module: GenericAnyModule
    :param media: Target media for the module
    :type media: enums.MediaConfigurationType
    :param force: Should reserve the module by force, defaults to True
    :type force: bool, optional
    :raises NotSupportMedia: The module does not support this media type
    :return: 
    :rtype: 
    """
    
    # reserve the module first
    await reserve_module(module, force)

    # get the supported media
    supported_media_list = await get_module_supported_media(module)

    # set the module media if the target media is found in supported media
    for item in supported_media_list:
        if item is not None:
            if item["media"] == media:
                await module.media.set(media_config = media)
                return None

    # raise exception is the target media is not found in the supported media
    raise NotSupportMedia(module)




async def set_module_port_config(module: t.Union[GenericL23Module, ModuleChimera], port_count: int, port_speed: int, force: bool = True) -> None:
    """Set module's port-speed configuration

    :param module: The module object
    :type module: t.Union[GenericL23Module, ModuleChimera]
    :param port_count: The port count
    :type port_count: int
    :param port_speed: The port speed in Mbps, e.g. 40000 for 40G
    :type port_speed: int
    :param force: Should reserve the module by force, defaults to True
    :type force: bool, optional
    :raises NotSupportPortSpeed: The module does not support the port-speed configuration under its current media configuration
    :return: 
    :rtype: 
    """
    
    # reserve the module first
    await reserve_module(module, force)

    # get the supported media by the module
    supported_media_list = await get_module_supported_media(module)

    # get the current media of the module
    reply = await module.media.get()
    current_media = reply.media_config

    # set the module port speed if we can find the port-speed in the corresponding media
    for item in supported_media_list:
        if item is not None:
            if item["media"] == enums.MediaConfigurationType(current_media):
                if (port_count, port_speed) in item["speeds"]:
                    portspeed_list = [port_count] + port_count*[port_speed]
                    await module.cfp.config.set(portspeed_list=portspeed_list)
                    return None
    raise NotSupportPortSpeed(module)





    


# endregion

# region Ports


def get_all_ports(tester: GenericAnyTester) -> tuple[GenericAnyPort, ...]:
    """Get all ports of the tester

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :return: List of port objects
    :rtype: tuple[GenericAnyPort]
    """
    all_ports_ = (m.ports for m in get_modules(tester))
    return tuple(chain.from_iterable(all_ports_))


def get_ports(tester: GenericAnyTester, module_id: int) -> tuple[GenericAnyPort, ...]:
    """Get all ports of the module

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :param module_id: The module index
    :type module_id: int
    :return: List of port objects
    :rtype: tuple[GenericAnyPort]
    """
    module = get_module(tester, module_id)
    return tuple(module.ports)


def get_port(tester: GenericAnyTester, module_id: int, port_id: int) -> GenericAnyPort:
    """Get a port of the module

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :param module_id: The module index
    :type module_id: int
    :param port_id: The port index
    :type port_id: int
    :raises NoSuchPortError: No port found with the index
    :return: The port object
    :rtype: :class:`~xoa_driver.ports.GenericAnyPort`
    """
    module = get_module(tester, module_id)
    try:
        return module.ports.obtain(port_id)
    except KeyError:
        raise NoSuchPortError(port_id)


async def reserve_port(port: GenericAnyPort, force: bool = True) -> None:
    """Reserve a port regardless whether it is owned by others or not.

    :param port: The port to reserve
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param force: Should force reserve the port
    :type force: boolean
    :return:
    :rtype: None
    """
    r = await port.reservation.get()
    if force and r.status == enums.ReservedStatus.RESERVED_BY_OTHER:
        await apply(
            port.reservation.set_relinquish(),
            port.reservation.set_reserve(),
        )
    elif r.status == enums.ReservedStatus.RELEASED:
        await port.reservation.set_reserve()


async def reset_port(port: GenericAnyPort) -> None:
    """Reserve and reset a port

    :param port: The port to reset
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return:
    :rtype: None
    """
    await reserve_port(port, False)
    await port.reset.set()


async def free_port(port: GenericAnyPort) -> None:
    """Free a port. If the port is reserved by you, release the port. If the port is reserved by others, relinquish the port. The port should have no owner afterwards.

    :param port: The port to free
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return:
    :rtype: None
    """
    r = await port.reservation.get()
    if r.status == enums.ReservedStatus.RESERVED_BY_OTHER:
        await port.reservation.set_relinquish()
    elif r.status == enums.ReservedStatus.RESERVED_BY_YOU:
        await port.reservation.set_release()


async def free_ports(*ports: GenericAnyPort) -> None:
    """Free all ports on a module.

    :param module: The module object
    :type module: GenericAnyModule
    """
    await asyncio.gather(*[free_port(port=p) for p in ports])


# endregion


__all__ = (
    "free_module",
    "free_port",
    "free_ports",
    "free_tester",
    "get_module",
    "get_port",
    "get_ports",
    "reset_port",
    "reserve_module",
    "reserve_port",
    "reserve_tester",
)
