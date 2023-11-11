Statistics
=========================
Statistics about PRBS pattern detection on the data received on a specified
SerDes.

Corresponding CLI command: ``PP_RXPRBSSTATUS``

.. code-block:: python

    # PRBS Statistics
    resp = await port.serdes[0].prbs.status.get()
    resp.byte_count
    resp.error_count
    resp.lock