MACsec on Stream
======================================

Enable MACsec on Stream
-------------------------

Enable or disable MACsec on the stream.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_MACSEC_ENABLE`

.. code-block:: python

    await stream_obj.macsec.enable.set(on_off=enums.OnOff.ON)
    await stream_obj.macsec.enable.set(on_off=enums.OnOff.OFF)

    resp = await stream_obj.macsec.enable.get()
    resp.on_off


Assign TX SC to Stream
-------------------------

Assign a TX SC to a stream.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_MACSEC_ASSIGN`

.. code-block:: python

    await stream_obj.macsec.assign.set(tx_sc_index=txsc_id)

    resp = await stream_obj.macsec.assign.get()
    resp.tx_sc_index
