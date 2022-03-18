import ctypes as c
import struct
from typing import (
    List,
    Optional,
    get_args, # py3.8 >
) 
from . import constants as const
from . import utils
from .struct_header import ResponseHeader
from .fields.data_types import (
    XmpDefaultList,
    XmpStr,
)

class NotEnoughBytesLeft(RuntimeError):
    def __init__(self, cmd_name: str, back, curent_field_name: str) -> None:
        self.cmd_name = cmd_name
        all_fields = list(back.__annotations__.keys())
        self.fields = all_fields[all_fields.index(curent_field_name):]
        self.msg = f"When parsing {self.cmd_name}, there are still fields {self.fields} to be parsed while there is no more bytes!"
        super().__init__(self.msg)

class Response:
    """
    Response serializer
    """
    __slots__ = ("class_name", "header", "raw_data", "__cursor", "index_values", "values",)
    def __init__(self, header: ResponseHeader, class_name: str, data: bytes, back: Optional[type]) -> None:
        self.class_name = class_name
        self.header = header
        self.raw_data = data
        self.__cursor = 0
        self.index_values = self.__parse_indices()
        self.values = None
        if self.header.cmd_type == const.CommandType.COMMAND_VALUE:
            self.values = self.__parse_values(back)
        # elif self.header.cmd_type == CommandType.COMMAND_STATUS:

        del self.__cursor


    def __str__(self) -> str:
        return utils.format_str(
            self,  
            b_str=bytes(self.header) + self.raw_data # type: ignore
        )

    def __repr__(self) -> str:
        return utils.format_repr(self)

    @property
    def command_status(self) -> Optional[const.CommandStatus]:
        if self.header.cmd_type == const.CommandType.COMMAND_STATUS:
            return const.CommandStatus(self.header.cmd_code)
        return None

    def __parse_indices(self) -> List[int]:
        format = f"!{self.header.number_of_indices}I"
        indices = struct.unpack_from(format, self.raw_data, 0 )
        self.__cursor += struct.calcsize(format)
        return list(indices)

    def __parse_values(self, back: Optional[type]):
        if not back: return None
        dic = {}
        for field_name, field_type in back.__annotations__.items():
            generic_type = get_args(field_type)[0]
            if generic_type == XmpStr:
                # NOTICE: Here can be issue if we having a command with string and list at the same time
                dic[field_name] = self.__parse_xmp_str(self.__calc_str_len(back))
            else:
                length = self.__calc_xmp_type_length(generic_type)
                value_bytes = self.raw_data[self.__cursor : self.__cursor + length]
                if (not issubclass(generic_type, XmpDefaultList)) and not value_bytes:
                    raise NotEnoughBytesLeft(self.class_name, back, field_name)
                dic[field_name] = generic_type.from_bytes(value_bytes)
                self.__cursor += length
        return back(**dic)

    def __calc_xmp_type_length(self, generic_type) -> int:
        if not issubclass(generic_type, XmpDefaultList):
            return int(generic_type.size)
        else:
            if generic_type.fix_length:
                return int(generic_type.fix_length * generic_type.element_type.size)
            elif generic_type.stop_to_keep:
                # weird parsing with helper types
                return int(self.header.number_of_value_bytes - generic_type.stop_to_keep)
            return int(self.header.number_of_value_bytes)

    def __calc_str_len(self, back) -> int:
        types_aligned = [ 
            get_args(field_type)[0] 
            for field_type in back.__annotations__.values() 
        ]
        sum_of_fixed_sizes = sum( 
            int(generic_type.size) 
            for generic_type in types_aligned 
        )
        return self.header.body_size - sum_of_fixed_sizes

    def __parse_xmp_str(self, string_lenght: int) -> bytes:
        raw_data: bytes = self.raw_data[self.__cursor:]
        zero: bytes = b"\x00"
        nvb: int = self.header.number_of_value_bytes
        if zero in raw_data:
            zero_index = raw_data.index(zero)
            length = zero_index if zero_index + self.__cursor <= nvb else nvb
        else:
            length = nvb
        self.__cursor += string_lenght
        return raw_data[:length]

    @property
    def is_ok(self) -> bool:
        return self.get_return_ok() or self.set_return_ok()

    def set_return_ok(self) -> bool:
        return all(
            {
                self.header.cmd_type == const.CommandType.COMMAND_STATUS,
                self.header.cmd_code == const.CommandStatus.OK,
            }
        )

    def get_return_ok(self) -> bool:
        return (
            self.header.cmd_type == const.CommandType.COMMAND_VALUE
            and self.values is not None
        )
