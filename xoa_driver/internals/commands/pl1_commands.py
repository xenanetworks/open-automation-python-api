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
    XmpInt,
    XmpSequence,
    XmpStr,
    Hex,
    XmpHex,
)
from .enums import (
    LinkTrainFrameLock,
    LinkTrainCmdResults,
    LinkTrainCmd,
    Layer1ConfigType,
    OnOff,
    FreyaLinkTrainingMode,
    FreyaAutonegMode,
    FreyaTecAbility,
    FreyaFECAbility,
    FreyaPauseAbility,
    AutoNegMode,
    AutoNegStatus,
    FreyaTechAbilityHCDStatus,
    FECMode,
    PauseMode,
    FreyaOutOfSyncPreset,
    TimeoutMode,
    LinkTrainingStatusMode,
    LinkTrainingStatus,
    LinkTrainingFailureType,
    Layer1Control,
    Layer1Opcode,
    FreyaPCSVariant,
    FreyaTecAbilityHCD,
)


@register_command
@dataclass
class PL1_AUTONEGINFO:
    """
    .. versionadded:: 2.0

    .. warning::

        Still in beta mode. Subjected to changes

    Get L1 auto-negotiation information. Information is split into a number of pages.

    """

    code: typing.ClassVar[int] = 385
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _page_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        rx_link_codeword_count: int = field(XmpInt(signed=False))
        """received number of Link Code Words (Base Pages)."""
        rx_next_page_message_count: int = field(XmpInt(signed=False))
        """received number of Next Pages - Message Pages."""
        rx_next_page_unformatted_count: int = field(XmpInt(signed=False))
        """received number of Nex Pages - Unformatted Pages."""
        tx_link_codeword_count: int = field(XmpInt(signed=False))
        """transmitted number of Link Code Words (Base Pages)."""
        tx_next_page_message_count: int = field(XmpInt(signed=False))
        """transmitted number of Next Pages - Message Pages."""
        tx_next_page_unformatted_count: int = field(XmpInt(signed=False))
        """transmitted number of Nex Pages - Unformatted Pages."""
        negotiation_hcd_fail_count: int = field(XmpInt(signed=False))
        """number of negotiation HCD (Highest Common Denominator) failures."""
        negotiation_fec_fail_count: int = field(XmpInt(signed=False))
        """number of negotiation FEC failures."""
        negotiation_loss_of_sync_count: int = field(XmpInt(signed=False))
        """number of negotiation Loss of Sync failures."""
        negotiation_timeout_count: int = field(XmpInt(signed=False))
        """number of negotiation timeouts."""
        negotiation_success_count: int = field(XmpInt(signed=False))
        """number of negotiation successes."""
        duration_us: int = field(XmpInt(signed=False))
        """duration of the auto-negotiation in microseconds, from autoneg is enabled on the port to the negotiation is finished."""

    def get(self) -> Token[GetDataAttr]:
        """Get L1 auto-negotiation information. Information is split into a number of pages.

        :return: L1 auto-negotiation information
        :rtype: PL1_AUTONEGINFO.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._page_xindex]))


@register_command
@dataclass
class PL1_LINKTRAININFO:
    """
    .. versionadded:: 2.0

    .. warning::

        Still in beta mode. Subjected to changes

    Get L1 link training information. Information is per Serdes and split into a number of pages.
    """

    code: typing.ClassVar[int] = 386
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int
    _page_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        duration_us: int = field(XmpInt(signed=False))
        """duration of the auto-negotiation process in microseconds, from autoneg is enabled on the port to the negotiation is finished."""
        lock_lost_count: int = field(XmpInt(signed=False))
        """number of lost locks on auto-neg."""
        pre1_current_level: int = field(XmpInt(signed=False))
        """c(-1) current level."""
        pre1_rx_increment_req_count: int = field(XmpInt(signed=False))
        """c(-1) received number of increment requests."""
        pre1_rx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(-1) received number of decrement requests."""
        pre1_rx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-1) received number of maximum limits of coefficient and equalization requests reached."""
        pre1_rx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-1) received number of maximum limits of equalization requests reached."""
        pre1_rx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(-1) received number of coefficients not supported."""
        pre1_rx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(-1) received number of coefficients at limit."""
        pre1_tx_increment_req_count: int = field(XmpInt(signed=False))
        """c(-1) transmitted number of increment requests."""
        pre1_tx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(-1) transmitted number of decrement requests."""
        pre1_tx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-1) transmitted number of maximum limits of coefficient and equalization requests reached."""
        pre1_tx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-1) transmitted number of maximum limits of equalization requests reached."""
        pre1_tx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(-1) transmitted number of coefficients not supported."""
        pre1_tx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(-1) transmitted number of coefficients at limit."""
        main_current_level: int = field(XmpInt(signed=False))
        """c(0) current level."""
        main_rx_increment_req_count: int = field(XmpInt(signed=False))
        """c(0) received number of increment requests."""
        main_rx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(0) received number of decrement requests."""
        main_rx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(0) received number of maximum limits of coefficient and equalization requests reached."""
        main_rx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(0) received number of maximum limits of equalization requests reached."""
        main_rx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(0) received number of coefficients not supported."""
        main_rx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(0) received number of coefficients at limit."""
        main_tx_increment_req_count: int = field(XmpInt(signed=False))
        """c(0) transmitted number of increment requests."""
        main_tx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(0) transmitted number of decrement requests."""
        main_tx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(0) transmitted number of maximum limits of coefficient and equalization requests reached."""
        main_tx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(0) transmitted number of maximum limits of equalization requests reached."""
        main_tx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(0) transmitted number of coefficients not supported."""
        main_tx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(0) transmitted number of coefficients at limit."""
        post1_current_level: int = field(XmpInt(signed=False))
        """c(1) current level."""
        post1_rx_increment_req_count: int = field(XmpInt(signed=False))
        """c(1) received number of increment requests."""
        post1_rx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(1) received number of decrement requests."""
        post1_rx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(1) received number of maximum limits of coefficient and equalization requests reached."""
        post1_rx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(1) received number of maximum limits of equalization requests reached."""
        post1_rx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(1) received number of coefficients not supported."""
        post1_rx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(1) received number of coefficients at limit."""
        post1_tx_increment_req_count: int = field(XmpInt(signed=False))
        """c(1) transmitted number of increment requests."""
        post1_tx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(1) transmitted number of decrement requests."""
        post1_tx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(1) transmitted number of maximum limits of coefficient and equalization requests reached."""
        post1_tx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(1) transmitted number of maximum limits of equalization requests reached."""
        post1_tx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(1) transmitted number of coefficients not supported."""
        post1_tx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(1) transmitted number of coefficients at limit."""
        pre2_current_level: int = field(XmpInt(signed=False))
        """c(-2) current level."""
        pre2_rx_increment_req_count: int = field(XmpInt(signed=False))
        """c(-2) received number of increment requests."""
        pre2_rx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(-2) received number of decrement requests."""
        pre2_rx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-2) received number of maximum limits of coefficient and equalization requests reached."""
        pre2_rx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-2) received number of maximum limits of equalization requests reached."""
        pre2_rx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(-2) received number of coefficients not supported."""
        pre2_rx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(-2) received number of coefficients at limit."""
        pre2_tx_increment_req_count: int = field(XmpInt(signed=False))
        """c(-2) transmitted number of increment requests."""
        pre2_tx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(-2) transmitted number of decrement requests."""
        pre2_tx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-2) transmitted number of maximum limits of coefficient and equalization requests reached."""
        pre2_tx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-2) transmitted number of maximum limits of equalization requests reached."""
        pre2_tx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(-2) transmitted number of coefficients not supported."""
        pre2_tx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(-2) transmitted number of coefficients at limit."""
        pre3_current_level: int = field(XmpInt(signed=False))
        """c(-3) current level."""
        pre3_rx_increment_req_count: int = field(XmpInt(signed=False))
        """c(-3) received number of increment requests."""
        pre3_rx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(-3) received number of decrement requests."""
        pre3_rx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-3) received number of maximum limits of coefficient and equalization requests reached."""
        pre3_rx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-3) received number of maximum limits of equalization requests reached."""
        pre3_rx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(-3) received number of coefficients not supported."""
        pre3_rx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(-3) received number of coefficients at limit."""
        pre3_tx_increment_req_count: int = field(XmpInt(signed=False))
        """c(-3) transmitted number of increment requests."""
        pre3_tx_decrement_req_count: int = field(XmpInt(signed=False))
        """c(-3) transmitted number of decrement requests."""
        pre3_tx_coeff_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-3) transmitted number of maximum limits of coefficient and equalization requests reached."""
        pre3_tx_eq_limit_reached_count: int = field(XmpInt(signed=False))
        """c(-3) transmitted number of maximum limits of equalization requests reached."""
        pre3_tx_coeff_not_supported_count: int = field(XmpInt(signed=False))
        """c(-3) transmitted number of coefficients not supported."""
        pre3_tx_coeff_at_limit_count: int = field(XmpInt(signed=False))
        """c(-3) transmitted number of coefficients at limit."""
        prbs_total_bits_high: int = field(XmpInt(signed=False))
        """PRBS total bits (most significant 32-bit)."""
        prbs_total_bits_low: int = field(XmpInt(signed=False))
        """PRBS total bits  (least significant 32-bit)."""
        prbs_total_error_bits_high: int = field(XmpInt(signed=False))
        """PRBS total error bits (most significant 32-bit, only bit 15-0 should be used)."""
        prbs_total_error_bits_low: int = field(XmpInt(signed=False))
        """PRBS total error bits (least significant 32-bit)."""
        frame_lock: LinkTrainFrameLock = field(XmpInt(signed=False))
        """frame lock status of the local end."""
        remote_frame_lock: LinkTrainFrameLock = field(XmpInt(signed=False))
        """frame lock status of the remote end."""
        num_frame_errors: int = field(XmpInt(signed=False))

        num_overruns: int = field(XmpInt(signed=False))

        last_ic_received: int = field(XmpInt(signed=False))

        last_ic_sent: int = field(XmpInt(signed=False))

    def get(self) -> Token[GetDataAttr]:
        """Get L1 link training information. Information is per Serdes and split into a number of pages.

        :return: L1 link training information
        :rtype: PL1_LINKTRAININFO.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._page_xindex]))


