from typing import TypeVar
from xoa_driver.internals.core.commands.enums import FilterType

T = TypeVar("T")

def prevent_set(inst: T, filter_type: FilterType = FilterType.WORKING) -> T:
    METHOD_NAME = "set"
    def _set(*args, **kwargs): raise Exception(f"Method {METHOD_NAME} is not allowed")
    if filter_type is FilterType.WORKING and hasattr(inst, METHOD_NAME):
        setattr(inst, METHOD_NAME, _set)
    return inst