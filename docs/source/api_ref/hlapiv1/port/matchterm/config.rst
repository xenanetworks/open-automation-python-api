Configuration
=========================

Match
-----------------
The value that must be found at the match term position for packets received on
the port. The mask can make certain bit positions don't-care.

Corresponding CLI command: ``PM_MATCH``

.. code-block:: python

    await match_term.match.set(mask=Hex("FF"), value=Hex("00"))

    resp = await match_term.match.get()
    resp.mask
    resp.value


Position
-----------
The position within each received packet where content matching begins for the port.

Corresponding CLI command: ``PM_POSITION``

.. code-block:: python

    await match_term.position.set(byte_offset=0)

    resp = await match_term.position.get()
    resp.byte_offset


Protocol Segments
-----------------
The protocol segments assumed on the packets received on the port. This is
mainly for information purposes, and helps you identify which portion of the
packet header is being matched. The actual value definition of the match
position is specified with PM_POSITION.

Corresponding CLI command: ``PM_PROTOCOL``

.. code-block:: python

    await match_term.protocol.set(segments=[enums.ProtocolOption.VLAN])

    resp = await match_term.protocol.get()
    resp.segments

