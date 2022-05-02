#: Impairment Port Commands

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
class PE_FCSDROP:
    """
    The action on packets with FCS errors on a port.
    """

    code: typing.ClassVar[int] = 1601
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, the action on packets with FCS errors on a port

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, the action on packets with FCS errors on a port

    def get(self) -> "Token[GetDataAttr]":
        """Get the status of whether the action on packets with FCS errors on a port is enabled.

        :return: whether the action on packets with FCS errors on a port is enabled
        :rtype: PE_FCSDROP.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> "Token":
        """Set the status of whether the action on packets with FCS errors on a port is enabled.

        :param on_off:  whether the action on packets with FCS errors on a port is enabled
        :type on_off: OnOff
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the action on packets with FCS errors on a port.
    """
    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the action on packets with FCS errors on a port.
    """


@register_command
@dataclass
class PE_TPLDMODE:
    """
    The action indicates the TPLD mode to be used per port.
    """

    code: typing.ClassVar[int] = 1602
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=TPLDMode)  # coded byte, indicating the TPLD mode.

    @dataclass(frozen=True)
    class GetDataAttr:
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=TPLDMode)  # coded byte, indicating the TPLD mode.

    def get(self) -> "Token[GetDataAttr]":
        """Get the TPLD mode of the port.

        :return: indicating the TPLD mode
        :rtype: PE_TPLDMODE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, mode: TPLDMode) -> "Token":
        """Set the TPLD mode of the port.

        :param mode: indicating the TPLD mode
        :type mode: TPLDMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, mode=mode))

    set_normal = functools.partialmethod(set, TPLDMode.NORMAL)
    """Set the TPLD mode to Normal.
    """
    set_micro = functools.partialmethod(set, TPLDMode.MICRO)
    """Set the TPLD mode to Micro.
    """


@register_command
@dataclass
class PE_COMMENT:
    """
    Flow description.
    """

    code: typing.ClassVar[int] = 1605
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the description of the flow.

    @dataclass(frozen=True)
    class GetDataAttr:
        comment: XmpField[XmpStr] = XmpField(XmpStr)  # string, containing the description of the flow.

    def get(self) -> "Token[GetDataAttr]":
        """Get the flow description.

        :return: the description of the flow
        :rtype: PE_COMMENT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))

    def set(self, comment: str) -> "Token":
        """Set the flow description.

        :param comment: the description of the flow
        :type comment: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex], comment=comment))


@register_command
@dataclass
class PE_INDICES:
    """
    Get the flow indices. Currently the number of flows is 8.
    """

    code: typing.ClassVar[int] = 1608
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        flow0_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 0.
        flow1_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 1.
        flow2_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 2.
        flow3_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 3.
        flow4_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 4.
        flow5_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 5.
        flow6_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 6.
        flow7_id: XmpField[XmpInt] = XmpField(XmpInt)  # integer, id of flow 7.

    def get(self) -> "Token[GetDataAttr]":
        """Get the flow indices of a port. Currently the number of flows is fixed to 8.

        :return: the flow indices of a port
        :rtype: PE_INDICES.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PE_LATENCYRANGE:
    """
    Retrieve minimum and maximum configurable latency per flow in nanoseconds.
    """

    code: typing.ClassVar[int] = 1646
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        min_latency: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, minimum configurable latency per flow in nanoseconds.
        max_latency: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, maximum configurable latency per flow in nanoseconds.

    def get(self) -> "Token[GetDataAttr]":
        """Get the minimum and maximum configurable latency per flow in nanoseconds.

        :return: minimum and maximum configurable latency per flow in nanoseconds.
        :rtype: PE_LATENCYRANGE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PE_CORRUPT:
    """
    Configures impairment corruption type.
    
    .. note::
        
        IP / TCP / UDP corruption modes are not supported on default flow (0)

    """

    code: typing.ClassVar[int] = 1660
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        corruption_type: XmpField[XmpByte] = XmpField(XmpByte, choices=CorruptionType)  # coded byte, specifying corruption type.

    @dataclass(frozen=True)
    class GetDataAttr:
        corruption_type: XmpField[XmpByte] = XmpField(XmpByte, choices=CorruptionType)  # coded byte, specifying corruption type.

    def get(self) -> "Token[GetDataAttr]":
        """Get the impairment corruption type of a flow.

        :return: the impairment corruption type of a flow.
        :rtype: PE_CORRUPT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))

    def set(self, corruption_type: CorruptionType) -> "Token":
        """Set the impairment corruption type.

        :param corruption_type: corruption type
        :type corruption_type: CorruptionType
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex], corruption_type=corruption_type))

    set_off = functools.partialmethod(set, CorruptionType.OFF)
    """Set the corruption type to OFF.
    """
    set_eth = functools.partialmethod(set, CorruptionType.ETH)
    """Set the corruption type to Ethernet.
    """
    set_ip = functools.partialmethod(set, CorruptionType.IP)
    """Set the corruption type to IP.
    """
    set_udp = functools.partialmethod(set, CorruptionType.UDP)
    """Set the corruption type to UDP.
    """
    set_tcp = functools.partialmethod(set, CorruptionType.TCP)
    """Set the corruption type to TCP.
    """
    set_ber = functools.partialmethod(set, CorruptionType.BER)
    """Set the corruption type to Bit Error Rate.
    """


