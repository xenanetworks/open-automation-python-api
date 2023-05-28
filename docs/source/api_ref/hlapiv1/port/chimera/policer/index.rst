Policer
=============================

.. note::

    Applicable to Chimera port only.

Configuration
-----------------------

.. code-block:: python

    await port.emulation.flows[flow_idx].bandwidth_control.policer.set()
    await port.emulation.flows[flow_idx].bandwidth_control.policer.get()