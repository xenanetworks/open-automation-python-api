Corruption Distribution
=========================

Enable/Disable
-----------------------

Control whether this impairment distribution is enabled.

.. note::

    This command is not applicable for PE_BANDPOLICER and PE_BANDSHAPER because they have a separate ``ON / OFF`` parameter.

Corresponding CLI command: ``PED_ENABLE``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.enable.set(action=enums.OnOff.ON)
    await flow.impairment_distribution.corruption_type_config.enable.set_on()
    await flow.impairment_distribution.corruption_type_config.enable.set(action=enums.OnOff.OFF)
    await flow.impairment_distribution.corruption_type_config.enable.set_off()

    resp = await flow.impairment_distribution.corruption_type_config.off.get()
    resp.action

Off Distribution
-----------------------

Configure Impairments Distribution to OFF. Assigning a different distribution than OFF to an impairment
will activate the impairment. To de-activate the impairment assign distribution OFF.

Corresponding CLI command: ``PED_OFF``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.off.set()

    resp = await flow.impairment_distribution.corruption_type_config.off.get()
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
    await flow.impairment_distribution.corruption_type_config.fixed_rate.set(probability=10_000)

    resp = await flow.impairment_distribution.corruption_type_config.fixed_rate.get()
    resp.probability

Random Rate Distribution
------------------------
Configuration of Random Rate distribution. Packets are impaired randomly based
on a per packet probability. This way the impaired fraction of packets will be
equal to the configured probability over time. Random probability in ppm (i.e. 1
means 0.0001%)

Corresponding CLI command: ``PED_RANDOM``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.random_rate.set(probability=10_000)

    resp = await flow.impairment_distribution.corruption_type_config.random_rate.get()
    resp.probability

Bit Error Rate Distribution
---------------------------
Configuration of Bit Error Rate distribution.

Corresponding CLI command: ``PED_BER``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.bit_error_rate.set(coef=1, exp=1)

    resp = await flow.impairment_distribution.corruption_type_config.bit_error_rate.get()
    resp.coef
    resp.exp

Fixed Burst Distribution
-------------------------
Configuration of Fixed Burst distribution.

Corresponding CLI command: ``PED_FIXEDBURST``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.fixed_burst.set(burst_size=1300)

    resp = await flow.impairment_distribution.corruption_type_config.fixed_burst.get()
    resp.burst_size
    
Random Burst Distribution
--------------------------
Configuration of Random Burst distribution.

Corresponding CLI command: ``PED_RANDOMBURST``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.random_burst.set(minimum=1, maximum=10, probability=10_000)

    resp = await flow.impairment_distribution.corruption_type_config.random_burst.get()
    resp.minimum
    resp.maximum
    resp.probability

Gilbert Elliott Distribution
----------------------------
Configuration of Gilbert-Elliot distribution.

Corresponding CLI command: ``PED_GE``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.ge.set(good_state_prob=0, good_state_trans_prob=0, bad_state_prob=0, bad_state_trans_prob=0)

    resp = await flow.impairment_distribution.corruption_type_config.ge.get()
    resp.good_state_prob
    resp.good_state_trans_prob
    resp.bad_state_prob
    resp.bad_state_trans_prob

Uniform Distribution
--------------------------
Configuration of Uniform distribution.

.. note::

    If minimum is less than minimum latency, value is set to minimum latency. If minimum is greater than maximum latency, value is set to maximum latency.

Corresponding CLI command: ``PED_UNI``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.uniform.set(minimum=1, maximum=1)

    resp = await flow.impairment_distribution.corruption_type_config.uniform.get()
    resp.minimum
    resp.maximum
    
Gaussian Distribution
--------------------------
Configuration of Gaussian distribution.

