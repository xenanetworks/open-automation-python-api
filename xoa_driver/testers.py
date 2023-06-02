#: All available tester types.
import sys

if "xoa_driver.v2" in sys.modules:
    raise ImportError("\33[31mOnly Single interface version is allowed to being use at the same time.\33[0m")

from .internals.hli_v1.testers.l23_tester import L23Tester
from .internals.hli_v1.testers.l23ve_tester import L23VeTester
from .internals.hli_v1.testers.l47_tester import L47Tester
from .internals.hli_v1.testers.l47ve_tester import L47VeTester

import typing as t

GenericAnyTester = t.Union[
    "L23Tester",
    "L23VeTester",
    "L47Tester",
    "L47VeTester",
]
GenericAnyGenuineTester = t.Union[
    "L23Tester",
    "L47Tester",
]
GenericAnyVirtualTester = t.Union[
    "L23VeTester",
    "L47VeTester",
]

__all__ = (
    "L23Tester",
    "L23VeTester",
    "L47Tester",
    "L47VeTester",
    "GenericAnyTester",
    "GenericAnyGenuineTester",
    "GenericAnyVirtualTester",
)
