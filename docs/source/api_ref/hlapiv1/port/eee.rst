Energy Efficiency Ethernet
==========================


Capabilities
------------

.. code-block:: python

    await port.eee.capabilities.get()


Partner Capabilities
--------------------

.. code-block:: python

    await port.eee.partner_capabilities.get()


Control
------------

.. code-block:: python

    await port.eee.enable.set_off()
    await port.eee.enable.set_on()
    await port.eee.enable.get()


Low Power TX Mode
-----------------

.. code-block:: python

    await port.eee.mode.set_off()
    await port.eee.mode.set_on()
    await port.eee.mode.get()


RX Power
------------

.. code-block:: python

    await port.eee.rx_power.get()


SNR Margin
------------

.. code-block:: python

    await port.eee.snr_margin.get()


Status
------------

.. code-block:: python

    await port.eee.status.get()

