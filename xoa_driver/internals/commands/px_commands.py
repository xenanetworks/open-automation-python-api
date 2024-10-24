from __future__ import annotations
from dataclasses import dataclass
import typing

from xoa_driver.internals.core.builders import (
    build_get_request,
    build_set_request
)
from xoa_driver.internals.core import interfaces
from xoa_driver.internals.core.token import Token
from xoa_driver.internals.core.transporter.registry import register_command
from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    RequestBodyStruct,
    ResponseBodyStruct,
    XmpByte,
    XmpHex,
    XmpSequence,
    XmpInt,
    Hex,
)


@register_command
@dataclass
class PX_RW:
    """
    Provides read and write access to the register interface supported by the port transceiver. It is possible to both read and write register values.
    """

    code: typing.ClassVar[int] = 501
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _page_xindex: int
    _register_xaddress: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex(size=4))
        """4 hex bytes, register value of the port transceiver"""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex(size=4))
        """4 hex bytes, register value of the port transceiver"""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver.

        :return: the register value of a transceiver
        :rtype: PX_RW.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress], value=value))


@register_command
@dataclass
class PX_RW_SEQ:
    """
    I2C sequential access to a transceiver's register. When invoked, the <byte_count> number of bytes will be read or written in one I2C transaction, in which the <value> is read or written with only a single register address setup. A subsequent invocation will perform a second I2C transaction in the same manner.

    * <_byte_xcount> number of bytes will be read or written in one I2C transaction

    * <_page_xindex>: the transceiver page address, integer, 0x00 - 0xFF (0-255).

    * <_register_xaddress>: the address within the page, integer, 0x00 - 0xFF (0-255).

    If <_register_xaddress> < 128, the page index <_page_xindex> is ignored by the server. The server will read from page 0 without writing 0 into byte 127.

    If <_register_xaddress> >=128, the page index <_page_xindex> will be written into byte 127.
    """

    code: typing.ClassVar[int] = 503
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _page_xindex: int
    _register_xaddress: int
    _byte_xcount: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the ``<value>`` equals ``<byte_count>``."""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the ``<value>`` equals ``<byte_count>``."""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver in one I2C transaction.

        :return: the register value of a transceiver
        :rtype: PX_RW_SEQ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress, self._byte_xcount]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver in one I2C transaction.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._page_xindex, self._register_xaddress, self._byte_xcount],
                value=value
            )
        )


@register_command
@dataclass
class PX_RW_SEQ_BANK:
    """
    I2C sequential access to a transceiver's register. When invoked, the <byte_count> number of bytes will be read or written in one I2C transaction, in which the <value> is read or written with only a single register address setup. A subsequent invocation will perform a second I2C transaction in the same manner.

    * <_bank_xindex>: the bank address, integer, 0x00 - 0xFF (0-255).

    * <_page_xindex>: the transceiver page address, integer, 0x00 - 0xFF (0-255).

    * <_register_xaddress>: the address within the page, integer, 0x00 - 0xFF (0-255).

    * <_byte_xcount> number of bytes will be read or written in one I2C transaction

    If <_register_xaddress> < 128, the page index <page> and the bank index <_bank_xindex> is ignored by the server. The server will read from page 0 without writing 0 into byte 127.

    If <_register_xaddress> >=128, the page index <page> will be written into byte 127, and the bank index <_bank_xindex> will be written into byte 126.
    """

    code: typing.ClassVar[int] = 504
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _bank_xindex: int
    _page_xindex: int
    _register_xaddress: int
    _byte_xcount: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the ``<value>`` equals ``<byte_count>``."""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the ``<value>`` equals ``<byte_count>``."""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver in one I2C transaction.

        :return: the register value of a transceiver
        :rtype: PX_RW_SEQ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._bank_xindex, self._page_xindex, self._register_xaddress, self._byte_xcount]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver in one I2C transaction.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._bank_xindex, self._page_xindex, self._register_xaddress, self._byte_xcount],
                value=value
            )
        )

@register_command
@dataclass
class PX_MII:
    """Provides access to the register interface supported by the media-independent interface (MII) transceiver. It
    is possible to both read and write register values."""

    code: typing.ClassVar[int] = 537
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _register_xaddress: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex(size=2))
        """2 hex bytes, register value of the transceiver"""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex(size=2))
        """2 hex bytes, register value of the transceiver"""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver.

        :return: the register value of a transceiver
        :rtype: PX_MII.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._register_xaddress]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._register_xaddress], value=value))


@register_command
@dataclass
class PX_TEMPERATURE:
    """
    Transceiver temperature in degrees Celsius.
    """

    code: typing.ClassVar[int] = 538
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        integral_part: int = field(XmpByte())
        """byte, temperature value before the decimal digit."""
        fractional_part: int = field(XmpByte())
        """byte, 1/256th of a degree Celsius after the decimal digit."""

    def get(self) -> Token[GetDataAttr]:
        """Get transceiver temperature in degrees Celsius.

        :return: temperature value before the decimal digit, and 1/256th of a degree Celsius after the decimal digit.
        :rtype: PX_TEMPERATURE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

@register_command
@dataclass
class PX_I2C_CONFIG:
    """
    Set the get the access speed on a transceiver I2C access in the unit of KHz. Default to 100. When the transceiver is plugged out and in again, the speed will be reset to the default value 100. The speed has a minimum and a maximum, which can be obtained from P_CAPABILITIES. The I2C speed configuration will not be included in the port configuration file (.xpc). When you load a port configuration to a port, the transceiver I2C access speed will be reset to default 100.
    """

    code: typing.ClassVar[int] = 539
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        frequency: int = field(XmpInt())
        """integer, frequency in kHz, default is 100."""
    
    class SetDataAttr(RequestBodyStruct):
        frequency: int = field(XmpInt())
        """integer, frequency in kHz, default is 100."""

    def get(self) -> Token[GetDataAttr]:
        """Get the speed on a transceiver I2C access in the unit of KHz.

        :return: frequency in kHz.
        :rtype: PX_I2C_CONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
    def set(self, frequency: int) -> Token[None]:
        """Set the speed on a transceiver I2C access in the unit of KHz.

        :param frequency: frequency in kHz
        :type frequency: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, frequency=frequency))