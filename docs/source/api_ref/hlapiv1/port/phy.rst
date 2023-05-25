PHY
=========================

Signal Status
-------------------------

.. code-block:: python

    await port.pcs_pma.phy.signal_status.get()


Settings
-------------------------

.. code-block:: python

    await port.pcs_pma.phy.settings.set()
    await port.pcs_pma.phy.settings.get()


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


Eye Diagram
-------------------------

Information
^^^^^^^^^^^^^^

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.info.get()


Bit Error Rate
^^^^^^^^^^^^^^

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.ber.get()


Dwell Bits
^^^^^^^^^^^^^^

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.dwell_bits.get()


Measure
^^^^^^^^^^^^^^

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.measure.get()


Resolution
^^^^^^^^^^^^^^

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.resolution.get()


Data Columns
^^^^^^^^^^^^^^

.. code-block:: python

    await port.serdes[serdex_idx].eye_diagram.read_column