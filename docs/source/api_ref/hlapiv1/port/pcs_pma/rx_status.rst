RX Status
=========================

Lane Error Counters
-------------------

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].rx_status.errors.get()


Lock Status
----------------

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].rx_status.lock.get()


Lane Status
----------------

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].rx_status.status.get()


Clear Counters
---------------

.. code-block:: python

    await port.pcs_pma.rx.clear.set()


RX FEC Stats
---------------

.. code-block:: python

    await port.pcs_pma.rx.fec_status.get()


RX Total Stats
---------------

.. code-block:: python

    await port.pcs_pma.rx.total_status.get()