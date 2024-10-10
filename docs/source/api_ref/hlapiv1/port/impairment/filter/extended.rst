Working Filter
=========================

.. note::

    Applicable to Chimera port only.


Use Segments
-------------------
This command is valid only for ``Extended filter mode`` (check PEF_MODE).

Defines the sequence of protocol segments that can be
matched. The total length of the specified segments cannot exceed 128 bytes. If
an existing sequence of segments is changed (using PEF_PROTOCOL) the underlying
value and mask bytes remain unchanged, even though the semantics of those bytes
may have changed. However, if the total length, in bytes, of the segments is
reduced, then the excess bytes of value and mask are set to zero. I.e. to update
an existing filter, you must first correct the list of segments (using
PEF_PROTOCOL) and subsequently update the filtering value (using PEF_VALUE) and filtering mask (PEF_MASK).
    
Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_PROTOCOL`

.. code-block:: python
    
    # Configure shadow filter to EXTENDED mode
    await flow.shadow_filter.use_extended_mode()

    # Query the mode of the filter (either basic or extended)
    filter = await flow.shadow_filter.get_mode()

    if isinstance(filter, misc.ExtendedImpairmentFlowFilter):
        # Ethernet is the default mandatory
        # Adding VLAN after Ethernet
        await filter.use_segments(
            enums.ProtocolOption.VLAN
            )
        protocol_segments = await filter.get_protocol_segments()

        await protocol_segments[0].value.set(value=Hex("AAAAAAAAAAAABBBBBBBBBBBB8100"))
        await protocol_segments[0].mask.set(masks=Hex("0000000000000000000000000000"))
        await protocol_segments[1].value.set(value=Hex("0064FFFF"))
        await protocol_segments[1].mask.set(masks=Hex("00000000"))

Segment Value
-------------------
This command is valid only for ``Extended filter mode`` (check PEF_MODE).

Defines the byte values that can be matched if selected by PEF_MASK.

If ``<protocol_segment_index> = 0`` the maximum number of match value
bytes that can be set is determined by the total length of the protocol segments
specified with PEF_PROTOCOL.

E.g. if PEF_PROTOCOL is set to ETHERNET then only
12 bytes can be set. In order to set the full 128 bytes, either specify a
detailed protocol segment list, or use the raw protocol segment type. This specifies 12 + 116 = 128 bytes.

If ``<protocol_segment_index> != 0`` only the bytes covered by that segment are manipulated,
so if PEF_PROTOCOL is set to ``ETHERNET VLAN ETHERTYPE eCPRI`` then ``<protocol_segment_index> = 4`` selects the 8
bytes of the eCPRI header starting at byte position (12 + 2 + 4) = 18.

For ``set`` command where fewer value bytes are provided than specified by the protocol segment, those unspecified bytes are set to zero.

The ``get`` command always returns the number of bytes specified by the protocol segment.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_VALUE`

.. code-block:: python
    
    # Configure shadow filter to EXTENDED mode
    await flow.shadow_filter.use_extended_mode()

    # Query the mode of the filter (either basic or extended)
    filter = await flow.shadow_filter.get_mode()

    if isinstance(filter, misc.ExtendedImpairmentFlowFilter):
        # Ethernet is the default mandatory
        # Adding VLAN after Ethernet
        await filter.use_segments(
            enums.ProtocolOption.VLAN
            )
        protocol_segments = await filter.get_protocol_segments()

        await protocol_segments[0].value.set(value=Hex("AAAAAAAAAAAABBBBBBBBBBBB8100"))
        await protocol_segments[0].mask.set(masks=Hex("0000000000000000000000000000"))
        await protocol_segments[1].value.set(value=Hex("0064FFFF"))
        await protocol_segments[1].mask.set(masks=Hex("00000000"))

        resp = await protocol_segments[0].value.get()
        resp.value
        resp = await protocol_segments[1].value.get()
        resp.value

Segment Mask
-------------------
This command is valid only for ``Extended filter mode`` (check PEF_MODE).

Defines the mask byte values that select the values specified by PEF_VALUE.

For a chosen ``<protocol_segment_index>`` the first byte in the value masks the
first byte of the corresponding PEF_VALUE and so on.

If ``<protocol_segment_index> = 0`` the maximum number of match value
bytes that can be set is determined by the total length of the protocol segments
specified with PEF_PROTOCOL`.

E.g. if PEF_PROTOCOL is set to ETHERNET then only
12 bytes can be set. In order to set the full 128 bytes, either specify a
detailed protocol segment list, or use the raw protocol segment type. This specifies 12 + 116 = 128 bytes.

If ``<protocol_segment_index> != 0`` only the bytes covered by that segment are manipulated,
so if PEF_PROTOCOL is set to ``ETHERNET VLAN ETHERTYPE eCPRI`` then ``<protocol_segment_index> = 4`` selects the 8
bytes of the eCPRI header starting at byte position (12 + 2 + 4) = 18.

``get/set`` semantics are similar to PEF_VALUE.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_MASK`

.. code-block:: python
    
    # Configure shadow filter to EXTENDED mode
    await flow.shadow_filter.use_extended_mode()

    # Query the mode of the filter (either basic or extended)
    filter = await flow.shadow_filter.get_mode()

    if isinstance(filter, misc.ExtendedImpairmentFlowFilter):
        # Ethernet is the default mandatory
        # Adding VLAN after Ethernet
        await filter.use_segments(
            enums.ProtocolOption.VLAN
            )
        protocol_segments = await filter.get_protocol_segments()

        await protocol_segments[0].value.set(value=Hex("AAAAAAAAAAAABBBBBBBBBBBB8100"))
        await protocol_segments[0].mask.set(masks=Hex("0000000000000000000000000000"))
        await protocol_segments[1].value.set(value=Hex("0064FFFF"))
        await protocol_segments[1].mask.set(masks=Hex("00000000"))

        resp = await protocol_segments[0].mask.get()
        resp.value
        resp = await protocol_segments[1].mask.get()
        resp.value