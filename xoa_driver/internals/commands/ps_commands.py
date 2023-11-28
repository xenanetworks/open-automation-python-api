from __future__ import annotations
from dataclasses import dataclass
import ipaddress
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
    XmpIPv4Address,
    XmpIPv6Address,
    XmpLong,
    XmpMacAddress,
    XmpSequence,
    XmpStr,
    Hex,
)
from .enums import (
    OnOff,
    OnOffWithSuppress,
    ProtocolOption,
    ModifierAction,
    LengthType,
    PayloadType,
    PFCMode,
    StreamOption,
)


@register_command
@dataclass
class PS_INDICES:
    """
    The full list of which streams are defined for a port. These are the sub-index
    values that are used for the parameters defining the traffic patterns
    transmitted for the port. Setting the value of this command creates a new
    empty stream for each value that is not already in use, and deletes each stream
    that is not mentioned in the list. The same can be accomplished one-stream-at-a-
    time using the :class:`PS_CREATE` and :class:`PS_DELETE` commands.
    """

    code: typing.ClassVar[int] = 150
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        stream_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of streams on the port."""

    class SetDataAttr(RequestBodyStruct):
        stream_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of streams on the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the full list of which streams are defined for a port.

        :return: the sub-indices of streams on the port
        :rtype: PS_INDICES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, stream_indices: typing.List[int]) -> Token[None]:
        """Creates a new empty stream for each value that is not already in use, and deletes each stream that is not mentioned in the list.

        :param stream_indices: the sub-indices of streams on the port
        :type stream_indices: typing.List[int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, stream_indices=stream_indices))


@register_command
@dataclass
class PS_CREATE:
    """
    Creates an empty stream definition with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 151
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Creates an empty stream definition with the specified sub-index value.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_DELETE:
    """
    Deletes the stream definition with the specified sub-index value.
    """

    code: typing.ClassVar[int] = 152
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Deletes the stream definition with the specified sub-index value.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_ENABLE:
    """
    This property determines if a stream contributes outgoing packets for a port.
    The value can be toggled between ON and SUPPRESS while traffic is enabled at the
    port level. Streams in the OFF state cannot be set to any other value while
    traffic is enabled. The sum of the rates of all enabled or suppressed streams
    must not exceed the effective port rate.
    """

    code: typing.ClassVar[int] = 153
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        state: OnOffWithSuppress = field(XmpByte())
        """coded byte, specifying a stream state."""

    class SetDataAttr(RequestBodyStruct):
        state: OnOffWithSuppress = field(XmpByte())
        """coded byte, specifying a stream state."""

    def get(self) -> Token[GetDataAttr]:
        """Get the stream status.

        :return: status of the stream
        :rtype: PS_ENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, state: OnOffWithSuppress) -> Token[None]:
        """Set the stream status. The value can be toggled between ON and SUPPRESS while traffic is enabled at the
        port level. Streams in the OFF state cannot be set to any other value while
        traffic is enabled. The sum of the rates of all enabled or suppressed streams
        must not exceed the effective port rate.

        :param state: a stream state
        :type state: OnOffWithSuppress
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], state=state))

    set_off = functools.partialmethod(set, OnOffWithSuppress.OFF)
    """Set the stream status to OFF.
    """

    set_on = functools.partialmethod(set, OnOffWithSuppress.ON)
    """Set the stream status to ON.
    """

    set_suppress = functools.partialmethod(set, OnOffWithSuppress.SUPPRESS)
    """Set the stream status to SUPPRESS.
    """


@register_command
@dataclass
class PS_PACKETLIMIT:
    """
    Based on different port transmission mode, the meaning of this API is different.
    When Port TX Mode is set to NORMAL, STRICT UNIFORM or BURST: The number of
    packets that will be transmitted when traffic is started on a port. A value of 0
    or -1 makes the stream transmit continuously. When Port TX Mode is set to
    SEQUENTIAL: The number of sequential packets sent before switching to the next
    stream. The minimum value is 1. The port will transmit continuously until the
    user stops the traffic.
    """

    code: typing.ClassVar[int] = 154
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        packet_count: int = field(XmpInt())
        """integer, the number of packets that the port will send. When Port TX Mode is set to NORMAL, STRICT UNIFORM or BURST: 0 or -1 (disable packet limitation).
        When Port TX Mode is set to SEQUENTIAL: 1 or larger (minimum value since the port transmits at least 1 packet per stream per round).
        """

    class SetDataAttr(RequestBodyStruct):
        packet_count: int = field(XmpInt())
        """integer, the number of packets that the port will send. When Port TX Mode is set to NORMAL, STRICT UNIFORM or BURST: 0 or -1 (disable packet limitation).
        When Port TX Mode is set to SEQUENTIAL: 1 or larger (minimum value since the port transmits at least 1 packet per stream per round).
        """

    def get(self) -> Token[GetDataAttr]:
        """If Port TX Mode is NORMAL, STRICT UNIFORM or BURST: get the number of packets that will be transmitted when traffic is started on a port.
        If Port TX Mode is SEQUENTIAL: get the number of sequential packets sent before switching to the next stream.

        :return: the number of packets
        :rtype: PS_PACKETLIMIT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, packet_count: int) -> Token[None]:
        """If Port TX Mode is NORMAL, STRICT UNIFORM or BURST: set the number of packets that will be transmitted when traffic is started on a port,
        0 or -1 (disable packet limitation).
        If Port TX Mode is SEQUENTIAL: set the number of sequential packets sent before switching to the next stream,
        1 or larger (minimum value since the port transmits at least 1 packet per stream per round).

        :param packet_count:  the number of packets
        :type packet_count: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], packet_count=packet_count))


@register_command
@dataclass
class PS_COMMENT:
    """
    The description of a stream.
    """

    code: typing.ClassVar[int] = 155
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        comment: str = field(XmpStr())
        """string, specifying the description of the stream."""

    class SetDataAttr(RequestBodyStruct):
        comment: str = field(XmpStr())
        """string, specifying the description of the stream."""

    def get(self) -> Token[GetDataAttr]:
        """Get the description of a stream.

        :return: the description of the stream
        :rtype: PS_COMMENT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, comment: str) -> Token[None]:
        """Set the description of a stream.

        :param comment: the description of the stream
        :type comment: str
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], comment=comment))


@register_command
@dataclass
class PS_TPLDID:
    """
    The identifier of the test payloads inserted into packets transmitted for a
    stream. A value of -1 disables test payloads for the stream. Test payloads are
    inserted at the end of each packet, and contains time-stamp and sequence-number
    information. This allows the receiving port to provide error-checking and
    latency measurements, in addition to the basic counts and rate measurements
    provided for all traffic. The test payload identifier furthermore allows the
    receiving port to distinguish multiple different streams, which may originate
    from multiple different chassis. Since test payloads are an inter-port and
    inter-chassis mechanism, the test payload identifier assignments should be
    planned globally across all the chassis and ports of the testbed.
    """

    code: typing.ClassVar[int] = 157
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        test_payload_identifier: int = field(XmpInt())
        """integer, the test payload identifier value. -1 = disable test payloads."""

    class SetDataAttr(RequestBodyStruct):
        test_payload_identifier: int = field(XmpInt())
        """integer, the test payload identifier value. -1 = disable test payloads."""

    def get(self) -> Token[GetDataAttr]:
        """Get the identifier of the test payloads inserted into packets transmitted for a stream.

        :return: the test payload identifier value. -1 = disable test payloads.
        :rtype: PS_TPLDID.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, test_payload_identifier: int) -> Token[None]:
        """Set the identifier of the test payloads inserted into packets transmitted for a stream.
        A value of -1 disables test payloads for the stream. Test payloads are
        inserted at the end of each packet, and contains time-stamp and sequence-number
        information.

        :param test_payload_identifier: the test payload identifier value. -1 = disable test payloads
        :type test_payload_identifier: int
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], test_payload_identifier=test_payload_identifier)
        )


@register_command
@dataclass
class PS_INSERTFCS:
    """
    Whether a valid frame checksum is added to the packets of a stream.
    """

    code: typing.ClassVar[int] = 158
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether frame checksums are inserted."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, whether frame checksums are inserted."""

    def get(self) -> Token[GetDataAttr]:
        """Get whether a valid frame checksum is added to the packets of a stream.

        :return: whether frame checksums are inserted
        :rtype: PS_INSERTFCS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set whether a valid frame checksum is added to the packets of a stream.

        :param on_off: whether frame checksums are inserted
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable a valid frame checksum to be added to the packets of a stream.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable a valid frame checksum to be added to the packets of a stream.
    """


