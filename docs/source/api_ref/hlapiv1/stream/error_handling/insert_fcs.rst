Insert Frame Checksum
=========================
Whether a valid frame checksum is added to the packets of a stream.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_INSERTFCS`

.. code-block:: python

    # Insert Frame Checksum
    await stream.insert_packets_checksum.set(on_off=enums.OnOff.ON)
    await stream.insert_packets_checksum.set_on()
    await stream.insert_packets_checksum.set(on_off=enums.OnOff.OFF)
    await stream.insert_packets_checksum.set_off()

    resp = await stream.insert_packets_checksum.get()
    resp.on_off
