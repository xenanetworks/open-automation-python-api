

import ctypes as c
from . import constants as const

class ProtocolHeader(c.BigEndianStructure):
    __slots__ = (
        "magic_word", 
        "number_of_indices", 
        "number_of_value_bytes", 
        "command_parameter", 
        "module_index", 
        "port_index", 
        "request_identifier"
    )
    _fields_ = [
        ("magic_word", c.c_char * 4),
        ("number_of_indices", c.c_ushort),
        ("number_of_value_bytes", c.c_ushort),
        ("command_parameter", c.c_ushort),
        ("module_index", c.c_ubyte),
        ("port_index", c.c_ubyte),
        ("request_identifier", c.c_uint32),
    ]

    @property
    def cmd_type(self) -> int:
        return (self.command_parameter & 0x0F00) >> 8

    @cmd_type.setter
    def cmd_type(self, val: int) -> None:
        assert 0 <= val < 4
        self.command_parameter |= val << 8

    @property
    def cmd_code(self) -> int:
        last = (self.command_parameter & 0xF000) >> 4
        first = self.command_parameter & 0x00FF
        return first | last

    @cmd_code.setter
    def cmd_code(self, val: int) -> None:
        first = (val & 0x0F00) << 4
        last = val & 0x00FF
        self.command_parameter |= first | last

    @property
    def body_size(self) -> int:
        """Calculate packet body size

        Returns:
            int: Packet body size
        """
        if self.magic_word != const.MAGIC_WORD:
            return 4
        body_size = self.number_of_value_bytes + (self.number_of_indices * 4)
        body_size += (4 - body_size % 4) % 4
        return body_size


class ResponseHeader(ProtocolHeader):
    @property
    def is_pushed(self) -> bool:
        """Check if response is pushed."""
        return self.request_identifier == 0