@register_command
@dataclass
class PS_AUTOADJUST:
    """
    .. versionadded:: v2.0

    Executing PS_AUTOADJUST will adjust the packet length distribution (:class:`PS_PACKETLENGTH`) of the stream:

        (1) Set the type of packet length distribution (:class:`PS_PACKETLENGTH` ``<length_type>``) to ``FIXED``.

        (2) Set the lower limit on the packet length (:class:`PS_PACKETLENGTH` ``<min_val>``) to exactly fit the specified protocol headers,
        TPLD and FCS (but never set to less than 64).

        (3) Set the payload type of packets transmitted for the stream (:class:`PS_PAYLOAD` ``<payload_type>``) to ``PATTERN``.

        (4) If necessary, also set the maximum number of header content bytes (`P_MAXHEADERLENGTH <p_maxheaderlength_label>` ``<max_header_length>``)
        that can be freely specified for each generated stream of the port to a higher value, if needed to accommodate the header size of the stream
        (implicitly given by the `PS_PACKETHEADER` command).

        (5) If the needed maximum header length (`P_MAXHEADERLENGTH <p_maxheaderlength_label>` ``<max_header_length>``)
        is not possible with the actual number of active streams for the port, the command will fail with :`<BADVALUE>`.
    """

    code: typing.ClassVar[int] = 159
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Adjust the packet length distribution of a stream.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_ARPREQUEST:
    """
    Generates an outgoing ARP request on the test port. The packet header for the
    stream must contain an IP protocol segment, and the destination IP address is
    used in the ARP request. If there is a gateway IP address specified for the port
    and it is on a different subnet than the destination IP address in the packet
    header, then the gateway IP address is used instead. The framing of the ARP
    request matches the packet header, including any VLAN protocol segments. This
    command does not generate an immediate result, but waits until an ARP
    reply is received on the test port. If no reply is received within 500
    milliseconds, it returns.
    """

    code: typing.ClassVar[int] = 161
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        mac_address: Hex = field(XmpMacAddress())
        """six hex bytes, specifying the six bytes of the MAC address."""

    def get(self) -> Token[GetDataAttr]:
        """Generates an outgoing ARP request on the test port. The packet header for the
        stream must contain an IP protocol segment, and the destination IP address is
        used in the ARP request. If there is a gateway IP address specified for the port
        and it is on a different subnet than the destination IP address in the packet
        header, then the gateway IP address is used instead. The framing of the ARP
        request matches the packet header, including any VLAN protocol segments. This
        command does not generate an immediate result, but waits until an ARP
        reply is received on the test port. If no reply is received within 500
        milliseconds, it returns.

        :return: the MAC address of the peer port
        :rtype: PS_ARPREQUEST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_PINGREQUEST:
    """
    Generates an outgoing ping request using the ICMP protocol on the test port. The
    packet header for the stream must contain an IP protocol segment, with valid
    source and destination IP addresses. The framing of the ping request matches the
    packet header, including any VLAN protocol segments, and the destination MAC
    address must also be valid, possibly containing a value obtained with
    PS_ARPREQUEST. This command does not generate an immediate result, but
    waits until a ping reply is received on the test port.
    """

    code: typing.ClassVar[int] = 162
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        delay: int = field(XmpInt())
        """integer, the number of milliseconds for the ping reply to arrive."""
        time_to_live: int = field(XmpByte())
        """byte, the time-to-live value in the ping reply packet."""

    def get(self) -> Token[GetDataAttr]:
        """Generates an outgoing ping request using the ICMP protocol on the test port. The
        packet header for the stream must contain an IP protocol segment, with valid
        source and destination IP addresses. The framing of the ping request matches the
        packet header, including any VLAN protocol segments, and the destination MAC
        address must also be valid, possibly containing a value obtained with
        PS_ARPREQUEST. This command does not generate an immediate result, but
        waits until a ping reply is received on the test port.

        :return: the number of milliseconds for the ping reply to arrive, and the time-to-live value in the ping reply packet.
        :rtype: PS_PINGREQUEST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_MODIFIEREXTRANGE:
    """
    Range specification for an extended packet modifier for a stream header,
    specifying which values the modifier should take on. This applies only to
    incrementing and decrementing modifiers; random modifiers always produce every
    possible bit pattern. The range is specified as a three values: mix, step, and
    max, where max must be equal to min plus a multiple of step. Note that when
    "decrement" is specified in PS_MODIFIEREXT as the action, the value sequence
    will begin with the max value instead of the min value and decrement from there:
    {max, max-1, max-2, ...., min, max, max-1...}.
    """

    code: typing.ClassVar[int] = 167
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int
    _modifier_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        min_val: int = field(XmpInt())
        """integer, the minimum modifier value."""
        step: int = field(XmpInt())
        """integer, the increment between modifier values."""
        max_val: int = field(XmpInt())
        """integer, the maximum modifier value."""

    class SetDataAttr(RequestBodyStruct):
        min_val: int = field(XmpInt())
        """integer, the minimum modifier value."""
        step: int = field(XmpInt())
        """integer, the increment between modifier values."""
        max_val: int = field(XmpInt())
        """integer, the maximum modifier value."""

    def get(self) -> Token[GetDataAttr]:
        """Get the range specification for an extended packet modifier for a stream header,
        specifying which values the modifier should take on.

        :return: the minimum modifier value, the increment between modifier values, the maximum modifier value.
        :rtype: PS_MODIFIEREXTRANGE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex, self._modifier_xindex]))

    def set(self, min_val: int, step: int, max_val: int) -> Token[None]:
        """Set the range specification for an extended packet modifier for a stream header,
        specifying which values the modifier should take on. This applies only to
        incrementing and decrementing modifiers; random modifiers always produce every
        possible bit pattern. The range is specified as a three values: mix, step, and
        max, where max must be equal to min plus a multiple of step. Note that when
        "decrement" is specified in PS_MODIFIEREXT as the action, the value sequence
        will begin with the max value instead of the min value and decrement from there:
        {max, max-1, max-2, ...., min, max, max-1...}.

        :param min_val: the minimum modifier value
        :type min_val: int
        :param step: the increment between modifier values
        :type step: int
        :param max_val: the maximum modifier value
        :type max_val: int
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex, self._modifier_xindex], min_val=min_val, step=step, max_val=max_val)
        )


