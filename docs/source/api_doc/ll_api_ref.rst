Low-Level API Reference
=============================

The low-level Python APIs are categorized into five groups:

* :ref:`L23 Group (Valkyrie) <l23>`
* :ref:`L47 Group (Vulcan) <l47>`
* :ref:`Impairment Group (Chimera) <impairment>`
* :ref:`Supporting Group <Supporting>`


.. _l23:

L23 Group (Valkyrie)
--------------------

Chassis APIs ``xoa_driver.lli.commands.c_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


This module contains the **chassis commands** that deal with basic information and configuration of the chassis itself (rather than its modules and test ports), as well as overall control of the scripting session. The chassis command names all have the form ``C_xxxx`` and use neither a module index nor a port index.

.. automodule:: xoa_driver.internals.core.commands.c_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Module APIs ``xoa_driver.lli.commands.m_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 module commands** that deal with basic information about, and configuration of the test modules. The module command names all have the form ``M_<xxx>`` and require a module index id.

.. automodule:: xoa_driver.internals.core.commands.m_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port APIs ``xoa_driver.lli.commands.p_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port commands** that deal with basic information about, and configuration of L23 test ports. The L23 port command names all have the form ``P_<xxx>`` and require a module index id and a port index id. In general, port commands cannot be changed while traffic is on. Additionally, every stream must be disabled before changing parameters that affect the bandwidth of the port.

.. automodule:: xoa_driver.internals.core.commands.p_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Stream APIs ``xoa_driver.lli.commands.ps_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 stream commands** deal with configuration of the traffic streams transmitted from a L23 port. The stream command names all have the form ``PS_<xxx>`` and require both a module index id and a port index id, as well as a sub-index identifying a particular stream.

.. rubric:: General Information

*Enabling Traffic*

Whether the port is actually transmitting packets is controlled both by the ``P_TRAFFIC`` command for the parent port and by the ``PS_ENABLE`` command for the stream.

While the parent port is transmitting, the parameters of any enabled stream cannot be changed.

*Stream Test Payload Data (TPLD)*

Each Xena test packet contains a special proprietary data area called the :term:`Test Payload Data (TPLD)<TPLD>`, which contains various information about the packet and is identified by a :term:`Test Payload ID (TID)<TID>`. The :term:`TPLD` is located just before the Ethernet FCS and consists of the following sections:

.. table:: Default TPLD (20 or 22 bytes)
   :widths: auto

   ===============================  ===================     ================================================================================ 
   Field                            Length                  Explanation
   ===============================  ===================     ================================================================================ 
   Checksum (optional)              2 bytes                 See the :ref:`note <note_tpld>`.
   Sequence Number                  3 bytes                 Packet sequence number used for loss and misordering detection.
   Timestamp                        4 bytes                 Timestamp value used for latency measurements.
   Test Payload ID (TID)            2 bytes                 Test payload identifier used to identify the sending stream.
   Payload Integrity Offset         1 bit                   Offset in packet from where to calculate payload integrity.
   First Packet Flag                1 bit                   Set if this is the first packet after traffic is started. 
   Checksum Enabled                 1 bit                   Set if payload integrity checksum is used.
   <reserved>                       7 bits                  
   Payload Integrity Offset (MSB)   3 bits                  Offset in packet from where to calculate payload integrity, MSB (bits 10:9:8)
   Timestamp Decimals               4 bits                  Additional decimals for the timestamp.
   Checksum                         8 bytes                 TPLD integrity checksum.
   **Total TPLD Size**              **20 or 22 bytes**
   ===============================  ===================     ================================================================================ 

.. _note_tpld:

.. note::

   If the ``P_CHECKSUM offset`` (Payload Checksum Offset) is enabled on the parent port, then an additional 2-byte checksum field is inserted in the TPLD, just before the Sequence Number. This increases the total size of the TPLD to 22 bytes.

