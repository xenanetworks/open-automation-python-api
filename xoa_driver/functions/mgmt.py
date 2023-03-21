from __future__ import annotations
import asyncio
import typing as t
from xoa_driver import enums, testers
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v2.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v2.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.modules import GenericAnyModule, GenericL23Module, ModuleChimera
from xoa_driver.testers import GenericAnyTester
from .exceptions import (
    NoSuchModuleError,
    NoSuchPortError,
    NotSupportMedia,
    NotSupportPortSpeed,
)
from .tools import module_eol_info
from itertools import chain
from datetime import datetime

PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


# region Testers
async def reserve_tester(tester: GenericAnyTester, force: bool = True) -> None:
    """
    .. versionadded:: 1.1
    
    Reserve a tester regardless whether it is owned by others or not.

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
    """
    .. versionadded:: 1.1
    
    Free a tester. If the tester is reserved by you, release the tester. If the tester is reserved by others, relinquish the tester. The tester should have no owner afterwards.

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


def get_testers(hosts: t.List[str], username: str) -> t.List["testers.GenericAnyTester"]:
    """
    .. versionadded:: 1.3

    Get tester objects from their host addresses

    :return: List of tester objects
    :rtype: List["testers.GenericAnyTester"]
    """
    return [ testers.L23Tester(host, username) for host in hosts ]

# endregion


# region Modules


def get_module(tester: GenericAnyTester, module_id: int) -> GenericAnyModule:
    """
    .. versionadded:: 1.1
    
    Get a module object of the tester.

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
    """
    .. versionadded:: 1.1
    
    Get all modules of the tester

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :return: List of module objects
    :rtype: tuple[GenericAnyModule]
    """
    return tuple(tester.modules)


async def reserve_module(module: GenericAnyModule, force: bool = True) -> None:
    """
    .. versionadded:: 1.1
    
    Reserve a module regardless whether it is owned by others or not.

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


async def free_module(module: GenericAnyModule, should_free_ports: bool = False) -> None:
    """
    .. versionadded:: 1.2
    
    Free a module. If the module is reserved by you, release the module. If the module is reserved by others, relinquish the module. The module should have no owner afterwards.

    :param module: The module to free
    :type module: :class:`~xoa_driver.modules.GenericAnyModule`
    :param should_free_ports: _description_, defaults to False
    :type should_free_ports: bool, optional
    :return:
    :rtype: None
    """
    r = await module.reservation.get()
    if r.operation == enums.ReservedStatus.RESERVED_BY_OTHER:
        await module.reservation.set_relinquish()
    elif r.operation == enums.ReservedStatus.RESERVED_BY_YOU:
        await module.reservation.set_release()
    if should_free_ports:
        await free_ports(*module.ports)


async def get_module_supported_media(
    module: GenericL23Module | ModuleChimera,
) -> list[dict[str, t.Any]]:
    """    
    .. versionadded:: 1.3

    Get a list of supported media, port speed and count of the module.

    :param module: The module object
    :type module: GenericAnyModule
    :return: List of supported media, port speed and count
    :rtype: list[dict[str, t.Any]]
    """
    supported_media_list = []
    reply = await module.available_speeds.get()
    info_list = reply.media_info_list

    media_type = True
    len_speed = 0
    left = True
    speed = tuple()
    item = {}

    for num in info_list:
        if media_type:
            item = {"media": enums.MediaConfigurationType(num), "speeds": []}
            media_type = False
        elif not len_speed:
            len_speed = num
        elif len_speed and left:
            speed = (num,)
            left = False
        elif len_speed and (not left):
            speed += (num,)
            item["speeds"].append(speed)
            len_speed -= 1
            left = True
            if not len_speed:
                supported_media_list.append(item)
                media_type = True

    return supported_media_list


async def set_module_media_config(
    module: t.Union[GenericL23Module, ModuleChimera],
    media: enums.MediaConfigurationType,
    force: bool = True,
) -> None:
    """
    .. versionadded:: 1.3

    Set module's media configuration.

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
        if item["media"] == media:
            await module.media.set(media_config=media)
            return None

    # raise exception is the target media is not found in the supported media
    raise NotSupportMedia(module)


async def set_module_port_config(
    module: t.Union[GenericL23Module, ModuleChimera],
    port_count: int,
    port_speed: int,
    force: bool = True,
) -> None:
    """
    .. versionadded:: 1.3

    Set module's port-speed configuration

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
        if all(
            (
                item["media"] == enums.MediaConfigurationType(current_media),
                (port_count, port_speed) in item["speeds"],
            )
        ):
            portspeed_list = [port_count] + port_count * [port_speed]
            await module.cfp.config.set(portspeed_list=portspeed_list)
            return None
    raise NotSupportPortSpeed(module)


async def get_module_eol_date(module: GenericAnyModule) -> str:
    """
    .. versionadded:: 1.3

    Get module's End-of-Life date

    :param module: The module object
    :type module: GenericAnyModule
    :return: Module's EOL date
    :rtype: str
    """
    m_eol = module_eol_info()
    resp = await module.serial_number.get()
    for key, value in m_eol.items():
        if str(resp.serial_number)[-2:] == key:
            return value
    return "2999-01-01"


async def get_module_eol_days(module: GenericAnyModule) -> int:
    """
    .. versionadded:: 1.3

    Get days until module's End-of-Life date

    :param module: The module object
    :type module: GenericAnyModule
    :return: days until module's End-of-Life date
    :rtype: int
    """
    date1 = datetime.now()
    date2 = datetime.strptime("2999-01-01", '%Y-%M-%d')
    timedelta = date2 - date1
    m_eol = module_eol_info()
    resp = await module.serial_number.get()
    for key, value in m_eol.items():
        if str(resp.serial_number)[-2:] == key:
            date1 = datetime.now()
            date2 = datetime.strptime(value, '%Y-%M-%d')
            timedelta = date2 - date1
            break
    return timedelta.days

# endregion


# region Ports


def get_all_ports(tester: GenericAnyTester) -> tuple[GenericAnyPort, ...]:
    """
    .. versionadded:: 1.1
    
    Get all ports of the tester

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :return: List of port objects
    :rtype: tuple[GenericAnyPort]
    """
    all_ports_ = (m.ports for m in get_modules(tester))
    return tuple(chain.from_iterable(all_ports_))


def get_ports(tester: GenericAnyTester, module_id: int) -> tuple[GenericAnyPort, ...]:
    """
    .. versionadded:: 1.1
    
    Get all ports of the module

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
    """
    .. versionadded:: 1.1
    
    Get a port of the module

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
    """
    .. versionadded:: 1.1
    
    Reserve a port regardless whether it is owned by others or not.

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
    """
    .. versionadded:: 1.1
    
    Reserve and reset a port

    :param port: The port to reset
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return:
    :rtype: None
    """
    await reserve_port(port, False)
    await port.reset.set()


async def free_port(port: GenericAnyPort) -> None:
    """
    .. versionadded:: 1.1
    
    Free a port. If the port is reserved by you, release the port. If the port is reserved by others, relinquish the port. The port should have no owner afterwards.

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
    """
    .. versionadded:: 1.1
    
    Free all ports on a module.

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
    "get_all_ports",
    "get_module",
    "get_module_eol_date",
    "get_module_eol_days",
    "get_module_supported_media",
    "get_modules",
    "get_port",
    "get_ports",
    "reserve_module",
    "reserve_port",
    "reserve_tester",
    "reset_port",
    "set_module_media_config",
    "set_module_port_config",
    "get_testers"
)
