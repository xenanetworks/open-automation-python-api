#: All avaliable tester types.

from .internals.testers.l23_tester import L23Tester
from .internals.testers.l47_tester import L47Tester
from .internals.testers.l47ve_tester import L47VeTester

import typing

GenericAnyTester = typing.Union[
    "L23Tester",
    "L47Tester",
    "L47VeTester",
]


__all__ = (
    "L23Tester",
    "L47Tester",
    "L47VeTester",
    "GenericAnyTester",
)