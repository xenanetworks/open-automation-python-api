Impairment
=========================

.. note::

    For Chimera module only.


Bypass Mode
--------------------

.. code-block:: python

    await module.emulator_bypass_mode.set_on()
    await module.emulator_bypass_mode.set_off()
    await module.emulator_bypass_mode.get()


Latency Mode
--------------------

.. code-block:: python

    await module.latency_mode.set_normal()
    await module.latency_mode.set_extended()
    await module.latency_mode.get()


TX Clock Source
--------------------

.. code-block:: python

    await module.tx_clock.source.set_modulelocalclock()
    await module.tx_clock.source.set_p0rxclk()
    await module.tx_clock.source.set_p1rxclk()
    await module.tx_clock.source.set_p2rxclk()
    await module.tx_clock.source.set_p3rxclk()
    await module.tx_clock.source.set_p4rxclk()
    await module.tx_clock.source.set_p5rxclk()
    await module.tx_clock.source.set_p6rxclk()
    await module.tx_clock.source.set_p7rxclk()
    await module.tx_clock.source.get()


TX Clock Status
----------------------------

.. code-block:: python

    await module.tx_clock.status.get()