@register_command
@dataclass
class PE_MISORDER:
    """
    Configures the misordering depth in number of packets.
    
    .. note::
        probability [see :class:`~xoa_driver.internals.core.commands.ped_commands.PED_FIXED`] * (depth + 1) should be less than 1,000,000.
        
    """

    code: typing.ClassVar[int] = 1661
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        depth: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, specifies the misordering depth (Range 1 - 32). Default value. Note: probability [see PED_FIXED] * (depth + 1) should be less than 1,000,000.

    @dataclass(frozen=True)
    class GetDataAttr:
        depth: XmpField[XmpInt] = XmpField(
            XmpInt
        )  # integer, specifies the misordering depth (Range 1 - 32). Default value. Note: probability [see PED_FIXED] * (depth + 1) should be less than 1,000,000.

    def get(self) -> "Token[GetDataAttr]":
        """Get the misordering depth in number of packets of a flow.

        :return: the misordering depth (Range 1 - 32). Default value. 
        :rtype: PE_MISORDER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))

    def set(self, depth: int) -> "Token":
        """Set the misordering depth in number of packets of a flow. Note: probability [see
        PED_FIXED] * (depth + 1) should be less than 1,000,000.

        :param depth: the misordering depth (Range 1 - 32). Default value.
        :type depth: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex], depth=depth))


