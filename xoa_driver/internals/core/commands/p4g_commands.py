#: L47 Port Connection Group Commands

from dataclasses import dataclass
import ipaddress
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
class P4G_INDICES:
    """
    The full list of Connection Groups on this port. These are the sub-index that
    are used for the parameters that specify TCP connection behavior.
    """

    code: typing.ClassVar[int] = 600
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        group_identifiers: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, list of indices identifying Connection Groups.

    @dataclass(frozen=True)
    class GetDataAttr:
        group_identifiers: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, list of indices identifying Connection Groups.

    def get(self) -> "Token[GetDataAttr]":
        """Get full list of Connection Groups on this port.

        :return: full list of Connection Groups on this port.
        :rtype: P4G_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, group_identifiers: typing.List[int]) -> "Token":
        """Create Connection Groups with the indices on the port. 

        :param group_identifiers: list of indices identifying Connection Groups.
        :type group_identifiers: typing.List[int]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, group_identifiers=group_identifiers))


@register_command
@dataclass
class P4G_CREATE:
    """
    Creates an empty Connection Group with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 601
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Creates an empty Connection Group with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
            ),
        )


@register_command
@dataclass
class P4G_DELETE:
    """
    Deletes a Connection Group with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 602
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Deletes a Connection Group with the specified sub-index value.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
            ),
        )


@register_command
@dataclass
class P4G_ENABLE:
    """
    Enable/disable/suppress a previously created Connection Group with the specified
    sub-index value.
    """

    code: typing.ClassVar[int] = 603
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOffWithSuppress)  # coded byte, specifies the state of the Connection Group.

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOffWithSuppress)  # coded byte, specifies the state of the Connection Group.

    def get(self) -> "Token[GetDataAttr]":
        """Get the state of a Connection Group on a port.

        :return: the state of a Connection Group on a port.
        :rtype: P4G_ENABLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, status: OnOffWithSuppress) -> "Token":
        """ Enable/disable/suppress a previously created Connection Group with the specified sub-index value.

        :param status: specifies the state of the Connection Group.
        :type status: OnOffWithSuppress
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], status=status))

    set_off = functools.partialmethod(set, OnOffWithSuppress.OFF)
    """Disable a Connection Group of with the specified index."""
    set_on = functools.partialmethod(set, OnOffWithSuppress.ON)
    """Enable a Connection Group of with the specified index."""
    set_suppress = functools.partialmethod(set, OnOffWithSuppress.SUPPRESS)
    """Suppress a Connection Group of with the specified index."""


@register_command
@dataclass
class P4G_COMMENT:
    """
    The description of a Connection Group.
    """

    code: typing.ClassVar[int] = 604
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the description of the Connection Group.

    @dataclass(frozen=True)
    class GetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the description of the Connection Group.

    def get(self) -> "Token[GetDataAttr]":
        """Get the description of a Connection Group.

        :return: the description of a Connection Group.
        :rtype: P4G_COMMENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, comment: str) -> "Token":
        """Set the description of a Connection Group.

        :param comment: the description of a Connection Group.
        :type comment: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], comment=comment))


@register_command
@dataclass
class P4G_CLEAR_COUNTERS:
    """
    Clears all run-time statistics for the Connection Group.
    """

    code: typing.ClassVar[int] = 605
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clears all run-time statistics for the Connection Group.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
            ),
        )


@register_command
@dataclass
class P4G_ROLE:
    """
    Specifies the client or server role for this Connection Group. A server
    passively waits for the clients to establish connections.
    """

    code: typing.ClassVar[int] = 606
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        role: XmpField[XmpByte] = XmpField(XmpByte, choices=Role)  # coded byte, specifies the role of the Connection Group.

    @dataclass(frozen=True)
    class GetDataAttr:
        role: XmpField[XmpByte] = XmpField(XmpByte, choices=Role)  # coded byte, specifies the role of the Connection Group.

    def get(self) -> "Token[GetDataAttr]":
        """Get the role of the Connection Group.

        :return: the role of the Connection Group.
        :rtype: P4G_ROLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, role: Role) -> "Token":
        """Set the role of the Connection Group.

        :param role: the role of the Connection Group.
        :type role: Role
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], role=role))

    set_client = functools.partialmethod(set, Role.CLIENT)
    """Set the role of the Connection Group to Client."""
    set_server = functools.partialmethod(set, Role.SERVER)
    """Set the role of the Connection Group to Server."""


@register_command
@dataclass
class P4G_CLIENT_RANGE:
    """
    Specifies a number of client sockets (ip address, port number)
    """

    code: typing.ClassVar[int] = 607
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports
        max_address_count: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, the maximum number of ip addresses that this Connection Group will use, when connection incarnation is set to REINCARNATE

    @dataclass(frozen=True)
    class GetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports
        max_address_count: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, the maximum number of ip addresses that this Connection Group will use, when connection incarnation is set to REINCARNATE

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of client sockets (ip address, port number)

        :return: the number of client sockets (ip address, port number)
        :rtype: P4G_CLIENT_RANGE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ipv4_address: typing.Union[str, int, ipaddress.IPv4Address], address_count: int, start_port: int, port_count: int, max_address_count: int) -> "Token":
        """Set the number of client sockets (ip address, port number)

        :param ipv4_address: the start IP address of the address range
        :type ipv4_address: typing.Union[str, int, ipaddress.IPv4Address]
        :param address_count: the number of IP addresses
        :type address_count: int
        :param start_port: the starting port number of the port range
        :type start_port: int
        :param port_count: the number of ports
        :type port_count: int
        :param max_address_count: the maximum number of IP addresses that this Connection Group will use, when connection incarnation is set to ``REINCARNATE``
        :type max_address_count: int
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
                ipv4_address=ipv4_address,
                address_count=address_count,
                start_port=start_port,
                port_count=port_count,
                max_address_count=max_address_count,
            ),
        )


@register_command
@dataclass
class P4G_SERVER_RANGE:
    """
    Specifies a number of server sockets (ip address, port number)
    """

    code: typing.ClassVar[int] = 608
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports

    @dataclass(frozen=True)
    class GetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of server sockets (ip address, port number)

        :return: the number of server sockets (ip address, port number)
        :rtype: P4G_SERVER_RANGE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ipv4_address: typing.Union[str, int, ipaddress.IPv4Address], address_count: int, start_port: int, port_count: int) -> "Token":
        """Set the number of server sockets (ip address, port number)

        :param ipv4_address: the start IP address of the address range
        :type ipv4_address: typing.Union[str, int, ipaddress.IPv4Address]
        :param address_count: the number of IP addresses
        :type address_count: int
        :param start_port: the starting port number of the port range
        :type start_port: int
        :param port_count: the number of ports
        :type port_count: int
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
                ipv4_address=ipv4_address,
                address_count=address_count,
                start_port=start_port,
                port_count=port_count,
            ),
        )


@register_command
@dataclass
class P4G_LP_TIME_SCALE:
    """
    Specifies the time scale of the load profile.
    """

    code: typing.ClassVar[int] = 609
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        timescale: XmpField[XmpByte] = XmpField(XmpByte, choices=Timescale)  # coded byte, specifying the time scale.

    @dataclass(frozen=True)
    class GetDataAttr:
        timescale: XmpField[XmpByte] = XmpField(XmpByte, choices=Timescale)  # coded byte, specifying the time scale.

    def get(self) -> "Token[GetDataAttr]":
        """Get the time scale of the load profile.

        :return: the time scale of the load profile.
        :rtype: P4G_LP_TIME_SCALE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, timescale: Timescale) -> "Token":
        """Set the time scale of the load profile.

        :param timescale: specifying the time scale.
        :type timescale: Timescale
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], timescale=timescale))

    set_msecs = functools.partialmethod(set, Timescale.MSECS)
    """Set the time scale of the load profile to Milliseconds."""
    set_seconds = functools.partialmethod(set, Timescale.SECONDS)
    """Set the time scale of the load profile to Seconds."""
    set_minutes = functools.partialmethod(set, Timescale.MINUTES)
    """Set the time scale of the load profile to Minutes."""
    set_hours = functools.partialmethod(set, Timescale.HOURS)
    """Set the time scale of the load profile to Hours."""


@register_command
@dataclass
class P4G_LP_SHAPE:
    """
    Specifies a load profile time duration. Time is measured from the beginning of
    the test when ``P€G_TRAFFIC`` is set to ``ON``.
    """

    code: typing.ClassVar[int] = 610
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        star_time: XmpField[XmpInt] = XmpField(XmpInt)  # integer, ramp-up start time.
        rampup_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, ramp-up phase duration.
        steady_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, steady phase duration.
        rampdown_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, ramp-down phase duration.

    @dataclass(frozen=True)
    class GetDataAttr:
        star_time: XmpField[XmpInt] = XmpField(XmpInt)  # integer, ramp-up start time.
        rampup_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, ramp-up phase duration.
        steady_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, steady phase duration.
        rampdown_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, ramp-down phase duration.

    def get(self) -> "Token[GetDataAttr]":
        """Get the load profile time duration.

        :return: the load profile time duration
        :rtype: P4G_LP_SHAPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, star_time: int, rampup_duration: int, steady_duration: int, rampdown_duration: int) -> "Token":
        """Set the load profile time duration.

        :param star_time: ramp-up start time
        :type star_time: int
        :param rampup_duration: ramp-up phase duration
        :type rampup_duration: int
        :param steady_duration: steady phase duration
        :type steady_duration: int
        :param rampdown_duration: ramp-down phase duration
        :type rampdown_duration: int
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
                star_time=star_time,
                rampup_duration=rampup_duration,
                steady_duration=steady_duration,
                rampdown_duration=rampdown_duration,
            ),
        )


@register_command
@dataclass
class P4G_NAT:
    """
    Specify whether to support DUT Source NAT functionality. NAT should be enabled on both Client and Server ports that belong to the same Connection Group.
    """

    code: typing.ClassVar[int] = 611
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifying whether to enable NAT

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, specifying whether to enable NAT

    def get(self) -> "Token[GetDataAttr]":
        """Get whether to support DUT Source NAT functionality.

        :return: whether to support DUT Source NAT functionality.
        :rtype: P4G_NAT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, on_off: OnOff) -> "Token":
        """Set whether to support DUT Source NAT functionality.

        :param on_off: specifying whether to enable Source NAT support
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable source NAT support."""
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable source NAT support."""


