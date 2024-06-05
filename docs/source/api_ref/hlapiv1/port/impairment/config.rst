Impairment Configuration
=========================

Impairment On/OFF
-------------------------
The action determines if emulation functionality is enabled or disabled.

Corresponding CLI command: ``P_EMULATE``

.. code-block:: python

    await port.emulate.set(action=enums.OnOff.ON)
    await port.emulate.set(action=enums.OnOff.OFF)

    resp = await port.emulate.get()
    resp.action


FCS Error Action
-------------------------
The action on packets with FCS errors on a port.

Corresponding CLI command: ``PE_FCSDROP``

.. code-block:: python

    await port.emulation.drop_fcs_errors.set(action=enums.OnOff.ON)
    await port.emulation.drop_fcs_errors.set(action=enums.OnOff.OFF)

    resp = await port.emulation.drop_fcs_errors.get()
    resp.action


TPLD Mode
-------------------------
The action indicates the TPLD mode to be used per port.

Corresponding CLI command: ``PE_TPLDMODE``

.. code-block:: python

    # Set TPLD mode
    await port.emulation.tpld_mode.set(mode=enums.TPLDMode.NORMAL)
    await port.emulation.tpld_mode.set(mode=enums.TPLDMode.MICRO)

    resp = await port.emulation.tpld_mode.get()
    resp.mode
