TX Profile
=========================

Rate Fraction
---------------
The rate of the traffic transmitted for a stream expressed in millionths of the
effective rate for the port. The bandwidth consumption includes the inter-frame
gap and is independent of the length of the packets generated for the stream.
The sum of the bandwidth consumption for all the enabled streams must not exceed
the effective rate for the port. Setting this command also instructs the
Manager to attempt to keep the rate-percentage unchanged in case it has to cap
stream rates. Get value is only valid if the rate was last set using this
command.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_RATEFRACTION`

.. code-block:: python

    # Rate Fraction
    await stream.rate.fraction.set(stream_rate_ppm=1_000_000)

    resp = await stream.rate.fraction.get()
    resp.stream_rate_ppm


Packet Rate
-------------------------
The rate of the traffic transmitted for a stream expressed in packets per
second. The bandwidth consumption is heavily dependent on the length of the
packets generated for the stream, and also on the inter-frame gap for the port.
The sum of the bandwidth consumption for all the enabled streams must not exceed
the effective rate for the port. Setting this command also instructs the
Manager to attempt to keep the packets-per-second unchanged in case it has to
cap stream rates. Get value is only valid if the rate was the last set using
this command.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_RATEPPS`

.. code-block:: python

    a# Packet Rate
    await stream.rate.pps.set(stream_rate_pps=1_000)
    
    resp = await stream.rate.pps.get()
    resp.stream_rate_pps


Bit Rate L2
--------------------------
The rate of the traffic transmitted for a stream, expressed in units of bits-
per-second at layer-2, thus including the Ethernet header but excluding the
inter-frame gap. The bandwidth consumption is somewhat dependent on the length
of the packets generated for the stream, and also on the inter-frame gap for the
port. The sum of the bandwidth consumption for all the enabled streams must not
exceed the effective rate for the port. Setting this command also instructs
the Manager to attempt to keep the layer-2 bps rate unchanged in case it has to
cap stream rates. Get value is only valid if the rate was the last set using
this command.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_RATEL2BPS`

.. code-block:: python

    # Bit Rate L2
    await stream.rate.l2bps.set(l2_bps=1_000_000)
    
    resp = await stream.rate.l2bps.get()
    resp.l2_bps


Packet Limit
--------------------------
The rate of the traffic transmitted for a stream expressed in packets per
second. The bandwidth consumption is heavily dependent on the length of the
packets generated for the stream, and also on the inter-frame gap for the port.
The sum of the bandwidth consumption for all the enabled streams must not exceed
the effective rate for the port. Setting this command also instructs the
Manager to attempt to keep the packets-per-second unchanged in case it has to
cap stream rates. Get value is only valid if the rate was the last set using
this command.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_RATEPPS`

.. code-block:: python

    # Packet Limit
    await stream.packet.limit.set(packet_count=1_000)
    
    resp = await stream.packet.limit.get()
    resp.packet_count


Burst Size and Density
--------------------------
The burstiness of the traffic transmitted for a stream, expressed in terms of
the number of packets in each burst, and how densely they are packed together.
The burstiness does not affect the bandwidth consumed by the stream, only the
spacing between the packets. A density value of 100 means that the packets are
packed tightly together, only spaced by the minimum inter-frame gap. A value of
0 means even, non-bursty, spacing. The exact spacing achieved depends on the
other enabled streams of the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_BURST`

.. code-block:: python

    # Burst Size and Density
    await stream.burst.burstiness.set(size=20, density=80)

    resp = await stream.burst.burstiness.get()
    resp.size
    resp.density


Inter Burst/Packet Gap
--------------------------
When the port is in in Burst TX mode, this command defines the gap between packets in a burst
(inter-packet gap) and the gap after a burst defined in one stream stops until a
burst defined in the next stream starts (inter-burst gap).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_BURSTGAP`

.. code-block:: python

    # Inter Burst/Packet Gap
    await stream.burst.gap.set(inter_packet_gap=30, inter_burst_gap=30)
    
    resp = await stream.burst.gap.get()
    resp.inter_packet_gap
    resp.inter_burst_gap


Priority Flow
--------------------------
Set and get the Priority Flow Control (PFC) Cos value of a stream.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_PFCPRIORITY`

.. code-block:: python

    # Priority Flow
    await stream.priority_flow.set(cos=enums.PFCMode.ZERO)
    await stream.priority_flow.set(cos=enums.PFCMode.ONE)
    await stream.priority_flow.set(cos=enums.PFCMode.TWO)
    await stream.priority_flow.set(cos=enums.PFCMode.THREE)
    await stream.priority_flow.set(cos=enums.PFCMode.FOUR)
    await stream.priority_flow.set(cos=enums.PFCMode.FIVE)
    await stream.priority_flow.set(cos=enums.PFCMode.SIX)
    await stream.priority_flow.set(cos=enums.PFCMode.SEVEN)
    await stream.priority_flow.set(cos=enums.PFCMode.VLAN_PCP)

    resp = await stream.priority_flow.get()
    resp.cos