@register_command
@dataclass
class P4G_TCP_RTT_VALUE:
    """
    Returns values that can be used to calculate the RTT value of all connections in
    a Connection Group.
    """

    code: typing.ClassVar[int] = 612
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        local_rtt_sum: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, accumulated RTT value (microsecond) in previous 200 milliseconds
        local_rtt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of RTT value accumulated in local_rtt_sum
        global_rtt_sum: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, accumulated RTT value (microsecond) since start of test
        global_rtt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of RTT values accumulated in global_rtt_sum

    def get(self) -> "Token[GetDataAttr]":
        """Get values that can be used to calculate the RTT value of all connections in a Connection Group.

        :return: values that can be used to calculate the RTT value of all connections in a Connection Group.
        :rtype: P4G_TCP_RTT_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_STATE_CURRENT:
    """
    Returns a list of the current TCP state counters. The counters returned
    corresponds the the following TCP states:
    
    * CLOSED
    * LISTEN
    * SYN_SENT
    * TCP_SYN_RCVD
    * ESTABLISHED
    * FIN_WAIT_1
    * FIN_WAIT_2
    * CLOSE_WAIT
    * CLOSING
    * LAST_ACK
    * TIME_WAIT

    """

    code: typing.ClassVar[int] = 613
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        closed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        listen: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        syn_sent: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        syn_rcvd: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        established: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        fin_wait_1: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        fin_wait_2: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        close_wait: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        closing: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        last_ack: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        time_wait: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the current TCP state counters

        :return: a list of the current TCP state counters
        :rtype: P4G_TCP_STATE_CURRENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_STATE_TOTAL:
    """
    Returns a list of the total TCP state counters. The counters returned
    corresponds the the following TCP states:

    * CLOSED
    * LISTEN
    * SYN_SENT
    * TCP_SYN_RCVD
    * ESTABLISHED
    * FIN_WAIT_1
    * FIN_WAIT_2
    * CLOSE_WAIT
    * CLOSING
    * LAST_ACK
    * TIME_WAIT

    """

    code: typing.ClassVar[int] = 614
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        closed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        listen: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        syn_sent: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        syn_rcvd: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        established: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        fin_wait_1: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        fin_wait_2: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        close_wait: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        closing: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        last_ack: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        time_wait: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the total TCP state counters.

        :return: a list of the total TCP state counters
        :rtype: P4G_TCP_STATE_TOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_STATE_RATE:
    """
    Returns a list of the TCP state rates measured in connections/second. The
    counters returned corresponds the the following TCP state rates:

    * CLOSED
    * LISTEN
    * SYN_SENT
    * TCP_SYN_RCVD
    * ESTABLISHED
    * FIN_WAIT_1
    * FIN_WAIT_2
    * CLOSE_WAIT
    * CLOSING
    * LAST_ACK
    * TIME_WAIT

    """

    code: typing.ClassVar[int] = 615
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        closed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        listen: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        syn_sent: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        syn_rcvd: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        established: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        fin_wait_1: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        fin_wait_2: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        close_wait: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        closing: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        last_ack: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        time_wait: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TCP state rates measured in connections/second.

        :return: a list of the TCP state rates measured in connections/second
        :rtype: P4G_TCP_STATE_RATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_RX_PAYLOAD_COUNTERS:
    """
    Returns a list of the TCP Rx payload counters.
    """

    code: typing.ClassVar[int] = 616
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        total_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of total TCP payload bytes received
        total_byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of total TCP payload bytes/second received
        good_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of good TCP payload bytes received
        good_byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of good TCP payload bytes/second received

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TCP Rx payload counters.

        :return: a list of the TCP Rx payload counters.
        :rtype: P4G_TCP_RX_PAYLOAD_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_TX_PAYLOAD_COUNTERS:
    """
    Returns a list of the TCP Tx payload counters.
    """

    code: typing.ClassVar[int] = 617
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        total_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of total TCP payload bytes transmitted
        total_byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of total TCP payload bytes/second transmitted
        good_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of good TCP payload bytes transmitted
        good_byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of good TCP payload bytes/second transmitted

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TCP Tx payload counters.

        :return: a list of the TCP Tx payload counters.
        :rtype: P4G_TCP_TX_PAYLOAD_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_RETRANSMIT_COUNTERS:
    """
    Returns a list of TCP retransmission counters.
    """

    code: typing.ClassVar[int] = 618
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        rx_duplicate_ack_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of duplicate ACK received
        rx_ooo_segment_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of out-of-order segments received
        fast_retrans_event_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of fast-retransmit events occurred
        fast_retrans_segment_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of segments retransmitted during fast-retransmit
        rto_retrans_event_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of timer based retransmit events occurred
        syn_retrans_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of SYN retransmitted
        fin_retrans_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of FIN retransmitted

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of TCP retransmission counters.

        :return: a list of TCP retransmission counters.
        :rtype: P4G_TCP_RETRANSMIT_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_ERROR_COUNTERS:
    """
    Returns a list of TCP error counters.
    """

    code: typing.ClassVar[int] = 619
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        rx_reset_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP RESET received
        tx_reset_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP RESET transmitted
        window_full_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP window full encountered
        max_syn_retrans_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of connections reset due to maximum number of SYN retransmits
        max_retrans_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of connections reset due to maximum number of RTO retransmits
        local_reset_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of connections reset locally by transmitting a TCP RESET
        peer_reset_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of connections reset by peer
        seg_not_send_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP segments not send due to exhausted Tx resources
        rx_zero_window_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of Zero Window ACKs received from the peer

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of TCP error counters.

        :return: a list of TCP error counters.
        :rtype: P4G_TCP_ERROR_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_IP_DS_TYPE:
    """
    Configure the mode of the DS field of the IP header of this Connection Group.
    """

    code: typing.ClassVar[int] = 620
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ds_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MSSType)  # coded byte, specifying how to fill out the DS field

    @dataclass(frozen=True)
    class GetDataAttr:
        ds_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MSSType)  # coded byte, specifying how to fill out the DS field

    def get(self) -> "Token[GetDataAttr]":
        """Get the value of the DS field of the IP header of this Connection Group.

        :return: the mode of the DS field
        :rtype: P4G_IP_DS_TYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ds_type: MSSType) -> "Token":
        """Set the value of the DS field of the IP header of this Connection Group.

        :param ds_type: specifying how to fill out the DS field
        :type ds_type: MSSType
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ds_type=ds_type))

    set_fixed = functools.partialmethod(set, MSSType.FIXED)
    """Use fixed value for DS."""
    set_increment = functools.partialmethod(set, MSSType.INCREMENT)
    """Use incrementing values for DS."""
    set_random = functools.partialmethod(set, MSSType.RANDOM)
    """Use pseudorandom values for DS."""


@register_command
@dataclass
class P4G_IP_DS_VALUE:
    """
    Specify the (FIXED) value used for DS.
    """

    code: typing.ClassVar[int] = 621
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ds_value: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, the fixed DS value to be used

    @dataclass(frozen=True)
    class GetDataAttr:
        ds_value: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, the fixed DS value to be used

    def get(self) -> "Token[GetDataAttr]":
        """Get the fixed DS value.

        :return: value of the DS field
        :rtype: P4G_IP_DS_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ds_value: str) -> "Token":
        """Set the fixed DS value.

        :param ds_value: the fixed DS value to be used
        :type ds_value: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ds_value=ds_value))


@register_command
@dataclass
class P4G_IP_DS_MASK:
    """
    Specify a bit mask to be applied to the DS field. If the fixed value is fixed,
    the current (calculated) value is curr, and the mask is mask, then the effective
    DS will be calculated as follows: (fixed AND (NOT mask)) OR (curr AND mask) or
    in C syntax (fixed & (~mask)) | (curr & mask)
    """

    code: typing.ClassVar[int] = 622
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ds_mask: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, the DS mask to be used.

    @dataclass(frozen=True)
    class GetDataAttr:
        ds_mask: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, the DS mask to be used.

    def get(self) -> "Token[GetDataAttr]":
        """Get the bit mask to be applied to the DS field.

        :return: the bit mask to be applied to the DS field
        :rtype: P4G_IP_DS_MASK.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ds_mask: str) -> "Token":
        """Set the bit mask to be applied to the DS field.

        :param ds_mask: the DS mask to be used.
        :type ds_mask: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ds_mask=ds_mask))


@register_command
@dataclass
class P4G_IP_DS_MINMAX:
    """
    Configure the min and max values of the range for the calculated part of the DS
    value. Both values are included in the range. Relevant when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_IP_DS_TYPE` is set to ``INCREMENT`` or ``RANDOM``.
    """

    code: typing.ClassVar[int] = 623
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ds_min: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, minimum value for the calculated part of DS
        ds_max: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, maximum value for the calculated part of DS

    @dataclass(frozen=True)
    class GetDataAttr:
        ds_min: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, minimum value for the calculated part of DS
        ds_max: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, maximum value for the calculated part of DS

    def get(self) -> "Token[GetDataAttr]":
        """Get the min and max values of the range for the calculated part of the DS value.

        :return: the min and max values of the range for the calculated part of the DS value.
        :rtype: P4G_IP_DS_MINMAX.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ds_min: str, ds_max: str) -> "Token":
        """Set the min and max values of the range for the calculated part of the DS value.

        :param ds_min: minimum value for the calculated part of DS
        :type ds_min: str
        :param ds_max: maximum value for the calculated part of DS
        :type ds_max: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ds_min=ds_min, ds_max=ds_max))


@register_command
@dataclass
class P4G_IP_DS_STEP:
    """
    Specifies the incrementing step size for the calculated part of the DS value.
    Relevant when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_IP_DS_TYPE` is set to ``INCREMENT``.
    """

    code: typing.ClassVar[int] = 624
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ds_step: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, the incrementing step size for DS.

    @dataclass(frozen=True)
    class GetDataAttr:
        ds_step: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, the incrementing step size for DS.

    def get(self) -> "Token[GetDataAttr]":
        """Get the incrementing step size for the calculated part of the DS value.

        :return: the incrementing step size for the calculated part of the DS value.
        :rtype: P4G_IP_DS_STEP.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ds_step: str) -> "Token":
        """Set the incrementing step size for the calculated part of the DS value.

        :param ds_step: the incrementing step size for DS.
        :type ds_step: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ds_step=ds_step))


@register_command
@dataclass
class P4G_TCP_MSS_TYPE:
    """
    Specifies the Maximum Segment size (MSS) type for a Connection Group. The MSS can
    either be fixed size identical for all connections in the Connection Group,
    incrementing or random. The individual MSS for a specific connection is always
    constant once the incrementing or random value has been created. Refer to
    :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_MSS_MINMAX` 
    command for information on how to configure min and max values.
    """

    code: typing.ClassVar[int] = 625
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mss_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MSSType)  # coded byte, specifying how MSS is set

    @dataclass(frozen=True)
    class GetDataAttr:
        mss_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MSSType)  # coded byte, specifying how MSS is set

    def get(self) -> "Token[GetDataAttr]":
        """Get the Maximum Segment size (MSS) type for a Connection Group.

        :return: the Maximum Segment size (MSS) type for a Connection Group
        :rtype: P4G_TCP_MSS_TYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mss_type: MSSType) -> "Token":
        """Set the Maximum Segment size (MSS) type for a Connection Group.

        :param mss_type: specifying how MSS is set
        :type mss_type: MSSType
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mss_type=mss_type))

    set_fixed = functools.partialmethod(set, MSSType.FIXED)
    """Use fixed value for TCP MSS."""
    set_increment = functools.partialmethod(set, MSSType.INCREMENT)
    """Use incrementing value for TCP MSS."""
    set_random = functools.partialmethod(set, MSSType.RANDOM)
    """Use pseudorandom value for TCP MSS."""


@register_command
@dataclass
class P4G_TCP_MSS_MINMAX:
    """
    Configure the min and max values of the range for MSS. Both values are
    included in the range. Relevant when P4G_TCP_MSS_TYPE is set to INCREMENT or
    RANDOM.
    """

    code: typing.ClassVar[int] = 626
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mss_min: XmpField[XmpInt] = XmpField(XmpInt)  # integer, minimum value of MSS
        mss_max: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum value of MSS

    @dataclass(frozen=True)
    class GetDataAttr:
        mss_min: XmpField[XmpInt] = XmpField(XmpInt)  # integer, minimum value of MSS
        mss_max: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum value of MSS

    def get(self) -> "Token[GetDataAttr]":
        """Get the min and max values of the range for TCP MSS.

        :return: the min and max values of the range for TCP MSS
        :rtype: P4G_TCP_MSS_MINMAX.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mss_min: int, mss_max: int) -> "Token":
        """Set the min and max values of the range for TCP MSS.

        :param mss_min: minimum value of MSS
        :type mss_min: int
        :param mss_max: maximum value of MSS
        :type mss_max: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mss_min=mss_min, mss_max=mss_max))


@register_command
@dataclass
class P4G_TCP_MSS_VALUE:
    """
    Configure the fixed MSS value. Relevant when P4G_TCP_MSS_TYPE is set to FIXED.
    """

    code: typing.ClassVar[int] = 627
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mss: XmpField[XmpInt] = XmpField(XmpInt)  # integer, fixed value of MSS

    @dataclass(frozen=True)
    class GetDataAttr:
        mss: XmpField[XmpInt] = XmpField(XmpInt)  # integer, fixed value of MSS

    def get(self) -> "Token[GetDataAttr]":
        """Get the fixed MSS value of the Connection Group.

        :return: the fixed MSS value of the Connection Group.
        :rtype: P4G_TCP_MSS_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mss: int) -> "Token":
        """Set the fixed MSS value of the Connection Group.

        :param mss: the fixed value of MSS (in bytes)
        :type mss: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mss=mss))


@register_command
@dataclass
class P4G_TCP_WINDOW_SIZE:
    """
    Configure the value of the TCP RWND.
    """

    code: typing.ClassVar[int] = 628
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        window_size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, window size in bytes

    @dataclass(frozen=True)
    class GetDataAttr:
        window_size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, window size in bytes

    def get(self) -> "Token[GetDataAttr]":
        """Get the value of the TCP RWND.

        :return: the value of the TCP RWND.
        :rtype: P4G_TCP_WINDOW_SIZE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, window_size: int) -> "Token":
        """Set the value of the TCP RWND.

        :param window_size: RWND size in bytes
        :type window_size: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], window_size=window_size))


@register_command
@dataclass
class P4G_TCP_DUP_THRES:
    """
    Configure the value of the TCP duplicate ACK threshold.
    """

    code: typing.ClassVar[int] = 629
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        threshold: XmpField[XmpByte] = XmpField(XmpByte)  # byte, duplicate ACK threshold - must be larger than 0

    @dataclass(frozen=True)
    class GetDataAttr:
        threshold: XmpField[XmpByte] = XmpField(XmpByte)  # byte, duplicate ACK threshold - must be larger than 0

    def get(self) -> "Token[GetDataAttr]":
        """Get the value of the TCP duplicate ACK threshold.

        :return: the value of the TCP duplicate ACK threshold.
        :rtype: P4G_TCP_DUP_THRES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, threshold: int) -> "Token":
        """Set the value of the TCP duplicate ACK threshold.

        :param threshold: duplicate ACK threshold - must be larger than 0
        :type threshold: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], threshold=threshold))


@register_command
@dataclass
class P4G_TCP_SYN_RTO:
    """
    Configure the value of the TCP SYN retransmission timeout, max retries and max backoff.
    """

    code: typing.ClassVar[int] = 630
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        retrans_timeout: XmpField[XmpInt] = XmpField(XmpInt)  # integer, SYN retransmission timeout [milliseconds] - must be larger than 0
        retry_count: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum SYN retransmission retries - must be larger than 0
        backoff: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum SYN retransmission backoff

    @dataclass(frozen=True)
    class GetDataAttr:
        retrans_timeout: XmpField[XmpInt] = XmpField(XmpInt)  # integer, SYN retransmission timeout [milliseconds] - must be larger than 0
        retry_count: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum SYN retransmission retries - must be larger than 0
        backoff: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum SYN retransmission backoff

    def get(self) -> "Token[GetDataAttr]":
        """Get the value of the TCP SYN retransmission timeout, max retries and max backoff.

        :return: the value of the TCP SYN retransmission timeout, max retries and max backoff.
        :rtype: P4G_TCP_SYN_RTO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, retrans_timeout: int, retry_count: int, backoff: int) -> "Token":
        """Set the value of the TCP SYN retransmission timeout, max retries and max backoff.

        :param retrans_timeout: SYN retransmission timeout [milliseconds] - must be larger than 0
        :type retrans_timeout: int
        :param retry_count: maximum SYN retransmission retries - must be larger than 0
        :type retry_count: int
        :param backoff: maximum SYN retransmission backoff
        :type backoff: int
        """
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, indices=[self._group_xindex], retrans_timeout=retrans_timeout, retry_count=retry_count, backoff=backoff
            ),
        )


@register_command
@dataclass
class P4G_TCP_RTO:
    """
    Configure the value of the TCP retransmission timeout, max retries and max backoff.
    """

    code: typing.ClassVar[int] = 631
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        rto_type: XmpField[XmpByte] = XmpField(XmpByte, choices=RTOType)  # coded byte, specifying RTO type
        retrans_timeout: XmpField[XmpInt] = XmpField(XmpInt)  # integer, retransmission timeout [milliseconds] - must be larger than 0
        retry_count: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum retransmission retries - must be larger than 0
        backoff: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum retransmission backoff

    @dataclass(frozen=True)
    class GetDataAttr:
        type: XmpField[XmpByte] = XmpField(XmpByte, choices=RTOType)  # coded byte, specifying RTO type
        retrans_timeout: XmpField[XmpInt] = XmpField(XmpInt)  # integer, retransmission timeout [milliseconds] - must be larger than 0
        retry_count: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum retransmission retries - must be larger than 0
        backoff: XmpField[XmpByte] = XmpField(XmpByte)  # byte, maximum retransmission backoff

    def get(self) -> "Token[GetDataAttr]":
        """Get the value of the TCP retransmission timeout, max retries and max backoff.

        :return: the value of the TCP retransmission timeout, max retries and max backoff.
        :rtype: P4G_TCP_RTO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, rto_type: RTOType, retrans_timeout: int, retry_count: int, backoff: int) -> "Token":
        """Set the value of the TCP retransmission timeout, max retries and max backoff.

        :param rto_type: specifying RTO type
        :type rto_type: RTOType
        :param retrans_timeout: retransmission timeout [milliseconds] - must be larger than 0
        :type retrans_timeout: int
        :param retry_count: maximum retransmission retries - must be larger than 0
        :type retry_count: int
        :param backoff: maximum retransmission backoff
        :type backoff: int
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
                rto_type=rto_type,
                retrans_timeout=retrans_timeout,
                retry_count=retry_count,
                backoff=backoff,
            ),
        )

    set_static = functools.partialmethod(set, RTOType.STATIC)
    """RTO is constant as configured"""
    set_dynamic = functools.partialmethod(set, RTOType.DYNAMIC)
    """RTO is dynamic and depending on round trip time (RTT)"""


@register_command
@dataclass
class P4G_UDP_PACKET_SIZE_TYPE:
    """
    Specifies the UDP packet size type for a Connection Group. The packet size can either
    be fixed size identical for all connections in the Connection Group,
    incrementing or random. The individual packet size for a specific connection is
    always constant once the incrementing or random value has been created. Refer to
    :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_UDP_PACKET_SIZE_MINMAX` command for information on how to configure min and max values.
    """

    code: typing.ClassVar[int] = 632
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        packet_size_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MSSType)  # coded byte, specifying how UDP packet size is set

    @dataclass(frozen=True)
    class GetDataAttr:
        packet_size_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MSSType)  # coded byte, specifying how UDP packet size is set

    def get(self) -> "Token[GetDataAttr]":
        """Get the UDP packet size type for the Connection Group.

        :return: the UDP packet size for the Connection Group.
        :rtype: P4G_UDP_PACKET_SIZE_TYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, packet_size_type: MSSType) -> "Token":
        """Set the UDP packet size type for the Connection Group.

        :param packet_size_type: specifying how UDP packet size is set
        :type packet_size_type: MSSType
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], packet_size_type=packet_size_type))

    set_fixed = functools.partialmethod(set, MSSType.FIXED)
    """Use fixed value for UDP packet size."""
    set_increment = functools.partialmethod(set, MSSType.INCREMENT)
    """Use incrementing value for UDP packet size."""
    set_random = functools.partialmethod(set, MSSType.RANDOM)
    """Use pseudorandom value for UDP packet size."""


@register_command
@dataclass
class P4G_UDP_PACKET_SIZE_MINMAX:
    """
    Configure the minimum and maximum values of the range for UDP packet size. Both
    values are included in the range. Relevant when P4G_UDP_PACKET_SIZE_TYPE is set
    to INCREMENT or RANDOM.
    """

    code: typing.ClassVar[int] = 633
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        size_min: XmpField[XmpInt] = XmpField(XmpInt)  # integer, minimum value of UDP packet size
        size_max: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum value of UDP packet size

    @dataclass(frozen=True)
    class GetDataAttr:
        size_min: XmpField[XmpInt] = XmpField(XmpInt)  # integer, minimum value of UDP packet size
        size_max: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum value of UDP packet size

    def get(self) -> "Token[GetDataAttr]":
        """Get the minimum and maximum values of the range for UDP packet size.

        :return: the minimum and maximum values of the range for UDP packet size.
        :rtype: P4G_UDP_PACKET_SIZE_MINMAX.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, size_min: int, size_max: int) -> "Token":
        """Set the minimum and maximum values of the range for UDP packet size.

        :param size_min: the minimum value of UDP packet size
        :type size_min: int
        :param size_max: the maximum value of UDP packet size
        :type size_max: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], size_min=size_min, size_max=size_max))


@register_command
@dataclass
class P4G_UDP_PACKET_SIZE_VALUE:
    """
    Configure the fixed UDP packet size value. Relevant when
    P4G_UDP_PACKET_SIZE_TYPE is set to FIXED.
    """

    code: typing.ClassVar[int] = 634
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, fixed value of UDP packet size

    @dataclass(frozen=True)
    class GetDataAttr:
        size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, fixed value of UDP packet size

    def get(self) -> "Token[GetDataAttr]":
        """Get the fixed UDP packet size value.

        :return: the fixed UDP packet size value
        :rtype: P4G_UDP_PACKET_SIZE_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, size: int) -> "Token":
        """Set the fixed UDP packet size value.

        :param size: the fixed value of UDP packet size
        :type size: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], size=size))


@register_command
@dataclass
class P4G_TCP_CONGESTION_MODE:
    """
    Configure the TCP congestion control algorithm.
    """

    code: typing.ClassVar[int] = 635
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        congestion_type: XmpField[XmpByte] = XmpField(XmpByte, choices=CongestionType)  # coded byte, specifying congestion algorithm type

    @dataclass(frozen=True)
    class GetDataAttr:
        congestion_type: XmpField[XmpByte] = XmpField(XmpByte, choices=CongestionType)  # coded byte, specifying congestion algorithm type

    def get(self) -> "Token[GetDataAttr]":
        """Get the TCP congestion control algorithm.

        :return: the TCP congestion control algorithm.
        :rtype: P4G_TCP_CONGESTION_MODE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, congestion_type: CongestionType) -> "Token":
        """Set the TCP congestion control algorithm.

        :param congestion_type: specifying congestion algorithm type
        :type congestion_type: CongestionType
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], congestion_type=congestion_type))

    set_none = functools.partialmethod(set, CongestionType.NONE)
    """Disable congestion control."""
    set_reno = functools.partialmethod(set, CongestionType.RENO)
    """Enable RENO congestion control algorithm."""
    set_new_reno = functools.partialmethod(set, CongestionType.NEW_RENO)
    """Enable New RENO congestion control algorithm."""


@register_command
@dataclass
class P4G_TCP_WINDOW_SCALING:
    """
    Enable window scaling for the Connection Group. Note to use windows scaling it
    need to be enabled in both the client and server Connection Group. .
    """

    code: typing.ClassVar[int] = 636
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # code byte, specifying whether to enable window scaling or not
        factor: XmpField[XmpByte] = XmpField(XmpByte)  # integer, default value is 0 and maximum value is 14 - ignored if window scaling is not enabled

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # code byte, specifying whether to enable window scaling or not
        factor: XmpField[XmpByte] = XmpField(XmpByte)  # integer, default value is 0 and maximum value is 14 - ignored if window scaling is not enabled

    def get(self) -> "Token[GetDataAttr]":
        """Get TCP window scaling settings for the Connection Group.

        :return: TCP window scaling settings for the Connection Group.
        :rtype: P4G_TCP_WINDOW_SCALING.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, on_off: YesNo, factor: int) -> "Token":
        """Set TCP window scaling settings for the Connection Group.

        :param on_off: specifying whether to enable window scaling or not
        :type on_off: YesNo
        :param factor: default value is 0 and maximum value is 14 - ignored if window scaling is not enabled
        :type factor: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], on_off=on_off, factor=factor))

    set_no = functools.partialmethod(set, YesNo.NO)
    """Disable TCP window scaling."""
    set_yes = functools.partialmethod(set, YesNo.YES)
    """Enable TCP window scaling."""


@register_command
@dataclass
class P4G_TCP_RTO_MINMAX:
    """
    Configure the min and max values of the TCP retransmission timeout, when rto type
    is set to dynamic. If the calculated rto fall outside the interval, the value is
    clamped to the min or max value.
    """

    code: typing.ClassVar[int] = 637
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        rto_min: XmpField[XmpInt] = XmpField(XmpInt)  # integer, min retransmission timeout [us] - must be larger than 0 and less than max.
        rto_max: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max retransmission timeout [us] - must be larger than 0 and greater than min.

    @dataclass(frozen=True)
    class GetDataAttr:
        rto_min: XmpField[XmpInt] = XmpField(XmpInt)  # integer, min retransmission timeout [us] - must be larger than 0 and less than max.
        rto_max: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max retransmission timeout [us] - must be larger than 0 and greater than min.

    def get(self) -> "Token[GetDataAttr]":
        """Get the min and max values of the TCP retransmission timeout.

        :return: the min and max values of the TCP retransmission timeout
        :rtype: P4G_TCP_RTO_MINMAX.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, rto_min: int, rto_max: int) -> "Token":
        """Set the min and max values of the TCP retransmission timeout.

        :param rto_min: min retransmission timeout [us] - must be larger than 0 and less than max.
        :type rto_min: int
        :param rto_max: max retransmission timeout [us] - must be larger than 0 and greater than min.
        :type rto_max: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], rto_min=rto_min, rto_max=rto_max))


@register_command
@dataclass
class P4G_TCP_RTO_PROLONGED_MODE:
    """
    Configure TCP retransmission prolonged mode. When enabled, TCP will, after
    exceeding max number of retransmission retries, continue trying retransmit until
    success, whereafter it will operate normally.
    """

    code: typing.ClassVar[int] = 638
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=IsEnabled)  # byte, specifying whether to enable/disable prolonged retransmission mode
        timeout: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # retransmission timeout in milliseconds, when prolonged mode is enabled. when mode is set to 0, the value of the timeout is ignored, when mode is set to 1, the value of the timeout may not be 0

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=IsEnabled)  # byte, specifying whether to enable/disable prolonged retransmission mode
        timeout: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # retransmission timeout in milliseconds, when prolonged mode is enabled. when mode is set to 0, the value of the timeout is ignored, when mode is set to 1, the value of the timeout may not be 0

    def get(self) -> "Token[GetDataAttr]":
        """Get TCP retransmission prolonged mode.

        :return: TCP retransmission prolonged mode
        :rtype: P4G_TCP_RTO_PROLONGED_MODE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: IsEnabled, timeout: int) -> "Token":
        """Set TCP retransmission prolonged mode.

        :param mode: specifying whether to enable/disable prolonged retransmission mode
        :type mode: IsEnabled
        :param timeout: retransmission timeout in milliseconds, when prolonged mode is enabled. When ``mode`` is set to 0, the value of the timeout is ignored. When ``mode`` is set to 1, the value of the timeout may not be 0.
        :type timeout: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode, timeout=timeout))

    set_disable = functools.partialmethod(set, IsEnabled.DISABLE)
    """Disable TCP retransmission prolonged mode."""
    set_enable = functools.partialmethod(set, IsEnabled.ENABLE)
    """Enable TCP retransmission prolonged mode."""


@register_command
@dataclass
class P4G_TCP_ICWND_CALC_METHOD:
    """
    Select the algorithm to calculate the TCP initial congestion window (ICWND).
    """

    code: typing.ClassVar[int] = 639
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        method: XmpField[XmpByte] = XmpField(XmpByte, choices=AlgorithmMethod)  # coded byte, specifying the algorithm
        factor: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, factor to multiply the senders MSS with, when method is set to 'FIXED_FACTOR'. Otherwise the value is ignored.

    @dataclass(frozen=True)
    class GetDataAttr:
        method: XmpField[XmpByte] = XmpField(XmpByte, choices=AlgorithmMethod)  # coded byte, specifying the algorithm
        factor: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, factor to multiply the senders MSS with, when method is set to 'FIXED_FACTOR'. Otherwise the value is ignored.

    def get(self) -> "Token[GetDataAttr]":
        """Get the algorithm to calculate the TCP initial congestion window (ICWND).

        :return: the algorithm to calculate the TCP initial congestion window (ICWND).
        :rtype: P4G_TCP_ICWND_CALC_METHOD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, method: AlgorithmMethod, factor: int) -> "Token":
        """Set the algorithm to calculate the TCP initial congestion window (ICWND).

        :param method: specifying the algorithm
        :type method: AlgorithmMethod
        :param factor: factor to multiply the senders MSS with, when method is set to ``FIXED_FACTOR``. Otherwise the value is ignored.
        :type factor: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], method=method, factor=factor))

    set_rfc5681 = functools.partialmethod(set, AlgorithmMethod.RFC5681)
    """ICWND is set according to RFC5681."""
    set_rfc2581 = functools.partialmethod(set, AlgorithmMethod.RFC2581)
    """ICWND is set according to RFC2581"""
    set_fixed_factor = functools.partialmethod(set, AlgorithmMethod.FIXED_FACTOR)
    """ICWND is set to a FACTOR * SMSS (Sender's MSS)"""


@register_command
@dataclass
class P4G_TCP_ISSTHRESH:
    """
    Configure the TCP initial slow start threshold (ISSTHRESH).
    """

    code: typing.ClassVar[int] = 640
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=AutoOrManual)  # coded byte, specifying TCP initial slow start mode
        threshold: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of bytes, value ignored when mode is set to MANUAL

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=AutoOrManual)  # coded byte, specifying TCP initial slow start mode
        threshold: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of bytes, value ignored when mode is set to MANUAL

    def get(self) -> "Token[GetDataAttr]":
        """Get the TCP initial slow start threshold (ISSTHRESH).

        :return: the TCP initial slow start threshold (ISSTHRESH).
        :rtype: P4G_TCP_ISSTHRESH.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: AutoOrManual, threshold: int) -> "Token":
        """Set the TCP initial slow start threshold (ISSTHRESH).

        :param mode: specifying TCP initial slow start mode
        :type mode: AutoOrManual
        :param threshold: number of bytes, value ignored when mode is set to ``MANUAL``
        :type threshold: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode, threshold=threshold))

    set_automatic = functools.partialmethod(set, AutoOrManual.AUTOMATIC)
    """TCP initial slow start mode set to Automatic"""
    set_manual = functools.partialmethod(set, AutoOrManual.MANUAL)
    """TCP initial slow start mode set to Manual"""


