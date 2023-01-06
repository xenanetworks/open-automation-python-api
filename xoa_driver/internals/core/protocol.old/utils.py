from __future__ import annotations
from typing import (
    NamedTuple,
    Protocol,
    Any,
)
import ctypes as c
from . import constants as const


class XmpHeader(Protocol):
    magic_word: c.c_char_p
    number_of_indices: c.c_ushort
    number_of_value_bytes: c.c_ushort
    command_parameter: c.c_ushort
    module_index: c.c_ubyte
    port_index: c.c_ubyte
    request_identifier: c.c_uint32

    @property
    def cmd_type(self) -> int: ...  # noqa: E704

    @property
    def cmd_code(self) -> int: ...   # noqa: E704

    @property
    def body_size(self) -> int: ...   # noqa: E704


class XmProtocol(Protocol):
    header: XmpHeader
    class_name: str
    index_values: list[int]
    values: Any

    def __bytes__(self) -> bytes: ...  # noqa: E704


class CodeTypeStr(NamedTuple):
    type: str  # name of command type
    code: str  # name of command status code, or command name


def repr_bytes(data: bytes) -> list[str]:
    return data.hex(",").split(",")


def get_code_str(x: XmProtocol) -> CodeTypeStr:
    code, ty = (
        x.header.cmd_code,
        x.header.cmd_type,
    )
    ty_str = const.CommandType(ty).name
    if ty == const.CommandType.COMMAND_STATUS:
        code_str = const.CommandStatus(code).name
    else:
        code_str = x.class_name
    return CodeTypeStr(ty_str, code_str)


def format_repr(obj: XmProtocol) -> str:
    ty_str, code_str = get_code_str(obj)
    return (
        f"{str(obj.header.module_index):3s} "
        f"{str(obj.header.port_index):3s} "
        f"{str(obj.index_values):10s} "
        f"{str(obj.header.request_identifier):5s} "
        f"{str(obj.class_name):25s} "
        f"{str(code_str):25s} "
        f"{str(ty_str):10s} "
        f"{obj.values}"
    )


def format_str(obj: XmProtocol, *args: str, b_str: bytes | None = None) -> str:
    bin_str = repr_bytes(bytes(obj) if not b_str else b_str)
    # The Response object are not having __bytes__ method,
    # but this function explicitly use <b_str> for <Response> and no other use cases forthis util so it's dosent mater
    (ty_str, code_str) = get_code_str(obj)
    obj_name = type(obj).__name__
    if obj_name == 'Response':
        cmd_p = 'Replied' if obj.header.request_identifier != 0 else 'Pushed'
    else:
        cmd_p = [code_str, ty_str]

    return "\n" + "\n".join(
        (
            f"{obj_name}              : {bin_str}",
            f"class_name           : {obj.class_name}",
            f"magic_word           : {obj.header.magic_word}",
            f"number_of_indices    : {obj.header.number_of_indices}",
            f"number_of_value_bytes: {obj.header.number_of_value_bytes}",
            f"command_parameter    : {obj.header.command_parameter}:{cmd_p}",
            f"module_index         : {obj.header.module_index}",
            f"port_index           : {obj.header.port_index}",
            f"request_identifier   : {obj.header.request_identifier}",
            f"index_values         : {obj.index_values}",
            f"values               : {obj.values}",
        ) + args
    )
