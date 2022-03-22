"""
Port L47 Packet Engine Commands
"""
from dataclasses import dataclass
import typing

from ..protocol.command_builders import (
    build_get_request,
    build_set_request
)
from .. import interfaces
from ..transporter.token import Token
from ..protocol.fields.data_types import *
from ..protocol.fields.field import XmpField
from ..registry import register_command
from .enums import *

@register_command
@dataclass
class P4E_ASSIGN:
    """
    Advanced mode only: Assign previously reserved PEs to a port.
    """

    code: typing.ClassVar[int] = 675
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # eigth hex bytes, a bitmask specifying which PEs should be assigned to this port

    @dataclass(frozen=True)
    class GetDataAttr:
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # eigth hex bytes, a bitmask specifying which PEs should be assigned to this port

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mask: str) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mask=mask))


@register_command
@dataclass
class P4E_AVAILABLE:
    """
    Simple mode only: Report the number of PEs available for allocation.
    """

    code: typing.ClassVar[int] = 676
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        available_pe_count: XmpField[XmpByte] = XmpField(
            XmpByte
        )  # byte, total number of PEs that can be allocated to the port - including the PEs already allocated to the port.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P4E_ALLOCATE:
    """
    Simple mode only: Allocate a number of PEs to this port.
    """

    code: typing.ClassVar[int] = 677
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pe_count_alloc: XmpField[XmpByte] = XmpField(XmpByte)  # byte, the total number of PEs to allocate to this port - including the PEs already allocated to the port.

    @dataclass(frozen=True)
    class GetDataAttr:
        pe_count_alloc: XmpField[XmpByte] = XmpField(XmpByte)  # byte, the total number of PEs to allocate to this port - including the PEs already allocated to the port.

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, pe_count_alloc: int) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, pe_count_alloc=pe_count_alloc))


@register_command
@dataclass
class P4E_ALLOCATION_INFO:
    """
    Display information about which PEs that are available for allocation/assignment
    and which are currently allocated/assigned to this port.
    """

    code: typing.ClassVar[int] = 678
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        available: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes (64-bit) mask of available PEs
        allocated: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes (64-bit) mask of PEs assigned to this port

    def get(self) -> "Token[GetDataAttr]":
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


