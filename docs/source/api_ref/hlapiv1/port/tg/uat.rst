Unavailable Time
=========================

Mode
-------------
This command defines if a port is currently used by test suite Xena1564, which means that UAT (UnAvailable Time) will be detected for the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_UAT_MODE`

.. code-block:: python

    await port.uat.mode.set(mode=enums.OnOff.ON, delay=500)
    await port.uat.mode.set(mode=enums.OnOff.OFF, delay=500)
    
    resp = await port.uat.mode.get()
    resp.mode
    resp.delay


Frame Loss Ratio
----------------
This command defines the threshold for the Frame Loss Ratio, where a second is
declared as a Severely Errored Second (SES). In Xena1564 UnAvailable Time
(UAT) is declared after 10 consecutive SES has been detected

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_UAT_FLR`

.. code-block:: python

    resp = await port.uat.frame_loss_ratio.get()
    resp.frame_loss_ratio