@register_command
@dataclass
class PL1_LOG:
    """
    .. versionadded:: 2.0

    .. warning::

        Still in beta mode. Subjected to changes

    Return a log line of either AN or LT for the given Serdes. The log string line contains the latest 100 lines.
    """

    code: typing.ClassVar[int] = 387
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        log_string: str = field(XmpStr())

    def get(self) -> Token[GetDataAttr]:
        """Return a log line of ANLT of all serdes on a port. (latest 100 lines)

        :return: a log line from AN/LT for the given Serdes.
        :rtype: PL1_LOG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class PL1_CFG_TMP:
    """
    .. versionadded:: 1.1

    .. warning::

        Still in beta mode. Subjected to changes

    Configure some L1 parameters.
    """

    code: typing.ClassVar[int] = 388
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int
    _type: Layer1ConfigType

    class GetDataAttr(ResponseBodyStruct):
        """Data structure of the get response.
        """
        values: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))

    class SetDataAttr(RequestBodyStruct):
        """Data structure of the set action.
        """
        values: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))

    def get(self) -> "Token[GetDataAttr]":
        """Get various L1 parameters

        :return: various L1 parameters
        :rtype: PL1_CFG_TMP.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._type]))

    def set(self, values: typing.List[int]) -> "Token":
        """Get various L1 parameters

        :param values: L1 parameters
        :type values: typing.List[int]
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._type], values=values))
    
@register_command
@dataclass
class PL1_LINKTRAIN_CMD:
    """
    .. versionadded:: 1.1

    .. warning::

        Still in beta mode. Subjected to changes

    Link training RPC. Issue link training commands on a given serdes and poll for status
    """

    code: typing.ClassVar[int] = 389
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        cmd: int = field(XmpByte())

        arg: int = field(XmpByte())

        result: LinkTrainCmdResults = field(XmpByte())

        flags: int = field(XmpByte())

    class SetDataAttr(RequestBodyStruct):
        cmd: LinkTrainCmd = field(XmpByte())

        arg: int = field(XmpByte())

    def get(self) -> Token[GetDataAttr]:
        """Get status of current command

        :return: 4 bytes: command, arg, result, flags
        :rtype: PL1_LINKTRAIN_CMD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, cmd: LinkTrainCmd, arg: int) -> Token[None]:
        """Issue a link train command (cmd, arg)

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], cmd=cmd, arg=arg))

@register_command
@dataclass
class PL1_CTRL:
    """
    .. versionadded:: 2.5

    The Signal Integrity feature offers the equivalent of an Equivalent Time oscilloscope trace of the RX PAM4 signal (later, also PAM2). The trace is done with the A/D converter in the GTM receiver also doing the data sampling / CDR function, i.e. the trace is taken after the RX equalizer.

    The HW characteristics of the Versal GTM used in Freya are: Trace length = 2000 samples, sample resolution = 7 bits 2's complement, i.e. range = -64..63.

    Using the sampled eye scan feature through CLI involves two steps:

    Trigger the acquisition of a trace (PL1_CTRL)

    Retrieve the trace data (PL1_GET_DATA)

    This command is a generic control function related to Layer 1 / SERDES. For now, only used for signal integrity scan.
    """

    code: typing.ClassVar[int] = 424
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int
    _func_xindex: Layer1Control

    class SetDataAttr(RequestBodyStruct):
        opcode: Layer1Opcode = field(XmpInt())

    def set(self, opcode: Layer1Opcode) -> Token[None]:

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._func_xindex], opcode=opcode))
    
@register_command
@dataclass
class PL1_GET_DATA:
    """
    .. versionadded:: 2.5

    The Signal Integrity feature offers the equivalent of an Equivalent Time oscilloscope trace of the RX PAM4 signal (later, also PAM2). The trace is done with the A/D converter in the GTM receiver also doing the data sampling / CDR function, i.e. the trace is taken after the RX equalizer.

    The HW characteristics of the Versal GTM used in Freya are: Trace length = 2000 samples, sample resolution = 7 bits 2’s complement, i.e. range = -64..63.

    Using the sampled eye scan feature through CLI involves two steps:

    Trigger the acquisition of a trace (PL1_CTRL)

    Retrieve the trace data (PL1_GET_DATA)

    This command is a generic function to retrieve dynamic data related to Layer 1 / SERDES. For now, only used for signal integrity scan.

    For ``func==0``, sampled eye scan:

    * ``result==0``: No data available.

        "No data available" means that either a scan was never started, an acquisition was started and in progress, or the acquired data has become too old (e.g. older than 500 ms). The acquisition time for a trace is in the very low ms-range. If ``result==0``, ``sweep_no`` and ``age_us`` are dummy (=0), and no additional data are returned.

    * ``result==1``: Data returned. In that case, the rest of the parameters apply:

        ``sweep_no``: per-SERDES trace acquisition counter: 1,2,3… Each trace can be returned multiple times, to different users, within its lifetime. A new trace acquisition is triggered with the PL1_CTRL command.

        ``age_us``: The “age” of the trace data in microseconds, i.e. the time from data acquisition from hardware was completed until the time the command reply data is generated.

        ``value``: The rest of the reply is a set of 16 bit signed 2-complement sample values. With present hardware, the range of each sample is -64..63. In XMP scripting, each sample value is represented as two bytes, msb first.

        With present implementation, 2006 sample values (4012 bytes) are returned.

        The first 6 sample values are so-called “sampled levels”: <p1> <p2> < p3> <m1> <m2> <m3>
    """

    code: typing.ClassVar[int] = 425
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int
    _func_xindex: Layer1Control

    class SetDataAttr(RequestBodyStruct):
        result: int = field(XmpInt())
        """Data availability."""

        sweep_no: int = field(XmpInt())
        """per-SERDES trace acquisition counter."""

        age_us: int = field(XmpInt())
        """the age of the trace data in microseconds, i.e. the time from data acquisition from hardware was completed until the time the command reply data is generated."""

        value: typing.List[int] = field(XmpSequence(types_chunk=[XmpByte()]))
        """a set of 16 bit signed 2-complement sample values. With present hardware, the range of each sample is -64..63. In CLI scripting, each sample value is represented as two bytes, msb first."""

    def set(self, opcode: Layer1Opcode) -> Token[None]:

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._func_xindex], opcode=opcode))
    
@register_command
@dataclass
class PL1_PHYTXEQ_LEVEL:
    """
    .. versionadded:: 2.5
    
    Control and monitor the equalizer settings of the on-board PHY in the transmission direction (towards the transceiver cage).

    .. note::

        PL1_PHYTXEQ, PL1_PHYTXEQ_LEVEL, and PL1_PHYTXEQ_COEFF facilitate the configuration and retrieval of TX tap values, each offering a unique perspective. Modifications made with any of these parameters will result in updates to the read results across all of them.

    """

    code: typing.ClassVar[int] = 430
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        pre3: int = field(XmpInt())
        """integer, pre3 tap value in dB/10, ranges from 0 to 71. Default = 0 (neutral)"""
        pre2: int = field(XmpInt())
        """integer, pre2 tap value in dB/10, ranges from 0 to 71. Default = 0 (neutral)"""
        pre: int = field(XmpInt())
        """integer, pre tap value in dB/10, ranges from 0 to 187. Default = 0 (neutral)"""
        main: int = field(XmpInt())
        """integer, main tap value in mV, ranges from 507 to 998."""
        post: int = field(XmpInt())
        """integer, post tap value in dB/10, ranges from 0 to 187 Default = 0 (neutral)"""
        
    class SetDataAttr(RequestBodyStruct):
        pre3: int = field(XmpInt())
        """integer, pre3 tap value in dB/10, ranges from 0 to 71. Default = 0 (neutral)"""
        pre2: int = field(XmpInt())
        """integer, pre2 tap value in dB/10, ranges from 0 to 71. Default = 0 (neutral)"""
        pre: int = field(XmpInt())
        """integer, pre tap value in dB/10, ranges from 0 to 187. Default = 0 (neutral)"""
        main: int = field(XmpInt())
        """integer, main tap value in mV, ranges from 507 to 998."""
        post: int = field(XmpInt())
        """integer, post tap value in dB/10, ranges from 0 to 187 Default = 0 (neutral)"""

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, pre3:int, pre2: int, pre: int, main: int, post: int) -> Token[None]:

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], pre3=pre3, pre2=pre2, pre=pre, main=main, post=post))
    
@register_command
@dataclass
class PL1_PHYTXEQ_COEFF:
    """
    .. versionadded:: 2.5
    
    Control and monitor the equalizer settings of the on-board PHY in the transmission direction (towards the transceiver cage).

    .. note::

        PL1_PHYTXEQ, PL1_PHYTXEQ_LEVEL, and PL1_PHYTXEQ_COEFF facilitate the configuration and retrieval of TX tap values, each offering a unique perspective. Modifications made with any of these parameters will result in updates to the read results across all of them.

    """

    code: typing.ClassVar[int] = 431
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        pre3: int = field(XmpInt())
        """integer, pre3 tap value, negative, scaled by 1E3. Default = 0 (neutral)"""
        pre2: int = field(XmpInt())
        """integer, pre2 tap value, positive, scaled by 1E3. Default = 0 (neutral)"""
        pre: int = field(XmpInt())
        """integer, pre tap value, negative, scaled by 1E3. Default = 0 (neutral)"""
        main: int = field(XmpInt())
        """integer, main tap value, positive, scaled by 1E3. Default = 1000"""
        post: int = field(XmpInt())
        """integer, post tap value, negative, scaled by 1E3. Default = 0 (neutral)"""
        
    class SetDataAttr(RequestBodyStruct):
        pre3: int = field(XmpInt())
        """integer, pre3 tap value, negative, scaled by 1E3. Default = 0 (neutral)"""
        pre2: int = field(XmpInt())
        """integer, pre2 tap value, positive, scaled by 1E3. Default = 0 (neutral)"""
        pre: int = field(XmpInt())
        """integer, pre tap value, negative, scaled by 1E3. Default = 0 (neutral)"""
        main: int = field(XmpInt())
        """integer, main tap value, positive, scaled by 1E3. Default = 1000"""
        post: int = field(XmpInt())
        """integer, post tap value, negative, scaled by 1E3. Default = 0 (neutral)"""

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, pre3:int, pre2: int, pre: int, main: int, post: int) -> Token[None]:

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], pre3=pre3, pre2=pre2, pre=pre, main=main, post=post))    

@register_command
@dataclass
class PL1_AUTONEG_STATUS:
    """
    .. versionadded:: 2.5

    Returns received technology abilities, FEC abilities, pause abilities, HCD technology ability, FEC mode result, and pause mode result.
    """

    code: typing.ClassVar[int] = 432
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        mode: AutoNegMode = field(XmpInt())
        autoneg_state: AutoNegStatus = field(XmpInt())
        received_tech_abilities: Hex = field(XmpHex(size=8))
        received_fec_abilities: Hex = field(XmpHex(size=1))
        received_pause_mode: Hex = field(XmpHex(size=1))
        tech_ability_hcd_status: FreyaTechAbilityHCDStatus = field(XmpInt())
        tech_ability_hcd_value: FreyaTecAbilityHCD = field(XmpInt())
        fec_mode_result: FECMode = field(XmpInt())
        pause_mode_result: PauseMode = field(XmpInt())

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

@register_command
@dataclass
class PL1_AUTONEG_ABILITIES:
    """
    .. versionadded:: 2.5

    Return the supported technology abilities, FEC abilities, and pause abilities of the port.
    """

    code: typing.ClassVar[int] = 433
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        tech_abilities_supported: Hex = field(XmpHex(size=8))
        """supported technology abilities by the port. This returns a value in Hex of the format 0xHHHHHHHH (64 bits). Each bit corresponds to technology ability as shown below. A bit of 1 means the corresponding technology ability is supported by the port."""

        fec_modes_supported: Hex = field(XmpHex(size=1))
        """supported FEC modes by the port. This returns a value in Hex of the format 0xH (8 bits). Each bit corresponds to FEC mode as shown below. A bit of 1 means the corresponding FEC mode is supported by the port."""

        pause_modes_supported: Hex = field(XmpHex(size=1))
        """pause abilities supported by the port. This returns a value in Hex of the format 0xH (8 bits). Each bit corresponds to pause mode as shown below. A bit of 1 means the corresponding FEC mode is supported by the port."""

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
@register_command
@dataclass
class PL1_PCS_VARIANT:
    """
    .. versionadded:: 2.5

    PCS variant configuration.
    """

    code: typing.ClassVar[int] = 434
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        variant: FreyaPCSVariant = field(XmpByte())

    class SetDataAttr(RequestBodyStruct):
        variant: FreyaPCSVariant = field(XmpByte())

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, variant: FreyaPCSVariant) -> Token[None]:

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, variant=variant))


@register_command
@dataclass
class PL1_AUTONEG_CONFIG:
    """
    .. versionadded:: 2.5

    Auto-negotiation configuration for Freya
    """

    code: typing.ClassVar[int] = 440
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        advertised_tech_abilities: Hex = field(XmpHex(size=8))
        advertised_fec_abilities: Hex = field(XmpHex(size=1))
        advertised_pause_mode: Hex = field(XmpHex(size=1))

    class SetDataAttr(RequestBodyStruct):
        advertised_tech_abilities: Hex = field(XmpHex(size=8))
        advertised_fec_abilities: Hex = field(XmpHex(size=1))
        advertised_pause_mode: Hex = field(XmpHex(size=1))

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, advertised_tech_abilities: Hex, advertised_fec_abilities: Hex, advertised_pause_mode: Hex) -> Token[None]:

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, advertised_tech_abilities=advertised_tech_abilities, advertised_fec_abilities=advertised_fec_abilities, advertised_pause_mode=advertised_pause_mode))
    
@register_command
@dataclass
class PL1_ANLT:
    """
    .. versionadded:: 2.5

    ANLT action
    """

    code: typing.ClassVar[int] = 441
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        an_mode: FreyaAutonegMode = field(XmpByte())

        lt_mode: FreyaLinkTrainingMode = field(XmpByte())

    class SetDataAttr(RequestBodyStruct):
        an_mode: FreyaAutonegMode = field(XmpByte())

        lt_mode: FreyaLinkTrainingMode = field(XmpByte())

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, an_mode: FreyaAutonegMode, lt_mode: FreyaLinkTrainingMode) -> Token[None]:

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, an_mode=an_mode, lt_mode=lt_mode))

@register_command
@dataclass
class PL1_PHYTXEQ:
    """
    .. versionadded:: 2.5
    
    Control and monitor the equalizer settings of the on-board PHY in the transmission direction (towards the transceiver cage).

    .. note::

        PL1_PHYTXEQ, PL1_PHYTXEQ_LEVEL, and PL1_PHYTXEQ_COEFF facilitate the configuration and retrieval of TX tap values, each offering a unique perspective. Modifications made with any of these parameters will result in updates to the read results across all of them.

    """

    code: typing.ClassVar[int] = 442
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        pre3: int = field(XmpInt())
        """integer, pre3 tap value. Default = 0 (neutral)"""
        pre2: int = field(XmpInt())
        """integer, pre2 tap value. Default = 0 (neutral)"""
        pre: int = field(XmpInt())
        """integer, pre tap value. Default = 0 (neutral)"""
        main: int = field(XmpInt())
        """integer, main tap value."""
        post: int = field(XmpInt())
        """integer, post tap value. Default = 0 (neutral)"""
        
    class SetDataAttr(RequestBodyStruct):
        pre3: int = field(XmpInt())
        """integer, pre3 tap value. Default = 0 (neutral)"""
        pre2: int = field(XmpInt())
        """integer, pre2 tap value. Default = 0 (neutral)"""
        pre: int = field(XmpInt())
        """integer, pre tap value. Default = 0 (neutral)"""
        main: int = field(XmpInt())
        """integer, main tap value."""
        post: int = field(XmpInt())
        """integer, post tap value. Default = 0 (neutral)"""

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, pre3:int, pre2: int, pre: int, main: int, post: int) -> Token[None]:

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], pre3=pre3, pre2=pre2, pre=pre, main=main, post=post))

@register_command
@dataclass
class PL1_LINKTRAIN_CONFIG:
    """
    .. versionadded:: 2.5

    Per-port link training settings
    """

    code: typing.ClassVar[int] = 443
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        oos_preset: FreyaOutOfSyncPreset = field(XmpByte())
        timeout_mode: TimeoutMode = field(XmpByte())

    class SetDataAttr(RequestBodyStruct):
        oos_preset: FreyaOutOfSyncPreset = field(XmpByte())
        timeout_mode: TimeoutMode = field(XmpByte())

    def get(self) -> Token[GetDataAttr]:

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, oos_preset: FreyaOutOfSyncPreset, timeout_mode: TimeoutMode) -> Token[None]:

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, oos_preset=oos_preset, timeout_mode=timeout_mode))
    
@register_command
@dataclass
class PL1_LINKTRAIN_STATUS:
    """
    Per-lane link training status
    """

    code: typing.ClassVar[int] = 444
    pushed: typing.ClassVar[bool] = False

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