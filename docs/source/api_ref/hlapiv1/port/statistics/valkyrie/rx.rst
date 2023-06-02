RX Statistics
=========================

RX Clear Counter
--------------------

.. code-block:: python

    await port.statistics.rx.clear.set()


RX Calibrate
--------------------

.. code-block:: python

    await port.statistics.rx.calibrate.set()


RX Total Counter
--------------------

.. code-block:: python

    await port.statistics.rx.total.get()


RX Non-TPLD Counter
--------------------

.. code-block:: python

    await port.statistics.rx.no_tpld.get()


RX PFC Counter
--------------------

.. code-block:: python

    await port.statistics.rx.pfc_stats.get()


RX Extra Counter
--------------------

.. code-block:: python

    await port.statistics.rx.extra.get()


RX UAT Status
--------------------

.. code-block:: python

    await port.statistics.rx.uat.status.get()


RX UAT Time
-------------

.. code-block:: python

    await port.statistics.rx.uat.time.get()


Received TPLDs
---------------

.. code-block:: python

    await port.statistics.rx.obtain_available_tplds()


RX TPLD - Error Counter
-----------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id).errors.get()


RX TPLD - Latency Counter
-------------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id=1).latency.get()


RX TPLD - Jitter Counter
------------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id=1).jitter.get()


RX TPLD - Traffic Counter
-------------------------

.. code-block:: python

    await port.statistics.rx.access_tpld(tpld_id=1).traffic.get()


RX Filter Statistics
--------------------

.. code-block:: python

    await port.statistics.rx.obtain_filter_statistics(filter_id).get()

