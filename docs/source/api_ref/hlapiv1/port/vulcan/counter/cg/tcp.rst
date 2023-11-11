TCP
=========================

.. note::

    Applicable to Vulcan port only.
    
Error
-----



.. code-block:: python

    await cg.tcp.counters.error.get()

Packet
------



.. code-block:: python

    await cg.tcp.counters.packet.tx.get()
    await cg.tcp.counters.packet.rx.get()

Payload
--------



.. code-block:: python

    await cg.tcp.counters.payload.rx.get()
    await cg.tcp.counters.payload.tx.get()

Retransmission
--------------



.. code-block:: python

    await cg.tcp.counters.retransmission.get()

State
-----



.. code-block:: python

    await cg.tcp.counters.state.current.get()
    await cg.tcp.counters.state.rate.get()
    await cg.tcp.counters.state.total.get()

Histogram
----------



.. code-block:: python

    await cg.tcp.histogram.connection.close_times.get()
    await cg.tcp.histogram.connection.establish_times.get()
    await cg.tcp.histogram.rx.good_bytes.get()
    await cg.tcp.histogram.rx.total_bytes.get()
    await cg.tcp.histogram.tx.good_bytes.get()
    await cg.tcp.histogram.tx.total_bytes.get()

Clear Port Test Statistics
--------------------------



.. code-block:: python

    await cg.tcp.clear_post_test_statistics.set()