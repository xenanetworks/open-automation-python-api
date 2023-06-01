Packet Content
=========================

Packet Size
---------------------

.. code-block:: python

    await stream.packet.length.set_fixed(min, max)
    await stream.packet.length.set_butterfly(min, max)
    await stream.packet.length.set_incrementing(min, max)
    await stream.packet.length.set_mix(min, max)
    await stream.packet.length.set_random(min, max)
    await stream.packet.length.get()


Packet Auto Size
-------------------------

.. code-block:: python

    await stream.packet.auto_adjust.set()
    await stream.packet.auto_adjust.get()


Payload Type
-------------------------


.. code-block:: python

    # Pattern string in hex, min = 1 byte, max = 18 bytes
    await stream.payload.content.set_pattern("AABBCCDD")
    
    # Patter string ignored for non-pattern types
    await stream.payload.content.set_inc_word("00")
    await stream.payload.content.set_inc_byte("00")
    await stream.payload.content.set_dec_byte("00")
    await stream.payload.content.set_dec_word("00")
    await stream.payload.content.set_prbs("00")
    await stream.payload.content.set_random("00")


Extended Payload
-------------------------

.. note::

    Use ``await port.payload_mode.set_extpl()`` to set the port's payload mode to Extended Payload.

.. code-block:: python

    await stream.payload.extended.set("00110022FF...")
    await stream.payload.extended.get()


