Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a filter on the port, and obtain the filter object. The filter index is automatically assigned by the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pf_commands.PF_CREATE`

.. code-block:: python

    filter = await port.filters.create()


Obtain One
-----------

Obtain an existing filter on the port with an explicit filter index.


.. code-block:: python

    filter = port.filters.obtain(position_idx=0)


Obtain Multiple
---------------

Obtain multiple existing filters on the port with explicit filter indices.

.. code-block:: python

    filter_list = port.filters.obtain_multiple(*[0,1,2])


Remove
---------------

Remove a filter on the port with an explicit filter index by the index manager of the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pf_commands.PF_DELETE`

.. code-block:: python

    await port.filters.remove(position_idx=0)
