Stream 16-bit Modifier
=========================


Create
---------------------

.. code-block:: python

    await stream.packet.header.modifiers.configure(modifier_count)



Clear
---------------------

.. code-block:: python

    await stream.packet.header.modifiers.clear()



Obtain
-------------------------

.. note::

    Must create modifiers before obtain.

.. code-block:: python

    modifier = stream.packet.header.modifiers.obtain(modifier_idx)


Range
-------------------------

.. code-block:: python

    await modifier.range.set()
    await modifier.range.get()


Position, Action, Mask
----------------------

.. code-block:: python

    await modifier.specification.set()
    await modifier.specification.get()