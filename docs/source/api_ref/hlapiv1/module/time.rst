Time and Clock
=========================

Local Clock Adjust
------------------
Makes small adjustments to the local clock of the test module, which drives the
TX rate of the test ports.

Corresponding CLI command: ``M_CLOCKPPB``

.. code-block:: python

    # Local Clock Adjust
    await module.timing.clock_local_adjust.set(ppb=10)
    
    resp = await module.timing.clock_local_adjust.get()
    resp.ppb


Clock Sync Status
----------------------------
Get module's clock sync status.

Corresponding CLI command: ``M_CLOCKSYNCSTATUS``

.. code-block:: python

    # Clock Sync Status
    resp = await module.timing.clock_sync_status.get()
    resp.m_clock_diff
    resp.m_correction
    resp.m_is_steady_state
    resp.m_tune_is_increase
    resp.m_tune_value


Clock Source
----------------------------
Control how the test module timestamp clock is running, either freely in the
chassis or locked to an external system time. Running with free chassis time
allows nano-second precision measurements of latencies, but only when the
transmitting and receiving ports are in the same chassis. Running with locked
external time enables inter-chassis latency measurements, but can introduce
small time discontinuities as the test module time is adjusted.

Corresponding CLI command: ``M_TIMESYNC``

.. code-block:: python

    # Clock Source
    await module.timing.source.set(source=enums.TimingSource.CHASSIS)
    await module.timing.source.set_chassis()
    await module.timing.source.set(source=enums.TimingSource.EXTERNAL)
    await module.timing.source.set_external()
    await module.timing.source.set(source=enums.TimingSource.MODULE)
    await module.timing.source.set_module()

    resp = await module.timing.source.get()
    resp.source


Clock PPM Sweep Configuration
-----------------------------

.. important::

    For Freya modules only

Start and stop deviation sweep the local clock of the test module, which drives the TX rate of the test ports.

The sweep is independent of the M_CLOCKPPB parameter, i.e. the sweep uses the deviation set by M_CLOCKPPB as its zero point.

Corresponding CLI command: ``M_CLOCKPPBSWEEP``

.. code-block:: python

    # Clock PPM Sweep Configuration
    FREYA_MODULES = (modules.MFreya800G4S1P_a, modules.MFreya800G4S1P_b, modules.MFreya800G4S1POSFP_a, modules.MFreya800G4S1POSFP_b)
    if isinstance(module, FREYA_MODULES):
        await module.clock_sweep.config.set(mode=enums.PPMSweepMode.OFF, ppb_step=10, step_delay=10, max_ppb=10, loops=1)
        await module.clock_sweep.config.set(mode=enums.PPMSweepMode.TRIANGLE, ppb_step=10, step_delay=10, max_ppb=10, loops=1)

        resp = await module.clock_sweep.config.get()
        resp.mode
        resp.ppb_step
        resp.step_delay
        resp.max_ppb
        resp.loops


Clock PPM Sweep Status
-----------------------------
Return the current status of the M_CLOCKPPBSWEEP command.

Corresponding CLI command: ``M_CLOCKSWEEPSTATUS``

.. code-block:: python

    # Clock PPM Sweep Status
    if isinstance(module, FREYA_MODULES):
        resp = await module.clock_sweep.status.get()
        resp.curr_step
        resp.curr_sweep
        resp.max_steps
