Distribution
=========================

Off
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.off.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.off.get()

Enable
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.enable.set_on()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.enable.set_off()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.enable.get()

Fixed Rate Distribution
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.fixed_rate.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.fixed_rate.get()

Random Rate Distribution
------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.random_rate.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.random_rate.get()

Bit Error Rate Distribution
---------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.bit_error_rate.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.bit_error_rate.get()

Fixed Burst Distribution
-------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.fixed_burst.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.fixed_burst.get()
    
Random Burst Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.random_burst.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.random_burst.get()

Gilbert Elliott Distribution
----------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.ge.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.ge.get()

Uniform Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.uniform.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.uniform.get()
    
Gaussian Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.gaussian.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.gaussian.get()

Poisson Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.poisson.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.poisson.get()

Gamma Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.gamma.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.gamma.get()
    
Custom Distribution
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.custom.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.custom.get()

Scheduling
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.schedule.set()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.schedule.get()
    await port.emulation.flows[flow_idx].impairment_distribution.drop_type_config.one_shot_status.get()