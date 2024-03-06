from __future__ import annotations
from dataclasses import dataclass
import typing
import functools

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
    XmpInt,
    XmpLong,
    XmpSequence,
    XmpStr,
    Hex,
)
from .enums import (
    OnOff,
    StartOrStop,
    InjectErrorType,
    HeaderLockStatus,
    AlignLockStatus,
    PRBSLockStatus,
    SerdesStatus,
    FECMode,
    PRBSInsertedType,
    PRBSPolynomial,
    PRBSInvertState,
    PRBSStatisticsMode,
    AutoNegMode,
    AutoNegTecAbility,
    AutoNegFECOption,
    PauseMode,
    AutoNegFECType,
    AutoNegStatus,
    AutoNegFECStatus,
    LinkTrainingMode,
    PAM4FrameSize,
    LinkTrainingInitCondition,
    NRZPreset,
    TimeoutMode,
    LinkTrainingStatusMode,
    LinkTrainingStatus,
    LinkTrainingFailureType,
    PRBSOnOff,
    ErrorOnOff,
    PRBSPattern,
    PHYSignalStatus,
    OnOffDefault,
    RxEqExtCap,
    RxEqExtCapMode,
    PreCodingMode,
    GrayCodingMode,
    Endianness
)


@register_command
@dataclass
class PP_ALARMS_ERRORS:
    """
    Obtain the error count of each alarm, PCS Error, FEC Error, Header Error, Align
    Error, BIP Error, and High BER Error.
    """

    code: typing.ClassVar[int] = 272
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        total_alarms: int = field(XmpInt())
        """integer, total number of triggered alarms"""
        valid_mask: Hex = field(XmpHex(size=8))
        """8 hex bytes, mask of valid alarms"""
        los_error_count: int = field(XmpLong())
        """long integer, number of no-sync alarms"""
        total_pcs_error_count: int = field(XmpLong())
        """long integer, number of errors of PCS error alarm"""
        total_fec_error_count: int = field(XmpLong())
        """long integer, number of errors of FEC error alarm"""
        total_header_error_count: int = field(XmpLong())
        """long integer, number of errors of header error alarm"""
        total_align_error_count: int = field(XmpLong())
        """long integer, number of errors of alignment error alarm"""
        total_bip_error_count: int = field(XmpLong())
        """long integer, number of errors of BIP error alarm"""
        total_higher_error_count: int = field(XmpLong())
        """long integer, number of errors of high BER error alarm"""

    def get(self) -> Token[GetDataAttr]:
        """Get the error count of each alarm, PCS Error, FEC Error, Header Error, Align Error, BIP Error, and High BER Error.

        :return: the error count of each alarm, PCS Error, FEC Error, Header Error, Align Error, BIP Error, and High BER Error.
        :rtype: PP_ALARMS_ERRORS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_TXLANECONFIG:
    """
    The virtual lane index and artificial skew for data transmitted on a specified
    physical lane.
    """

    code: typing.ClassVar[int] = 280
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lane_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        virt_lane_index: int = field(XmpInt())
        """integer, virtual lane index."""
        skew: int = field(XmpInt())
        """integer, the inserted skew on the lane, in bit units."""

    class SetDataAttr(RequestBodyStruct):
        virt_lane_index: int = field(XmpInt())
        """integer, virtual lane index."""
        skew: int = field(XmpInt())
        """integer, the inserted skew on the lane, in bit units."""

    def get(self) -> Token[GetDataAttr]:
        """Get the virtual lane index and artificial skew for data transmitted on a specified physical lane.

        :return: virtual lane index, and the inserted skew on the lane, in bit units.
        :rtype: PP_TXLANECONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._lane_xindex]))

    def set(self, virt_lane_index: int, skew: int) -> Token[None]:
        """Set the virtual lane index and artificial skew for data transmitted on a specified physical lane.

        :param virt_lane_index: virtual lane index
        :type virt_lane_index: int
        :param skew: the inserted skew on the lane, in bit units
        :type skew: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._lane_xindex], virt_lane_index=virt_lane_index, skew=skew))


@register_command
@dataclass
class PP_TXLANEINJECT:
    """
    Inject a particular kind of CAUI error into a specific physical lane.
    """

    code: typing.ClassVar[int] = 281
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lane_xindex: int

    class SetDataAttr(RequestBodyStruct):
        inject_error_type: InjectErrorType = field(XmpByte())
        """coded byte, specifying what kind of error to inject."""

    def set(self, inject_error_type: InjectErrorType) -> Token[None]:
        """Inject a particular kind of CAUI error into a specific physical lane.

        :param inject_error_type: specifying what kind of error to inject
        :type inject_error_type: InjectErrorType
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._lane_xindex], inject_error_type=inject_error_type))

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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        prbs_seed: int = field(XmpInt())
        """integer, PRBS seed value."""
        prbs_on_off: PRBSOnOff = field(XmpByte())
        """code byte, whether this SerDes is transmitting PRBS data."""
        error_on_off: ErrorOnOff = field(XmpByte())
        """code byte, whether bit-level errors are injected into this SerDes."""

    class SetDataAttr(RequestBodyStruct):
        prbs_seed: int = field(XmpInt())
        """integer, PRBS seed value."""
        prbs_on_off: PRBSOnOff = field(XmpByte())
        """code byte, whether this SerDes is transmitting PRBS data."""
        error_on_off: ErrorOnOff = field(XmpByte())
        """code byte, whether bit-level errors are injected into this SerDes."""

    def get(self) -> Token[GetDataAttr]:
        """Get the PRBS configuration for a particular SerDes. When PRBS is enabled for any SerDes
        then the overall link is compromised and drops out of sync.

        :return: the PRBS configuration for a particular SerDes
        :rtype: PP_TXPRBSCONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, prbs_seed: int, prbs_on_off: PRBSOnOff, error_on_off: ErrorOnOff) -> Token[None]:
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
                self,
                module=self._module,
                port=self._port,
                indices=[self._serdes_xindex],
                prbs_seed=prbs_seed,
                prbs_on_off=prbs_on_off,
                error_on_off=error_on_off
            )
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        rate: int = field(XmpLong())
        """long integer, the number of bits between each error. 0, no error injection."""

    class SetDataAttr(RequestBodyStruct):
        rate: int = field(XmpLong())
        """long integer, the number of bits between each error. 0, no error injection."""

    def get(self) -> Token[GetDataAttr]:
        """Get the rate of continuous bit-level error injection. Errors are injected evenly
        across the SerDes where injection is enabled.

        :return: the number of bits between each error. 0, no error injection
        :rtype: PP_TXERRORRATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, rate: int) -> Token[None]:
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Inject a single bit-level error into one of the SerDes where injection is
        enabled.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_RXTOTALSTATS:
    """
    Provides FEC Total counters.
    """

    code: typing.ClassVar[int] = 270
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        total_rx_bit_count: int = field(XmpLong())
        """integer, total received bits"""

        total_rx_codeword_count: int = field(XmpLong())
        """integer, total received codewords"""

        total_corrected_codeword_count: int = field(XmpLong())
        """integer, total corrected codewords"""

        total_uncorrectable_codeword_count: int = field(XmpLong())
        """integer, total uncorrectable codewords"""

        total_corrected_symbol_count: int = field(XmpLong())
        """integer, total corrected symbol count."""

        total_pre_fec_ber: int = field(XmpLong())
        """integer, total pre-FEC BER estimate sent as "total_pre_fec_ber = received_bits / total_corfecerrs".
        To get the real total pre-BER, calculate the inverse: 1/total_pre_fec_ber. If zero physical bit errors have been detected,
        the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.
        """

        total_post_fec_ber: int = field(XmpLong())
        """integer, total post-FEC BER estimate sent as "total_post_fec_ber = received_bits / total_estimated_uncorrectable_errors".
        To get the real total post-BER, calculate the inverse: 1/total_post_fec_ber. If zero physical bit errors have been detected,
        the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get FEC Total counters of the port            

        :return:
            1. Total RX bits

            2. Total codewords

            3. Corrected codewords

            4. Uncorrectable codewords

            5. Corrected symbols

            6. Pre-FEC BER estimate, sent as "total_pre_fec_ber = received_bits / total_corfecerrs".
                To get the real total pre-BER, calculate the inverse: 1/total_pre_fec_ber.
                If zero physical bit errors have been detected, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.
                
            7. Post-FEC BER estimate sent as "total_post_fec_ber = received_bits / total_estimated_uncorrectable_errors".
                To get the real total post-BER, calculate the inverse: 1/total_post_fec_ber.
                If zero physical bit errors have been detected, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.

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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        stats_type: int = field(XmpLong())
        """long integer, currently always 0."""
        data_count: int = field(XmpLong())
        """long integer, number of values."""
        stats: typing.List[int] = field(XmpSequence(types_chunk=[XmpLong()]))
        """list of long integers, array of length value_count. The stats array shows how many FEC blocks have been seen with [0, 1, 2, 3....15, >15] symbol errors and the last one is the sum of FEC blocks with <=n symbol errors"""
        # sum_of_zero_and_correctable_fec_block: int = field(XmpLong())
        # """long integer, the sum of FEC blocks with <=n symbol errors."""

    def get(self) -> Token[GetDataAttr]:
        """Get statistics on how many FEC blocks have been seen with a given number of symbol errors.

        :return: stats type (currently always 0), number of values, correction stats array, and the number of received uncorrectable code words.

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
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        duration: int = field(XmpInt())
        """integer, 0 ms - 1000 ms; increments of 1 ms; 0 = permanently link down."""
        period: int = field(XmpInt())
        """integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms."""
        repetition: int = field(XmpInt())
        """integer, 1 - 64K; 0 = continuous."""

    class SetDataAttr(RequestBodyStruct):
        duration: int = field(XmpInt())
        """integer, 0 ms - 1000 ms; increments of 1 ms; 0 = permanently link down."""
        period: int = field(XmpInt())
        """integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms."""
        repetition: int = field(XmpInt())
        """integer, 1 - 64K; 0 = continuous."""

    def get(self) -> Token[GetDataAttr]:
        """Get port 'link flap' settings.

        :return: duration, period, and repetition of link flapping.
        :rtype: PP_LINKFLAP_PARAMS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, duration: int, period: int, repetition: int) -> Token[None]:
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
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether link flap is enabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether link flap is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get the port 'link flap' status of the port.

        :return: whether link flap is enabled
        :rtype: PP_LINKFLAP_ENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
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
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        duration: int = field(XmpInt())
        """integer, 0 ms - 5000m s; increments of 1 ms; 0 = constant BER"""
        period: int = field(XmpInt())
        """integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms"""
        repetition: int = field(XmpInt())
        """integer, 1 - 64K; 0 = continuous"""
        coeff: int = field(XmpInt())
        """long integer, (0.01 < coeff < 9.99) * 100"""
        exp: int = field(XmpInt(climb=(-16, -4)))
        """integer, -3 < exp < -17"""

    class SetDataAttr(RequestBodyStruct):
        duration: int = field(XmpInt())
        """integer, 0 ms - 5000m s; increments of 1 ms; 0 = constant BER"""
        period: int = field(XmpInt())
        """integer, 10 ms - 50000 ms; number of ms - must be multiple of 10 ms"""
        repetition: int = field(XmpInt())
        """integer, 1 - 64K; 0 = continuous"""
        coeff: int = field(XmpInt())
        """long integer, (0.01 < coeff < 9.99) * 100"""
        exp: int = field(XmpInt(climb=(-16, -4)))
        """integer, -3 < exp < -17"""

    def get(self) -> Token[GetDataAttr]:
        """Get PMA pulse error injection settings.

        :return: PMA pulse error injection settings
        :rtype: PP_PMAERRPUL_PARAMS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, duration: int, period: int, repetition: int, coeff: int, exp: int) -> Token[None]:
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
        :type exp: int
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lane_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        header_lock: HeaderLockStatus = field(XmpByte())
        """coded byte, whether this lane has achieved header lock."""
        align_lock: AlignLockStatus = field(XmpByte())
        """coded byte, whether this lane has achieved alignment lock."""

    def get(self) -> Token[GetDataAttr]:
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lane_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        virtual_lane: int = field(XmpInt())
        """integer, the logical lane number."""
        skew: int = field(XmpInt())
        """integer, the measured skew on the lane, in bit units."""

    def get(self) -> Token[GetDataAttr]:
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

    code: typing.ClassVar[int] = 271
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lane_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        header_error_count: int = field(XmpLong())
        """long integer, the number of header errors."""
        alignment_error_count: int = field(XmpLong())
        """long integer, the number of alignment errors."""
        bip8_error_count: int = field(XmpLong())
        """long integer, the number of bip8 errors."""
        corrected_fec_error_count: int = field(XmpLong())
        """long integer, corrected FEC bit errors."""
        pre_ber: int = field(XmpLong())
        """long integer, received_bits / corfecerrs. To get the pre_ber, calculate the inverse: 1/pre_ber.
        If zero bit errors have been received, the negative value "-received_bits" is provided, which can be used to generate the "< BER" value.
        """

    def get(self) -> Token[GetDataAttr]:
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        byte_count: int = field(XmpLong())
        """long integer, the number of bytes received while in PRBS lock."""
        error_count: int = field(XmpLong())
        """long integer, the number of errors detected while in PRBS lock."""
        lock: PRBSLockStatus = field(XmpByte())
        """coded byte, whether this lane is in PRBS lock."""

    def get(self) -> Token[GetDataAttr]:
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Clear all the PCS/PMA receiver statistics for a port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        nanowatts: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, received signal level, in nanowatts. 0, when no signal."""

    def get(self) -> Token[GetDataAttr]:
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
    value for each laser/wavelength, and the number of these depends on the kind of CFP transceiver used. The list is empty if the CFP transceiver does not support optical power read-out.
    """

    code: typing.ClassVar[int] = 296
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        nanowatts: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, received signal level, in nanowatts. 0, when no signal."""

    def get(self) -> Token[GetDataAttr]:
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
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether PMA pulse error inject is enabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether PMA pulse error inject is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of 'PMA pulse error inject'.

        :return: whether PMA pulse error inject is enabled
        :rtype: PP_PMAERRPUL_ENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        status: SerdesStatus = field(XmpByte())
        """coded byte, status of the serdes."""
        dummy: typing.List[int] = field(XmpSequence(types_chunk=[XmpByte()]))
        """list of bytes, should always be 0, reserved for future expansion."""

    class SetDataAttr(RequestBodyStruct):
        status: StartOrStop = field(XmpByte())
        """coded byte, status of the serdes."""
        dummy: typing.List[int] = field(XmpSequence(types_chunk=[XmpByte()]))
        """list of bytes, should always be 0, reserved for future expansion."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of the BER eye-measure data gathering process.

        :return: status of the serdes
        :rtype: PP_EYEMEASURE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, status: StartOrStop) -> Token[None]:
        """Start/stop a new BER eye-measure on a 25G serdes.

        :param status: status of the serdes
        :type status: StartOrStop
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], status=status, dummy=[]))

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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        x_resolution: int = field(XmpInt())
        """integer, number of columns, must be between 9 and 65 and be in the form 2^n+1"""
        y_resolution: int = field(XmpInt())
        """integer, number of columns, must be between 7 and 255 and be in the form 2^n-1"""

    class SetDataAttr(RequestBodyStruct):
        x_resolution: int = field(XmpInt())
        """integer, number of columns, must be between 9 and 65 and be in the form 2^n+1"""
        y_resolution: int = field(XmpInt())
        """integer, number of columns, must be between 7 and 255 and be in the form 2^n-1"""

    def get(self) -> Token[GetDataAttr]:
        """Get the resolution used for the next BER eye-measurement.

        :return: x resolution and y resolution
        :rtype: PP_EYERESOLUTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, x_resolution: int, y_resolution: int) -> Token[None]:
        """Set the resolution used for the next BER eye-measurement.

        :param x_resolution: number of columns, must be between 9 and 65 and be in the form 2^n+1
        :type x_resolution: int
        :param y_resolution: number of columns, must be between 7 and 255 and be in the form 2^n-1
        :type y_resolution: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._serdes_xindex],
                x_resolution=x_resolution,
                y_resolution=y_resolution
            )
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int
    _colum_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        x_resolution: int = field(XmpInt())
        """integer, specifying X resolution."""
        y_resolution: int = field(XmpInt())
        """integer, specifying Y resolution."""
        valid_column_count: int = field(XmpInt())
        """integer, specifying the number of valid columns."""
        values: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, showing the number of bit errors measured out of a total of 1M bits at each of the individual sampling points (x=timeaxis, y = 0/1 threshold)."""

    def get(self) -> Token[GetDataAttr]:
        """Read a single column of a measured BER eye on a 25G serdes.

        :return: x resolution, y resolution, number of valid columns, and the number of bit errors measured out of a total of 1M bits
            at each of the individual sampling points (x=timeaxis, y = 0/1 threshold).
        :rtype: PP_EYEREAD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._colum_xindex]))


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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        width_mui: int = field(XmpInt())
        """integer, value and unit 0..1000 (mUI), group = Horizontal bathtub curve"""
        height_mv: int = field(XmpInt())
        """integer, value and unit 0..1000 (mV), group = Vertical bathtub curve"""
        h_slope_left: int = field(XmpInt())
        """integer, value and unit (Q/UI) x100, signed integer, group = Horizontal bathtub curve"""
        h_slope_right: int = field(XmpInt())
        """integer, value and unit (Q/UI) x100, signed integer, group = Horizontal bathtub curve"""
        y_intercept_left: int = field(XmpInt())
        """integer, value and unit (Q) x100, signed integer, group = Horizontal bathtub curve"""
        y_intercept_right: int = field(XmpInt())
        """integer, value and unit (Q) x100, signed integer, group = Horizontal bathtub curve"""
        r_squared_fit_left: int = field(XmpInt())
        """integer, value and unit Int x100, group = Horizontal bathtub curve"""
        r_squared_fit_right: int = field(XmpInt())
        """integer, value and unit Int x100, group = Horizontal bathtub curve"""
        est_rj_rms_left: int = field(XmpInt())
        """integer, value and unit (mUI) x1000, group = Horizontal bathtub curve"""
        est_rj_rms_right: int = field(XmpInt())
        """integer, value and unit (mUI) x1000, group = Horizontal bathtub curve"""
        est_dj_pp: int = field(XmpInt())
        """integer, value and unit (mUI) x1000, group = Horizontal bathtub curve"""
        v_slope_bottom: int = field(XmpInt())
        """integer, value and unit (mV/Q) x100, signed integer, group = Vertical bathtub curve"""
        v_slope_top: int = field(XmpInt())
        """integer, value and unit (mV/Q) x100, signed integer, group = Vertical bathtub curve"""
        x_intercept_bottom: int = field(XmpInt())
        """integer, value and unit (Q) x100), signed integer, group = Vertical bathtub curve"""
        x_intercept_top: int = field(XmpInt())
        """integer, value and unit (Q) x100, signed integer, group = Vertical bathtub curve"""
        r_squared_fit_bottom: int = field(XmpInt())
        """integer, value and unit Int x100, group = Vertical bathtub curve"""
        r_squared_fit_top: int = field(XmpInt())
        """integer, value and unit Int x100, group = Vertical bathtub curve"""
        est_rj_rms_bottom: int = field(XmpInt())
        """integer, value and unit (mV) x1000, group = Vertical bathtub curve"""
        est_rj_rms_top: int = field(XmpInt())
        """integer, value and unit (mV) x1000, group = Vertical bathtub curve"""

    def get(self) -> Token[GetDataAttr]:
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

    .. versionchanged:: 1.1

    """

    code: typing.ClassVar[int] = 358
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        pre: int = field(XmpInt())
        """integer, preemphasis, (range: Module dependent), default = 0 (neutral)."""
        main: int = field(XmpInt())
        """integer, amplification, (range: Module dependent), default = 0 (neutral)."""
        post: int = field(XmpInt())
        """integer, postemphasis, (range: Module dependent), default = 0 (neutral)."""
        pre2: int = field(XmpInt())
        """integer, preemphasis, (range: Module dependent), default = 0 (neutral)."""
        pre3_post2: int = field(XmpInt())
        """integer, postemphasis, (range: Module dependent), default = 0 (neutral)."""
        post3: int = field(XmpInt())
        """integer, postemphasis, (range: Module dependent), default = 0 (neutral)."""
        mode: int = field(XmpInt())
        """integer, value must be 4"""

    class SetDataAttr(RequestBodyStruct):
        pre: int = field(XmpInt())
        """integer, preemphasis, (range: Module dependent), default = 0 (neutral)."""
        main: int = field(XmpInt())
        """integer, amplification, (range: Module dependent), default = 0 (neutral)."""
        post: int = field(XmpInt())
        """integer, postemphasis, (range: Module dependent), default = 0 (neutral)."""
        pre2: int = field(XmpInt())
        """integer, preemphasis, (range: Module dependent), default = 0 (neutral)."""
        pre3_post2: int = field(XmpInt())
        """integer, postemphasis, (range: Module dependent), default = 0 (neutral)."""
        post3: int = field(XmpInt())
        """integer, postemphasis, (range: Module dependent), default = 0 (neutral)."""
        mode: int = field(XmpInt())
        """integer, value must be 4"""

    def get(self) -> Token[GetDataAttr]:
        """Get the equalizer settings of the on-board PHY in the
        transmission direction (towards the transceiver cage) on Thor and Loki modules.

        :return: preemphasis, (range: Module dependent), default = 0 (neutral).
        :rtype: PP_PHYTXEQ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, pre2: int, pre: int, main: int, post: int, pre3_post2: int, post3: int) -> Token[None]:
        """Set the equalizer settings of the on-board PHY in the
        transmission direction (towards the transceiver cage) on Thor and Loki modules.

        :param pre2: pre2 emphasis
        :type pre2: int
        :param pre: pre emphasis
        :type pre: int
        :param main: main emphasis
        :type main: int
        :param post: post emphasis
        :type post: int
        :param pre3_post2: post2 or pre3 emphasis
        :type pre3_post2: int
        :param post3: post3 emphasis
        :type post3: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._serdes_xindex],
                pre2=pre2,
                pre=pre,
                main=main,
                post=post,
                pre3_post2=pre3_post2,
                post3=post3,
                mode=4))


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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class SetDataAttr(RequestBodyStruct):
        dummy: int = field(XmpByte())
        """byte, reserved for future improvements, always set to 1"""

    def set(self, dummy: int) -> Token[None]:
        """Trigger a new retuning of the receive equalizer on the PHY for one of the 25G
        serdes.

        :param dummy: reserved for future improvements, always set to 1
        :type dummy: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], dummy=dummy))


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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: int = field(XmpByte())
        """coded byte, enable/disable automatic receiving PHY retuning. Default is enabled."""

    class SetDataAttr(RequestBodyStruct):
        on_off: int = field(XmpByte())
        """coded byte, enable/disable automatic receiving PHY retuning. Default is enabled."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether the auto PHY retuning is enabled.

        :return: enable/disable automatic receiving PHY retuning
        :rtype: PP_PHYAUTOTUNE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, on_off: OnOff) -> Token[None]:
        """Enable/disable automatic receiving PHY retuning. Default is enabled.

        :param on_off: Enable/disable automatic receiving PHY retuning. Default is enabled
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], on_off=on_off))
    
    set_off = functools.partialmethod(set, OnOff.OFF)
    """Turn off tap autotune.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Turn off tap autotune.
    """


@register_command
@dataclass
class PP_EYEBER:
    """
    Obtain BER estimations of an eye diagram.
    """

    code: typing.ClassVar[int] = 361
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        eye_ber_estimation: str = field(XmpStr())
        """string, BER estimations of an eye diagram"""

    def get(self) -> Token[GetDataAttr]:
        """GEt BER estimations of an eye diagram.

        :return: BER estimations of an eye diagram
        :rtype: PP_EYEBER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))


