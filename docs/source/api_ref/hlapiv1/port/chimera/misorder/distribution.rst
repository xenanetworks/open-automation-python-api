Distribution
=========================

Off
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.off.set()
    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.off.get()

Enable
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.enable.set_on()
    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.enable.set_off()
    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.enable.get()

Fixed Rate Distribution
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.fixed_rate.set()
    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.fixed_rate.get()

Fixed Burst Distribution
-------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.fixed_burst.set()
    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.fixed_burst.get()

Scheduling
--------------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.schedule.set()
    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.schedule.get()
    await port.emulation.flows[flow_idx].impairment_distribution.misorder_type_config.one_shot_status.get()