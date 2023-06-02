Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a stream on the port, and obtain the stream object. The stream index is automatically assigned by the port.

.. code-block:: python

    stream = await port.streams.create()


Obtain One
-----------

Obtain an existing stream on the port with an explicit stream index.

.. code-block:: python

    stream = port.streams.obtain(stream_idx)


Obtain Multiple
---------------

Obtain multiple existing streams on the port with explicit stream indices.

.. code-block:: python

    stream_list = port.streams.obtain_multiple(*stream_idx_list)


Remove
---------------

Remove a stream on the port with an explicit stream index.

.. code-block:: python

    await port.streams.remove(stream_idx)