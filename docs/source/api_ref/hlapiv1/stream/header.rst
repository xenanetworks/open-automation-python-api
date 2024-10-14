Packet Header Definition
=========================

Header Protocol Segment
------------------------
This command will inform the Xena tester how to interpret the packet header
byte sequence specified with :class:`~xoa_driver.internals.commands.ps_commands.PS_PACKETHEADER`.  This is mainly for information
purposes, and the stream will transmit the packet header bytes even if no
protocol segments are specified.  The Xena tester however support calculation of
certain field values in hardware, such as the IP, TCP and UDP length and
checksum fields.  This allow the use of hardware modifiers for these protocol
segments.  In order for this function to work the Xena tester needs to know the
type of each segment that precedes the segment where the hardware calculation is
to be performed.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_HEADERPROTOCOL`

.. code-block:: python

    # Header Protocol Segment
    await stream.packet.header.protocol.set(segments=[
        enums.ProtocolOption.ETHERNET,
        enums.ProtocolOption.VLAN,
        enums.ProtocolOption.IP,
        enums.ProtocolOption.UDP,
    ])

    # ETHERNET = 1
    # """Ethernet II"""
    # VLAN = 2
    # """VLAN"""
    # ARP = 3
    # """Address Resolution Protocol"""
    # IP = 4
    # """IPv4"""
    # IPV6 = 5
    # """IPv6"""
    # UDP = 6
    # """User Datagram Protocol (w/o checksum)"""
    # TCP = 7
    # """Transmission Control Protocol (w/o checksum)"""
    # LLC = 8
    # """Logic Link Control"""
    # SNAP = 9
    # """Subnetwork Access Protocol"""
    # GTP = 10
    # """GPRS Tunnelling Protocol"""
    # ICMP = 11
    # """Internet Control Message Protocol"""
    # RTP = 12
    # """Real-time Transport Protocol"""
    # RTCP = 13
    # """RTP Control Protocol"""
    # STP = 14
    # """Spanning Tree Protocol"""
    # SCTP = 15
    # """Stream Control Transmission Protocol"""
    # MACCTRL = 16
    # """MAC Control"""
    # MPLS = 17
    # """Multiprotocol Label Switching"""
    # PBBTAG = 18
    # """Provider Backbone Bridge tag"""
    # FCOE = 19
    # """Fibre Channel over Ethernet"""
    # FC = 20
    # """Fibre Channel"""
    # FCOETAIL = 21
    # """Fibre Channel over Ethernet (tail)"""
    # IGMPV3L0 = 22
    # """IGMPv3 Membership Query L=0"""
    # IGMPV3L1 = 23
    # """IGMPv3 Membership Query L=1"""
    # UDPCHECK = 24
    # """User Datagram Protocol (w/ checksum)"""
    # IGMPV2 = 25
    # """Internet Group Management Protocol v2"""
    # MPLS_TP_OAM = 26
    # """MPLS-TP, OAM Header"""
    # GRE_NOCHECK = 27
    # """Generic Routing Encapsulation (w/o checksum)"""
    # GRE_CHECK = 28
    # """Generic Routing Encapsulation (w/ checksum)"""
    # TCPCHECK = 29
    # """Transmission Control Protocol (w/ checksum)"""
    # GTPV1L0 = 30
    # """GTPv1 (no options), GPRS Tunneling Protocol v1"""
    # GTPV1L1 = 31
    # """GTPv1 (w/ options), GPRS Tunneling Protocol v1"""
    # GTPV2L0 = 32
    # """GTPv2 (no options), GPRS Tunneling Protocol v2"""
    # GTPV2L1 = 33
    # """GTPv2 (w/ options), GPRS Tunneling Protocol v2"""
    # IGMPV1 = 34
    # """Internet Group Management Protocol v1"""
    # PWETHCTRL = 35
    # """PW Ethernet Control Word"""
    # VXLAN = 36
    # """Virtual eXtensible LAN"""
    # ETHERNET_8023 = 37
    # """Ethernet 802.3"""
    # NVGRE = 38
    # """Generic Routing Encapsulation (Network Virtualization)"""
    # DHCPV4 = 39
    # """Dynamic Host Configuration Protocol (IPv4)"""
    # GENEVE = 40
    # """Generic Network Virtualization Encapsulation"""

    resp = await stream.packet.header.protocol.get()
    resp.segments


Header Value
-------------------------
The first portion of the packet bytes that are transmitted for a stream. This
starts with the 14 bytes of the Ethernet header, followed by any contained
protocol segments. All packets transmitted for the stream start with this fixed
header. Individual byte positions of the packet header may be varied on a
packet-to-packet basis using modifiers. The full packet comprises the header,
the payload, an optional test payload, and the frame checksum. The header data
is specified as raw bytes, since the script environment does not know the field-
by-field layout of the various protocol segments.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_PACKETHEADER`

.. code-block:: python

    # Header Value
    await stream.packet.header.data.set(
        hex_data=Hex("00000000000004F4BC7FFE908100000008004500002A000000007F113BC400000000000000000000000000160000"))
    
    resp = await stream.packet.header.data.get()
    resp.hex_data