@register_command
@dataclass
class PP_PHYAUTONEG:
    """
    Auto-negotiation settings of the PHY.
    """

    code: typing.ClassVar[int] = 362
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        fec_mode: OnOff = field(XmpInt())
        """coded integer, FEC mode ON or OFF."""
        reserved_1: int = field(XmpInt())
        """integer, reserved for future use."""
        reserved_2: int = field(XmpInt())
        """integer, reserved for future use."""
        reserved_3: int = field(XmpInt())
        """integer, reserved for future use."""
        reserved_4: int = field(XmpInt())
        """integer, reserved for future use."""

    class SetDataAttr(RequestBodyStruct):
        fec_mode: OnOff = field(XmpInt())
        """coded integer, FEC mode ON or OFF."""
        reserved_1: int = field(XmpInt())
        """integer, reserved for future use."""
        reserved_2: int = field(XmpInt())
        """integer, reserved for future use."""
        reserved_3: int = field(XmpInt())
        """integer, reserved for future use."""
        reserved_4: int = field(XmpInt())
        """integer, reserved for future use."""

    def get(self) -> Token[GetDataAttr]:
        """Get auto-negotiation settings of the PHY.

        :return: FEC mode ON or OFF
        :rtype: PP_PHYAUTONEG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, fec_mode: OnOff, reserved_1: int, reserved_2: int, reserved_3: int, reserved_4: int) -> Token[None]:
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
                self,
                module=self._module,
                port=self._port, fec_mode=fec_mode,
                reserved_1=reserved_1,
                reserved_2=reserved_2,
                reserved_3=reserved_3,
                reserved_4=reserved_4
            )
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        prbs_inserted_type: PRBSInsertedType = field(XmpByte())
        """coded byte, PRBS inserted type."""
        prbs_pattern: PRBSPattern = field(XmpByte())
        """coded byte, PRBS pattern."""
        invert: PRBSInvertState = field(XmpByte())
        """coded byte, PRBS invert state."""

    class SetDataAttr(RequestBodyStruct):
        prbs_inserted_type: PRBSInsertedType = field(XmpByte())
        """coded byte, PRBS inserted type."""
        prbs_pattern: PRBSPattern = field(XmpByte())
        """coded byte, PRBS pattern."""
        invert: PRBSInvertState = field(XmpByte())
        """coded byte, PRBS invert state."""

    def get(self) -> Token[GetDataAttr]:
        """Get the TX PRBS type used when the interface is in PRBS mode.

        :return: PRBS inserted type, PRBS pattern, and PRBS invert state.
        :rtype: PP_TXPRBSTYPE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, prbs_inserted_type: PRBSInsertedType, prbs_pattern: PRBSPattern, invert: PRBSInvertState) -> Token[None]:
        """Set the TX PRBS type used when the interface is in PRBS mode.

        :param prbs_inserted_type: PRBS inserted type
        :type prbs_inserted_type: PRBSInsertedType
        :param prbs_pattern: PRBS pattern
        :type prbs_pattern: PRBSPattern
        :param invert: PRBS invert state
        :type invert: PRBSInvertState
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                prbs_inserted_type=prbs_inserted_type,
                prbs_pattern=prbs_pattern,
                invert=invert
            )
        )


@register_command
@dataclass
class PP_RXPRBSTYPE:
    """
    The RX PRBS type used when the interface is in PRBS mode.
    """

    code: typing.ClassVar[int] = 365
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        prbs_inserted_type: PRBSInsertedType = field(XmpByte())
        """coded byte, PRBS inserted type."""
        prbs_pattern: PRBSPattern = field(XmpByte())
        """coded byte, PRBS pattern."""
        invert: PRBSInvertState = field(XmpByte())
        """coded byte, PRBS invert state."""
        statistics_mode: PRBSStatisticsMode = field(XmpByte())
        """coded byte, PRBS statistics mode"""

    class SetDataAttr(RequestBodyStruct):
        prbs_inserted_type: PRBSInsertedType = field(XmpByte())
        """coded byte, PRBS inserted type."""
        prbs_pattern: PRBSPattern = field(XmpByte())
        """coded byte, PRBS pattern."""
        invert: PRBSInvertState = field(XmpByte())
        """coded byte, PRBS invert state."""
        statistics_mode: PRBSStatisticsMode = field(XmpByte())
        """coded byte, PRBS statistics mode"""

    def get(self) -> Token[GetDataAttr]:
        """Get the RX PRBS type used when the interface is in PRBS mode.

        :return: PRBS inserted type, PRBS pattern, PRBS invert state, and PRBS statistics mode.
        :rtype: PP_RXPRBSTYPE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, prbs_inserted_type: PRBSInsertedType, prbs_pattern: PRBSPattern, invert: PRBSInvertState, statistics_mode: PRBSStatisticsMode) -> Token[None]:
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
                self,
                module=self._module,
                port=self._port,
                prbs_inserted_type=prbs_inserted_type,
                prbs_pattern=prbs_pattern,
                invert=invert,
                statistics_mode=statistics_mode
            )
        )


