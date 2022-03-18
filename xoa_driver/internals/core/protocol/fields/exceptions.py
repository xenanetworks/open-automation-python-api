from typing import (
    Union, 
    Any,
    Type,
    Iterable,
    Tuple,
    List
)

# region Converter Errors

class PaddingOddError(ValueError):
    def __init__(self, value: int) -> None:
        self.value = value
        self.msg = f"Parameter <'{self.value!r}'> must be an even number!"
        super().__init__(self.msg)


class PaddingToShortError(ValueError):
    def __init__(self, value: int, hex_string: str) -> None:
        self.value = value
        self.hex_string = hex_string
        self.msg = f"Parameter <'{self.value!r}'> is smaller than length of '{self.hex_string}' !"
        super().__init__(self.msg)


# endregion

# region DataTypes

class ExpectingBytesError(ValueError):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.msg = f"Expected {self.value!r} to be an string of bytes."
        super().__init__(self.msg)


class NumberRangeError(ValueError):
    def __init__(self, value: int, max_val: int, min_val: int = 0) -> None:
        self.value = value
        self.min_val = min_val
        self.max_val = max_val
        self.msg = f"Expected({self.value!r}) to be not bigger than {self.max_val} and not smaller than {self.min_val}."
        super().__init__(self.msg)


class HexRangeError(ValueError):
    def __init__(self,  value: str, max_val: int, min_val: int = 0) -> None:
        self.value = value
        self.min_val = min_val
        self.max_val = max_val
        self.msg = f"Expected {value!r} to be not bigger than {max_val} and not smaller than {self.min_val}."
        super().__init__(self.msg)


class InvalidMacAddressError(ValueError):
    def __init__(self, value: Union[int, str]) -> None:
        self.value = value
        self.msg = f"Invalid mac address {self.value!r}!"
        super().__init__(self.msg)


class StartWithError(ValueError):
    def __init__(self, value: str,  *variations) -> None:
        self.value = value
        self.msg = f"Expected {self.value!r} to start with { ' or '.join(variations) }."
        super().__init__(self.msg)


class NotAllowedTypeError(TypeError):
    def __init__(self, value: Any, allowed_types: Iterable[Type]) -> None:
        self.value = value
        self.allowed_types = allowed_types
        self.msg = f"the type of <{type(self.value)} {self.value}> is not in allowed types { ' or '.join(allowed_types) }."
        super().__init__(self.msg)


class FixedLenghtError(ValueError):
    def __init__(self, value: Any,  fix_length: int) -> None:
        self.value = value
        self.fix_length = fix_length
        self.msg = f"Data {self.value} failed to follow the specified fixed length {self.fix_length}."
        super().__init__(self.msg)
        
        
class ElementTypeError(NotImplementedError):
    def __init__(self, class_name: str) -> None:
        self.class_name = class_name
        self.msg = f"Ups, someone forgot to set a correct value for: <element_type> in <class {self.class_name}>"
        super().__init__(self.msg)

# endregion

# region Fields Errors

class ValueOutOfRangeError(ValueError):
    def __init__(self, value: Union[int, float, List[int], List[float]], climb: Tuple[Union[int, float], Union[int, float]]) -> None:
        self.value = value
        self.climb = climb
        self.msg = f"Expect value: <{value}> to be in range of {climb}!"
        super().__init__(self.msg)

# endregion