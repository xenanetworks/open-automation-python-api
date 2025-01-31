MACsec Statistics
======================================

Port TX Statistics
-------------------------

Port-level MACsec TX counters

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TX_STATS`

.. code-block:: python

    resp = await port_obj.statistics.tx.macsec.total.get()


Port TX SC Statistics
-------------------------

SC-level MACsec TX counters.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TXSC_STATS`

.. code-block:: python

    txsc_obj = await port_obj.macsec_txscs.create()
    resp = await txsc_obj.stats.get()


Clear TX Statistics
-------------------------

Clear the MACsec TX counters of the port, including both the port-level and the sc-level counters.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_TX_CLEAR`

.. code-block:: python

    await port_obj.statistics.tx.macsec.clear.set()



Port RX Statistics
-------------------------

Port-level MACsec RX counters

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RX_STATS`

.. code-block:: python

    resp = await port_obj.statistics.rx.macsec.total.get()


Port RX SC Statistics
-------------------------

SC-level MACsec RX counters.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RXSC_STATS`

.. code-block:: python

    rxsc_obj = await port_obj.macsec_rxscs.create()
    resp = await rxsc_obj.stats.get()


Clear RX Statistics
-------------------------

Clear the MACsec RX counters of the port, including both the port-level and the sc-level counters.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RX_CLEAR`

.. code-block:: python

    await port_obj.statistics.rx.macsec.clear.set()