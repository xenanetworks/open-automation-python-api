from __future__ import annotations

import ctypes as c
from typing import (
    Type,
    ClassVar,
    TypeVar
)
from . import _constants as const


class ProtocolHeader(c.BigEndianStructure):
    """The structure for the header data of a packet in the protocol."""
    __slots__ = (
        "magic_word",
        "number_of_indices",
        "number_of_value_bytes",
        "command_parameter",
        "module_index",
        "port_index",
        "request_identifier",
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
        """Get command type.

        Returns:
            int: Command type
        """
        return (self.command_parameter & 0x0F00) >> 8

    @cmd_type.setter
    def cmd_type(self, val: int) -> None:
        """Set command type.

        Args:
            val (int): Command type
        """
        assert 0 <= val < 4
        self.command_parameter |= val << 8

    @property
    def cmd_code(self) -> int:
        """Get command code.

        Returns:
            int: Command code
        """
        last = (self.command_parameter & 0xF000) >> 4
        first = self.command_parameter & 0x00FF
        return first | last

    @cmd_code.setter
    def cmd_code(self, val: int) -> None:
        """Set command code.

        Args:
            val (int): Command code
        """
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


Self = TypeVar("Self", bound="ResponseHeader")


class ResponseHeader(ProtocolHeader):
    """The structure for the response header data of a packet in the protocol."""
    size: ClassVar[int] = c.sizeof(ProtocolHeader)

    @property
    def is_pushed(self) -> bool:
        """Check if response is pushed."""
        return self.request_identifier == 0

    @classmethod
    def from_bytes(cls: Type[Self], buff: bytes) -> Self | None:
        """Create ResponseHeader object from bytes."""
        header_bytes = memoryview(buff)
        if not cls._header_bytes_is_valid(header_bytes, cls.size, const.MAGIC_WORD):
            return None
        return cls.from_buffer_copy(header_bytes)

    @staticmethod
    def _header_bytes_is_valid(header_bytes: memoryview, expected_size: int, magic_wrd: bytes) -> bool:
        """Check whether the header bytes are valid.

        Args:
            header_bytes (memoryview): Header bytes
            expected_size (int): Expected header size
            magic_wrd (bytes): Magic word bytes

        Returns:
            bool: True if the header bytes are valid, False otherwise
        """
        is_correct_size = len(header_bytes) == expected_size
        start_with_mw = header_bytes[:len(magic_wrd)] == magic_wrd
        return is_correct_size and start_with_mw
