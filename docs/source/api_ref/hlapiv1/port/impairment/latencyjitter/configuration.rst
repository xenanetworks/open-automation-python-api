Latency & Jitter Configuration
==============================

Latency Range
--------------

Retrieve minimum and maximum configurable latency per flow in nanoseconds.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_LATENCYRANGE`

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    resp = await flow.latency_range.get()
    resp.min
    resp.max



