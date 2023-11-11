TLS
=========================

.. note::

    Applicable to Vulcan port only.
    
Alerts
------



.. code-block:: python

    await cg.tls.counters.alert.fatal.get()

    await cg.tls.counters.alert.warning.get()

Payload
--------



.. code-block:: python

    await cg.tls.counters.payload.tx.get()
    await cg.tls.counters.payload.rx.get()

State
-----



.. code-block:: python

    await cg.tls.counters.state.current.get()
    await cg.tls.counters.state.rate.get()
    await cg.tls.counters.state.total.get()

Histogram
----------



.. code-block:: python

    await cg.tls.histogram.handshake.get()
    await cg.tls.histogram.payload.rx_bytes.get()
    await cg.tls.histogram.payload.tx_bytes.get()
