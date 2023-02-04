from __future__ import annotations
import asyncio
from typing import Any, Dict, List
from xoa_driver.enums import (
    ReservedStatus,
)
from xoa_driver.misc import Token
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v2.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v2.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.ports import GenericAnyPort
from xoa_driver.modules import GenericAnyModule
from xoa_driver.testers import L23Tester, L47Tester, L23VeTester, L47VeTester, GenericAnyTester
from xoa_driver.lli import commands

from .exceptions import (
    NotConnectedError,
    NoSuchModuleError,
)
PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL

async def connect(
    tester_type: str,
    host: str,
    username: str,
    password: str = "xena",
    port: int = 22606,
) -> GenericAnyTester:
    """Connect to a Xena tester.

    :param tester_type: Tester type, either "l23" or "l47"
    :type tester_type: str
    :param host: IP address or hostname of the tester.
    :type host: str
    :param username: Username used to log on the tester
    :type username: str
    :param password: Password of the tester, defaults to "xena"
    :type password: str, optional
    :param port: the port number for establishing the TCP connection, defaults to 22606
    :type port: int, optional
    :return: tester object
    :rtype: :class:`~xoa_driver.testers.GenericAnyTester`
    """
    assert tester_type in ("l23", "l47"), "Para 'tester_type' not in ('l23', 'l47', 'l23ve', 'l47ve')!"
    class_ = {"l23": L23Tester, "l47": L47Tester, "l23ve": L23VeTester, "l47ve": L47VeTester}[tester_type]
    current_tester = await class_(host, username, password, port, debug=True)
    return current_tester


def get_port(
    tester: GenericAnyTester,
    module_id: int,
    port_id: int,
) -> GenericAnyPort:
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
    if tester is None:
        raise NotConnectedError()
    try:
        module = tester.modules.obtain(module_id)
    except KeyError:
        raise NoSuchModuleError(module_id)
    try:
        port = module.ports.obtain(port_id)
    except KeyError:
        raise NoSuchModuleError(port_id)
    return port


def get_ports(
    tester: GenericAnyTester,
    module_id: int,
) -> list[GenericAnyPort]:
    """Get all port objects on a module

    :param tester: The tester object
    :type tester: GenericAnyTester
    :param module_id: module index
    :type module_id: int
    :raises NotConnectedError: _description_
    :raises NoSuchModuleError: _description_
    :return: _description_
    :rtype: list[GenericAnyPort]
    """
    if tester is None:
        raise NotConnectedError()
    try:
        module = tester.modules.obtain(module_id)
    except KeyError:
        raise NoSuchModuleError(module_id)
    return list(module.ports)


async def reserve_port(port: GenericAnyPort, force: bool = True) -> None:
    """Reserve a port regardless whether it is owned by others or not.

    :param port: The port to reserve
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :param force: Should force reserve the port
    :type force: boolean
    :return:
    :rtype: None
    """
    tokens = []
    r = await port.reservation.get()
    if force:
        if r.status == ReservedStatus.RESERVED_BY_OTHER:
            tokens.append(port.reservation.set_relinquish())
            tokens.append(port.reservation.set_reserve())
        elif r.status == ReservedStatus.RELEASED:
            tokens.append(port.reservation.set_reserve())
    else:
        if r.status == ReservedStatus.RELEASED:
            tokens.append(port.reservation.set_reserve())
    await apply(*tokens)
    return None


async def reset_port(port: GenericAnyPort) -> None:
    """Reserve and reset a port

    :param port: The port to reset
    :type port: :class:`~xoa_driver.ports.GenericAnyPort`
    :return:
    :rtype: None
    """
    await reserve_port(port)
    await port.reset.set()
    return None


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
    return None


async def free_ports(module: GenericAnyModule) -> None:
    """Free all ports on a module.

    :param module: The module object
    :type module: GenericAnyModule
    """
    await asyncio.gather(*[free_port(port=p) for p in module.ports])


async def reserve_module(module: GenericAnyModule, force: bool = True) -> None:
    """Reserve a module regardless whether it is owned by others or not.

    :param module: The module to reserve
    :type module: :class:`~xoa_driver.modules.GenericAnyModule`
    :param force: Should force reserve the module
    :type force: boolean
    :return:
    :rtype: None
    """
    tokens = []
    r = await module.reservation.get()
    if force:
        await free_ports(module)
        if r.operation == ReservedStatus.RESERVED_BY_OTHER:
            tokens.append(module.reservation.set_reserve())
        elif r.operation == ReservedStatus.RELEASED:
            tokens.append(module.reservation.set_reserve())
    else:
        if r.operation == ReservedStatus.RELEASED:
            tokens.append(module.reservation.set_reserve())
    await apply(*tokens)
    return None


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
    await asyncio.gather(*[free_port(port=p) for p in module.ports])
    return None


async def reserve_tester(tester: GenericAnyTester, force: bool = True) -> None:
    """Reserve a tester regardless whether it is owned by others or not.

    :param tester: The tester to reserve
    :type tester: :class:`~xoa_driver.testers.GenericAnyTester`
    :param force: Should force reserve the tester
    :type force: boolean
    :return:
    :rtype: None
    """
    tokens = []
    r = await tester.reservation.get()
    if force:
        if r.operation == ReservedStatus.RESERVED_BY_OTHER:
            for m in tester.modules:
                await free_module(m)
            tokens.append(tester.reservation.set_reserve())
        elif r.operation == ReservedStatus.RELEASED:
            tokens.append(tester.reservation.set_reserve())
    else:
        if r.operation == ReservedStatus.RELEASED:
            tokens.append(tester.reservation.set_reserve())
    await apply(*tokens)
    return None


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
    for m in tester.modules:
        await free_module(m)
    return None

