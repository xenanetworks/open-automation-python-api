UDP
=========================

.. note::

    Applicable to Vulcan port only.
    
Packet
------

.. code-block:: python

    await cg.udp.counters.packet.rx.get()
    await cg.udp.counters.packet.tx.get()

Payload
--------

.. code-block:: python

    await cg.udp.counters.payload.rx.get()
    await cg.udp.counters.payload.tx.get()


State
-----

.. code-block:: python

    await cg.udp.counters.state.current.get()
    await cg.udp.counters.state.rate.get()
    await cg.udp.counters.state.total.get()

Histogram
----------

.. code-block:: python

    await cg.udp.histogram.rx_bytes.get()
    await cg.udp.histogram.tx_bytes.get()

