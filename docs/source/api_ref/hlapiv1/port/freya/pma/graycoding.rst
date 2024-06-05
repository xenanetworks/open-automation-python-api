Gray Coding
=========================

Corresponding CLI command: ``PP_GRAYCODING``

.. code-block:: python

    await port.l1.serdes[0].pma.graycoding.set(rx_mode=enums.GrayCodingMode.ON, rx_endianness=enums.Endianness.NORMAL, tx_mode=enums.GrayCodingMode.ON, tx_endianness=enums.Endianness.NORMAL)

    resp = await port.l1.serdes[0].pma.graycoding.get()
    resp.rx_mode
    resp.rx_endianness
    resp.tx_mode
    resp.tx_endianness
