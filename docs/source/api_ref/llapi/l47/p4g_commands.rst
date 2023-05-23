Connection Group Classes
=================================

This module contains the **L47 connection group classes** that deal with configuration of TCP connections and are specific to L47. The commands have the form ``P4G_<xxx>`` and require a module index id and a port index id, and a connection group index id.

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

* ``RAW``, which means that the TCP connections transmit and receive user defined raw data. The contents of the raw TCP payload can be configured using the P4G_RAW_PAYLOAD command. Raw TCP payload can also be specified  as random and incrementing data.

Using test application ``RAW``, the CG must also be configured with a test scenario, which defines the data flow between the TCP client and server. Currently the following test scenarios can be configured: ``download``, ``upload``, and ``both``.

By combining several :term:`CGs<CG>` on a port, it is possible to create more complex traffic scenarios and more complex :term:`load profile` shapes than the individual :term:`CG` allows.

-------

.. currentmodule:: xoa_driver.internals.commands.p4g_commands


P4G_INDICES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_INDICES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_CREATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_CREATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_DELETE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_DELETE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_COMMENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_COMMENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_CLEAR_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_CLEAR_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_ROLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_ROLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_CLIENT_RANGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_CLIENT_RANGE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_SERVER_RANGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_SERVER_RANGE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_LP_TIME_SCALE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_LP_TIME_SCALE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_LP_SHAPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_LP_SHAPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_NAT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_NAT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RTT_VALUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RTT_VALUE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_STATE_CURRENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_STATE_CURRENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_STATE_TOTAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_STATE_TOTAL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_STATE_RATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_STATE_RATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RX_PAYLOAD_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RX_PAYLOAD_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_TX_PAYLOAD_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_TX_PAYLOAD_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RETRANSMIT_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RETRANSMIT_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_ERROR_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_ERROR_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IP_DS_TYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IP_DS_TYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IP_DS_VALUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IP_DS_VALUE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IP_DS_MASK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IP_DS_MASK
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IP_DS_MINMAX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IP_DS_MINMAX
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IP_DS_STEP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IP_DS_STEP
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_MSS_TYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_MSS_TYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_MSS_MINMAX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_MSS_MINMAX
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_MSS_VALUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_MSS_VALUE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_WINDOW_SIZE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_WINDOW_SIZE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_DUP_THRES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_DUP_THRES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_SYN_RTO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_SYN_RTO
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RTO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RTO
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_PACKET_SIZE_TYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_PACKET_SIZE_TYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_PACKET_SIZE_MINMAX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_PACKET_SIZE_MINMAX
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_PACKET_SIZE_VALUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_PACKET_SIZE_VALUE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_CONGESTION_MODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_CONGESTION_MODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_WINDOW_SCALING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_WINDOW_SCALING
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RTO_MINMAX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RTO_MINMAX
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RTO_PROLONGED_MODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RTO_PROLONGED_MODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_ICWND_CALC_METHOD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_ICWND_CALC_METHOD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_ISSTHRESH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_ISSTHRESH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_ACK_FREQUENCY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_ACK_FREQUENCY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_ACK_TIMEOUT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_ACK_TIMEOUT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_L2_CLIENT_MAC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_L2_CLIENT_MAC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_L2_SERVER_MAC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_L2_SERVER_MAC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_L2_USE_ADDRESS_RES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_L2_USE_ADDRESS_RES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_L2_USE_GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_L2_USE_GW
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_L2_GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_L2_GW
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_L2_IPV6_GW
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_L2_IPV6_GW
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TEST_APPLICATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TEST_APPLICATION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_TEST_SCENARIO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_TEST_SCENARIO
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_PAYLOAD_TYPE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_PAYLOAD_TYPE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_PAYLOAD_TOTAL_LEN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_PAYLOAD_TOTAL_LEN
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_PAYLOAD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_PAYLOAD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_PAYLOAD_REPEAT_LEN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_PAYLOAD_REPEAT_LEN
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_HAS_DOWNLOAD_REQ
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_HAS_DOWNLOAD_REQ
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_CLOSE_CONN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_CLOSE_CONN
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_UTILIZATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_UTILIZATION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_DOWNLOAD_REQUEST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_DOWNLOAD_REQUEST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_TX_DURING_RAMP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_TX_DURING_RAMP
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_TX_TIME_OFFSET
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_TX_TIME_OFFSET
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_BURSTY_TX
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_BURSTY_TX
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_BURSTY_CONF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_BURSTY_CONF
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_VLAN_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_VLAN_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_VLAN_TCI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_VLAN_TCI
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TIME_HIST_CONF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TIME_HIST_CONF
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_PAYLOAD_HIST_CONF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_PAYLOAD_HIST_CONF
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TRANSACTION_HIST_CONF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TRANSACTION_HIST_CONF
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_RX_PAYLOAD_LEN
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_RX_PAYLOAD_LEN
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_REQUEST_REPEAT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_REQUEST_REPEAT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_CONN_INCARNATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_CONN_INCARNATION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_CONN_REPETITIONS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_CONN_REPETITIONS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RAW_CONN_LIFETIME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RAW_CONN_LIFETIME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IP_VERSION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IP_VERSION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IPV6_CLIENT_RANGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IPV6_CLIENT_RANGE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IPV6_SERVER_RANGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IPV6_SERVER_RANGE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IPV6_TRAFFIC_CLASS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IPV6_TRAFFIC_CLASS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_IPV6_FLOW_LABEL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_IPV6_FLOW_LABEL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_L4_PROTOCOL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_L4_PROTOCOL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_ESTABLISH_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_ESTABLISH_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_CLOSE_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_CLOSE_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RX_TOTAL_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RX_TOTAL_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RX_GOOD_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RX_GOOD_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_TX_TOTAL_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_TX_TOTAL_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_TX_GOOD_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_TX_GOOD_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_APP_REPLAY_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_APP_REPLAY_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_APP_TRANSACTION_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_APP_TRANSACTION_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_APP_TRANSACTION_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_APP_TRANSACTION_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_STATE_CURRENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_STATE_CURRENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_STATE_TOTAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_STATE_TOTAL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_STATE_RATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_STATE_RATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_RX_PAYLOAD_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_RX_PAYLOAD_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_TX_PAYLOAD_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_TX_PAYLOAD_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_RX_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_RX_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_TX_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_TX_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_RX_PACKET_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_RX_PACKET_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TCP_TX_PACKET_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TCP_TX_PACKET_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_RX_PACKET_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_RX_PACKET_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_UDP_TX_PACKET_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_UDP_TX_PACKET_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_CLEAR_POST_STAT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_CLEAR_POST_STAT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RECALC_TIME_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RECALC_TIME_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RECALC_PAYLOAD_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RECALC_PAYLOAD_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_RECALC_TRANSACTION_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_RECALC_TRANSACTION_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_REPLAY_FILE_INDICES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_REPLAY_FILE_INDICES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_REPLAY_FILE_NAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_REPLAY_FILE_NAME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_REPLAY_FILE_CLEAR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_REPLAY_FILE_CLEAR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_REPLAY_UTILIZATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_REPLAY_UTILIZATION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_REPLAY_USER_INCARNATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_REPLAY_USER_INCARNATION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_REPLAY_USER_REPETITIONS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_REPLAY_USER_REPETITIONS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_USER_STATE_CURRENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_USER_STATE_CURRENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_USER_STATE_TOTAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_USER_STATE_TOTAL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_USER_STATE_RATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_USER_STATE_RATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_CIPHER_SUITES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_CIPHER_SUITES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_MAX_RECORD_SIZE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_MAX_RECORD_SIZE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_CERTIFICATE_FILENAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_CERTIFICATE_FILENAME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_PRIVATE_KEY_FILENAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_PRIVATE_KEY_FILENAME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_DHPARAMS_FILENAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_DHPARAMS_FILENAME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_CLOSE_NOTIFY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_CLOSE_NOTIFY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_ALERT_WARNING_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_ALERT_WARNING_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_ALERT_FATAL_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_ALERT_FATAL_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_STATE_CURRENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_STATE_CURRENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_STATE_TOTAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_STATE_TOTAL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_STATE_RATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_STATE_RATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_RX_PAYLOAD_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_RX_PAYLOAD_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_TX_PAYLOAD_COUNTERS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_TX_PAYLOAD_COUNTERS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_RX_PAYLOAD_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_RX_PAYLOAD_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_TX_PAYLOAD_BYTES_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_TX_PAYLOAD_BYTES_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_HANDSHAKE_HIST
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_HANDSHAKE_HIST
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_SERVER_NAME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_SERVER_NAME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_PROTOCOL_VER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_PROTOCOL_VER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


P4G_TLS_MIN_REQ_PROTOCOL_VER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: P4G_TLS_MIN_REQ_PROTOCOL_VER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

