#: L23 Module Commands

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
from . import subtypes

@register_command
@dataclass
class M_RESERVATION:
    """
    Set this command to reserve, release, or relinquish a module itself (as
    opposed to its ports). The module must be reserved before its hardware image can
    be upgraded. The owner of the session must already have been specified.
    Reservation will fail if the chassis or any ports are reserved for other users.

    .. note::

        The reservation parameters are slightly asymmetric with respect to set/get. When querying for the current reservation state, the chassis will use these values.

    """

    code: typing.ClassVar[int] = 72
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

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
        """Get the reservation status of the test module.

        :return: the reservation status of the test module
        :rtype: M_RESERVATION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, operation: ReservedAction) -> "Token":
        """Set the reservation status of the test module.

        :param operation: reservation operation to perform
        :type operation: ReservedAction
        """
        return Token(self._connection, build_set_request(self, module=self._module, operation=operation))

    set_release = functools.partialmethod(set, ReservedAction.RELEASE)
    """Release the test module.
    """
    set_reserve = functools.partialmethod(set, ReservedAction.RESERVE)
    """Reserve the test module.
    """
    set_relinquish = functools.partialmethod(set, ReservedAction.RELINQUISH)
    """Release the ownership of the test module from another user.
    """


@register_command
@dataclass
class M_RESERVEDBY:
    """
    Identify the user who has a module reserved. Returns an empty string if the
    module is not currently reserved by anyone.
    """

    code: typing.ClassVar[int] = 73
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        username: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the name of the current owner of the module.

    def get(self) -> "Token[GetDataAttr]":
        """Get the username who has reserved the test module.

        :return: the username who has reserved the test module
        :rtype: M_RESERVEDBY.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_MODEL:
    """
    Gets the legacy model P/N name of a Xena test module.
    """

    code: typing.ClassVar[int] = 75
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        model: XmpField[XmpStr] = XmpField(XmpStr)  # string, the legacy model P/N name of a Xena test module.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the legacy model P/N name of a Xena test module.

        :return: the legacy model P/N name of a Xena test module
        :rtype: M_MODEL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_SERIALNO:
    """
    Gets the unique serial number of a module.
    """

    code: typing.ClassVar[int] = 76
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        serial_number: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the serial number of this module.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the unique serial number of the test module.

        :return: the serial number of this test module
        :rtype: M_SERIALNO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_VERSIONNO:
    """
    Gets the version number of the hardware image installed on a module.
    """

    code: typing.ClassVar[int] = 77
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    @dataclass(frozen=True)
    class GetDataAttr:
        version: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the hardware image version number.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the version number of the hardware image installed on the test module.

        :return: the hardware image version number of the test module
        :rtype: M_VERSIONNO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_STATUS:
    """
    Get status readings for the test module itself.
    """

    code: typing.ClassVar[int] = 79
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        temperature: XmpField[XmpInt] = XmpField(XmpInt)  # integer, temperature of the main hardware chip, in degrees Celsius.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status readings of the test module

        :return: temperature of the main hardware chip, in degrees Celsius
        :rtype: M_STATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_PORTCOUNT:
    """
    Gets the maximum number of ports on a module.

    .. note::

        For a CFP-type module this number refers to the maximum number of ports possible on the module regardless of the media configuration. So if a CFP-type module can be set in for instance either 1x100G mode or 8x10G mode then this command will always return 8. If you want the current number of ports for a CFP-type module you need to read the :class:`~xoa_driver.internals.core.commands.m_commands.M_CFPCONFIG` command which returns the number of current ports.

    """

    code: typing.ClassVar[int] = 80
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        port_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the maximum number of ports.

    def get(self) -> "Token[GetDataAttr]":
        """Gets the maximum number of ports on a module.

        :return: the maximum number of ports on the test module
        :rtype: M_PORTCOUNT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_UPGRADE:
    """
    Transfers a hardware image file from the chassis to a module. This image will
    take effect when the chassis is powered-on the next time. The transfer takes
    approximately 3 minutes, but no further action is required by the client.
    """

    code: typing.ClassVar[int] = 81
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        magic: XmpField[XmpInt] = XmpField(XmpInt)  # integer, must be the special value -1480937026.
        image_name: XmpField[XmpStr] = XmpField(XmpStr)  # string, the fully qualified name of a file previously uploaded to the chassis.

    def set(self, image_name: str) -> "Token":
        """Transfers a hardware image file from the chassis to a module. This image will
        take effect when the chassis is powered-on the next time. The transfer takes
        approximately 3 minutes, but no further action is required by the client.

        :param image_name: the fully qualified name of a file previously uploaded to the chassis
        :type image_name: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, magic=-1480937026, image_name=image_name))


