Packet Content
=========================

Packet Size
---------------------
The length distribution of the packets transmitted for a stream. The length of
the packets transmitted for a stream can be varied from packet to packet,
according to a choice of distributions within a specified min...max range. The
length of each packet is reflected in the size of the payload portion of the
packet, whereas the header has constant length. Length variation complements,
and is independent of, the content variation produced by header modifiers.

Corresponding CLI command: ``PS_PACKETLENGTH``

.. code-block:: python

    # Packet Size
    await stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=64, max_val=64)
    await stream.packet.length.set(length_type=enums.LengthType.INCREMENTING, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.BUTTERFLY, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.RANDOM, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.MIX, min_val=64, max_val=64)

    resp = await stream.packet.length.get()
    resp.length_type
    resp.min_val
    resp.max_val


Packet Auto Size
-------------------------
Executing PS_AUTOADJUST will adjust the packet length distribution (PS_PACKETLENGTH) of the stream:

(1) Set the type of packet length distribution (PS_PACKETLENGTH ``<length_type>``) to ``FIXED``.

(2) Set the lower limit on the packet length (PS_PACKETLENGTH ``<min_val>``) to exactly fit the specified protocol headers,
TPLD and FCS (but never set to less than 64).

(3) Set the payload type of packets transmitted for the stream (PS_PAYLOAD ``<payload_type>``) to ``PATTERN``.

(4) If necessary, also set the maximum number of header content bytes (P_MAXHEADERLENGTH ``<p_maxheaderlength_label>`` ``<max_header_length>``)
that can be freely specified for each generated stream of the port to a higher value, if needed to accommodate the header size of the stream
(implicitly given by the PS_PACKETHEADER command).

(5) If the needed maximum header length (P_MAXHEADERLENGTH ``<p_maxheaderlength_label>`` ``<max_header_length>``)
is not possible with the actual number of active streams for the port, the command will fail with: <BADVALUE>.

Corresponding CLI command: ``PS_AUTOADJUST``

.. code-block:: python

    # Packet Auto Size
    await stream.packet.auto_adjust.set()


Payload Type
-------------------------
The payload content of the packets transmitted for a stream. The payload portion
of a packet starts after the header and continues up until the test payload or
the frame checksum. The payload may vary in length and is filled with either an
incrementing sequence of byte values or a repeated multi-byte pattern. Length
variation complements and is independent of the content variation produced by
header modifiers.

Corresponding CLI command: ``PS_PAYLOAD``

.. code-block:: python

    # Payload Type
    # Pattern string in hex, min = 1 byte, max = 18 bytes
    await stream.payload.content.set(payload_type=enums.PayloadType.PATTERN, hex_data=Hex("000102030405060708090A0B0C0D0E0FDEAD"))
    await stream.payload.content.set(payload_type=enums.PayloadType.PATTERN, hex_data=Hex("F5"))
    
    # Patter string ignored for non-pattern types
    await stream.payload.content.set(payload_type=enums.PayloadType.INC16, hex_data=Hex("F5"))
    await stream.payload.content.set_inc_word("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.INC8, hex_data=Hex("F5"))
    await stream.payload.content.set_inc_byte("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.DEC8, hex_data=Hex("F5"))
    await stream.payload.content.set_dec_byte("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.DEC16, hex_data=Hex("F5"))
    await stream.payload.content.set_dec_word("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.PRBS, hex_data=Hex("F5"))
    await stream.payload.content.set_prbs("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.RANDOM, hex_data=Hex("F5"))
    await stream.payload.content.set_random("00")

    resp = await stream.payload.content.get()
    resp.hex_data
    resp.payload_type


Extended Payload
-------------------------
This command controls the extended payload feature. The PS_PAYLOAD command
described above only allow the user to specify an 18-byte pattern (when
PS_PAYLOAD is set to PATTERN). The PS_EXTPAYLOAD command allow the definition
of a much larger (up to MTU) payload buffer for each stream. The extended
payload will be inserted immediately after the end of the protocol segment area.
The feature requires the P_PAYLOADMODE command on the parent port being set to
EXTPL. This enables the feature for all streams on this port.

.. note::

    Use ``await port.payload_mode.set_extpl()`` to set the port's payload mode to Extended Payload.

Corresponding CLI command: ``PS_EXTPAYLOAD``

.. code-block:: python

    # Extended Payload
    # Use await port.payload_mode.set_extpl() to set the port's payload mode to Extended Payload.
    await stream.payload.extended.set(hex_data=Hex("00110022FF"))
    
    resp = await stream.payload.extended.get()
    resp.hex_data


