Configuration
=========================

Enable
-----------------

.. code-block:: python

    await dataset.enable.set_on()
    await dataset.enable.set_off()
    await dataset.enable.get()


Data Source
-----------

.. code-block:: python

    await dataset.source.set()
    await dataset.source.get()


Data Range
---------------

.. code-block:: python

    await dataset.range.set()
    await dataset.range.get()


Data Samples
---------------

Remove a histogram on the port with an explicit histogram index.

.. code-block:: python

    await dataset.samples.get()