.. note::

    In case of ``_impairment_type_xindex != DELAY``:
        (1) mean plus 3 times standard deviation should be less than or equal to max allowed (4194288).
        (2) mean should always be at least 3 times the standard deviation, this to ensure that the impairment distance is always positive.

    In case of ``_impairment_type_xindex = DELAY``:
        (1) mean plus 3 times standard deviation should be less than or equal to the maximum latency.
        (2) mean minus 3 times the standard deviation should be greater than or equal to minimum latency.

Corresponding CLI command: ``PED_GAUSS``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.gaussian.set(mean=1, std_deviation=1)

    resp = await flow.impairment_distribution.corruption_type_config.gaussian.get()
    resp.mean
    resp.std_deviation

Poisson Distribution
--------------------------
Configuration of "Poisson" distribution.

.. note::

    Standard deviation is derived from mean, i.e., standard deviation = SQRT(mean).

    In case of ``_impairment_type_xindex != DELAY``, mean plus 3 times standard deviation should be less than or equal to max allowed (4194288).

    In case of ``_impairment_type_xindex = DELAY``, mean plus 3 times standard deviation should be less than or equal to the maximum latency.

Corresponding CLI command: ``PED_POISSON``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.poisson.set(mean=100)

    resp = await flow.impairment_distribution.corruption_type_config.poisson.get()
    resp.mean

Gamma Distribution
--------------------------
Configuration of Gamma distribution.

.. note::

    Mean and Standard deviation are calculated from Shape and Scale parameters and validation is performed using those.
    standard deviation = [SQRT(shape * scale * scale)]mean = [shape * scale].

    In case of ``_impairment_type_xindex != DELAY``,
    (1) mean plus 4 times standard deviation should be less than or equal to max allowed(4194288).
    (2)shape and scale should be greater than or equal to 0.

    In case of ``_impairment_type_xindex = DELAY``, mean plus 4 times standard deviation should be less than or equal to the maximum latency.

Corresponding CLI command: ``PED_GAMMA``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.gamma.set(shape=1, scale=1)

    resp = await flow.impairment_distribution.corruption_type_config.gamma.get()
    resp.shape
    resp.scale
    
Custom Distribution
--------------------------
Associate a custom distribution to a flow and impairment type.

.. note::

    Before associating a custom distribution, the below validation checks are applied.

    In case of ``_impairment_type_xindex != DELAY``,
    (1) Custom values should be less than or equal to max allowed (4194288).
    (2) Custom distribution bust contain 512 values.

    In case of ``_impairment_type_xindex = DELAY``,
    (1) Custom values should be less than or equal to the maximum latency.
    (2) Custom values should be greater than or equal to minimum latency.
    (3) Custom distribution should contain 1024 values.

Corresponding CLI command: ``PED_CUST``

.. code-block:: python

    # Custom distribution for impairment Corruption
    flow = port.emulation.flows[1] # e.g. flow_id = 1
    data_x=[0, 1] * 256
    await port.custom_distributions.assign(0)
    await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
    await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
    await flow.impairment_distribution.corruption_type_config.custom.set(cust_id=0)

    resp = await flow.impairment_distribution.corruption_type_config.custom.get()
    resp.cust_id


Scheduling
--------------------------
Configure the impairment scheduler function.  The configuration of the scheduler
depends on the kind of distribution to schedule:

1. Burst distributions: "Fixed Burst" and "Accumulate and Burst".
2. Non-Burst distributions: All others.  For burst distributions, the scheduler can be configured for "One-shot" operation or "Repeat Operation".  When running in "Repeat Operation" the "Repeat Period" must be configured. For non-burst distributions,  the scheduler can be configured operate in either "Continuous" or "Repeat Period" modes. When running in "Repeat Period" configuration of "Duration" and "Repeat Period" is required.

Corresponding CLI command: ``PED_SCHEDULE``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1) # repeat pattern
    await flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0) # continuous

    resp = await flow.impairment_distribution.corruption_type_config.schedule.get()

    await flow.impairment_distribution.corruption_type_config.one_shot_status.get()