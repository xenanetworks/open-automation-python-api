Impairment Configuration
=========================

Impairment On/OFF
-------------------------
The action determines if emulation functionality is enabled or disabled.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_EMULATE`

.. code-block:: python

    await port.emulate.set(action=enums.OnOff.ON)
    await port.emulate.set(action=enums.OnOff.OFF)

    resp = await port.emulate.get()
    resp.action


FCS Error Action
-------------------------
The action on packets with FCS errors on a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_FCSDROP`

.. code-block:: python

    await port.emulation.drop_fcs_errors.set(action=enums.OnOff.ON)
    await port.emulation.drop_fcs_errors.set(action=enums.OnOff.OFF)

    resp = await port.emulation.drop_fcs_errors.get()
    resp.action


TPLD Mode
-------------------------
The action indicates the TPLD mode to be used per port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_TPLDMODE`

.. code-block:: python

    # Set TPLD mode
    await port.emulation.tpld_mode.set(mode=enums.TPLDMode.NORMAL)
    await port.emulation.tpld_mode.set(mode=enums.TPLDMode.MICRO)

    resp = await port.emulation.tpld_mode.get()
    resp.mode
