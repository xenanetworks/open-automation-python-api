Preamble
=========================


RX Preamble Insert
------------------

.. code-block:: python

    await port.preamble.rx_insert.set()
    await port.preamble.rx_insert.get()


TX Preamble Removal
-------------------

.. code-block:: python
    
    await port.preamble.tx_remove.set()
    await port.preamble.tx_remove.get()