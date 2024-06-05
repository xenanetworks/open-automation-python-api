Traffic Control
=========================

Rate Percent
------------
The port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in millionths of the effective rate for the port. The bandwidth consumption includes the inter-frame gaps, and does not depend on the length of the packets for the streams.

Corresponding CLI command: ``P_RATEFRACTION``

.. code-block:: python

    # Traffic Control - Rate Percent
    await port.rate.fraction.set(port_rate_ppm=1_000_000)
    
    resp = await port.rate.fraction.get()
    resp.port_rate_ppm


Rate L2 Bits Per Second
-----------------------
The port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in units of bits per-second at layer-2, thus including the Ethernet header but excluding the inter-frame gap. The bandwidth consumption is somewhat dependent on the length of the packets generated for the stream, and also on the inter-frame gap for the port.

Corresponding CLI command: ``P_RATEL2BPS``

.. code-block:: python

    # Traffic Control - Rate L2 Bits Per Second
    await port.rate.l2_bps.set(port_rate_bps=1_000_000)

    resp = await port.rate.l2_bps.get()
    resp.port_rate_bps


Rate Frames Per Second
----------------------
The port-level rate of the traffic transmitted for a port in sequential tx mode, expressed in packets per second. The bandwidth consumption is heavily dependent on the length of the packets generated for the streams, and also on the inter-frame gap for the port.

Corresponding CLI command: ``P_RATEPPS``

.. code-block:: python

    # Traffic Control - Rate Frames Per Second
    await port.rate.pps.set(port_rate_pps=10_000)
    
    resp = await port.rate.pps.get()
    resp.port_rate_pps


Start and Stop
----------------
Whether a port is transmitting packets. When on, the port generates a sequence
of packets with contributions from each stream that is enabled. The streams are configured using the PS_xxx parameters.

.. note::

    If any of the specified packet sizes cannot fit into the packet generator, this command will return FAILED and not start the traffic.
    While traffic is on the streams for this port cannot be enabled or disabled, and the configuration of those streams that are enabled cannot be changed.

Corresponding CLI command: ``P_TRAFFIC``

.. code-block:: python

    # Traffic Control - Start and Stop
    await port.traffic.state.set(on_off=enums.StartOrStop.START)
    await port.traffic.state.set_start()
    await port.traffic.state.set(on_off=enums.StartOrStop.STOP)
    await port.traffic.state.set_stop()

    resp = await port.traffic.state.get()
    resp.on_off


Traffic Error
----------------------------
Obtain the traffic error which has occurred in the last ``*_TRAFFIC`` or ``C_TRAFFICSYNC`` command.

Corresponding CLI command: ``P_TRAFFICERR``

.. code-block:: python

    # Traffic Control - Traffic Error
    resp = await port.traffic.error.get()
    resp.error


Single Frame TX
----------------------------
Transmits a single packet from a port, independent of the stream definitions,
and independent of whether traffic is on. A valid Frame Check Sum is written
into the final four bytes.

Corresponding CLI command: ``P_XMITONE``

.. code-block:: python

    # Traffic Control - Single Frame TX
    await port.tx_single_pkt.send.set(hex_data=Hex("00000000000102030405060800FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"))


Single Frame Time
----------------------------
The time at which the latest packet was transmitted using the P_XMITONE command. The time reference is the same used by the time stamps of captured packets.

Corresponding CLI command: ``P_XMITONETIME``

.. code-block:: python

    # Traffic Control - Single Frame Time
    resp = await port.tx_single_pkt.time.get()
    resp.nanoseconds
