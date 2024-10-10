Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a histogram on the port, and obtain the histogram object. The histogram index is automatically assigned by the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pd_commands.PD_CREATE`

.. code-block:: python

    dataset = await port.datasets.create()


Obtain One
-----------

Obtain an existing histogram on the port with an explicit histogram index.


.. code-block:: python

    dataset = port.datasets.obtain(key=0)


Obtain Multiple
---------------

Obtain multiple existing histograms on the port with explicit histogram indices.


.. code-block:: python

    dataset_list = port.datasets.obtain_multiple(*[0,1,2])


Remove
---------------

Remove a histogram on the port with an explicit histogram index by the index manager of the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pd_commands.PD_DELETE`

.. code-block:: python

    await port.datasets.remove(position_idx=0)