.. table:: Micro-TPLD (6 bytes)
   :widths: auto

   =========================  ============   ================================================================
   Field                      Length         Explanation                                                     
   =========================  ============   ================================================================
   First Packet Flag          1 bit          Packet sequence number used for loss and misordering detection.
   <reserved>                 1 bit
   Test Payload ID (TID)      10 bits        Test payload identifier used to identify the sending stream.
   Timestamp                  28 bits        Timestamp value used for latency measurements.
   Checksum                   8 bits         TPLD integrity checksum (CRC-8)
   **Total Micro-TPLD Size**  **6 bytes**
   =========================  ============   ================================================================

The selection between the default TPLD and the micro-TPLD is done on the parent port. It is thus not possible to use different TPLD types for streams on the same port.

*Disabling TPLD*
The TPLD function can also be completely disabled for any given stream by setting the :term:`Test Payload ID (TID)<TID>` value for the stream to the value -1.

.. rubric:: Minimum Packet Size Considerations

The stream will generally accept any configuration and attempt to transmit packets according to the configuration. In order for the various Xena stream features to work correctly certain aspects about the minimum packet size used must be observed.

The minimum packet size must obviously be large enough to accommodate the defined ``protocol headers + the final Ethernet FCS field``.

If the :term:`TPLD` function explained above is enabled then each packet must also be able to contain the :term:`TPLD` area (20, 22 or 6 bytes depending on the configuration).

If the stream payload type is set to ``Incrementing``, then an additional minimum payload area of 2 bytes is needed. Otherwise excessive payload errors will be reported. This is however not necessary if the ``P_CHECKSUM offset`` (Payload Checksum Offset) option is enabled on the parent port as this will override the payload integrity check implied by the ``Incrementing`` payload type.


.. automodule:: xoa_driver.internals.core.commands.ps_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 High-Speed Port APIs ``xoa_driver.lli.commands.pp_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 high-speed port commands** that provide configuration and status for the Gigabit Attachment Unit Interface (CAUI) physical coding sublayer used by 40G, 50G, 100G, 200G, 400G and 800G ports. The data is broken down into a number of lower-speed lanes. For 40G there are 4 lanes of 10 Gbps each. For 100G there are 20 lanes of 5 Gbps each. Within each lane the data is broken down into 66-bit code-words.

During transport, the lanes may be swapped and skewed with respect to each other. To deal with this, each lane contains marker words with a virtual lane index id. The commands are indexed with a physical lane index that corresponds to a fixed numbering of the underlying fibers or wavelengths.

The lanes can also be put into :term:`Pseudorandom Binary Sequence (PRBS)<PRBS>` mode where they transmit a bit pattern used for diagnosing fiber-level problems, and the receiving side can lock to these patterns.

Errors can be injected both at the CAUI level and at the bit level.

The high-speed port command names all have the form ``PP_<xxx>`` and require a module index id and a port index id, and most also require a physical lane index id.


.. automodule:: xoa_driver.internals.core.commands.pp_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port TX Statistics APIs ``xoa_driver.lli.commands.pt_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port TX statistics commands** that provide quantitative information about the transmitted packets on a port.

The command names all have the form ``PT_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific transmitted stream also have a sub-index.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

.. automodule:: xoa_driver.internals.core.commands.pt_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port RX Statistics APIs ``xoa_driver.lli.commands.pr_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port RX statistics commands** that provide quantitative information about the received packets on a port.

The command names all have the form ``PR_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific received test payload id and a specific filter also have a sub-index id.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

.. automodule:: xoa_driver.internals.core.commands.pr_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port Capture APIs ``xoa_driver.lli.commands.pc_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port capture commands** that deal with configuration of the capture criteria and inspection of the captured data from a port.

Whether the port is enabled for capturing packets is specified by the ``P_CAPTURE`` command. Captured packets are indexed starting from 0, and are stored in a buffer that is cleared before capture starts. While on, the capture configuration parameters cannot be changed.

The capture command names all have the form ``PC_<xxx>`` and require both a module index id and a port index id. The per-packet parameters also use a sub-index identifying a particular packet in the capture buffer.

.. automodule:: xoa_driver.internals.core.commands.pc_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port Histogram APIs ``xoa_driver.lli.commands.pd_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port histogram commands** that deal with configuration of data collection and retrieval of samples from a port.

The histogram command names all have the form ``PD_<xxx>`` and require both a module index id and a port index id, as well as a sub-index identifying a particular histogram.

