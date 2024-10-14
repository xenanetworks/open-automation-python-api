TX Statistics
=========================

Clear Counter
-------------
Clear all the transmit statistics for a port. The byte and packet counts will
restart at zero.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pt_commands.PT_CLEAR`

.. code-block:: python

    # TX Statistics - Clear Counter
    await port.statistics.tx.clear.set()


Total Counter
--------------
Obtains statistics concerning all the packets transmitted on a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pt_commands.PT_TOTAL`

.. code-block:: python

    # TX Statistics - Total Counter
    resp = await port.statistics.tx.total.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


Non-TPLD Counter
-----------------
Obtains statistics concerning the packets without a test payload transmitted on
a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pt_commands.PT_NOTPLD`

.. code-block:: python

    # TX Statistics - Non-TPLD Counter
    resp = await port.statistics.tx.no_tpld.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


Extra Counter
-------------
Obtains additional statistics for packets transmitted on a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pt_commands.PT_EXTRA`

.. code-block:: python

    # TX Statistics - Extra Counter
    resp = await port.statistics.tx.extra.get()
    resp.tx_arp_req_count


Stream Counter
---------------
Obtains statistics concerning the packets of a specific stream transmitted on a
port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pt_commands.PT_STREAM`

.. code-block:: python

    # TX Statistics - Stream Counter
    resp = await port.statistics.tx.obtain_from_stream(stream=0).get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

