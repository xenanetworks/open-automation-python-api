Traffic Control
=========================

Rate Percent
------------

.. code-block:: python

    await port.rate.fraction.set()
    await port.rate.fraction.get()


Rate L2 Bits Per Second
-----------------------

.. code-block:: python

    await port.rate.l2_bps.set()
    await port.rate.l2_bps.get()


Rate Frames Per Second
----------------------

.. code-block:: python

    await port.rate.pps.set()
    await port.rate.pps.get()


Start and Stop
----------------

.. code-block:: python

    await port.traffic.state.set_start()
    await port.traffic.state.set_stop()
    await port.traffic.state.get()
    port.on_traffic_change(_callback_func)


Traffic Error
----------------------------

.. code-block:: python

    await port.traffic.error.get()


Single Frame TX
----------------------------

.. code-block:: python

    await port.tx_single_pkt.send.set()


Single Frame Time
----------------------------

.. code-block:: python

    await port.tx_single_pkt.time.get()