A histogram has a number of *buckets* and counts the packets transmitted or received on a port, possibly limited to those with a particular test payload id. The packet length, inter-frame gap preceding it, or its latency is measured, and the bucket whose range contains this value is incremented.

While a histogram is actively collecting samples its parameters cannot be changed.

.. automodule:: xoa_driver.internals.core.commands.pd_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port Filter APIss ``xoa_driver.lli.commands.pf_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port filter commands** that deal with configuration of the filters on the received traffic of a port.

The filter command names all have the form ``PF_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular filter.

Each filter specifies a compound Boolean condition on these true/false values to determine if the filter as a whole is true/false.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. automodule:: xoa_driver.internals.core.commands.pf_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port Length Term APIss ``xoa_driver.lli.commands.pl_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port length term commands** that deal with configuration of the length term on the received traffic of a port.

The length term command names all have the form ``PL_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular length term.

The length terms provide basic true/false indications for each packet received on the port.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. automodule:: xoa_driver.internals.core.commands.pl_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port Match Term APIss ``xoa_driver.lli.commands.pm_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port match term commands** that deal with configuration of the length term on the received traffic of a port.

The match term command names all have the form ``PM_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular match term.

The match terms provide basic true/false indications for each packet received on the port.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. automodule:: xoa_driver.internals.core.commands.pm_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L23 Port Transceiver APIs ``xoa_driver.lli.commands.px_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L23 port transceiver commands** that deal with access to the register interfaces of the transceiver on a port.

.. automodule:: xoa_driver.internals.core.commands.px_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


.. _l47:

L47 Group (Vulcan)
--------------------

L47 Module APIs ``xoa_driver.lli.commands.m4_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L47 module commands**.

.. automodule:: xoa_driver.internals.core.commands.m4_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L47 Module Packet Engine APIs ``xoa_driver.lli.commands.m4e_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L47 module packet engine commands**.

.. automodule:: xoa_driver.internals.core.commands.m4e_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L47 Port APIs ``xoa_driver.lli.commands.p4_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L47 port commands**.

The Xena L47 test execution engine has seven states: ``off``, ``prepare``, ``prepare_rdy``, ``prerun``, ``prerun_rdy``, ``running`` and ``stopped``. Traffic is generated in the ``prerun`` and running states only, and configuration of parameters is only valid in state ``off`` except for a few runtime options. Port traffic commands can be given with :class:`~xoa_driver.internals.core.commands.p4_commands.P4_TRAFFIC` and port state queried by :class:`~xoa_driver.internals.core.commands.p4_commands.P4_STATE`.

