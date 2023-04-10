import sys
import warnings
print(sys.modules.get("xoa_driver.internals.hli_v1"))
if "xoa_driver.internals.hli_v1" in sys.modules:
    raise ImportError("\33[101mUsing xoa_driver and xoa_driver.v2 at the same time is not allowed.\33[0m")
else:
    warnings.simplefilter('always', ResourceWarning)
    warnings.formatwarning = lambda message, category, filename, lineno, *_: f"\n\33[103m{category.__name__}\33[0m: {message}\n\n"
    warnings.warn("xoa_driver.v2 is under development and it subject to changes without notice.", ResourceWarning)
