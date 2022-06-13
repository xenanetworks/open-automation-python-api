#: Chassis Commands

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
class C_LOGON:
    """
    You log on to the chassis by setting the value of this command to the correct
    password for the chassis. All other commands will fail if the session has not
    been logged on.
    """

    code: typing.ClassVar[int] = 1
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        password: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the password value.

    def set(self, password: str) -> "Token":
        """Set the password for creating a tester management session and logging on to the tester.

        :param password: password for creating a tester management session and logging on to the tester.
        :type password: str
        """
        return Token(self._connection, build_set_request(self, password=password))


@register_command
@dataclass
class C_OWNER:
    """
    Identify the owner of the management session. The name can be any short quoted
    string up to eight characters long. This name will be used when reserving ports
    prior to updating their configuration. There is no authentication of the users,
    and the chassis does not have any actual user accounts. Multiple concurrent
    connections may use the same owner name, but only one connection can have any
    particular resource reserved at any given time. Until an owner is specified the
    chassis configuration can only be read. Once specified, the session can reserve
    ports for that owner, and will inherit any existing reservations for that owner
    retained at the chassis. Maximum 32 ASCII characters.
    """

    code: typing.ClassVar[int] = 2
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        username: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the name of the owner of this session.

    @dataclass(frozen=True)
    class GetDataAttr:
        username: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the name of the owner of this session.

    def get(self) -> "Token[GetDataAttr]":
        """Get the username of this chassis management session.

        :return: The username of this chassis management session.
        :rtype: C_OWNER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, username: str) -> "Token":
        """Set the username of this chassis management session.

        :param username: the username of this chassis management session.
        :type username: str
        """
        return Token(self._connection, build_set_request(self, username=username))


@register_command
@dataclass
class C_KEEPALIVE:
    """
    You can request this value from the chassis, simply to let it (as well as and
    any routers and proxies between you) know that the connection is still valid.
    """

    code: typing.ClassVar[int] = 3
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        tick_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, an increasing number from the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Get the tick count value.

        :return: an increasing number from the chassis.
        :rtype: C_KEEPALIVE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_TIMEOUT:
    """
    The maximum number of idle seconds allowed before the connection is timed out by
    the tester.
    """

    code: typing.ClassVar[int] = 4
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        second_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the maximum idle interval, default is 130 seconds.

    @dataclass(frozen=True)
    class GetDataAttr:
        second_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the maximum idle interval, default is 130 seconds.

    def get(self) -> "Token[GetDataAttr]":
        """Get the timeout value.

        :return: the maximum idle interval, default is 130 seconds. 
        :rtype: C_TIMEOUT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, second_count: int) -> "Token":
        """Set the timeout value.

        :param second_count: the maximum idle interval, default is 130 seconds.
        :type second_count: int
        """
        return Token(self._connection, build_set_request(self, second_count=second_count))


@register_command
@dataclass
class C_RESERVATION:
    """
    You set this command to reserve, release, or relinquish the chassis itself.
    The chassis must be reserved before any of the chassis-level parameters can be
    changed. The owner of the session must already have been specified.
    Reservation will fail if any modules or ports are reserved for other users.
    
    NOTICE: Before reserve Tester need to reserve all the ports on it, otherwise 
    ``<STATUS_NOTVALID>``
    """

    code: typing.ClassVar[int] = 5
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        operation: XmpField[XmpByte] = XmpField(
            XmpByte, choices=ReservedAction
        )  # coded byte, containing the operation to perform. The reservation parameters are asymmetric with respect to set/get. When set, it contains the operation to perform. When get, it contains the status.

    @dataclass(frozen=True)
    class GetDataAttr:
        operation: XmpField[XmpByte] = XmpField(
            XmpByte, choices=ReservedStatus
        )  # coded byte, containing the operation to perform. The reservation parameters are asymmetric with respect to set/get. When set, it contains the operation to perform. When get, it contains the status.

    def get(self) -> "Token[GetDataAttr]":
        """Get the chassis reservation status.

        :return: the status of chassis reservation.
        :rtype: C_RESERVATION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, operation: ReservedAction) -> "Token":
        """Set the chassis reservation operation to be performed.

        :param operation: reservation operation to be performed.
        :type operation: ReservedAction
        """
        return Token(self._connection, build_set_request(self, operation=operation))

    set_release = functools.partialmethod(set, ReservedAction.RELEASE)
    """Release the ownership of the tester.
    """
    set_reserve = functools.partialmethod(set, ReservedAction.RESERVE)
    """Reserve the tester.
    """
    set_relinquish = functools.partialmethod(set, ReservedAction.RELINQUISH)
    """Release the ownership of the tester from another user.
    """


@register_command
@dataclass
class C_RESERVEDBY:
    """
    Identify the user who has the chassis reserved. The empty string if the chassis
    is not currently reserved.
    """

    code: typing.ClassVar[int] = 6
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        username: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the name of the current owner of the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Get the username of the current owner of the tester.

        :return: the username of the current owner of the tester.
        :rtype: C_RESERVEDBY.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_LOGOFF:
    """
    Terminates the current scripting session. Courtesy only, the chassis will also
    handle disconnection at the TCP/IP level
    """

    code: typing.ClassVar[int] = 7
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Log off from the tester and close the management session.
        """
        return Token(self._connection, build_set_request(self))


