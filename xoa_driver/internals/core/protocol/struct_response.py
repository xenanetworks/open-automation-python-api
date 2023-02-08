from __future__ import annotations
import struct
from typing import (
    Any,
)
from . import constants as const
from . import utils
from .struct_header import ResponseHeader
from .payload import ResponseBodyStruct


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

    __slots__ = (
        "class_name",
        "header",
        "_buff",
        "__cursor",
        "index_values",
        "values",
    )

    def __init__(self, header: ResponseHeader, class_name: str, buffer: memoryview, response_struct: type[ResponseBodyStruct] | None) -> None:
        self.class_name = class_name
        self.header = header
        self._buff = buffer
        self.index_values = self.__parse_indices()
        self.values: Any = None
        if self.header.cmd_type == const.CommandType.COMMAND_VALUE:
            self.values = response_struct(self._buff) if response_struct else None

    def __str__(self) -> str:
        return utils.format_str(self)

    def __repr__(self) -> str:
        return utils.format_repr(self)

    def __bytes__(self) -> bytes:
        return bytes(self.header) + self._buff.tobytes()

    @property
    def command_status(self) -> const.CommandStatus | None:
        if self.header.cmd_type == const.CommandType.COMMAND_STATUS:
            return const.CommandStatus(self.header.cmd_code)
        return None

    def __parse_indices(self) -> list[int]:
        format = f"!{self.header.number_of_indices}I"
        indices = struct.unpack_from(format, self._buff, 0)
        return list(indices)

    @property
    def is_ok(self) -> bool:
        return self.get_return_ok() or self.set_return_ok()

    def set_return_ok(self) -> bool:
        is_status_resp = self.header.cmd_type == const.CommandType.COMMAND_STATUS
        is_succesful = self.header.cmd_code == const.CommandStatus.OK
        return is_status_resp and is_succesful

    def get_return_ok(self) -> bool:
        is_payload_resp = self.header.cmd_type == const.CommandType.COMMAND_VALUE
        contain_values = self.values is not None
        return is_payload_resp and contain_values
