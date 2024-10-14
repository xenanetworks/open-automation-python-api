Policer
=============================

.. note::

    Applicable to Chimera port only.

Policer Configuration
-----------------------
Configures the bandwidth policer.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_BANDPOLICER`

.. code-block:: python

    # Configure bandwidth control - Policer
    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.bandwidth_control.policer.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L1, cir=10_000, cbs=1_000)
    await flow.bandwidth_control.policer.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L2, cir=10_000, cbs=1_000)

    resp = await flow.bandwidth_control.policer.get()
    resp.on_off
    resp.mode
    resp.cir
    resp.cbs