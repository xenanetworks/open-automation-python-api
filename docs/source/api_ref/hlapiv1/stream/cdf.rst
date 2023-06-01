Custom Data Field
=========================

.. note::

    Use ``await port.payload_mode.set_cdf()`` to set the port's payload mode to Custom Data Field.

Field Offset
---------------------

.. code-block:: python

    await stream.cdf.offset.set()
    await stream.cdf.offset.get()


Byte Count
-------------------------

.. code-block:: python

    await stream.cdf.count.set()
    await stream.cdf.count.get()

