Stream 32-bit Modifier
=========================


Create
---------------------

.. code-block:: python

    await stream.packet.header.modifiers_extended.configure(modifier_count)



Clear
---------------------

.. code-block:: python

    await stream.packet.header.modifiers_extended.clear()



Obtain
-------------------------

.. note::

    Must create modifiers before obtain.

.. code-block:: python

    modifier_ext = stream.packet.header.modifiers_extended.obtain(modifier_idx)


Range
-------------------------

.. code-block:: python

    await modifier_ext.range.set()
    await modifier_ext.range.get()


Position, Action, Mask
----------------------

.. code-block:: python

    await modifier_ext.specification.set()
    await modifier_ext.specification.get()