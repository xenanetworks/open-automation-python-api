Port Address
=========================

MAC Address
-----------

.. code-block:: python

    await port.net_config.mac_address.set()
    await port.net_config.mac_address.get()


IPv4 Address
------------

.. code-block:: python

    await port.net_config.ipv4.address.set()
    await port.net_config.ipv4.address.get()


ARP Reply
-----------

.. code-block:: python

    await port.net_config.ipv4.arp_reply.set()
    await port.net_config.ipv4.arp_reply.get()


Ping Reply
-----------

.. code-block:: python

    await port.net_config.ipv4.ping_reply.set()
    await port.net_config.ipv4.ping_reply.get()


IPv6 Address
------------

.. code-block:: python

    await port.net_config.ipv6.address.set()
    await port.net_config.ipv6.address.get()


NDP Reply
-----------

.. code-block:: python

    await port.net_config.ipv6.arp_reply.set()
    await port.net_config.ipv6.arp_reply.get()


IPv6 Ping Reply
---------------

.. code-block:: python

    await port.net_config.ipv6.ping_reply.set()
    await port.net_config.ipv6.ping_reply.get()


ARP Table
------------

.. code-block:: python

    await port.arp_rx_table.set()
    await port.arp_rx_table.get()


NDP Table
------------

.. code-block:: python

    await port.ndp_rx_table.set()
    await port.ndp_rx_table.get()