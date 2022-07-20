#: L23 High-speed Port Commands

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
class PP_ALARMS_ERRORS:
    """
    Obtain the error count of each alarm, PCS Error, FEC Error, Header Error, Align
    Error, BIP Error, and High BER Error.
    """

    code: typing.ClassVar[int] = 272
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        total_alarms: XmpField[XmpInt] = XmpField(XmpInt)  # integer, total number of triggered alarms
        valid_mask: XmpField[XmpHex8] = XmpField(XmpHex8)  # 8 hex bytes, mask of valid alarms
        los_error_cournt: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of no-sync alarms
        total_pcs_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of errors of PCS error alarm
        total_fec_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of errors of FEC error alarm
        total_header_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of errors of header error alarm
        total_align_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of errors of alignment error alarm
        total_bip_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of errors of BIP error alarm
        total_highber_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of errors of high BER error alarm

    def get(self) -> "Token[GetDataAttr]":
        """Get the error count of each alarm, PCS Error, FEC Error, Header Error, Align Error, BIP Error, and High BER Error.

        :return: the error count of each alarm, PCS Error, FEC Error, Header Error, Align Error, BIP Error, and High BER Error.
        :rtype: PP_ALARMS_ERRORS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_ALARMS_ERRORS_CLEAR:
    """
    Clear all PCS/PMA alarms.
    """

    code: typing.ClassVar[int] = 273
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self, dummy: int) -> "Token":
        """Clear all PCS/PMA alarms.
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_TXLANECONFIG:
    """
    The virtual lane index and artificial skew for data transmitted on a specified
    physical lane.
    """

    code: typing.ClassVar[int] = 280
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _lane_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        virt_lane_index: XmpField[XmpInt] = XmpField(XmpInt)  # integer, virtual lane index.
        skew: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the inserted skew on the lane, in bit units.

    @dataclass(frozen=True)
    class GetDataAttr:
        virt_lane_index: XmpField[XmpInt] = XmpField(XmpInt)  # integer, virtual lane index.
        skew: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the inserted skew on the lane, in bit units.

    def get(self) -> "Token[GetDataAttr]":
        """Get the virtual lane index and artificial skew for data transmitted on a specified physical lane.

        :return: virtual lane index, and the inserted skew on the lane, in bit units.
        :rtype: PP_TXLANECONFIG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._lane_xindex]))

    def set(self, virt_lane_index: int, skew: int) -> "Token":
        """Set the virtual lane index and artificial skew for data transmitted on a specified physical lane.

        :param virt_lane_index: virtual lane index
        :type virt_lane_index: int
        :param skew: the inserted skew on the lane, in bit units
        :type skew: int
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._lane_xindex], virt_lane_index=virt_lane_index, skew=skew)
        )


@register_command
@dataclass
class PP_TXLANEINJECT:
    """
    Inject a particular kind of CAUI error into a specific physical lane.
    """

    code: typing.ClassVar[int] = 281
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _lane_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        inject_error_type: XmpField[XmpByte] = XmpField(XmpByte, choices=InjectErrorType)  # coded byte, specifying what kind of error to inject.

    def set(self, inject_error_type: InjectErrorType) -> "Token":
        """Inject a particular kind of CAUI error into a specific physical lane.

        :param inject_error_type: specifying what kind of error to inject
        :type inject_error_type: InjectErrorType
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._lane_xindex], inject_error_type=inject_error_type)
        )

    set_headererror = functools.partialmethod(set, InjectErrorType.HEADERERROR)
    """Inject Header error into a specific physical lane.
    """
    set_alignerror = functools.partialmethod(set, InjectErrorType.ALIGNERROR)
    """Inject Alignment error into a specific physical lane.
    """
    set_bip8error = functools.partialmethod(set, InjectErrorType.BIP8ERROR)
    """Inject BIP8 error into a specific physical lane.
    """


@register_command
@dataclass
class PP_TXPRBSCONFIG:
    """
    The PRBS configuration for a particular SerDes. When PRBS is enabled for any SerDes
    then the overall link is compromised and drops out of sync.
    """

    code: typing.ClassVar[int] = 282
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        prbs_seed: XmpField[XmpInt] = XmpField(XmpInt)  # integer, PRBS seed value.
        prbs_on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSOnOff)  # code byte, whether this SerDes is transmitting PRBS data.
        error_on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=ErrorOnOff)  # code byte, whether bit-level errors are injected into this SerDes.

    @dataclass(frozen=True)
    class GetDataAttr:
        prbs_seed: XmpField[XmpInt] = XmpField(XmpInt)  # integer, PRBS seed value.
        prbs_on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSOnOff)  # code byte, whether this SerDes is transmitting PRBS data.
        error_on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=ErrorOnOff)  # code byte, whether bit-level errors are injected into this SerDes.

    def get(self) -> "Token[GetDataAttr]":
        """Get the PRBS configuration for a particular SerDes. When PRBS is enabled for any SerDes
        then the overall link is compromised and drops out of sync.

        :return: the PRBS configuration for a particular SerDes
        :rtype: PP_TXPRBSCONFIG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, prbs_seed: int, prbs_on_off: PRBSOnOff, error_on_off: ErrorOnOff) -> "Token":
        """Set the PRBS configuration for a particular SerDes.

        :param prbs_seed: not used, set to 0.
        :type prbs_seed: int
        :param prbs_on_off: whether this SerDes is transmitting PRBS data.
        :type prbs_on_off: PRBSOnOff
        :param error_on_off: whether bit-level errors are injected into this SerDes
        :type error_on_off: ErrorOnOff
        """
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, indices=[self._serdes_xindex], prbs_seed=prbs_seed, prbs_on_off=prbs_on_off, error_on_off=error_on_off
            ),
        )