@register_command
@dataclass
class P4G_TCP_ACK_FREQUENCY:
    """
    Number of received packets before a pure-ACK is sent.
    """

    code: typing.ClassVar[int] = 641
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        packets_before_ack: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, number of received packets before an ACK is sent, range between 1 and 255, default 1. When set to 1, every packet is ACKed

    @dataclass(frozen=True)
    class GetDataAttr:
        packets_before_ack: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, number of received packets before an ACK is sent, range between 1 and 255, default 1. When set to 1, every packet is ACKed

    def get(self) -> "Token[GetDataAttr]":
        """Get the configuration of the number of received packets before a pure-ACK is sent.

        :return: the configuration of the number of received packets before a pure-ACK is sent.
        :rtype: P4G_TCP_ACK_FREQUENCY.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, packets_before_ack: int) -> "Token":
        """Set the configuration of the number of received packets before a pure-ACK is sent.

        :param packets_before_ack: number of received packets before an ACK is sent, range between 1 and 255, default 1. When set to 1, every packet is ACKed.
        :type packets_before_ack: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], packets_before_ack=packets_before_ack))


@register_command
@dataclass
class P4G_TCP_ACK_TIMEOUT:
    """
    Delayed ACK timeout in microsecondsA pure ACK for the last RX packet will be
    sent after :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ACK_TIMEOUT` microseconds in case it cannot be sent by other means, ie. a number of packets received since last ACK is less than :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ACK_FREQUENCY` and there is no TX packets to sent (to piggy-back an ACK)
    """

    code: typing.ClassVar[int] = 642
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ack_timeout: XmpField[XmpInt] = XmpField(XmpInt)  # integer, timeout value in microseconds, default 200000.

    @dataclass(frozen=True)
    class GetDataAttr:
        ack_timeout: XmpField[XmpInt] = XmpField(XmpInt)  # integer, timeout value in microseconds, default 200000.

    def get(self) -> "Token[GetDataAttr]":
        """Get the Delayed ACK timeout.

        :return: the Delayed ACK timeout 
        :rtype: P4G_TCP_ACK_TIMEOUT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ack_timeout: int) -> "Token":
        """Set the Delayed ACK timeout.

        :param ack_timeout: timeout value in microseconds, default 200000.
        :type ack_timeout: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ack_timeout=ack_timeout))


@register_command
@dataclass
class P4G_L2_CLIENT_MAC:
    """
    Configure the client MAC address. This is either a single static MAC
    address or an embedding of the four byte IPv4 address into the lower 4 bytes of
    the 6 byte MAC address.
    """

    code: typing.ClassVar[int] = 644
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address specified as hexadecimal
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=EmbedIP)  # coded byte, whether to embed the IP address or not

    @dataclass(frozen=True)
    class GetDataAttr:
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address specified as hexadecimal
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=EmbedIP)  # coded byte, whether to embed the IP address or not

    def get(self) -> "Token[GetDataAttr]":
        """Get the client MAC address.

        :return: the client MAC address
        :rtype: P4G_L2_CLIENT_MAC.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mac_address: str, mode: EmbedIP) -> "Token":
        """Set the client MAC address.

        :param mac_address: the MAC address specified as hexadecimal
        :type mac_address: str
        :param mode: whether to embed the IP address in MAC
        :type mode: EmbedIP
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mac_address=mac_address, mode=mode))

    set_dont_embed_ip = functools.partialmethod(set, mode=EmbedIP.DONT_EMBED_IP)
    """Not embed IP address in MAC address."""
    set_embed_ip = functools.partialmethod(set, mode=EmbedIP.EMBED_IP)
    """Embed IP address in MAC address."""


