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
from xoa_driver.lli import commands
from .module import free_module

from .exceptions import (
    NotConnectedError,
    NoSuchModuleError,
)
PcsPmaSupported = (FamilyL, FamilyL1)
AutoNegSupported = (FamilyL, FamilyL1)
LinkTrainingSupported = FamilyL


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
        if r.status == ReservedStatus.RESERVED_BY_OTHER:
            for m in tester.modules:
                await free_module(m)
            tokens.append(tester.reservation.set_reserve())
        elif r.status == ReservedStatus.RELEASED:
            tokens.append(tester.reservation.set_reserve())
    else:
        if r.status == ReservedStatus.RELEASED:
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
    if r.status == ReservedStatus.RESERVED_BY_OTHER:
        await tester.reservation.set_relinquish()
    elif r.status == ReservedStatus.RESERVED_BY_YOU:
        await tester.reservation.set_release()
    for m in tester.modules:
        await free_module(m)
    return None
