Distribution
=========================

Off
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.off.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.off.get()

Enable
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.enable.set_on()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.enable.set_off()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.enable.get()

Constant
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.constant_delay.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.constant_delay.get()

Accumulative Burst Distribution
-------------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.accumulate_and_burst.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.accumulate_and_burst.get()

Step Distribution
---------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.step.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.step.get()

Uniform Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.uniform.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.uniform.get()
    
Gaussian Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.gaussian.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.gaussian.get()

Poisson Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.poisson.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.poisson.get()

Gamma Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.gamma.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.gamma.get()
    
Custom Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.custom.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.custom.get()

Scheduling
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.schedule.set()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.schedule.get()
    await port.emulation.flows[flow_idx].impairment_distribution.latency_jitter_type_config.one_shot_status.get()