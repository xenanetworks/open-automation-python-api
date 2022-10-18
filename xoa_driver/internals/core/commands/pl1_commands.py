#: L23 Port Layer-1 Commands

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
class PL1_AUTONEGINFO:
    """
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

        rx_link_codeword_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # received number of Link Code Words (Base Pages).

        rx_next_page_message_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # received number of Next Pages - Message Pages.

        rx_next_page_unformatted_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # received number of Nex Pages - Unformatted Pages.

        tx_link_codeword_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # transmitted number of Link Code Words (Base Pages).

        tx_next_page_message_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #transmitted number of Next Pages - Message Pages.

        tx_next_page_unformatted_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # transmitted number of Nex Pages - Unformatted Pages.

        negotiation_hcd_fail_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # number of negotiation HCD (Highest Common Denominator) failures.

        negotiation_fec_fail_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # number of negotiation FEC failures.

        negotiation_loss_of_sync_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # number of negotiation Loss of Sync failures.

        negotiation_timeout_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # number of negotiation timeouts.

        negotiation_success_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # number of negotiation successes.

        duration_us: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  # duration of the auto-negotiation in microseconds, from autoneg is enabled on the port to the negotiation is finished.


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
    Get L1 link training information. Information is per Serdes and split into a number of pages.
    """

    code: typing.ClassVar[int] = 386
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _page_xindex: int
    _serdes_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:

        duration_us: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #duration of the auto-negotiation process in microseconds, from autoneg is enabled on the port to the negotiation is finished.

        lock_lost_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #number of lost locks on auto-neg.

        coeff_neg_three_current_level: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) current level.

        coeff_neg_three_rx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) received number of increment requests.

        coeff_neg_three_rx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) received number of decrement requests.

        coeff_neg_three_rx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) received number of maximum limits of coefficient and equalization requests reached.

        coeff_neg_three_rx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) received number of maximum limits of equalization requests reached.

        coeff_neg_three_rx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) received number of coefficients not supported.

        coeff_neg_three_rx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) received number of coefficients at limit.

        coeff_neg_three_tx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) transmitted number of increment requests.

        coeff_neg_three_tx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) transmitted number of decrement requests.

        coeff_neg_three_tx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) transmitted number of maximum limits of coefficient and equalization requests reached.

        coeff_neg_three_tx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) transmitted number of maximum limits of equalization requests reached.

        coeff_neg_three_tx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) transmitted number of coefficients not supported.

        coeff_neg_three_tx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-3) transmitted number of coefficients at limit.

        coeff_neg_two_current_level: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) current level.

        coeff_neg_two_rx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) received number of increment requests.

        coeff_neg_two_rx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) received number of decrement requests.

        coeff_neg_two_rx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) received number of maximum limits of coefficient and equalization requests reached.

        coeff_neg_two_rx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) received number of maximum limits of equalization requests reached.

        coeff_neg_two_rx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) received number of coefficients not supported.

        coeff_neg_two_rx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) received number of coefficients at limit.

        coeff_neg_two_tx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) transmitted number of increment requests.

        coeff_neg_two_tx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) transmitted number of decrement requests.

        coeff_neg_two_tx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) transmitted number of maximum limits of coefficient and equalization requests reached.

        coeff_neg_two_tx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) transmitted number of maximum limits of equalization requests reached.

        coeff_neg_two_tx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) transmitted number of coefficients not supported.

        coeff_neg_two_tx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-2) transmitted number of coefficients at limit.

        coeff_neg_one_current_level: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) current level.

        coeff_neg_one_rx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) received number of increment requests.

        coeff_neg_one_rx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) received number of decrement requests.

        coeff_neg_one_rx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) received number of maximum limits of coefficient and equalization requests reached.

        coeff_neg_one_rx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) received number of maximum limits of equalization requests reached.

        coeff_neg_one_rx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) received number of coefficients not supported.

        coeff_neg_one_rx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) received number of coefficients at limit.

        coeff_neg_one_tx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) transmitted number of increment requests.

        coeff_neg_one_tx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) transmitted number of decrement requests.

        coeff_neg_one_tx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) transmitted number of maximum limits of coefficient and equalization requests reached.

        coeff_neg_one_tx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) transmitted number of maximum limits of equalization requests reached.

        coeff_neg_one_tx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) transmitted number of coefficients not supported.

        coeff_neg_one_tx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(-1) transmitted number of coefficients at limit.

        coeff_zero_current_level: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) current level.

        coeff_zero_rx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) received number of increment requests.

        coeff_zero_rx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) received number of decrement requests.

        coeff_zero_rx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) received number of maximum limits of coefficient and equalization requests reached.

        coeff_zero_rx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) received number of maximum limits of equalization requests reached.

        coeff_zero_rx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) received number of coefficients not supported.

        coeff_zero_rx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) received number of coefficients at limit.

        coeff_zero_tx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) transmitted number of increment requests.

        coeff_zero_tx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) transmitted number of decrement requests.

        coeff_zero_tx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) transmitted number of maximum limits of coefficient and equalization requests reached.

        coeff_zero_tx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) transmitted number of maximum limits of equalization requests reached.

        coeff_zero_tx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) transmitted number of coefficients not supported.

        coeff_zero_tx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(0) transmitted number of coefficients at limit.


        coeff_one_current_level: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) current level.

        coeff_one_rx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) received number of increment requests.

        coeff_one_rx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) received number of decrement requests.

        coeff_one_rx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) received number of maximum limits of coefficient and equalization requests reached.

        coeff_one_rx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) received number of maximum limits of equalization requests reached.

        coeff_one_rx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) received number of coefficients not supported.

        coeff_one_rx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) received number of coefficients at limit.

        coeff_one_tx_increment_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) transmitted number of increment requests.

        coeff_one_tx_decrement_req_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) transmitted number of decrement requests.

        coeff_one_tx_coeff_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) transmitted number of maximum limits of coefficient and equalization requests reached.

        coeff_one_tx_eq_limit_reached_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) transmitted number of maximum limits of equalization requests reached.

        coeff_one_tx_coeff_not_supported_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) transmitted number of coefficients not supported.

        coeff_one_tx_coeff_at_limit_count: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #c(1) transmitted number of coefficients at limit.

        prbs_total_bits_high: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #PRBS total bits (most significant 32-bit).

        prbs_total_bits_low: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #PRBS total bits  (least significant 32-bit).

        prbs_total_error_bits_high: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #PRBS total error bits (most significant 32-bit, only bit 15-0 should be used).

        prbs_total_error_bits_low: XmpField[XmpUnsignedInt] = XmpField(XmpUnsignedInt)  #PRBS total error bits (least significant 32-bit).

        frame_lock: XmpField[XmpByte] = XmpField(XmpByte, choices=L1LinkTrainFrameLock) # whether frame lock is detected.

        remote_frame_lock: XmpField[XmpByte] = XmpField(XmpByte, choices=L1LinkTrainFrameLock) # whether frame lock is detected by the remote side.


    def get(self) -> "Token[GetDataAttr]":
        """Get L1 link training information. Information is per Serdes and split into a number of pages.

        :return: L1 link training information
        :rtype: PL1_LINKTRAININFO.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._serdes_xindex]))


@register_command
@dataclass
class PL1_LOG:
    """
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

        log_string: XmpField[XmpStr] = XmpField(XmpStr)  # return a log line from AN/LT for the given Serdes.

    def get(self) -> "Token[GetDataAttr]":
        """Return a log line of either AN (``<_type> = 0``) or LT (``<_type> = 1``) for the given Serdes. (latest 100 lines)

        :return: a log line from AN/LT for the given Serdes.
        :rtype: PL1_LOG.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex, self._type]))