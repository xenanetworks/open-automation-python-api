from __future__ import annotations
import struct
from typing import Any
from . import _constants as const
from . import _utils
from .struct_header import ResponseHeader
from .payload import ResponseBodyStruct
from .exceptions import get_status_error, XmpStatusException


class Response:
    """
    Response serializer
    """

    __slots__ = (
        "class_name",
        "header",
        "index_values",
        "values",
        "__buffer",
    )

    def __init__(self, class_name: str, header: ResponseHeader, buffer: bytes, response_struct: type[ResponseBodyStruct] | None) -> None:
        self.class_name = class_name
        self.header = header
        idces_fmt_ = const.indices_format(header.number_of_indices)
        idx_count_ = struct.calcsize(idces_fmt_)
        self.__buffer = memoryview(buffer)
        self.index_values = self.__parse_indices(idces_fmt_, self.__buffer[:idx_count_])
        payload_position = slice(idx_count_, idx_count_ + header.number_of_value_bytes)
        self.values: Any = self.__parse_values(self.__buffer[payload_position], response_struct)

    def __str__(self) -> str:
        return _utils.format_str(self)

    def __repr__(self) -> str:
        return _utils.format_repr(self)

    def __bytes__(self) -> bytes:
        return bytes().join((self.header, self.__buffer))

    def __parse_indices(self, fmt: str, buffer: memoryview) -> list[int]:
        return list(struct.unpack_from(fmt, buffer, 0))

    def __parse_values(self, buffer: memoryview, struct_type: type[ResponseBodyStruct] | None) -> ResponseBodyStruct | None:
        if self.header.cmd_type == const.CommandType.COMMAND_VALUE:
            return struct_type(buffer) if struct_type else None
        return None

    def get_error(self) -> XmpStatusException | None:
        if self.is_ok:
            return None
        exception = get_status_error(self.command_status)
        return exception(self.class_name)

    @property
    def is_pushed(self) -> bool:
        return self.header.is_pushed

    @property
    def request_identifier(self) -> int:
        return self.header.request_identifier

    @property
    def cmd_code(self) -> int:
        return self.header.cmd_code

    @property
    def command_status(self) -> const.CommandStatus | None:
        if self.header.cmd_type == const.CommandType.COMMAND_STATUS:
            return const.CommandStatus(self.header.cmd_code)
        return None

    @property
    def is_ok(self) -> bool:
        return self.get_return_ok or self.set_return_ok

    @property
    def set_return_ok(self) -> bool:
        is_status_resp = self.header.cmd_type == const.CommandType.COMMAND_STATUS
        is_succesful = self.header.cmd_code == const.CommandStatus.OK
        return is_status_resp and is_succesful

    @property
    def get_return_ok(self) -> bool:
        is_payload_resp = self.header.cmd_type == const.CommandType.COMMAND_VALUE
        contain_values = self.values is not None
        return is_payload_resp and contain_values
