Misorder Configuration
=========================

Misorder Depth
---------------

Configures the misordering depth in number of packets.

.. note::

    probability * (depth + 1) should be less than 1,000,000. (see PED_FIXED)

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_MISORDER`

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.misordering.set(depth=1)

    resp = await flow.misordering.get()
    resp.depth



