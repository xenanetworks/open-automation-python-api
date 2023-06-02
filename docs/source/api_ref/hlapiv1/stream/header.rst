Packet Header Definition
=========================

Header Protocol Segment
------------------------

.. code-block:: python

    await stream.packet.header.protocol.set(segments)
    await stream.packet.header.protocol.get()


Header Value
-------------------------

.. code-block:: python

    await stream.packet.header.data.set("11223344FFEEBB...")
    await stream.packet.header.data.get()

