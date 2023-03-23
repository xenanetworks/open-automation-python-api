import warnings

warnings.simplefilter('always', ResourceWarning)
warnings.formatwarning = lambda message, category, filename, lineno, *_: f"\n\33[103m{category.__name__}\33[0m: {message}\n\n"
warnings.warn("xoa_driver.v2 is under development and it subject to changes without notice.", ResourceWarning)
