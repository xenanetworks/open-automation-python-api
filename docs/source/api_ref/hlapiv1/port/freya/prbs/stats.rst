Statistics
=========================
Statistics about PRBS pattern detection on the data received on a specified
SerDes.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_RXPRBSSTATUS`

.. code-block:: python

    # PRBS Statistics
    resp = await port.l1.serdes[0].prbs.status.get()
    resp.byte_count
    resp.error_count
    resp.lock