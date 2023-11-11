Connectivity Check
=========================

IPv4 Gateway Address
--------------------
An IPv4 gateway configuration specified for a stream.

Corresponding CLI command: ``PS_IPV4GATEWAY``

.. code-block:: python

    # IPv4 Gateway Address
    await stream.gateway.ipv4.set(gateway=ipaddress.IPv4Address("10.10.10.1"))
    
    resp = await stream.gateway.ipv4.get()
    resp.gateway


IPv6 Gateway Address
--------------------
An IPv6 gateway configuration specified for a stream.

Corresponding CLI command: ``PS_IPV6GATEWAY``

.. code-block:: python

    # IPv6 Gateway Address
    await stream.gateway.ipv6.set(gateway=ipaddress.IPv6Address("::0001"))
    
    resp = await stream.gateway.ipv6.get()
    resp.gateway


ARP Resolve Peer Address
------------------------
Generates an outgoing ARP request on the test port. The packet header for the
stream must contain an IP protocol segment, and the destination IP address is
used in the ARP request. If there is a gateway IP address specified for the port
and it is on a different subnet than the destination IP address in the packet
header, then the gateway IP address is used instead. The framing of the ARP
request matches the packet header, including any VLAN protocol segments. This
command does not generate an immediate result, but waits until an ARP
reply is received on the test port. If no reply is received within 500
milliseconds, it returns.

.. note::
    
    You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ARP resolve the MAC address.

Corresponding CLI command: ``PS_ARPREQUEST``

.. code-block:: python

    # ARP Resolve Peer Address
    # You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ARP resolve the MAC address.
    resp = await stream.request.arp.get()
    resp.mac_address


PING Check IP Peer
------------------------
Generates an outgoing ping request using the ICMP protocol on the test port. The
packet header for the stream must contain an IP protocol segment, with valid
source and destination IP addresses. The framing of the ping request matches the
packet header, including any VLAN protocol segments, and the destination MAC
address must also be valid, possibly containing a value obtained with
PS_ARPREQUEST. This command does not generate an immediate result, but
waits until a ping reply is received on the test port.

.. note::

    You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ping.

Corresponding CLI command: ``PS_PINGREQUEST``

.. code-block:: python

    # PING Check IP Peer
    # You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ping.
    resp = await stream.request.ping.get()
    resp.delay
    resp.time_to_live