@register_command
@dataclass
class M_UPGRADEPROGRESS:
    """
    Provides a value indicating the current stage of an ongoing hardware image
    upgrade operation. This is for information only; the upgrade operation runs to
    completion by itself. The progress values are pushed to the client without it
    having to request them.
    """

    code: typing.ClassVar[int] = 82
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        progress: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, the current stage within the three phases. 0: Failure. 1-100: Erase completion percentage. 101-200: Write completion percentage. 201-300: Verify completion percentage.

    def get(self) -> "Token[GetDataAttr]":
        """Get the current stage of an ongoing hardware image
        upgrade operation. This is for information only; the upgrade operation runs to
        completion by itself. The progress values are pushed to the client without it
        having to request them.

        :param progress: the current stage within the three phases. 0: Failure. 1-100: Erase completion percentage. 101-200: Write completion percentage. 201-300: Verify completion percentage.
        :type progress: M_UPGRADEPROGRESS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_TIMESYNC:
    """
    Control how the test module timestamp clock is running, either freely in the
    chassis or locked to an external system time. Running with free chassis time
    allows nano-second precision measurements of latencies, but only when the
    transmitting and receiving ports are in the same chassis. Running with locked
    external time enables inter-chassis latency measurements, but can introduce
    small time discontinuities as the test module time is adjusted.
    """

    code: typing.ClassVar[int] = 83
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeSyncMode)  # coded byte, selecting the time sync mode.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeSyncMode)  # coded byte, selecting the time sync mode.

    def get(self) -> "Token[GetDataAttr]":
        """Get the time sync mode of the test module timestamp clock.

        :return: the time sync mode of the test module timestamp clock
        :rtype: M_TIMESYNC.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, mode: TimeSyncMode) -> "Token":
        """Set the time sync mode of the test module timestamp clock.

        :param mode: the time sync mode of the test module timestamp clock
        :type mode: TimeSyncMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, mode=mode))

    set_chassis = functools.partialmethod(set, TimeSyncMode.CHASSIS)
    """Set the time sync mode of the test module to Chassis Mode.
    """
    set_external = functools.partialmethod(set, TimeSyncMode.EXTERNAL)
    """Set the time sync mode of the test module to External Mode.
    """
    set_module = functools.partialmethod(set, TimeSyncMode.MODULE)
    """Set the time sync mode of the test module to Module Mode.
    """


@register_command
@dataclass
class M_CFPTYPE:
    """
    Get information about the transceiver currently inserted into the cages.
    """

    code: typing.ClassVar[int] = 84
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        state: XmpField[XmpByte] = XmpField(XmpByte, choices=CFPState)  # coded byte, specifying the CFP state.
        type: XmpField[XmpByte] = XmpField(XmpByte, choices=CFPType)  # coded byte, specifying the CFP type.

    def get(self) -> "Token[GetDataAttr]":
        """Get CFP type information about the transceiver currently inserted into the cage.

        :return:
            - the CFP state
            - the CFP type
        :rtype: M_CFPTYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_CFPCONFIG:
    """
    The current number of ports and their speed of a CFP test module. If the CFP
    type is NOTFLEXIBLE then it reflects the transceiver currently in the CFP cage.
    If the CFP type is FLEXIBLE (or NOTPRESENT) then the configuration can be changed
    explicitly. The following combinations are possible: 4x10G, 8x10G, 1x40G, 2x40G,
    and 1x100G. (replaced by ``M_CFPCONFIGEXT``)
    """

    code: typing.ClassVar[int] = 85
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        port_count: XmpField[XmpByte] = XmpField(XmpByte)  # byte, number of ports.
        port_speed: XmpField[XmpByte] = XmpField(XmpByte)  # byte, port speed, in Gbps.

    @dataclass(frozen=True)
    class GetDataAttr:
        port_count: XmpField[XmpByte] = XmpField(XmpByte)  # byte, number of ports.
        port_speed: XmpField[XmpByte] = XmpField(XmpByte)  # byte, port speed, in Gbps.

    def get(self) -> "Token[GetDataAttr]":
        """Get the current number of ports and their speed of a CFP test module.

        :return:
            - number of ports
            - port speed, in Gbps
        :rtype: M_CFPCONFIG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, port_count: int, port_speed: int) -> "Token":
        """Set the current number of ports and their speed of a CFP test module.

        :param port_count: number of ports
        :type port_count: int
        :param port_speed: port speed, in Gbps
        :type port_speed: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port_count=port_count, port_speed=port_speed))


