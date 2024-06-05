Misorder Distribution
=========================

Enable/Disable
-----------------------

Control whether this impairment distribution is enabled.

.. note::

    This command is not applicable for PE_BANDPOLICER and PE_BANDSHAPER because they have a separate ``ON / OFF`` parameter.

Corresponding CLI command: ``PED_ENABLE``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.misorder_type_config.enable.set(action=enums.OnOff.ON)
    await flow.impairment_distribution.misorder_type_config.enable.set_on()
    await flow.impairment_distribution.misorder_type_config.enable.set(action=enums.OnOff.OFF)
    await flow.impairment_distribution.misorder_type_config.enable.set_off()

    resp = await flow.impairment_distribution.misorder_type_config.off.get()
    resp.action

Off Distribution
-----------------------

Configure Impairments Distribution to OFF. Assigning a different distribution than OFF to an impairment
will activate the impairment. To de-activate the impairment assign distribution OFF.

Corresponding CLI command: ``PED_OFF``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.misorder_type_config.off.set()

    resp = await flow.impairment_distribution.misorder_type_config.off.get()
    resp.action


Fixed Rate Distribution
-----------------------
Configuration of Fixed Rate distribution. This is predictable distribution with
nearly equal distance between impairments, to match the configured probability.

.. note::

    In case of misordering, a special limit applies, probability * (depth + 1) should be less than 1000000.

Corresponding CLI command: ``PED_FIXED``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.misorder_type_config.fixed_rate.set(probability=10_000)

    resp = await flow.impairment_distribution.misorder_type_config.fixed_rate.get()
    resp.probability

Fixed Burst Distribution
-------------------------
Configuration of Fixed Burst distribution.

Corresponding CLI command: ``PED_FIXEDBURST``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.misorder_type_config.fixed_burst.set(burst_size=1300)

    resp = await flow.impairment_distribution.misorder_type_config.fixed_burst.get()
    resp.burst_size
