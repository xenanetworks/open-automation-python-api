RX Status
=========================

Lane Error Counters
-------------------
Statistics about errors detected at the physical coding sub-layer on the data
received on a specified physical lane.

Corresponding CLI command: ``PP_RXLANEERRORS``

.. code-block:: python

    # RX Status - Lane Error Counters
    resp = await port.pcs_pma.lanes[0].rx_status.errors.get()
    resp.alignment_error_count
    resp.corrected_fec_error_count
    resp.header_error_count


Lock Status
----------------
Whether the receiver has achieved header lock and alignment lock on the data
received on a specified physical lane.

Corresponding CLI command: ``PP_RXLANELOCK``

.. code-block:: python

    # RX Status - Lock Status
    resp = await port.pcs_pma.lanes[0].rx_status.lock.get()
    resp.align_lock
    resp.header_lock


Lane Status
----------------
The virtual lane index and actual skew for data received on a specified physical
lane. This is only meaningful when the lane is in header lock and alignment
lock.

Corresponding CLI command: ``PP_RXLANESTATUS``

.. code-block:: python

    # RX Status - Lane Status
    resp = await port.pcs_pma.lanes[0].rx_status.status.get()
    resp.skew
    resp.virtual_lane


Clear Counters
---------------
Clear all the PCS/PMA receiver statistics for a port.

Corresponding CLI command: ``PP_RXCLEAR``

.. code-block:: python

    # RX Status - Clear Counters
    await port.pcs_pma.rx.clear.set()


RX FEC Stats
---------------
Provides statistics on how many FEC blocks have been seen with a given number of symbol errors.

Corresponding CLI command: ``PP_RXFECSTATS``

.. code-block:: python

    # RX Status - RX FEC Stats
    resp = await port.pcs_pma.rx.fec_status.get()
    resp.stats_type
    resp.data_count # number of values in stats
    resp.stats # list of long integers, array of length value_count. The stats array shows how many FEC blocks have been seen with [0, 1, 2, 3....15, >15] symbol errors and the last one is the sum of FEC blocks with <=n symbol errors


RX Total Stats
---------------
Provides FEC Total counters.

Corresponding CLI command: ``PP_RXTOTALSTATS``

.. code-block:: python

    # RX Status - RX Total Stats
    resp = await port.pcs_pma.rx.total_status.get()
    resp.total_corrected_codeword_count
    resp.total_corrected_symbol_count
    resp.total_rx_bit_count
    resp.total_rx_codeword_count
    resp.total_uncorrectable_codeword_count
    post_fec_ber = 1/resp.total_post_fec_ber
    pre_fec_ber = 1/resp.total_pre_fec_ber