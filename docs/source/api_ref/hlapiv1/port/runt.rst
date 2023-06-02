Runt
=========================

RX Length
---------------

.. code-block:: python

    await port.runt.rx_length.set()
    await port.runt.rx_length.get()


TX Length
---------------

.. code-block:: python

    await port.runt.tx_length.set()
    await port.runt.tx_length.get()


Length Error
---------------------

.. code-block:: python

    await port.runt.has_length_errors.get()