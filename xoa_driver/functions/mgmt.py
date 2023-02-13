from __future__ import annotations
import asyncio
from xoa_driver.enums import ReservedStatus
from xoa_driver.misc import Token
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v2.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v2.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.modules import GenericAnyModule
from xoa_driver.testers import GenericAnyTester
from xoa_driver.lli import commands

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

def get_module(tester: GenericAnyTester, module_id: int):
    try:
        return tester.modules.obtain(module_id)
    except KeyError:
        raise NoSuchModuleError(module_id)


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


def get_ports(tester: GenericAnyTester, module_id: int) -> tuple[GenericAnyPort]:
    """_summary_

    :param tester: _description_
    :type tester: GenericAnyTester
    :param module_id: _description_
    :type module_id: int
    :param port_id: _description_
    :type port_id: int
    :raises NotConnectedError: _description_
    :raises NoSuchModuleError: _description_
    :raises NoSuchModuleError: _description_
    :return: _description_
    :rtype: GenericAnyPort
    """
    module = get_module(tester, module_id)
    return tuple(module.ports)


def get_port(tester: GenericAnyTester, module_id: int, port_id: int) -> GenericAnyPort:
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