@register_command
@dataclass
class P4G_L2_SERVER_MAC:
    """
    Configure the server MAC address. This is either a single static MAC
    address or an embedding of the four byte IPv4 address into the lower 4 bytes of
    the 6 byte MAC address.
    """

    code: typing.ClassVar[int] = 645
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address specified as hexadecimal
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=EmbedIP)  # coded byte, whether to embed the ip address or not

    @dataclass(frozen=True)
    class GetDataAttr:
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address specified as hexadecimal
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=EmbedIP)  # coded byte, whether to embed the ip address or not

    def get(self) -> "Token[GetDataAttr]":
        """Get the server MAC address.

        :return: the server MAC address
        :rtype: P4G_L2_SERVER_MAC.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mac_address: str, mode: EmbedIP) -> "Token":
        """Set the server MAC address.

        :param mac_address: the MAC address specified as hexadecimal
        :type mac_address: str
        :param mode: whether to embed the IP address in MAC
        :type mode: EmbedIP
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mac_address=mac_address, mode=mode))

    set_dont_embed_ip = functools.partialmethod(set, mode=EmbedIP.DONT_EMBED_IP)
    """Not embed IP address in MAC address."""
    set_embed_ip = functools.partialmethod(set, mode=EmbedIP.EMBED_IP)
    """Embed IP address in MAC address."""


@register_command
@dataclass
class P4G_L2_USE_ADDRESS_RES:
    """
    Specify whether to use ARP and NDP to resolve hardware (MAC) addresses in the
    ``pre_run`` phase.
    """

    code: typing.ClassVar[int] = 646
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        is_enabled: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, specifying whether to use ARP and NDP or not

    @dataclass(frozen=True)
    class GetDataAttr:
        is_enabled: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, specifying whether to use ARP and NDP or not

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of using ARP and NDP to resolve hardware (MAC) addresses.

        :return: specifying whether to use ARP and NDP to resolve hardware (MAC) addresses.
        :rtype: P4G_L2_USE_ADDRESS_RES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, is_enabled: YesNo) -> "Token":
        """Set the status of using ARP and NDP to resolve hardware (MAC) addresses.

        :param is_enabled: specifying whether to use ARP and NDP to resolve hardware (MAC) addresses.
        :type is_enabled: YesNo
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], is_enabled=is_enabled))

    set_no = functools.partialmethod(set, YesNo.NO)
    """Disable using ARP and NDP to resolve hardware (MAC) addresses."""
    set_yes = functools.partialmethod(set, YesNo.YES)
    """Enable using ARP and NDP to resolve hardware (MAC) addresses."""


@register_command
@dataclass
class P4G_L2_USE_GW:
    """
    Specify whether to use the resolved default gateway's MAC address as the destination MAC address in the packets.
    """

    code: typing.ClassVar[int] = 647
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        is_enabled: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, specifying whether to use gateway MAC or not

    @dataclass(frozen=True)
    class GetDataAttr:
        is_enabled: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, specifying whether to use gateway MAC or not

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of using the resolved default gateway's MAC address as the destination MAC address in the packets.

        :return: the status of using the resolved default gateway's MAC address as the destination MAC address in the packets
        :rtype: P4G_L2_USE_GW.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, is_enabled: YesNo) -> "Token":
        """Set the status of using the resolved default gateway's MAC address as the destination MAC address in the packets.

        :param is_enabled: specifying whether to use gateway's MAC address as the destination MAC address in the packets.
        :type is_enabled: YesNo
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], is_enabled=is_enabled))

    set_no = functools.partialmethod(set, YesNo.NO)
    """Disable using gateway's MAC address as the destination MAC address."""
    set_yes = functools.partialmethod(set, YesNo.YES)
    """Enable using gateway's MAC address as the destination MAC address."""


@register_command
@dataclass
class P4G_L2_GW:
    """
    Specify a default gateway for IPv4.
    """

    code: typing.ClassVar[int] = 648
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, ip address of gateway
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address of the gateway

    @dataclass(frozen=True)
    class GetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, ip address of gateway
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address of the gateway

    def get(self) -> "Token[GetDataAttr]":
        """Get the settings of the default gateway for IPv4.

        :return: IPv4 address and MAC address of the default gateway for IPv4.
        :rtype: P4G_L2_GW.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ipv4_address: typing.Union[str, int, ipaddress.IPv4Address], mac_address: str) -> "Token":
        """Set a default gateway for IPv4.

        :param ipv4_address: IPv5 address of the gateway
        :type ipv4_address: typing.Union[str, int, ipaddress.IPv4Address]
        :param mac_address: the MAC address of the gateway
        :type mac_address: str
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ipv4_address=ipv4_address, mac_address=mac_address)
        )


@register_command
@dataclass
class P4G_L2_IPV6_GW:
    """
    Specify a default gateway for IPv6.
    """

    code: typing.ClassVar[int] = 649
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ipv6_address: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, the 16 bytes of IPv6 address of gateway
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address of the gateway

    @dataclass(frozen=True)
    class GetDataAttr:
        ipv6_address: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, the 16 bytes of IPv6 address of gateway
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, the MAC address of the gateway

    def get(self) -> "Token[GetDataAttr]":
        """Get the settings of the default gateway for IPv6.

        :return: IPv6 address and MAC address of the default gateway for IPv6.
        :rtype: P4G_L2_IPV6_GW.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ipv6_address: typing.Union[str, int, ipaddress.IPv6Address], mac_address: str) -> "Token":
        """Set the default gateway for IPv6.

        :param ipv6_address: the 16 bytes of IPv6 address of gateway
        :type ipv6_address: typing.Union[str, int, ipaddress.IPv6Address]
        :param mac_address: the MAC address of the gateway
        :type mac_address: str
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ipv6_address=ipv6_address, mac_address=mac_address)
        )


@register_command
@dataclass
class P4G_TEST_APPLICATION:
    """
    Configure the application layer mode. This command affects whether TCP payload is generated.
    
    * ``NONE`` means that TCP connections are created according to the client and server ranges, and ramped up/down as specified in the load profile. But no payload is transmitted.
    
    * ``RAW`` differs from ``NONE`` in that it transmits payload when the TCP connection is established.

    * ``REPLAY`` refers to PCAP replay.

    """

    code: typing.ClassVar[int] = 650
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        behavior: XmpField[XmpByte] = XmpField(XmpByte, choices=ApplicationLayerBehavior)  # coded byte, application behavior

    @dataclass(frozen=True)
    class GetDataAttr:
        behavior: XmpField[XmpByte] = XmpField(XmpByte, choices=ApplicationLayerBehavior)  # coded byte, application behavior

    def get(self) -> "Token[GetDataAttr]":
        """Get the application layer mode.

        :return: the application layer mode
        :rtype: P4G_TEST_APPLICATION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, behavior: ApplicationLayerBehavior) -> "Token":
        """Set he application layer mode.

        :param behavior: the application layer mode
        :type behavior: ApplicationLayerBehavior
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], behavior=behavior))

    set_none = functools.partialmethod(set, ApplicationLayerBehavior.NONE)
    """Application layer is set to connection-only."""
    set_raw = functools.partialmethod(set, ApplicationLayerBehavior.RAW)
    """Application layer is set to connection + payload."""
    set_replay = functools.partialmethod(set, ApplicationLayerBehavior.REPLAY)
    """Application layer is set to pcap replay."""


@register_command
@dataclass
class P4G_RAW_TEST_SCENARIO:
    """
    Configure the traffic direction scenario for RAW mode.
    """

    code: typing.ClassVar[int] = 651
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        scenario: XmpField[XmpByte] = XmpField(XmpByte, choices=TrafficScenario)  # coded byte, traffic scenario

    @dataclass(frozen=True)
    class GetDataAttr:
        scenario: XmpField[XmpByte] = XmpField(XmpByte, choices=TrafficScenario)  # coded byte, traffic scenario

    def get(self) -> "Token[GetDataAttr]":
        """Get the traffic scenario for RAW mode.

        :return: the traffic scenario for RAW mode.
        :rtype: P4G_RAW_TEST_SCENARIO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, scenario: TrafficScenario) -> "Token":
        """Set the traffic scenario for RAW mode.

        :param scenario: traffic scenario
        :type scenario: TrafficScenario
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], scenario=scenario))

    set_download = functools.partialmethod(set, TrafficScenario.DOWNLOAD)
    """Server transmits payload to client."""
    set_upload = functools.partialmethod(set, TrafficScenario.UPLOAD)
    """Client transmits payload to server."""
    set_both = functools.partialmethod(set, TrafficScenario.BOTH)
    """Payload is transmitted in both directions."""
    set_echo = functools.partialmethod(set, TrafficScenario.ECHO)
    """Client transmits payload to server, server echoes the payload back"""


@register_command
@dataclass
class P4G_RAW_PAYLOAD_TYPE:
    """
    Specify the payload generation method.
    """

    code: typing.ClassVar[int] = 652
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        gen_method: XmpField[XmpByte] = XmpField(XmpByte, choices=PayloadGenerationMethod)  # coded byte, payload generation method

    @dataclass(frozen=True)
    class GetDataAttr:
        gen_method: XmpField[XmpByte] = XmpField(XmpByte, choices=PayloadGenerationMethod)  # coded byte, payload generation method

    def get(self) -> "Token[GetDataAttr]":
        """Get the payload generation method.

        :return: payload generation method
        :rtype: P4G_RAW_PAYLOAD_TYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, gen_method: PayloadGenerationMethod) -> "Token":
        """Set the payload generation method.

        :param gen_method: payload generation method
        :type gen_method: PayloadGenerationMethod
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], gen_method=gen_method))

    set_fixed = functools.partialmethod(set, PayloadGenerationMethod.FIXED)
    """Payload has a fixed value - as specified by the :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD` command."""
    set_increment = functools.partialmethod(set, PayloadGenerationMethod.INCREMENT)
    """Payload consist of incrementing bytes."""
    set_random = functools.partialmethod(set, PayloadGenerationMethod.RANDOM)
    """Payload consists of pseudo random bytes with a repeat cycle of 1 MB."""
    set_longrandom = functools.partialmethod(set, PayloadGenerationMethod.LONGRANDOM)
    """Payload consists of pseudo random bytes with a repeat cycle of 4 GB."""


@register_command
@dataclass
class P4G_RAW_PAYLOAD_TOTAL_LEN:
    """
    Configure the total amount of payload to transmit on one connection.
    """

    code: typing.ClassVar[int] = 653
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, generation mode.
        length: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, size of the payload

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, generation mode.
        length: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, size of the payload

    def get(self) -> "Token[GetDataAttr]":
        """Get the total amount of payload to transmit on one connection.

        :return: the total amount of payload to transmit on one connection
        :rtype: P4G_RAW_PAYLOAD_TOTAL_LEN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: InfiniteOrFinite, length: int) -> "Token":
        """Set the total amount of payload to transmit on one connection.

        :param mode: generation mode.
        :type mode: InfiniteOrFinite
        :param length: size of the payload
        :type length: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode, length=length))

    set_infinite = functools.partialmethod(set, InfiniteOrFinite.INFINITE)
    """Generates payload as long as test is running."""
    set_finite = functools.partialmethod(set, InfiniteOrFinite.FINITE)
    """Stop generating payload after length bytes are transmitted."""


@register_command
@dataclass
class P4G_RAW_PAYLOAD:
    """
    Specify raw payload as hex bytes. This command can be called several times to build
    a custom payload.
    """

    code: typing.ClassVar[int] = 654
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the offset in the payload buffer where data is to be written
        length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of bytes to write
        content: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, specifying the payload

    @dataclass(frozen=True)
    class GetDataAttr:
        offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the offset in the payload buffer where data is to be written
        length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of bytes to write
        content: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, specifying the payload

    def get(self) -> "Token[GetDataAttr]":
        """Get the payload as hex bytes.

        :return: the payload as hex bytes
        :rtype: P4G_RAW_PAYLOAD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, offset: int, length: int, content: str) -> "Token":
        """Set the payload as hex bytes.

        :param offset: the offset in the payload buffer where data is to be written
        :type offset: int
        :param length: number of bytes to write
        :type length: int
        :param content: specifying the payload
        :type content: str
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], offset=offset, length=length, content=content)
        )


@register_command
@dataclass
class P4G_RAW_PAYLOAD_REPEAT_LEN:
    """
    Specify the length of the raw payload, which is defined by one or more :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD` commands, to repeat.
    
    :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_REPEAT_LEN` number of bytes will be repeated until :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_TOTAL_LEN` bytes are transmitted on the connection.
    """

    code: typing.ClassVar[int] = 655
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying the repeat length of the custom payload

    @dataclass(frozen=True)
    class GetDataAttr:
        length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying the length of the custom payload

    def get(self) -> "Token[GetDataAttr]":
        """Get the length of the raw payload to repeat.

        :return: the length of the raw payload to repeat
        :rtype: P4G_RAW_PAYLOAD_REPEAT_LEN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, length: int) -> "Token":
        """Set the length of the raw payload to repeat.

        :param length: the length of the raw payload to repeat
        :type length: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], length=length))


@register_command
@dataclass
class P4G_RAW_HAS_DOWNLOAD_REQ:
    """
    Specify whether the server waits for a request from the client before it starts transmitting.
    
    .. note::
    
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

    """

    code: typing.ClassVar[int] = 656
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, expect request before sending payload or not

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, expect request before sending payload or not

    def get(self) -> "Token[GetDataAttr]":
        """Get whether the server waits for a request from the client before it starts transmitting.

        :return: whether the server waits for a request from the client before it starts transmitting.
        :rtype: P4G_RAW_HAS_DOWNLOAD_REQ.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, on_off: YesNo) -> "Token":
        """Set whether the server waits for a request from the client before it starts transmitting.

        :param on_off: whether the server waits for a request from the client before it starts transmitting.
        :type on_off: YesNo
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], on_off=on_off))

    set_no = functools.partialmethod(set, YesNo.NO)
    """The server does not wait for a request from the client before it starts transmitting."""
    set_yes = functools.partialmethod(set, YesNo.YES)
    """The server waits for a request from the client before it starts transmitting."""


@register_command
@dataclass
class P4G_RAW_CLOSE_CONN:
    """
    Specify how to close TCP connection when all payload has been transmitted.
    
    In raw test scenario ``DOWNLOAD``, the server can close the connection, when all payload has been transmitted.
    
    In raw test scenario ``UPLOAD``, the client can close the connection, when all payload has been transmitted. In any case, both server and client Connection Groups must be configured with the same value of this parameter.
    
    In raw test scenario ``BOTH`` (bidirectional), this parameter is N/A and will be ignored.
    
    In a transaction scenario, where :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_HAS_DOWNLOAD_REQ` is set to ``YES``, both client and server can close the connection, when the last transaction has been completed.
    
    When :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_INCARNATION` is set to ``IMMORTAL`` or ``REINCARNATE``, and this command is set to ``NONE``, connections will be closed after 'connection lifetime', set by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_LIFETIME`.
    
    .. note::
    
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

    """

    code: typing.ClassVar[int] = 657
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        who_close: XmpField[XmpByte] = XmpField(XmpByte, choices=WhoClose)  # coded byte, specifying who closes the connection

    @dataclass(frozen=True)
    class GetDataAttr:
        who_close: XmpField[XmpByte] = XmpField(XmpByte, choices=WhoClose)  # coded byte, specifying who closes the connection

    def get(self) -> "Token[GetDataAttr]":
        """Get how to close TCP connection when all payload has been transmitted.

        :return: how to close TCP connection when all payload has been transmitted
        :rtype: P4G_RAW_CLOSE_CONN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, who_close: WhoClose) -> "Token":
        """Set how to close TCP connection when all payload has been transmitted.

        :param who_close: specifying how to close TCP connection
        :type who_close: WhoClose
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], who_close=who_close))

    set_none = functools.partialmethod(set, WhoClose.NONE)
    """Keep the connection open after last byte is transmitted."""
    set_client = functools.partialmethod(set, WhoClose.CLIENT)
    """Client closes the connection after last byte is receiver/transmitted."""
    set_server = functools.partialmethod(set, WhoClose.SERVER)
    """Server closes the connection after last byte is transmitted."""


