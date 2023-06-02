from typing import NoReturn, TypeVar
from xoa_driver.internals.commands.enums import FilterType

T = TypeVar("T")


def prevent_set(inst: T, filter_type: FilterType = FilterType.WORKING) -> T:
    METHOD_NAME = "set"

    def _set(*args, **kwargs) -> NoReturn:
        raise Exception(f"Method {METHOD_NAME} is not allowed")

    if filter_type is FilterType.WORKING and hasattr(inst, METHOD_NAME):
        setattr(inst, METHOD_NAME, _set)
    return inst
