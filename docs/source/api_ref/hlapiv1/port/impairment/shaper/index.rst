Shaper
=============================

.. note::

    Applicable to Chimera port only.

Shaper Configuration
-----------------------
Configures the bandwidth shaper. L1 (0) (Shaper performed at Layer 1 level. I.e. including the preamble and min interpacket gap) L2 (1) (Shaper performed at Layer 2 level. I.e. excluding the preamble and min interpacket gap) Default value: L2 (0)

Corresponding CLI command: ``PE_BANDSHAPER``

.. code-block:: python
    
    # Configure bandwidth control - Shaper
    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.bandwidth_control.shaper.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L1, cir=10_000, cbs=1_000, buffer_size=1_000)
    await flow.bandwidth_control.shaper.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L2, cir=10_000, cbs=1_000, buffer_size=1_000)

    resp = await flow.bandwidth_control.shaper.get()
    resp.on_off
    resp.mode
    resp.cir
    resp.cbs
    resp.buffer_size