@register_command
@dataclass
class PS_MODIFIERRANGE:
    """
    Range specification for a packet modifier for a stream header, specifying which
    values the modifier should take on. This applies only to incrementing and
    decrementing modifiers; random modifiers always produce every possible bit
    pattern. The range is specified as three values: mix, step, and max, where max
    must be equal to min plus a multiple of step. Note that when "decrement" is
    specified in PS_MODIFIER as the action, the value sequence will begin with the
    max value instead of the min value and decrement from there: {max, max-1, max-2,
    ...., min, max, max-1...}.
    """

    code: typing.ClassVar[int] = 168
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int
    _modifier_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        min_val: int = field(XmpInt())
        """integer, the minimum modifier value."""
        step: int = field(XmpInt())
        """integer, the increment between modifier values."""
        max_val: int = field(XmpInt())
        """integer, the maximum modifier value."""

    class SetDataAttr(RequestBodyStruct):
        min_val: int = field(XmpInt())
        """integer, the minimum modifier value."""
        step: int = field(XmpInt())
        """integer, the increment between modifier values."""
        max_val: int = field(XmpInt())
        """integer, the maximum modifier value."""

    def get(self) -> Token[GetDataAttr]:
        """Get the range specification for a packet modifier for a stream header, specifying which values the modifier should take on.

        :return: the minimum modifier value, the increment between modifier values, the maximum modifier value.
        :rtype: PS_MODIFIERRANGE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex, self._modifier_xindex]))

    def set(self, min_val: int, step: int, max_val: int) -> Token[None]:
        """Set the range specification for a packet modifier for a stream header, specifying which
        values the modifier should take on. This applies only to incrementing and
        decrementing modifiers; random modifiers always produce every possible bit
        pattern. The range is specified as three values: mix, step, and max, where max
        must be equal to min plus a multiple of step. Note that when "decrement" is
        specified in PS_MODIFIER as the action, the value sequence will begin with the
        max value instead of the min value and decrement from there: {max, max-1, max-2,
        ...., min, max, max-1...}.

        :param min_val: the minimum modifier value
        :type min_val: int
        :param step: the increment between modifier values
        :type step: int
        :param max_val: the maximum modifier value
        :type max_val: int
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex, self._modifier_xindex], min_val=min_val, step=step, max_val=max_val)
        )


@register_command
@dataclass
class PS_RATEFRACTION:
    """
    The rate of the traffic transmitted for a stream expressed in millionths of the
    effective rate for the port. The bandwidth consumption includes the inter-frame
    gap and is independent of the length of the packets generated for the stream.
    The sum of the bandwidth consumption for all the enabled streams must not exceed
    the effective rate for the port. Setting this command also instructs the
    Manager to attempt to keep the rate-percentage unchanged in case it has to cap
    stream rates. Get value is only valid if the rate was last set using this
    command.
    """

    code: typing.ClassVar[int] = 169
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        stream_rate_ppm: int = field(XmpInt())
        """integer, stream rate expressed as a ppm value between 0 and 1,000,000."""

    class SetDataAttr(RequestBodyStruct):
        stream_rate_ppm: int = field(XmpInt())
        """integer, stream rate expressed as a ppm value between 0 and 1,000,000."""

    def get(self) -> Token[GetDataAttr]:
        """Get the rate of the traffic transmitted for a stream expressed in millionths of the
        effective rate for the port. Get value is only valid if the rate was last set using this
        command.

        :return: stream rate expressed as a ppm value between 0 and 1,000,000
        :rtype: PS_RATEFRACTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, stream_rate_ppm: int) -> Token[None]:
        """Set the rate of the traffic transmitted for a stream expressed in millionths of the
        effective rate for the port. The bandwidth consumption includes the inter-frame
        gap and is independent of the length of the packets generated for the stream.
        The sum of the bandwidth consumption for all the enabled streams must not exceed
        the effective rate for the port. Setting this command also instructs the
        Manager to attempt to keep the rate-percentage unchanged in case it has to cap
        stream rates.

        :param stream_rate_ppm: stream rate expressed as a ppm value between 0 and 1,000,000.
        :type stream_rate_ppm: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], stream_rate_ppm=stream_rate_ppm))


@register_command
@dataclass
class PS_RATEPPS:
    """
    The rate of the traffic transmitted for a stream expressed in packets per
    second. The bandwidth consumption is heavily dependent on the length of the
    packets generated for the stream, and also on the inter-frame gap for the port.
    The sum of the bandwidth consumption for all the enabled streams must not exceed
    the effective rate for the port. Setting this command also instructs the
    Manager to attempt to keep the packets-per-second unchanged in case it has to
    cap stream rates. Get value is only valid if the rate was the last set using
    this command.
    """

    code: typing.ClassVar[int] = 170
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        stream_rate_pps: int = field(XmpInt())
        """integer, stream rate expressed in packets per second."""

    class SetDataAttr(RequestBodyStruct):
        stream_rate_pps: int = field(XmpInt())
        """integer, stream rate expressed in packets per second."""

    def get(self) -> Token[GetDataAttr]:
        """Get The rate of the traffic transmitted for a stream expressed in packets per
        second. Get value is only valid if the rate was the last set using
        this command.

        :return: stream rate expressed in packets per second
        :rtype: PS_RATEPPS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, stream_rate_pps: int) -> Token[None]:
        """Set The rate of the traffic transmitted for a stream expressed in packets per
        second. The bandwidth consumption is heavily dependent on the length of the
        packets generated for the stream, and also on the inter-frame gap for the port.
        The sum of the bandwidth consumption for all the enabled streams must not exceed
        the effective rate for the port. Setting this command also instructs the
        Manager to attempt to keep the packets-per-second unchanged in case it has to
        cap stream rates.

        :param stream_rate_pps: stream rate expressed in packets per second
        :type stream_rate_pps: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], stream_rate_pps=stream_rate_pps))


@register_command
@dataclass
class PS_RATEL2BPS:
    """
    The rate of the traffic transmitted for a stream, expressed in units of bits-
    per-second at layer-2, thus including the Ethernet header but excluding the
    inter-frame gap. The bandwidth consumption is somewhat dependent on the length
    of the packets generated for the stream, and also on the inter-frame gap for the
    port. The sum of the bandwidth consumption for all the enabled streams must not
    exceed the effective rate for the port. Setting this command also instructs
    the Manager to attempt to keep the layer-2 bps rate unchanged in case it has to
    cap stream rates. Get value is only valid if the rate was the last set using
    this command.
    """

    code: typing.ClassVar[int] = 171
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        l2_bps: int = field(XmpLong())
        """long integer, stream rate expressed in bits per second."""

    class SetDataAttr(RequestBodyStruct):
        l2_bps: int = field(XmpLong())
        """long integer, stream rate expressed in bits per second."""

    def get(self) -> Token[GetDataAttr]:
        """Get the rate of the traffic transmitted for a stream, expressed in units of bits-
        per-second at layer-2, thus including the Ethernet header but excluding the
        inter-frame gap. Get value is only valid if the rate was the last set using
        this command.

        :return: stream rate expressed in bits per second
        :rtype: PS_RATEL2BPS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, l2_bps: int) -> Token[None]:
        """Set the rate of the traffic transmitted for a stream, expressed in units of bits-
        per-second at layer-2, thus including the Ethernet header but excluding the
        inter-frame gap. The bandwidth consumption is somewhat dependent on the length
        of the packets generated for the stream, and also on the inter-frame gap for the
        port. The sum of the bandwidth consumption for all the enabled streams must not
        exceed the effective rate for the port. Setting this command also instructs
        the Manager to attempt to keep the layer-2 bps rate unchanged in case it has to
        cap stream rates.

        :param l2_bps: stream rate expressed in bits per second
        :type l2_bps: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], l2_bps=l2_bps))


