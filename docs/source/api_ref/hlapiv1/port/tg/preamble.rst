Preamble
=========================


RX Preamble Insert
------------------
Insert preambles to the incoming frames.

Corresponding CLI command: ``P_RXPREAMBLE_INSERT``

.. code-block:: python

    # RX Preamble Insert
    await port.preamble.rx_insert.set(on_off=enums.OnOff.ON)
    await port.preamble.rx_insert.set(on_off=enums.OnOff.OFF)

    resp = await port.preamble.rx_insert.get()
    resp.on_off


TX Preamble Removal
-------------------
Remove preamble from outgoing frames.

Corresponding CLI command: ``P_TXPREAMBLE_REMOVE``

.. code-block:: python
    
    # TX Preamble Removal   
    await port.preamble.tx_remove.set(on_off=enums.OnOff.ON)
    await port.preamble.tx_remove.set(on_off=enums.OnOff.OFF)

    resp = await port.preamble.tx_remove.get()
    resp.on_off