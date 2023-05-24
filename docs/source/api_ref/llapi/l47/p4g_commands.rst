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

.. automodule:: xoa_driver.internals.commands.p4g_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__

