#: L23 Port Filter Commands

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
class PF_INDICES:
    """
    The full list of which filters are defined for a port. These are the sub-index
    values that are used for the parameters defining the compound conditions on the
    match/length terms operating on the packets received for the port. Setting the
    value of this parameter creates a new empty filter for each value that is not
    already in use, and deletes each filter that is not mentioned in the list. The
    same can be accomplished one-filter-at-a-time using the PF_CREATE and PF_DELETE
    commands.
    """

    code: typing.ClassVar[int] = 211
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filter_xindices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the list of indices of filters on a port.

    @dataclass(frozen=True)
    class GetDataAttr:
        filter_xindices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the list of indices of filters on a port.

    def get(self) -> "Token[GetDataAttr]":
        """Get the full list of which filters are defined for a port.

        :return: the list of indices of filters on a port
        :rtype: PF_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, filter_xindices: typing.List[int]) -> "Token":
        """Create a new empty filter for each index value that is not already in use, and deletes each filter that is not mentioned in the list.

        :param filter_xindices: the list of indices of filters to be created on a port.
        :type filter_xindices: List[int]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, filter_xindices=filter_xindices))


@register_command
@dataclass
class PF_CREATE:
    """
    Creates an empty filter definition with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 212
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _filter_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Creates an empty filter definition with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._filter_xindex],
            ),
        )


@register_command
@dataclass
class PF_DELETE:
    """
    Deletes the filter definition with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 213
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _filter_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Delete the filter definition with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._filter_xindex],
            ),
        )


@register_command
@dataclass
class PF_ENABLE:
    """
    Whether a filter is currently active on a port. While a filter is enabled its
    condition cannot be changed, nor can any match term or length terms used by it.
    """

    code: typing.ClassVar[int] = 214
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _filter_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether the filter is enabled.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether the filter is enabled.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether a filter is currently active on the port.

        :return: whether the filter is enabled
        :rtype: PF_ENABLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._filter_xindex]))

    def set(self, on_off: OnOff) -> "Token":
        """Set whether a filter is currently active on the port.

        :param on_off: whether the filter is enabled
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._filter_xindex], on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable a filter on a port.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable a filter on a port.
    """


@register_command
@dataclass
class PF_COMMENT:
    """
    The description of a filter.
    """

    code: typing.ClassVar[int] = 215
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _filter_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the description of the filter.

    @dataclass(frozen=True)
    class GetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the description of the filter.

    def get(self) -> "Token[GetDataAttr]":
        """Get the description of a filter.

        :return: the description of the filter
        :rtype: PF_COMMENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._filter_xindex]))

    def set(self, comment: str) -> "Token":
        """Set the description of a filter. 

        :param comment: the description of the filter.
        :type comment: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._filter_xindex], comment=comment))


@register_command
@dataclass
class PF_CONDITION:
    """
        The boolean condition on the terms specifying when the filter is satisfied. The condition uses a canonical and-or-not expression on the match terms and length terms. The condition is specified using a number of compound terms, each encoded as an integer value specifying an arbitrary set of the match terms and length terms defined for the port. Each match or length term has a specific power-of-two value, and the set is encoded as the sum of the values for the contained terms:
        
        Value for match term ``[match_term_xindex] = 2^match_term_xindex``

        Value for length term ``[length_term_xindex] = 2^(length_term_xindex+16)``

        A compound term is true if all the match terms and length terms contained in it are true. This supports the and-part of the condition. If some compound term is satisfied, the condition as a whole is true.

        This is the or-part of the condition. The first few compound terms at the even positions (second, fourth, ...) are inverted, and all the contained match terms and length terms must be false at the same time that the those of the preceding compound term are true. This is the not-part of the condition.

        At the top level, a condition is a bunch of things or-ed together.

        ``<filter-condition> = <or-expr>`` 

        Two of the or-operands are *general*, two are 'simple'.

        ``<or-expr> =  <general-and-expr>  or  <general-and-expr>  or  <simple-and-expr>  or  <simple-and-expr>`` 

        A 'general' and-expression can include negated terms.

        ``<general-and-expr>  =  <term>  and  <term>  and ... and  not <term>  and ... and  not <term>`` 

        A 'simple' and-expression can only have non-negated terms.

        ``<simple-and-expr>   =  <term>  and  <term>  and ... and <term>``  

        ``<term>              =  <match-term>``
        
        ``<term>              =  <length-term>``  

        In practice, the simplest way to generate these encodings is to use the ValkyrieManager, which supports Boolean expressions using the operators ``&, |, and ~``, and simply query the chassis for the resulting script-level definition.

    """

    code: typing.ClassVar[int] = 216
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _filter_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        and_expression_0: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.
        and_not_expression_0: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match NOT terms AND length NOT terms.
        and_expression_1: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.
        and_not_expression_1: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match NOT terms AND length NOT terms.
        and_expression_2: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.
        and_expression_3: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.

    @dataclass(frozen=True)
    class GetDataAttr:
        and_expression_0: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.
        and_not_expression_0: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match NOT terms AND length NOT terms.
        and_expression_1: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.
        and_not_expression_1: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match NOT terms AND length NOT terms.
        and_expression_2: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.
        and_expression_3: XmpField[XmpInt] = XmpField(XmpInt)  # unsigned integer, encoding a compound term which is a set of the match terms AND length terms.

    def get(self) -> "Token[GetDataAttr]":
        """Get the condition on the terms specifying when the filter is satisfied.

        :return: and_expression_0, and_not_expression_0, and_expression_1, and_not_expression_1, and_expression_2, and and_expression_3.

        :rtype: Token[GetDataAttr]
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._filter_xindex]))

    def set(self, and_expression_0: int, and_not_expression_0: int, and_expression_1: int, and_not_expression_1: int, and_expression_2: int, and_expression_3: int) -> "Token":
        """_summary_

        :param and_expression_0: encoding a compound term which is a set of the match terms AND length terms.
        :type and_expression_0: int
        :param and_not_expression_0: encoding a compound term which is a set of the match NOT terms AND length NOT terms.
        :type and_not_expression_0: int
        :param and_expression_1: encoding a compound term which is a set of the match terms AND length terms.
        :type and_expression_1: int
        :param and_not_expression_1: encoding a compound term which is a set of the match NOT terms AND length NOT terms.
        :type and_not_expression_1: int
        :param and_expression_2: encoding a compound term which is a set of the match terms AND length terms.
        :type and_expression_2: int
        :param and_expression_3: encoding a compound term which is a set of the match terms AND length terms.
        :type and_expression_3: int

        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._filter_xindex], and_expression_0=and_expression_0, and_not_expression_0=and_not_expression_0, and_expression_1=and_expression_1, and_not_expression_1=and_not_expression_1, and_expression_2=and_expression_2, and_expression_3=and_expression_3))


@register_command
@dataclass
class PF_STRING:
    """
    The string representation of a filter.
    """

    code: typing.ClassVar[int] = 217
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _filter_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        string_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, the string representation of the filter.

    @dataclass(frozen=True)
    class GetDataAttr:
        string_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, the string representation of the filter.

    def get(self) -> "Token[GetDataAttr]":
        """Get the string representation of a filter.

        :return: the string representation of a filter
        :rtype: PF_STRING.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._filter_xindex]))

    def set(self, string_name: str) -> "Token":
        """Set the string representation of a filter. 

        :param string_name: the string representation of the filter
        :type string_name: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._filter_xindex], string_name=string_name))


