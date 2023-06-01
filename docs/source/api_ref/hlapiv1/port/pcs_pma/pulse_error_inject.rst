PMA Pulse Error Inject
=========================

Control
--------

.. code-block:: python

    await port.pcs_pma.pma_pulse_err_inj.enable.set_on()
    await port.pcs_pma.pma_pulse_err_inj.enable.set_off()
    await port.pcs_pma.pma_pulse_err_inj.enable.get()


Configuration
--------------

.. code-block:: python

    await port.pcs_pma.pma_pulse_err_inj.params.set()
    await port.pcs_pma.pma_pulse_err_inj.params.get()