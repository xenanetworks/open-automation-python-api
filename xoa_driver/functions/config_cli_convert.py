from __future__ import annotations
from dataclasses import dataclass, field
import typing as t
import inspect
import ipaddress
from enum import Enum
from xoa_driver.internals import commands
from xoa_driver import enums
from xoa_driver.misc import ArpChunk, NdpChunk
from xoa_driver.internals.core.transporter.protocol.payload import Hex
from xoa_driver.internals.core.transporter.protocol.struct_request import Request
from xoa_driver.internals.core.transporter.protocol._constants import CommandType
from xoa_driver.internals.core.transporter._typings import (
    XoaCommandType,
    ICmdOnlyGet,
    ICmdOnlySet,
)
from typing import ClassVar, Protocol
import re


class ICmdOnlyGett(ICmdOnlyGet, Protocol):
    __name__: ClassVar[str]


class ICmdOnlySett(ICmdOnlySet, Protocol):
    __name__: ClassVar[str]


def build_set_requestt(cls: ICmdOnlySett, **kwargs) -> Request:
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", None)
    port = kwargs.pop("port", None)
    req_values = cls.SetDataAttr(**kwargs)
    return Request(
        class_name=cls.__name__,
        cmd_type=CommandType.COMMAND_VALUE,
        cmd_code=cls.code,
        module_index=module,
        port_index=port,
        indices=indices,
        values=req_values,
    )


def build_get_requestt(cls: ICmdOnlyGett, **kwargs) -> Request:
    indices = kwargs.pop("indices", [])
    module = kwargs.pop("module", None)
    port = kwargs.pop("port", None)
    req_values = None
    return Request(
        class_name=cls.__name__,
        cmd_type=CommandType.COMMAND_QUERY,
        cmd_code=cls.code,
        module_index=module,
        port_index=port,
        indices=indices,
        values=req_values,
    )


module = port = r"\d+"  # hm.one_or_more(hm.DIGIT)
index = r"((0x|0X)?[A-Fa-f\d]+)"
zero_or_more_space = r"\s*"  # hm.zero_or_more(hm.WHITESPACE)
module_port_group = r"((?P<module>\d+)(/(?P<port>\d+))?\s*)?"
# hm.optional_group(
#     hm.named_group("module", module)
#     + hm.optional_group("/" + hm.named_group("port", port))
#     + zero_or_more_space
# )
command_name_group = r"(?P<command_name>[A-Z_a-z0-9]+\s*)"
# hm.named_group(
#     "command_name",
#     hm.one_or_more(hm.chars("A-Z", "_", "a-z", "0-9")) + zero_or_more_space,
# )
indices_group = r"(?P<indices>(\[((0x|0X)?[A-Fa-f\d]+)(,?\s*((0x|0X)?[A-Fa-f\d]+))?(,?\s*((0x|0X)?[A-Fa-f\d]+))?\]\s*)?)"
# hm.named_group(
#     "indices",
#     hm.optional_group(
#         "\["
#         + hm.one_or_more(hm.DIGIT)
#         + hm.optional_group(hm.optional(",") + zero_or_more_space + index)
#         + hm.optional_group(hm.optional(",") + zero_or_more_space + index)
#         + "\]"
#         + zero_or_more_space
#     ),
# )
params_group = r"(?P<params>.*)"
# hm.named_group("params", hm.zero_or_more(hm.ANYCHAR))
command_pattern = re.compile(
    module_port_group + command_name_group + indices_group + params_group
)


class Unpassed:
    """
    None has special meaning, so this empty type is needed for parameters which are not passed.
    """

    pass


