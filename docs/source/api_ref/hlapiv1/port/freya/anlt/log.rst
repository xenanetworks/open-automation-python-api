Log
===========================

Get ANLT log trace. The log trace is a JSON string.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_LOG`

.. code-block:: python

    resp = await port.l1.anlt.log.get()
    resp.log_string