@register_command
@dataclass
class PS_BURST:
    """
    The burstiness of the traffic transmitted for a stream, expressed in terms of
    the number of packets in each burst, and how densely they are packed together.
    The burstiness does not affect the bandwidth consumed by the stream, only the
    spacing between the packets. A density value of 100 means that the packets are
    packed tightly together, only spaced by the minimum inter-frame gap. A value of
    0 means even, non-bursty, spacing. The exact spacing achieved depends on the
    other enabled streams of the port.
    """

    code: typing.ClassVar[int] = 174
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        size: int = field(XmpInt())
        """integer, the number of packets lumped together in a burst."""
        density: int = field(XmpInt())
        """integer, the percentage of the available spacing that is inserted between bursts."""

    class SetDataAttr(RequestBodyStruct):
        size: int = field(XmpInt())
        """integer, the number of packets lumped together in a burst."""
        density: int = field(XmpInt())
        """integer, the percentage of the available spacing that is inserted between bursts."""

    def get(self) -> Token[GetDataAttr]:
        """Get the burstiness of the traffic transmitted for a stream, expressed in terms of
        the number of packets in each burst, and how densely they are packed together.

        :return: the number of packets lumped together in a burst, and the percentage of the available spacing that is inserted between bursts
        :rtype: ~PS_BURST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, size: int, density: int) -> Token[None]:
        """Set the burstiness of the traffic transmitted for a stream, expressed in terms of
        the number of packets in each burst, and how densely they are packed together.
        The burstiness does not affect the bandwidth consumed by the stream, only the
        spacing between the packets. A density value of 100 means that the packets are
        packed tightly together, only spaced by the minimum inter-frame gap. A value of
        0 means even, non-bursty, spacing. The exact spacing achieved depends on the
        other enabled streams of the port.

        :param size: the number of packets lumped together in a burst
        :type size: int
        :param density: the percentage of the available spacing that is inserted between bursts
        :type density: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], size=size, density=density))


@register_command
@dataclass
class PS_PACKETHEADER:
    """
    The first portion of the packet bytes that are transmitted for a stream. This
    starts with the 14 bytes of the Ethernet header, followed by any contained
    protocol segments. All packets transmitted for the stream start with this fixed
    header. Individual byte positions of the packet header may be varied on a
    packet-to-packet basis using modifiers. The full packet comprises the header,
    the payload, an optional test payload, and the frame checksum. The header data
    is specified as raw bytes, since the script environment does not know the field-
    by-field layout of the various protocol segments.
    """

    code: typing.ClassVar[int] = 175
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, the raw bytes comprising the packet header."""

    class SetDataAttr(RequestBodyStruct):
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, the raw bytes comprising the packet header."""

    def get(self) -> Token[GetDataAttr]:
        """Get the packet header of a stream. This
        starts with the 14 bytes of the Ethernet header, followed by any contained
        protocol segments. All packets transmitted for the stream start with this fixed
        header. Individual byte positions of the packet header may be varied on a
        packet-to-packet basis using modifiers. The full packet comprises the header,
        the payload, an optional test payload, and the frame checksum. The header data
        is specified as raw bytes, since the script environment does not know the field-
        by-field layout of the various protocol segments.

        :return: the raw bytes comprising the packet header
        :rtype: PS_PACKETHEADER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, hex_data: Hex) -> Token[None]:
        """Set the packet header of a stream. This
        starts with the 14 bytes of the Ethernet header, followed by any contained
        protocol segments. All packets transmitted for the stream start with this fixed
        header. Individual byte positions of the packet header may be varied on a
        packet-to-packet basis using modifiers. The full packet comprises the header,
        the payload, an optional test payload, and the frame checksum. The header data
        is specified as raw bytes, since the script environment does not know the field-
        by-field layout of the various protocol segments.

        :param hex_data: the raw bytes comprising the packet header
        :type hex_data: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], hex_data=hex_data))


@register_command
@dataclass
class PS_HEADERPROTOCOL:
    """
    This command will inform the Xena tester how to interpret the packet header
    byte sequence specified with PS_PACKETHEADER.  This is mainly for information
    purposes, and the stream will transmit the packet header bytes even if no
    protocol segments are specified.  The Xena tester however support calculation of
    certain field values in hardware, such as the IP, TCP and UDP length and
    checksum fields.  This allow the use of hardware modifiers for these protocol
    segments.  In order for this function to work the Xena tester needs to know the
    type of each segment that precedes the segment where the hardware calculation is
    to be performed.
    """

    code: typing.ClassVar[int] = 176
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        segments: typing.List[ProtocolOption] = field(XmpSequence(types_chunk=[XmpByte()]))
        """list of coded bytes, a number specifying a built-in protocol segment."""

    class SetDataAttr(RequestBodyStruct):
        segments: typing.List[ProtocolOption] = field(XmpSequence(types_chunk=[XmpByte()]))
        """list of coded bytes, a number specifying a built-in protocol segment."""

    def get(self) -> Token[GetDataAttr]:
        """Get the packet header segments in protocol names.

        :return: a number specifying a built-in protocol segment
        :rtype: PS_HEADERPROTOCOL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, segments: typing.List[ProtocolOption]) -> Token[None]:
        """Inform the Xena tester how to interpret the packet header
        byte sequence specified with PS_PACKETHEADER.  This is mainly for information
        purposes, and the stream will transmit the packet header bytes even if no
        protocol segments are specified.  The Xena tester however support calculation of
        certain field values in hardware, such as the IP, TCP and UDP length and
        checksum fields. This allow the use of hardware modifiers for these protocol
        segments. In order for this function to work the Xena tester needs to know the
        type of each segment that precedes the segment where the hardware calculation is
        to be performed.

        :param segments: a number specifying a built-in protocol segment
        :type segments: typing.List[ProtocolOption]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], segments=segments))


@register_command
@dataclass
class PS_MODIFIERCOUNT:
    """
    The number of standard 16-bit modifiers active on the packet header of a stream.
    Each modifier is specified using PS_MODIFIER.
    """

    code: typing.ClassVar[int] = 177
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        modifier_count: int = field(XmpInt())
        """integer, the number of modifiers for the stream."""

    class SetDataAttr(RequestBodyStruct):
        modifier_count: int = field(XmpInt())
        """integer, the number of modifiers for the stream."""

    def get(self) -> Token[GetDataAttr]:
        """Get the number of standard 16-bit modifiers active on the packet header of a stream.
        Each modifier is specified using PS_MODIFIER.

        :return: the number of modifiers for the stream
        :rtype: PS_MODIFIERCOUNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, modifier_count: int) -> Token[None]:
        """Set the number of standard 16-bit modifiers active on the packet header of a stream.
        Each modifier is specified using PS_MODIFIER.

        :param modifier_count: the number of modifiers for the stream
        :type modifier_count: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], modifier_count=modifier_count))


