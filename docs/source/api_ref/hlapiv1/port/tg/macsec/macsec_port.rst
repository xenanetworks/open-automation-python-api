MACsec on Port
======================================

Enable MACsec on RX Port
-------------------------

This will enable/disable the MACSec functionality on the RX side. With it ON, the RX port will try to decode the received packets. If it is OFF, the port will not try to decode any received packets.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MACSEC_RX_ENABLE`

.. code-block:: python

    await port_obj.macsec_rx.set(on_off=enums.OnOff.ON)
    await port_obj.macsec_rx.set(on_off=enums.OnOff.OFF)

    resp = await port_obj.macsec_rx.get()
    resp.on_off