@register_command
@dataclass
class M_COMMENT:
    """
    Gets the user-defined description string of a module.
    """

    code: typing.ClassVar[int] = 86
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the user-specified comment/description for the module.

    @dataclass(frozen=True)
    class GetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, the user-specified comment/description for the module.

    def get(self) -> "Token[GetDataAttr]":
        """Get the user-defined description string of a module.

        :return: the user-specified comment/description for the module
        :rtype: M_COMMENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, comment: str) -> "Token":
        """Set the user-defined description string of a module.

        :param comment: the user-specified comment/description for the module
        :type comment: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, comment=comment))


@register_command
@dataclass
class M_TIMEADJUSTMENT:
    """
    Control time adjustment for module wall clock.
    """

    code: typing.ClassVar[int] = 88
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        adjust: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, adjustment in nanoseconds. This value should be a multiple of 8 as it will be converted to a number of 125 MHz clocks.

    @dataclass(frozen=True)
    class GetDataAttr:
        adjust: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, adjustment in nanoseconds. This value should be a multiple of 8 as it will be converted to a number of 125 MHz clocks.

    def get(self) -> "Token[GetDataAttr]":
        """Get the time adjustment value for the module clock.

        :return: the time adjustment value for the module clock
        :rtype: M_TIMEADJUSTMENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, adjust: int) -> "Token":
        """Set the time adjustment value for the module clock. This value should be a multiple of 8 as it will be converted to a number of 125 MHz clocks.

        :param adjust: the time adjustment value for the module clock
        :type adjust: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, adjust=adjust))


@register_command
@dataclass
class M_CAPABILITIES:
    """
    Gets the module capabilities.
    """

    code: typing.ClassVar[int] = 89
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        can_advanced_timing: XmpField[XmpInt] = XmpField(XmpInt, choices=YesNo)  # coded integer, is advanced timing functions supported?
        can_local_time_adjust: XmpField[XmpInt] = XmpField(XmpInt, choices=YesNo)  # coded integer, is local time adjustment supported?
        can_media_config: XmpField[XmpInt] = XmpField(XmpInt, choices=YesNo)  # coded integer, is module media configuration supported?
        require_multi_image: XmpField[XmpInt] = XmpField(XmpInt, choices=YesNo)  # coded integer, does this module switch images during runtime?
        is_chimera: XmpField[XmpInt] = XmpField(XmpInt, choices=YesNo)  # coded integer, is this a Chimera module?
        max_clock_ppm: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum supported absolute +- clock ppm setting.

    def get(self) -> "Token[GetDataAttr]":
        """Get the test module capabilities.

        :return:
            - is advanced timing functions supported?
            - is local time adjustment supported?
            - is module media configuration supported?
            - does this module switch images during runtime?
            - is this a Chimera module?
            - maximum supported absolute +- clock ppm setting.
        :rtype: M_CAPABILITIES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_MEDIASUPPORT:
    """
    This command shows the available speeds on a module. The structure of the returned value is
    [<cage_type> <available_speed_count> [<ports_per_speed> <speed>] ].
    [<ports_per_speed> <speed>] are repeated until all speeds supported by the <cage_type> has been listed.
    [<cage_type> <available_speed_count>] are repeated for all cage types on the module
    including the related <ports_per_speed> <speed> information.
    """

    code: typing.ClassVar[int] = 90
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        media_info_list: XmpField[XmpIntList] = XmpField(XmpIntList) # coded integer, media information

    def get(self) -> "Token[GetDataAttr]":
        """Get the

        :return:
            a list of integers. The structure of the returned value is [<cage_type> <available_speed_count>[<ports_per_speed> <speed>] ]. [<ports_per_speed> <speed>] are repeated until all speeds supported by the <cage_type> has been listed. [<cage_type> <available_speed_count>] are repeated for all cage types on the module including the related <ports_per_speed> <speed> information.

        :rtype: M_MEDIASUPPORT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_FPGAREIMAGE:
    """
    Reload FPGA image.
    """

    code: typing.ClassVar[int] = 91
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        key_code: XmpField[XmpInt] = XmpField(XmpInt)  # integer, must be 42.

    def set(self) -> "Token":
        """Reload the FPGA image.

        :param key_code: must be 42.
        :type key_code: int.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                key_code=42,
            ),
        )


@register_command
@dataclass
class M_MULTIUSER:
    """
    Enable or disable multiple sessions to control the same module.
    """

    code: typing.ClassVar[int] = 92
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, enable or disable multiple sessions to control the same module.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, enable or disable multiple sessions to control the same module.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of multiple sessions controling the same module.

        :return: the status of multiple sessions controling the same module
        :rtype: M_MULTIUSER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, on_off: OnOff) -> "Token":
        """Enable or disable multiple sessions to control the same module.

        :param on_off: Enable or disable multiple sessions to control the same module
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable multiple sessions to control the same module.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable multiple sessions to control the same module.
    """


@register_command
@dataclass
class M_CFPCONFIGEXT:
    """
    This property defines the current number of ports and the speed of each of them
    on a CFP test module. If the CFP type is NOTFLEXIBLE then it reflects the
    transceiver currently in the CFP cage. If the CFP type is FLEXIBLE(or
    NOTPRESENT) then the configuration can be changed explicitly. The following
    combinations are possible: 2x10G, 4x10G, 8x10G, 2x25G, 4x25G, 8x25G, 1x40G,
    2x40G, 2x50G, 4x50G, 8x50G, 1x100G, 2x100G, 4x100G, 2x200G, and 1x400G.
    (replaces M_CFPCONFIG)
    """

    code: typing.ClassVar[int] = 93
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        portspeed_chunck_list: XmpField[subtypes.PortSpeedChuckList] = XmpField(subtypes.PortSpeedChuckList)

    @dataclass(frozen=True)
    class GetDataAttr:
        portspeed_chunck_list: XmpField[subtypes.PortSpeedChuckList] = XmpField(subtypes.PortSpeedChuckList)


    def get(self) -> "Token[GetDataAttr]": #TODO
        """Get a list of port count and corresponding speeds supported by the current module config.

        :return: a list of port count and corresponding speeds supported by the current module config
        :rtype: M_CFPCONFIGEXT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, port_count: typing.List[int]) -> "Token":
        return Token(self._connection, build_set_request(self, module=self._module, port_count=port_count))


