import ipaddress
from dataclasses import dataclass

from ..protocol.payload import Hex
from .enums import OnOff


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
