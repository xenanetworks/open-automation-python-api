# : L23 Port Layer-1 Commands

from dataclasses import dataclass
import typing
import functools

from ..protocol.command_builders import (
    build_get_request,
    build_set_request
)
from .. import interfaces
from ..transporter.token import Token
from ..protocol.fields import data_types as xt
from ..protocol.fields.field import XmpField
from ..registry import register_command
from .enums import *  # noqa: F403


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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _page_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:

        rx_link_codeword_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # received number of Link Code Words (Base Pages).

        rx_next_page_message_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # received number of Next Pages - Message Pages.

        rx_next_page_unformatted_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # received number of Nex Pages - Unformatted Pages.

        tx_link_codeword_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # transmitted number of Link Code Words (Base Pages).

        tx_next_page_message_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # transmitted number of Next Pages - Message Pages.

        tx_next_page_unformatted_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # transmitted number of Nex Pages - Unformatted Pages.

        negotiation_hcd_fail_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # number of negotiation HCD (Highest Common Denominator) failures.

        negotiation_fec_fail_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # number of negotiation FEC failures.

        negotiation_loss_of_sync_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # number of negotiation Loss of Sync failures.

        negotiation_timeout_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # number of negotiation timeouts.

        negotiation_success_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # number of negotiation successes.

        duration_us: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # duration of the auto-negotiation in microseconds, from autoneg is enabled on the port to the negotiation is finished.

    def get(self) -> "Token[GetDataAttr]":
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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int
    _page_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:

        duration_us: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # duration of the auto-negotiation process in microseconds, from autoneg is enabled on the port to the negotiation is finished.

        lock_lost_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # number of lost locks on auto-neg.

        pre1_current_level: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) current level.

        pre1_rx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) received number of increment requests.

        pre1_rx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) received number of decrement requests.

        pre1_rx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) received number of maximum limits of coefficient and equalization requests reached.

        pre1_rx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) received number of maximum limits of equalization requests reached.

        pre1_rx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) received number of coefficients not supported.

        pre1_rx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) received number of coefficients at limit.

        pre1_tx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) transmitted number of increment requests.

        pre1_tx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) transmitted number of decrement requests.

        pre1_tx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) transmitted number of maximum limits of coefficient and equalization requests reached.

        pre1_tx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) transmitted number of maximum limits of equalization requests reached.

        pre1_tx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) transmitted number of coefficients not supported.

        pre1_tx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-1) transmitted number of coefficients at limit.

        main_current_level: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) current level.

        main_rx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) received number of increment requests.

        main_rx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) received number of decrement requests.

        main_rx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) received number of maximum limits of coefficient and equalization requests reached.

        main_rx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) received number of maximum limits of equalization requests reached.

        main_rx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) received number of coefficients not supported.

        main_rx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) received number of coefficients at limit.

        main_tx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) transmitted number of increment requests.

        main_tx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) transmitted number of decrement requests.

        main_tx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) transmitted number of maximum limits of coefficient and equalization requests reached.

        main_tx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) transmitted number of maximum limits of equalization requests reached.

        main_tx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) transmitted number of coefficients not supported.

        main_tx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(0) transmitted number of coefficients at limit.

        post1_current_level: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) current level.

        post1_rx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) received number of increment requests.

        post1_rx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) received number of decrement requests.

        post1_rx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) received number of maximum limits of coefficient and equalization requests reached.

        post1_rx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) received number of maximum limits of equalization requests reached.

        post1_rx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) received number of coefficients not supported.

        post1_rx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) received number of coefficients at limit.

        post1_tx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) transmitted number of increment requests.

        post1_tx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) transmitted number of decrement requests.

        post1_tx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) transmitted number of maximum limits of coefficient and equalization requests reached.

        post1_tx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) transmitted number of maximum limits of equalization requests reached.

        post1_tx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) transmitted number of coefficients not supported.

        post1_tx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(1) transmitted number of coefficients at limit.

        pre2_current_level: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) current level.

        pre2_rx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) received number of increment requests.

        pre2_rx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) received number of decrement requests.

        pre2_rx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) received number of maximum limits of coefficient and equalization requests reached.

        pre2_rx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) received number of maximum limits of equalization requests reached.

        pre2_rx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) received number of coefficients not supported.

        pre2_rx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) received number of coefficients at limit.

        pre2_tx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) transmitted number of increment requests.

        pre2_tx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) transmitted number of decrement requests.

        pre2_tx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) transmitted number of maximum limits of coefficient and equalization requests reached.

        pre2_tx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) transmitted number of maximum limits of equalization requests reached.

        pre2_tx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) transmitted number of coefficients not supported.

        pre2_tx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-2) transmitted number of coefficients at limit.

        pre3_current_level: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) current level.

        pre3_rx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) received number of increment requests.

        pre3_rx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) received number of decrement requests.

        pre3_rx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) received number of maximum limits of coefficient and equalization requests reached.

        pre3_rx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) received number of maximum limits of equalization requests reached.

        pre3_rx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) received number of coefficients not supported.

        pre3_rx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) received number of coefficients at limit.

        pre3_tx_increment_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) transmitted number of increment requests.

        pre3_tx_decrement_req_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) transmitted number of decrement requests.

        pre3_tx_coeff_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) transmitted number of maximum limits of coefficient and equalization requests reached.

        pre3_tx_eq_limit_reached_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) transmitted number of maximum limits of equalization requests reached.

        pre3_tx_coeff_not_supported_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) transmitted number of coefficients not supported.

        pre3_tx_coeff_at_limit_count: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # c(-3) transmitted number of coefficients at limit.

        prbs_total_bits_high: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # PRBS total bits (most significant 32-bit).

        prbs_total_bits_low: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # PRBS total bits  (least significant 32-bit).

        prbs_total_error_bits_high: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # PRBS total error bits (most significant 32-bit, only bit 15-0 should be used).

        prbs_total_error_bits_low: XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # PRBS total error bits (least significant 32-bit).

        frame_lock: XmpField[xt.XmpHex4] = XmpField(xt.XmpHex4, choices=L1LinkTrainFrameLock)  # frame lock status of the local end.

        remote_frame_lock: XmpField[xt.XmpHex4] = XmpField(xt.XmpHex4, choices=L1LinkTrainFrameLock)  # frame lock status of the remote end.

        num_frame_errors:  XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # Number of frame errors received

        num_overruns:  XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # Number of overruns

        num_last_ic_received:  XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # Last preset request receuved

        num_last_ic_sent:  XmpField[xt.XmpUnsignedInt] = XmpField(xt.XmpUnsignedInt)  # Last preset request sent

    def get(self) -> "Token[GetDataAttr]":
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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int
    _type: int

    @dataclass(frozen=True)
    class GetDataAttr:

        log_string: XmpField[xt.XmpStr] = XmpField(xt.XmpStr)
        # TODO: the type of this param returned from xenaserver will be a JSON.
        # Then xoa-driver should parse it into a Python dict.
        # We will need to modify this as soon as the part on xenaserver is ready.

    def get(self) -> "Token[GetDataAttr]":
        """Return a log line of either AN (``<_type> = 0``) or LT (``<_type> = 1``) for the given Serdes. (latest 100 lines)

        :return: a log line from AN/LT for the given Serdes.
        :rtype: PL1_LOG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._type]))


@register_command
@dataclass
class PL1_CFG_TMP:
    """
    .. versionadded:: 2.0

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
    _type: int

    @dataclass(frozen=True)
    class GetDataAttr:
        """Data structure of the get response.
        """
        value: XmpField[xt.XmpIntList] = XmpField(xt.XmpIntList)

    @dataclass(frozen=True)
    class SetDataAttr:
        """Data structure of the set action.
        """
        value: XmpField[xt.XmpIntList] = XmpField(xt.XmpIntList)

    def get(self) -> "Token[GetDataAttr]":
        """Get various L1 parameters

        :return: various L1 parameters
        :rtype: PL1_CFG_TMP.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._type]))

    def set(self, value: int) -> "Token":
        """Get various L1 parameters

        :param value: whether it is on or off
        :type value: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._type], value=value))


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

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        """Data structure of the get response.
        """
        cmd: XmpField[xt.XmpByte] = XmpField(xt.XmpByte)
        arg: XmpField[xt.XmpByte] = XmpField(xt.XmpByte)
        result: XmpField[xt.XmpByte] = XmpField(xt.XmpByte, choices=LinkTrainCmdResults)
        flags: XmpField[xt.XmpByte] = XmpField(xt.XmpByte)

    @dataclass(frozen=True)
    class SetDataAttr:
        """Data structure of the set action.
        """
        cmd: XmpField[xt.XmpByte] = XmpField(xt.XmpByte, choices=LinkTrainCmd)
        arg: XmpField[xt.XmpByte] = XmpField(xt.XmpByte)

    def get(self) -> "Token[GetDataAttr]":
        """Get status of current command

        :return: 4 bytes: command, arg, result, flags
        :rtype: PL1_LINKTRAIN_CMD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))

    def set(self, cmd, arg) -> "Token":
        """Issue a link train command (cmd, arg)

        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex], cmd=cmd, arg=arg))
