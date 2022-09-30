.. _l23_p_commands:

Port
=================================

This module contains the **L23 port commands** that deal with basic information about, and configuration of L23 test ports. The L23 port command names all have the form ``P_<xxx>`` and require a module index id and a port index id. In general, port commands cannot be changed while traffic is on. Additionally, every stream must be disabled before changing parameters that affect the bandwidth of the port.

-------

.. currentmodule:: xoa_driver.internals.core.commands.p_commands


P_RESERVATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RESERVATION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RESERVEDBY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RESERVEDBY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RESET
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RESET
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_CAPABILITIES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_CAPABILITIES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_INTERFACE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_INTERFACE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_SPEEDSELECTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_SPEEDSELECTION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_SPEED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_SPEED
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RECEIVESYNC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RECEIVESYNC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_COMMENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_COMMENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_SPEEDREDUCTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_SPEEDREDUCTION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_INTERFRAMEGAP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_INTERFRAMEGAP
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MACADDRESS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MACADDRESS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_IPADDRESS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_IPADDRESS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_ARPREPLY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_ARPREPLY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_PINGREPLY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_PINGREPLY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_PAUSE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_PAUSE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RANDOMSEED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RANDOMSEED
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LOOPBACK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LOOPBACK
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_FLASH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_FLASH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TRAFFIC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TRAFFIC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_CAPTURE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_CAPTURE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_XMITONE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_XMITONE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LATENCYOFFSET
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LATENCYOFFSET
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LATENCYMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LATENCYMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_AUTOTRAIN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_AUTOTRAIN
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_UAT_MODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_UAT_MODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_UAT_FLR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_UAT_FLR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MIXWEIGHTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MIXWEIGHTS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MDIXMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MDIXMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TRAFFICERR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TRAFFICERR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_GAPMONITOR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_GAPMONITOR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_CHECKSUM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_CHECKSUM
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_STATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_STATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_AUTONEGSELECTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_AUTONEGSELECTION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MIXLENGTH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MIXLENGTH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_ARPRXTABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_ARPRXTABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_NDPRXTABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_NDPRXTABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MULTICAST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MULTICAST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MULTICASTEXT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MULTICASTEXT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MCSRCLIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MCSRCLIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MULTICASTHDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MULTICASTHDR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RATEFRACTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RATEFRACTION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RATEPPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RATEPPS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RATEL2BPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RATEL2BPS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_PAYLOADMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_PAYLOADMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_BRRMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_BRRMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_MAXHEADERLENGTH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_MAXHEADERLENGTH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXTIMELIMIT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXTIMELIMIT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXTIME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXTIME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_XMITONETIME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_XMITONETIME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_IPV6ADDRESS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_IPV6ADDRESS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_ARPV6REPLY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_ARPV6REPLY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_PINGV6REPLY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_PINGV6REPLY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_ERRORS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_ERRORS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXPREPARE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXPREPARE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXDELAY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXDELAY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LPENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LPENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LPTXMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LPTXMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LPSTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LPSTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LPPARTNERAUTONEG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LPPARTNERAUTONEG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LPSNRMARGIN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LPSNRMARGIN
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LPRXPOWER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LPRXPOWER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_FAULTSIGNALING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_FAULTSIGNALING
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_FAULTSTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_FAULTSTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TPLDMODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TPLDMODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_LPSUPPORT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_LPSUPPORT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXPACKETLIMIT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXPACKETLIMIT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TCVRSTATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TCVRSTATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_DYNAMIC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_DYNAMIC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_PFCENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_PFCENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXBURSTPERIOD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXBURSTPERIOD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXRUNTLENGTH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXRUNTLENGTH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RXRUNTLENGTH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RXRUNTLENGTH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RXRUNTLEN_ERRS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RXRUNTLEN_ERRS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_TXPREAMBLE_REMOVE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_TXPREAMBLE_REMOVE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_RXPREAMBLE_INSERT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_RXPREAMBLE_INSERT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P_SPEEDS_SUPPORTED
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P_SPEEDS_SUPPORTED
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr
