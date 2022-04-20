#: L23 Port Transceiver Commands

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
class PX_RW:
    """
    Provides access to the register interface supported by the port transceiver.  It
    is possible to both read and write register values.
    """

    code: typing.ClassVar[int] = 501
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _page_xindex: int
    _register_xaddress: int

    @dataclass(frozen=True)
    class SetDataAttr:
        value: XmpField[XmpHex4] = XmpField(XmpHex4)  # 4 hex bytes, register value of the port transceiver

    @dataclass(frozen=True)
    class GetDataAttr:
        value: XmpField[XmpHex4] = XmpField(XmpHex4)  # 4 hex bytes, register value of the port transceiver

    def get(self) -> "Token[GetDataAttr]":
        """Get the register value of a transceiver.

        :return: the register value of a transceiver
        :rtype: PX_RW.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress]))

    def set(self, value: str) -> "Token":
        """Set the register value of a transceiver.

        :param value: register value of a transceiver
        :type value: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress], value=value))


@register_command
@dataclass
class PX_MII:
    """Provides access to the register interface supported by the media-independent interface (MII) transceiver.  It
    is possible to both read and write register values."""

    code: typing.ClassVar[int] = 537
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _register_xaddress: int

    @dataclass(frozen=True)
    class SetDataAttr:
        value: XmpField[XmpHex2] = XmpField(XmpHex2)  # 2 hex bytes, register value of the transceiver

    @dataclass(frozen=True)
    class GetDataAttr:
        value: XmpField[XmpHex2] = XmpField(XmpHex2)  # 2 hex bytes, register value of the transceiver

    def get(self) -> "Token[GetDataAttr]":
        """Get the register value of a transceiver.

        :return: the register value of a transceiver
        :rtype: PX_MII.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._register_xaddress]))

    def set(self, value: str) -> "Token":
        """Set the register value of a transceiver.

        :param value: register value of a transceiver
        :type value: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._register_xaddress], value=value))


@register_command
@dataclass
class PX_TEMPERATURE:
    """
    Transceiver temperature in degrees Celsius.
    """

    code: typing.ClassVar[int] = 538
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        temperature_msb: XmpField[XmpByte] = XmpField(XmpByte)  # byte, temperature value before the decimal digit.
        temperature_decimal_fraction: XmpField[XmpByte] = XmpField(XmpByte)  # byte, 1/256th of a degree Celsius after the decimal digit.

    def get(self) -> "Token[GetDataAttr]":
        """Get transceiver temperature in degrees Celsius.

        :return: temperature value before the decimal digit, and 1/256th of a degree Celsius after the decimal digit.
        :rtype: PX_TEMPERATURE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


