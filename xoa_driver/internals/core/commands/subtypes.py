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
    element_type = NdpChunk  # type

@add_on
@dataclass
class DhcpChunk:
    ipv4_address: XmpField[xt.XmpIPV4Address] = XmpField(xt.XmpIPV4Address)  # provided IP address by DHCP Server
    subnet_mask: XmpField[xt.XmpIPV4Address] = XmpField(xt.XmpIPV4Address)  # provided Subnet mask by DHCP Server
    braodcast_address: XmpField[xt.XmpIPV4Address] = XmpField(xt.XmpIPV4Address)  # provided Broadcast address by DHCP Server
    defaultgw: XmpField[xt.XmpIPV4Address] = XmpField(xt.XmpIPV4Address)  # provided Default GW by DHCP Server
    lease_time: XmpField[xt.XmpInt] = XmpField(xt.XmpInt)  # provided Lease Time by DHCP Server
    mac_address: XmpField[xt.XmpMacAddress] = XmpField(xt.XmpMacAddress)  # The client source mac address that this DHCP request blongs to


class DhcpChunkList(xt.XmpDefaultList):
    element_type = DhcpChunk # type
    

@add_on
@dataclass
class GroupAddressElem:
    def __init__(self, ip_address, subnet_mask, mac_address):
        self.ipv4_address = ip_address
        self.subnet_mask = subnet_mask
        self.mac_address = mac_address
        
    
    
    ipv4_address: XmpField[xt.XmpIPV4Address] = XmpField(xt.XmpIPV4Address)  # Ip address
    subnet_mask: XmpField[xt.XmpIPV4Address] = XmpField(xt.XmpIPV4Address)  # Subne Mask
    mac_address: XmpField[xt.XmpMacAddress] = XmpField(xt.XmpMacAddress)  # Mac Address


class GroupAddressPool(xt.XmpDefaultList):
    element_type = GroupAddressElem # type
    
class VlanTags(xt.XmpDefaultList):
    element_type = xt.XmpHex2 # type
    
@add_on
@dataclass
class QueueStatsElem:
    rx_bytes: XmpField[xt.XmpLong] = XmpField(xt.XmpLong)  # Total Received Bytes
    rx_packets: XmpField[xt.XmpLong] = XmpField(xt.XmpLong)  # Total Received Packets
    tx_bytes: XmpField[xt.XmpLong] = XmpField(xt.XmpLong)  # Total Sent Bytes
    tx_packets: XmpField[xt.XmpLong] = XmpField(xt.XmpLong)  # Total Sent Packets


class QueueStatsList(xt.XmpDefaultList):
    element_type = QueueStatsElem # type