* ``off`` - default state. Entered from stopped or prepare on ``OFF`` command. This is the only state that allows configuration commands. :class:`~xoa_driver.internals.core.commands.p4_commands.P4_RESET` is also considered a configuration command. Upon entering off state, some internal ''house cleaning''' is done. For example: freeing TCP Connections, clearing test specific counters etc.

* ``prepare`` - this state is entered from state off on ``PREPARE`` command. Here internal data structures relevant for the test configuration are created.

* ``prepare_rdy`` - entered automatically after activities in prepare have completed successfully.

* ``prepare_fail`` - entered automatically from prepare, if an error occurs. An error could for example be failure to load a configured replay file.

* ``prerun`` - entered from ``prepare_ready`` on ``PRERUN`` command. If enabled, this is where ARP and NDP requests are sent.

* ``prerun_rdy`` - entered automatically after activities in prerun have completed.

* ``running`` - entered either from ``prepare_ready`` or ``prerun_ready`` on ``ON`` command. This is where TCP connections are established, payload is generated and connections are closed again.

* ``stopping`` - entered from ``running``, ``prerun_ready`` or ``prerun`` on ``STOP`` command. Stops Rx/Tx traffic. In the ``stopping`` state, post-test data are calculated and captured packets are saved to files.

* ``stopped`` - entered automatically after activities in ``stopping`` are complete. This is where you can read post-test statistics and extract captured packets.

.. automodule:: xoa_driver.internals.core.commands.p4_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L47 Port Packet Engine APIs ``xoa_driver.lli.commands.p4e_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L47 port packet engine commands**.

.. automodule:: xoa_driver.internals.core.commands.p4e_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L47 Connection Group APIs ``xoa_driver.lli.commands.p4g_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **L47 connection group commands** that deal with configuration of TCP connections and are specific to L47. The commands have the form ``P4G_<xxx>`` and require a module index id and a port index id, and a connection group index id.

A :term:`Connection Group (CG) <CG>` is the basic building block when creating L47 traffic. A :term:`CG` consists of a number of TCP connections - between one and millions. A CG has a role, which is either client or server. In order to create TCP connections between two ports on a L47 chassis, two matching :term:`CGs<CG>` must be configured - one on each port - one configured as client and the other configured as server.

The number of connections in a :term:`CG`, is defined by the server range and the client range. A server/client range is a number of TCP connection endpoints defined by a number of IP addresses and a number of TCP ports. A server/client range is configured by specifying a start IP address, a number of IP addresses, a start TCP port and a number of TCP addresses. The number of clients is the number of client IP addresses times the number of client TCP ports, and the same goes for the number of servers. The number of TCP connections in a CG is the number of clients times the number of servers, that is TCP connections are created from all clients in the CG to all servers in the :term:`CG`.

.. note::

   Connection Group index must start from 0.

.. note::

   When configuring a :term:`CG`, both client AND server range must be configured on both :term:`CGs<CG>` - that is, the server CG must also know the client range and vice versa.

A :term:`CG` must be configured with a :term:`Load Profile`, which is an envelope over the TCP connection's lifetime. A connection in the :term:`CG` goes through three phases. A :term:`load profile` defines a start time and a duration of each of these phases. During the ramp-up phase connections are established at a rate defined by the number of connections divided by the ramp-up duration. During the steady-state phase connections may transmit and receive payload data, depending on the configuration of test application and test scenario for the CG. During the ramp-down phase connections are closed at a rate defined by the number of connections divided by the ramp-up duration, if they were not already closed as a result of the traffic scenario configured.

.. note::
   
   Just like client and server range, both the client and server :term:`CGs<CG>` must be configured with the :term:`load profile`.

Next the :term:`CG` must be configured with a test application, which defines what kind of traffic is transported in the TCP payload. Currently there are two kinds of test applications:

* ``NONE``, which means that no payload is sent on the TCP connections. This test application is suitable for a test, where the only purpose is to measure TCP connection open and close rates.

* ``RAW``, which means that the TCP connections transmit and receive user defined raw data. The contents of the raw TCP payload can be configured using the :class:`~xoa_driver.internals.core.commands.p4g_commands.P4G_RAW_PAYLOAD` command. Raw TCP payload can also be specified  as random and incrementing data.

Using test application ``RAW``, the CG must also be configured with a test scenario, which defines the data flow between the TCP client and server. Currently the following test scenarios can be configured: ``download``, ``upload``, and ``both``.

By combining several :term:`CGs<CG>` on a port, it is possible to create more complex traffic scenarios and more complex :term:`load profile` shapes than the individual :term:`CG` allows.

.. automodule:: xoa_driver.internals.core.commands.p4g_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


.. _impairment:

Impairment Group (Chimera)
--------------------------

Impairment Flow APIs ``xoa_driver.lli.commands.pe_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **impairment port flow commands**.

.. automodule:: xoa_driver.internals.core.commands.pe_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Impairment Custom Distribution APIs ``xoa_driver.lli.commands.pec_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **impairment port custom distribution commands**.

.. automodule:: xoa_driver.internals.core.commands.pec_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Impairment Distribution APIs ``xoa_driver.lli.commands.ped_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **impairment port distribution commands**.

.. automodule:: xoa_driver.internals.core.commands.ped_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Impairment Flow Filter APIs ``xoa_driver.lli.commands.pef_commands``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the **impairment port flow filter commands**.

.. automodule:: xoa_driver.internals.core.commands.pef_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


.. _supporting:

Supporting Group
-----------------

Helper APIs ``xoa_driver.lli``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains some *helper functions*.

.. automodule:: xoa_driver.lli
   :members:
   :no-undoc-members: