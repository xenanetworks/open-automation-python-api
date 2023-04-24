import warnings
from functools import partial

__all__ = (
    "depricated",
    "resource"
)


class XoaResourceWarning(ResourceWarning):
    ...


class XoaDeprecationWarning(DeprecationWarning):
    ...


warnings.simplefilter('always', XoaResourceWarning)
warnings.simplefilter('always', XoaDeprecationWarning)


def formatter(message, category, filename, lineno, *_) -> str:
    if category is XoaDeprecationWarning:
        return f"\n\33[101m{category.__name__}\33[0m: {message}\n\n"
    return f"\n\33[103m{category.__name__}\33[0m: {message}\n\n"


warnings.formatwarning = formatter


depricated = partial(warnings.warn, category=XoaDeprecationWarning)
resource = partial(warnings.warn, category=XoaResourceWarning)
