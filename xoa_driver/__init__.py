__version__ = "1.3.0b2"
__short_version__ = "1.3"

import warnings
warnings.simplefilter('always', DeprecationWarning)
warnings.formatwarning = lambda message, category, filename, lineno, *_: f"\n\33[101m{category.__name__}\33[0m: {message}\n\n"
