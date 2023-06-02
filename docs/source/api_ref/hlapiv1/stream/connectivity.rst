Connectivity Check
=========================

IPv4 Gateway Address
--------------------

.. code-block:: python

    await stream.gateway.ipv4.set()
    await stream.gateway.ipv4.get()


IPv6 Gateway Address
--------------------

.. code-block:: python

    await stream.gateway.ipv6.set()
    await stream.gateway.ipv6.get()


ARP Resolve Peer Address
------------------------

.. note::
    
    You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ARP resolve the MAC address.

.. code-block:: python

    await stream.request.arp.get()


PING Check IP Peer
------------------------

.. note::

    You need to make sure either the port has a correct gateway or the stream has a correct destination IP address to ping.

.. code-block:: python

    await stream.request.ping.get()

