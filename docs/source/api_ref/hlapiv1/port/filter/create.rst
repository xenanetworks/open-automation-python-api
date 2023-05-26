Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a filter on the port, and obtain the filter object. The filter index is automatically assigned by the port.

.. code-block:: python

    filter = await port.filters.create()


Obtain One
-----------

Obtain an existing filter on the port with an explicit filter index.

.. code-block:: python

    filter = port.filters.obtain(idx)


Obtain Multiple
---------------

Obtain multiple existing filters on the port with explicit filter indices.

.. code-block:: python

    filter_list = port.filters.obtain_multiple(*idx_list)


Remove
---------------

Remove a filter on the port with an explicit filter index by the index manager of the port.

.. code-block:: python

    await port.filters.remove(idx)

Remove a filter by deleting the object.

.. code-block:: python

    await filter.delete()