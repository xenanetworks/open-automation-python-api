Port Classes
=================================

This module contains the **L47 port classes**.

The Xena L47 test execution engine has seven states: ``off``, ``prepare``, ``prepare_rdy``, ``prerun``, ``prerun_rdy``, ``running`` and ``stopped``. Traffic is generated in the ``prerun`` and running states only, and configuration of parameters is only valid in state ``off`` except for a few runtime options. Port traffic commands can be given with :class:`~xoa_driver.internals.core.commands.p4_commands.P4_TRAFFIC` and port state queried by :class:`~xoa_driver.internals.core.commands.p4_commands.P4_STATE`.

* ``off`` - default state. Entered from stopped or prepare on ``OFF`` command. This is the only state that allows configuration commands. :class:`~xoa_driver.internals.core.commands.p_commands.P_RESET` is also considered a configuration command. Upon entering off state, some internal ''house cleaning''' is done. For example: freeing TCP Connections, clearing test specific counters etc.

* ``prepare`` - this state is entered from state off on ``PREPARE`` command. Here internal data structures relevant for the test configuration are created.

* ``prepare_rdy`` - entered automatically after activities in prepare have completed successfully.

* ``prepare_fail`` - entered automatically from prepare, if an error occurs. An error could for example be failure to load a configured replay file.

* ``prerun`` - entered from ``prepare_ready`` on ``PRERUN`` command. If enabled, this is where ARP and NDP requests are sent.

* ``prerun_rdy`` - entered automatically after activities in prerun have completed.

* ``running`` - entered either from ``prepare_ready`` or ``prerun_ready`` on ``ON`` command. This is where TCP connections are established, payload is generated and connections are closed again.

* ``stopping`` - entered from ``running``, ``prerun_ready`` or ``prerun`` on ``STOP`` command. Stops Rx/Tx traffic. In the ``stopping`` state, post-test data are calculated and captured packets are saved to files.

* ``stopped`` - entered automatically after activities in ``stopping`` are complete. This is where you can read post-test statistics and extract captured packets.

-------

.. currentmodule:: xoa_driver.internals.core.commands.p4_commands


P4_TRAFFIC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_TRAFFIC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_STATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_STATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_CAPABILITIES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_CAPABILITIES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_STATE_STATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_STATE_STATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_VLAN_OFFLOAD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_VLAN_OFFLOAD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ARP_CONFIG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ARP_CONFIG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_NDP_CONFIG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_NDP_CONFIG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_CAPTURE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_CAPTURE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_CAPTURE_GET_FIRST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_CAPTURE_GET_FIRST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_CAPTURE_GET_NEXT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_CAPTURE_GET_NEXT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ETH_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ETH_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ETH_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ETH_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_PORT_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_PORT_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_PORT_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_PORT_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_PORT_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_PORT_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_TX_PACKET_SIZE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_TX_PACKET_SIZE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_RX_PACKET_SIZE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_RX_PACKET_SIZE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_TX_MTU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_TX_MTU
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_RX_MTU
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_RX_MTU
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_IPV4_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_IPV4_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_IPV4_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_IPV4_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_IPV4_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_IPV4_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_IPV6_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_IPV6_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_IPV6_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_IPV6_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_IPV6_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_IPV6_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ARP_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ARP_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ARP_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ARP_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ARP_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ARP_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_NDP_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_NDP_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_NDP_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_NDP_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_NDP_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_NDP_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ICMP_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ICMP_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ICMP_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ICMP_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ICMP_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ICMP_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_TCP_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_TCP_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_TCP_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_TCP_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_TCP_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_TCP_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_UDP_RX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_UDP_RX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_UDP_TX_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_UDP_TX_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_UDP_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_UDP_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_CLEAR_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_CLEAR_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_ETH_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_ETH_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_CLEAR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_CLEAR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_SPEEDSELECTION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_SPEEDSELECTION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_MAX_PACKET_RATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_MAX_PACKET_RATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_PCI_INFO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_PCI_INFO
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_FW_VER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_FW_VER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_DEV_NAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_DEV_NAME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_PORT_TYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_PORT_TYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_LICENSE_INFO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_LICENSE_INFO
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4_APTITUDES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4_APTITUDES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr



