Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a stream on the port, and obtain the stream object. The stream index is automatically assigned by the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_CREATE`

.. code-block:: python

    stream = await port.streams.create()


Obtain One
-----------

Obtain an existing stream on the port with an explicit stream index.

.. code-block:: python

    stream = = port.streams.obtain(0)


Obtain Multiple
---------------

Obtain multiple existing streams on the port with explicit stream indices.

.. code-block:: python

    stream_list = port.streams.obtain_multiple(*[0,1,2])


Remove
---------------

Deletes the stream definition with the specified sub-index value.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_DELETE`

.. code-block:: python

    # Remove
    # Remove a stream on the port with an explicit stream index.
    await port.streams.remove(position_idx=0)