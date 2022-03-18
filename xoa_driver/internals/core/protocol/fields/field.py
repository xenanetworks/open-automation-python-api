from enum import IntEnum
from typing import (
    Any,
    Generic,
    List,
    Tuple,
    Optional,
    Type,
    Union,
    NamedTuple,
)
from collections import UserList
from . import exceptions as excp
from . import interfaces as itf



def patch_type(base_type: Type, choices: Type["IntEnum"], bit_map: List[str]) -> Type:
    """Function dynamically patch XTypes for show meaningful choices value"""
    def _choice_str(self) -> str:
        c_format = lambda cho, itm : f"{cho.__name__}.{cho(int(itm)).name}"
        if issubclass(base_type, UserList):
            return str([c_format(choices, i) for i in self])
        return c_format(choices, self)

    # def _bit_map_str(self) -> str:
    #     results = []
    #     for e in self:
    #         one_result = [b for i, b in enumerate(bit_map) if e & (1 << i)]
    #         results.append(one_result)
    #     return str(results)

    dic = {}
    if choices:
        dic["__str__"] = _choice_str
        dic["__repr__"] = _choice_str
    # elif bit_map: # need to improve logic this part will not work coz function will be colled only if <choices> are defined
    #     dic["__str__"] = _bit_map_str 
    #     dic["__repr__"] = _bit_map_str
    return type(base_type.__name__, (base_type,), dic)


class ClimbRange(NamedTuple):
    min: Union[int, float]
    max: Union[int, float]

class XmpField(Generic[itf.XmpGenericField]):
    """
    Xmp Field descriptor for command structures.
    Taking care of all passed values to the Packet structure will be
    in correct convertable type for Xena Management Protocol.
    """

    def __init__(
        self, 
        xmp_type: Type[itf.XmpGenericField], 
        *_, 
        choices: Optional[Type["IntEnum"]] = None, 
        climb: Optional[Tuple[Union[int, float], Union[int, float]]] = None,
    ) -> None:
        self.xmp_type = xmp_type
        
        self.choices: Optional[Type["IntEnum"]] = None
        self.climb: Optional[ClimbRange] = None
        self.bit_map: List[str] = []
        
        is_numerical = issubclass(self.xmp_type, (int, float))
        
        if is_numerical or issubclass(self.xmp_type, UserList):
            if choices:
                self.choices = choices
                self.xmp_type = patch_type(
                    self.xmp_type, 
                    self.choices, 
                    self.bit_map
                )
        if is_numerical:
            self.climb = ClimbRange(*climb) if climb else None

    def __validate_choices(self, val: "itf.XmpGenericField") -> None:
        if not self.choices:
            return None
        elif isinstance(val, UserList):
            [ self.choices(v) for v in val ]
        else:
            self.choices(val)  # raise an exception if value is not in provided enum
    
    def __validate_limits(self, val: Union[int, float]) -> None:
        if not self.climb:
            return None
        elif not (self.climb.min <= val <= self.climb.max):
            raise excp.ValueOutOfRangeError(val, self.climb)

    def __set_name__(self, owner: object, name: str) -> None:
        self._private_name = name

    def __set__(self, obj: object, value: Any) -> None:
        val = (
            self.xmp_type.from_bytes(value) 
            if isinstance(value, bytes) 
            else self.xmp_type(value)
        )
        
        self.__validate_choices(val) # type: ignore
        self.__validate_limits(val) # type: ignore
        obj.__dict__[self._private_name] = val

    def __get__(self, obj: object, objtype: Any = None) -> "itf.XmpGenericField":
        return obj.__dict__[self._private_name]


# class StateStringType:
#     @staticmethod
#     def validate(inst, val) -> None:
#         return None

# class StateNumericalType:
#     @staticmethod
#     def _validate_choices(inst, val) -> None:
#         if not inst.choices:
#             return None
#         inst.choices(val)  # raise an exception if value is not in provided enum

#     @staticmethod
#     def _validate_limits(inst, val: Union[int, float]) -> None:
#         if not inst.climb:
#             return None
#         elif not (inst.climb.min <= val <= inst.climb.max):
#             raise excp.ValueOutOfRangeError(val, inst.climb)

#     @staticmethod
#     def validate(inst, val) -> None:
#         StateNumericalType._validate_choices(inst, val)
#         StateNumericalType._validate_limits(inst, val)
        

# class StateIterableNumericalType:
#     @staticmethod
#     def _validate_choices(inst, val) -> None:
#         if not inst.choices:
#             return None
#         [ inst.choices(v) for v in val ]
    
#     @staticmethod
#     def _validate_limits(inst, val: Union[List[int], List[float]]) -> None:
#         if not inst.climb:
#             return None
#         elif any((inst.climb.min > v > inst.climb.max) for v in val):
#             raise excp.ValueOutOfRangeError(val, inst.climb)

#     @staticmethod
#     def validate(inst, val) -> None:
#         StateIterableNumericalType._validate_choices(inst, val)
#         StateIterableNumericalType._validate_limits(inst, val)