@register_command
@dataclass
class PP_TXERRORRATE:
    """
    The rate of continuous bit-level error injection. Errors are injected evenly
    across the SerDes where injection is enabled.
    """

    code: typing.ClassVar[int] = 283
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        rate: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of bits between each error. 0, no error injection.

    @dataclass(frozen=True)
    class GetDataAttr:
        rate: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of bits between each error. 0, no error injection.

    def get(self) -> "Token[GetDataAttr]":
        """Get the rate of continuous bit-level error injection. Errors are injected evenly
        across the SerDes where injection is enabled.

        :return: the number of bits between each error. 0, no error injection
        :rtype: PP_TXERRORRATE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, rate: int) -> "Token":
        """Set the rate of continuous bit-level error injection. Errors are injected evenly
        across the SerDes where injection is enabled.

        :param rate: the number of bits between each error. 0, no error injection
        :type rate: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, rate=rate))


@register_command
@dataclass
class PP_TXINJECTONE:
    """
    Inject a single bit-level error into the SerDes where injection has been enabled.
    """

    code: typing.ClassVar[int] = 284
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Inject a single bit-level error into one of the SerDes where injection is
        enabled.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
            ),
        )


@register_command
@dataclass
class PP_RXTOTALSTATS:
    """
    Provides FEC Total counters.
    """

    code: typing.ClassVar[int] = 285
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        total_corrected_fec_symbol_count: XmpField[XmpLong] = XmpField(XmpLong)  # integer, total corrected FEC symbols count.
        total_uncorrectable_fec_block_count: XmpField[XmpLong] = XmpField(XmpLong)  # integer, total uncorrectable FEC blocks count.
        total_pre_ber: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # integer, total pre-FEC BER estimate sent as "total_pre_ber = received_bits / total_corfecerrs". To get the real total pre-BER, calculate the inverse: 1/total_pre_ber. If zero physical bit errors have been detected, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.
        total_post_ber: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # integer, total post-FEC BER estimate sent as "total_post_ber = received_bits / total_estimated_uncorrectable_errors". To get the real total post-BER, calculate the inverse: 1/total_post_ber. If zero physical bit errors have been detected, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.

    def get(self) -> "Token[GetDataAttr]":
        """Get FEC Total counters of the port:
            1. total corrected FEC symbols count.
            2. total uncorrectable FEC blocks count.
            3. total pre-FEC BER estimate sent as "total_pre_ber = received_bits / total_corfecerrs".
                To get the real total pre-BER, calculate the inverse: 1/total_pre_ber.
                If zero physical bit errors have been detected, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.
            4. total post-FEC BER estimate sent as "total_post_ber = received_bits / total_estimated_uncorrectable_errors".
                To get the real total post-BER, calculate the inverse: 1/total_post_ber.
                If zero physical bit errors have been detected, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.

        :return: total corrected FEC symbols count, total uncorrectable FEC blocks count, total pre-FEC BER estimate sent, and Total post-FEC BER estimate sent.

        :rtype: PP_RXTOTALSTATS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_RXFECSTATS:
    """
    Provides statistics on how many FEC blocks have been seen with a given number of symbol errors.
    """

    code: typing.ClassVar[int] = 286
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        stats_type: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, currently always 0.
        value_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of values in correction_stats.
        correction_stats: XmpField[XmpLongListStopToKeep8] = XmpField(
            XmpLongListStopToKeep8
        )  # list of long integers, array of length value_count-1. The correction_stats array shows how many FEC blocks have been seen with [0, 1, 2, 3....15, >15] symbol errors.
        rx_uncorrectable_code_word_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of received uncorrectable code words.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics on how many FEC blocks have been seen with a given number of symbol errors.

        :return: stats type (currently always 0), number of values in correction_stats, array of length value_count-1.
            The correction_stats array shows how many FEC blocks have been seen with [0, 1, 2, 3....15, >15] symbol errors, and the number of received uncorrectable code words

        :rtype: PP_RXFECSTATS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_LINKFLAP_PARAMS:
    """
    Set port 'link flap' parameters. Notice: Period must be larger than duration.
    """

    code: typing.ClassVar[int] = 287
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 0 ms - 1000 ms; increments of 1 ms; 0 = permanently link down.
        period: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms.
        repetition: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 1 - 64K; 0 = continuous.

    @dataclass(frozen=True)
    class GetDataAttr:
        duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 0 ms - 1000 ms; increments of 1 ms; 0 = permanently link down.
        period: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms.
        repetition: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 1 - 64K; 0 = continuous.

    def get(self) -> "Token[GetDataAttr]":
        """Get port 'link flap' settings.

        :return: duration, period, and repetition of link flapping.
        :rtype: PP_LINKFLAP_PARAMS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, duration: int, period: int, repetition: int) -> "Token":
        """Set port 'link flap' settings. Notice: Period must be larger than duration.

        :param duration: 0 ms - 1000 ms; increments of 1 ms; 0 = permanently link down.
        :type duration: int
        :param period: 10 ms - 50000 ms; number of ms - must be multiple of 10 ms.
        :type period: int
        :param repetition: 1 - 64K; 0 = continuous.
        :type repetition: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, duration=duration, period=period, repetition=repetition))


@register_command
@dataclass
class PP_LINKFLAP_ENABLE:
    """
    Enable / disable port 'link flap'.
    """

    code: typing.ClassVar[int] = 288
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether link flap is enabled.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether link flap is enabled.

    def get(self) -> "Token[GetDataAttr]":
        """Get the port 'link flap' status of the port.

        :return: whether link flap is enabled
        :rtype: PP_LINKFLAP_ENABLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> "Token":
        """Set the port 'link flap' status of the port.

        :param on_off: whether link flap is enabled
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the port 'link flap'.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the port 'link flap'.
    """


