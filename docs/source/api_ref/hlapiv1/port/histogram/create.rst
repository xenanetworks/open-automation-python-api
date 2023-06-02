Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a histogram on the port, and obtain the histogram object. The histogram index is automatically assigned by the port.

.. code-block:: python

    dataset = await port.datasets.create()


Obtain One
-----------

Obtain an existing histogram on the port with an explicit histogram index.

.. code-block:: python

    dataset = port.datasets.obtain(idx)


Obtain Multiple
---------------

Obtain multiple existing histograms on the port with explicit histogram indices.

.. code-block:: python

    dataset_list = port.datasets.obtain_multiple(*idx_list)


Remove
---------------

Remove a histogram on the port with an explicit histogram index by the index manager of the port.

.. code-block:: python

    await port.datasets.remove(idx)

Remove a histogram by deleting the object.

.. code-block:: python

    await dataset.delete()