@register_command
@dataclass
class PP_FECMODE:
    """
    FEC mode for port that supports FEC.
    """

    code: typing.ClassVar[int] = 366
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: FECMode = field(XmpByte())
        """coded byte, FEC mode for port."""

    class SetDataAttr(RequestBodyStruct):
        mode: FECMode = field(XmpByte())
        """coded byte, FEC mode for port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the FEC mode for port that supports FEC.

        :return: the FEC mode for port
        :rtype: PP_FECMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: FECMode) -> Token[None]:
        """Set the FEC mode for port that supports FEC.

        :param mode: FEC mode for port
        :type mode: FECMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_off = functools.partialmethod(set, FECMode.OFF)
    """Turn FEC off."""

    set_rs_fec = functools.partialmethod(set, FECMode.RS_FEC)
    """Turn RS FEC on, either RS-FEC KR or RS-FEC KP, automatically selected based on the FEC modes supported by the port."""

    set_fc_fec = functools.partialmethod(set, FECMode.FC_FEC)
    """Turn Firecode FEC on."""


@register_command
@dataclass
class PP_EYEDWELLBITS:
    """
    Min and max dwell bits for an eye capture.
    """

    code: typing.ClassVar[int] = 367
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        min_dwell_bit_count: int = field(XmpInt())
        """integer, minimum dwell bits for an eye capture"""
        max_dwell_bit_count: int = field(XmpInt())
        """integer, maximum dwell bits for an eye capture"""

    class SetDataAttr(RequestBodyStruct):
        min_dwell_bit_count: int = field(XmpInt())
        """integer, minimum dwell bits for an eye capture"""
        max_dwell_bit_count: int = field(XmpInt())
        """integer, maximum dwell bits for an eye capture"""

    def get(self) -> Token[GetDataAttr]:
        """Get the min and max dwell bits for an eye capture.

        :return: the min and the max dwell bits for an eye capture
        :rtype: PP_EYEDWELLBITS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, min_dwell_bit_count: int, max_dwell_bit_count: int) -> Token[None]:
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
                max_dwell_bit_count=max_dwell_bit_count
            )
        )


@register_command
@dataclass
class PP_PHYSIGNALSTATUS:
    """
    Obtain the PHY signal status.
    """

    code: typing.ClassVar[int] = 375
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        phy_signal_status: PHYSignalStatus = field(XmpByte())
        """coded byte, PHY signal status"""

    def get(self) -> Token[GetDataAttr]:
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

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        prbs_inserted_type: PRBSInsertedType = field(XmpByte())
        """coded byte, specifying where the PRBS is inserted."""
        polynomial: PRBSPolynomial = field(XmpByte())
        """coded byte, specifying which PRBS that is used."""
        invert: PRBSInvertState = field(XmpByte())
        """coded byte, specifying if the PRBS is inverted."""
        statistics_mode: PRBSStatisticsMode = field(XmpByte())
        """coded byte, specifying PRBS statistics mode, accumulative or for last second"""

    class SetDataAttr(RequestBodyStruct):
        prbs_inserted_type: PRBSInsertedType = field(XmpByte())
        """coded byte, specifying where the PRBS is inserted."""
        polynomial: PRBSPolynomial = field(XmpByte())
        """coded byte, specifying which PRBS to use."""
        invert: PRBSInvertState = field(XmpByte())
        """coded byte, specifying if the PRBS is inverted."""
        statistics_mode: PRBSStatisticsMode = field(XmpByte())
        """coded byte, specifying PRBS statistics mode, accumulative or for last second"""

    def get(self) -> Token[GetDataAttr]:
        """Get the PRBS type used when the interface is in PRBS mode.

        :return: where the PRBS is inserted, which PRBS that is used, if the PRBS is inverted, and PRBS statistics mode
        :rtype: PP_PRBSTYPE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, prbs_inserted_type: PRBSInsertedType, polynomial: PRBSPolynomial, invert: PRBSInvertState, statistics_mode: PRBSStatisticsMode) -> Token[None]:
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
                self,
                module=self._module,
                port=self._port,
                prbs_inserted_type=prbs_inserted_type,
                polynomial=polynomial,
                invert=invert,
                statistics_mode=statistics_mode
            )
        )


