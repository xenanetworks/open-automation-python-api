from __future__ import annotations
from dataclasses import dataclass, field, fields
import typing as t
import inspect
import ipaddress
from enum import Enum
from xoa_driver.internals import commands
from xoa_driver import enums
from xoa_driver.misc import ArpChunk, NdpChunk
from xoa_driver.internals.core.transporter.protocol.payload import Hex
from xoa_driver.internals.core.builders import build_get_request, build_set_request
from xoa_driver.internals.core.transporter.protocol.struct_request import Request
from xoa_driver.internals.core.transporter.protocol._constants import CommandType
from xoa_driver.internals.core.transporter._typings import (
    ICmdOnlyGet,
    ICmdOnlySet,
    XoaCommandType,
)
import re
import humre as hm

module = port = index = hm.one_or_more(hm.DIGIT)
zero_or_more_space = hm.zero_or_more(hm.WHITESPACE)
module_port_group = hm.optional_group(
    hm.named_group("module", module)
    + hm.optional_group("/" + hm.named_group("port", port))
    + zero_or_more_space
)
command_name_group = hm.named_group(
    "command_name",
    hm.one_or_more(hm.chars("A-Z", "_", "a-z", "0-9")) + zero_or_more_space,
)
indices_group = hm.named_group(
    "indices",
    hm.optional_group(
        "\["
        + hm.one_or_more(hm.DIGIT)
        + hm.optional_group(hm.optional(",") + zero_or_more_space + index)
        + hm.optional_group(hm.optional(",") + zero_or_more_space + index)
        + "\]"
        + zero_or_more_space
    ),
)
params_group = hm.named_group("params", hm.zero_or_more(hm.ANYCHAR))

command_pattern = hm.compile(
    module_port_group + command_name_group + indices_group + params_group
)


@dataclass
class Body:
    command_name: str = ""
    cmd_class: XoaCommandType = XoaCommandType
    type: CommandType = CommandType.COMMAND_STATUS
    module: t.Optional[int] = None
    port: t.Optional[int] = None
    indices: list[int] = field(default_factory=list)
    values: dict = field(default_factory=dict)

    def as_request(
        self,
        module_num: int | None = None,
        port_num: int | None = None,
        indices_num: list[int] | None = None,
    ) -> Request:
        if indices_num is None:
            indices_num = []
        self.module = module_num
        self.port = port_num
        self.indices = indices_num
        dic = dict(
            indices=self.indices, module=self.module, port=self.port, **self.values
        )
        return (
            build_get_request(self.cmd_class, **dic) # type: ignore
            if self.type == CommandType.COMMAND_QUERY
            else build_set_request(self.cmd_class, **dic) # type: ignore
        )