@register_command
@dataclass
class M_CLOCKPPB:
    """
    Makes small adjustments to the local clock of the test module, which drives the
    TX rate of the test ports.
    """

    code: typing.ClassVar[int] = 94
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        ppb: XmpField[XmpInt] = XmpField(XmpInt)  # integer, adjustment from nominal value, in parts-per-billion, positive or negative.

    @dataclass(frozen=True)
    class GetDataAttr:
        ppb: XmpField[XmpInt] = XmpField(XmpInt)  # integer, adjustment from nominal value, in parts-per-billion, positive or negative.

    def get(self) -> "Token[GetDataAttr]":
        """Get the module clock adjustment in ppb.

        :return: the module clock adjustment in ppb
        :rtype: M_CLOCKPPB.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, ppb: int) -> "Token":
        """Set the module clock adjustment in ppb.

        :param ppb: adjustment from nominal value, in parts-per-billion, positive or negative
        :type ppb: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, ppb=ppb))


@register_command
@dataclass
class M_SMAINPUT:
    """
    For test modules with SMA (SubMiniature version A) connectors, selects the function of the SMA input.
    """

    code: typing.ClassVar[int] = 95
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        sma_in: XmpField[XmpByte] = XmpField(XmpByte, choices=SMAInputFunction)  # coded byte, specifying the function of the SMA input.

    @dataclass(frozen=True)
    class GetDataAttr:
        sma_in: XmpField[XmpByte] = XmpField(XmpByte, choices=SMAInputFunction)  # coded byte, specifying the function of the SMA input.

    def get(self) -> "Token[GetDataAttr]":
        """Get the function of the SMA (SubMiniature version A) input of the module

        :return: the function of the SMA (SubMiniature version A) input of the module
        :rtype: M_SMAINPUT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, sma_in: SMAInputFunction) -> "Token":
        """Set the function of the SMA (SubMiniature version A) input of the module

        :param sma_in: the function of the SMA (SubMiniature version A) input of the module
        :type sma_in: SMAInputFunction
        """
        return Token(self._connection, build_set_request(self, module=self._module, sma_in=sma_in))

    set_notused = functools.partialmethod(set, SMAInputFunction.NOTUSED)
    """Set SMA input to Not Used
    """
    set_tx2mhz = functools.partialmethod(set, SMAInputFunction.TX2MHZ)
    """Set SMA input to TX Clock Ref. 2.048 MHz
    """
    set_tx10mhz = functools.partialmethod(set, SMAInputFunction.TX10MHZ)
    """Set SMA input to TX Clock Ref. 10.0 MHz
    """


@register_command
@dataclass
class M_SMAOUTPUT:
    """
    For test modules with SMA (SubMiniature version A) connectors, selects the function of the SMA output.
    """

    code: typing.ClassVar[int] = 96
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        sma_out: XmpField[XmpByte] = XmpField(XmpByte, choices=SMAOutputFunction)  # coded byte, specifying the function of the SMA output.

    @dataclass(frozen=True)
    class GetDataAttr:
        sma_out: XmpField[XmpByte] = XmpField(XmpByte, choices=SMAOutputFunction)  # coded byte, specifying the function of the SMA output.

    def get(self) -> "Token[GetDataAttr]":
        """Get the function of the SMA (SubMiniature version A) output of the module

        :return: the function of the SMA (SubMiniature version A) output of the module
        :rtype: M_SMAOUTPUT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, sma_out: SMAOutputFunction) -> "Token":
        """Set the function of the SMA (SubMiniature version A) output of the module

        :param sma_in: the function of the SMA (SubMiniature version A) output of the module
        :type sma_in: SMAOutputFunction
        """
        return Token(self._connection, build_set_request(self, module=self._module, sma_out=sma_out))

    set_disabled = functools.partialmethod(set, SMAOutputFunction.DISABLED)
    """Set SMA output function to Disabled.
    """
    set_passthrough = functools.partialmethod(set, SMAOutputFunction.PASSTHROUGH)
    """Set SMA output function to Pass-Through.
    """
    set_p0sof = functools.partialmethod(set, SMAOutputFunction.P0SOF)
    """Set SMA output function to Port 0 Start-of-Frame Pulse.
    """
    set_p1sof = functools.partialmethod(set, SMAOutputFunction.P1SOF)
    """Set SMA output function to Port 1 Start-of-Frame Pulse.
    """
    set_ref2mhz = functools.partialmethod(set, SMAOutputFunction.REF2MHZ)
    """Set SMA output function to TX Clock (nom. 2.048 MHz).
    """
    set_ref10mhz = functools.partialmethod(set, SMAOutputFunction.REF10MHZ)
    """Set SMA output function to TX Clock (nom. 10.0 MHz).
    """
    set_ref125mhz = functools.partialmethod(set, SMAOutputFunction.REF125MHZ)
    """Set SMA output function to TX Clock (nom. 125 MHz).
    """
    set_ref156mhz = functools.partialmethod(set, SMAOutputFunction.REF156MHZ)
    """Set SMA output function to TX Clock (nom. 156.25 MHz).
    """
    set_p0rxclk = functools.partialmethod(set, SMAOutputFunction.P0RXCLK)
    """Set SMA output function to Port 0 RX Clock (nom. 10.0 MHz).
    """
    set_p1rxclk = functools.partialmethod(set, SMAOutputFunction.P1RXCLK)
    """Set SMA output function to Port 1 RX Clock (nom. 10.0 MHz).
    """
    set_p0rxclk2mhz = functools.partialmethod(set, SMAOutputFunction.P0RXCLK2MHZ)
    """Set SMA output function to Port 0 RX Clock (nom. 2.048 MHz).
    """
    set_p1rxclk2mhz = functools.partialmethod(set, SMAOutputFunction.P1RXCLK2MHZ)
    """Set SMA output function to Port 1 RX Clock (nom. 2.048 MHz).
    """
    set_ts_pps = functools.partialmethod(set, SMAOutputFunction.TS_PPS)
    """Set SMA output function to Timing Source (Pulse-Per-Second).
    """


