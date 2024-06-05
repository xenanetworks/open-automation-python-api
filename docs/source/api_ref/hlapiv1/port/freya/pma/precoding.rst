Precoding
=========================

Corresponding CLI command: ``PP_PRECODING``

.. code-block:: python

    await port.l1.serdes[0].pma.precoding.set(rx_mode=enums.PreCodingMode.ON, rx_endianness=enums.Endianness.NORMAL,tx_mode=enums.PreCodingMode.ON, tx_endianness=enums.Endianness.NORMAL)

    resp = await port.l1.serdes[0].pma.precoding.get()
    resp.rx_mode
    resp.rx_endianness
    resp.tx_mode
    resp.tx_endianness