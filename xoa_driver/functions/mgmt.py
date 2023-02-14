from __future__ import annotations
import asyncio
from xoa_driver.enums import ReservedStatus
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v2.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v2.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.modules import GenericAnyModule
from xoa_driver.testers import GenericAnyTester
from .exceptions import NoSuchModuleError, NoSuchPortError

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
    if force and r.operation == ReservedStatus.RESERVED_BY_OTHER:
        await asyncio.gather(*[free_module(m) for m in tester.modules])
        await tester.reservation.set_reserve()
    elif r.operation == ReservedStatus.RELEASED:
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
    if r.operation == ReservedStatus.RESERVED_BY_OTHER:
        await tester.reservation.set_relinquish()
    elif r.operation == ReservedStatus.RESERVED_BY_YOU:
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
    :param force: Should force reserve the module
    :type force: boolean
    :return:
    :rtype: None
    """
    r = await module.reservation.get()
    if force and r.operation == ReservedStatus.RESERVED_BY_OTHER:
        await free_module(module)
        await module.reservation.set_reserve()
    elif r.operation == ReservedStatus.RELEASED:
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
    if r.operation == ReservedStatus.RESERVED_BY_OTHER:
        await module.reservation.set_relinquish()
    elif r.operation == ReservedStatus.RESERVED_BY_YOU:
        await module.reservation.set_release()
    await free_ports(*module.ports)


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
    if force and r.status == ReservedStatus.RESERVED_BY_OTHER:
        await apply(
            port.reservation.set_relinquish(),
            port.reservation.set_reserve(),
        )
    elif r.status == ReservedStatus.RELEASED:
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
    if r.status == ReservedStatus.RESERVED_BY_OTHER:
        await port.reservation.set_relinquish()
    elif r.status == ReservedStatus.RESERVED_BY_YOU:
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