class CLIConverter:
    @classmethod
    def _read_indices(cls, indices_str: str) -> list[int]:
        result = []
        ind = indices_str.strip().strip("[").strip("]").split(",")
        for i in ind:
            if not i:
                continue
            try:
                result.append(int(i.strip()))
            except Exception:
                raise ValueError(f"Invalid indices str {indices_str}!")
        return result

    @classmethod
    def _read_response_values(cls, params: list[str], cmd_class: t.Type) -> dict:
        dic = {}
        attr_set = getattr(cmd_class, "set")
        values = list(inspect.signature(attr_set).parameters.values())
        func_sigs: list[inspect.Parameter] = []
        list_index = -1
        class_name = cmd_class.__name__
        for i, v in enumerate(values):
            if v.name == "self":
                continue
            if "list[" in str(v.annotation).lower():
                list_index = i - 1
            func_sigs.append(v)
        # if len(params) < len(func_sigs) and func_sigs:
        #     raise ValueError("Not enough parameters!")

        if list_index == -1:
            dic = {
                f.name: cls._bind_one_param(class_name, p, f.annotation)
                for p, f in zip(params, func_sigs)
            }
        else:
            element_sig = (
                values[list_index + 1]
                .annotation.replace("typing.", "")
                .replace("list[", "")
                .replace("List[", "")
                .replace("]", "")
            )
            dic = cls._bind_has_list(
                class_name, params, func_sigs, list_index, element_sig
            )
        return dic

    @classmethod
    def _bind_has_list(
        cls,
        class_name: str,
        params: list[str],
        func_sigs: list[inspect.Parameter],
        list_index: int,
        element_sig: str,
    ) -> dict[str, t.Any]:
        dic = {}
        name = func_sigs[list_index].name
        fore_sigs = func_sigs[:list_index]
        fore_params = params[:list_index]

        back_sigs = func_sigs[list_index + 1 :]
        back_params = params[-len(back_sigs) :]

        if len(func_sigs) and len(params) == 1:  # only one param and is list
            chunks = {"ArpChunk": ArpChunk, "NdpChunk": NdpChunk}
            if element_sig in chunks:
                result = []
                tye = chunks[element_sig]
                sig_types = [f.type.__name__ for f in fields(tye)]

                for i in range(0, len(params), 4):
                    args = [
                        cls._bind_one_param(class_name, p, f)
                        for p, f in zip(params[i : i + 4], sig_types)
                    ]
                    result.append(tye(*args))

                dic[name] = result
            else:
                dic.update(
                    {
                        name: [
                            cls._bind_one_param(class_name, p, element_sig)
                            for p in params
                        ]
                    }
                )
        elif len(fore_params) == len(fore_sigs) != 0:  # others followed by a list
            list_params = params[list_index:]
            dic.update(
                {
                    f.name: cls._bind_one_param(class_name, p, f.annotation)
                    for p, f in zip(fore_params, fore_sigs)
                }
            )
            dic[name] = [
                cls._bind_one_param(class_name, b, element_sig) for b in list_params
            ]
        elif len(back_params) == len(back_sigs) != 0:  # a list follow by others
            list_params = params[: -(len(func_sigs) - list_index - 1)]
            dic.update(
                {
                    f.name: cls._bind_one_param(class_name, p, f.annotation)
                    for p, f in zip(back_params, back_sigs)
                }
            )
            dic[name] = [
                cls._bind_one_param(class_name, b, element_sig) for b in list_params
            ]
        return dic

    @classmethod
    def _basic_cast(
        cls, string_param: str, type_name: str
    ) -> str | int | float | Hex | None:
        basics = {
            "str": str,
            "int": int,
            "float": float,
            "Hex": Hex,
        }
        basic_type = basics.get(type_name, None)
        if basic_type is not None:
            try:
                return basic_type(string_param)
            except ValueError:
                return None

    @classmethod
    def _ip_cast(
        cls,
        string_param: str,
        type_name: str,
    ) -> ipaddress.IPv4Address | ipaddress.IPv6Address | None:
        ips = {
            "ipaddress.IPv4Address": ipaddress.ip_address,
            "IPv4Address": ipaddress.ip_address,
            "ipaddress.IPv6Address": ipaddress.ip_address,
            "IPv6Address": ipaddress.ip_address,
        }
        ips_cast = ips.get(type_name, None)
        if ips_cast is not None:
            try:
                return ips_cast(string_param)
            except Exception:
                pass
            try:
                # input is int-IPv4 but in a str form:
                # ipaddress.ip_address(3232235788) -> IPv4Address('192.168.1.12')
                return ips_cast(int(string_param))
            except Exception:
                pass
            try:
                # input is IPV6 but in a str form:
                # ipaddress.ip_address(int('0x10000000000000000000000000000000'), 16) -> IPv6Address('1000::')
                return ips_cast(int(string_param, 16))
            except Exception:
                pass
        return None

    @classmethod
    def _enum_cast(cls, string_param: str, type_name: str) -> Enum | None:
        enum_cast = getattr(enums, type_name, None)
        if enum_cast is not None:
            try:
                return enum_cast(int(string_param))
            except Exception:
                pass
            try:
                return enum_cast[string_param.upper()]
            except Exception:
                pass
        return None

    @classmethod
    def _special_cast(cls, class_name: str, string_param: str, type_name: str) -> t.Any:
        if class_name == "P_MULTICASTHDR":
            enum_cast = getattr(enums, type_name, None)
            if enum_cast is not None:
                return enum_cast[string_param.upper().replace("DEI_", "")]
        elif class_name == "P_CHECKSUM":
            return {"ON": 14, "OFF": 0}.get(string_param, None)

    @classmethod
    def _bind_one_param(
        cls, class_name: str, string_param: str, type_name: str
    ) -> t.Any:
        basic_cast = cls._basic_cast(string_param, type_name)
        if basic_cast is not None:
            return basic_cast

        ip_cast = cls._ip_cast(string_param, type_name)
        if ip_cast is not None:
            return ip_cast

        enum_cast = cls._enum_cast(string_param, type_name)
        if enum_cast is not None:
            return enum_cast

        special_cast = cls._special_cast(class_name, string_param, type_name)
        if special_cast is not None:
            return special_cast

        raise ValueError(f"Cannot bind param '{string_param}' to type '{type_name}'!")

    @classmethod
    def _read_params(
        cls, param_string: str, cmd_class: t.Type
    ) -> tuple[CommandType, dict]:
        params = [p.strip() for p in param_string.split()]
        if params == ["?"]:
            return CommandType.COMMAND_QUERY, {}
        return CommandType.COMMAND_VALUE, cls._read_response_values(params, cmd_class)

    @classmethod
    def _read_command_name(cls, command_name: str) -> t.Type:
        return getattr(commands, command_name.upper())

    @classmethod
    def _read_int(cls, n: str | int | None) -> int | None:
        if n is None:
            return None
        try:
            return int(n)
        except Exception:
            return None

    @classmethod
    def convert_each_command(cls, command: str) -> Body | None:
        result = re.search(command_pattern, command)
        if not result:
            return None
        command_name = result.group("command_name").strip() or ""
        cmd_class = cls._read_command_name(command_name)
        module_index = cls._read_int(result.group("module"))
        port_index = cls._read_int(result.group("port"))
        indices = cls._read_indices(result.group("indices"))
        body_type, values = cls._read_params(result.group("params") or "", cmd_class)
        body = Body(
            command_name,
            cmd_class,
            body_type,
            module_index,
            port_index,
            indices,
            values,
        )
        return body

    @classmethod
    def read_commands_from_file(
        cls, path: str, comment_start: tuple[str, ...] = (";", "#", "//")
    ) -> t.Generator[Body, None, None]:
        with open(path, "r") as f:
            for line in f:
                buf = line.strip()
                for i, char in enumerate(buf):
                    if char in comment_start:
                        buf = buf[:i]
                        break
                if not buf:
                    continue
                r = cls.convert_each_command(buf)
                if r is not None:
                    yield r


if __name__ == "__main__":
    for i in CLIConverter.read_commands_from_file("198-5.xmc"):
        print(i.as_request(3))

    for i in CLIConverter.read_commands_from_file("198-5.xpc"):
        print(i.as_request(3, 1))
