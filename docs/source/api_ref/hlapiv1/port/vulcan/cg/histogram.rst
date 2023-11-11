Histogram
=========================

.. note::

    Applicable to Vulcan port only.

    
Configuration
--------------



.. code-block:: python

    await cg.histogram.config.transaction.set()
    await cg.histogram.config.transaction.get()

    await cg.histogram.config.payload.set()
    await cg.histogram.config.payload.get()

    await cg.histogram.config.time.set()
    await cg.histogram.config.time.get()

Recalculate
--------------



.. code-block:: python

    await cg.histogram.recalculates.transaction.set()
    await cg.histogram.recalculates.transaction.get()

    await cg.histogram.recalculates.payload.set()

    await cg.histogram.recalculates.time.set()

Transaction
--------------



.. code-block:: python

    await cg.histogram.transaction.get()

