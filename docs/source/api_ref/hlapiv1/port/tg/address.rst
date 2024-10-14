Port Address
=========================

MAC Address
-----------
A 48-bit Ethernet MAC address specified for a port. This address is used as the
default source MAC field in the header of generated traffic for the port, and is
also used for support of the ARP protocol.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACADDRESS`

.. code-block:: python

    # MAC Address
    await port.net_config.mac_address.set(mac_address=Hex("000000000000"))
    
    resp = await port.net_config.mac_address.get()
    resp.mac_address


IPv4 Address
------------
An IPv4 network configuration specified for a port. The address is used as the
default source address field in the IP header of generated traffic, and the
configuration is also used for support of the ARP and PING protocols.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_IPADDRESS`

.. code-block:: python

    # IPv4 Address
    await port.net_config.ipv4.address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.1.1"),
        wild=ipaddress.IPv4Address("0.0.0.0"))
    
    resp = await port.net_config.ipv4.address.get()
    resp.ipv4_address
    resp.gateway
    resp.subnet_mask
    resp.wild


ARP Reply
-----------
Whether the port replies to ARP requests. The
port can reply to incoming ARP requests by mapping the IP address specified for
the port to the MAC address specified for the port. ARP/NDP reply generation is
independent of whether traffic and capture is on for the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_ARPREPLY`

.. code-block:: python

    # ARP Reply
    await port.net_config.ipv4.arp_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv4.arp_reply.set(on_off=enums.OnOff.OFF)

    resp = await port.net_config.ipv4.arp_reply.get()
    resp.on_off


Ping Reply
-----------
Whether the port replies to IPv4/IPv6 PING. The port can
reply to incoming IPv4/IPv6 PING requests to the IP address specified for the port. IPv4/IPv6 PING
reply generation is independent of whether traffic and capture is on for the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_PINGREPLY`

.. code-block:: python

    # Ping Reply
    await port.net_config.ipv4.ping_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv4.ping_reply.set(on_off=enums.OnOff.OFF)

    resp = await port.net_config.ipv4.ping_reply.get()
    resp.on_off


IPv6 Address
------------
An IPv6 network configuration specified for a port. The address is used as the
default source address field in the IP header of generated traffic, and the
configuration is also used for support of the NDP and PINGv6 protocols.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_IPV6ADDRESS`

.. code-block:: python

    # IPv6 Address
    await port.net_config.ipv6.address.set(
        ipv6_address=ipaddress.IPv6Address("fc00::0002"),
        gateway=ipaddress.IPv6Address("fc00::0001"),
        subnet_prefix=7,
        wildcard_prefix=0
    )
    
    resp = await port.net_config.ipv6.address.get()
    resp.ipv6_address
    resp.gateway
    resp.subnet_prefix
    resp.wildcard_prefix


NDP Reply
-----------
Whether the port generates replies using the IPv6 Network Discovery Protocol.
The port can reply to incoming NDP Neighbor Solicitations by mapping the IPv6 address
specified for the port to the MAC address specified for the port. NDP reply
generation is independent of whether traffic and capture is on for the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_ARPV6REPLY`

.. code-block:: python

    # NDP Reply
    await port.net_config.ipv6.arp_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv6.arp_reply.set(on_off=enums.OnOff.OFF)

    resp = await port.net_config.ipv6.arp_reply.get()
    resp.on_off


IPv6 Ping Reply
---------------
Whether the port generates PINGv6 replies using the ICMP protocol received over
IPv6. The port can reply to incoming PINGv6 requests to the IPv6 address
specified for the port. PINGv6 reply generation is independent of whether
traffic and capture is on for the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_PINGV6REPLY`

.. code-block:: python

    # IPv6 Ping Reply
    await port.net_config.ipv6.ping_reply.set(on_off=enums.OnOff.ON)
    await port.net_config.ipv6.ping_reply.set(on_off=enums.OnOff.OFF)

    resp = await port.net_config.ipv6.ping_reply.get()
    resp.on_off


ARP Table
------------
Port ARP table used to reply to incoming ARP requests.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_ARPRXTABLE`

.. seealso::

    Detailed script example can be found at `ip_streams_arp_ndp_table <https://github.com/xenanetworks/open-automation-script-library/tree/main/ip_streams_arp_ndp_table>`_

.. code-block:: python

    # ARP Table
    await port.arp_rx_table.set(chunks=[])
    
    resp = await port.arp_rx_table.get()
    resp.chunks


NDP Table
------------
Port NDP table used to reply to incoming NDP Neighbor Solicitation.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_NDPRXTABLE`

.. seealso::

    Detailed script example can be found at `ip_streams_arp_ndp_table <https://github.com/xenanetworks/open-automation-script-library/tree/main/ip_streams_arp_ndp_table>`_

.. code-block:: python

    # NDP Table
    await port.ndp_rx_table.set(chunks=[])
    
    resp = await port.ndp_rx_table.get()
    resp.chunks