@register_command
@dataclass
class PS_MODIFIER:
    """
    A packet modifier for a stream header. The headers of each packet transmitted
    for the stream will be varied according to the modifier specification. This
    command requires two sub-indices, one for the stream and one for the modifier.
    A modifier is positioned at a fixed place in the header, selects a number of
    consecutive bits starting from that position, and applies an action to those
    bits in each packet. Packets can be repeated so that a certain number of
    identical packets are transmitted before applying the next modification.
    """

    code: typing.ClassVar[int] = 178
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int
    _modifier_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        position: int = field(XmpInt())
        """integer, the byte position from the start of the packet."""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, the mask specifying which bits to affect."""
        action: ModifierAction = field(XmpInt())
        """coded integer, which action to perform on the affected bits."""
        repetition: int = field(XmpInt())
        """integer, how many times to repeat on each packet."""

    class SetDataAttr(RequestBodyStruct):
        position: int = field(XmpInt())
        """integer, the byte position from the start of the packet."""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, the mask specifying which bits to affect."""
        action: ModifierAction = field(XmpInt())
        """coded integer, which action to perform on the affected bits."""
        repetition: int = field(XmpInt())
        """integer, how many times to repeat on each packet."""

    def get(self) -> Token[GetDataAttr]:
        """Get a packet modifier for a stream header. The headers of each packet transmitted
        for the stream will be varied according to the modifier specification. This
        command requires two sub-indices, one for the stream and one for the modifier.
        A modifier is positioned at a fixed place in the header, selects a number of
        consecutive bits starting from that position, and applies an action to those
        bits in each packet. Packets can be repeated so that a certain number of
        identical packets are transmitted before applying the next modification.

        :return: the byte position from the start of the packet, the mask specifying which bits to affect, which action to perform on the affected bits,
            and how many times to repeat on each packet
        :rtype: PS_MODIFIER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex, self._modifier_xindex]))

    def set(self, position: int, mask: Hex, action: ModifierAction, repetition: int) -> Token[None]:
        """Set a packet modifier for a stream header. The headers of each packet transmitted
        for the stream will be varied according to the modifier specification. This
        command requires two sub-indices, one for the stream and one for the modifier.
        A modifier is positioned at a fixed place in the header, selects a number of
        consecutive bits starting from that position, and applies an action to those
        bits in each packet. Packets can be repeated so that a certain number of
        identical packets are transmitted before applying the next modification.

        :param position: the byte position from the start of the packet
        :type position: int
        :param mask: the mask specifying which bits to affect
        :type mask: str
        :param action: which action to perform on the affected bits
        :type action: ModifierAction
        :param repetition: how many times to repeat on each packet
        :type repetition: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._stream_xindex, self._modifier_xindex],
                position=position,
                mask=mask,
                action=action,
                repetition=repetition
            )
        )

    set_inc = functools.partialmethod(set, action=ModifierAction.INC)
    """Set a packet modifier action to incrementing.
    """

    set_dec = functools.partialmethod(set, action=ModifierAction.DEC)
    """Set a packet modifier action to decrementing.
    """

    set_random = functools.partialmethod(set, action=ModifierAction.RANDOM)
    """Set a packet modifier action to random.
    """


@register_command
@dataclass
class PS_PACKETLENGTH:
    """
    The length distribution of the packets transmitted for a stream. The length of
    the packets transmitted for a stream can be varied from packet to packet,
    according to a choice of distributions within a specified min...max range. The
    length of each packet is reflected in the size of the payload portion of the
    packet, whereas the header has constant length. Length variation complements,
    and is independent of, the content variation produced by header modifiers.
    """

    code: typing.ClassVar[int] = 179
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        length_type: LengthType = field(XmpInt())
        """coded integer, the kind of distribution of packet length."""
        min_val: int = field(XmpInt())
        """integer, lower limit on the packet length."""
        max_val: int = field(XmpInt())
        """integer, upper limit on the packet length."""

    class SetDataAttr(RequestBodyStruct):
        length_type: LengthType = field(XmpInt())
        """coded integer, the kind of distribution of packet length."""
        min_val: int = field(XmpInt())
        """integer, lower limit on the packet length."""
        max_val: int = field(XmpInt())
        """integer, upper limit on the packet length."""

    def get(self) -> Token[GetDataAttr]:
        """Get the length distribution of the packets transmitted for a stream. The length of
        the packets transmitted for a stream can be varied from packet to packet,
        according to a choice of distributions within a specified min..max range. The
        length of each packet is reflected in the size of the payload portion of the
        packet, whereas the header has constant length. Length variation complements,
        and is independent of, the content variation produced by header modifiers.

        :return: the kind of distribution of packet length, lower limit on the packet length, and upper limit on the packet length.
        :rtype: PS_PACKETLENGTH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, length_type: LengthType, min_val: int, max_val: int) -> Token[None]:
        """Set the length distribution of the packets transmitted for a stream. The length of
        the packets transmitted for a stream can be varied from packet to packet,
        according to a choice of distributions within a specified min..max range. The
        length of each packet is reflected in the size of the payload portion of the
        packet, whereas the header has constant length. Length variation complements,
        and is independent of, the content variation produced by header modifiers.

        :param length_type: the kind of distribution of packet length
        :type length_type: LengthType
        :param min_val: lower limit on the packet length
        :type min_val: int
        :param max_val: upper limit on the packet length
        :type max_val: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._stream_xindex],
                length_type=length_type,
                min_val=min_val,
                max_val=max_val
            )
        )

    set_fixed = functools.partialmethod(set, LengthType.FIXED)
    """Set the packet length distribution to Fixed.
    """

    set_incrementing = functools.partialmethod(set, LengthType.INCREMENTING)
    """Set the packet length distribution to Incrementing. Length per packet: {min, min+1, min+2,
    ...., max-2, max-1, max...}.
    """

    set_butterfly = functools.partialmethod(set, LengthType.BUTTERFLY)
    """Set the packet length distribution to Butterfly. Length per packet: {min, max, min+1, max-1, min+2, max-2,
    ...}.
    """

    set_random = functools.partialmethod(set, LengthType.RANDOM)
    """Set the packet length distribution to Random.
    """

    set_mix = functools.partialmethod(set, LengthType.MIX)
    """Set the packet length distribution to Mix.
    """


@register_command
@dataclass
class PS_PAYLOAD:
    """
    The payload content of the packets transmitted for a stream. The payload portion
    of a packet starts after the header and continues up until the test payload or
    the frame checksum. The payload may vary in length and is filled with either an
    incrementing sequence of byte values or a repeated multi-byte pattern. Length
    variation complements and is independent of the content variation produced by
    header modifiers.
    """

    code: typing.ClassVar[int] = 180
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        payload_type: PayloadType = field(XmpByte())
        """coded byte, the kind of payload content."""
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, a pattern of bytes to be repeated. The maximum length of the pattern is 18 bytes. Only used if the type is set to PATTERN."""

    class SetDataAttr(RequestBodyStruct):
        payload_type: PayloadType = field(XmpByte())
        """coded byte, the kind of payload content."""
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, a pattern of bytes to be repeated. The maximum length of the pattern is 18 bytes. Only used if the type is set to PATTERN."""

    def get(self) -> Token[GetDataAttr]:
        """Get the payload content of the packets transmitted for a stream. The payload portion
        of a packet starts after the header and continues up until the test payload or
        the frame checksum. The payload may vary in length and is filled with either an
        incrementing sequence of byte values or a repeated multi-byte pattern. Length
        variation complements and is independent of the content variation produced by
        header modifiers.

        :return: the kind of payload content, and a pattern of bytes to be repeated.
        :rtype: PS_PAYLOAD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, payload_type: PayloadType, hex_data: Hex) -> Token[None]:
        """Set the payload content of the packets transmitted for a stream. The payload portion
        of a packet starts after the header and continues up until the test payload or
        the frame checksum. The payload may vary in length and is filled with either an
        incrementing sequence of byte values or a repeated multi-byte pattern. Length
        variation complements and is independent of the content variation produced by
        header modifiers.

        :param payload_type: the kind of payload content
        :type payload_type: PayloadType
        :param hex_data: a pattern of bytes to be repeated. The maximum length of the pattern is 18 bytes. Only used if the type is set to PATTERN.
        :type hex_data: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], payload_type=payload_type, hex_data=hex_data))

    set_pattern = functools.partialmethod(set, PayloadType.PATTERN)
    """Set payload type to the custom pattern.
    """

    set_inc_byte = functools.partialmethod(set, PayloadType.INC8)
    """Set payload type to Incrementing 0xFF (8-bit mode).
    """

    set_prbs = functools.partialmethod(set, PayloadType.PRBS)
    """Set payload type to PRBS.
    """

    set_random = functools.partialmethod(set, PayloadType.RANDOM)
    """Set payload type to Random.
    """

    set_dec_byte = functools.partialmethod(set, PayloadType.DEC8)
    """Set payload type to Decrementing 0xFF (8-bit mode).
    """

    set_inc_word = functools.partialmethod(set, PayloadType.INC16)
    """Set payload type to Incrementing 0xFFFF (16-bit mode).
    """

    set_dec_word = functools.partialmethod(set, PayloadType.DEC16)
    """Set payload type to Decrementing 0xFFFF (16-bit mode).
    """