@register_command
@dataclass
class PP_PHYSETTINGS:
    """
    Get/Set low-level PHY settings.
    """

    code: typing.ClassVar[int] = 379
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        link_training_on_off: OnOff = field(XmpInt())
        """coded integer, enabling/disabling link training."""
        precode_on_off: OnOffDefault = field(XmpInt())
        """coded integer, enabling/disabling link precode."""
        graycode_on_off: OnOff = field(XmpInt())
        """coded integer, enabling/disabling link graycode."""
        pam4_msb_lsb_swap: OnOff = field(XmpInt())
        """coded integer, enabling/disabling PAM4 MSB/LSB swap."""

    class SetDataAttr(RequestBodyStruct):
        link_training_on_off: OnOff = field(XmpInt())
        """coded integer, enabling/disabling link training."""
        precode_on_off: OnOffDefault = field(XmpInt())
        """coded integer, enabling/disabling link precode."""
        graycode_on_off: OnOff = field(XmpInt())
        """coded integer, enabling/disabling link graycode."""
        pam4_msb_lsb_swap: OnOff = field(XmpInt())
        """coded integer, enabling/disabling PAM4 MSB/LSB swap."""

    def get(self) -> Token[GetDataAttr]:
        """Get low-level PHY settings.

        :return: low-level PHY settings
        :rtype: PP_PHYSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, link_training_on_off: OnOff, precode_on_off: OnOffDefault, graycode_on_off: OnOff, pam4_msb_lsb_swap: OnOff) -> Token[None]:
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
            )
        )


@register_command
@dataclass
class PP_PHYRXEQ:
    """
    RX EQ parameters (For non Freya Modules).
    """

    code: typing.ClassVar[int] = 380
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        auto: int = field(XmpInt())
        """integer, auto on or off"""
        ctle: int = field(XmpInt())
        """integer, Continuous Time Linear equalization"""
        reserved: int = field(XmpInt())
        """integer, reserved"""

    class SetDataAttr(RequestBodyStruct):
        auto: int = field(XmpInt())
        """integer, auto on or off"""
        ctle: int = field(XmpInt())
        """integer, Continuous Time Linear equalization"""
        reserved: int = field(XmpInt())
        """integer, reserved"""

    def get(self) -> Token[GetDataAttr]:
        """Get RX EQ parameters.

        :return: auto on or off, CTLE, and reserved.
        :rtype: PP_PHYRXEQ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, auto: int, ctle: int, reserved: int) -> Token[None]:
        """Set RX EQ parameters.

        :param auto:  auto on or off
        :type auto: int
        :param ctle: Continuous Time Linear equalization
        :type ctle: int
        :param reserved: reserved
        :type reserved: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], auto=auto, ctle=ctle, reserved=reserved))


@register_command
@dataclass
class PP_PHYRXEQ_EXT:
    """
    GET/SET RX EQ Advanced parameters(Only for Freya Modules).
    """

    code: typing.ClassVar[int] = 397
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int
    _capability_type: RxEqExtCap

    class GetDataAttr(ResponseBodyStruct):
        mode: RxEqExtCapMode = field(XmpInt())
        """The capability mode"""
        value: int = field(XmpInt())
        """The value for the capability"""

    class SetDataAttr(RequestBodyStruct):
        mode: RxEqExtCapMode = field(XmpInt())
        """The capability mode Auto/Manual/Freeze"""
        value: int = field(XmpInt())
        """The value for the capability"""

    def get(self) -> Token[GetDataAttr]:
        """Get RX EQ Advanced parameters.

        :return: mode Auto/Manual/Freeze, value.
        :rtype: PP_PHYRXEQ_EXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._capability_type]))
    
    def set(self, mode: RxEqExtCapMode, value: int) -> Token[None]:
        """Set RX EQ Advanced parameters.
        The type of the capability(RxEqExtCap) should be passed as the second index.

        :param mode:  Auto/Manual/Freeze
        :type mode: RxEqExtCapMode
        :param value: The value for the capability
        :type value: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._capability_type], mode=mode, value=value))


@register_command
@dataclass
class PP_PHYRXEQSTATUS_EXT:
    """
    Get RX EQ advanced parameter values. (Only for Freya modules)
    """

    code: typing.ClassVar[int] = 398
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int
    _capability_type: RxEqExtCap

    class GetDataAttr(ResponseBodyStruct):
        value1: int = field(XmpInt())
        """the 1st value for the capability"""
        value2: int = field(XmpInt())
        """the 2nd value for the capability"""


    def get(self) -> Token[GetDataAttr]:
        """Get RX EQ Advanced parameters.

        :return: mode Auto/Manual/Freeze, value.
        :rtype: PP_PHYRXEQ_EXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._capability_type]))

    

