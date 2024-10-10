Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a match term on the port, and obtain the match term object. The match term index is automatically assigned by the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pm_commands.PM_CREATE`

.. code-block:: python

    match_term = await port.match_terms.create()


Obtain One
-----------

Obtain an existing match term on the port with an explicit match term index.

.. code-block:: python

    match_term = port.match_terms.obtain(key=0)


Obtain Multiple
---------------

Obtain multiple existing match terms on the port with explicit match term indices.


.. code-block:: python

    match_term_list = port.match_terms.obtain_multiple(*[0,1,2])


Remove
---------------

Deletes the match term definition with the specified sub-index value. A match
term cannot be deleted while it is used in the condition of any filter for the
port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pm_commands.PM_DELETE`

.. code-block:: python

    await port.match_terms.remove(position_idx=0)