@register_command
@dataclass
class PE_BANDPOLICER:
    """
    Configures the bandwidth policer.
    """

    code: typing.ClassVar[int] = 1662
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, enables/disables policer. Note: PED_ENABLE is not supported for the policer.
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PolicerMode)  # coded byte, sets policer mode.
        cir: XmpField[XmpInt] = XmpField(XmpInt)  # integer, policer committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.
        cbs: XmpField[XmpInt] = XmpField(XmpInt)  # integer, policer committed burst size in bytes (range 0 to 4194304), default is 0.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, enables/disables policer. Note: PED_ENABLE is not supported for the policer.
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PolicerMode)  # coded byte, sets policer mode.
        cir: XmpField[XmpInt] = XmpField(XmpInt)  # integer, policer committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.
        cbs: XmpField[XmpInt] = XmpField(XmpInt)  # integer, policer committed burst burst in bytes (range 0 to 4194304), default is 0.

    def get(self) -> "Token[GetDataAttr]":
        """Get the bandwidth polcier configuration.

        :return: enabled/disabled, policer mode, committed information rate, and committed burst size.
        :rtype: PE_BANDPOLICER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))

    def set(self, on_off: OnOff, mode: PolicerMode, cir: int, cbs: int) -> "Token":
        """Set the bandwidth polcier configuration. 

        :param on_off: enables/disables policer. Note: PED_ENABLE is not supported for the policer.
        :type on_off: OnOff
        :param mode: policer mode
        :type mode: PolicerMode
        :param cir: policer committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.
        :type cir: int
        :param cbs: policer committed burst burst in bytes (range 0 to 4194304), default is 0.
        :type cbs: int
        """
        return Token(
            self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex], on_off=on_off, mode=mode, cir=cir, cbs=cbs)
        )


@register_command
@dataclass
class PE_BANDSHAPER:
    """
    Configures the bandwidth shaper. L1 (0) (Shaper performed at Layer 1 level. I.e. including
    the preamble and min interpacket gap) L2 (1) (Shaper performed at Layer 2 level. I.e. excluding the preamble and min interpacket gap) Default value: L2 (0)
    """

    code: typing.ClassVar[int] = 1663
    pushed: typing.ClassVar[bool] = True

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, enables/disables shaper.
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PolicerMode)  # coded byte, sets shaper mode.
        cir: XmpField[XmpInt] = XmpField(XmpInt)  # integer, shaper committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.
        cbs: XmpField[XmpInt] = XmpField(XmpInt)  # integer, shaper committed burst size in bytes (range 0 to 4194304), default is 0.
        buffer_size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, shaper buffer size in bytes (range 0 to 2097152), default is 0.

    @dataclass(frozen=True)
    class GetDataAttr:
        on_off: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # coded byte, enables/disables shaper.
        mode: XmpField[XmpByte] = XmpField(XmpByte, choices=PolicerMode)  # coded byte, sets shaper mode.
        cir: XmpField[XmpInt] = XmpField(XmpInt)  # integer, shaper committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.
        cbs: XmpField[XmpInt] = XmpField(XmpInt)  # integer, shaper committed burst size in bytes (range 0 to 4194304), default is 0.
        buffer_size: XmpField[XmpInt] = XmpField(XmpInt)  # integer, shaper buffer size in bytes (range 0 to 2097152), default is 0.

    def get(self) -> "Token[GetDataAttr]":
        """Get the bandwidth shaper configuration.

        :return: the bandwidth shaper configuration, including on/off, mode, CIR, CBS, and shaper buffer size.
        :rtype: PE_BANDSHAPER.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))

    def set(self, on_off: OnOff, mode: PolicerMode, cir: int, cbs: int, buffer_size: int) -> "Token":
        """Set the bandwidth shaper configuration.

        :param on_off: enables/disables shaper
        :type on_off: OnOff
        :param mode: shaper mode
        :type mode: PolicerMode
        :param cir: shaper committed information rate in units of 100 kbps (range 0 to 1000000), default is 0.
        :type cir: int
        :param cbs: shaper committed burst size in bytes (range 0 to 4194304), default is 0.
        :type cbs: int
        :param buffer_size: shaper buffer size in bytes (range 0 to 2097152), default is 0.
        :type buffer_size: int
        """
        return Token(
            self._connection,
            build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex], on_off=on_off, mode=mode, cir=cir, cbs=cbs, buffer_size=buffer_size),
        )