@register_command
@dataclass
class PP_PMAERRPUL_PARAMS:
    """
    The 'PMA pulse error inject'.

    .. note::

        Period must be > duration. BER will be: coeff * 10exp
    """

    code: typing.ClassVar[int] = 289
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 0 ms - 5000m s; increments of 1 ms; 0 = constant BER
        period: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms
        repetition: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 1 - 64K; 0 = continuous
        coeff: XmpField[XmpInt] = XmpField(XmpInt)  # long integer, (0.01 < coeff < 9.99) * 100
        exp: XmpField[XmpInt] = XmpField(XmpInt, climb=(-16, -4))  # integer, -3 < exp < -17

    @dataclass(frozen=True)
    class GetDataAttr:
        duration: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 0 ms - 5000m s; increments of 1 ms; 0 = constant BER
        period: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms
        repetition: XmpField[XmpInt] = XmpField(XmpInt)  # integer, 1 - 64K; 0 = continuous
        coeff: XmpField[XmpInt] = XmpField(XmpInt)  # long integer, (0.01 < coeff < 9.99) * 100
        exp: XmpField[XmpInt] = XmpField(XmpInt, climb=(-16, -4))  # integer, -3 < exp < -17

    def get(self) -> "Token[GetDataAttr]":
        """Get PMA pulse error injection settings.

        :return: PMA pulse error injection settings
        :rtype: PP_PMAERRPUL_PARAMS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, duration: int, period: int, repetition: int, coeff: int, exp: int) -> "Token":
        """Set PMA pulse error injection settings.

        :param duration: 0 ms - 5000m s; increments of 1 ms; 0 = constant BER
        :type duration: int
        :param period: 10 ms - 50000 ms; number of ms - must be multiple of 10 ms
        :type period: int
        :param repetition: 1 - 64K; 0 = continuous
        :type repetition: int
        :param coeff: (0.01 < coeff < 9.99) * 100
        :type coeff: int
        :param exp: -3 < exp < -17
        :type exp: Infinite
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, duration=duration, period=period, repetition=repetition, coeff=coeff, exp=exp))


@register_command
@dataclass
class PP_RXLANELOCK:
    """
    Whether the receiver has achieved header lock and alignment lock on the data
    received on a specified physical lane.
    """

    code: typing.ClassVar[int] = 290
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _lane_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        headerlock: XmpField[XmpByte] = XmpField(XmpByte, choices=HeaderLockStatus)  # coded byte, whether this lane has achieved header lock.
        alignlock: XmpField[XmpByte] = XmpField(XmpByte, choices=AlignLockStatus)  # coded byte, whether this lane has achieved alignment lock.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether the receiver has achieved header lock and alignment lock on the data
        received on a specified physical lane.

        :return: whether this lane has achieved header lock, and whether this lane has achieved alignment lock.
        :rtype: PP_RXLANELOCK.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._lane_xindex]))


@register_command
@dataclass
class PP_RXLANESTATUS:
    """
    The virtual lane index and actual skew for data received on a specified physical
    lane. This is only meaningful when the lane is in header lock and alignment
    lock.
    """

    code: typing.ClassVar[int] = 291
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _lane_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        virtual_lane: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the logical lane number.
        skew: XmpField[XmpInt] = XmpField(XmpInt)  # integer, the measured skew on the lane, in bit units.

    def get(self) -> "Token[GetDataAttr]":
        """Get the virtual lane index and actual skew for data received on a specified physical lane.

        :return: the virtual lane index and actual skew for data received on a specified physical lane
        :rtype: PP_RXLANESTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._lane_xindex]))


@register_command
@dataclass
class PP_RXLANEERRORS:
    """
    Statistics about errors detected at the physical coding sub-layer on the data
    received on a specified physical lane.
    """

    code: typing.ClassVar[int] = 292
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _lane_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        header_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of header errors.
        alignment_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of alignment errors.
        bip8_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of bip8 errors.
        corrected_fec_error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, corrected FEC bit errors.
        pre_ber: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, received_bits / corfecerrs. To get the pre_ber, calculate the inverse: 1/pre_ber. If zero bit errors have been received, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics about errors detected at the physical coding sub-layer on the data
        received on a specified physical lane.

        :return: the number of header errors, the number of alignment errors, the number of bip8 errors, and corrected FEC bit errors
        :rtype: PP_RXLANEERRORS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._lane_xindex]))


@register_command
@dataclass
class PP_RXPRBSSTATUS:
    """
    Statistics about PRBS pattern detection on the data received on a specified
    SerDes.
    """

    code: typing.ClassVar[int] = 293
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        byte_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of bytes received while in PRBS lock.
        error_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, the number of errors detected while in PRBS lock.
        lock: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSLockStatus)  # coded byte, whether this lane is in PRBS lock.

    def get(self) -> "Token[GetDataAttr]":
        """Get the statistics about PRBS pattern detection on the data received on a specified
        SerDes.

        :return: the number of bytes received while in PRBS lock, the number of errors detected while in PRBS lock, and whether this SerDes is in PRBS lock.
        :rtype: PP_RXPRBSSTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))


@register_command
@dataclass
class PP_RXCLEAR:
    """
    Clear all the PCS/PMA receiver statistics for a port.
    """

    code: typing.ClassVar[int] = 294
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clear all the PCS/PMA receiver statistics for a port.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
            ),
        )


@register_command
@dataclass
class PP_RXLASERPOWER:
    """
    Reading of the optical power level of the received signal. There is one value
    for each laser/wavelength, and the number of these depends on the kind of CFP
    transceiver used. The list is empty if the CFP transceiver does not support
    optical power read-out.
    """

    code: typing.ClassVar[int] = 295
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        nanowatts: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, received signal level, in nanowatts. 0, when no signal.

    def get(self) -> "Token[GetDataAttr]":
        """Get the readings of the optical power level of the received signal.

        :return: received signal level, in nanowatts. 0, when no signal.
        :rtype: PP_RXLASERPOWER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_TXLASERPOWER:
    """
    Reading of the optical power level of the transmission signal. There is one
    value for each laser/wavelength, and the number of these depends on the kind of
    CFP transceiver used. The list is empty if the CFP transceiver does not support
    optical power read-out.
    """

    code: typing.ClassVar[int] = 296
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        nanowatts: XmpField[XmpIntList] = XmpField(XmpIntList)  # list of integers, received signal level, in nanowatts. 0, when no signal.

    def get(self) -> "Token[GetDataAttr]":
        """Get the reading of the optical power level of the transmission signal.

        :return: received signal level, in nanowatts. 0, when no signal.
        :rtype: PP_TXLASERPOWER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_PMAERRPUL_ENABLE:
    """
    Enable / disable 'PMA pulse error inject'.
    """

    code: typing.ClassVar[int] = 300
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether PMA pulse error inject is enabled.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, whether PMA pulse error inject is enabled.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of 'PMA pulse error inject'.

        :return: whether PMA pulse error inject is enabled
        :rtype: PP_PMAERRPUL_ENABLE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> "Token":
        """Set the status of 'PMA pulse error inject'.

        :param on_off: whether PMA pulse error inject is enabled
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable 'PMA pulse error inject'.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable 'PMA pulse error inject'.
    """


