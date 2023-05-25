Time and Clock
=========================

Local Clock Adjust
------------------

.. code-block:: python

    await module.timing.clock_local_adjust.set()
    await module.timing.clock_local_adjust.get()


Clock Sync Status
----------------------------

.. code-block:: python

    await module.timing.clock_sync_status.get()


Clock Source
----------------------------

.. code-block:: python

    await module.timing.source.set_chassis()
    await module.timing.source.set_external()
    await module.timing.source.set_module()
    await module.timing.source.get()


Clock PPM Sweep Configuration
-----------------------------

.. code-block:: python

    await module.clock_sweep.config.set()
    await module.clock_sweep.config.get()


Clock PPM Sweep Status
-----------------------------

.. code-block:: python

    await module.clock_sweep.status.get()
