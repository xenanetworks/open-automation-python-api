Tap Configuration
=========================


TX Tap Autotune
-------------------------

.. code-block:: python

    await port.serdes[serdex_idx].phy.autotune.set_on()
    await port.serdes[serdex_idx].phy.autotune.set_off()
    await port.serdes[serdex_idx].phy.autotune.get()


TX Tap Retune
-------------------------

.. code-block:: python

    await port.serdes[serdex_idx].phy.retune.set()


TX Tap Configuration
-------------------------

.. code-block:: python

    await port.serdes[serdex_idx].phy.tx_equalizer.set()
    await port.serdes[serdex_idx].phy.tx_equalizer.get()


RX Tap Configuration
-------------------------

.. code-block:: python

    await port.serdes[serdex_idx].phy.rx_equalizer.set()
    await port.serdes[serdex_idx].phy.rx_equalizer.get()
