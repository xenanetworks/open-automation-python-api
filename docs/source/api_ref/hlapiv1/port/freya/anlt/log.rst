Log
===========================

Get ANLT log trace. The log trace is a JSON string.

.. code-block:: python

    resp = await port.l1.anlt.log.get()
    resp.log_string