@register_command
@dataclass
class PS_IPV4GATEWAY:
    """
    An IPv4 gateway configuration specified for a stream.
    """

    code: typing.ClassVar[int] = 181
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        gateway: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, the IPv4 gateway address of the stream."""

    class SetDataAttr(RequestBodyStruct):
        gateway: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, IPv4 gateway address of the stream."""

    def get(self) -> Token[GetDataAttr]:
        """Get the IPv4 gateway address of a stream.

        :return: the IPv4 gateway address of the stream
        :rtype: PS_IPV4GATEWAY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, gateway: ipaddress.IPv4Address) -> Token[None]:
        """Set the IPv4 gateway address of a stream.

        :param gateway: the IPv4 gateway address of the stream
        :type gateway: Union[str, ipaddress.IPv4Address, int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], gateway=gateway))


@register_command
@dataclass
class PS_IPV6GATEWAY:
    """
    An IPv6 gateway configuration specified for a stream.
    """

    code: typing.ClassVar[int] = 182
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        gateway: ipaddress.IPv6Address = field(XmpIPv6Address())
        """address, the IPv6 gateway address of the stream."""

    class SetDataAttr(RequestBodyStruct):
        gateway: ipaddress.IPv6Address = field(XmpIPv6Address())
        """address, IPv6 gateway address of the stream."""

    def get(self) -> Token[GetDataAttr]:
        """Get the IPv6 gateway address of a stream.

        :return: the IPv6 gateway address of the stream
        :rtype: PS_IPV6GATEWAY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, gateway: ipaddress.IPv6Address) -> Token[None]:
        """Set the IPv6 gateway address of a stream.

        :param gateway: the IPv6 gateway address of the stream
        :type gateway: Union[str, ipaddress.IPv6Address, int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], gateway=gateway))


