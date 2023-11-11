Create, Obtain, Remove
=========================

.. note::

    Applicable to Vulcan port only.
    
Create and Obtain
-----------------

Create a connection group on the Vulcan port, and obtain the connection group object. The connection group index is automatically assigned by the port.



.. code-block:: python

    cg = await port.connection_groups.create()


Obtain One
-----------

Obtain an existing connection group on the port with an explicit connection group index.



.. code-block:: python

    cg = port.connection_groups.obtain(cg_idx)


Obtain Multiple
---------------

Obtain multiple existing connection groups on the port with explicit connection group indices.



.. code-block:: python

    cg_list = port.connection_groups.obtain_multiple(*cg_idx_list)


Remove
---------------

Remove a connection group on the port with an explicit connection group index.



.. code-block:: python

    await port.connection_groups.remove(cg_idx)