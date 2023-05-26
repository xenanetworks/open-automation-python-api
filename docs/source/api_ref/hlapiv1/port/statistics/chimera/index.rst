Statistics
=========================

Statistics for Chimera ports.

Corruption
-------------

.. code-block:: python

    await port.emulation.statistics.corrupted.get()


Drop Counter
-------------

.. code-block:: python

    await port.emulation.statistics.drop.get()


Duplication Counter
-------------------

.. code-block:: python

    await port.emulation.statistics.duplicated.get()


Jittered Counter
----------------

.. code-block:: python

    await port.emulation.statistics.jittered.get()


Delay Counter
-------------

.. code-block:: python

    await port.emulation.statistics.latency.get()


Misordering Counter
-------------------

.. code-block:: python

    await port.emulation.statistics.mis_ordered.get()