@register_command
@dataclass
class PS_BURSTGAP:
    """
    When the port is in in Burst TX mode, this command defines the gap between packets in a burst
    (inter-packet gap) and the gap after a burst defined in one stream stops until a
    burst defined in the next stream starts (inter-burst gap).
    """

    code: typing.ClassVar[int] = 183
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        inter_packet_gap: int = field(XmpInt())
        """integer, Burst Inter Packet Gap (in bytes)."""
        inter_burst_gap: int = field(XmpInt())
        """integer, Inter Burst Gap (in bytes)."""

    class SetDataAttr(RequestBodyStruct):
        inter_packet_gap: int = field(XmpInt())
        """integer, Burst Inter Packet Gap (in bytes)."""
        inter_burst_gap: int = field(XmpInt())
        """integer, Inter Burst Gap (in bytes)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the gap between packets in a burst (inter-packet gap) and the gap after a burst defined in one stream stops until a
        burst defined in the next stream starts (inter-burst gap).

        :return: the gap between packets in a burst
        :rtype: PS_BURSTGAP.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, inter_packet_gap: int, inter_burst_gap: int) -> Token[None]:
        """Set the gap between packets in a burst (inter-packet gap) and the gap after a burst defined in one stream stops until a
        burst defined in the next stream starts (inter-burst gap).

        :param inter_packet_gap: Burst Inter Packet Gap (in bytes).
        :type inter_packet_gap: int
        :param inter_burst_gap: Inter Burst Gap (in bytes).
        :type inter_burst_gap: int
        """

        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], inter_packet_gap=inter_packet_gap, inter_burst_gap=inter_burst_gap)
        )


@register_command
@dataclass
class PS_INJECTFCSERR:
    """
    Force a frame checksum error in one of the packets currently being transmitted
    from a stream. This can aid in analyzing the error-detection functionality of
    the system under test. Traffic must be on for the port, and the stream must be
    enabled.
    """

    code: typing.ClassVar[int] = 185
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Set a frame checksum error in one of the packets currently being transmitted
        from a stream. This can aid in analyzing the error-detection functionality of
        the system under test. Traffic must be on for the port, and the stream must be
        enabled.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_INJECTSEQERR:
    """
    Force a sequence error by skipping a test payload sequence number in one of the
    packets currently being transmitted from a stream. This can aid in analyzing the
    error-detection functionality of the system under test. Traffic must be on for
    the port, and the stream must be enabled and include test payloads.
    """

    code: typing.ClassVar[int] = 186
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Set a sequence error by skipping a test payload sequence number in one of the
        packets currently being transmitted from a stream. This can aid in analyzing the
        error-detection functionality of the system under test. Traffic must be on for
        the port, and the stream must be enabled and include test payloads.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_INJECTMISERR:
    """
    Force a misorder error by swapping the test payload sequence numbers in two of
    the packets currently being transmitted from a stream. This can aid in analyzing
    the error-detection functionality of the system under test. Traffic must be on
    for the port, and the stream must be enabled and include test payloads.
    """

    code: typing.ClassVar[int] = 187
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Set a misorder error by swapping the test payload sequence numbers in two of
        the packets currently being transmitted from a stream. This can aid in analyzing
        the error-detection functionality of the system under test. Traffic must be on
        for the port, and the stream must be enabled and include test payloads.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_INJECTPLDERR:
    """
    Force a payload integrity error in one of the packets currently being
    transmitted from a stream. Payload integrity validation is only available for
    incrementing payloads, and the error is created by changing a byte from the
    incrementing sequence. The packet will have a correct frame checksum, but the
    receiving Xena chassis will detect the invalid payload based on information in
    the test payload. Traffic must be on for the port, and the stream must be
    enabled and include test payloads.
    """

    code: typing.ClassVar[int] = 188
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Set a payload integrity error in one of the packets currently being
        transmitted from a stream. Payload integrity validation is only available for
        incrementing payloads, and the error is created by changing a byte from the
        incrementing sequence. The packet will have a correct frame checksum, but the
        receiving Xena chassis will detect the invalid payload based on information in
        the test payload. Traffic must be on for the port, and the stream must be
        enabled and include test payloads.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_INJECTTPLDERR:
    """
    Force a test payload error in one of the packets currently being transmitted
    from a stream. This means that the test payload will not be recognized at the
    receiving port, so it will be counted as a no-test-payload packet, and there
    will be a lost packet for the stream. Traffic must be on for the port, and the
    stream must be enabled and include test payloads.
    """

    code: typing.ClassVar[int] = 189
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Set a test payload error in one of the packets currently being transmitted
        from a stream. This means that the test payload will not be recognized at the
        receiving port, so it will be counted as a no-test-payload packet, and there
        will be a lost packet for the stream. Traffic must be on for the port, and the
        stream must be enabled and include test payloads.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))


@register_command
@dataclass
class PS_MODIFIEREXT:
    """
    An extended packet modifier for a stream header. The headers of each packet
    transmitted for the stream will be varied according to the modifier
    specification. The modifier acts on 32 bits and takes up the space for two
    16-bit modifiers to do this. This command requires two sub-indices, one for
    the stream and one for the modifier. A modifier is positioned at a fixed place
    in the header, selects a number of consecutive bits starting from that position,
    and applies an action to those bits in each packet. Packets can be repeated so
    that a certain number of identical packets are transmitted before applying the
    next modification.
    """

    code: typing.ClassVar[int] = 190
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int
    _modifier_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        position: int = field(XmpInt())
        """integer, the byte position from the start of the packet. Cannot be < 1!"""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, the mask specifying which bits to affect."""
        action: ModifierAction = field(XmpInt())
        """coded integer, which action to perform on the affected bits."""
        repetition: int = field(XmpInt())
        """integer, how many times to repeat on each packet. Note: For now the only value supported is 1."""

    class SetDataAttr(RequestBodyStruct):
        position: int = field(XmpInt())
        """integer, the byte position from the start of the packet. Cannot be < 1!"""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, the mask specifying which bits to affect."""
        action: ModifierAction = field(XmpInt())
        """coded integer, which action to perform on the affected bits."""
        repetition: int = field(XmpInt())
        """integer, how many times to repeat on each packet. Note: For now the only value supported is 1."""

    def get(self) -> Token[GetDataAttr]:
        """Get an extended packet modifier for a stream header. The headers of each packet
        transmitted for the stream will be varied according to the modifier
        specification. The modifier acts on 24 bits and takes up the space for two
        16-bit modifiers to do this. This command requires two sub-indices, one for
        the stream and one for the modifier. A modifier is positioned at a fixed place
        in the header, selects a number of consecutive bits starting from that position,
        and applies an action to those bits in each packet. Packets can be repeated so
        that a certain number of identical packets are transmitted before applying the
        next modification.

        :return: the byte position from the start of the packet. Cannot be < 1!,
            the mask specifying which bits to affect, which action to perform on the affected bits,
            and how many times to repeat on each packet. Note: For now the only value supported is 1.
        :rtype: PS_MODIFIEREXT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex, self._modifier_xindex]))

    def set(self, position: int, mask: Hex, action: ModifierAction, repetition: int) -> Token[None]:
        """Set an extended packet modifier for a stream header. The headers of each packet
        transmitted for the stream will be varied according to the modifier
        specification. The modifier acts on 24 bits and takes up the space for two
        16-bit modifiers to do this. This command requires two sub-indices, one for
        the stream and one for the modifier. A modifier is positioned at a fixed place
        in the header, selects a number of consecutive bits starting from that position,
        and applies an action to those bits in each packet. Packets can be repeated so
        that a certain number of identical packets are transmitted before applying the
        next modification.

        :param position: the byte position from the start of the packet. Cannot be < 1!
        :type position: int
        :param mask: the mask specifying which bits to affect
        :type mask: str
        :param action: which action to perform on the affected bits,
        :type action: ModifierAction
        :param repetition: how many times to repeat on each packet. Note: For now the only value supported is 1.
        :type repetition: int
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._stream_xindex, self._modifier_xindex],
                position=position,
                mask=mask,
                action=action,
                repetition=repetition
            )
        )

    set_inc = functools.partialmethod(set, action=ModifierAction.INC)
    """Set modifier action to Incrementing.
    """

    set_dec = functools.partialmethod(set, action=ModifierAction.DEC)
    """Set modifier action to Decrementing.
    """

    set_random = functools.partialmethod(set, action=ModifierAction.RANDOM)
    """Set modifier action to Random.
    """


@register_command
@dataclass
class PS_MODIFIEREXTCOUNT:
    """
    The number of extended 24-bit modifiers active on the packet header of a stream.
    Each modifier is specified using PS_MODIFIEREXT.
    """

    code: typing.ClassVar[int] = 191
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        ext_modifier_count: int = field(XmpInt())
        """integer, the number of extended 24-bit modifiers for the stream."""

    class SetDataAttr(RequestBodyStruct):
        ext_modifier_count: int = field(XmpInt())
        """integer, the number of extended 24-bit modifiers for the stream."""

    def get(self) -> Token[GetDataAttr]:
        """Get the number of extended 24-bit modifiers active on the packet header of a stream.
        Each modifier is specified using PS_MODIFIEREXT.

        :return: the number of extended 24-bit modifiers for the stream
        :rtype: PS_MODIFIEREXTCOUNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, ext_modifier_count: int) -> Token[None]:
        """Set the number of extended 24-bit modifiers active on the packet header of a stream.
        Each modifier is specified using PS_MODIFIEREXT.

        :param ext_modifier_count: the number of extended 24-bit modifiers for the stream
        :type ext_modifier_count: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], ext_modifier_count=ext_modifier_count))


@register_command
@dataclass
class PS_CDFOFFSET:
    """
    This command is part of the Custom Data Field (CDF) feature. The CDF offset
    for the stream is the location in the stream data packets where the various CDF
    data will be inserted. All fields for a given stream uses the same offset
    value. The default value is zero (0) which means that the CDF data  will be
    inserted at the very start of the packet, thus overwriting the packet protocol
    headers.  If you want the CDF data to start immediately after the end of the
    packet protocol headers you will have to set the CDF field offset manually. The
    feature requires that the P_PAYLOADMODE command on the parent port has been
    set to CDF. This enables the feature for all streams on this port.
    """

    code: typing.ClassVar[int] = 195
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        offset: int = field(XmpInt())
        """integer, the location where the CDF data will be inserted."""

    class SetDataAttr(RequestBodyStruct):
        offset: int = field(XmpInt())
        """integer, the location where the CDF data will be inserted."""

    def get(self) -> Token[GetDataAttr]:
        """Get the CDF offset for the stream. This command is part of the Custom Data Field (CDF) feature. The CDF offset
        for the stream is the location in the stream data packets where the various CDF
        data will be inserted. All fields for a given stream uses the same offset
        value. The default value is zero (0) which means that the CDF data  will be
        inserted at the very start of the packet, thus overwriting the packet protocol
        headers.  If you want the CDF data to start immediately after the end of the
        packet protocol headers you will have to set the CDF field offset manually. The
        feature requires that the P_PAYLOADMODE command on the parent port has been
        set to CDF. This enables the feature for all streams on this port.

        :return: the location where the CDF data will be inserted
        :rtype: PS_CDFOFFSET.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, offset: int) -> Token[None]:
        """Set the CDF offset for the stream. This command is part of the Custom Data Field (CDF) feature. The CDF offset
        for the stream is the location in the stream data packets where the various CDF
        data will be inserted. All fields for a given stream uses the same offset
        value. The default value is zero (0) which means that the CDF data  will be
        inserted at the very start of the packet, thus overwriting the packet protocol
        headers.  If you want the CDF data to start immediately after the end of the
        packet protocol headers you will have to set the CDF field offset manually. The
        feature requires that the P_PAYLOADMODE command on the parent port has been
        set to CDF. This enables the feature for all streams on this port.

        :param offset: the location where the CDF data will be inserted
        :type offset: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], offset=offset))


@register_command
@dataclass
class PS_CDFCOUNT:
    """
    This command is part of the Custom Data Field (CDF) feature. It controls the
    number of custom data fields available for each stream. You can set a different number
    of fields for each stream. Changing the field count value to a larger value will
    leave all existing fields intact. Changing the field count value to a smaller
    value will remove all existing fields with an index larger than or equal to the
    new count. The feature requires that the P_PAYLOADMODE command on the parent
    port has been set to CDF. This enables the feature for all streams on this port.
    """

    code: typing.ClassVar[int] = 196
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        cdf_count: int = field(XmpInt())
        """integer, the number of CDF data fields to allocate for the stream."""

    class SetDataAttr(RequestBodyStruct):
        cdf_count: int = field(XmpInt())
        """integer, the number of CDF data fields to allocate for the stream."""

    def get(self) -> Token[GetDataAttr]:
        """Get the number of custom data fields available for each stream. You can set a different number
        of fields for each stream. Changing the field count value to a larger value will
        leave all existing fields intact. Changing the field count value to a smaller
        value will remove all existing fields with an index larger than or equal to the
        new count. The feature requires that the P_PAYLOADMODE command on the parent
        port has been set to CDF. This enables the feature for all streams on this port.

        :return: the number of CDF data fields to allocate for the stream
        :rtype: PS_CDFCOUNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, cdf_count: int) -> Token[None]:
        """Set the number of custom data fields available for each stream. You can set a different number
        of fields for each stream. Changing the field count value to a larger value will
        leave all existing fields intact. Changing the field count value to a smaller
        value will remove all existing fields with an index larger than or equal to the
        new count. The feature requires that the P_PAYLOADMODE command on the parent
        port has been set to CDF. This enables the feature for all streams on this port.


        :param cdf_count: the number of CDF data fields to allocate for the stream
        :type cdf_count: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], cdf_count=cdf_count))


@register_command
@dataclass
class PS_CDFDATA:
    """
    This command is part of the Custom Data Field (CDF) feature. It controls the
    actual field data for a single field. It is possible to define fields with
    different data lengths for each stream. If the length of a data field exceeds
    (packet length - CDF offset) defined for the stream the field data will be
    truncated when transmitted. The feature requires that the P_PAYLOADMODE
    command on the parent port has been set to CDF. This enables the feature for
    all streams on this port.
    """

    code: typing.ClassVar[int] = 197
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int
    _custom_data_field_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, the actual field data for a single field."""

    class SetDataAttr(RequestBodyStruct):
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, a pattern of bytes to be used."""

    def get(self) -> Token[GetDataAttr]:
        """Get the actual field data for a single field. It is possible to define fields with
        different data lengths for each stream. If the length of a data field exceeds
        (packet length - CDF offset) defined for the stream the field data will be
        truncated when transmitted. The feature requires that the P_PAYLOADMODE
        command on the parent port has been set to CDF. This enables the feature for
        all streams on this port.

        :return: the actual field data for a single field
        :rtype: PS_CDFDATA.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex, self._custom_data_field_xindex]))

    def set(self, hex_data: Hex) -> Token[None]:
        """Set the actual field data for a single field. It is possible to define fields with
        different data lengths for each stream. If the length of a data field exceeds
        (packet length - CDF offset) defined for the stream the field data will be
        truncated when transmitted. The feature requires that the P_PAYLOADMODE
        command on the parent port has been set to CDF. This enables the feature for
        all streams on this port.

        :param hex_data: a pattern of bytes to be used
        :type hex_data: Hex
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._stream_xindex, self._custom_data_field_xindex],
                hex_data=hex_data
            )
        )


@register_command
@dataclass
class PS_EXTPAYLOAD:
    """
    This command controls the extended payload feature. The PS_PAYLOAD command
    described above only allow the user to specify an 18-byte pattern (when
    PS_PAYLOAD is set to PATTERN). The PS_EXTPAYLOAD command allow the definition
    of a much larger (up to MTU) payload buffer for each stream. The extended
    payload will be inserted immediately after the end of the protocol segment area.
    The feature requires the P_PAYLOADMODE command on the parent port being set to
    EXTPL. This enables the feature for all streams on this port.
    """

    code: typing.ClassVar[int] = 199
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, a pattern of bytes to be repeated."""

    class SetDataAttr(RequestBodyStruct):
        hex_data: Hex = field(XmpHex())
        """list of hex bytes, a pattern of bytes to be repeated."""

    def get(self) -> Token[GetDataAttr]:
        """Get the extended payload in bytes of a stream.

        :return: the extended payload in bytes of a stream
        :rtype: PS_EXTPAYLOAD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, hex_data: Hex) -> Token[None]:
        """Set the extended payload in bytes of a stream. The PS_EXTPAYLOAD command allow the definition
        of a much larger (up to MTU) payload buffer for each stream. The extended
        payload will be inserted immediately after the end of the protocol segment area.
        The feature requires the P_PAYLOADMODE command on the parent port being set to
        EXTPL. This enables the feature for all streams on this port.

        :param hex_data: the extended payload in bytes of a stream
        :type hex_data: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], hex_data=hex_data))


