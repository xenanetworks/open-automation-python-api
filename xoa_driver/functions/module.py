from __future__ import annotations

from typing import Any, Dict, List
from xoa_driver.enums import (
    ReservedStatus,
)

from xoa_driver.misc import Token
from xoa_driver.utils import apply
from xoa_driver.internals.hli_v2.ports.port_l23.family_l import FamilyL
from xoa_driver.internals.hli_v2.ports.port_l23.family_l1 import FamilyL1
from xoa_driver.testers import GenericAnyTester
from xoa_driver.modules import GenericAnyModule
from xoa_driver.ports import GenericAnyPort
from xoa_driver.lli import commands
from .port import free_port

from .exceptions import (
    NotConnectedError,
    NoSuchModuleError,
)
PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


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
        if r.status == ReservedStatus.RESERVED_BY_OTHER:
            for p in module.ports:
                await free_port(port=p)
            tokens.append(module.reservation.set_reserve())
        elif r.status == ReservedStatus.RELEASED:
            tokens.append(module.reservation.set_reserve())
    else:
        if r.status == ReservedStatus.RELEASED:
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
    if r.status == ReservedStatus.RESERVED_BY_OTHER:
        await module.reservation.set_relinquish()
    elif r.status == ReservedStatus.RESERVED_BY_YOU:
        await module.reservation.set_release()
    for p in module.ports:
        await free_port(port=p)
    return None

def get_ports(
    tester: GenericAnyTester,
    module_id: int,
) -> list[GenericAnyPort]:
    if tester is None:
        raise NotConnectedError()
    try:
        module = tester.modules.obtain(module_id)
    except KeyError:
        raise NoSuchModuleError(module_id)
    ports = []
    for port in module.ports:
        ports.append(port)
    return ports

def get_port(
    tester: GenericAnyTester,
    module_id: int,
    port_id: int,
) -> GenericAnyPort:
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