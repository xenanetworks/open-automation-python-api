TX Configuration
=========================

Error Counters
---------------------

.. code-block:: python

    await port.pcs_pma.alarms.errors.get()


Error Generation Rate
---------------------

.. code-block:: python

    await port.pcs_pma.error_gen.error_rate.get()


Error Generation Inject
-----------------------

.. code-block:: python

    await port.pcs_pma.error_gen.inject_one.set()


Error Injection
---------------------

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].tx_error_inject.set_alignerror()
    await port.pcs_pma.lanes[lane_idx].tx_error_inject.set_bip8error()
    await port.pcs_pma.lanes[lane_idx].tx_error_inject.set_headererror()


Lane Configuration
---------------------

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].tx_config.set()
    await port.pcs_pma.lanes[lane_idx].tx_config.get()