@register_command
@dataclass
class PS_PFCPRIORITY:
    """
    Set and get the Priority Flow Control (PFC) Cos value of a stream.
    """

    code: typing.ClassVar[int] = 219
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        cos: PFCMode = field(XmpByte())
        """coded byte, the Priority Flow Control (PFC) Cos value of a stream."""

    class SetDataAttr(RequestBodyStruct):
        cos: PFCMode = field(XmpByte())
        """coded byte, the Priority Flow Control (PFC) Cos value of a stream."""

    def get(self) -> Token[GetDataAttr]:
        """Get the the Priority Flow Control (PFC) Cos value of a stream.

        :return: the Priority Flow Control (PFC) Cos value of a stream.
        :rtype: PS_PFCPRIORITY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, cos: PFCMode) -> Token[None]:
        """Set the Priority Flow Control (PFC) Cos value of a stream.

        :param cos: the Priority Flow Control (PFC) Cos value of a stream.
        :type cos: PFCMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], cos=cos))


@register_command
@dataclass
class PS_OPTIONS:
    """
    Define the set of active option flags for the stream. The set form sets the flags listed in <options>, and clears the flags not listed. To clear all flags, simply omit <options> in the command.
    """

    code: typing.ClassVar[int] = 220
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        options: typing.List[StreamOption] = field(XmpSequence(types_chunk=[XmpByte()]))
        """coded byte, This flag affects the INC8/DEC8/INC16/DEC16 payload types (refer to the PS_PAYLOAD command): With the flag set, the first payload byte/word after the header will be 0 (INC8/INC16) or -1 (DEC8/DEC16). With the flag unset, the default is used: The first payload byte/word of the payload will be equal to <length of header> (INC8/INC16), or -<length of header> - 1 (DEC8/DEC16)."""

    class SetDataAttr(RequestBodyStruct):
        options: typing.List[StreamOption] = field(XmpSequence(types_chunk=[XmpByte()]))
        """coded byte, This flag affects the INC8/DEC8/INC16/DEC16 payload types (refer to the PS_PAYLOAD command): With the flag set, the first payload byte/word after the header will be 0 (INC8/INC16) or -1 (DEC8/DEC16). With the flag unset, the default is used: The first payload byte/word of the payload will be equal to <length of header> (INC8/INC16), or -<length of header> - 1 (DEC8/DEC16)."""

    def get(self) -> Token[GetDataAttr]:
        """Define the set of active “option flags” for the stream. The “set” form sets the flags listed in <options>, and clears the flags not listed. To clear all flags, simply omit <options> in the command.

        :return: the option flags
        :rtype: PS_OPTION.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, options: typing.List[StreamOption]) -> Token[None]:
        """Define the set of active “option flags” for the stream. The “set” form sets the flags listed in <options>, and clears the flags not listed. To clear all flags, simply omit <options> in the command.

        :param options: the option flags
        :type options: StreamOption
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], options=options))
