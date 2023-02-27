from __future__ import annotations
from typing import Generator
from . import _constants as const


def repr_bytes(data: bytes) -> list[str]:
    return data.hex(",").split(",")


def get_code_str(x) -> Generator[int | str, None, None]:
    code, ty = (
        x.header.cmd_code,
        x.header.cmd_type,
    )
    yield const.CommandType(ty).name
    if ty == const.CommandType.COMMAND_STATUS:
        yield const.CommandStatus(code).name
    else:
        yield code


def format_repr(obj) -> str:
    ty_str, code_str = get_code_str(obj)
    return (
        f"{str(obj.header.request_identifier):5s} "
        f"{str(obj.header.module_index):3s} "
        f"{str(obj.header.port_index):3s} "
        f"{str(obj.index_values):10s} "
        f"{str(obj.class_name):25s} "
        f"{str(code_str):6s} "
        f"{str(ty_str):15s} "
        f"{obj.values}"
    )


def format_str(obj) -> str:
    bin_str = repr_bytes(bytes(obj))
    ty_str, code_str = get_code_str(obj)
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
        )
    )
