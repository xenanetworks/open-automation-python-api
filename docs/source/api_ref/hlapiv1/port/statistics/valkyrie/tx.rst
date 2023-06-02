TX Statistics
=========================

Clear Counter
-------------

.. code-block:: python

    await port.statistics.tx.clear.set()


Total Counter
--------------

.. code-block:: python

    await port.statistics.tx.total.get()


Non-TPLD Counter
-----------------

.. code-block:: python

    await port.statistics.tx.no_tpld.get()


Extra Counter
-------------

.. code-block:: python

    await port.statistics.tx.extra.get()


Stream Counter
---------------

.. code-block:: python

    await port.statistics.tx.obtain_from_stream(stream_id).get()

