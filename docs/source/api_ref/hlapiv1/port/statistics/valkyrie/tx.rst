TX Statistics
=========================

TX Clear Counter
-------------

.. code-block:: python

    await port.statistics.tx.clear.set()


TX Total Counter
--------------

.. code-block:: python

    await port.statistics.tx.total.get()


TX Non-TPLD Counter
-----------------

.. code-block:: python

    await port.statistics.tx.no_tpld.get()


TX Extra Counter
-------------

.. code-block:: python

    await port.statistics.tx.extra.get()


TX Stream Counter
---------------

.. code-block:: python

    await port.statistics.tx.obtain_from_stream(stream_id).get()

