from dataclasses import dataclass
from ..protocol.fields import data_types as xt
from ..protocol.fields.add_on import add_on
from ..protocol.fields.field import XmpField
from .enums import OnOff


@add_on
@dataclass
class ArpChunk:
    ipv4_address: XmpField[xt.XmpIPV4Address] = XmpField(xt.XmpIPV4Address)  # The IP address to match to the Target IP address in the ARP requests
    prefix: XmpField[xt.XmpShort] = XmpField(xt.XmpShort)  # The IP prefix used for address matching.
    patched_mac: XmpField[xt.XmpByte] = XmpField(xt.XmpByte, choices=OnOff)  # If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix
    mac_address: XmpField[xt.XmpMacAddress] = XmpField(xt.XmpMacAddress)  # The target MAC address to return in the ARP reply. If set t to all-zero, the port MAC address will be used.


class ArpChunkList(xt.XmpDefaultList):
    element_type = ArpChunk  # type: ignore


@add_on
@dataclass
class NdpChunk:
    ipv6_address: XmpField[xt.XmpIPV6Address] = XmpField(xt.XmpIPV6Address)  # The IP address to match to the Target IP address in the NDP Neighbor Solicitation
    prefix: XmpField[xt.XmpShort] = XmpField(xt.XmpShort)  # The IP prefix used for address matching.
    patched_mac: XmpField[xt.XmpByte] = XmpField(xt.XmpByte, choices=OnOff)  # If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix
    mac_address: XmpField[xt.XmpMacAddress] = XmpField(xt.XmpMacAddress)  # The target MAC address to return in the NDP Neighbor Advertisement. If set t to all-zero, the port MAC address will be used.


class NdpChunkList(xt.XmpDefaultList):
    element_type = NdpChunk  # type: ignore