@register_command
@dataclass
class C_DOWN:
    """
    Shuts down the chassis, and either restarts it in a clean state or leaves it
    powered off.
    """

    code: typing.ClassVar[int] = 8
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        magic: XmpField[XmpInt] = XmpField(XmpInt)  # integer, must be the special value -1480937026.
        operation: XmpField[XmpByte] = XmpField(XmpByte, choices=ChassisShutdownAction)  # coded byte, what to do after shutting chassis down.

    def set(self, operation: ChassisShutdownAction) -> "Token":
        """Shuts down the chassis, and either restarts it in a clean state or leaves it powered off.

        :param operation: what to do after shutting chassis down.
        :type operation: ChassisShutdownAction
        """
        return Token(self._connection, build_set_request(self, magic=-1480937026, operation=operation))

    set_restart = functools.partialmethod(set, ChassisShutdownAction.RESTART)
    """Shuts down the tester and then restarts it.
    """
    set_poweroff = functools.partialmethod(set, ChassisShutdownAction.POWEROFF)
    """Shuts down the tester and leaves it powered off.
    """


@register_command
@dataclass
class C_CAPABILITIES:
    """
    A series of integer values specifying various internal limits (aka.
    capabilities) of the chassis.
    """

    code: typing.ClassVar[int] = 9
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        version: XmpField[XmpInt] = XmpField(XmpInt)  # integer, chassis software build number.
        max_name_len: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max ASCII characters in chassis name.
        max_comment_len: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max ASCII characters in chassis comment.
        max_password_len: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max ASCII characters in chassis password.
        max_ext_rate: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum rate for external traffic.
        max_session_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max number of management and scripting sessions.
        max_chain_depth: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max chain index.
        max_module_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum number of L23 modules.
        max_protocol_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max protocol segments in a packet.
        can_stream_based_arp: XmpField[XmpInt] = XmpField(XmpInt)  # integer, does server support stream-based ARP/NDP?
        can_sync_traffic_start: XmpField[XmpInt] = XmpField(XmpInt)  # integer, does server support synchronous traffic start?
        can_read_log_files: XmpField[XmpInt] = XmpField(XmpInt)  # integer, can clients read debug log files from server?
        can_par_module_upgrade: XmpField[XmpInt] = XmpField(XmpInt)  # integer, can server handle parallel module upgrades?
        can_upgrade_timekeeper: XmpField[XmpInt] = XmpField(XmpInt)  # integer, is server capable of upgrading the TimeKeeper application?
        can_custom_defaults: XmpField[XmpInt] = XmpField(XmpInt)  # integer, can server handle custom default values for XMP parameters?
        can_latency_f2f: XmpField[XmpInt] = XmpField(XmpInt)  # integer, can server handle first-to-first latency mode?
        max_owner_name_length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, max number of ASCII characters in C_OWNER name
        can_read_temperatures: XmpField[XmpInt] = XmpField(XmpInt)  # integer, can the server read out chassis and/or CPU temperatures? (C_TEMPERATURE ?)

    def get(self) -> "Token[GetDataAttr]":
        """Get the internal limits (capabilities) of the tester.

        :return: A series of integer values specifying various internal limits
            - chassis software build number
            - max ASCII characters in chassis name
            - max ASCII characters in chassis comment
            - max ASCII characters in chassis password
            - maximum rate for external traffic
            - max number of management and scripting sessions
            - max chain index
            - maximum number of L23 modules 
            - max protocol segments in a packet
            - does server support stream-based ARP/NDP?
            - does server support synchronous traffic start?
            - can clients read debug log files from server?
            - can server handle parallel module upgrades?
            - is server capable of upgrading the TimeKeeper application?
            - can server handle custom default values for XMP parameters?
            - can server handle first-to-first latency mode?
            - max number of ASCII characters in ``C_OWNER`` name
            - can the server read out chassis and/or CPU temperatures?

        :rtype: C_CAPABILITIES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_MODEL:
    """
    Gets the specific model of this Xena chassis.
    """

    code: typing.ClassVar[int] = 10
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        model: XmpField[XmpStr] = XmpField(XmpStr)  # string, the Xena model designation for the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Get the model of this Xena tester.

        :return: the model of the Xena tester
        :rtype: C_MODEL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_SERIALNO:
    """
    Gets the unique serial number of this particular Xena chassis.
    """

    code: typing.ClassVar[int] = 11
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        serial_number: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the serial number of this chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Get the serial number of this Xena tester.

        :return: the serial number of the Xena tester 
        :rtype: C_SERIALNO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_VERSIONNO:
    """
    Gets the major version numbers for the chassis firmware and the Xena PCI
    driver installed on the chassis.
    """

    code: typing.ClassVar[int] = 12
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        chassis_major_version: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the chassis firmware major version number.
        pci_driver_version: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the cXena PCI driver version.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the major version numbers for the tester firmware and the Xena PCI driver installed on the chassis.

        :return: the firmware major version number of the tester and the PCI driver version
        :rtype: C_VERSIONNO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_PORTCOUNTS:
    """
    Gets the number of ports in each module slot of the chassis, and indirectly
    the number of slots and modules.
    
    .. note::
    
        CFP modules return the number 8 which is the maximum number of 10G ports, but the actual number of ports can be configured dynamically using the :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIG` command.

    """

    code: typing.ClassVar[int] = 13
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        port_counts: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of bytes, the number of ports, typically 2 or 6, or 0 for an empty slot.

    def get(self) -> "Token[GetDataAttr]":
        """Get the number of ports in each module slot of the tester, and indirectly the number of slots and modules.

        :return: the number of ports of each module slot of the tester, 0 for an empty slot.
        :rtype: C_PORTCOUNTS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_PORTERRORS:
    """
    Gets the number of errors detected across all streams on each port of each
    test module of the chassis. The counts are ordered in sequence with those of
    the module in the lowest numbered chassis slot first. Empty slots are skipped
    so that a chassis with a 6-port and a 2-port test module will return eight
    counts regardless of which slots they are in.
    
    .. note::
    
        CFP modules return eight error counts since they can be configured as up to eight 10G ports. When in 100G and 40G mode only the first one or two counts are significant.
    
    .. note::
        
        FCS errors are included, which leads to double-counting for streams detecting lost packets using the test payload mechanism.

    """

    code: typing.ClassVar[int] = 16
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        error_count: XmpField[XmpLongList] = XmpField(XmpLongList)  # list of long integers, the total number of errors across all streams, and including FCS errors.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the number of errors detected across all streams on each port of each
        test module of the chassis. The counts are ordered in sequence with those of
        the module in the lowest numbered chassis slot first. Empty slots are skipped
        so that a chassis with a 6-port and a 2-port test module will return eight
        counts regardless of which slots they are in.

        :return: the total number of errors across all streams, and including FCS errors.
        :rtype: C_PORTERRORS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_REMOTEPORTCOUNTS:
    """
    Gets the number of ports of each remote module. A remote module is a
    relative to the xenaserver, for example, xenal47server. The first integer in
    the returned list is always 0 because it represents the xenaserver, which is
    not a remote module.
    """

    code: typing.ClassVar[int] = 17
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        port_counts: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of bytes, the number of ports, typically 2 or 6, or 0 for an empty slot.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the number of ports of each remote module. A remote module is a
        relative to the xenaserver, for example, xenal47server. The first integer in
        the returned list is always 0 because it represents the xenaserver, which is
        not a remote module.

        :return: the number of ports of each module slot of the tester, 0 for an empty slot.
        :rtype: C_REMOTEPORTCOUNTS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_BUILDSTRING:
    """
    Identify the hostname of the PC that builds the xenaserver. It uniquely
    identifies the build of a xenaserver.
    """

    code: typing.ClassVar[int] = 19
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        build_string: XmpField[XmpStr] = XmpField(XmpStr)  # string, identify the hostname of the PC that builds the xenaserver

    def get(self) -> "Token[GetDataAttr]":
        """Get the build string of the xenaserver.

        :return: build string that identifies the hostname of the PC that builds the xenaserver
        :rtype: C_BUILDSTRING.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_NAME:
    """
    The name of the chassis, as it appears at various places in the user interface.
    The name is also used to distinguish the various chassis contained within a
    testbed  and in files containing the configuration for an entire test case.
    """

    code: typing.ClassVar[int] = 20
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        chassis_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the name of the chassis.

    @dataclass(frozen=True)
    class GetDataAttr:
        chassis_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the name of the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Get the name of the tester

        :return: the name of the tester
        :rtype: C_NAME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, chassis_name: str) -> "Token":
        """Set the name of the tester

        :param chassis_name: the name of the tester
        :type chassis_name: str
        """
        return Token(self._connection, build_set_request(self, chassis_name=chassis_name))


@register_command
@dataclass
class C_COMMENT:
    """
    The description of the chassis.
    """

    code: typing.ClassVar[int] = 21
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the description of the chassis.

    @dataclass(frozen=True)
    class GetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the description of the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Get the description of the tester.

        :return: the description of the tester
        :rtype: C_COMMENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, comment: str) -> "Token":
        """Set the description of the tester.

        :param comment: the description of the tester
        :type comment: str
        """
        return Token(self._connection, build_set_request(self, comment=comment))


@register_command
@dataclass
class C_PASSWORD:
    """
    The password of the chassis, which must be provided when logging on to the chassis.
    """

    code: typing.ClassVar[int] = 22
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        password: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the password for the chassis.

    @dataclass(frozen=True)
    class GetDataAttr:
        password: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the password for the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Get the password of the tester.

        :return: the password of the tester
        :rtype: C_PASSWORD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, password: str) -> "Token":
        """Set the password of the tester.

        :param password: the password of the tester
        :type password: str
        """
        return Token(self._connection, build_set_request(self, password=password))


@register_command
@dataclass
class C_IPADDRESS:
    """
    The network configuration parameters of the chassis management port.
    """

    code: typing.ClassVar[int] = 24
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the static IP address of the chassis.
        subnet_mask: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the subnet mask of the local network segment.
        gateway: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the gateway of the local network segment.

    @dataclass(frozen=True)
    class GetDataAttr:
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the static IP address of the chassis.
        subnet_mask: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the subnet mask of the local network segment.
        gateway: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, the gateway of the local network segment.

    def get(self) -> "Token[GetDataAttr]":
        """Get the IP configuration information of the tester.

        :return:
            - the static IP address of the chassis
            - the subnet mask of the local network segment
            - the gateway of the local network segment
        :rtype: C_IPADDRESS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(
        self,
        ipv4_address: typing.Union[str, int, ipaddress.IPv4Address],
        subnet_mask: typing.Union[str, int, ipaddress.IPv4Address],
        gateway: typing.Union[str, int, ipaddress.IPv4Address],
    ) -> "Token":
        """the IP configuration information of the tester.

        :param ipv4_address: the static IP address of the chassis
        :type ipv4_address: typing.Union[str, int, ipaddress.IPv4Address]
        :param subnet_mask: the subnet mask of the local network segment
        :type subnet_mask: typing.Union[str, int, ipaddress.IPv4Address]
        :param gateway: the gateway of the local network segment
        :type gateway: typing.Union[str, int, ipaddress.IPv4Address]
        """
        return Token(self._connection, build_set_request(self, ipv4_address=ipv4_address, subnet_mask=subnet_mask, gateway=gateway))


@register_command
@dataclass
class C_DHCP:
    """
    Controls whether the chassis will use DHCP to get the management IP address.
    """

    code: typing.ClassVar[int] = 25
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether DHCP is enabled or disabled.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether DHCP is enabled or disabled.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether DHCP is enabled for getting management IP.

        :return: whether DHCP is enabled.
        :rtype: C_DHCP.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, on_off: OnOff) -> "Token":
        """Set DHCP for getting management IP.

        :param on_off: whether DHCP is enabled or disabled.
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable DHCP for for getting management IP.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable on to DHCP for for getting management IP.
    """


@register_command
@dataclass
class C_MACADDRESS:
    """
    Get the MAC address for the chassis management port.
    """

    code: typing.ClassVar[int] = 26
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # six hex bytes, indicating the MAC address

    def get(self) -> "Token[GetDataAttr]":
        """Get the MAC address for the chassis management port.

        :return: the MAC address for the chassis management port
        :rtype: C_MACADDRESS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_HOSTNAME:
    """
    Get or set the chassis hostname used when DHCP is enabled.
    """

    code: typing.ClassVar[int] = 27
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        hostname: XmpField[XmpStr] = XmpField(XmpStr)  # string, hostname for chassis (default value "xena-")

    @dataclass(frozen=True)
    class GetDataAttr:
        hostname: XmpField[XmpStr] = XmpField(XmpStr)  # string, hostname for chassis (default value "xena-")

    def get(self) -> "Token[GetDataAttr]":
        """Get the chassis hostname used when DHCP is enabled.

        :return: the chassis hostname
        :rtype: C_HOSTNAME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, hostname: str) -> "Token":
        """Set the chassis hostname.

        :param hostname: the chassis hostname
        :type hostname: str
        """
        return Token(self._connection, build_set_request(self, hostname=hostname))


@register_command
@dataclass
class C_FLASH:
    """
    Make all the test port LEDs flash on and off with a 1-second interval. This is
    helpful if you have multiple chassis mounted side by side and you need to
    identify a specific one.

    NOTICE: Require Tester to be reserved before change value.
    """

    code: typing.ClassVar[int] = 28
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, determines whether to blink all test port LEDs.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, determines whether to blink all test port LEDs.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of test port LEDs.

        :return: the blinking status of test port LEDs
        :rtype: C_FLASH.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, on_off: OnOff) -> "Token":
        """Set test ports LEDs blinking status.

        :param on_off: determines whether to blink all test port LEDs.
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable flashing test port LEDs.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable flashing test port LEDs.
    """


@register_command
@dataclass
class C_DEBUGLOGS:
    """
    Allows to dump all the logs of a chassis.
    """

    code: typing.ClassVar[int] = 30
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        message_length: XmpField[XmpInt] = XmpField(XmpInt)  # integer, length of the message.

        data: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, all the logs of a chassis

    def get(self) -> "Token[GetDataAttr]":
        """Get chassis logs.

        :return: length of the message and all the logs of the chassis
        :rtype: C_DEBUGLOGS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_TEMPERATURE:
    """
    Get chassis temperature readings, if supported. Unit is millidegree Celsius.
    """

    code: typing.ClassVar[int] = 31
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        mb1_temperature: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the temperature of motherboard 1. Unit is millidegree Celsius.

        mb2_temperature: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the temperature of motherboard 2. Unit is millidegree Celsius.

        cpu_temperature: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the temperature of CPU. Unit is millidegree Celsius.

    def get(self) -> "Token[GetDataAttr]":
        """Get chassis temperature readings.

        :return:
            - the temperature of motherboard 1 (millidegree Celsius)
            - the temperature of motherboard 2 (millidegree Celsius)
            - the temperature of CPU (millidegree Celsius)
        :rtype: C_TEMPERATURE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_RESTPORT:
    """
    The TCP port used by the REST API server.
    """

    code: typing.ClassVar[int] = 32
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        tcp_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, containing the TCP port number (default 57911)

    @dataclass(frozen=True)
    class GetDataAttr:
        tcp_port: XmpField[XmpInt] = XmpField(XmpInt)  # integer, containing the TCP port number (default 57911)

    def get(self) -> "Token[GetDataAttr]":
        """Get the TCP port number used by the REST API server.

        :return: the TCP port number used by the REST API server
        :rtype: XmpInt
        """
        return Token(self._connection, build_get_request(self))

    def set(self, tcp_port: int) -> "Token":
        """Set the TCP port number used by the REST API server.

        :param tcp_port: the TCP port number (default 57911)
        :type tcp_port: int
        """
        return Token(self._connection, build_set_request(self, tcp_port=tcp_port))


@register_command
@dataclass
class C_RESTENABLE:
    """
    Controls whether the chassis will run REST API server or not. The command takes
    affect only after chassis reset. To start/stop REST API server use ``C_RESTCONTROL`` command.
    """

    code: typing.ClassVar[int] = 33
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, determines whether REST API server should be enabled or disabled.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, determines whether REST API server should be enabled or disabled.

    def get(self) -> "Token[GetDataAttr]":
        """Get the On/Off status of the REST API server.

        :return: the status of the REST API server, whether it is enabled.
        :rtype: XmpByte
        """
        return Token(self._connection, build_get_request(self))

    def set(self, on_off: OnOff) -> "Token":
        """Set the On/Off status of the REST API server.

        :param on_off: determines whether REST API server should be enabled or disabled
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the REST API server.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the REST API server.
    """


@register_command
@dataclass
class C_RESTCONTROL:
    """
    Controls REST API server. This command should be used with extra care as it can
    affect other users using the server.
    """

    code: typing.ClassVar[int] = 34
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        operation: XmpField[XmpByte] = XmpField(XmpByte, choices=RESTControlAction)  # coded byte, what to do with the REST API server.

    def set(self, operation: RESTControlAction) -> "Token":
        """Controlling the REST API server.

        :param operation: what to do with the REST API server
        :type operation: RESTControlAction
        """
        return Token(self._connection, build_set_request(self, operation=operation))


@register_command
@dataclass
class C_RESTSTATUS:
    """
    Gets the REST API server operation status - whether it is active (running) or
    not. To get the admin status (whether the server is enabled or disabled) use
    ``C_RESTCONTROL`` command.
    """

    code: typing.ClassVar[int] = 35
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=ServiceStatus)  # coded byte, determines the REST API server running status.

    def get(self) -> "Token[GetDataAttr]":
        """Get the operation status of th REST API server.

        :return: the operation status of th REST API server
        :rtype: C_RESTSTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_WATCHDOG:
    """
    If the chassis stalls for a long time, when the timer expires the chassis will
    be rebooted automatically.
    """

    code: typing.ClassVar[int] = 36
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        timer_value: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the timer value that reboots the chassis. Unit = second.

    @dataclass(frozen=True)
    class GetDataAttr:
        timer_value: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the timer value that reboots the chassis. Unit = second.

    def get(self) -> "Token[GetDataAttr]":
        """Get the time value that reboots the chassis if it stalls for a long time.

        :return: the timer value that reboots the chassis. Unit = second.
        :rtype: C_WATCHDOG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, timer_value: int) -> "Token":
        """Set the time value that reboots the chassis if it stalls for a long time. 

        :param timer_value: the timer value that reboots the chassis
        :type timer_value: int
        """
        return Token(self._connection, build_set_request(self, timer_value=timer_value))


@register_command
@dataclass
class C_INDICES:
    """
    Gets the session indices for all current sessions on the chassis.
    """

    code: typing.ClassVar[int] = 40
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        session_ids: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, the session indices for all current sessions on the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the session indices for all current sessions on the chassis. 

        :return: the session indices for all current sessions on the chassis
        :rtype: C_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_STATSESSION:
    """
    Gets information and statistics for a particular session on the chassis.
    """

    code: typing.ClassVar[int] = 41
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    session_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        session_type: XmpField[XmpInt] = XmpField(XmpInt, choices=ChassisSessionType)  # coded integer, which kind of session.
        ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # address, client IP address.
        owner: XmpField[XmpStr] = XmpField(XmpStr)  # string, the name of the session owner.
        operation_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of operations done during the session.
        requested_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes received by the chassis.
        responded_byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of bytes sent by the chassis.

    def get(self) -> "Token[GetDataAttr]":
        """Gets information and statistics for a particular session on the chassis.

        :return:
            - type of session
            - client IP address
            - the name of the session owner
            - number of operations done during the session
            - number of bytes received by the chassis
            - number of bytes sent by the chassis
        :rtype: C_STATSESSION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, indices=[self.session_xindex]))


@register_command
@dataclass
class C_TKLICFILE:
    """
    Get Xena TimeKeeper license file content.
    """

    code: typing.ClassVar[int] = 49
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        license_content: XmpField[XmpByteList] = XmpField(XmpByteList)  # ToDo: probably wrong type

    @dataclass(frozen=True)
    class GetDataAttr:
        license_content: XmpField[XmpByteList] = XmpField(XmpByteList)  # ToDo: probably wrong type

    def get(self) -> "Token[GetDataAttr]":
        """Get Xena TimeKeeper license file content. 

        :return: Xena TimeKeeper license file content
        :rtype: C_TKLICFILE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, license_content: str) -> "Token":
        """Set Xena TimeKeeper license file content.

        :param license_content: Xena TimeKeeper license file content
        :type license_content: str
        """
        return Token(self._connection, build_set_request(self, license_content=license_content))


@register_command
@dataclass
class C_TKLICSTATE:
    """
    Get the state of the Xena TimeKeeper license file content.
    """

    code: typing.ClassVar[int] = 50
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        license_file_state: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeKeeperLicenseFileState)  # coded byte, timekeeper license state.

        license_type: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeKeeperLicenseType)  # coded byte, license type.

        license_errors: XmpField[XmpIntList] = XmpField(XmpIntList, choices=TimeKeeperLicenseError)  # coded integers, license errors.

    def get(self) -> "Token[GetDataAttr]":
        """Get the state of the Xena TimeKeeper license file content.

        :return:
            - timekeeper license state
            - license type
            - license errors
        :rtype: C_TKLICSTATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_FILESTART:
    """
    Initiates upload of a file to the chassis. This command should be followed by
    a sequence og ``C_FILEDATA`` parameters to provide the file content, and finally a
    ``C_FILEFINISH`` to commit the new file to the chassis.
    """

    code: typing.ClassVar[int] = 51
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        file_type: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, little-endian integer, the file type, should be 1.
        size: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, little-endian integer, the number of bytes in the file.
        time: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, little-endian integer, the Linux date+time of the file.
        mode: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, little-endian integer, the Linux permissions of the file.
        checksum: XmpField[XmpHex4] = XmpField(XmpHex4)  # four hex bytes, little-endian integer, the checksum of the file.
        name: XmpField[XmpStr] = XmpField(XmpStr)  # string, the name and location of the file, as a full path.

    def set(self, file_type: str, size: str, time: str, mode: str, checksum: str, name: str) -> "Token":
        """Initiates upload of a file to the chassis.

        :param file_type: the file type, should be 1
        :type file_type: str
        :param size: the number of bytes in the file
        :type size: str
        :param time: he Linux date+time of the file
        :type time: str
        :param mode: the Linux permissions of the file
        :type mode: str
        :param checksum: the checksum of the file
        :type checksum: str
        :param name: the name and location of the file, as a full path
        :type name: str
        """
        return Token(self._connection, build_set_request(self, file_type=file_type, size=size, time=time, mode=mode, checksum=checksum, name=name))


@register_command
@dataclass
class C_FILEDATA:
    """
    Uploads a fragment of a file to the chassis.
    """

    code: typing.ClassVar[int] = 52
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        offset: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the position within the file.
        data_bytes: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, the data content of a section of the file.

    def set(self, offset: int, data_bytes: str) -> "Token":
        """Uploads a fragment of a file to the chassis.

        :param offset: the position within the file
        :type offset: int
        :param data_bytes: the data content of a section of the file
        :type data_bytes: str
        """
        return Token(self._connection, build_set_request(self, offset=offset, data_bytes=data_bytes))


@register_command
@dataclass
class C_FILEFINISH:
    """
    Completes upload of a file to the chassis. After validation it will replace any
    existing file with the same name.
    """

    code: typing.ClassVar[int] = 53
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        magic: XmpField[XmpInt] = XmpField(XmpInt)  # integer, must be the special value -1480937026.

    def set(self) -> "Token":
        """Completes upload of a file to the chassis. After validation it will replace any existing file with the same name.
        """
        return Token(self._connection, build_set_request(self, magic=-1480937026))


@register_command
@dataclass
class C_TRAFFIC:
    """
    Starts or stops the traffic on a number of ports on the chassis simultaneously.
    The ports are identified by pairs of integers (module port).
    """

    code: typing.ClassVar[int] = 55
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, determines whether to start or stop traffic generation.
        module_ports: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, specifies ports on modules, which should stop or start generating traffic.

    def set(self, on_off: OnOff, module_ports: typing.List[int]) -> "Token":
        """Starts or stops the traffic on a number of ports on the chassis simultaneously.

        :param on_off: determines whether to start or stop traffic generation
        :type on_off: OnOff
        :param module_ports: specifies ports on modules, which should stop or start generating traffic
        :type module_ports: typing.List[int]
        """
        return Token(self._connection, build_set_request(self, on_off=on_off, module_ports=module_ports))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Stop the traffic on a number of ports on the chassis simultaneously.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Start the traffic on a number of ports on the chassis simultaneously.
    """


@register_command
@dataclass
class C_VERSIONNO_MINOR:
    """
    Gets the minor version number for the chassis firmware. The full version of
    the chassis firmware is thus where the number is obtained  with the ``C_VERSIONNO``
    command and the number is obtained with the ``C_VERSIONNO_MINOR`` command.
    """

    code: typing.ClassVar[int] = 56
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        chassis_minor_version: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the chassis firmware minor version number.
        reserved_1: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved.
        reserved_2: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved.

    def get(self) -> "Token[GetDataAttr]":
        """Get the minor version number for the chassis firmware.

        :return:
            - the minor version number for the chassis firmware
            - reserved, 0
            - reserved, 0
        :rtype: C_VERSIONNO_MINOR.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_START:
    """
    Start traffic on N ports and each port is described by (module index, port
    index).
    """

    code: typing.ClassVar[int] = 60
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        module_ports: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of bytes, specifies ports on modules, which should stop or start generating traffic.

    def set(self, module_ports: typing.List[int]) -> "Token":
        """Start traffic on N ports and each port is described by (module index, port index).

        :param module_ports: specifies ports on modules, which should stop or start generating traffic
        :type module_ports: typing.List[int]
        """
        return Token(self._connection, build_set_request(self, module_ports=module_ports))


@register_command
@dataclass
class C_STOP:
    """
    Stop traffic on N ports and each port is described by (module index, port index)
    """

    code: typing.ClassVar[int] = 61
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        module_ports: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of bytes, specifies ports on modules, which should stop or start generating traffic.

    def set(self, module_ports: typing.List[int]) -> "Token":
        """Stop traffic on N ports and each port is described by (module index, port index).

        :param module_ports: specifies ports on modules, which should stop or start generating traffic
        :type module_ports: typing.List[int]
        """
        return Token(self._connection, build_set_request(self, module_ports=module_ports))


@register_command
@dataclass
class C_MULTIUSER:
    """
    Enable or disable the ability to control one resource from several different TCP
    connections.
    """

    code: typing.ClassVar[int] = 62
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(
            XmpByte, choices=OnOff
        )  # coded byte, enable or disable the ability to control one resource from several different TCP connections

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(
            XmpByte, choices=OnOff
        )  # coded byte, enable or disable the ability to control one resource from several different TCP connections

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of the ability to control one resource from several different TCP connections.

        :return: the status of the ability to control one resource from several different TCP connections
        :rtype: C_MULTIUSER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, on_off: OnOff) -> "Token":
        """Enable or disable the ability to control one resource from several different TCP connections.

        :param on_off: enable or disable the ability to control one resource from several different TCP connections
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the ability to control one resource from several different TCP.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the ability to control one resource from several different TCP.
    """


@register_command
@dataclass
class C_SCRIPT:
    """
    To load and save CLI commands e.g. port configuration, through the binary XMP session.
    """

    code: typing.ClassVar[int] = 64
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        command_string: XmpField[XmpStr] = XmpField(XmpStr)  # string, text CLI command

    def set(self, command_string: str) -> "Token":
        """Set the CLI commands through a binary XMP session.

        :param command_string: text CLI command
        :type command_string: str
        """
        return Token(self._connection, build_set_request(self, command_string=command_string))


@register_command
@dataclass
class C_TKSTATUS:
    """
    Report TimeKeeper version and status.
    """

    code: typing.ClassVar[int] = 65
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        status_string: XmpField[XmpStr] = XmpField(
            XmpStr
        )  # string. Version, TimeKeeper license expiration, and TimeKeeper status. The string is formatted as shown in the example below. Each line is separated by \n.

        # TimeKeeper Status\n
        # ================================================================================\n
        # TimeKeeper version 8.0.3\n
        # License expires in 33 days (including grace period)\n
        # TimeKeeper is not running\n

    def get(self) -> "Token[GetDataAttr]":
        """Get the version and status of TimeKeeper

        :return:
            Version, TimeKeeper license expiration, and TimeKeeper status. The string is formatted as shown in the example below.
            
            The format is shown below.
        
            TimeKeeper Status
            TimeKeeper version 8.0.3
            License expires in 33 days (including grace period)
            TimeKeeper is not running

        :rtype: C_TKSTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_TKSVCSTATE:
    """
    Get and control TimeKeeper service state.
    """

    code: typing.ClassVar[int] = 66
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        state: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeKeeperServiceAction)  # coded byte, TimeKeeper service state

    @dataclass(frozen=True)
    class GetDataAttr:
        state: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeKeeperServiceStatus)  # coded byte, TimeKeeper service state

    def get(self) -> "Token[GetDataAttr]":
        """Get TimeKeeper service state

        :return: TimeKeeper service state
        :rtype: C_TKSVCSTATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, state: TimeKeeperServiceAction) -> "Token":
        """Control TimeKeeper service state

        :param state: TimeKeeper service state
        :type state: TimeKeeperServiceAction
        """
        return Token(self._connection, build_set_request(self, state=state))

    set_stop = functools.partialmethod(set, TimeKeeperServiceAction.STOP)
    """Stop the TimerKeeper service.
    """
    set_start = functools.partialmethod(set, TimeKeeperServiceAction.START)
    """Start the TimerKeeper service.
    """
    set_restart = functools.partialmethod(set, TimeKeeperServiceAction.RESTART)
    """Restart the TimerKeeper service.
    """


@register_command
@dataclass
class C_TKCONFIG:
    """
    TimeKeeper config file content.
    """

    code: typing.ClassVar[int] = 67
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        config_file: XmpField[XmpStr] = XmpField(XmpStr)  # string, TimeKeeper config file content

    @dataclass(frozen=True)
    class GetDataAttr:
        config_file: XmpField[XmpStr] = XmpField(XmpStr)  # string, TimeKeeper config file content

    def get(self) -> "Token[GetDataAttr]":
        """Get TimeKeeper config file content.

        :return: TimeKeeper config file content
        :rtype: C_TKCONFIG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, config_file: str) -> "Token":
        """Set TimeKeeper config file content.

        :param config_file: TimeKeeper config file content
        :type config_file: str
        """
        return Token(self._connection, build_set_request(self, config_file=config_file))


@register_command
@dataclass
class C_TKGPSSTATE:
    """
    Get TimeKeeper GPS status.
    """

    code: typing.ClassVar[int] = 68
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpStr] = XmpField(XmpStr)  # string, TimeKeeper GPS status

    def get(self) -> "Token[GetDataAttr]":
        """Get TimeKeeper GPS status.

        :return: TimeKeeper GPS status
        :rtype: C_TKGPSSTATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_TIME:
    """
    Get local chassis time in seconds.
    """

    code: typing.ClassVar[int] = 69
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        local_time: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, local chassis time in seconds

    def get(self) -> "Token[GetDataAttr]":
        """Get local chassis time in seconds.

        :return: local chassis time in seconds
        :rtype: C_TIME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_TRAFFICSYNC:
    """
    Works just as the ``C_TRAFFIC`` command described above with an additional option to
    specify  a point in time where traffic should be started. This can be used to
    start traffic simultaneously on multiple chassis. The ports are identified by
    pairs of integers (module port).
    
    .. note::
    
        This requires that the chassis in question all use the TimeKeeper option to keep their CPU clocks synchronized.

    """

    code: typing.ClassVar[int] = 70
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, determines whether to start or stop traffic generation.
        timestamp: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, the time where traffic should be started, expressed as the number of seconds since January 1 2010, 00
        module_ports: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, specifies ports on modules, which should stop or start traffic generation.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, status traffic generation.
        timestamp: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, the time where traffic should be started, expressed as the number of seconds since January 1 2010, 00
        module_ports: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, specifies ports on modules, which should stop or start traffic generation.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of traffic generation.

        :return:
            - status traffic generation
            - the time where traffic should be started, expressed as the number of seconds since January 1 2010, 00
            - ports on modules, which should stop or start traffic generation
        :rtype: C_TRAFFICSYNC.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))

    def set(self, on_off: OnOff, timestamp: int, module_ports: typing.List[int]) -> "Token":
        """Set the status of traffic generation.

        :param on_off: determines whether to start or stop traffic generation
        :type on_off: OnOff
        :param timestamp: the time where traffic should be started, expressed as the number of seconds since January 1 2010, 00
        :type timestamp: int
        :param module_ports: specifies ports on modules, which should stop or start traffic generation.
        :type module_ports: typing.List[int]
        """
        return Token(self._connection, build_set_request(self, on_off=on_off, timestamp=timestamp, module_ports=module_ports))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Stop traffic generation on the given ports simultaneously on different chassis.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Start traffic generation on the given ports simultaneously on different chassis.
    """


@register_command
@dataclass
class C_TKSTATUSEXT:
    """
    Report TimeKeeper version and status (extended version).
    """

    code: typing.ClassVar[int] = 71
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        status_string: XmpField[XmpStr] = XmpField(XmpStr)  # string, extended status in JSON format. The string is formatted as shown in the example below.

        # {
        #     "FormatVersion": 1,
        #     "ApplicationVersion": 452.0,
        #     "TimeKeeperStatus":
        #     {
        #         "systemtimingstatus": "Waiting for good time source",
        #         "syncsource": "NTP",
        #         "sourcestate": "NTP server 10.0.0.110",
        #         "sourceaccuracy": " No updates yet",
        #         "versioninfo": "8.0.3",
        #         "timesincestart": "0 day(s) 0 hours 1 minutes",
        #         "timesinceboot": "0 day(s) 0 hours 2 minutes",
        #         "updatetime": 1637916837
        #     }
        # }

    def get(self) -> "Token[GetDataAttr]":
        """Get the TimeKeeper version and status.

        :return: extended status in JSON format. The string is formatted as shown in the example below.
        
        ```json
        {"FormatVersion": 1, "ApplicationVersion": 452.0, "TimeKeeperStatus": { "systemtimingstatus": "Waiting for good time source", "syncsource": "NTP", "sourcestate": "NTP server 10.0.0.110", "versioninfo": "8.0.3", "timesincestart": "0 day(s) 0 hours 1 minutes", "timesinceboot": "0 day(s) 0 hours 2 minutes", "updatetime": 1637916837 } }
        ```

        :rtype: C_TKSTATUSEXT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


@register_command
@dataclass
class C_EXTNAME:
    """
    Get the chassis extension name.
    """

    code: typing.ClassVar[int] = 450
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"

    @dataclass(frozen=True)
    class GetDataAttr:
        ext_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, chassis extension name

    def get(self) -> "Token[GetDataAttr]":
        """Get the chassis extension name.

        :return: chassis extension name
        :rtype: C_EXTNAME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self))