@register_command
@dataclass
class PP_EYEMEASURE:
    """
    Start/stop a new BER eye-measure on a 25G serdes. Use "get" to see the status of
    the data gathering process.
    """

    code: typing.ClassVar[int] = 353
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=StartOrStop)  # coded byte, status of the serdes.
        dummy: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of bytes, reserved for future expansion.

    @dataclass(frozen=True)
    class GetDataAttr:
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=SerdesStatus)  # coded byte, status of the serdes.
        dummy: XmpField[XmpByteList] = XmpField(XmpByteList)  # list of bytes, reserved for future expansion.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of the BER eye-measure data gathering process.

        :return: status of the serdes
        :rtype: PP_EYEMEASURE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, status: StartOrStop, dummy: typing.List[int]) -> "Token":
        """Start/stop a new BER eye-measure on a 25G serdes.

        :param status: status of the serdes
        :type status: StartOrStop
        :param dummy: reserved for future expansion
        :type dummy: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], status=status, dummy=dummy))

    set_stop = functools.partialmethod(set, StartOrStop.STOP)
    """Start a new BER eye-measure on a 25G serdes.
    """
    set_start = functools.partialmethod(set, StartOrStop.START)
    """Stop a new BER eye-measure on a 25G serdes.
    """


@register_command
@dataclass
class PP_EYERESOLUTION:
    """
    Set or get the resolution used for the next BER eye-measurement.
    """

    code: typing.ClassVar[int] = 354
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        x_resolution: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of columns, must be between 9 and 65 and be in the form 2^n+1
        y_resolution: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of columns, must be between 7 and 255 and be in the form 2^n-1

    @dataclass(frozen=True)
    class GetDataAttr:
        x_resolution: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of columns, must be between 9 and 65 and be in the form 2^n+1
        y_resolution: XmpField[XmpInt] = XmpField(XmpInt)  # integer, number of columns, must be between 7 and 255 and be in the form 2^n-1

    def get(self) -> "Token[GetDataAttr]":
        """Get the resolution used for the next BER eye-measurement.

        :return: x resolution and y resolution
        :rtype: PP_EYERESOLUTION.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, x_resolution: int, y_resolution: int) -> "Token":
        """Set the resolution used for the next BER eye-measurement.

        :param x_resolution: number of columns, must be between 9 and 65 and be in the form 2^n+1
        :type x_resolution: int
        :param y_resolution: number of columns, must be between 7 and 255 and be in the form 2^n-1
        :type y_resolution: int
        """
        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], x_resolution=x_resolution, y_resolution=y_resolution),
        )


@register_command
@dataclass
class PP_EYEREAD:
    """
    Read a single column of a measured BER eye on a 25G serdes. Every readout also
    returns the resolution (x,y) and the number of valid columns (used to facilitate
    reading out the eye while it is being measured).  Note that the columns of the
    eye-data will be measured in the order: xres-1, xres-2, xres-3, ... 0.  The
    values show the number of bit errors measured out of a total of 1M bits at each
    of the individual sampling points (x=timeaxis, y = 0/1 threshold).
    """

    code: typing.ClassVar[int] = 355
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int
    colum_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        x_resolution: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying X resolution.
        y_resolution: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying Y resolution.
        valid_column_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, specifying the number of valid columns.
        values: XmpField[XmpIntList] = XmpField(
            XmpIntList
        )  # list of integers, showing the number of bit errors measured out of a total of 1M bits at each of the individual sampling points (x=timeaxis, y = 0/1 threshold).

    def get(self) -> "Token[GetDataAttr]":
        """Read a single column of a measured BER eye on a 25G serdes.

        :return: x resolution, y resolution, number of valid columns, and the number of bit errors measured out of a total of 1M bits at each of the individual sampling points (x=timeaxis, y = 0/1 threshold).
        :rtype: PP_EYEREAD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self.colum_xindex]))


@register_command
@dataclass
class PP_EYEINFO:
    """
    Read out BER eye-measurement information such as the vertical and horizontal
    bathtub curve information on a 25G serdes. This must be called after "PP_EYEMEASURE"
    has run to return valid results.  Use "get" to see the status of the data
    gathering process.

    """

    code: typing.ClassVar[int] = 356
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        width_mui: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit 0..1000 (mUI), group = Horizontal bathtub curve
        height_mv: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit 0..1000 (mV), group = Vertical bathtub curve
        h_slope_left: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (Q/UI) *100, signed integer, group = Horizontal bathtub curve
        h_slope_right: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (Q/UI) *100, signed integer, group = Horizontal bathtub curve
        y_intercept_left: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (Q) * 100, signed integer, group = Horizontal bathtub curve
        y_intercept_right: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (Q) * 100, signed integer, group = Horizontal bathtub curve
        r_squared_fit_left: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit Int * 100, group = Horizontal bathtub curve
        r_squared_fit_right: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit Int * 100, group = Horizontal bathtub curve
        est_rj_rms_left: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (mUI) * 1000, group = Horizontal bathtub curve
        est_rj_rms_right: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (mUI) * 1000, group = Horizontal bathtub curve
        est_dj_pp: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (mUI) * 1000, group = Horizontal bathtub curve
        v_slope_bottom: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (mV/Q) *100, signed integer, group = Vertical bathtub curve
        v_slope_top: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (mV/Q) *100, signed integer, group = Vertical bathtub curve
        x_intercept_bottom: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (Q) *100), signed integer, group = Vertical bathtub curve
        x_intercept_top: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (Q) *100, signed integer, group = Vertical bathtub curve
        r_squared_fit_bottom: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit Int * 100, group = Vertical bathtub curve
        r_squared_fit_top: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit Int * 100, group = Vertical bathtub curve
        est_rj_rms_bottom: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (mV) * 1000, group = Vertical bathtub curve
        est_rj_rms_top: XmpField[XmpInt] = XmpField(XmpInt)  # integer, value and unit (mV) * 1000, group = Vertical bathtub curve

    def get(self) -> "Token[GetDataAttr]":
        """Read out BER eye-measurement information such as the vertical and horizontal
        bathtub curve information on a 25G serdes. This must be called after "PP_EYEMEASURE"
        has run to return valid results.  Use "get" to see the status of the data
        gathering process.

        :return: BER eye-measurement information such as the vertical and horizontal bathtub curve information on a 25G serdes
        :rtype: PP_EYEINFO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))


