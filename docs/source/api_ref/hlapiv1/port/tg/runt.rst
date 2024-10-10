Runt
=========================

RX Length
---------------
Enable RX runt length detection to flag if packets are seen with length not being I bytes.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_RXRUNTLENGTH`

.. code-block:: python

    # Runt - RX Length
    await port.runt.rx_length.set(runt_length=40)
    
    resp = await port.runt.rx_length.get()
    resp.runt_length


TX Length
---------------
Enable TX runt feature to cut all packets to a number of bytes.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_TXRUNTLENGTH`

.. code-block:: python

    # Runt - TX Length
    await port.runt.tx_length.set(runt_length=40)

    resp = await port.runt.tx_length.get()
    resp.runt_length


Length Error
---------------------
Sticky clear on read: Have packets with wrong runt length been detected since last read?

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_RXRUNTLEN_ERRS`

.. code-block:: python

    # Runt - Length Error
    resp = await port.runt.has_length_errors.get()
    resp.status