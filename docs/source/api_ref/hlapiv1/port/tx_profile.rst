TX Profile
=========================


TPLD Mode
-----------

.. code-block:: python

    await port.tpld_mode.set_normal()
    await port.tpld_mode.set_micro()
    await port.tpld_mode.get()


TX Mode
-----------

.. code-block:: python

    await port.tx_config.mode.set_normal()
    await port.tx_config.mode.set_burst()
    await port.tx_config.mode.set_sequential()
    await port.tx_config.mode.set_strictuniform()
    await port.tx_config.mode.get()


Burst Period
------------

.. code-block:: python

    await port.tx_config.burst_period.set()
    await port.tx_config.burst_period.get()


TX Delay
------------

.. code-block:: python

    await port.tx_config.delay.set()
    await port.tx_config.delay.get()


TX Enable
------------

.. code-block:: python

    await port.tx_config.enable.set()
    await port.tx_config.enable.get()


Packet Limit
------------

.. code-block:: python

    await port.tx_config.packet_limit.set()
    await port.tx_config.packet_limit.get()


Time Limit
------------

.. code-block:: python

    await port.tx_config.time_limit.set()
    await port.tx_config.time_limit.get()


TX Time Elapsed
---------------

.. code-block:: python

    await port.tx_config.time.get()


Prepare TX
------------

.. code-block:: python

    await port.tx_config.prepare.set()


Dynamic TX Rate
---------------

.. code-block:: python
    
    await port.dynamic.set_off()
    await port.dynamic.set_on()
    await port.dynamic.get()

    port.on_dynamic_change(_callback_func)