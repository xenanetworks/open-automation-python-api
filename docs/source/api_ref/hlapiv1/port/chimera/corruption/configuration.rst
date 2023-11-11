Corruption Configuration
=========================

Type
-------------------------
Configures impairment corruption type.

.. note::

    IP / TCP / UDP corruption modes are not supported on default flow (0)

Corresponding CLI command: ``PE_CORRUPT``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.corruption.set(corruption_type=enums.CorruptionType.OFF)
    await flow.corruption.set(corruption_type=enums.CorruptionType.ETH)
    await flow.corruption.set(corruption_type=enums.CorruptionType.IP)
    await flow.corruption.set(corruption_type=enums.CorruptionType.TCP)
    await flow.corruption.set(corruption_type=enums.CorruptionType.UDP)
    await flow.corruption.set(corruption_type=enums.CorruptionType.BER)

    resp = await flow.corruption.get()
    resp.corruption_type



