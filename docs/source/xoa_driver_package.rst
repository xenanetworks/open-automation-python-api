.. _command_ref:


API Documentation
=============================

This section includes the Python module references of both XOA :ref:`HL-PYTHON <hl_api>` and :ref:`LL-PYTHON <ll_api>`.

High-Level Python Modules
-----------------------------

Module ``xoa_driver.testers``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the all the available *tester types* supported by XOA Python API.

.. automodule:: xoa_driver.testers
   :members:
   :inherited-members:


Module ``xoa_driver.modules``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the all the available *test module types* supported by XOA Python API.

.. automodule:: xoa_driver.modules
   :members:
   :inherited-members:


Module ``xoa_driver.ports``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains the all the available *test port types* supported by XOA Python API.

.. automodule:: xoa_driver.ports
   :members:
   :inherited-members:


Module ``xoa_driver.utils``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains some *helper functions*.

.. automodule:: xoa_driver.utils
   :members:


Module ``xoa_driver.enums``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains available enumeration types and server response statuses.

.. automodule:: xoa_driver.enums
   :members:


Module ``xoa_driver.exceptions``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This module contains all exception classes that can be propagated to the upper level.

.. automodule:: xoa_driver.exceptions
   :members:


Low-Level Python Modules
-----------------------------

L23 - Basic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Module ``xoa_driver.lli.commands.c_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **chassis commands** that deal with basic information and configuration of the chassis itself (rather than its modules and test ports), as well as overall control of the scripting session. The chassis command names all have the form ``C_xxxx`` and use neither a module index nor a port index.

.. automodule:: xoa_driver.internals.core.commands.c_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.m_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 module commands** that deal with basic information about, and configuration of the test modules. The module command names all have the form ``M_<xxx>`` and require a module index id.

.. automodule:: xoa_driver.internals.core.commands.m_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.p_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port commands** that deal with basic information about, and configuration of L23 test ports. The L23 port command names all have the form ``P_<xxx>`` and require a module index id and a port index id. In general, port commands cannot be changed while traffic is on. Additionally, every stream must be disabled before changing parameters that affect the bandwidth of the port.

.. automodule:: xoa_driver.internals.core.commands.p_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.ps_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 stream commands** deal with configuration of the traffic streams transmitted from a L23 port. The stream command names all have the form ``PS_<xxx>`` and require both a module index id and a port index id, as well as a sub-index id identifying a particular stream.

.. rubric:: General Information

*Enabling Traffic*

Whether the port is actually transmitting packets is controlled both by the ``P_TRAFFIC`` command for the parent port and by the ``PS_ENABLE`` command for the stream.

While the parent port is transmitting, the parameters of any enabled stream cannot be changed.

*Stream Test Payload Data (TPLD)*

Each Xena test packet contains a special proprietary data area called the *Test Payload Data* (TPLD), which contains various information about the packet. The TPLD is located just before the Ethernet FCS and consists of the following sections:

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
The TPLD function can also be completely disabled for any given stream by setting the Test Payload ID (TID) value for the stream to the value -1.

.. rubric:: Minimum Packet Size Considerations

The stream will generally accept any configuration and attempt to transmit packets according to the configuration. In order for the various Xena stream features to work correctly certain aspects about the minimum packet size used must be observed.

The minimum packet size must obviously be large enough to accommodate the defined ``protocol headers + the final Ethernet FCS field``.

If the TPLD function explained above is enabled then each packet must also be able to contain the TPLD area (20, 22 or 6 bytes depending on the configuration).

If the stream payload type is set to ``Incrementing``, then an additional minimum payload area of 2 bytes is needed. Otherwise excessive payload errors will be reported. This is however not necessary if the ``P_CHECKSUM offset`` (Payload Checksum Offset) option is enabled on the parent port as this will override the payload integrity check implied by the ``Incrementing`` payload type.


.. automodule:: xoa_driver.internals.core.commands.ps_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pp_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 high-speed port commands** that provide configuration and status for the Gigabit Attachment Unit Interface (CAUI) physical coding sublayer used by 40G, 50G, 100G, 200G, 400G and 800G ports. The data is broken down into a number of lower-speed lanes. For 40G there are 4 lanes of 10 Gbps each. For 100G there are 20 lanes of 5 Gbps each. Within each lane the data is broken down into 66-bit code-words.

During transport, the lanes may be swapped and skewed with respect to each other. To deal with this, each lane contains marker words with a virtual lane index id. The commands are indexed with a physical lane index that corresponds to a fixed numbering of the underlying fibers or wavelengths.

The lanes can also be put into Pseudorandom Binary Sequence (PRBS) mode where they transmit a bit pattern used for diagnosing fiber-level problems, and the receiving side can lock to these patterns.

Errors can be injected both at the CAUI level and at the bit level.