@register_command
@dataclass
class PP_AUTONEG:
    """
    Auto-negotiation settings of the PHY - for Thor-400G-7S-1P Thor-400G-7S-1P[b]
    and [c]
    """

    code: typing.ClassVar[int] = 381
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: AutoNegMode = field(XmpInt())
        """coded integer, mode"""
        tec_ability: AutoNegTecAbility = field(XmpInt())
        """coded integer, technical ability."""
        fec_capable: int = field(XmpInt())
        """coded integer, FEC capable."""
        fec_requested: int = field(XmpInt())
        """coded integer, FEC requested."""
        pause_mode: PauseMode = field(XmpInt())
        """coded integer, pause mode."""

    class SetDataAttr(RequestBodyStruct):
        mode: AutoNegMode = field(XmpInt())
        """coded integer, mode"""
        tec_ability: AutoNegTecAbility = field(XmpInt())
        """coded integer, technical ability."""
        fec_capable: int = field(XmpInt())
        """coded integer, FEC capable."""
        fec_requested: int = field(XmpInt())
        """coded integer, FEC requested."""
        pause_mode: PauseMode = field(XmpInt())
        """coded integer, pause mode."""

    def get(self) -> Token[GetDataAttr]:
        """Get the auto-negotiation settings of the PHY.

        :return: auto-negotiation settings of the PHY including mode, technical ability, FEC capable, FEC requested, and pause mode.
        :rtype: PP_AUTONEG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: AutoNegMode, tec_ability: AutoNegTecAbility, fec_capable: AutoNegFECOption, fec_requested: AutoNegFECOption, pause_mode: PauseMode) -> Token[None]:
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
                self,
                module=self._module,
                port=self._port,
                mode=mode,
                tec_ability=tec_ability,
                fec_capable=fec_capable,
                fec_requested=fec_requested,
                pause_mode=pause_mode
            )
        )


@register_command
@dataclass
class PP_AUTONEGSTATUS:
    """
    Status of auto-negotiation settings of the PHY - for Thor-400G-7S-1P[b] and [c]
    """

    code: typing.ClassVar[int] = 382
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: AutoNegMode = field(XmpInt())
        """coded integer, mode"""
        fec: AutoNegFECType = field(XmpInt())
        """codec integer, FEC."""
        auto_state: AutoNegStatus = field(XmpInt())
        """coded integer, auto-negotiation state."""
        tec_ability: AutoNegTecAbility = field(XmpInt())
        """coded integer, technical ability."""
        fec_capable: int = field(XmpInt())
        """coded integer, FEC capable partner."""
        fec_requested: int = field(XmpInt())
        """coded integer, FEC requested partner."""
        pause_mode: PauseMode = field(XmpInt())
        """coded integer, pause mode."""

    def get(self) -> Token[GetDataAttr]:
        """Get the status of auto-negotiation settings of the PHY.

        :return: the status of auto-negotiation settings of the PHY
        :rtype: PP_AUTONEGSTATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PP_LINKTRAIN:
    """
    Link training settings - for Thor-400G-7S-1P and Freya modules
    """

    code: typing.ClassVar[int] = 383
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: LinkTrainingMode = field(XmpByte())
        """coded byte, link training mode"""
        pam4_frame_size: PAM4FrameSize = field(XmpByte())
        """codec byte, PAM4 frame size."""
        nrz_pam4_init_cond: LinkTrainingInitCondition = field(XmpByte())
        """coded byte, link training init condition."""
        nrz_preset: NRZPreset = field(XmpByte())
        """coded byte, NRZ preset."""
        timeout_mode: TimeoutMode = field(XmpByte())
        """coded byte, timeout mode."""

    class SetDataAttr(RequestBodyStruct):
        mode: LinkTrainingMode = field(XmpByte())
        """coded byte, link training mode"""
        pam4_frame_size: PAM4FrameSize = field(XmpByte())
        """codec byte, PAM4 frame size."""
        nrz_pam4_init_cond: LinkTrainingInitCondition = field(XmpByte())
        """coded byte, link training init condition."""
        nrz_preset: NRZPreset = field(XmpByte())
        """coded byte, NRZ preset."""
        timeout_mode: TimeoutMode = field(XmpByte())
        """coded byte, timeout mode."""

    def get(self) -> Token[GetDataAttr]:
        """Get the link training settings of the port.

        :return: the link training settings, including mode, PAM4 frame size, link training init condition, NRZ preset, and timeout mode.
        :rtype: PP_LINKTRAIN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(
        self,
        mode: LinkTrainingMode,
        pam4_frame_size: PAM4FrameSize,
        nrz_pam4_init_cond: LinkTrainingInitCondition,
        nrz_preset: NRZPreset,
        timeout_mode: TimeoutMode
    ) -> Token[None]:
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
                timeout_mode=timeout_mode
            )
        )


@register_command
@dataclass
class PP_LINKTRAINSTATUS:
    """
    Per lane Link training status - for Thor-400G-7S-1P and Freya modules
    """

    code: typing.ClassVar[int] = 384
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        mode: LinkTrainingStatusMode = field(XmpByte())
        """coded byte, link training mode"""
        status: LinkTrainingStatus = field(XmpByte())
        """coded byte, lane status."""
        failure: LinkTrainingFailureType = field(XmpByte())
        """coded byte, failure type."""

    def get(self) -> Token[GetDataAttr]:
        """Get link training status of a lane of a port.

        :return: link training status of a lane of a port, including mode, lane status, and failure type.
        :rtype: PP_LINKTRAINSTATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