@register_command
@dataclass
class M_SMASTATUS:
    """
    For test modules with SMA connectors, this returns the status of the SMA input.
    """

    code: typing.ClassVar[int] = 97
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=SMAStatus)  # coded byte, specifying the status of the SMA input.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of the SMA input

        :return: the status of the SMA input
        :rtype: M_SMASTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_NAME:
    """
    Gets the name of a module.
    """

    code: typing.ClassVar[int] = 99
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        name: XmpField[XmpStr] = XmpField(XmpStr)  # string, the name for the module.

    def get(self) -> "Token[GetDataAttr]":
        """Get the name of the module.

        :return: the name of the module
        :rtype: M_NAME.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_REVISION:
    """
    Gets the model P/N name of a Xena test module.
    """

    code: typing.ClassVar[int] = 100
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        revision: XmpField[XmpStr] = XmpField(XmpStr)  # string, the model P/N name of a Xena test module.

    def get(self) -> "Token[GetDataAttr]":
        """Get the model P/N name of a Xena test module.

        :return: the model P/N name of a Xena test module.
        :rtype: M_REVISION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_MEDIA:
    """
    For the test modules that support media configuration (check M_CAPABILITIES), this command sets the desired media
    type (front port).
    """

    code: typing.ClassVar[int] = 342
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        media_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MediaType)  # coded byte, specifying the active front port: CFP4, QSFP28, CXP, SFP28.

    @dataclass(frozen=True)
    class GetDataAttr:
        media_type: XmpField[XmpByte] = XmpField(XmpByte, choices=MediaType)  # coded byte, specifying the active front port: CFP4, QSFP28, CXP, SFP28.

    def get(self) -> "Token[GetDataAttr]":
        """Get the media type of the test module.

        :return: the media type of the test module
        :rtype: M_MEDIA.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, media_type: MediaType) -> "Token":
        """Set the media type of the test module.

        :param media_type: the media type of the test module
        :type media_type: MediaType
        """
        return Token(self._connection, build_set_request(self, module=self._module, media_type=media_type))


@register_command
@dataclass
class M_CLOCKSYNCSTATUS:
    """
    Get module's clock sync status.
    """

    code: typing.ClassVar[int] = 370
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        m_clock_diff: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, module clock diff
        m_correction: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, module correction
        m_tune_is_increase: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, whether module tune is increased
        m_tune_value: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, module tune value
        m_is_steady_state: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, whether module is in steady state

    def get(self) -> "Token[GetDataAttr]":
        """Get the test module's clock sync status.

        :return: the test module's clock sync status
        :rtype: M_CLOCKSYNCSTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_LICENSE_DEMO_INFO:
    """
    Returns info about the demo status of the module. Only applicable to L47 test module.
    """

    code: typing.ClassVar[int] = 400
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        demo: XmpField[XmpByte] = XmpField(XmpByte, choices=HasDemo)  # coded byte, specifies if this is a demo module or not.
        valid: XmpField[XmpByte] = XmpField(XmpByte, choices=IsValid)  # coded byte, if this is a demo module, specifies if the demo license is valid.
        permanent: XmpField[XmpByte] = XmpField(
            XmpByte, choices=IsPermanent
        )  # coded byte, if this is a demo module and the demo license is valid, specifies if the demo license is permanent.
        expiration: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, if this is a demo module and the demo license is valid and not permanent, specifies the expiration date of the demo license - in seconds since Jan 1, 1970.

    def get(self) -> "Token[GetDataAttr]":
        """Get info of the demo status of the test module. Only applicable to L47 test module.

        :return: info of the demo status of the test module.
        :rtype: M_LICENSE_DEMO_INFO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_LICENSE_MAINTENANCE_INFO:
    """
    Returns info about the maintenance license status for the module. Only applicable to L47 test module.
    """

    code: typing.ClassVar[int] = 401
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        valid: XmpField[XmpByte] = XmpField(XmpByte, choices=IsValid)  # coded byte, specifies if the maintenance license is valid.
        permanent: XmpField[XmpByte] = XmpField(
            XmpByte, choices=IsPermanent
        )  # coded byte, if the maintenance license is valid, specifies if the maintenance license is permanent.
        expiration: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, if the maintenance license is valid and not permanent, specifies the expiration date of the maintenance license - in seconds since Jan 1, 1970.

    def get(self) -> "Token[GetDataAttr]":
        """Get the info about the maintenance license status for the module. Only applicable to L47 test module.

        :return: the info about the maintenance license status for the test module
        :rtype: M_LICENSE_MAINTENANCE_INFO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_LICENSE_CWB_DETECTED:
    """
    Returns if clock-windback is detected. If clock-windback has been detected the
    chassis is locked and no reservations of ports can be performed. To recover from
    clock-windback, set the system time correct (via the M4_SYSTEM_TIME command) and
    perform a license update (via the M_LICENSE_UPDATE command). Only applicable to L47 test module.
    """

    code: typing.ClassVar[int] = 402
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        detected: XmpField[XmpByte] = XmpField(XmpByte, choices=YesNo)  # coded byte, specifies if clock-windback is detected.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether clock-windback is detected.

        :return: whether clock-windback is detected
        :rtype: M_LICENSE_CWB_DETECTED.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_LICENSE_UPDATE:
    """
    This command instructs the chassis to update its local license information from
    FlexNet Operations. The chassis can be configured in on-line and off-line mode
    (by the M_LICENSE_ONLINE command). In on-line mode, the chassis sends a
    capability request to FlexNet Operations and receives a capability response. In
    offline mode a capability response (bin file) must be downloaded from FlexNet
    Operations and uploaded to the chassis. The capability response (bin file) is
    parsed and the license info is stored locally in trusted storage. A capability
    response (bin file) has a lifetime of one day (24 hours). The result of the
    license update operation can be retrieved by M_LICENSE_UPDATE_STATUS.
    """

    code: typing.ClassVar[int] = 403
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Start license update
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
            ),
        )


