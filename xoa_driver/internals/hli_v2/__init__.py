import warnings

warnings.formatwarning = lambda message, category, filename, lineno, *_: f"\n\33[33m{category.__name__}\33[0m: {message}\n\n"
warnings.warn("The HLIv2 is under havy development, and api can be changet dramaticly in the future.", ResourceWarning)