@register_command
@dataclass
class PP_PHYTXEQ:
    """
    Control and monitor the equalizer settings of the on-board PHY in the
    transmission direction (towards the transceiver cage) on Thor and Loki modules.
    """

    code: typing.ClassVar[int] = 358
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pre1: XmpField[XmpIntList] = XmpField(XmpIntList)  # integer, preemphasis, (range: Module dependent), default = 0 (neutral).

    @dataclass(frozen=True)
    class GetDataAttr:
        pre1: XmpField[XmpIntList] = XmpField(XmpIntList)  # integer, preemphasis, (range: Module dependent), default = 0 (neutral).

    def get(self) -> "Token[GetDataAttr]":
        """Get the equalizer settings of the on-board PHY in the
        transmission direction (towards the transceiver cage) on Thor and Loki modules.

        :return: preemphasis, (range: Module dependent), default = 0 (neutral).
        :rtype: PP_PHYTXEQ.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, pre1: typing.List[int]) -> "Token":
        """Set the equalizer settings of the on-board PHY in the
        transmission direction (towards the transceiver cage) on Thor and Loki modules.

        :param pre1: preemphasis, (range: Module dependent), default = 0 (neutral)
        :type pre1: List[int]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], pre1=pre1))


@register_command
@dataclass
class PP_PHYRETUNE:
    """
    Trigger a new retuning of the receive equalizer on the PHY for one of the 25G
    serdes. Useful if e.g. a direct attached copper cable or loop transceiver does
    not go into sync after insertion. Note that the retuning will cause disruption
    of the traffic on all serdes.
    """

    code: typing.ClassVar[int] = 359
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        dummy: XmpField[XmpByte] = XmpField(XmpByte)  # byte, reserved for future improvements, always set to 1

    def set(self, dummy: int) -> "Token":
        """Trigger a new retuning of the receive equalizer on the PHY for one of the 25G
        serdes.

        :param dummy: reserved for future improvements, always set to 1
        :type dummy: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], dummy=1))


@register_command
@dataclass
class PP_PHYAUTOTUNE:
    """
    Enable or disable the automatic receiving of PHY retuning (see PP_PHYRETUNE), which
    is performed on the 25G interfaces as soon as a signal is detected by the
    transceiver. Useful if a bad signal causes the PHY to continuously retune or if
    for some other reason it is preferable to use manual retuning (PP_PHYRETUNE).
    """

    code: typing.ClassVar[int] = 360
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte)  # coded byte, enable/disable automatic receiving PHY retuning. Default is enabled.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte)  # coded byte, enable/disable automatic receiving PHY retuning. Default is enabled.

    def get(self) -> "Token[GetDataAttr]":
        """Get whether the auto PHY retuning is enabled.

        :return: enable/disable automatic receiving PHY retuning
        :rtype: PP_PHYAUTOTUNE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, on_off: OnOff) -> "Token":
        """Enable/disable automatic receiving PHY retuning. Default is enabled.

        :param on_off: Enable/disable automatic receiving PHY retuning. Default is enabled
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], on_off=on_off))


@register_command
@dataclass
class PP_EYEBER:
    """
    Obtain BER estimations of an eye diagram.
    """

    code: typing.ClassVar[int] = 361
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        eye_ber_estimation: XmpField[XmpStr] = XmpField(XmpStr)  # string, BER estimations of an eye diagram

    def get(self) -> "Token[GetDataAttr]":
        """GEt BER estimations of an eye diagram.

        :return: BER estimations of an eye diagram
        :rtype: PP_EYEBER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))


@register_command
@dataclass
class PP_PHYAUTONEG:
    """
    Autonegotiation settings of the PHY.
    """

    code: typing.ClassVar[int] = 362
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        fec_mode: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, FEC mode ON or OFF.
        reserved_1: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.
        reserved_2: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.
        reserved_3: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.
        reserved_4: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.

    @dataclass(frozen=True)
    class GetDataAttr:
        fec_mode: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, FEC mode ON or OFF.
        reserved_1: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.
        reserved_2: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.
        reserved_3: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.
        reserved_4: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved for future use.

    def get(self) -> "Token[GetDataAttr]":
        """Get auto-negotiation settings of the PHY.

        :return: FEC mode ON or OFF
        :rtype: PP_PHYAUTONEG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, fec_mode: OnOff, reserved_1: int, reserved_2: int, reserved_3: int, reserved_4: int) -> "Token":
        """Set auto-negotiation settings of the PHY.

        :param fec_mode: FEC mode ON or OFF
        :type fec_mode: OnOff
        :param reserved_1: reserved for future use.
        :type reserved_1: int
        :param reserved_2: reserved for future use.
        :type reserved_2: int
        :param reserved_3: reserved for future use.
        :type reserved_3: int
        :param reserved_4: reserved for future use.
        :type reserved_4: int
        """
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, fec_mode=fec_mode, reserved_1=reserved_1, reserved_2=reserved_2, reserved_3=reserved_3, reserved_4=reserved_4
            ),
        )

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Enable auto-negotiation settings of the PHY.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Disable auto-negotiation settings of the PHY.
    """


