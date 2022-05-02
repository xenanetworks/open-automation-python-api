"""
L47 Module Packet Engine Commands
"""
from dataclasses import dataclass
import typing
import functools

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
class M4E_MODE:
    """
    Select resource allocation mode.
    """

    code: typing.ClassVar[int] = 850
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=ResourceAllocationMode)  # coded byte, resource allocation mode.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=ResourceAllocationMode)  # coded byte, resource allocation mode.

    def get(self) -> "Token[GetDataAttr]":
        """Get the resource allocation mode.

        :return: resource allocation mode
        :rtype: M4E_MODE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, mode: ResourceAllocationMode) -> "Token":
        """Set the resource allocation mode.

        :param mode: resource allocation mode
        :type mode: ResourceAllocationMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, mode=mode))

    set_simple = functools.partialmethod(set, ResourceAllocationMode.SIMPLE)
    """Set resource allocation mode to Simple."""
    set_advanced = functools.partialmethod(set, ResourceAllocationMode.ADVANCED)
    """Set resource allocation mode to Advanced."""


@register_command
@dataclass
class M4E_RESERVE:
    """
    Advanced mode only: Reserve a number of PEs so they later can be assigned to
    specific ports.
    """

    code: typing.ClassVar[int] = 851
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes, bitmask of PEs to reserve

    @dataclass(frozen=True)
    class GetDataAttr:
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes, bitmask of PEs to reserve

    def get(self) -> "Token[GetDataAttr]":
        """Get the PEs reserved.

        :return: the number of PEs reserved.
        :rtype: M4E_RESERVE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, mask: str) -> "Token":
        """Set PEs reserved.

        :param mask: bitmask of PEs to reserve
        :type mask: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, mask=mask))


