Control
=======

Controls the PRBS mode of the interface.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_TXPRBSCONFIG`

.. code-block:: python

    await port.l1.serdes[0].prbs.control.set(prbs_seed=0, prbs_on_off=enums.PRBSOnOff.PRBSON, error_on_off=enums.ErrorOnOff.ERRORSOFF)
            
    await port.l1.serdes[0].prbs.control.set(prbs_seed=0, prbs_on_off=enums.PRBSOnOff.PRBSOFF, error_on_off=enums.ErrorOnOff.ERRORSOFF)