@register_command
@dataclass
class PP_TXPRBSTYPE:
    """
    The TX PRBS type used when the interface is in PRBS mode.
    """

    code: typing.ClassVar[int] = 364
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        prbs_inserted_type: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInsertedType)  # coded byte, PRBS inserted type.
        prbs_pattern: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSPattern)  # coded byte, PRBS pattern.
        invert: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInvertState)  # coded byte, PRBS invert state.

    @dataclass(frozen=True)
    class GetDataAttr:
        prbs_inserted_type: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInsertedType)  # coded byte, PRBS inserted type.
        prbs_pattern: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSPattern)  # coded byte, PRBS pattern.
        invert: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInvertState)  # coded byte, PRBS invert state.

    def get(self) -> "Token[GetDataAttr]":
        """Get the TX PRBS type used when the interface is in PRBS mode.

        :return: PRBS inserted type, PRBS pattern, and PRBS invert state.
        :rtype: PP_TXPRBSTYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, prbs_inserted_type: PRBSInsertedType, prbs_pattern: PRBSPattern, invert: PRBSInvertState) -> "Token":
        """Set the TX PRBS type used when the interface is in PRBS mode.

        :param prbs_inserted_type: PRBS inserted type
        :type prbs_inserted_type: PRBSInsertedType
        :param prbs_pattern: PRBS pattern
        :type prbs_pattern: PRBSPattern
        :param invert: PRBS invert state
        :type invert: PRBSInvertState
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, prbs_inserted_type=prbs_inserted_type, prbs_pattern=prbs_pattern, invert=invert)
        )


