FEC Mode
=========================

FEC mode for port that supports FEC.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_FECMODE`

.. code-block:: python

    # FEC Mode
    await port.fec_mode.set(mode=enums.FECMode.RS_FEC)
    await port.fec_mode.set(mode=enums.FECMode.RS_FEC_KP)
    await port.fec_mode.set(mode=enums.FECMode.RS_FEC_KR)
    await port.fec_mode.set(mode=enums.FECMode.FC_FEC)
    await port.fec_mode.set(mode=enums.FECMode.OFF)
    await port.fec_mode.set(mode=enums.FECMode.ON)

    resp = await port.fec_mode.get()
    resp.mode
