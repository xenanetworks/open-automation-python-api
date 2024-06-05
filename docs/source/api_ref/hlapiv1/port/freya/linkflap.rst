Link Flap
=========================

Control
-------------
Enable / disable port 'link flap'.

Corresponding CLI command: ``PP_LINKFLAP_ENABLE``

.. code-block:: python

    # Link Flap - Control
    await port.pcs_pma.link_flap.enable.set(on_off=enums.OnOff.ON)
    await port.pcs_pma.link_flap.enable.set_on()
    await port.pcs_pma.link_flap.enable.set(on_off=enums.OnOff.OFF)
    await port.pcs_pma.link_flap.enable.set_off()

    resp = await port.pcs_pma.link_flap.enable.get()
    resp.on_off


Configuration
-------------
Set port 'link flap' parameters. Notice: Period must be larger than duration.

Corresponding CLI command: ``PP_LINKFLAP_PARAMS``

.. code-block:: python

    # Link Flap - Configuration
    await port.pcs_pma.link_flap.params.set(duration=10, period=20, repetition=0)
    
    resp = await port.pcs_pma.link_flap.params.get()
    resp.duration
    resp.period
    resp.repetition