@register_command
@dataclass
class PP_RXPRBSTYPE:
    """
    The RX PRBS type used when the interface is in PRBS mode.
    """

    code: typing.ClassVar[int] = 365
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        prbs_inserted_type: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInsertedType)  # coded byte, PRBS inserted type.
        prbs_pattern: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSPattern)  # coded byte, PRBS pattern.
        invert: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInvertState)  # coded byte, PRBS invert state.
        statistics_mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSStatisticsMode)  # coded byte, PRBS statistics mode

    @dataclass(frozen=True)
    class GetDataAttr:
        prbs_inserted_type: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInsertedType)  # coded byte, PRBS inserted type.
        prbs_pattern: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSPattern)  # coded byte, PRBS pattern.
        invert: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInvertState)  # coded byte, PRBS invert state.
        statistics_mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSStatisticsMode)  # coded byte, PRBS statistics mode

    def get(self) -> "Token[GetDataAttr]":
        """Get the RX PRBS type used when the interface is in PRBS mode.

        :return: PRBS inserted type, PRBS pattern, PRBS invert state, and PRBS statistics mode.
        :rtype: PP_RXPRBSTYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, prbs_inserted_type: PRBSInsertedType, prbs_pattern: PRBSPattern, invert: PRBSInvertState, statistics_mode: PRBSStatisticsMode) -> "Token":
        """Set the RX PRBS type used when the interface is in PRBS mode.

        :param prbs_inserted_type: PRBS inserted type
        :type prbs_inserted_type: PRBSInsertedType
        :param prbs_pattern: PRBS pattern
        :type prbs_pattern: PRBSPattern
        :param invert: PRBS invert state
        :type invert: PRBSInvertState
        :param statistics_mode: PRBS statistics mode
        :type statistics_mode: PRBSStatisticsMode
        """
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, prbs_inserted_type=prbs_inserted_type, prbs_pattern=prbs_pattern, invert=invert, statistics_mode=statistics_mode
            ),
        )


@register_command
@dataclass
class PP_FECMODE:
    """
    FEC mode for port that supports FEC.
    """

    code: typing.ClassVar[int] = 366
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=FECMode)  # coded byte, FEC mode for port.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=FECMode)  # coded byte, FEC mode for port.

    def get(self) -> "Token[GetDataAttr]":
        """Get the FEC mode for port that supports FEC.

        :return: the FEC mode for port
        :rtype: PP_FECMODE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: FECMode) -> "Token":
        """Set the FEC mode for port that supports FEC.

        :param mode: FEC mode for port
        :type mode: FECMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_off = functools.partialmethod(set, FECMode.OFF) # Turn FEC off.
    """Turn FEC off.
    """
    set_rs_fec = functools.partialmethod(set, FECMode.RS_FEC) # Turn RS FEC on, either RS-FEC KR or RS-FEC KP, automatically selected based on the FEC modes supported by the port.
    """Turn RS FEC on, either RS-FEC KR or RS-FEC KP, automatically selected based on the FEC modes supported by the port.
    """
    set_fc_fec = functools.partialmethod(set, FECMode.FC_FEC) # Turn Firecode FEC on.
    """Turn Firecode FEC on.
    """
    # set_on = functools.partialmethod(set, FECMode.ON) # Turn RS FEC on, either RS-FEC KR or RS-FEC KP, automatically selected based on the FEC modes supported by the port.
    # set_rs_fec_kr = functools.partialmethod(set, FECMode.RS_FEC_KR) # Explicitly turn RS-FEC KR on.
    # set_rs_fec_kp = functools.partialmethod(set, FECMode.RS_FEC_KP) # Explicitly turn RS-FEC KP on.


@register_command
@dataclass
class PP_EYEDWELLBITS:
    """
    Min and max dwell bits for an eye capture.
    """

    code: typing.ClassVar[int] = 367
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        min_dwell_bit_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, minimum dwell bits for an eye capture
        max_dwell_bit_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum dwell bits for an eye capture

    @dataclass(frozen=True)
    class GetDataAttr:
        min_dwell_bit_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, minimum dwell bits for an eye capture
        max_dwell_bit_count: XmpField[XmpInt] = XmpField(XmpInt)  # integer, maximum dwell bits for an eye capture

    def get(self) -> "Token[GetDataAttr]":
        """Get the min and max dwell bits for an eye capture.

        :return: the min and the max dwell bits for an eye capture
        :rtype: PP_EYEDWELLBITS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, min_dwell_bit_count: int, max_dwell_bit_count: int) -> "Token":
        """Set the min and max dwell bits for an eye capture.

        :param min_dwell_bit_count: minimum dwell bits for an eye capture
        :type min_dwell_bit_count: int
        :param max_dwell_bit_count: maximum dwell bits for an eye capture
        :type max_dwell_bit_count: int
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._serdes_xindex],
                min_dwell_bit_count=min_dwell_bit_count,
                max_dwell_bit_count=max_dwell_bit_count,
            ),
        )


@register_command
@dataclass
class PP_PHYSIGNALSTATUS:
    """
    Obtain the PHY signal status.
    """

    code: typing.ClassVar[int] = 375
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        phy_signal_status: XmpField[XmpByte] = XmpField(XmpByte, choices=PHYSignalStatus)  # coded byte, PHY signal status

    def get(self) -> "Token[GetDataAttr]":
        """Get the PHY signal status.

        :return: PHY signal status
        :rtype: PP_PHYSIGNALSTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_PRBSTYPE:
    """
    Defines the PRBS type used when the interface is in PRBS mode.
    """

    code: typing.ClassVar[int] = 378
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        prbs_inserted_type: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInsertedType)  # coded byte, specifying where the PRBS is inserted.
        polynomial: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSPolynomial)  # coded byte, specifying which PRBS to use.
        invert: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInvertState)  # coded byte, specifying if the PRBS is inverted.
        statistics_mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSStatisticsMode)  # coded byte, specifying PRBS statistics mode, accumulative or for last second

    @dataclass(frozen=True)
    class GetDataAttr:
        prbs_inserted_type: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInsertedType)  # coded byte, specifying where the PRBS is inserted.
        polynomial: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSPolynomial)  # coded byte, specifying which PRBS that is used.
        invert: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSInvertState)  # coded byte, specifying if the PRBS is inverted.
        statistics_mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PRBSStatisticsMode)  # coded byte, specifying PRBS statistics mode, accumulative or for last second

    def get(self) -> "Token[GetDataAttr]":
        """Get the PRBS type used when the interface is in PRBS mode.

        :return: where the PRBS is inserted, which PRBS that is used, if the PRBS is inverted, and PRBS statistics mode
        :rtype: PP_PRBSTYPE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, prbs_inserted_type: PRBSInsertedType, polynomial: PRBSPolynomial, invert: PRBSInvertState, statistics_mode: PRBSStatisticsMode) -> "Token":
        """Set the PRBS type used when the interface is in PRBS mode.

        :param prbs_inserted_type: specifying where the PRBS is inserted
        :type prbs_inserted_type: PRBSInsertedType
        :param polynomial: specifying which PRBS that is used
        :type polynomial: PRBSPolynomial
        :param invert: specifying if the PRBS is inverted
        :type invert: PRBSInvertState
        :param statistics_mode: specifying PRBS statistics mode, accumulative or for last second
        :type statistics_mode: PRBSStatisticsMode
        """
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, prbs_inserted_type=prbs_inserted_type, polynomial=polynomial, invert=invert, statistics_mode=statistics_mode
            ),
        )


@register_command
@dataclass
class PP_PHYSETTINGS:
    """
    Get/Set low-level PHY settings.
    """

    code: typing.ClassVar[int] = 379
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        link_training_on_off: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, enabling/disabling link training.
        precode_on_off: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOffDefault)  # coded integer, enabling/disabling link precode.
        graycode_on_off: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, enabling/disabling link graycode.
        pam4_msb_lsb_swap: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, enabling/disabling PAM4 MSB/LSB swap.

    @dataclass(frozen=True)
    class GetDataAttr:
        link_training_on_off: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, enabling/disabling link training.
        precode_on_off: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOffDefault)  # coded integer, enabling/disabling link precode.
        graycode_on_off: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, enabling/disabling link graycode.
        pam4_msb_lsb_swap: XmpField[XmpInt] = XmpField(XmpInt, choices=OnOff)  # coded integer, enabling/disabling PAM4 MSB/LSB swap.

    def get(self) -> "Token[GetDataAttr]":
        """Get low-level PHY settings.

        :return: low-level PHY settings
        :rtype: PP_PHYSETTINGS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, link_training_on_off: OnOff, precode_on_off: OnOffDefault, graycode_on_off: OnOff, pam4_msb_lsb_swap: OnOff) -> "Token":
        """Set low-level PHY settings.

        :param link_training_on_off: enabling/disabling link training
        :type link_training_on_off: OnOff
        :param precode_on_off: enabling/disabling link precode
        :type precode_on_off: OnOffDefault
        :param graycode_on_off: enabling/disabling link graycode.
        :type graycode_on_off: OnOff
        :param pam4_msb_lsb_swap: enabling/disabling PAM4 MSB/LSB swap.
        :type pam4_msb_lsb_swap: OnOff
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                link_training_on_off=link_training_on_off,
                precode_on_off=precode_on_off,
                graycode_on_off=graycode_on_off,
                pam4_msb_lsb_swap=pam4_msb_lsb_swap
            ),
        )


@register_command
@dataclass
class PP_PHYRXEQ:
    """
    RX EQ parameters.
    """

    code: typing.ClassVar[int] = 380
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        auto: XmpField[XmpInt] = XmpField(XmpInt)  # integer, auto on or off
        ctle: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Continuous Time Linear equalization
        reserved: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved

    @dataclass(frozen=True)
    class GetDataAttr:
        auto: XmpField[XmpInt] = XmpField(XmpInt)  # integer, auto on or off
        ctle: XmpField[XmpInt] = XmpField(XmpInt)  # integer, Continuous Time Linear equalization
        reserved: XmpField[XmpInt] = XmpField(XmpInt)  # integer, reserved

    def get(self) -> "Token[GetDataAttr]":
        """Get RX EQ parameters.

        :return: auto on or off, CTLE, and reserved.
        :rtype: PP_PHYRXEQ.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, auto: int, ctle: int, reserved: int) -> "Token":
        """Set RX EQ parameters.

        :param auto:  auto on or off
        :type auto: int
        :param ctle: Continuous Time Linear equalization
        :type ctle: int
        :param reserved: reserved
        :type reserved: int
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], auto=auto, ctle=ctle, reserved=reserved)
        )


@register_command
@dataclass
class PP_AUTONEG:
    """
    Auto-negotiation settings of the PHY - for Thor-400G-7S-1P Thor-400G-7S-1P[b]
    and [c]
    """

    code: typing.ClassVar[int] = 381
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegMode)  # coded byte, mode
        tec_ability: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegTecAbility)  # coded byte, technical ability.
        fec_capable: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegFECOption)  # coded byte, FEC capable.
        fec_requested: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegFECOption)  # coded byte, FEC requested.
        pause_mode: XmpField[XmpInt] = XmpField(XmpInt, choices=PauseMode)  # coded byte, pause mode.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegMode)  # coded byte, mode
        tec_ability: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegTecAbility)  # coded byte, technical ability.
        fec_capable: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegFECOption)  # coded byte, FEC capable.
        fec_requested: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegFECOption)  # coded byte, FEC requested.
        pause_mode: XmpField[XmpInt] = XmpField(XmpInt, choices=PauseMode)  # coded byte, pause mode.

    def get(self) -> "Token[GetDataAttr]":
        """Get the auto-negotiation settings of the PHY.

        :return: auto-negotiation settings of the PHY including mode, technical ability, FEC capable, FEC requested, and pause mode.
        :rtype: PP_AUTONEG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: AutoNegMode, tec_ability: AutoNegTecAbility, fec_capable: AutoNegFECOption, fec_requested: AutoNegFECOption, pause_mode: PauseMode) -> "Token":
        """Set the auto-negotiation settings of the PHY.

        :param mode: auto neg mode
        :type mode: AutoNegMode
        :param tec_ability: technical ability
        :type tec_ability: AutoNegTecAbility
        :param fec_capable: FEC capable
        :type fec_capable: AutoNegFECOption
        :param fec_requested: FEC requested
        :type fec_requested: AutoNegFECOption
        :param pause_mode: pause mode
        :type pause_mode: PauseMode
        """
        return Token(
            self._connection,
            build_set_request(
                self, module=self._module, port=self._port, mode=mode, tec_ability=tec_ability, fec_capable=fec_capable, fec_requested=fec_requested, pause_mode=pause_mode
            ),
        )


