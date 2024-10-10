Stream 16-bit Modifier
=========================


Create
---------------------

.. code-block:: python

    # Create
    await stream.packet.header.modifiers.configure(number=1)


Clear
---------------------

.. code-block:: python

    # Clear
    await stream.packet.header.modifiers.clear()



Obtain
-------------------------

.. note::

    Must create modifiers before obtain.

.. code-block:: python

    # Obtain
    # Must create modifiers before obtain.
    modifier = stream.packet.header.modifiers.obtain(idx=0)


Range
-------------------------
Range specification for a packet modifier for a stream header, specifying which
values the modifier should take on. This applies only to incrementing and
decrementing modifiers; random modifiers always produce every possible bit
pattern. The range is specified as three values: mix, step, and max, where max
must be equal to min plus a multiple of step. Note that when "decrement" is
specified in :class:`~xoa_driver.internals.commands.ps_commands.PS_MODIFIER` as the action, the value sequence will begin with the
max value instead of the min value and decrement from there: {max, max-1, max-2,
...., min, max, max-1...}.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_MODIFIERRANGE`

.. code-block:: python

    # Range
    await modifier.range.set(min_val=0, step=10, max_val=9)
    
    resp = await modifier.range.get()
    resp.min_val
    resp.max_val
    resp.step


Position, Action, Mask
----------------------
A packet modifier for a stream header. The headers of each packet transmitted
for the stream will be varied according to the modifier specification. This
command requires two sub-indices, one for the stream and one for the modifier.
A modifier is positioned at a fixed place in the header, selects a number of
consecutive bits starting from that position, and applies an action to those
bits in each packet. Packets can be repeated so that a certain number of
identical packets are transmitted before applying the next modification.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_MODIFIER`

.. code-block:: python

    # Position, Action, Mask
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.INC, repetition=1)
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.DEC, repetition=1)
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.RANDOM, repetition=1)
    
    resp = await modifier.specification.get()
    resp.action
    resp.mask
    resp.position
    resp.repetition