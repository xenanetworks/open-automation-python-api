import sys
print(sys.modules.get("xoa_driver.internals.hli_v1"))
if "xoa_driver.internals.hli_v1" in sys.modules:
    raise ImportError("\33[31mOnly Single interface version is allowed to being use at the same time.\33[0m")