@register_command
@dataclass
class PP_AUTONEGSTATUS:
    """
    Status of auto-negotiation settings of the PHY - for Thor-400G-7S-1P[b] and [c]
    """

    code: typing.ClassVar[int] = 382
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegMode)  # coded byte, mode
        fec: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegFECType)  # codec byte, FEC.
        auto_state: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegStatus)  # coded byte, autonegotiation state.
        tec_ability: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegTecAbility)  # coded byte, technical ability.
        fec_capable: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegFECStatus)  # coded byte, FEC capable partner.
        fec_requested: XmpField[XmpInt] = XmpField(XmpInt, choices=AutoNegFECStatus)  # coded byte, FEC requested partner.
        pause_mode: XmpField[XmpInt] = XmpField(XmpInt, choices=PauseMode)  # coded byte, pause mode.

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of auto-negotiation settings of the PHY.

        :return: the status of auto-negotiation settings of the PHY
        :rtype: PP_AUTONEGSTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_LINKTRAIN:
    """
    Link training settings - for Thor-400G-7S-1P rev.B. The PP_LINKTRAIN command is
    per port.
    """

    code: typing.ClassVar[int] = 383
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=LinkTrainingMode)  # coded byte, link training mode
        pam4_frame_size: XmpField[XmpByte] = XmpField(XmpByte, choices=PAM4FrameSize)  # codec byte, PAM4 frame size.
        nrz_pam4_init_cond: XmpField[XmpByte] = XmpField(XmpByte, choices=LinkTrainingInitCondition)  # coded byte, link training init condition.
        nrz_preset: XmpField[XmpByte] = XmpField(XmpByte, choices=NRZPreset)  # coded byte, NRZ preset.
        timeout_mode: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeoutMode)  # coded byte, timeout mode.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=LinkTrainingMode)  # coded byte, link training mode
        pam4_frame_size: XmpField[XmpByte] = XmpField(XmpByte, choices=PAM4FrameSize)  # codec byte, PAM4 frame size.
        nrz_pam4_init_cond: XmpField[XmpByte] = XmpField(XmpByte, choices=LinkTrainingInitCondition)  # coded byte, link training init condition.
        nrz_preset: XmpField[XmpByte] = XmpField(XmpByte, choices=NRZPreset)  # coded byte, NRZ preset.
        timeout_mode: XmpField[XmpByte] = XmpField(XmpByte, choices=TimeoutMode)  # coded byte, timeout mode.

    def get(self) -> "Token[GetDataAttr]":
        """Get the link training settings of the port.

        :return: the link training settings, including mode, PAM4 frame size, link training init condition, NRZ preset, and timeout mode.
        :rtype: PP_LINKTRAIN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(
        self, mode: LinkTrainingMode, pam4_frame_size: PAM4FrameSize, nrz_pam4_init_cond: LinkTrainingInitCondition, nrz_preset: NRZPreset, timeout_mode: TimeoutMode
    ) -> "Token":
        """Set the link training settings of the port.

        :param mode: link training mode
        :type mode: LinkTrainingMode
        :param pam4_frame_size: PAM4 frame size
        :type pam4_frame_size: PAM4FrameSize
        :param nrz_pam4_init_cond: link training init condition
        :type nrz_pam4_init_cond: LinkTrainingInitCondition
        :param nrz_preset: NRZ preset
        :type nrz_preset: NRZPreset
        :param timeout_mode: timeout mode
        :type timeout_mode: TimeoutMode
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                mode=mode,
                pam4_frame_size=pam4_frame_size,
                nrz_pam4_init_cond=nrz_pam4_init_cond,
                nrz_preset=nrz_preset,
                timeout_mode=timeout_mode,
            ),
        )


@register_command
@dataclass
class PP_LINKTRAINSTATUS:
    """
    Link training status - for Thor-400G-7S-1P rev.B. The PP_LINKTRAINSTATUS command
    is per lane.
    """

    code: typing.ClassVar[int] = 384
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _lane_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=LinkTrainingStatusMode)  # coded byte, link training mode
        status: XmpField[XmpByte] = XmpField(XmpByte, choices=LinkTrainingStatus)  # coded byte, lane status.
        failure: XmpField[XmpByte] = XmpField(XmpByte, choices=LinkTrainingFailureType)  # coded byte, failure type.

    def get(self) -> "Token[GetDataAttr]":
        """Get link training status of a lane of a port.

        :return: link training status of a lane of a port, including mode, lane status, and failure type.
        :rtype: PP_LINKTRAINSTATUS.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._lane_xindex]))