@register_command
@dataclass
class PP_PRECODING:
    """
    GET/SET Pre-Coding Configurations. (only for Freya)
    """
    
    code: typing.ClassVar[int] = 420
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        rx_mode: PreCodingMode = field(XmpInt())
        """RX Mode Off/On/Auto"""
        rx_endianness: Endianness = field(XmpInt())
        """RX Endianness Normal/Reverted(BigEndian/LittleEndian)) """
        tx_mode: PreCodingMode = field(XmpInt())
        """TX Mode Off/On/Auto"""
        tx_endianness: Endianness = field(XmpInt())
        """TX Endianness Normal/Reverted(BigEndian/LittleEndian)) """

    class SetDataAttr(RequestBodyStruct):
        rx_mode: PreCodingMode = field(XmpInt())
        """RX Mode Off/On/Auto"""
        rx_endianness: Endianness = field(XmpInt())
        """RX Endianness Normal/Reverted(BigEndian/LittleEndian)) """
        tx_mode: PreCodingMode = field(XmpInt())
        """TX Mode Off/On/Auto"""
        tx_endianness: Endianness = field(XmpInt())
        """TX Endianness Normal/Reverted(BigEndian/LittleEndian)) """

    def get(self) -> Token[GetDataAttr]:
        """Get the Pre-Coding Configurations.

        :return: Pre-Coding configurations including rx_mode, rx_endianness, tx_mode, and tx_endianness.
        :rtype: PP_PRECODING.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, rx_mode: PreCodingMode, rx_endianness: Endianness, tx_mode: PreCodingMode, tx_endianness: Endianness) -> Token[None]:
        """Set the Rx Pre-coding settings of the PHY.

        :param rx_mode: The RX Mode(Off/On/Auto)
        :type rx_mode: PreCodingMode
        :param rx_endianness: RX Endianness type
        :type rx_endianness: Endianness
        :param tx_mode: The TX Mode(Off/On/Auto)
        :type tx_mode: PreCodingMode
        :param tx_endianness: TX Endianness type
        :type endianness: Endianness
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], rx_mode=rx_mode, rx_endianness=rx_endianness, tx_mode=tx_mode, tx_endianness=tx_endianness))

