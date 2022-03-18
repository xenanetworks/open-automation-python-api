from dataclasses import dataclass
from ..protocol.fields.data_types import *
from ..protocol.fields.add_on import add_on
from ..protocol.fields.field import XmpField
from .enums import OnOff

@add_on
@dataclass
class ArpChunk:
    ipv4_address: XmpField[XmpIPV4Address] = XmpField(XmpIPV4Address)  # The IP address to match to the Target IP address in the ARP requests
    prefix: XmpField[XmpShort] = XmpField(XmpShort)  # The IP prefix used for address matching.
    patched_mac: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix
    mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # The target MAC address to return in the ARP reply. If set t to all-zero, the port MAC address will be used.


class ArpChunkList(XmpDefaultList):
    element_type = ArpChunk # type: ignore


@add_on
@dataclass
class NdpChunk:
    ipv6_address: XmpField[XmpIPV6Address] = XmpField(XmpIPV6Address)  # The IP address to match to the Target IP address in the NDP Neighbor Solicitation
    prefix: XmpField[XmpShort] = XmpField(XmpShort)  # The IP prefix used for address matching.
    patched_mac: XmpField[XmpByte] = XmpField(XmpByte, choices=OnOff)  # If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix
    mac_address: XmpField[XmpMacAddress] = XmpField(XmpMacAddress)  # The target MAC address to return in the NDP Neighbor Advertisement. If set t to all-zero, the port MAC address will be used.


class NdpChunkList(XmpDefaultList):
    element_type = NdpChunk # type: ignore


@add_on
@dataclass
class PortSpeedChuck:
    port_count: XmpField[XmpInt] = XmpField(XmpInt)   # Number of ports for this speed.
    port_speed: XmpField[XmpInt] = XmpField(XmpInt)  # Unit is Mbps.

class PortSpeedChuckList(XmpDefaultList):
    element_type = PortSpeedChuck # type: ignore



