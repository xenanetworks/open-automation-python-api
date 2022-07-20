#: L23 Port Match Term Commands

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
class PM_INDICES:
    """
    The full list of which match terms are defined for a port. These are the sub-
    index values that are used for the parameters defining the content-based
    matching of packets received for the port. Setting the value of this parameter
    creates a new empty match term for each value that is not already in use, and
    deletes each match term that is not mentioned in the list. The same can be
    accomplished one match-term-at-a-time using the PM_CREATE and PM_DELETE commands.
    """

    code: typing.ClassVar[int] = 200
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        match_term_xindices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the sub-index of a match term definition for the port.

    @dataclass(frozen=True)
    class GetDataAttr:
        match_term_xindices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the sub-index of a match term definition for the port.

    def get(self) -> "Token[GetDataAttr]":
        """Get the full list of which match terms are defined for a port.

        :return: the full list of which match terms are defined for a port
        :rtype: PM_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, match_term_xindices: typing.List[int]) -> "Token":
        """Creates a new empty match term for each value that is not already in use, and delete each match term that is not mentioned in the list

        :param match_term_xindices: the sub-index of a match term definition for the port
        :type match_term_xindices: List[int]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, match_term_xindices=match_term_xindices))


@register_command
@dataclass
class PM_CREATE:
    """
    Creates an empty match term definition with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 201
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _match_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Creates an empty match term definition with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._match_term_xindex],
            ),
        )


@register_command
@dataclass
class PM_DELETE:
    """
    Deletes the match term definition with the specified sub-index value. A match
    term cannot be deleted while it is used in the condition of any filter for the
    port.
    """

    code: typing.ClassVar[int] = 202
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _match_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Deletes the match term definition with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._match_term_xindex],
            ),
        )


@register_command
@dataclass
class PM_PROTOCOL:
    """
    The protocol segments assumed on the packets received on the port. This is
    mainly for information purposes, and helps you identify which portion of the
    packet header is being matched. The actual value definition of the match
    position is specified with PM_POSITION.
    """

    code: typing.ClassVar[int] = 203
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _match_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        segments: XmpField[XmpByteList] = XmpField(
            XmpByteList, choices=ProtocolOption
        )  # list of coded bytes, a number specifying a built-in protocol segment: Uses the same coded values as the PS_HEADERPROTOCOL parameter.

    @dataclass(frozen=True)
    class GetDataAttr:
        segments: XmpField[XmpByteList] = XmpField(
            XmpByteList, choices=ProtocolOption
        )  # list of coded bytes, a number specifying a built-in protocol segment: Uses the same coded values as the PS_HEADERPROTOCOL parameter.

    def get(self) -> "Token[GetDataAttr]":
        """Get the protocol segments assumed on the packets received on the port.

        :return: a number specifying a built-in protocol segment: Uses the same coded values as the PS_HEADERPROTOCOL parameter.
        :rtype: PM_PROTOCOL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._match_term_xindex]))

    def set(self, segments: typing.List[ProtocolOption]) -> "Token":
        """Set the protocol segments assumed on the packets received on the port.

        :param segments: a number specifying a built-in protocol segment: Uses the same coded values as the PS_HEADERPROTOCOL parameter
        :type segments: List[ProtocolOption]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._match_term_xindex], segments=segments))


@register_command
@dataclass
class PM_POSITION:
    """
    The position within each received packet where content matching begins for the
    port.
    """

    code: typing.ClassVar[int] = 204
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _match_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        byte_offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, offset from the start of the packet bytes.

    @dataclass(frozen=True)
    class GetDataAttr:
        byte_offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, offset from the start of the packet bytes.

    def get(self) -> "Token[GetDataAttr]":
        """Get the position within each received packet where content matching begins for the port.

        :return: offset from the start of the packet bytes
        :rtype: PM_POSITION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._match_term_xindex]))

    def set(self, byte_offset: int) -> "Token":
        """Set the position within each received packet where content matching begins for the port. 

        :param byte_offset: offset from the start of the packet bytes
        :type byte_offset: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._match_term_xindex], byte_offset=byte_offset))


@register_command
@dataclass
class PM_MATCH:
    """
    The value that must be found at the match term position for packets received on
    the port. The mask can make certain bit positions don't-care.
    """

    code: typing.ClassVar[int] = 205
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _match_term_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes, which bits are significant in the match operation.
        value: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes, the value that must be found for the match term to be true.

    @dataclass(frozen=True)
    class GetDataAttr:
        mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes, which bits are significant in the match operation.
        value: XmpField[XmpHex8] = XmpField(XmpHex8)  # eight hex bytes, the value that must be found for the match term to be true.

    def get(self) -> "Token[GetDataAttr]":
        """Get the value that must be found at the match term position for packets received on the port.

        :return: which bits are significant in the match operation, and the value that must be found for the match term to be true.
        :rtype: PM_MATCH.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._match_term_xindex]))

    def set(self, mask: str, value: str) -> "Token":
        """Set the value that must be found at the match term position for packets received on the port.

        :param mask: which bits are significant in the match operation
        :type mask: str
        :param value: the value that must be found for the match term to be true
        :type value: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._match_term_xindex], mask=mask, value=value))