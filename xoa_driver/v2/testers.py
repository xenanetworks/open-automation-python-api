#: All available tester types.

from xoa_driver.internals.hli_v2.testers.l23_tester import L23Tester
from xoa_driver.internals.hli_v2.testers.l23ve_tester import L23VeTester
from xoa_driver.internals.hli_v2.testers.l47_tester import L47Tester
from xoa_driver.internals.hli_v2.testers.l47ve_tester import L47VeTester

import typing

GenericAnyTester = typing.Union[
    "L23Tester",
    "L23VeTester",
    "L47Tester",
    "L47VeTester",
]


__all__ = (
    "L23Tester",
    "L23VeTester",
    "L47Tester",
    "L47VeTester",
    "GenericAnyTester",
)
