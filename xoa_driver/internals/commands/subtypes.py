import ipaddress
from dataclasses import dataclass

from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    XmpByte,
    XmpShort,
    XmpInt,
    XmpLong,
    XmpMacAddress,
    XmpIPv4Address,
    Hex,
)
from .enums import (
    OnOff,
    VlanType
)


@dataclass
class ArpChunk:
    ipv4_address: ipaddress.IPv4Address
    """The IP address to match to the Target IP address in the ARP requests"""

    prefix: int
    """The IP prefix used for address matching."""

    patched_mac: OnOff
    """If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix"""

    mac_address: Hex
    """The target MAC address to return in the ARP reply. If set t to all-zero, the port MAC address will be used."""


@dataclass
class NdpChunk:
    ipv6_address: ipaddress.IPv6Address
    """The IP address to match to the Target IP address in the NDP Neighbor Solicitation"""

    prefix: int
    """The IP prefix used for address matching."""

    patched_mac: OnOff
    """If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix"""

    mac_address: Hex
    """The target MAC address to return in the NDP Neighbor Advertisement. If set t to all-zero, the port MAC address will be used."""

@dataclass
class DhcpChunk:
    ipv4_address:       ipaddress.IPv4Address = field(XmpIPv4Address())  # provided IP address by DHCP Server
    subnet_mask:        ipaddress.IPv4Address = field(XmpIPv4Address())  # provided Subnet mask by DHCP Server
    braodcast_address:  ipaddress.IPv4Address = field(XmpIPv4Address())  # provided Broadcast address by DHCP Server
    defaultgw:          ipaddress.IPv4Address = field(XmpIPv4Address())  # provided Default GW by DHCP Server
    lease_time:         int                   = field(XmpInt())          # provided Lease Time by DHCP Server
    mac_address:        Hex                   = field(XmpMacAddress())   # The client source mac address that this DHCP request blongs to

@dataclass
class GroupAddressElem:
    def __init__(self, ip_address, subnet_mask, mac_address):
        self.ipv4_address = ip_address
        self.subnet_mask = subnet_mask
        self.mac_address = mac_address
        
    
    
    ipv4_address:   ipaddress.IPv4Address = field(XmpIPv4Address()) # Ip address
    subnet_mask:    ipaddress.IPv4Address = field(XmpIPv4Address()) # Subne Mask
    mac_address:    Hex                   = field(XmpMacAddress())  # Mac Address

    
@dataclass
class VlanTag:
    def __init__(self, tci, type):
        self.tci = tci
        self.type = type
    
    tci: int        =   field(XmpShort())  # 
    type: VlanType  =   field(XmpByte())  # Subne Mask
    
@dataclass
class QueueStatsElem:
    rx_bytes:   int = field(XmpLong())  # Total Received Bytes
    rx_packets: int = field(XmpLong())  # Total Received Packets
    tx_bytes:   int = field(XmpLong())  # Total Sent Bytes
    tx_packets: int = field(XmpLong())  # Total Sent Packets
