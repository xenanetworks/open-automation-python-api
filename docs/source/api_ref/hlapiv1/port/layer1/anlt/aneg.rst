Auto-Negotiation
=========================

Configuration
--------------
Auto-negotiation configuration.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_AUTONEG`

.. code-block:: python

    # Auto-Negotiation Settings
    resp = await port.pcs_pma.auto_neg.settings.get()
    resp.tec_ability
    resp.fec_capable
    resp.fec_requested
    resp.pause_mode

Status
--------
Status of auto-negotiation.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_AUTONEGSTATUS`

.. code-block:: python

    a# Auto-Negotiation Status
    resp = await port.pcs_pma.auto_neg.status.get()
    resp.mode
    resp.auto_state
    resp.tec_ability
    resp.fec_capable
    resp.fec_requested
    resp.fec
    resp.pause_mode


Selection
----------
Whether the port responds to incoming auto-negotiation requests.

.. note::
    
    Only applicable to RJ45 ports

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_AUTONEGSELECTION`

.. code-block:: python

    # Auto-Negotiation Selection
    # Only applicable to RJ45 ports
    await port.autoneg_selection.set(on_off=enums.OnOff.ON)
    await port.autoneg_selection.set_on()
    await port.autoneg_selection.set(on_off=enums.OnOff.OFF)
    await port.autoneg_selection.set_off()

    resp = await port.autoneg_selection.get()
    resp.on_off

