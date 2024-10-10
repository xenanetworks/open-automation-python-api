Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a length term on the port, and obtain the length term object. The length term index is automatically assigned by the port.

.. code-block:: python

    length_term = await port.length_terms.create()


Obtain One
-----------

Obtain an existing length term on the port with an explicit length term index.

.. code-block:: python

    length_term = port.length_terms.obtain(key=0)


Obtain Multiple
---------------

Obtain multiple existing length terms on the port with explicit length term indices.

.. code-block:: python

    length_term_list = port.length_terms.obtain_multiple(*[0,1,2])


Remove
---------------

Deletes the length term definition with the specified sub-index value. A length
term cannot be deleted while it is used in the condition of any filter for the
port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl_commands.PL_DELETE`

.. code-block:: python

    # Remove a length term on the port with an explicit length term index by the index manager of the port.
    await port.length_terms.remove(position_idx=0)