@dataclass
class Body:
    command_name: str = ""
    cmd_class: XoaCommandType = XoaCommandType  # type: ignore
    type: CommandType = CommandType.COMMAND_STATUS
    module: t.Optional[int] = None
    port: t.Optional[int] = None
    square_indices: list[int] = field(default_factory=list)
    values: dict = field(default_factory=dict)

    def as_request(
        self,
        module_num: int | None | Unpassed = Unpassed(),
        port_num: int | None | Unpassed = Unpassed(),
        indices_num: list[int] | Unpassed = Unpassed(),
    ) -> Request:
        if not isinstance(indices_num, Unpassed):
            self.square_indices = indices_num
        if not isinstance(module_num, Unpassed):
            self.module = module_num
        if not isinstance(port_num, Unpassed):
            self.port = port_num

        dic = dict(
            indices=self.square_indices,
            module=self.module,
            port=self.port,
            **self.values,
        )
        return (
            build_get_requestt(self.cmd_class, **dic)  # type: ignore
            if self.type == CommandType.COMMAND_QUERY
            else build_set_requestt(self.cmd_class, **dic)  # type: ignore
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
                if "0x" in i or "0X" in i:
                    result.append(int(i.strip(), 16))
                else:
                    result.append(int(i.strip()))
            except Exception:
                raise ValueError(f"Invalid indices str {indices_str}!")
        return result

    @classmethod
    def _special_read(cls, class_name: str, or_params: list[str]) -> list[str]:
        params = or_params
        if class_name == "C_DOWN" and params.index("-1480937026") == 0:
            params.pop(0)
        elif class_name == "P_ARPRXTABLE":
            orr_params = or_params[0].replace("0x", "").replace("0X", "")
            params = [orr_params[i : i + 26] for i in range(0, len(orr_params), 26)]
        elif class_name == "P_NDPRXTABLE":
            orr_params = or_params[0].replace("0x", "").replace("0X", "")
            params = [orr_params[i : i + 50] for i in range(0, len(orr_params), 50)]

        return params

    @classmethod
    def _special_add(cls, class_name: str, dic: dict) -> dict:
        if class_name in ("C_DOWN", "C_FILEFINISH", "M_UPGRADE"):
            dic["magic"] = -1480937026
        elif class_name == "M_FPGAREIMAGE":
            dic["key_code"] = 42
        elif class_name == "PP_EYEMEASURE":
            dic["dummy"] = []
        elif class_name == "PP_PHYTXEQ":
            dic["mode"] = 4
        return dic

    @classmethod
    def _read_response_values(cls, or_params: list[str], cmd_class: t.Type) -> dict:
        dic = {}
        attr_set = getattr(cmd_class, "set")
        class_name = cmd_class.__name__
        values = list(inspect.signature(attr_set).parameters.values())
        params = cls._special_read(class_name, or_params)
        func_sigs: list[inspect.Parameter] = []
        list_index = -1
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
        dic = cls._special_add(class_name, dic)
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

        if len(func_sigs) == 1:  # only one param and is list
            dic.update(
                {
                    name: [
                        cls._bind_one_param(class_name, p, element_sig) for p in params
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
                if basic_type is str:
                    return str(string_param).strip('"').strip("'")
                elif basic_type is Hex:
                    s = string_param.replace("0x", "").replace("0X", "")
                    if len(s) % 2:
                        s = "0" + s
                    return Hex(s)
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
            "ipaddress.IPv4Address": ipaddress.IPv4Address,
            "IPv4Address": ipaddress.IPv4Address,
            "ipaddress.IPv6Address": ipaddress.IPv6Address,
            "IPv6Address": ipaddress.IPv6Address,
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
        if type_name == "ProtocolOption":
            enum_cast = getattr(enums, type_name, None)
            if enum_cast is not None:
                try:
                    i = int(string_param)
                    return enum_cast(256 + i)
                except Exception:
                    return None
        elif type_name == "SMAInputFunction":
            enum_cast = getattr(enums, type_name, None)
            if enum_cast is not None and string_param == "NOTUSED":
                return enum_cast["NOT_USED"]
        elif type_name == "SourceType":
            enum_cast = getattr(enums, type_name, None)
            if enum_cast is not None:
                return {
                    "TXIFG": enum_cast["TX_IFG"],
                    "TXLEN": enum_cast["TX_LEN"],
                    "RXIFG": enum_cast["RX_IFG"],
                    "RXLEN": enum_cast["RX_LEN"],
                    "RXLAT": enum_cast["RX_LATENCY"],
                    "RXJIT": enum_cast["RX_JITTER"],
                }.get(string_param, None)
        elif class_name == "P_MULTICASTHDR":
            enum_cast = getattr(enums, type_name, None)
            if enum_cast is not None:
                return enum_cast[string_param.upper().replace("DEI_", "")]
        elif class_name == "P_CHECKSUM":
            return {"ON": 14, "OFF": 0}.get(string_param, None)
        elif class_name == "P_ARPRXTABLE":
            ipv4_address = ipaddress.IPv4Address(bytes.fromhex(string_param[0:8]))
            prefix = int.from_bytes(bytes.fromhex(string_param[8:12]), "big")
            patched_mac = enums.OnOff(
                int.from_bytes(bytes.fromhex(string_param[12:14]), "big")
            )
            mac_address = Hex(string_param[14:])
            chunk = ArpChunk(ipv4_address, prefix, patched_mac, mac_address)
            return chunk
        elif class_name == "P_NDPRXTABLE":
            ipv6_address = ipaddress.IPv6Address(bytes.fromhex(string_param[0:32]))
            prefix = int.from_bytes(bytes.fromhex(string_param[32:36]), "big")
            patched_mac = enums.OnOff(
                int.from_bytes(bytes.fromhex(string_param[36:38]), "big")
            )
            mac_address = Hex(string_param[38:])
            chunk = NdpChunk(ipv6_address, prefix, patched_mac, mac_address)
            return chunk
        elif class_name == "PL1_LINKTRAIN_CMD":
            s = string_param.upper()
            t1 = ("PRE1", "MAIN", "POST", "PRE2", "PRE3")
            t2 = ("PRESET_1", "PRESET_2", "PRESET_3", "PRESET_4", "PRESET_5")
            t3 = ("PAM2", "PAM4", "PAM4_WITH_PRECODING")
            if s in t1:
                return t1.index(s)
            elif s in t2:
                return t2.index(s)
            elif s in t3:
                return t3.index(s)

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
    def _parse_param_string(cls, param_string: str) -> list[str]:
        """Handle extreme cases where \',\",\\\',\\\" or string inside param_string."""
        (
            OUTSIDE,
            INSIDE_DOUBLE_QUOTE,
            INSIDE_SINGLE_QUOTE,
            ESCAPED_DOUBLE_QUOTE,
            ESCAPED_SINGLE_QUOTE,
        ) = range(5)
        state = OUTSIDE
        string_list = []
        buf = []
        for c in param_string:
            if state == OUTSIDE:
                if c in (" ", "\t", "\r", "\n", "\f"):
                    string = "".join(buf).strip()
                    if string:
                        string_list.append(string)
                    if buf:
                        buf = []
                elif c == '"':
                    state = INSIDE_DOUBLE_QUOTE
                elif c == "'":
                    state = INSIDE_SINGLE_QUOTE
                else:
                    buf.append(c)
            elif state == INSIDE_DOUBLE_QUOTE:
                if c == "\\":
                    state = ESCAPED_DOUBLE_QUOTE
                elif c == '"':
                    string_list.append("".join(buf))
                    buf = []
                    state = OUTSIDE
                else:
                    buf.append(c)
            elif state == INSIDE_SINGLE_QUOTE:
                if c == "\\":
                    state = ESCAPED_SINGLE_QUOTE
                elif c == "'":
                    string_list.append("".join(buf))
                    buf = []
                    state = OUTSIDE
                else:
                    buf.append(c)
            elif state == ESCAPED_DOUBLE_QUOTE:
                buf.append(c)
                state = INSIDE_DOUBLE_QUOTE
            elif state == ESCAPED_SINGLE_QUOTE:
                buf.append(c)
                state = INSIDE_SINGLE_QUOTE
        if state != OUTSIDE:
            s = '"' if state == INSIDE_DOUBLE_QUOTE else "'"
            raise ValueError(f"String not complete: ({s}{''.join(buf)}).")
        if buf:
            string_list.append("".join(buf).strip())
        return string_list

    @classmethod
    def _read_params(
        cls, param_string: str, cmd_class: t.Type
    ) -> tuple[CommandType, dict]:
        params = cls._parse_param_string(param_string)
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
            if isinstance(n, str) and ("0x" in n or "0X" in n):
                return int(n.strip(), 16)
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

    @classmethod
    def read_commands_from_long_string(
        cls, long_str: str, comment_start: tuple[str, ...] = (";", "#", "//")
    ) -> t.Generator[Body, None, None]:
        for line in long_str.split("\n"):
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


# example:
# for i in CLIConverter.read_commands_from_file("198-5.xmc"):
#     print(i.as_request(3))

# for i in CLIConverter.read_commands_from_file("198-5.xpc"):
#     print(i.as_request(3, 1))