@register_command
@dataclass
class PP_GRAYCODING:
    """
    GET/SET Gray-Coding Configurations. (only for Freya)
    """
    
    code: typing.ClassVar[int] = 421
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        rx_mode: GrayCodingMode = field(XmpInt())
        """RX Mode Off/On/Auto"""
        rx_endianness: Endianness = field(XmpInt())
        """RX Endianness Normal/Reverted(BigEndian/LittleEndian)) """
        tx_mode: GrayCodingMode = field(XmpInt())
        """TX Mode Off/On/Auto"""
        tx_endianness: Endianness = field(XmpInt())
        """TX Endianness Normal/Reverted(BigEndian/LittleEndian)) """

    class SetDataAttr(RequestBodyStruct):
        rx_mode: GrayCodingMode = field(XmpInt())
        """RX Mode Off/On/Auto"""
        rx_endianness: Endianness = field(XmpInt())
        """RX Endianness Normal/Reverted(BigEndian/LittleEndian)) """
        tx_mode: GrayCodingMode = field(XmpInt())
        """TX Mode Off/On/Auto"""
        tx_endianness: Endianness = field(XmpInt())
        """TX Endianness Normal/Reverted(BigEndian/LittleEndian)) """

    def get(self) -> Token[GetDataAttr]:
        """Get the Gray-Coding Configurations.

        :return: Gray-Coding configurations including rx_mode, rx_endianness, tx_mode, and tx_endianness.
        :rtype: PP_GRAYCODING.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, rx_mode: GrayCodingMode, rx_endianness: Endianness, tx_mode: GrayCodingMode, tx_endianness: Endianness) -> Token[None]:
        """Set the Rx Gray-coding settings of the PHY.

        :param rx_mode: The RX Mode(Off/On/Auto)
        :type rx_mode: GrayCodingMode
        :param rx_endianness: RX Endianness type
        :type rx_endianness: Endianness
        :param tx_mode: The TX Mode(Off/On/Auto)
        :type tx_mode: GrayCodingMode
        :param tx_endianness: TX Endianness type
        :type endianness: Endianness
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], rx_mode=rx_mode, rx_endianness=rx_endianness, tx_mode=tx_mode, tx_endianness=tx_endianness))


@register_command
@dataclass
class PP_PRECODINGSTATUS:
    """
    GET Pre-Coding status (only for Freya)
    """
    
    code: typing.ClassVar[int] = 422
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        rx_mode: OnOff = field(XmpInt())
        """RX Mode Off/On"""
        rx_endianness: Endianness = field(XmpInt())
        """RX Endianness Normal/Reverted(BigEndian/LittleEndian)) """
        tx_mode: OnOff = field(XmpInt())
        """TX Mode Off/On"""
        tx_endianness: Endianness = field(XmpInt())
        """TX Endianness Normal/Reverted(BigEndian/LittleEndian)) """

    def get(self) -> Token[GetDataAttr]:
        """Get the Pre-Coding Configurations.

        :return: Pre-Coding configurations including rx_mode, rx_endianness, tx_mode, and tx_endianness.
        :rtype: PP_PRECODING.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))