@register_command
@dataclass
class PE_DROPTOTAL:
    """
    Obtains statistics concerning all the packets dropped between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1750
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_drop_count_total: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped in all flows.
        pkt_drop_count_programmed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped as programmed in all flows.
        pkt_drop_count_bandwidth: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped due to bandwidth control in all flows.
        pkt_drop_count_other: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped for other reasons in all flows.
        pkt_drop_ratio_total: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets dropped in all flows, expressed in ppm.
        pkt_drop_ratio_programmed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets dropped as programmed in all flows, expressed in ppm.
        pkt_drop_ratio_bandwidth: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets dropped due to bandwidth control in all flows, expressed in ppm.
        pkt_drop_ratio_other: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets dropped for other reasons in all flows, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets dropped between this receive port and its partner TX port. 

        :return: total number of packets dropped in all flows,
            total number of packets dropped as programmed in all flows,
            total number of packets dropped due to bandwidth control in all flows,
            total number of packets dropped for other reasons in all flows,
            ratio of number of packets dropped in all flows, expressed in ppm,
            ratio of number of packets dropped as programmed in all flows, expressed in ppm
        :rtype: PE_DROPTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PE_LATENCYTOTAL:
    """
    Obtains statistics concerning all the packets delayed this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1751
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets delayed in all flows.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets delayed in all flows, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets delayed this receive port and its
        partner TX port.

        :return: number of packets delayed in all flows, and ratio of number of packets delayed in all flows, expressed in ppm.
        :rtype: PE_LATENCYTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PE_DUPTOTAL:
    """
    Obtains statistics concerning all the packets duplicated between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1752
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets duplicated in all flows.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets duplicated in all flows, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets duplicated between this receive
        port and its partner TX port.

        :return: number of packets duplicated in all flows, ratio of number of packets duplicated in all flows, expressed in ppm.
        :rtype: PE_DUPTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PE_MISTOTAL:
    """
    Obtains statistics concerning all the packets mis-ordered between this receive
    port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1753
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets mis-ordered in all flows.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets mis-ordered in all flows, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets mis-ordered between this receive port and its partner TX port.

        :return: number of packets mis-ordered in all flows, number of packets mis-ordered in all flows, expressed in ppm.
        :rtype: PE_MISTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PE_CORTOTAL:
    """
    Obtains statistics concerning all the packets corrupted on between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1754
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        total_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets corrupted in all flows.
        fcs_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with Ethernet FCS corrupted in all flows.
        ip_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with IP header checksum corrupted in all flows.
        udp_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with UDP checksum corrupted in all flows.
        tcp_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with TCP checksum corrupted in all flows.
        total_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets corrupted in all flows, expressed in ppm.
        fcs_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with Ethernet FCS corrupted in all flows, expressed in ppm.
        ip_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with IP Header checksum corrupted in all flows, expressed in ppm.
        udp_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with UDP checksum corrupted in all flows, expressed in ppm.
        tcp_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with TCP checksum corrupted in all flows, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets corrupted on between this receive port and its partner TX port.

        :return: number of packets corrupted in all flows;
            number of packets with Ethernet FCS corrupted in all flows;
            number of packets with IP header checksum corrupted in all flows;
            number of packets with UDP checksum corrupted in all flows;
            number of packets with TCP checksum corrupted in all flows;
            ratio of number of packets corrupted in all flows, expressed in ppm;
            ratio of number of packets with Ethernet FCS corrupted in all flows expressed in ppm;
            ratio of number of packets with IP Header checksum corrupted in all flows, expressed in ppm;
            ratio of number of packets with UDP checksum corrupted in all flows, expressed in ppm;
            ratio of number of packets with TCP checksum corrupted in all flows, expressed in ppm
        :rtype: PE_CORTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PE_JITTERTOTAL:
    """
    Obtains statistics concerning all the packets jittered between this receive port
    and its partner TX port.
    """

    code: typing.ClassVar[int] = 1755
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets jittered in all flows.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets jittered in all flows expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets jittered between this receive port
        and its partner TX port.

        :return: number of packets jittered in all flows, ratio of number of packets jittered in all flows expressed in ppm.
        :rtype: PE_JITTERTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PE_CLEAR:
    """
    Clear all the impairment (duplicate, drop, mis-ordered, corrupted, latency and
    jitter) statistics for a Chimera port and flows on the port. The byte and packet
    counts will restart at zero.
    """

    code: typing.ClassVar[int] = 1756
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clear all the impairment (duplicate, drop, mis-ordered, corrupted, latency and
        jitter) statistics for a Chimera port and flows on the port. The byte and packet
        counts will restart at zero.
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
class PE_FLOWDROPTOTAL:
    """
    Obtains statistics concerning all the packets dropped in a flow between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1770
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_drop_count_total: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped for the flow.
        pkt_drop_count_programmed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped as programmed for the flow.
        pkt_drop_count_bandwidth: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped due to bandwidth control for the flow.
        pkt_drop_count_other: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, total number of packets dropped for other reasons for the flow.
        pkt_drop_ratio_total: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets dropped for the flow, expressed in ppm.
        pkt_drop_ratio_programmed: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets dropped as programmed for the flow, expressed in ppm.
        pkt_drop_ratio_bandwidth: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets dropped due to bandwidth control for the flow, expressed in ppm.
        pkt_drop_ratio_other: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets dropped for other reasons for the flow, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets dropped in a flow between this receive port and its partner TX port.

        :return:
            total number of packets dropped for the flow,
            total number of packets dropped as programmed for the flow,
            total number of packets dropped due to bandwidth control for the flow,
            total number of packets dropped for other reasons for the flow,
            ratio of number of packets dropped for the flow, expressed in ppm,
            ratio of number of packets dropped as programmed for the flow, expressed in ppm,
            ratio of number of packets dropped due to bandwidth control for the flow, expressed in ppm,
            ratio of number of packets dropped for other reasons for the flow, expressed in ppm.
        :rtype: PE_FLOWDROPTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PE_FLOWLATENCYTOTAL:
    """
    Obtains statistics concerning all the packets delayed between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1771
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets delayed in the flow.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets delayed in the flow, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets delayed between this receive port and its partner TX port.

        :return: number of packets delayed in the flow, ratio of number of packets delayed in the flow, expressed in ppm.
        :rtype: PE_FLOWLATENCYTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PE_FLOWDUPTOTAL:
    """
    Obtains statistics concerning all the packets duplicated in a flow between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1772
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets duplicated for the flow.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets duplicated for the flow - expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets duplicated in a flow between this receive port and its partner TX port.

        :return: number of packets duplicated for the flow, ratio of number of packets duplicated for the flow - expressed in ppm.
        :rtype: PE_FLOWDUPTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PE_FLOWMISTOTAL:
    """
    Obtains statistics concerning all the packets mis-ordered in a flow between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1773
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets mis-ordered for the flow.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets mis-ordered in a flow between this receive port and its partner TX port.

        :return: number of packets mis-ordered for the flow, ratio of number of packets, expressed in ppm.
        :rtype: PE_FLOWMISTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PE_FLOWCORTOTAL:
    """
    Obtains statistics concerning all the packets corrupted in a flow between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1774
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        total_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets corrupted for the flow.
        fcs_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with Ethernet FCS corrupted for the flow.
        ip_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with IP header checksum corrupted for the flow.
        udp_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with UDP checksum corrupted for the flow.
        tcp_corrupted_pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets with TCP checksum corrupted for the flow.
        total_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets corrupted for the flow expressed in ppm.
        fcs_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with Ethernet FCS corrupted for the flow expressed in ppm.
        ip_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with IP Header checksum corrupted for the flowexpressed in ppm.
        udp_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with UDP checksum corrupted for the flow expressed in ppm.
        tcp_corrupted_pkt_ratio: XmpField[XmpLong] = XmpField(
            XmpLong
        )  # long integer, ratio of number of packets with TCP checksum corrupted for the flow expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets corrupted in a flow between this receive port and its partner TX port.

        :return:
            number of packets corrupted for the flow,
            number of packets with Ethernet FCS corrupted for the flow,
            number of packets with IP header checksum corrupted for the flow,
            number of packets with UDP checksum corrupted for the flow,
            number of packets with TCP checksum corrupted for the flow,
            ratio of number of packets corrupted for the flow expressed in ppm,
            ratio of number of packets with Ethernet FCS corrupted for the flow expressed in ppm,
            ratio of number of packets with IP Header checksum corrupted for the flowexpressed in ppm,
            ratio of number of packets with UDP checksum corrupted for the flow expressed in ppm,
            ratio of number of packets with TCP checksum corrupted for the flow expressed in ppm.
        :rtype: PE_FLOWCORTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PE_FLOWJITTERTOTAL:
    """
    Obtains statistics concerning all the packets jittered in a flow between this receive port and its partner TX port.
    """

    code: typing.ClassVar[int] = 1775
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class GetDataAttr:
        pkt_count: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, number of packets jittered in the flow.
        ratio: XmpField[XmpLong] = XmpField(XmpLong)  # long integer, ratio of number of packets jittered in the flow, expressed in ppm.

    def get(self) -> "Token[GetDataAttr]":
        """Get statistics concerning all the packets jittered in a flow between this receive port and its partner TX port.

        :return: number of packets jittered in the flow, ratio of number of packets jittered in the flow, expressed in ppm
        :rtype: PE_FLOWJITTERTOTAL.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PE_FLOWCLEAR:
    """
    Clear all the impairment (duplicate, drop, mis-ordered, corrupted, latency and
    jitter) statistics on a particular flow on the port. The byte and packet counts
    will restart at zero.
    """

    code: typing.ClassVar[int] = 1776
    pushed: typing.ClassVar[bool] = False

    _connection: "interfaces.IConnection"
    _module: int
    _port: int
    _flow_xindex: int

    @dataclass(frozen=True)
    class SetDataAttr:
        pass

    def set(self) -> "Token":
        """Clear all the impairment (duplicate, drop, mis-ordered, corrupted, latency and
        jitter) statistics on a particular flow on the port. The byte and packet counts
        will restart at zero.
        """
        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._flow_xindex],
            ),
        )


