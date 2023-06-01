Configuration
=========================

RX Type
-------------------------

.. code-block:: python

    await port.serdes[serdex_idx].prbs.config.rx_type.set()
    await port.serdes[serdex_idx].prbs.config.rx_type.get()

TX Type
-------------------------

.. code-block:: python

    await port.serdes[serdex_idx].prbs.config.tx_type.set()
    await port.serdes[serdex_idx].prbs.config.tx_type.get()

Type
-------------------------

.. code-block:: python

    await port.serdes[serdex_idx].prbs.config.type.set()
    await port.serdes[serdex_idx].prbs.config.type.get()
