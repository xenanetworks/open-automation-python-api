Statistics
=========================

Statistics for Chimera ports.

Clear Counter
-------------
Clear all the impairment (duplicate, drop, mis-ordered, corrupted, latency and
jitter) statistics for a Chimera port and flows on the port. The byte and packet
counts will restart at zero.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_CLEAR`

.. code-block:: python

    await port.emulation.clear.set()

Corruption
-------------
Obtains statistics concerning all the packets corrupted on between this receive port and its partner TX port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_CORTOTAL`

.. code-block:: python

    port_corrupted = await port.emulation.statistics.corrupted.get()
    port_corrupted.fcs_corrupted_pkt_count
    port_corrupted.fcs_corrupted_pkt_ratio
    port_corrupted.ip_corrupted_pkt_count
    port_corrupted.ip_corrupted_pkt_ratio
    port_corrupted.tcp_corrupted_pkt_count
    port_corrupted.tcp_corrupted_pkt_ratio
    port_corrupted.total_corrupted_pkt_count
    port_corrupted.total_corrupted_pkt_ratio
    port_corrupted.udp_corrupted_pkt_count
    port_corrupted.udp_corrupted_pkt_ratio


Drop Counter
-------------
Obtains statistics concerning all the packets dropped between this receive port and its partner TX port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_DROPTOTAL`

.. code-block:: python

    port_drop = await port.emulation.statistics.drop.get()
    port_drop.pkt_drop_count_total
    port_drop.pkt_drop_count_programmed
    port_drop.pkt_drop_count_bandwidth
    port_drop.pkt_drop_count_other
    port_drop.pkt_drop_ratio_total
    port_drop.pkt_drop_ratio_programmed
    port_drop.pkt_drop_ratio_bandwidth
    port_drop.pkt_drop_ratio_other


Duplication Counter
-------------------
Obtains statistics concerning all the packets duplicated between this receive port and its partner TX port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_DUPTOTAL`

.. code-block:: python

    port_duplicated = await port.emulation.statistics.duplicated.get()
    port_duplicated.pkt_count
    port_duplicated.ratio


Jittered Counter
----------------
Obtains statistics concerning all the packets jittered between this receive port
and its partner TX port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_JITTERTOTAL`

.. code-block:: python

    port_jittered = await port.emulation.statistics.jittered.get()
    port_jittered.pkt_count
    port_jittered.ratio


Delay Counter
-------------
Obtains statistics concerning all the packets delayed this receive port and its partner TX port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_LATENCYTOTAL`

.. code-block:: python

    port_delayed = await port.emulation.statistics.latency.get()
    port_delayed.pkt_count
    port_delayed.ratio


Misordering Counter
-------------------
Obtains statistics concerning all the packets mis-ordered between this receive
port and its partner TX port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_MISTOTAL`

.. code-block:: python

    port_misordered = await port.emulation.statistics.mis_ordered.get()
    port_misordered.pkt_count
    port_misordered.ratio