@register_command
@dataclass
class P4G_RAW_UTILIZATION:
    """
    Specify the link layer bandwidth utilization for all the generated traffic from
    the specified Raw Connection Group.
    """

    code: typing.ClassVar[int] = 658
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        utilization: XmpField[XmpInt] = XmpField(XmpInt)  # integer, utilization specified in ppm.

    @dataclass(frozen=True)
    class GetDataAttr:
        utilization: XmpField[XmpInt] = XmpField(XmpInt)  # integer, utilization specified in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get the link layer bandwidth utilization for all the generated traffic from the specified Raw Connection Group.

        :return: the link layer bandwidth utilization for all the generated traffic from the specified Raw Connection Group.
        :rtype: P4G_RAW_UTILIZATION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, utilization: int) -> "Token":
        """Set the link layer bandwidth utilization for all the generated traffic from the specified Raw Connection Group.

        :param utilization: utilization specified in ppm.
        :type utilization: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], utilization=utilization))


@register_command
@dataclass
class P4G_RAW_DOWNLOAD_REQUEST:
    """
    Specify the content of the download request sent by the client and expected by the server as hex bytes.
    
    .. note::
    
        This parameter is N/A when P4G_L4_PROTOCOL is configured as UDP.

    """

    code: typing.ClassVar[int] = 659
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying the number of bytes to write. Maximum request length is 1024 bytes.
        content: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, specifying the request content.

    @dataclass(frozen=True)
    class GetDataAttr:
        length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying the number of bytes to write. Maximum request length is 1024 bytes.
        content: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, specifying the request content.

    def get(self) -> "Token[GetDataAttr]":
        """Get the content of the download request sent by the client and expected by the server as hex bytes.

        :return: the content of the download request sent by the client and expected by the server as hex bytes.
        :rtype: P4G_RAW_DOWNLOAD_REQUEST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, length: int, content: str) -> "Token":
        """Set the content of the download request sent by the client and expected by the server as hex bytes.

        :param length: specifying the number of bytes to write. Maximum request length is 1024 bytes.
        :type length: int
        :param content: specifying the request content.
        :type content: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], length=length, content=content))


@register_command
@dataclass
class P4G_RAW_TX_DURING_RAMP:
    """
    Specify if TCP payload transmission should take place during ramp-up and ramp-down. 
    
    .. note::
    
        For UDP connections payload transmission will always take place during ramp-up and ramp-down, and this parameter is therefore N/A.

    """

    code: typing.ClassVar[int] = 660
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        should_close_conn_ramp_up: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, whether TCP payload transmission should take place during ramp up.
        should_close_conn_ramp_down: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, whether TCP payload transmission should take place during ramp down.

    @dataclass(frozen=True)
    class GetDataAttr:
        should_close_conn_ramp_up: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, whether TCP payload transmission should take place during ramp up.
        should_close_conn_ramp_down: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, whether TCP payload transmission should take place during ramp down.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether TCP payload transmission should take place during ramp-up and ramp-down. 

        :return: whether TCP payload transmission should take place during ramp-up and ramp-down. 
        :rtype: P4G_RAW_TX_DURING_RAMP.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, should_close_conn_ramp_up: YesNo, should_close_conn_ramp_down: YesNo) -> "Token":
        """Set whether TCP payload transmission should take place during ramp-up and ramp-down. 

        :param should_close_conn_ramp_up: whether TCP payload transmission should take place during ramp-up.
        :type should_close_conn_ramp_up: YesNo
        :param should_close_conn_ramp_down: whether TCP payload transmission should take place during ramp-down.
        :type should_close_conn_ramp_down: YesNo
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
                should_close_conn_ramp_up=should_close_conn_ramp_up,
                should_close_conn_ramp_down=should_close_conn_ramp_down,
            ),
        )


@register_command
@dataclass
class P4G_RAW_TX_TIME_OFFSET:
    """
    Specify a time offset to the transmit start and stop time, if :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TX_DURING_RAMP` is set to ``NO`` for ramp-up and ramp-down respectively.
    """

    code: typing.ClassVar[int] = 661
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        start_offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specify time in milliseconds from ramp-up has completed to start of payload transmit.
        stop_offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specify time in milliseconds from stop of payload transmit to start of ramp-down.

    @dataclass(frozen=True)
    class GetDataAttr:
        start_offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specify time in milliseconds from ramp-up has completed to start of payload transmit.
        stop_offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specify time in milliseconds from stop of payload transmit to start of ramp-down.

    def get(self) -> "Token[GetDataAttr]":
        """Get the time offset to the transmit start and stop time.

        :return: the time offset to the transmit start and stop time
        :rtype: P4G_RAW_TX_TIME_OFFSET.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, start_offset: int, stop_offset: int) -> "Token":
        """Set the time offset to the transmit start and stop time.

        :param start_offset: specify time in milliseconds from ramp-up has completed to start of payload transmit.
        :type start_offset: int
        :param stop_offset: specify time in milliseconds from stop of payload transmit to start of ramp-down.
        :type stop_offset: int
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], start_offset=start_offset, stop_offset=stop_offset)
        )


@register_command
@dataclass
class P4G_RAW_BURSTY_TX:
    """
    Enables or disables bursty transmission.
    """

    code: typing.ClassVar[int] = 662
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        bursty: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether bursty transmission is on or off.

    @dataclass(frozen=True)
    class GetDataAttr:
        bursty: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether bursty transmission is on or off.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether to use bursty transmission.

        :return: whether to use bursty transmission.
        :rtype: P4G_RAW_BURSTY_TX.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, bursty: OnOff) -> "Token":
        """Set whether to use bursty transmission.

        :param bursty: whether bursty transmission is on or off.
        :type bursty: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], bursty=bursty))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable bursty transmission."""
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable bursty transmission."""


@register_command
@dataclass
class P4G_RAW_BURSTY_CONF:
    """
    Specifies active and inactive periods of bursty transmission in milliseconds. The burst period starts with the active part.
    """

    code: typing.ClassVar[int] = 663
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        active_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifies the duration in milliseconds of the active part of the burst period.
        inactive_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifies the duration in milliseconds of the inactive part of the burst period.

    @dataclass(frozen=True)
    class GetDataAttr:
        active_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifies the duration in milliseconds of the active part of the burst period.
        inactive_duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifies the duration in milliseconds of the inactive part of the burst period.

    def get(self) -> "Token[GetDataAttr]":
        """Get active and inactive periods of bursty transmission in milliseconds.

        :return: active and inactive period of bursty transmission in milliseconds.
        :rtype: P4G_RAW_BURSTY_CONF.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, active_duration: int, inactive_duration: int) -> "Token":
        """Set active and inactive periods of bursty transmission in milliseconds.

        :param active_duration: specifies the duration in milliseconds of the active part of the burst period.
        :type active_duration: int
        :param inactive_duration: specifies the duration in milliseconds of the inactive part of the burst period.
        :type inactive_duration: int
        """
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, indices=[self._group_xindex], active_duration=active_duration, inactive_duration=inactive_duration
            ),
        )


@register_command
@dataclass
class P4G_VLAN_ENABLE:
    """
    Specify whether to insert a VLAN tag header upon transmit.
    """

    code: typing.ClassVar[int] = 664
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, specifying whether to enable VLAN tag

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, specifying whether to enable VLAN tag

    def get(self) -> "Token[GetDataAttr]":
        """Get whether to insert a VLAN tag header upon transmit.

        :return: whether to insert a VLAN tag header upon transmit.
        :rtype: P4G_VLAN_ENABLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, on_off: OnOff) -> "Token":
        """Set whether to insert a VLAN tag header upon transmit.

        :param on_off: specifying whether to enable VLAN tag
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable VLAN tag insertion upon transmit."""
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable VLAN tag insertion upon transmit."""


@register_command
@dataclass
class P4G_VLAN_TCI:
    """
    Specify the VLAN TCI.
    """

    code: typing.ClassVar[int] = 665
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        tci: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes, specifying the 16 bit TCI

    @dataclass(frozen=True)
    class GetDataAttr:
        tci: XmpField[XmpHex2] = XmpField(XmpHex2)  # two hex bytes, specifying the 16 bit TCI

    def get(self) -> "Token[GetDataAttr]":
        """Get the VLAN TCI value.

        :return: the VLAN TCI value.
        :rtype: P4G_VLAN_TCI.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, tci: str) -> "Token":
        """Set the VLAN TCI value.

        :param tci: specifying the 16 bit TCI
        :type tci: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], tci=tci))


@register_command
@dataclass
class P4G_TIME_HIST_CONF:
    """
    Sets the start value and the interval size for the time histograms (:class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ESTABLISH_HIST` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_CLOSE_HIST`).
    """

    code: typing.ClassVar[int] = 666
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in us
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in us

    @dataclass(frozen=True)
    class GetDataAttr:
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in us
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in us

    def get(self) -> "Token[GetDataAttr]":
        """Get the start value and the interval size for the time histograms.

        :return: the start value and the interval size for the time histograms.
        :rtype: P4G_TIME_HIST_CONF.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, start: int, interval: int) -> "Token":
        """Set the start value and the interval size for the time histograms.

        :param start: start value of first histogram interval in microseconds
        :type start: int
        :param interval: histogram interval size in microseconds
        :type interval: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], start=start, interval=interval))


@register_command
@dataclass
class P4G_PAYLOAD_HIST_CONF:
    """
    Sets the start value and the interval size for the payload histograms.
    """

    code: typing.ClassVar[int] = 667
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes

    @dataclass(frozen=True)
    class GetDataAttr:
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes

    def get(self) -> "Token[GetDataAttr]":
        """Get the start value and the interval size for the payload histograms.

        :return: the start value and the interval size for the payload histograms.
        :rtype: P4G_PAYLOAD_HIST_CONF.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, start: int, interval: int) -> "Token":
        """Set the start value and the interval size for the payload histograms.

        :param start: start value of first histogram interval in bytes
        :type start: int
        :param interval: histogram interval size in bytes
        :type interval: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], start=start, interval=interval))


@register_command
@dataclass
class P4G_TRANSACTION_HIST_CONF:
    """
    Sets the start value and the interval size for the transaction histogram (:class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_APP_TRANSACTION_HIST`).
    """

    code: typing.ClassVar[int] = 668
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size

    @dataclass(frozen=True)
    class GetDataAttr:
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size

    def get(self) -> "Token[GetDataAttr]":
        """Get the start value and the interval size for the transaction histogram.

        :return: the start value and the interval size for the transaction histogram
        :rtype: P4G_TRANSACTION_HIST_CONF.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, start: int, interval: int) -> "Token":
        """Set the start value and the interval size for the transaction histogram.

        :param start: tart value of first histogram interval
        :type start: int
        :param interval: histogram interval size
        :type interval: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], start=start, interval=interval))


@register_command
@dataclass
class P4G_RAW_RX_PAYLOAD_LEN:
    """
    Specify the length of the payload the Client should expect to receive before sending the next download request to the Server. Should be configured identical to the :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD_TOTAL_LEN` for the Server. If mode is set to INFINITE, effectively no request/response repetitions will be performed.
    
    .. note::
    
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

    """

    code: typing.ClassVar[int] = 669
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, specifying the payload length mode
        length: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, number of payload bytes the client should receive before sending the next request, if mode is FINITE.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, specifying the payload length mode
        length: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, number of payload bytes the client should receive before sending the next request, if mode is FINITE.

    def get(self) -> "Token[GetDataAttr]":
        """Get the length of the payload the Client should expect to receive before sending the next download request to the Server.

        :return: the length of the payload the Client should expect to receive before sending the next download request to the Server.
        :rtype: P4G_RAW_RX_PAYLOAD_LEN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: InfiniteOrFinite, length: int) -> "Token":
        """Set the length of the payload the Client should expect to receive before sending the next download request to the Server.

        :param mode: specifying the payload length mode
        :type mode: InfiniteOrFinite
        :param length: number of payload bytes the client should receive before sending the next request, if mode is ``FINITE``.
        :type length: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode, length=length))

    set_infinite = functools.partialmethod(set, InfiniteOrFinite.INFINITE)
    """Expects payload as long as test is running."""
    set_finite = functools.partialmethod(set, InfiniteOrFinite.FINITE)
    """Expects a number of bytes of payload defined by the command."""