The high-speed port command names all have the form ``PP_<xxx>`` and require a module index id and a port index id, and most also require a physical lane index id.


.. automodule:: xoa_driver.internals.core.commands.pp_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pt_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port TX statistics commands** that provide quantitative information about the transmitted packets on a port.

The command names all have the form ``PT_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific transmitted stream also have a sub-index id.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

.. automodule:: xoa_driver.internals.core.commands.pt_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pr_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port RX statistics commands** that provide quantitative information about the received packets on a port.

The command names all have the form ``PR_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific received test payload id and a specific filter also have a sub-index id.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

.. automodule:: xoa_driver.internals.core.commands.pr_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pc_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port capture commands** that deal with configuration of the capture criteria and inspection of the captured data from a port.

Whether the port is enabled for capturing packets is specified by the ``P_CAPTURE`` command. Captured packets are indexed starting from 0, and are stored in a buffer that is cleared before capture starts. While on, the capture configuration parameters cannot be changed.

The capture command names all have the form ``PC_<xxx>`` and require both a module index id and a port index id. The per-packet parameters also use a sub-index identifying a particular packet in the capture buffer.

.. automodule:: xoa_driver.internals.core.commands.pc_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pd_commands``
""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port histogram commands** that deal with configuration of data collection and retrieval of samples from a port.

The histogram command names all have the form ``PD_<xxx>`` and require both a module index id and a port index id, as well as a sub-index identifying a particular histogram.

A histogram has a number of *buckets* and counts the packets transmitted or received on a port, possibly limited to those with a particular test payload id. The packet length, inter-frame gap preceding it, or its latency is measured, and the bucket whose range contains this value is incremented.

While a histogram is actively collecting samples its parameters cannot be changed.

.. automodule:: xoa_driver.internals.core.commands.pd_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pf_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port filter commands** that deal with configuration of the filters on the received traffic of a port.

The filter command names all have the form ``PF_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular filter.

Each filter specifies a compound Boolean condition on these true/false values to determine if the filter as a whole is true/false.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. automodule:: xoa_driver.internals.core.commands.pf_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pl_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port length term commands** that deal with configuration of the length term on the received traffic of a port.

The length term command names all have the form ``PL_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular length term.

The length terms provide basic true/false indications for each packet received on the port.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. automodule:: xoa_driver.internals.core.commands.pl_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pm_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port match term commands** that deal with configuration of the length term on the received traffic of a port.

The match term command names all have the form ``PM_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular match term.

The match terms provide basic true/false indications for each packet received on the port.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. automodule:: xoa_driver.internals.core.commands.pm_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.px_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L23 port transceiver commands** that deal with access to the register interfaces of the transceiver on a port.

.. automodule:: xoa_driver.internals.core.commands.px_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Supporting Classes
""""""""""""""""""""""""""""""""""""

.. automodule:: xoa_driver.lli
   :members:


L23 - TSN (under construction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This section is under construction, and will be completed in the next release.

Module ``xoa_driver.lli.commands.xp_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **TSN extension for L23 port commands**.

.. automodule:: xoa_driver.internals.core.commands.xp_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.xpd_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **TSN extension for L23 port histogram commands**.

.. automodule:: xoa_driver.internals.core.commands.xpd_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


L47 (under construction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This section is under construction, and will be completed in the next release.

Module ``xoa_driver.lli.commands.m4_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L47 module commands**.

.. automodule:: xoa_driver.internals.core.commands.m4_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.m4e_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L47 module packet engine commands**.

.. automodule:: xoa_driver.internals.core.commands.m4e_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.p4_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L47 port commands**.

.. automodule:: xoa_driver.internals.core.commands.p4_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.p4e_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L47 port packet engine commands**.

.. automodule:: xoa_driver.internals.core.commands.p4e_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.p4g_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **L47 connection group commands** that deal with configuration of TCP connections and are specific to L47. The commands have the form ``P4G_<xxx>`` and require a module index id and a port index id, and a connection group index id.


.. automodule:: xoa_driver.internals.core.commands.p4g_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Impairment (under construction)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   This section is under construction, and will be completed in the next release.

Module ``xoa_driver.lli.commands.pe_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **impairment port flow commands**.

.. automodule:: xoa_driver.internals.core.commands.pe_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pec_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **impairment port custome distribution commands**.

.. automodule:: xoa_driver.internals.core.commands.pec_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.ped_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **impairment port distribution commands**.

.. automodule:: xoa_driver.internals.core.commands.ped_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr


Module ``xoa_driver.lli.commands.pef_commands``
""""""""""""""""""""""""""""""""""""""""""""""""

This module contains the **impairment port flow filter commands**.

.. automodule:: xoa_driver.internals.core.commands.pef_commands
   :members:
   :no-undoc-members:
   :exclude-members: GetDataAttr, SetDataAttr

