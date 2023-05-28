UDP
=========================

.. note::

    Applicable to Vulcan port only.
    
Packet Size Range
-----------------------

.. code-block:: python

    await cg.udp.packet_size.range_limits.set()
    await cg.udp.packet_size.range_limits.get()


Packet Size Type
----------------------

.. code-block:: python

    await cg.udp.packet_size.type.set_fixed()
    await cg.udp.packet_size.type.set_increment()
    await cg.udp.packet_size.type.set_random()
    await cg.udp.packet_size.type.get()


Packet Size Value
----------------------

.. code-block:: python

    await cg.udp.packet_size.value.set()
    await cg.udp.packet_size.value.get()

