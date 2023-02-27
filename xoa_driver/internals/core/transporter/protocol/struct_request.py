from __future__ import annotations
import struct

from . import _constants as const
from . import _utils
from .struct_header import ProtocolHeader
from .payload import RequestBodyStruct

NOT_SET_IDENTIFIER = 0


class Request:
    __slots__ = (
        "class_name",
        "header",
        "index_values",
        "values"
    )

    def __init__(
        self,
        class_name: str,
        cmd_type: const.CommandType,
        cmd_code: int,
        module_index: int | None,
        port_index: int | None,
        indices: list[int],
        values: RequestBodyStruct | None = None,
    ) -> None:
        self.class_name = class_name
        self.header = ProtocolHeader(
            magic_word=const.MAGIC_WORD,
            number_of_indices=len(indices),
            number_of_value_bytes=values.nbytes() if values else 0,
            cmd_code=cmd_code,
            cmd_type=cmd_type.value,
            module_index=const.NOTHING if module_index is None else module_index,
            port_index=const.NOTHING if port_index is None else port_index,
            request_identifier=NOT_SET_IDENTIFIER,
        )
        self.index_values = indices
        self.values = values

    def __str__(self) -> str:
        return _utils.format_str(self)

    def __repr__(self) -> str:
        return _utils.format_repr(self)

    def __bytes__(self) -> bytes:
        idx_format = const.indices_format(self.header.number_of_indices)
        return bytes().join(
            (
                self.header,
                struct.pack(idx_format, *self.index_values),
                self.values.to_bytes() if self.values else b""
            )
        )

    def update_identifier(self, request_id: int) -> None:
        self.header.request_identifier = request_id

    @property
    def cmd_code(self) -> int:
        return self.header.cmd_code
