PMA Pulse Error Inject
=========================

Control
--------
Enable / disable 'PMA pulse error inject'.

Corresponding CLI command: ``PP_PMAERRPUL_ENABLE``

.. code-block:: python

    # PMA Pulse Error Inject Control
    await port.pcs_pma.pma_pulse_err_inj.enable.set(on_off=enums.OnOff.ON)
    await port.pcs_pma.pma_pulse_err_inj.enable.set_on()
    await port.pcs_pma.pma_pulse_err_inj.enable.set(on_off=enums.OnOff.OFF)
    await port.pcs_pma.pma_pulse_err_inj.enable.set_off()

    resp = await port.pcs_pma.pma_pulse_err_inj.enable.get()
    resp.on_off


Configuration
--------------
The 'PMA pulse error inject'.

.. note::

    Period must be > duration. BER will be: coeff * 10exp

Corresponding CLI command: ``PP_PMAERRPUL_PARAMS``

.. code-block:: python

    # PMA Pulse Error Inject Configuration
    await port.pcs_pma.pma_pulse_err_inj.params.set(duration=1000, period=1000, repetition=10, coeff=5, exp=-5)
    
    resp = await port.pcs_pma.pma_pulse_err_inj.params.get()
    resp.duration
    resp.period
    resp.coeff
    resp.exp