@register_command
@dataclass
class P4G_RAW_REQUEST_REPEAT:
    """
    Specify the number of request/response transactions to perform - if :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_HAS_DOWNLOAD_REQ` is set to ``YES``.
    
    .. note::
        
        This parameter is N/A when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_L4_PROTOCOL` is configured as UDP.

    """

    code: typing.ClassVar[int] = 670
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, specifying the transaction mode.
        repeat: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of request/response transactions to perform , if mode is FINITE.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, specifying the transaction mode.
        repeat: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of request/response transactions to perform , if mode is FINITE.

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of request/response transactions to perform.

        :return: the number of request/response transactions to perform
        :rtype: P4G_RAW_REQUEST_REPEAT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: InfiniteOrFinite, repeat: int) -> "Token":
        """Set the number of request/response transactions to perform.

        :param mode: specifying the transaction mode.
        :type mode: InfiniteOrFinite
        :param repeat: number of request/response transactions to perform , if mode is ``FINITE``.
        :type repeat: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode, repeat=repeat))

    set_infinite = functools.partialmethod(set, InfiniteOrFinite.INFINITE)
    """Repeats request/response transactions as long as test is running."""
    set_finite = functools.partialmethod(set, InfiniteOrFinite.FINITE)
    """Stop generating request/response transactions after a number of cycles"""


@register_command
@dataclass
class P4G_RAW_CONN_INCARNATION:
    """
    Defines the lifecycle of a connection and how new connections should be established as old connections are closed.
    """

    code: typing.ClassVar[int] = 671
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=LifecycleMode)  # coded byte, defines the lifecycle of connections

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=LifecycleMode)  # coded byte, defines the lifecycle of connections

    def get(self) -> "Token[GetDataAttr]":
        """Get the lifecycle of a connection and how new connections should be established.

        :return: the lifecycle of a connection and how new connections should be established.
        :rtype: P4G_RAW_CONN_INCARNATION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: LifecycleMode) -> "Token":
        """Set the lifecycle of a connection and how new connections should be established.

        :param mode: connection lifecycle mode
        :type mode: LifecycleMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode))

    set_once = functools.partialmethod(set, LifecycleMode.ONCE)
    """Connections are established during the ramp-up phase and not closed until the ramp-down phase of the load profile. That is, each configured connection only exists once."""
    set_immortal = functools.partialmethod(set, LifecycleMode.IMMORTAL)
    """Connections are established during the ramp-up phase of the load profile, and are closed after the configured lifetime (configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_LIFETIME`). As connections close, new connections are established, attempting to keep the concurrent number of established connections constant. A new connection will have the same IP address as the connection it replaces, but will have a new TCP port number. This will simulate that the user (defined by the client IP address) is living on, and creates new connections as old connections close."""
    set_reincarnate = functools.partialmethod(set, LifecycleMode.REINCARNATE)
    """Connections are established during the ramp-up phase of the load profile, and are closed after the configured lifetime (configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_LIFETIME`). As connections close, new connections are established, attempting to keep the concurrent number of established connections constant. A new connection will have the same TCP port number as the connection it replaces, but will have a new IP address. This will simulate that the user (defined by the client IP address) ceases to exist, and new users appear as old users die."""


@register_command
@dataclass
class P4G_RAW_CONN_REPETITIONS:
    """
    Defines how many times a new connection should be created, after an old
    connection has been closed, when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_INCARNATION` is set to ``IMMORTAL`` or
    ``REINCARNATE``.
    """

    code: typing.ClassVar[int] = 672
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, repetition mode.
        repetition_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of repetitions

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, repetition mode.
        repetition_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of repetitions

    def get(self) -> "Token[GetDataAttr]":
        """Get how many times a new connection should be created after an old connection is closed.

        :return: how many times a new connection should be created after an old connection is closed.
        :rtype: P4G_RAW_CONN_REPETITIONS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: InfiniteOrFinite, repetition_count: int) -> "Token":
        """Set how many times a new connection should be created after an old connection is closed.

        :param mode: repetition mode.
        :type mode: InfiniteOrFinite
        :param repetition_count:  number of repetitions
        :type repetition_count: int
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode, repetition_count=repetition_count)
        )

    set_infinite = functools.partialmethod(set, InfiniteOrFinite.INFINITE)
    """New connections are generated as long as the load profile allows."""
    set_finite = functools.partialmethod(set, InfiniteOrFinite.FINITE)
    """Each configured connection is closed and re-established repetitions number of times."""


@register_command
@dataclass
class P4G_RAW_CONN_LIFETIME:
    """
    Defines the lifetime of a connection, when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_CONN_INCARNATION` is set to ``IMMORTAL`` or ``REINCARNATE``.
    """

    code: typing.ClassVar[int] = 673
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        timescale: XmpField[XmpByte] = XmpField(XmpByte, choices=Timescale)  # coded byte, specifying the time scale
        lifetime: XmpField[XmpInt] = XmpField(XmpInt)  # integer, time from a connection is established until it will be closed.

    @dataclass(frozen=True)
    class GetDataAttr:
        timescale: XmpField[XmpByte] = XmpField(XmpByte, choices=Timescale)  # coded byte, specifying the time scale
        lifetime: XmpField[XmpInt] = XmpField(XmpInt)  # integer, time from a connection is established until it will be closed.

    def get(self) -> "Token[GetDataAttr]":
        """Get the lifetime of a connection.

        :return: the lifetime of a connection
        :rtype: P4G_RAW_CONN_LIFETIME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, timescale: Timescale, lifetime: int) -> "Token":
        """Set the lifetime of a connection.

        :param timescale: specifying the time scale
        :type timescale: Timescale
        :param lifetime: time from a connection is established until it will be closed.
        :type lifetime: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], timescale=timescale, lifetime=lifetime))

    set_msecs = functools.partialmethod(set, Timescale.MSECS)
    """Set the time scale of a connection lifetime to milliseconds."""
    set_seconds = functools.partialmethod(set, Timescale.SECONDS)
    """Set the time scale of a connection lifetime to seconds."""
    set_minutes = functools.partialmethod(set, Timescale.MINUTES)
    """Set the time scale of a connection lifetime to minutes."""
    set_hours = functools.partialmethod(set, Timescale.HOURS)
    """Set the time scale of a connection lifetime to hours."""


@register_command
@dataclass
class P4G_IP_VERSION:
    """
    Specifies either IPv4 or IPv6.
    """

    code: typing.ClassVar[int] = 684
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        version_number: XmpField[XmpByte] = XmpField(XmpByte, choices=L47IPVersion)  # coded byte, IP version

    @dataclass(frozen=True)
    class GetDataAttr:
        version_number: XmpField[XmpByte] = XmpField(XmpByte, choices=L47IPVersion)  # coded byte, IP version

    def get(self) -> "Token[GetDataAttr]":
        """Get the IP version of a Connection Group.

        :return: the IP version of a Connection Group.
        :rtype: P4G_IP_VERSION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, version_number: L47IPVersion) -> "Token":
        """Set the IP version of a Connection Group.

        :param version_number: IP version
        :type version_number: L47IPVersion
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], version_number=version_number))

    set_ipv4 = functools.partialmethod(set, L47IPVersion.IPV4)
    """Set IP version to IPv4."""
    set_ipv6 = functools.partialmethod(set, L47IPVersion.IPV6)
    """Set IP version to IPv6."""


@register_command
@dataclass
class P4G_IPV6_CLIENT_RANGE:
    """
    Specifies the number of client sockets (IPv6 address, port number).
    """

    code: typing.ClassVar[int] = 685
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ipv6_address: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports
        max_address_count: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, the maximum number of ip addresses that this Connection Group will use, when connection incarnation is set to REINCARNATE

    @dataclass(frozen=True)
    class GetDataAttr:
        ipv6_address: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # 16 hex bytes, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports
        max_address_count: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, the maximum number of ip addresses that this Connection Group will use, when connection incarnation is set to REINCARNATE

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of client sockets (IPv6 address, port number).

        :return: the number of client sockets (IPv6 address, port number).
        :rtype: P4G_IPV6_CLIENT_RANGE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ipv6_address: typing.Union[str, int, ipaddress.IPv6Address], address_count: int, start_port: int, port_count: int, max_address_count: int) -> "Token":
        """Set the number of client sockets (IPv6 address, port number).

        :param ipv6_address: the start ip address of the address range
        :type ipv6_address: typing.Union[str, int, ipaddress.IPv6Address]
        :param address_count: the number of IPv6 addresses
        :type address_count: int
        :param start_port: the start port number of the port range
        :type start_port: int
        :param port_count: the number of ports
        :type port_count: int
        :param max_address_count: the maximum number of IPv6 addresses that this Connection Group will use, when connection incarnation is set to ``REINCARNATE``
        :type max_address_count: int
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
                ipv6_address=ipv6_address,
                address_count=address_count,
                start_port=start_port,
                port_count=port_count,
                max_address_count=max_address_count,
            ),
        )


@register_command
@dataclass
class P4G_IPV6_SERVER_RANGE:
    """
    Specifies the number of server sockets (IPv6 address, port number)
    """

    code: typing.ClassVar[int] = 686
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ipv6_address: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # hexbytes, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports

    @dataclass(frozen=True)
    class GetDataAttr:
        ipv6_address: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # hexbytes, the start ip address of the address range
        address_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ip addresses
        start_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the start port number, of the port range
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the number of ports

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of server sockets (IPv6 address, port number).

        :return: the number of server sockets (IPv6 address, port number)
        :rtype: P4G_IPV6_SERVER_RANGE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ipv6_address: typing.Union[str, int, ipaddress.IPv6Address], address_count: int, start_port: int, port_count: int) -> "Token":
        """Set the number of server sockets (IPv6 address, port number).

        :param ipv6_address: the start IPv6 address of the address range
        :type ipv6_address: typing.Union[str, int, ipaddress.IPv6Address]
        :param address_count: the number of IPv6 addresses
        :type address_count: int
        :param start_port: the start port number of the port range
        :type start_port: int
        :param port_count: the number of ports
        :type port_count: int
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
                ipv6_address=ipv6_address,
                address_count=address_count,
                start_port=start_port,
                port_count=port_count,
            ),
        )


@register_command
@dataclass
class P4G_IPV6_TRAFFIC_CLASS:
    """
    Configure the value of the traffic class field of the IPv6 header.
    """

    code: typing.ClassVar[int] = 687
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        traffic_class: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, value of the traffic class field

    @dataclass(frozen=True)
    class GetDataAttr:
        traffic_class: XmpField[XmpHex1] = XmpField(XmpHex1)  # hex byte, value of the traffic class field

    def get(self) -> "Token[GetDataAttr]":
        """Get the value of the traffic class field of the IPv6 header.

        :return: the value of the traffic class field of the IPv6 header.
        :rtype: P4G_IPV6_TRAFFIC_CLASS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, traffic_class: str) -> "Token":
        """Set the value of the traffic class field of the IPv6 header.

        :param traffic_class: value of the traffic class field
        :type traffic_class: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], traffic_class=traffic_class))


@register_command
@dataclass
class P4G_IPV6_FLOW_LABEL:
    """
    Configure the value of the flow label field of the IPv6 header.
    """

    code: typing.ClassVar[int] = 688
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        flow_label: XmpField[XmpHex4] = XmpField(XmpHex4)  # 4 hex bytes, value of the traffic class field (only lowest 20 bits are valid)

    @dataclass(frozen=True)
    class GetDataAttr:
        flow_label: XmpField[XmpHex4] = XmpField(XmpHex4)  # 4 hex bytes, value of the traffic class field (only lowest 20 bits are valid)

    def get(self) -> "Token[GetDataAttr]":
        """Get the value of the flow label field of the IPv6 header.

        :return: the value of the flow label field of the IPv6 header.
        :rtype: P4G_IPV6_FLOW_LABEL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, flow_label: str) -> "Token":
        """Set the value of the flow label field of the IPv6 header.

        :param flow_label: value of the traffic class field (only lowest 20 bits are valid)
        :type flow_label: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], flow_label=flow_label))


@register_command
@dataclass
class P4G_L4_PROTOCOL:
    """
    Specifies either TCP or UDP as Layer 4 protocol.
    """

    code: typing.ClassVar[int] = 689
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        protocol_type: XmpField[XmpByte] = XmpField(XmpByte, choices=L47ProtocolType)  # coded byte, layer 4 protocol.

    @dataclass(frozen=True)
    class GetDataAttr:
        protocol_type: XmpField[XmpByte] = XmpField(XmpByte, choices=L47ProtocolType)  # coded byte, layer 4 protocol.

    def get(self) -> "Token[GetDataAttr]":
        """Get the Layer 4 protocol used by the Connection Group.

        :return: the Layer 4 protocol used by the Connection Group.
        :rtype: P4G_L4_PROTOCOL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, protocol_type: L47ProtocolType) -> "Token":
        """Set the Layer 4 protocol used by the Connection Group.

        :param protocol_type: the Layer 4 protocol
        :type protocol_type: L47ProtocolType
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], protocol_type=protocol_type))

    set_tcp = functools.partialmethod(set, L47ProtocolType.TCP)
    """Use TCP as the Layer 4 protocol of the Connection Group."""
    set_udp = functools.partialmethod(set, L47ProtocolType.UDP)
    """Use UDP as the Layer 4 protocol of the Connection Group."""


@register_command
@dataclass
class P4G_TCP_ESTABLISH_HIST:
    """
    Returns a histogram over TCP connection establish times, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TIME_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 741
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections established.
        min_connection_estab_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum connection establish time in us.
        max_connection_estab_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum connection establish time in us.
        avg_connection_estab_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average connection establish time in us.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in us
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in us
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with establish time within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over TCP connection establish times.

        :return: a histogram over TCP connection establish times
        :rtype: P4G_TCP_ESTABLISH_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_CLOSE_HIST:
    """
    Returns a histogram over TCP connection close times, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TIME_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 742
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections closed.
        min_connection_close_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum connection close time in us.
        max_connection_close_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum connection close time in us.
        avg_connection_close_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average connection close time in us.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in us
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in us
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with close time within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over TCP connection close times.

        :return: a histogram over TCP connection close times
        :rtype: P4G_TCP_CLOSE_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_RX_TOTAL_BYTES_HIST:
    """
    Returns a histogram over number of total TCP bytes received, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 743
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum total TCP bytes received on a connection.
        max_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum total TCP bytes received on a connection.
        avg_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average total TCP bytes received on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received total TCP bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of total TCP bytes received.

        :return: a histogram over number of total TCP bytes received
        :rtype: P4G_TCP_RX_TOTAL_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_RX_GOOD_BYTES_HIST:
    """
    Returns a histogram over number of good TCP bytes received, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 744
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum good TCP bytes received on a connection.
        max_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum good TCP bytes received on a connection.
        avg: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average good TCP bytes received on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received good TCP bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of good TCP bytes received.

        :return: a histogram over number of good TCP bytes received
        :rtype: P4G_TCP_RX_GOOD_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_TX_TOTAL_BYTES_HIST:
    """
    Returns a histogram over number of total TCP bytes transmitted, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 745
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum total TCP bytes transmitted on a connection.
        max_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum total TCP bytes transmitted on a connection.
        avg_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average total TCP bytes transmitted on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted total TCP bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of total TCP bytes transmitted.

        :return: a histogram over number of total TCP bytes transmitted
        :rtype: P4G_TCP_TX_TOTAL_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_TX_GOOD_BYTES_HIST:
    """
    Returns a histogram over number of good TCP bytes transmitted, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 746
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        conn: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum good TCP bytes transmitted on a connection.
        max: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum good TCP bytes transmitted on a connection.
        average: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average good TCP bytes transmitted on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted good TCP bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of good TCP bytes transmitted.

        :return: a histogram over number of good TCP bytes transmitted
        :rtype: P4G_TCP_TX_GOOD_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_APP_REPLAY_COUNTERS:
    """
    Returns NAT collisions of a replay application.
    """

    code: typing.ClassVar[int] = 747
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        nat_collision_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of NAT collisions

    def get(self) -> "Token[GetDataAttr]":
        """Get NAT collisions of a replay application.

        :return: NAT collisions of a replay application.
        :rtype: P4G_APP_REPLAY_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_APP_TRANSACTION_COUNTERS:
    """
    Returns request/response transaction statistics.
    """

    code: typing.ClassVar[int] = 753
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        transaction_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of completed request/response transactions
        transaction_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of completed transactions/second

    def get(self) -> "Token[GetDataAttr]":
        """Get request/response transaction statistics.

        :return: request/response transaction statistics.
        :rtype: P4G_APP_TRANSACTION_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_APP_TRANSACTION_HIST:
    """
    Returns a histogram over completed request/response transactions per connection,
    with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TRANSACTION_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 754
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections.
        min_transaction_per_con: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum number of transactions per connection.
        max_transaction_per_con: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum number of transactions per connection.
        avg_transaction_per_con: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average number of transactions per connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with number of transactions within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over completed request/response transactions per connection.

        :return: a histogram over completed request/response transactions per connection
        :rtype: P4G_APP_TRANSACTION_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_STATE_CURRENT:
    """
    Returns a list of the current UDP state counters. The counters returned
    corresponds the the following UDP states:
    
    * ``CLOSED`` The connection structure has been created, but has not been 'ramped up' yet.
    
    * ``OPEN`` The connection has been 'ramped up', and is ready to transmit or receive data.
    
    * ``ACTIVE``. The connection is actively transmitting data.

    """

    code: typing.ClassVar[int] = 756
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        closed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        opened: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        active: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the current UDP state counters.

        :return: a list of the current UDP state counters
        :rtype: P4G_UDP_STATE_CURRENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_STATE_TOTAL:
    """
    Returns a list of the total UDP state counters. The counters returned
    corresponds the the following UDP states:
    
    * ``CLOSED`` The connection structure has been created, but has not been 'ramped up' yet.
    
    * ``OPEN`` The connection has been 'ramped up', and is ready to transmit or receive data.
    
    * ``ACTIVE`` The connection is actively transmitting data.

    """

    code: typing.ClassVar[int] = 757
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        closed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        opened: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        active: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the total UDP state counters.

        :return: a list of the total UDP state counters.
        :rtype: P4G_UDP_STATE_TOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_STATE_RATE:
    """
    Returns a list of the UDP state rates measured in connections/second. The
    counters returned corresponds the the following UDP state rates:
    
    * ``CLOSED`` The connection structure has been created, but has not been 'ramped up' yet.
    
    * ``OPEN`` The connection has been 'ramped up', and is ready to transmit or receive data
    
    * ``ACTIVE`` The connection is actively transmitting data.

    """

    code: typing.ClassVar[int] = 758
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        closed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        open: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        active: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the UDP state rates measured in connections/second.

        :return: a list of the UDP state rates measured in connections/second.
        :rtype: P4G_UDP_STATE_RATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_RX_PAYLOAD_COUNTERS:
    """
    Returns a list of the UDP RX payload counters.
    """

    code: typing.ClassVar[int] = 759
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP payload bytes received
        byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP payload bytes/second received

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the UDP RX payload counters.

        :return: a list of the UDP RX payload counters.
        :rtype: P4G_UDP_RX_PAYLOAD_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_TX_PAYLOAD_COUNTERS:
    """
    Returns a list of the UDP TX payload counters.
    """

    code: typing.ClassVar[int] = 760
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP payload bytes transmitted
        byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP payload bytes/second transmitted

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the UDP TX payload counters.

        :return: a list of the UDP TX payload counters.
        :rtype: P4G_UDP_TX_PAYLOAD_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_RX_BYTES_HIST:
    """
    Returns a histogram over number of UDP bytes received, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 761
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum UDP bytes received on a connection.
        max_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum UDP bytes received on a connection.
        avg_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average UDP bytes received on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received UDP bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of UDP bytes received.

        :return: a histogram over number of UDP bytes received
        :rtype: P4G_UDP_RX_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_TX_BYTES_HIST:
    """
    Returns a histogram over number of UDP bytes transmitted, with start and interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 762
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum UDP bytes transmitted on a connection.
        max_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum UDP bytes transmitted on a connection.
        avg_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average UDP bytes transmitted on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted UDP bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of UDP bytes transmitted.

        :return: a histogram over number of UDP bytes transmitted
        :rtype: P4G_UDP_TX_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_RX_PACKET_COUNTERS:
    """
    Returns a list of the TCP RX packet counters.
    """

    code: typing.ClassVar[int] = 770
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        packet_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP packets received
        packet_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP packets/second received

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TCP RX packet counters.

        :return: a list of the TCP RX packet counters.
        :rtype: P4G_TCP_RX_PACKET_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TCP_TX_PACKET_COUNTERS:
    """
    Returns a list of the TCP TX packet counters.
    """

    code: typing.ClassVar[int] = 771
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        packet_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP packets transmitted
        packet_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TCP packets/second transmitted

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TCP TX packet counters.

        :return: a list of the TCP TX packet counters.
        :rtype: P4G_TCP_TX_PACKET_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_RX_PACKET_COUNTERS:
    """
    Returns a list of the UDP RX packet counters.
    """

    code: typing.ClassVar[int] = 772
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        packet_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP packets received
        packet_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP packets/second received

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the UDP RX packet counters.

        :return: a list of the UDP RX packet counters.
        :rtype: P4G_UDP_RX_PACKET_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_UDP_TX_PACKET_COUNTERS:
    """
    Returns a list of the UDP TX packet counters.
    """

    code: typing.ClassVar[int] = 773
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        packet_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP packets transmitted
        packet_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of UDP packets/second transmitted

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the UDP TX packet counters.

        :return: a list of the UDP TX packet counters.
        :rtype: P4G_UDP_TX_PACKET_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_CLEAR_POST_STAT:
    """
    Clears all TCP Connection Group post-test statistics.
    """

    code: typing.ClassVar[int] = 790
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clears all TCP Connection Group post-test statistics.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
            ),
        )


