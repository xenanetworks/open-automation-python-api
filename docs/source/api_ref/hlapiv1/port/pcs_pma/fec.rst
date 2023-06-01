Forward Error Correction
=========================

FEC Mode
--------

.. code-block:: python

    await port.pcs_pma.phy.auto_neg.set()
    await port.fec_mode.set()
    await port.fec_mode.get()
