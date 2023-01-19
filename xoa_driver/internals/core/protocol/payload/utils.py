from __future__ import annotations
import sys
from functools import partial
from typing import (
    Dict,
    ForwardRef,
    Iterable,
    Type,
    Any,
    Optional,
    _eval_type,  # type: ignore
)


def resolve_annotations(raw_annotations: dict[str, Type[Any]], module_name: str | None) -> dict[str, Type[Any]]:
    """
    Partially taken from typing.get_type_hints.

    Resolve string or ForwardRef annotations into type objects if possible.
    """
    base_globals: Optional[Dict[str, Any]] = None
    if module_name:
        if module := sys.modules.get(module_name, None):
            base_globals = module.__dict__

    validate_version = (3, 10) > sys.version_info >= (3, 9, 8) or sys.version_info >= (3, 10, 1)
    forward_ref = (
        partial(ForwardRef, is_argument=False, is_class=True)
        if validate_version else
        partial(ForwardRef, is_argument=False)
    )

    annotations = {}
    for name, value in raw_annotations.items():
        val_ = forward_ref(value) if isinstance(value, str) else value
        try:
            val_ = _eval_type(val_, base_globals, None)
        except NameError:
            pass
        except TypeError:
            if sys.version_info < (3, 9):
                version_str = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
                raise TypeError(f"The Python version you using is: {version_str} and it's supports type hints only from <typing> module") from None
        annotations[name] = val_
    return annotations


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
