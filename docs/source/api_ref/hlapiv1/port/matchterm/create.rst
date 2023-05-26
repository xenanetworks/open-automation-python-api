Create, Obtain, Remove
=========================

Create and Obtain
-----------------

Create a match term on the port, and obtain the match term object. The match term index is automatically assigned by the port.

.. code-block:: python

    match_term = await port.match_terms.create()


Obtain One
-----------

Obtain an existing match term on the port with an explicit match term index.

.. code-block:: python

    match_term = port.match_terms.obtain(idx)


Obtain Multiple
---------------

Obtain multiple existing match terms on the port with explicit match term indices.

.. code-block:: python

    match_term_list = port.match_terms.obtain_multiple(*idx_list)


Remove
---------------

Remove a match term on the port with an explicit match term index by the index manager of the port.

.. code-block:: python

    await port.match_terms.remove(idx)

Remove a match term by deleting the object.

.. code-block:: python

    await match_term.delete()