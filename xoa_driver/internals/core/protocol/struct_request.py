import ctypes as c
import struct
from typing import List

from . import constants as const
from .fields.data_types import XmpEmpty
from . import utils
from .struct_header import ProtocolHeader


class Request:
    def __init__(
        self,
        class_name: str,
        indices: List[int],
        cmd_type: int,
        cmd_code: int,
        module_index: int = const.NOTHING,
        port_index: int = const.NOTHING,
        values: object = None,
    ) -> None:
        self.class_name = class_name
        self.header = ProtocolHeader(
            magic_word = const.MAGIC_WORD,
            number_of_indices = len(indices),
            number_of_value_bytes = self._get_values_length(values),
            cmd_code = cmd_code,
            cmd_type = cmd_type,
            module_index = module_index,
            port_index = port_index,
            request_identifier = 0,
        )
        self.index_values = indices
        self.values = values
        self.padding = (
            4 - (self.header.number_of_value_bytes % 4)
            if self.header.number_of_value_bytes % 4
            else 0
        )

    def __str__(self) -> str:
        return utils.format_str(
            self, 
            f"padding              : {self.padding}",
        )

    def __repr__(self) -> str:
        return utils.format_repr(self)

    def __bytes__(self) -> bytes:
        cmd_all = b"".join(
            (
                bytes(self.header), # type: ignore
                struct.pack(f"!{self.header.number_of_indices}I", *self.index_values),
                self._get_values_bytes(self.values),
                bytes(self.padding),
            )
        )
        return cmd_all

    @staticmethod
    def _get_values_length(values: object) -> int:
        if values is None or not hasattr(values, "__annotations__"):
            return 0
        return sum(
            getattr(values, k, XmpEmpty()).byte_length()
            for k in values.__annotations__.keys()
        )

    @staticmethod
    def _get_values_bytes(values: object) -> bytes:
        if values is None or not hasattr(values, "__annotations__"):
            return b""
        return b"".join(
            bytes(getattr(values, k))
            for k in values.__annotations__.keys()
        )