Properties
=========================

Description
---------------

.. code-block:: python

    await port.emulation.flows[0].comment.set()
    await port.emulation.flows[0].comment.get()

Initiation
---------------

.. code-block:: python

    await port.emulation.flows[flow_idx].shadow_filter.initiating.set()


Apply
------

.. code-block:: python

    await port.emulation.flows[flow_idx].shadow_filter.apply.set()


Enable
------

.. code-block:: python

    await port.emulation.flows[flow_idx].shadow_filter.enable.set_on()
    await port.emulation.flows[flow_idx].shadow_filter.enable.set_off()
    await port.emulation.flows[flow_idx].shadow_filter.enable.get()

Cancel
------

.. code-block:: python

    await port.emulation.flows[flow_idx].shadow_filter.cancel.set()

Filter Mode
-----------

.. code-block:: python

    await port.emulation.flows[flow_idx].shadow_filter.use_basic_mode()
    await port.emulation.flows[flow_idx].shadow_filter.use_extended_mode()
    await port.emulation.flows[flow_idx].shadow_filter.get_mode()

    await port.emulation.flows[flow_idx].working_filter.get_mode()