@register_command
@dataclass
class P4G_RECALC_TIME_HIST:
    """
    Recalculates connection time histograms (retrieved with: :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_ESTABLISH_HIST` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_CLOSE_HIST`). Used in case time histogram configuration has been changed (using :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TIME_HIST_CONF`).
    """

    code: typing.ClassVar[int] = 791
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Recalculates connection time histograms
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
            ),
        )


@register_command
@dataclass
class P4G_RECALC_PAYLOAD_HIST:
    """
    Recalculates connection payload histograms (retrieved with: :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_TOTAL_BYTES_HIST`, :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_RX_GOOD_BYTES_HIST`, :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_TOTAL_BYTES_HIST` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TCP_TX_GOOD_BYTES_HIST`). Used in case
    payload histogram configuration has been changed (using :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`)
    """

    code: typing.ClassVar[int] = 792
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Recalculates connection payload histograms.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
            ),
        )


@register_command
@dataclass
class P4G_RECALC_TRANSACTION_HIST:
    """
    Recalculates transaction histograms (retrieved with: :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_APP_TRANSACTION_HIST`).
    Used in case transaction histogram configuration has been changed (using :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_TRANSACTION_HIST_CONF`)
    """

    code: typing.ClassVar[int] = 793
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Recalculates transaction histograms.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._group_xindex],
            ),
        )


@register_command
@dataclass
class P4G_REPLAY_FILE_INDICES:
    """
    Returns an index list of configured Replay Files for this Connection Group.
    These are the Replay File Index that are used for :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_FILE_NAME` and :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_FILE_CLEAR` commands.  More than one Replay File can be configured for a Connection Group. When configuring a Replay File for a Connection Group, it must have an index.
    """

    code: typing.ClassVar[int] = 900
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        replay_file_indices: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, indices of configured replay files

    def get(self) -> "Token[GetDataAttr]":
        """Get an index list of configured Replay Files for this Connection Group.

        :return: an index list of configured Replay Files for this Connection Group.
        :rtype: P4G_REPLAY_FILE_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_REPLAY_FILE_NAME:
    """
    More than one Replay File can be configured for a Connection Group. When
    configuring a Replay File for a Connection Group, it must have an index. The
    indices at which Replay Files are configured does not have to be continuous.
    """

    code: typing.ClassVar[int] = 901
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int
    _replay_file_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        file_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, file name (including relative path and excluding the '.bson' extension).

    @dataclass(frozen=True)
    class GetDataAttr:
        file_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, file name (including relative path and excluding the '.bson' extension).

    def get(self) -> "Token[GetDataAttr]":
        """Get the name of a replay file configured for the Connection Group.

        :return: the name of a replay file configured for the Connection Group.
        :rtype: P4G_REPLAY_FILE_NAME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex, self._replay_file_xindex]))

    def set(self, file_name: str) -> "Token":
        """Set the name of a replay file configured for the Connection Group.

        :param file_name: file name (including relative path and excluding the ``.bson`` extension).
        :type file_name: str
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex, self._replay_file_xindex], file_name=file_name)
        )


@register_command
@dataclass
class P4G_REPLAY_FILE_CLEAR:
    """
    Clears a Replay File index, so no Replay File is configured for that index.
    """

    code: typing.ClassVar[int] = 902
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _replay_file_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clears a Replay File index.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._replay_file_xindex],
            ),
        )


@register_command
@dataclass
class P4G_REPLAY_UTILIZATION:
    """
    Specify the link layer bandwidth utilization for all the generated traffic from
    the specified Replay Connection Group.
    """

    code: typing.ClassVar[int] = 903
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        utilization: XmpField[XmpInt] = XmpField(XmpInt)  # integer, utilization specified in ppm.

    @dataclass(frozen=True)
    class GetDataAttr:
        utilization: XmpField[XmpInt] = XmpField(XmpInt)  # integer, utilization specified in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get the link layer bandwidth utilization for all the generated traffic from the specified Replay Connection Group.

        :return: the link layer bandwidth utilization for all the generated traffic from the specified Replay Connection Group.
        :rtype: P4G_REPLAY_UTILIZATION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, utilization: int) -> "Token":
        """Set the link layer bandwidth utilization for all the generated traffic from the specified Replay Connection Group.

        :param utilization: utilization specified in ppm.
        :type utilization: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], utilization=utilization))


@register_command
@dataclass
class P4G_REPLAY_USER_INCARNATION:
    """
    Defines the lifecycle mode of a user and its connections, and how new users should be
    established as old connections are closed.
    """

    code: typing.ClassVar[int] = 904
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=LifecycleMode)  # coded byte, defines the lifecycle mode of connections.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=LifecycleMode)  # coded byte, defines the lifecycle mode of connections.

    def get(self) -> "Token[GetDataAttr]":
        """Get the lifecycle mode of a user and its connections.

        :return: the lifecycle mode of a user and its connections
        :rtype: P4G_REPLAY_USER_INCARNATION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: LifecycleMode) -> "Token":
        """Set the lifecycle mode of a user and its connections.

        :param mode: defines the lifecycle mode of connections.
        :type mode: LifecycleMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode))

    set_once = functools.partialmethod(set, LifecycleMode.ONCE)
    """Users are created and its connections are established during the ramp-up phase and not closed until the ramp-down phase of the load profile. That is, each configured user only exists once."""
    set_immortal = functools.partialmethod(set, LifecycleMode.IMMORTAL)
    """Users are created and its connections are established during the ramp-up phase of the load profile. Each connection is closed when all payload in the Replay File for that connection has been transmitted. A user is destroyed when all its connections are closed. As users are destroyed, new users are created, attempting to keep the concurrent number of users constant. A new user will have the same IP address as the user he replaces, but the new connections will have new TCP/UDP port numbers. This will simulate that the user is living on, and creates new connections as old connections close."""
    set_reincarnate = functools.partialmethod(set, LifecycleMode.REINCARNATE)
    """Users are created and its connections are established during the ramp-up phase of the load profile. Each connection is closed when all payload in the Replay File for that connection has been transmitted. A user is destroyed when all its connections are closed. As users are destroyed, new users are created, attempting to keep the concurrent number of users constant. A new user will have a different IP address than the user it replaces, but its connection will have the same TCP/UDP port numbers. This will simulate that the user ceases to exist, and new users appear as old users die."""


@register_command
@dataclass
class P4G_REPLAY_USER_REPETITIONS:
    """
    Defines how many times a new user should be created after an old user has been destroyed, when :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_REPLAY_USER_INCARNATION` is set to ``IMMORTAL`` or ``REINCARNATE``.
    """

    code: typing.ClassVar[int] = 905
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, repetition mode.
        repetition_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of repetitions

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=InfiniteOrFinite)  # coded byte, repetition mode.
        repetition_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of repetitions

    def get(self) -> "Token[GetDataAttr]":
        """Get how many times a new user should be created, after an old user has been destroyed.

        :return: how many times a new user should be created, after an old user has been destroyed
        :rtype: P4G_REPLAY_USER_REPETITIONS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, mode: InfiniteOrFinite, repetition_count: int) -> "Token":
        """Set how many times a new user should be created, after an old user has been destroyed.

        :param mode: the repetition mode
        :type mode: InfiniteOrFinite
        :param repetition_count: number of repetitions
        :type repetition_count: int
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], mode=mode, repetition_count=repetition_count)
        )

    set_infinite = functools.partialmethod(set, InfiniteOrFinite.INFINITE)
    """New users are generated as long as the load profile allows."""
    set_finite = functools.partialmethod(set, InfiniteOrFinite.FINITE)
    """Each configured user is destroyed and re-created repetitions number of times."""


@register_command
@dataclass
class P4G_USER_STATE_CURRENT:
    """
    Returns a list of the current user state counters. A user is identified by a
    Client IP address. The counters returned corresponds the the following user
    states:
    
    * ``INIT`` The user has been created,  but has no open connections yet.
    
    * ``ACTIVE``  The user has at least one open connection.
    
    * ``SUCCESS`` The user has successfully transmitted and received all payload.
    
    * ``FAILED`` The user has failed in transmitting or receiving all payload.  STOPPED The user has been stopped due to ramp-down.
    
    * ``INACTIVE`` All the users connection is closed, but the user has not been destroyed yet.
    """

    code: typing.ClassVar[int] = 910
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        init: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users currently in this state
        active: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users currently in this state
        success: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users currently in this state
        failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users currently in this state
        stopped: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users currently in this state
        inactive: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users currently in this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the current user state counters.

        :return: a list of the current user state counters.
        :rtype: P4G_USER_STATE_CURRENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_USER_STATE_TOTAL:
    """
    Returns a list of the total user state counters. A user is identified by a
    Client IP address. The counters returned corresponds the the following user
    states:
    
    * ``INIT`` The user has been created, but has no open connections yet.
    
    * ``ACTIVE`` The user has at least one open connection.
    
    * ``SUCCESS`` The user has successfully transmitted and received all payload.
    
    * ``FAILED`` The user has failed in transmitting or receiving all payload.
    
    * ``STOPPED`` The user has been stopped due to ramp-down.
    
    * ``INACTIVE`` All the users connection is closed, but the user has not been destroyed yet.
    """

    code: typing.ClassVar[int] = 911
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        init: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of users that has entered this state
        active: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of users that has entered this state
        success: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of users that has entered this state
        failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of users that has entered this state
        stopped: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of users that has entered this state
        inactive: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of users that has entered this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the total user state counters.

        :return: a list of the total user state counters.
        :rtype: P4G_USER_STATE_TOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_USER_STATE_RATE:
    """
    Returns a list of the user state rates measured in users/second. A user is
    identified by a Client IP address. The counters returned  corresponds the the
    following user states:
    
    * ``INIT`` The user has been created, but has no open connections yet.
    
    * ``ACTIVE`` The user has at least one open connection.
    
    * ``SUCCESS`` The user has successfully transmitted and received all payload.
    
    * ``FAILED`` The user has failed in transmitting or receiving all payload.
    
    * ``STOPPED`` The user has been stopped due to ramp-down.
    
    * ``INACTIVE`` All the users connection is closed, but the user has not been destroyed yet.

    """

    code: typing.ClassVar[int] = 912
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        stats: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users/second entering this state
        init: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users/second entering this state
        active: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users/second entering this state
        success: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users/second entering this state
        failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users/second entering this state
        stopped: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of users/second entering this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the user state rates measured in users/second.

        :return: a list of the user state rates measured in users/second.
        :rtype: P4G_USER_STATE_RATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_ENABLE:
    """
    Enable/Disable TLS.
    """

    code: typing.ClassVar[int] = 1100
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # code byte, specifying whether to enable TLS

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # code byte, specifying whether to enable TLS

    def get(self) -> "Token[GetDataAttr]":
        """Get whether TLS is enabled.

        :return: whether TLS is enabled.
        :rtype: P4G_TLS_ENABLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, on_off: YesNo) -> "Token":
        """Set whether TLS is enabled.

        :param on_off: specifying whether to enable TLS
        :type on_off: YesNo
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], on_off=on_off))

    set_no = functools.partialmethod(set, YesNo.NO)
    """Disable TLS."""
    set_yes = functools.partialmethod(set, YesNo.YES)
    """Enable TLS."""


@register_command
@dataclass
class P4G_TLS_CIPHER_SUITES:
    """
    Configure the list of ciphers to announce in order of priorities.
    """

    code: typing.ClassVar[int] = 1101
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ciphers: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, sequence of ciphers identified by theirs IANA number in order of priority.

    @dataclass(frozen=True)
    class GetDataAttr:
        ciphers: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, sequence of ciphers identified by theirs IANA number in order of priority.

    def get(self) -> "Token[GetDataAttr]":
        """Get the list of ciphers to announce in order of priorities.

        :return: the list of ciphers to announce in order of priorities.
        :rtype: P4G_TLS_CIPHER_SUITES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, ciphers: str) -> "Token":
        """Set the list of ciphers to announce in order of priorities.

        :param ciphers: sequence of ciphers identified by theirs IANA number in order of priority.
        :type ciphers: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], ciphers=ciphers))


