Latency
=========================

Mode
------------

.. code-block:: python

    await port.latency_config.mode.set_first2first()
    await port.latency_config.mode.set_first2last()
    await port.latency_config.mode.set_last2first()
    await port.latency_config.mode.set_last2last()
    await port.latency_config.mode.get()


Offset
--------------

.. code-block:: python

    await port.latency_config.offset.set()
    await port.latency_config.offset.get()