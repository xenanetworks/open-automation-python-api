#: L23 Port Length Term Commands

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
class PL_INDICES:
    """
    The full list of which length terms are defined for a port. These are the sub-
    index values that are used for the parameters defining the length-based matching
    of packets received for the port. Setting the value of this parameter creates a
    new empty length term for each value that is not already in use, and deletes
    each length term that is not mentioned in the list. The same can be accomplished
    one- length-term-at-a-time using the PL_CREATE and PL_DELETE commands.
    """

    code: typing.ClassVar[int] = 207
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        length_term_xindices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the sub-index of a length term definition for the port.

    @dataclass(frozen=True)
    class GetDataAttr:
        length_term_xindices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the sub-index of a length term definition for the port.

    def get(self) -> "Token[GetDataAttr]":
        """Get the full list of which length terms are defined for a port.

        :return: the full list of which length terms are defined for a port
        :rtype: PL_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, length_term_xindices: typing.List[int]) -> "Token":
        """Create a new empty length term for each value that is not already in use, and deletes each length term that is not mentioned in the list.

        :param length_term_xindices: the list of indices of length terms to be created on a port.
        :type length_term_xindices: List[int]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, length_term_xindices=length_term_xindices))


@register_command
@dataclass
class PL_CREATE:
    """
    Creates an empty length term definition with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 208
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _length_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Creates an empty length term definition with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._length_term_xindex],
            ),
        )


@register_command
@dataclass
class PL_DELETE:
    """
    Deletes the length term definition with the specified sub-index value. A length
    term cannot be deleted while it is used in the condition of any filter for the
    port.
    """

    code: typing.ClassVar[int] = 209
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _length_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Deletes the length term definition with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._length_term_xindex],
            ),
        )


@register_command
@dataclass
class PL_LENGTH:
    """
    The specification for a length-based check that is applied on the packets
    received on the port.
    """

    code: typing.ClassVar[int] = 210
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _length_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        length_check_type: XmpField[XmpInt] = XmpField(XmpInt, choices=LengthCheckType)  # coded integer, whether to test for shorter-than or longer-than.
        size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the value to compare the packet length against.

    @dataclass(frozen=True)
    class GetDataAttr:
        length_check_type: XmpField[XmpInt] = XmpField(XmpInt, choices=LengthCheckType)  # coded integer, whether to test for shorter-than or longer-than.
        size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the value to compare the packet length against.

    def get(self) -> "Token[GetDataAttr]":
        """Get the configuration of a length-based check that is applied on the packets received on a port.

        :return: whether to test for shorter-than or longer-than, and the value to compare the packet length against
        :rtype: PL_LENGTH.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._length_term_xindex]))

    def set(self, length_check_type: LengthCheckType, size: int) -> "Token":
        """Set the configuration of a length-based check that is applied on the packets received on a port. 

        :param length_check_type: whether to test for shorter-than or longer-than
        :type length_check_type: LengthCheckType
        :param size: the value to compare the packet length against
        :type size: int
        """
        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._length_term_xindex], length_check_type=length_check_type, size=size),
        )

    set_at_most = functools.partialmethod(set, LengthCheckType.AT_MOST)
    """Set the length check to be short than or equal to the given length (at most).
    """
    set_at_least = functools.partialmethod(set, LengthCheckType.AT_LEAST)
    """Set the length check to be longer than or equal to the given length (at least).
    """


