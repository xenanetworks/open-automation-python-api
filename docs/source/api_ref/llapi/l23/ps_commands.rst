Stream Classes
=================================

This module contains the **L23 stream classes** deal with configuration of the traffic streams transmitted from a L23 port. The stream command names all have the form ``PS_<xxx>`` and require both a module index id and a port index id, as well as a sub-index identifying a particular stream.

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


-------

.. currentmodule:: xoa_driver.internals.commands.ps_commands

PS_INDICES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_INDICES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_CREATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_CREATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_DELETE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_DELETE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_PACKETLIMIT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_PACKETLIMIT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_COMMENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_COMMENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_TPLDID
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_TPLDID
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_INSERTFCS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_INSERTFCS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_ARPREQUEST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_ARPREQUEST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_PINGREQUEST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_PINGREQUEST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_MODIFIEREXTRANGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_MODIFIEREXTRANGE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_MODIFIERRANGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_MODIFIERRANGE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_RATEFRACTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_RATEFRACTION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_RATEPPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_RATEPPS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_RATEL2BPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_RATEL2BPS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_BURST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_BURST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_PACKETHEADER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_PACKETHEADER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_HEADERPROTOCOL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_HEADERPROTOCOL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_MODIFIERCOUNT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_MODIFIERCOUNT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_MODIFIER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_MODIFIER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_PACKETLENGTH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_PACKETLENGTH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_PAYLOAD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_PAYLOAD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_IPV4GATEWAY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_IPV4GATEWAY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_IPV6GATEWAY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_IPV6GATEWAY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_BURSTGAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_BURSTGAP
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_INJECTFCSERR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_INJECTFCSERR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_INJECTSEQERR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_INJECTSEQERR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_INJECTMISERR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_INJECTMISERR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_INJECTPLDERR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_INJECTPLDERR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_INJECTTPLDERR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_INJECTTPLDERR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_MODIFIEREXT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_MODIFIEREXT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_MODIFIEREXTCOUNT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_MODIFIEREXTCOUNT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_CDFOFFSET
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_CDFOFFSET
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_CDFCOUNT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_CDFCOUNT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_CDFDATA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_CDFDATA
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_EXTPAYLOAD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_EXTPAYLOAD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_PFCPRIORITY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_PFCPRIORITY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PS_AUTOADJUST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PS_AUTOADJUST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr
