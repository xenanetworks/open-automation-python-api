RX Statistics
=========================

Clear Counter
-------------

.. code-block:: python

    await port.statistics.rx.clear.set()


Calibrate
-------------

.. code-block:: python

    await port.statistics.rx.calibrate.set()


Total Counter
-------------

.. code-block:: python

    await port.statistics.rx.total.get()


Non-TPLD Counter
-----------------

.. code-block:: python

    await port.statistics.rx.no_tpld.get()


PFC Counter
-------------

.. code-block:: python

    await port.statistics.rx.pfc_stats.get()


Extra Counter
-------------

.. code-block:: python

    await port.statistics.rx.extra.get()


UAT Status
-------------

.. code-block:: python

    await port.statistics.rx.uat.status.get()


UAT Time
-------------

.. code-block:: python

    await port.statistics.rx.uat.time.get()


Received TPLDs
---------------

.. code-block:: python

    await port.statistics.rx.obtain_available_tplds()


TPLD - Error Counter
--------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id).errors.get()


TPLD - Latency Counter
-----------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id=1).latency.get()


TPLD - Jitter Counter
-----------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id=1).jitter.get()


TPLD - Traffic Counter
-----------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id=1).traffic.get()


Filter Statistics
--------------------

.. code-block:: python

    await port.statistics.rx.obtain_filter_statistics(filter_id).get()

