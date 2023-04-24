import sys


if "xoa_driver.internals.hli_v1" in sys.modules:
    raise ImportError("\33[101mUsing xoa_driver and xoa_driver.v2 at the same time is not allowed.\33[0m")

from xoa_driver.internals import warn

warn.resource(
    "xoa_driver.v2 is under development and it subject to changes without notice.",
)
