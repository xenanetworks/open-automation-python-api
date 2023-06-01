Link Training
=========================

Settings
-------------------------

.. code-block:: python

    await port.pcs_pma.link_training.settings.set()
    await port.pcs_pma.link_training.settings.get()


Serdes Status
-------------------------

.. code-block:: python

    await port.pcs_pma.link_training.per_lane_status[serdes_idx].get()

