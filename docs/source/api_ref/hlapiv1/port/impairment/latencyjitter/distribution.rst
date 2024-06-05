Latency & Jitter Distribution
=============================

Enable/Disable
-----------------------

Control whether this impairment distribution is enabled.

.. note::

    This command is not applicable for PE_BANDPOLICER and PE_BANDSHAPER because they have a separate ``ON / OFF`` parameter.

Corresponding CLI command: ``PED_ENABLE``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.latency_jitter_type_config.enable.set(action=enums.OnOff.ON)
    await flow.impairment_distribution.latency_jitter_type_config.enable.set_on()
    await flow.impairment_distribution.latency_jitter_type_config.enable.set(action=enums.OnOff.OFF)
    await flow.impairment_distribution.latency_jitter_type_config.enable.set_off()

    resp = await flow.impairment_distribution.latency_jitter_type_config.off.get()
    resp.action

Off Distribution
-----------------------

Configure Impairments Distribution to OFF. Assigning a different distribution than OFF to an impairment
will activate the impairment. To de-activate the impairment assign distribution OFF.

Corresponding CLI command: ``PED_OFF``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.latency_jitter_type_config.off.set()

    resp = await flow.impairment_distribution.latency_jitter_type_config.off.get()
    resp.action

Constant
-----------------------
Configuration of Constant Delay distribution (DELAY only). Unit is ns (must be
multiples of 100ns). Default value: Minimum supported per speed and FEC mode.

.. note::

    If the latency is less than minimum latency, value is set to minimum latency. If the latency is greater than maximum latency, value is set to maximum latency.
    
Corresponding CLI command: ``PED_CONST``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.latency_jitter_type_config.constant_delay.set(delay=100)

    resp = await flow.impairment_distribution.latency_jitter_type_config.constant_delay.get()
    resp.delay

Accumulative Burst Distribution
-------------------------------
Configuration of Accumulate & Burst distribution (DELAY only).

.. note::

    If the delay is less than minimum latency, value is set to minimum latency. If the delay is greater than maximum latency, value is set to maximum latency.

Corresponding CLI command: ``PED_ACCBURST``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.latency_jitter_type_config.accumulate_and_burst.set(delay=1300)

    resp = await flow.impairment_distribution.latency_jitter_type_config.accumulate_and_burst.get()
    resp.delay

Step Distribution
---------------------------
Configuration of Step distribution (DELAY only).

.. note::

    If the low/high is less than minimum latency, value is set to minimum latency. If the low/high is greater than maximum latency, value is set to maximum latency.


Corresponding CLI command: ``PED_STEP``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.latency_jitter_type_config.step.set(low=1300, high=77000)

    resp = await flow.impairment_distribution.latency_jitter_type_config.step.get()
    resp.low
    resp.high

Uniform Distribution
--------------------------
Configuration of Uniform distribution.

.. note::

    If minimum is less than minimum, value is set to minimum. If minimum is greater than maximum, value is set to maximum.

Corresponding CLI command: ``PED_UNI``

.. code-block:: python

    flow = port.emulation.flows[1] # e.g. flow_id = 1
    await flow.impairment_distribution.latency_jitter_type_config.uniform.set(minimum=1, maximum=1)

    resp = await flow.impairment_distribution.latency_jitter_type_config.uniform.get()
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
    await flow.impairment_distribution.latency_jitter_type_config.gaussian.set(mean=1, std_deviation=1)

    resp = await flow.impairment_distribution.latency_jitter_type_config.gaussian.get()
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
    await flow.impairment_distribution.latency_jitter_type_config.poisson.set(mean=100)

    resp = await flow.impairment_distribution.latency_jitter_type_config.poisson.get()
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
    await flow.impairment_distribution.latency_jitter_type_config.gamma.set(shape=1, scale=1)

    resp = await flow.impairment_distribution.latency_jitter_type_config.gamma.get()
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
    await flow.impairment_distribution.latency_jitter_type_config.custom.set(cust_id=0)

    resp = await flow.impairment_distribution.latency_jitter_type_config.custom.get()
    resp.cust_id
