Auto-Negotiation
=========================

Settings
--------

.. code-block:: python

    await port.pcs_pma.auto_neg.settings.get()

Status
--------

.. code-block:: python

    await port.pcs_pma.auto_neg.status.get()


Selection
----------

.. note::
    
    Only applicable to RJ45 ports

.. code-block:: python

    await port.autoneg_selection.set_on()
    await port.autoneg_selection.set_off()
    await port.autoneg_selection.get()

