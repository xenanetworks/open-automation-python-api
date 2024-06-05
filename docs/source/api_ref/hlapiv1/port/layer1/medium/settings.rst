Settings and Status
=========================

Signal Status
-------------------------
Obtain the PHY signal status.

Corresponding CLI command: ``PP_PHYSIGNALSTATUS``

.. code-block:: python

    # PHY - Signal Status
    resp = await port.pcs_pma.phy.signal_status.get()
    resp.phy_signal_status


Settings
-------------------------
Get/Set low-level PHY settings.

Corresponding CLI command: ``PP_PHYSETTINGS``

.. code-block:: python

    # PHY - Settings
    await port.pcs_pma.phy.settings.set(
        link_training_on_off=enums.OnOff.ON, 
        precode_on_off=enums.OnOffDefault.DEFAULT, 
        graycode_on_off=enums.OnOff.OFF, pam4_msb_lsb_swap=enums.OnOff.OFF)
    
    resp = await port.pcs_pma.phy.settings.get()
    resp.link_training_on_off
    resp.precode_on_off
    resp.graycode_on_off
    resp.pam4_msb_lsb_swap

