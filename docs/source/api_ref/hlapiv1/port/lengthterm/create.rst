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

    length_term = port.length_terms.obtain(idx)


Obtain Multiple
---------------

Obtain multiple existing length terms on the port with explicit length term indices.

.. code-block:: python

    length_term_list = port.length_terms.obtain_multiple(*idx_list)


Remove
---------------

Remove a length term on the port with an explicit length term index by the index manager of the port.

.. code-block:: python

    await port.length_terms.remove(idx)

Remove a length term by deleting the object.

.. code-block:: python

    await length_term.delete()