@register_command
@dataclass
class M_LICENSE_UPDATE_STATUS:
    """
    Returns the status of the latest license update operations.
    """

    code: typing.ClassVar[int] = 404
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        update_state: XmpField[XmpByte] = XmpField(XmpByte, choices=UpdateState)  # coded byte, specifies the state of the license update procedure
        last_update: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, time for the last update request - in seconds since Jan 1, 1979
        last_success: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, time for the last successful update - in seconds since Jan 1, 1979
        last_fail: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, time for the last failed update - in seconds since Jan 1, 1979
        Info: XmpField[XmpStr] = XmpField(XmpStr)  # string, info about the last license update operation - reason for failed update.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of the latest license update operation.

        :return: the status of the latest license update operation
        :rtype: M_LICENSE_UPDATE_STATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_LICENSE_LIST_BSON:
    """
    Returns a list of locally stored licenses - formatted as a BSON document.
    """

    code: typing.ClassVar[int] = 405
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        bson: XmpField[XmpHexList] = XmpField(XmpHexList)  # list of hex bytes, bson document containing the list of locally stored licenses

    def get(self) -> "Token[GetDataAttr]":
        """Get the a list of locally stored licenses - formatted as a BSON document.

        :return: a list of locally stored licenses - formatted as a BSON document.
        :rtype: M_LICENSE_LIST_BSON.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_LICENSE_ONLINE:
    """
    Configures the chassis in online or offline mode. The online mode configuration
    defines two different license update procedures as described for the
    M_LICENSE_UPDATE command. In online mode the license update procedure requires
    access to the Internet. In offline mode the license update procedure can be
    performed without access to the Internet.
    """

    code: typing.ClassVar[int] = 406
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=IsOnline)  # coded byte, chassis online/offline mode.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=IsOnline)  # coded byte, chassis online/offline mode.

    def get(self) -> "Token[GetDataAttr]":
        """Get the current online/offline mode of the L47 tester.

        :return: the current online/offline mode of the L47 tester
        :rtype: M_LICENSE_ONLINE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, mode: IsOnline) -> "Token":
        """Set the current online/offline mode of the L47 tester.

        :param mode: the current online/offline mode of the L47 tester
        :type mode: IsOnline
        """
        return Token(self._connection, build_set_request(self, module=self._module, mode=mode))

    set_offline = functools.partialmethod(set, IsOnline.OFFLINE)
    """Set the L47 tester to offline mode.
    """
    set_online = functools.partialmethod(set, IsOnline.ONLINE)
    """Set the L47 tester to online mode.
    """


