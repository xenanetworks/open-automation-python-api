Duplication Scheduling
=========================

Schedule
--------------------------
Configure the impairment scheduler function.  The configuration of the scheduler
depends on the kind of distribution to schedule:

1. Burst distributions: "Fixed Burst" and "Accumulate and Burst".
2. Non-Burst distributions: All others.  For burst distributions, the scheduler can be configured for "One-shot" operation or "Repeat Operation".  When running in "Repeat Operation" the "Repeat Period" must be configured. For non-burst distributions,  the scheduler can be configured operate in either "Continuous" or "Repeat Period" modes. When running in "Repeat Period" configuration of "Duration" and "Repeat Period" is required.

Corresponding CLI command: ``PED_SCHEDULE``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1) # repeat pattern
    await flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0) # continuous

    resp = await flow.impairment_distribution.duplication_type_config.schedule.get()


One-Shot Status
--------------------------
Retrieves the one-shot completion status.

.. note::

    The return value is only valid, if the configured distribution is either accumulate & burst (DELAY) or fixed burst (non-DELAY).

Corresponding CLI command: ``PED_ONESHOTSTATUS``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    resp = await flow.impairment_distribution.duplication_type_config.one_shot_status.get()
    resp.one_shot_status