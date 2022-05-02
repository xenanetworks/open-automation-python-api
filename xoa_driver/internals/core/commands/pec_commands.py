#: Impairment Port Custom Distribution Commands

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
class PEC_INDICES:
    """
    The full list of which custom distributions which are defined for a port. These
    are the custom id values that are used for assigning the custom distributions to
    an impairment. Setting the value of this command creates a new custom
    distribution (default values) for each value that is not already in use, and
    deletes each custom distribution that is not mentioned in the list. The same can
    be accomplished one-custom-distribution-at-a-time using the PEC_VAL and
    PEC_DELETE commands.
    
    .. note::
        
        Custom distributions which are currently defined are not affected when mentioned in a PEC_INDICES set command. Custom distributions which are currently assigned to an impairment cannot be deleted and any attempt of deleting such a custom distribution using either :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_DELETE` or :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_INDICES` will result in an error.

    """

    code: typing.ClassVar[int] = 1610
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        indices: XmpField[XmpIntList] = XmpField(XmpIntList, climb=(0, 40))  # list of integers, a list of the indices to the custom distributions which are currently defined on that port, max 40 elements.
    
    @dataclass(frozen=True)
    class GetDataAttr:
        indices: XmpField[XmpIntList] = XmpField(XmpIntList, climb=(0, 40))  # list of integers, a list of the indices to the custom distributions which are currently defined on that port, max 40 elements.

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the indices to the custom distributions which are currently defined on that port. 

        :return: a list of the indices to the custom distributions which are currently defined on that port
        :rtype: PEC_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
    def set(self, indices: typing.List[int]) -> "Token":
        """Set a list of indices to create new custom distributions.

        :param indices: a list of indices to create new custom distributions
        :type indices: List[int]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=indices))


@register_command
@dataclass
class PEC_VAL:
    """
    Definition of custom distribution. Custom distributions can be defined for
    latency with 1024 entries and for non-latency impairments with 512 entries. Each
    port will maintain a list of defined custom distributions, identified by an
    CUST_ID. (Range: 1 - 40).
    """

    code: typing.ClassVar[int] = 1680
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _custom_distribution_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        linear: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, defines the way the FPGA RAM content is played out.
        symmetric: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, reserved for future use, must be set to OFF.
        entry_count: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, defines the number of entries in "dataX" (allowed value: 512,1024). NOTE: For Latency, 1024 entries are used, and for rest, 512 entries are used)
        data_x: XmpField[XmpLongList] = XmpField(XmpLongList)  # array of long integers, array size="num_entries", holds values to be filled in the RAM memory.

    @dataclass(frozen=True)
    class GetDataAttr:
        linear: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, defines the way the FPGA RAM content is played out.
        symmetric: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, reserved for future use, must be set to OFF.
        entry_count: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, defines the number of entries in "dataX" (allowed value: 512,1024). NOTE: For Latency, 1024 entries are used, and for rest, 512 entries are used)
        data_x: XmpField[XmpLongList] = XmpField(XmpLongList)  # array of long integers, array size="num_entries", holds values to be filled in the RAM memory.

    def get(self) -> "Token[GetDataAttr]":
        """Get the definition of custom distribution.

        :return: definition of custom distribution
        :rtype: PEC_VAL.GetDataAttr.
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._custom_distribution_xindex]))

    def set(self, linear: OnOff, symmetric: OnOff, entry_count: int, data_x: typing.List[int]) -> "Token":
        """Set the definition of custom distribution. Custom distributions can be defined for
        latency with 1024 entries and for non-latency impairments with 512 entries. Each
        port will maintain a list of defined custom distributions, identified by an
        CUST_ID. (Range: 1 - 40).

        :param linear: defines the way the FPGA RAM content is played out
        :type linear: OnOff
        :param symmetric: reserved for future use, must be set to 0.
        :type symmetric: OnOff
        :param entry_count: defines the number of entries in "dataX" (allowed value: 512,1024). For Latency, 1024 entries are used, and for rest, 512 entries are used)
        :type entry_count: int
        :param data_x: array size="num_entries", holds values to be filled in the RAM memory.
        :type data_x: List[int]
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._custom_distribution_xindex],
                linear=linear,
                symmetric=symmetric,
                entry_count=entry_count,
                data_x=data_x,
            ),
        )


@register_command
@dataclass
class PEC_COMMENT:
    """
    Defines the user-defined description string of a custom distribution.
    """

    code: typing.ClassVar[int] = 1681
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _custom_distribution_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the user-specified comment/description for the custom distribution.

    @dataclass(frozen=True)
    class GetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the user-specified comment/description for the custom distribution.

    def get(self) -> "Token[GetDataAttr]":
        """Get the user-defined description string of a custom distribution. 

        :return: the user-specified comment/description for the custom distribution.
        :rtype: PEC_COMMENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._custom_distribution_xindex]))

    def set(self, comment: str) -> "Token":
        """Set the user-defined description string of a custom distribution.  

        :param comment: the user-specified comment/description for the custom distribution.
        :type comment: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._custom_distribution_xindex], comment=comment))


@register_command
@dataclass
class PEC_DELETE:
    """
    Deletes the custom distribution definition.
    
    .. note::
    
        Once a customer has defined a customer distribution using :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_VAL`, it is defined until it is explicitly deleted.Only customer distributions which are not referenced by any impairments, can be deleted.

    """

    code: typing.ClassVar[int] = 1682
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _custom_distribution_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Deletes the custom distribution definition. 
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._custom_distribution_xindex],
            ),
        )


@register_command
@dataclass
class PEC_DISTTYPE:
    """
    Retrieves if a custom distribution is defined for latency or non-latency.
    
    .. note::
    
        Using :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_DISTTYPE` as set has no effect. The disttype is determined upon custom distribution creation and cannot be modified later. However, it is legal to issue the :class:`~xoa_driver.internals.core.commands.pec_commands.PEC_DISTTYPE` set command with no effect.
    """

    code: typing.ClassVar[int] = 1683
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _custom_distribution_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        latency_type: XmpField[XmpByte] = XmpField(XmpByte, choices=LatencyTypeCustomDist)  # byte, 0 indicates interpacket distribution, 1 indicates latency distribution.

    def get(self) -> "Token[GetDataAttr]":
        """Get the latency type of a custom distribution.

        :return: latency type of a custom distribution
        :rtype: PEC_DISTTYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._custom_distribution_xindex]))


