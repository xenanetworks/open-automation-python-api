RX Statistics
=========================

Clear Counter
-------------
Clear all the receive statistics for a port. The byte and packet counts will
restart at zero.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_CLEAR`

.. code-block:: python

    # RX Statistics - Clear Counter
    await port.statistics.rx.clear.set()


Calibrate
-------------
Calibrate the latency calculation for packets received on a port. The lowest
detected latency value (across all Test Payload IDs) will be set as the new
base.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_CALIBRATE`

.. code-block:: python

    # RX Statistics - Calibrate
    await port.statistics.rx.calibrate.set()


Total Counter
-------------
Obtains statistics concerning all the packets received on a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_TOTAL`

.. code-block:: python

    # RX Statistics - Total Counter
    resp = await port.statistics.rx.total.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


Non-TPLD Counter
-----------------
Obtains statistics concerning the packets without a test payload received on a
port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_NOTPLD`

.. code-block:: python

    # RX Statistics - Non-TPLD Counter
    resp = await port.statistics.rx.no_tpld.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


PFC Counter
-------------
Obtains statistics of received Priority Flow Control (PFC) packets on a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_PFCSTATS`

.. code-block:: python

    # RX Statistics - PFC Counter
    resp = await port.statistics.rx.pfc_stats.get()
    resp.packet_count
    resp.quanta_pri_0
    resp.quanta_pri_1
    resp.quanta_pri_2
    resp.quanta_pri_3
    resp.quanta_pri_4
    resp.quanta_pri_5
    resp.quanta_pri_6
    resp.quanta_pri_7



Extra Counter
-------------
Obtains statistics concerning special errors received on a port since received statistics were cleared.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_EXTRA`

.. code-block:: python

    # RX Statistics - Extra Counter
    resp = await port.statistics.rx.extra.get()
    resp.fcs_error_count
    resp.pause_frame_count
    resp.gap_count
    resp.gap_duration
    resp.pause_frame_count
    resp.rx_arp_reply_count
    resp.rx_arp_request_count
    resp.rx_ping_reply_count
    resp.rx_ping_request_count


Received TPLDs
---------------
Obtain the set of test payload IDs observed among the received packets since
receive statistics were cleared. Traffic statistics for these test payload
streams will have non-zero byte and packet count.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_TPLDS`

.. code-block:: python

    # RX Statistics - Received TPLDs
    await port.statistics.rx.obtain_available_tplds()


TPLD - Error Counter
--------------------
Obtains statistics concerning errors in the packets with a particular test
payload id received on a port. The error information is derived from analyzing
the various fields contained in the embedded test payloads of the received
packets, independent of which chassis and port may have originated the packets.
Note that packet-lost statistics involve both a transmitting port and a
receiving port, and in particular knowing which port originated the packets with
a particular test payload identifier. This information requires knowledge of the
global test environment, and is not supported at the port-level.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_TPLDERRORS`

.. code-block:: python

    # RX Statistics - TPLD - Error Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).errors.get()
    resp.non_incre_payload_packet_count
    resp.non_incre_seq_event_count
    resp.swapped_seq_misorder_event_count


TPLD - Latency Counter
-----------------------
Obtains statistics concerning the latency experienced by the packets with a
particular test payload id received on a port. The values are adjusted by the
port-level :class:`~xoa_driver.internals.commands.p_commands.P_LATENCYOFFSET`` value. A special value of -1 is returned if latency
numbers are not applicable. Latency is only meaningful when the clocks of the
transmitter and receiver are synchronized. This requires the two ports to be on
the same test module, and it requires knowledge of the global test environment
to ensure that packets are in fact routed between these ports.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_TPLDLATENCY`

.. code-block:: python

    # RX Statistics - TPLD - Latency Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).latency.get()
    resp.avg_last_sec
    resp.max_last_sec
    resp.min_last_sec
    resp.avg_val
    resp.max_val
    resp.min_val


TPLD - Jitter Counter
-----------------------
Obtains statistics concerning the jitter experienced by the packets with a
particular test payload id received on a port. The values are the difference in
packet-to-packet latency, and the minimum will usually be zero.A special value
of -1 is returned if jitter numbers are not applicable. They are only available
for TID values 0..31.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_TPLDJITTER`

.. code-block:: python

    # RX Statistics - TPLD - Jitter Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).jitter.get()
    resp.avg_last_sec
    resp.max_last_sec
    resp.min_last_sec
    resp.avg_val
    resp.max_val
    resp.min_val

TPLD - Traffic Counter
-----------------------
Obtains traffic statistics concerning the packets with a particular test payload
identifier received on a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_TPLDTRAFFIC`

.. code-block:: python

    # RX Statistics - TPLD - Traffic Counter
    resp = await port.statistics.rx.access_tpld(tpld_id=0).traffic.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


Filter Statistics
--------------------
Obtains statistics concerning the packets satisfying the condition of a
particular filter for a port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_FILTER`

.. code-block:: python

    # RX Statistics - Filter Statistics
    resp = await port.statistics.rx.obtain_filter_statistics(filter=0).get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec

UAT Status
-------------
This command will show the current UAT (UnAvailable Time) state, which is used
in Xena1564.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_UAT_STATUS`

.. code-block:: python

    await port.statistics.rx.uat.status.get()


UAT Time
-------------
This command will show the current number of unavailable seconds, which is used in Xena1564.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pr_commands.PR_UAT_TIME`

.. code-block:: python

    await port.statistics.rx.uat.time.get()
