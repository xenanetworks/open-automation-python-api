Error Counter
=========================
Obtains the total number of errors detected across all streams on the port,
including lost packets, misorder events, and payload errors.

.. note::

    FCS errors are included, which will typically lead to double-counting of lost packets.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_ERRORS`

.. code-block:: python

    # Error Counter
    resp = await port.errors_count.get()
    resp.error_count

