Latency & Jitter Configuration
==============================

Latency Range
--------------

Retrieve minimum and maximum configurable latency per flow in nanoseconds.

Corresponding CLI command: ``PE_LATENCYRANGE``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    resp = await flow.latency_range.get()
    resp.min
    resp.max