@register_command
@dataclass
class P4G_TLS_MAX_RECORD_SIZE:
    """
    Configure the maximum outgoing TLS record size.
    """

    code: typing.ClassVar[int] = 1102
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum outgoing record size in the interval ]0;16384], default value 8087.

    @dataclass(frozen=True)
    class GetDataAttr:
        size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum outgoing record size in the interval ]0;16384], default value 8087.

    def get(self) -> "Token[GetDataAttr]":
        """Get the maximum outgoing TLS record size.

        :return: the maximum outgoing TLS record size.
        :rtype: P4G_TLS_MAX_RECORD_SIZE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, size: int) -> "Token":
        """Set the maximum outgoing TLS record size.

        :param size: maximum outgoing record size in the interval (0, 16384], default value 8087.
        :type size: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], size=size))


@register_command
@dataclass
class P4G_TLS_CERTIFICATE_FILENAME:
    """
    Configure the TLS certificate.
    """

    code: typing.ClassVar[int] = 1103
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filename: XmpField[XmpStr] = XmpField(XmpStr)  # string, the filename of the certificate relative to the ftp tls folder

    def set(self, filename: str) -> "Token":
        """Set the TLS certificate.

        :param filename: the filename of the certificate relative to the FTP TLS folder on the tester.
        :type filename: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], filename=filename))


@register_command
@dataclass
class P4G_TLS_PRIVATE_KEY_FILENAME:
    """
    Configure the private key matching the TLS certificate.
    """

    code: typing.ClassVar[int] = 1104
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filename: XmpField[XmpStr] = XmpField(XmpStr)  # string, the filename of the private key relative to the ftp tls folder

    def set(self, filename: str) -> "Token":
        """Set the private key matching the TLS certificate.

        :param filename: the filename of the private key relative to the FTP TLS folder on the tester.
        :type filename: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], filename=filename))


@register_command
@dataclass
class P4G_TLS_DHPARAMS_FILENAME:
    """
    Configure TLS DH parameters, if not set a default set will be used.
    """

    code: typing.ClassVar[int] = 1105
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filename: XmpField[XmpStr] = XmpField(XmpStr)  # string, the filename of the dhparams relative to the ftp tls folder

    def set(self, filename: str) -> "Token":
        """Set TLS DH parameters.

        :param filename: the filename of the TLS DH parameters relative to the FTP TLS folder on the tester.
        :type filename: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], filename=filename))


@register_command
@dataclass
class P4G_TLS_CLOSE_NOTIFY:
    """
    Enable/Disable TLS sending close notify alert on connection tear-down.
    """

    code: typing.ClassVar[int] = 1106
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # code byte, specifying whether to send close notify on connection tear down

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # code byte, specifying whether to send close notify on connection tear down

    def get(self) -> "Token[GetDataAttr]":
        """Get whether TLS sends close notify alert on connection tear-down.

        :return: whether TLS sends close notify alert on connection tear-down.
        :rtype: P4G_TLS_CLOSE_NOTIFY.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, on_off: YesNo) -> "Token":
        """Set whether TLS sends close notify alert on connection tear-down.

        :param on_off: whether TLS sends close notify alert on connection tear-down.
        :type on_off: YesNo
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], on_off=on_off))

    set_no = functools.partialmethod(set, YesNo.NO)
    """TLS does not send close notify alert on connection tear-down."""
    set_yes = functools.partialmethod(set, YesNo.YES)
    """TLS sends close notify alert on connection tear-down."""


@register_command
@dataclass
class P4G_TLS_ALERT_WARNING_COUNTERS:
    """
    Returns a list of TLS warning counters.  The counters returned corresponds the
    the following TLS warnings:

    * close_notify
    * unexpected_message
    * bad_record_mac
    * record_overflow
    * decompression_failure
    * handshake_failure
    * bad_certificate
    * unsupported_certificate
    * certificate_revoked
    * certificate_expired
    * certificate_unknown
    * illegal_parameter
    * unknown_ca
    * access_denied
    * decode_error
    * decrypt_error
    * protocol_version
    * insufficient_security
    * internal_error
    * user_canceled
    * no_renegotiation
    * unsupported_extension
    * unknown.
    """

    code: typing.ClassVar[int] = 1107
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        close_notify: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        unexpected_message: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        bad_record_mac: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        record_overflow: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        decompression_failure: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        handshake_failure: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        bad_certificate: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        unsupported_certificate: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        certificate_revoked: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        certificate_expired: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        certificate_unknown: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        illegal_parameter: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        unknown_ca: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        access_denied: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        decode_error: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        decrypt_error: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        protocol_version: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        insufficient_security: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        internal_error: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        user_canceled: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        no_renegotiation: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        unsupported_extension: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received
        unknown: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this warning received

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of TLS warning counters.

        :return: a list of TLS warning counters
        :rtype: P4G_TLS_ALERT_WARNING_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_ALERT_FATAL_COUNTERS:
    """
    Returns a list of TLS error counters. The counters returned corresponds the the
    following TLS warnings:

    * close_notify
    * unexpected_message
    * bad_record_mac
    * record_overflow
    * decompression_failure
    * handshake_failure
    * bad_certificate
    * unsupported_certificate
    * certificate_revoked
    * certificate_expired
    * certificate_unknown
    * illegal_parameter
    * unknown_ca
    * access_denied
    * decode_error
    * decrypt_error
    * protocol_version
    * insufficient_security
    * internal_error
    * user_canceled
    * no_renegotiation
    * unsupported_extension
    * unknown.
    """

    code: typing.ClassVar[int] = 1108
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        stats: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        unexpected_message: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        bad_record_mac: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        record_overflow: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        decompression_failure: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        handshake_failure: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        bad_certificate: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        unsupported_certificate: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        certificate_revoked: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        certificate_expired: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        certificate_unknown: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        illegal_parameter: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        unknown_ca: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        access_denied: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        decode_error: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        decrypt_error: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        protocol_version: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        insufficient_security: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        internal_error: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        user_canceled: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        no_renegotiation: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        unsupported_extension: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received
        unknown: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of this error received

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of TLS error counters.

        :return: a list of TLS error counters
        :rtype: P4G_TLS_ALERT_FATAL_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_STATE_CURRENT:
    """
    Returns a list of the current TLS state counters. The counters returned
    corresponds the the following TLS states:
    
    * TLS_INACTIVE
    * TLS_HANDSHAKING
    * TLS_HANDSHAKE_DONE
    * TLS_HANDSHAKE_FAILED
    * TLS_FAILED
    * TLS_INTERNAL_FAILED
    * TLS_CLOSE_NOTIFY
    * TLS_DONE
    """

    code: typing.ClassVar[int] = 1109
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        tls_inactive: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        tls_handshaking: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        tls_handshake_done: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        tls_handshake_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        tls_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        tls_internal_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        tls_close_notify: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state
        tls_done: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections currently in this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the current TLS state counters.

        :return: a list of the current TLS state counters
        :rtype: P4G_TLS_STATE_CURRENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_STATE_TOTAL:
    """
    Returns a list of the total TLS state counters. The counters returned
    corresponds the the following TLS states:

    * TLS_INACTIVE
    * TLS_HANDSHAKING
    * TLS_HANDSHAKE_DONE
    * TLS_HANDSHAKE_FAILED
    * TLS_FAILED
    * TLS_INTERNAL_FAILED
    * TLS_CLOSE_NOTIFY
    * TLS_DONE
    """

    code: typing.ClassVar[int] = 1110
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        tls_inactive: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        tls_handshaking: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        tls_handshake_done: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        tls_handshake_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        tls_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        tls_internal_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        tls_close_notify: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state
        tls_done: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the total number of connections that has entered this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the total TLS state counters.

        :return: a list of the total TLS state counters
        :rtype: P4G_TLS_STATE_TOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_STATE_RATE:
    """
    Returns a list of the TLS state rates measured in per second. The
    counters returned corresponds the the following TLS states:

    * TLS_INACTIVE
    * TLS_HANDSHAKING
    * TLS_HANDSHAKE_DONE
    * TLS_HANDSHAKE_FAILED
    * TLS_FAILED
    * TLS_INTERNAL_FAILED
    * TLS_CLOSE_NOTIFY
    * TLS_DONE
    """

    code: typing.ClassVar[int] = 1111
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        tls_inactive: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        tls_handshaking: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        tls_handshake_done: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        tls_handshake_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        tls_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        tls_internal_failed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        tls_close_notify: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state
        tls_done: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of connections/second entering this state

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TLS state rates measured in per second.

        :return: a list of the TLS state rates measured in per second
        :rtype: P4G_TLS_STATE_RATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_RX_PAYLOAD_COUNTERS:
    """
    Returns a list of the TLS Rx payload counters.
    """

    code: typing.ClassVar[int] = 1112
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TLS payload bytes received
        byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TLS payload bytes/second received

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TLS Rx payload counters.

        :return: a list of the TLS Rx payload counters.
        :rtype: P4G_TLS_RX_PAYLOAD_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_TX_PAYLOAD_COUNTERS:
    """
    Returns a list of the TLS Tx payload counters.
    """

    code: typing.ClassVar[int] = 1113
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        current_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the current time (mSec since module restart)
        ref_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, reference time (mSec for P4_TRAFFIC on)
        byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TLS payload bytes transmitted
        byte_per_second: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of TLS payload bytes/second transmitted

    def get(self) -> "Token[GetDataAttr]":
        """Get a list of the TLS Tx payload counters.

        :return: a list of the TLS Tx payload counters.
        :rtype: P4G_TLS_TX_PAYLOAD_COUNTERS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_RX_PAYLOAD_BYTES_HIST:
    """
    Returns a histogram over number of TLS Payload bytes received, with start and
    interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 1114
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum TLS Payload bytes received on a connection.
        max_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum TLS Payload bytes received on a connection.
        avg_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average TLS Payload bytes received on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has received TLS Payload bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of TLS Payload bytes received.

        :return: a histogram over number of TLS Payload bytes received
        :rtype: P4G_TLS_RX_PAYLOAD_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_TX_PAYLOAD_BYTES_HIST:
    """
    Returns a histogram over number of TLS Payload bytes transmitted, with start and
    interval values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 1115
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections.
        min_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum TLS Payload bytes transmitted on a connection.
        max_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum TLS Payload bytes transmitted on a connection.
        avg_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average TLS Payload bytes transmitted on a connection.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in bytes
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in bytes
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections that has transmitted TLS Payload bytes within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over number of TLS Payload bytes transmitted.

        :return: a histogram over number of TLS Payload bytes transmitted
        :rtype: P4G_TLS_TX_PAYLOAD_BYTES_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_HANDSHAKE_HIST:
    """
    Returns a histogram over TLS connection handshake times, with start and interval
    values as configured by :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_PAYLOAD_HIST_CONF`.
    """

    code: typing.ClassVar[int] = 1116
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        connection_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer,number of connections established.
        min_connection_handshake_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum connection handshake time in us.
        max_connection_handshake_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum connection handshake time in us.
        avg_connection_handshake_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, average connection handshake time in us.
        start: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, start value of first histogram interval in us
        interval: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, histogram interval size in us
        bin_00: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_01: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_02: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_03: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_04: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_05: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_06: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_07: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_08: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_09: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_10: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_11: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_12: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_13: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_14: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_15: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_16: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_17: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_18: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_19: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_20: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_21: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_22: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_23: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_24: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_25: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_26: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_27: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_28: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_29: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_30: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.
        bin_31: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of connections with handshake time within the given interval.

    def get(self) -> "Token[GetDataAttr]":
        """Get a histogram over TLS connection handshake times.

        :return: a histogram over TLS connection handshake times
        :rtype: P4G_TLS_HANDSHAKE_HIST.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


@register_command
@dataclass
class P4G_TLS_SERVER_NAME:
    """
    Configure the server name advertised by the client in the TLS SNI (Server Name
    Indication) extension. Both the client and server must be configured with the
    same server_name, as the server will check the server name in Client Hello
    message. If server name is not configured (or configured blank), the SNI
    extension will not be inserted in the Client Hello message.
    """

    code: typing.ClassVar[int] = 1117
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        server_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, server name inserted in the SNI TLS extension

    @dataclass(frozen=True)
    class GetDataAttr:
        server_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, server name inserted in the SNI TLS extension

    def get(self) -> "Token[GetDataAttr]":
        """Get the server name advertised by the client in the TLS SNI.

        :return: the server name advertised by the client in the TLS SNI
        :rtype: P4G_TLS_SERVER_NAME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, server_name: str) -> "Token":
        """Set the server name advertised by the client in the TLS SNI.

        :param server_name: server name inserted in the SNI TLS extension
        :type server_name: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], server_name=server_name))


@register_command
@dataclass
class P4G_TLS_PROTOCOL_VER:
    """
    Configures the desired TLS protocol version. More specifically the TLS version
    configured is the protocol version advertised by the client in the Client Hello
    message, and the highest TLS protocol version accepted by the server. If the
    protocol_version in the Client Hello message is higher than the highest protocol
    version accepted by the server, the TLS Handshake will fail.
    """

    code: typing.ClassVar[int] = 1118
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        tls_version: XmpField[XmpByte] = XmpField(XmpByte, choices=TLSVersion)  # coded byte, maximum supported TLS protocol version

    @dataclass(frozen=True)
    class GetDataAttr:
        tls_version: XmpField[XmpByte] = XmpField(XmpByte, choices=TLSVersion)  # coded byte, maximum supported TLS protocol version

    def get(self) -> "Token[GetDataAttr]":
        """Get the highest supported TLS protocol version.

        :return: the highest supported TLS protocol version
        :rtype: P4G_TLS_PROTOCOL_VER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))

    def set(self, tls_version: TLSVersion) -> "Token":
        """Set the highest supported TLS protocol version.

        :param tls_version:  the highest supported TLS protocol version
        :type tls_version: TLSVersion
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._group_xindex], tls_version=tls_version))

    set_sslv3 = functools.partialmethod(set, TLSVersion.SSLV3)
    """The highest supported TLS protocol version is set to SSLv3."""
    set_tls10 = functools.partialmethod(set, TLSVersion.TLS10)
    """The highest supported TLS protocol version is set to TLS 1.0."""
    set_tls11 = functools.partialmethod(set, TLSVersion.TLS11)
    """The highest supported TLS protocol version is set to TLS 1.1."""
    set_tls12 = functools.partialmethod(set, TLSVersion.TLS12)
    """The highest supported TLS protocol version is set to TLS 1.2."""


@register_command
@dataclass
class P4G_TLS_MIN_REQ_PROTOCOL_VER:
    """
    Returns the minimum TLS protocol version required by the configured list of
    cipher suites. Each cipher suite has a minimum required TLS protocol version
    that will support the cipher suite. The minimum required TLS protocol version
    for a list of cipher suites is the lowest minimum required TLS protocol version
    of all the cipher suites in the list.
    """

    code: typing.ClassVar[int] = 1119
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _group_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        tls_version: XmpField[XmpByte] = XmpField(XmpByte, choices=TLSVersion)  # coded byte, minimum required TLS protocol version

    def get(self) -> "Token[GetDataAttr]":
        """Get the minimum TLS protocol version required by the configured list of cipher suites. 

        :return: the minimum TLS protocol version required by the configured list of cipher suites. 
        :rtype: P4G_TLS_MIN_REQ_PROTOCOL_VER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._group_xindex]))