@register_command
@dataclass
class M_TXCLOCKSOURCE_NEW:
    """
    For test modules with advanced timing features, select what clock drives the port TX
    rates.
    """

    code: typing.ClassVar[int] = 410
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        tx_clock: XmpField[XmpByte] = XmpField(XmpByte, choices=TXClockSource)  # coded byte, specifying what drives the port TX rates.

    @dataclass(frozen=True)
    class GetDataAttr:
        tx_clock: XmpField[XmpByte] = XmpField(XmpByte, choices=TXClockSource)  # coded byte, specifying what drives the port TX rates.

    def get(self) -> "Token[GetDataAttr]":
        """Get the test module's TX clock source settings.

        :return: the test module's TX clock source settings.
        :rtype: M_TXCLOCKSOURCE_NEW.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, tx_clock: TXClockSource) -> "Token":
        """Set the test module's TX clock source settings.

        :param tx_clock: the test module's TX clock source settings
        :type tx_clock: TXClockSource
        """
        return Token(self._connection, build_set_request(self, module=self._module, tx_clock=tx_clock))

    set_modulelocalclock = functools.partialmethod(set, TXClockSource.MODULELOCALCLOCK)
    """Set the test module's TX clock source to Module Local Clock
    """
    set_smainput = functools.partialmethod(set, TXClockSource.SMAINPUT)
    """Set the test module's TX clock source to SMA Input
    """
    set_p0rxclk = functools.partialmethod(set, TXClockSource.P0RXCLK)
    """Set the test module's TX clock source to Port 0 RX Clock
    """
    set_p1rxclk = functools.partialmethod(set, TXClockSource.P1RXCLK)
    """Set the test module's TX clock source to Port 1 RX Clock
    """
    set_p2rxclk = functools.partialmethod(set, TXClockSource.P2RXCLK)
    """Set the test module's TX clock source to Port 2 RX Clock
    """
    set_p3rxclk = functools.partialmethod(set, TXClockSource.P3RXCLK)
    """Set the test module's TX clock source to Port 3 RX Clock
    """
    set_p4rxclk = functools.partialmethod(set, TXClockSource.P4RXCLK)
    """Set the test module's TX clock source to Port 4 RX Clock
    """
    set_p5rxclk = functools.partialmethod(set, TXClockSource.P5RXCLK)
    """Set the test module's TX clock source to Port 5 RX Clock
    """
    set_p6rxclk = functools.partialmethod(set, TXClockSource.P6RXCLK)
    """Set the test module's TX clock source to Port 6 RX Clock
    """
    set_p7rxclk = functools.partialmethod(set, TXClockSource.P7RXCLK)
    """Set the test module's TX clock source to Port 7 RX Clock
    """


@register_command
@dataclass
class M_TXCLOCKSTATUS_NEW:
    """
    For test modules with advanced timing features, check whether a valid clock is
    present.
    """

    code: typing.ClassVar[int] = 411
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=TXClockStatus)  # coded byte, specifying the status of the TX clock.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of whether a valid clock is present for the test module.

        :return: the status of whether a valid clock is present for the test module.
        :rtype: M_TXCLOCKSTATUS_NEW.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))


@register_command
@dataclass
class M_TXCLOCKFILTER_NEW:
    """
    For test modules with advanced timing features, the loop bandwidth on the TX
    clock filter.
    """

    code: typing.ClassVar[int] = 412
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        filter_bandwidth: XmpField[XmpByte] = XmpField(XmpByte, choices=LoopBandwidth)  # coded byte, the loop bandwidth on the TX clock filter.

    @dataclass(frozen=True)
    class GetDataAttr:
        filter_bandwidth: XmpField[XmpByte] = XmpField(XmpByte, choices=LoopBandwidth)  # coded byte, the loop bandwidth on the TX clock filter.

    def get(self) -> "Token[GetDataAttr]":
        """Get the setting of the loop bandwidth on the TX clock filter.

        :return: the setting of the loop bandwidth on the TX clock filter.
        :rtype: M_TXCLOCKFILTER_NEW.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, filter_bandwidth: LoopBandwidth) -> "Token":
        """Set the setting of the loop bandwidth on the TX clock filter.

        :param filter_bandwidth: the setting of the loop bandwidth on the TX clock filter
        :type filter_bandwidth: LoopBandwidth
        """
        return Token(self._connection, build_set_request(self, module=self._module, filter_bandwidth=filter_bandwidth))

    set_bw103hz = functools.partialmethod(set, LoopBandwidth.BW103HZ)
    """Set the loop bandwidth on the TX clock filter to BW = 103 Hz.
    """
    set_bw207hz = functools.partialmethod(set, LoopBandwidth.BW207HZ)
    """Set the loop bandwidth on the TX clock filter to BW = 207 Hz.
    """
    set_bw416hz = functools.partialmethod(set, LoopBandwidth.BW416HZ)
    """Set the loop bandwidth on the TX clock filter to BW = 416 Hz.
    """
    set_bw1683hz = functools.partialmethod(set, LoopBandwidth.BW1683HZ)
    """Set the loop bandwidth on the TX clock filter to BW = 1683 Hz.
    """
    set_bw7019hz = functools.partialmethod(set, LoopBandwidth.BW7019HZ)
    """Set the loop bandwidth on the TX clock filter to BW = 7019 Hz.
    """


@register_command
@dataclass
class M_EMULBYPASS:
    """
    Set emulator bypass mode. Emulator bypass mode will bypass the entire emulator
    for minimum latency.
    """

    code: typing.ClassVar[int] = 454
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether the emulator bypass is enabled.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether the emulator bypass is enabled.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of bypass mode of the impairment emulator.

        :return: the status of bypass mode of the impairment emulator.
        :rtype: M_EMULBYPASS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module))

    def set(self, on_off: OnOff) -> "Token":
        """Set the bypass mode of the impairment emulator.

        :param on_off: the bypass mode of the impairment emulator.
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the bypass mode of the impairment emulator.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the bypass mode of the impairment emulator.
    """


