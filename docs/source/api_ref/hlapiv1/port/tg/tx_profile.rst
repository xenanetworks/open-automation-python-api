TX Profile
=========================


TPLD Mode
-----------
Sets the size of the Xena Test Payload (TPLD) used to track streams, perform
latency measurements etc. Default is "Normal", which is a 20 byte TPLD. "Micro"
is a condensed version, which is useful when generating very small packets with
relatively long headers (like IPv6). It has the following characteristics
compared to the "normal" TPLD. When the TPLDMODE is changed, it will affect ALL
streams on the port. 1) Only 6 byte long. 2) Less accurate mechanism to separate
Xena-generated packets from other packets is the network - it is recommended not
to have too much other traffic going into the receive Xena port, when micro TPLD
is used. 3) No sequence checking (packet loss or packet misordering). The number
of received packets for each stream can still be compared to the number of
transmitted packets to detect packet loss once traffic has been stopped. Note:
Currently not available on M6SFP, M2SFPT, M6RJ45+/M2RJ45+, M2CFP40, M1CFP100,
M2SFP+4SFP

Corresponding CLI command: ``P_TPLDMODE``

.. code-block:: python

    # TPLD Mode
    await port.tpld_mode.set(mode=enums.TPLDMode.NORMAL)
    await port.tpld_mode.set_normal()
    await port.tpld_mode.set(mode=enums.TPLDMode.MICRO)
    await port.tpld_mode.set_micro()

    resp = await port.tpld_mode.get()
    resp.mode


TX Mode
-----------
The scheduling mode for outgoing traffic from the port, specifying how multiple
logical streams are merged onto one physical port. There are four primary modes:

* Normal Interleaved: The streams are treated independently, and are merged into a combined traffic pattern for the port, which honors each stream's ideal packet placements as well as possible. This is the default mode.

* Strict Uniform: This is a slight variation of normal interleaved scheduling, which emphasizes strict uniformity of the inter-packet-gaps as more important than hitting the stream rates absolutely precisely.

* Sequential: Each stream in turn contribute one or more packets, before continuing to the next stream, in a cyclical pattern. The count of packets for each stream is obtained from the PS_PACKETLIMIT command value for the stream. The individual rates for each stream are ignored, and instead the overall rate is determined at the port-level. This in turn determines the rates for each stream, taking into account their packet lengths and counts. The maximum number of packets in a cycle (i.e. the sum of PS_PACKETLIMIT for all enabled streams) is 500. If the packet number is larger than 500,  will be returned when attempting to start the traffic (P_TRAFFIC ON).

* Burst: When this mode is selected, frames from the streams on a port are sent as bursts as depicted below:
    * The Burst Period is defined in the P_TXBURSTPERIOD command.
    * For the individual streams the number of packets in a burst is defined by the PS_BURST command, while the Inter Packet Gap and the Inter Burst Gap are defined by the PS_BURSTGAP command.

Corresponding CLI command: ``P_TXMODE``

.. code-block:: python

    # TX Mode
    await port.tx_config.mode.set(mode=enums.TXMode.NORMAL)
    await port.tx_config.mode.set_normal()
    await port.tx_config.mode.set(mode=enums.TXMode.BURST)
    await port.tx_config.mode.set_burst()
    await port.tx_config.mode.set(mode=enums.TXMode.SEQUENTIAL)
    await port.tx_config.mode.set_sequential()
    await port.tx_config.mode.set(mode=enums.TXMode.STRICTUNIFORM)
    await port.tx_config.mode.set_strictuniform()

    resp = await port.tx_config.mode.get()
    resp.mode


Burst Period
------------
In Burst TX mode this command defines the time from the start of one sequence of
bursts (from a number of streams) to the start of next sequence of bursts.

.. note::
    
    Only used when Port TX Mode is "BURST".

Corresponding CLI command: ``P_TXBURSTPERIOD``

.. code-block:: python

    # Burst Period
    await port.tx_config.burst_period.set(burst_period=100)
    
    resp = await port.tx_config.burst_period.get()
    resp.burst_period


TX Delay
------------
Sets a variable delay from a traffic start command received by the port until
it starts transmitting. The delay is specified in multiples of 64 microseconds.
Valid values are 0-31250 (0 to 2,000,000 microseconds).

.. note::

    You must use C_TRAFFIC instead of P_TRAFFIC to start traffic for P_TXDELAY to take effect.

Corresponding CLI command: ``P_TXDELAY``

.. code-block:: python

    # TX Delay
    await port.tx_config.delay.set(delay_val=100)

    resp = await port.tx_config.delay.get()
    resp.delay_val


TX Enable
------------
Whether a port should enable its transmitter, or keep the outgoing link down.

Corresponding CLI command: ``P_TXENABLE``

.. code-block:: python

    # TX Enable
    await port.tx_config.enable.set(on_off=enums.OnOff.ON)
    await port.tx_config.enable.set(on_off=enums.OnOff.OFF)
    
    resp = await port.tx_config.enable.get()
    resp.on_off


Packet Limit
------------
The number of packets that will be transmitted from a port when traffic is
started on the port. A value of 0 or -1 makes the port transmit continuously.
Traffic from the streams on the port can however also be set to stop after
transmitting a number of packets.

Corresponding CLI command: ``P_TXPACKETLIMIT``

.. code-block:: python

    # Packet Limit
    await port.tx_config.packet_limit.set(packet_count_limit=1_000_000)
    
    resp = await port.tx_config.packet_limit.get()
    resp.packet_count_limit


Time Limit
------------
A port-level time-limit on how long it keeps transmitting when started. After
the elapsed time traffic must be stopped and restarted. This complements the
stream-level PS_PACKETLIMIT function.

Corresponding CLI command: ``P_TXTIMELIMIT``

.. code-block:: python

    # Time Limit
    await port.tx_config.time_limit.set(microseconds=1_000_000)
    
    resp = await port.tx_config.time_limit.get()
    resp.microseconds


TX Time Elapsed
---------------
How long the port has been transmitting, the elapsed time since traffic was
started.

Corresponding CLI command: ``P_TXTIME``

.. code-block:: python

    # TX Time Elapsed
    resp = await port.tx_config.time.get()
    resp.microseconds


Prepare TX
------------
Prepare port for transmission.

Corresponding CLI command: ``P_TXPREPARE``

.. code-block:: python

    # Prepare TX
    await port.tx_config.prepare.set()


Dynamic TX Rate
---------------
Controls if a port with speed higher than 10G supports dynamic changes when the traffic is running.

.. note::
    
    This command is only supported by ports with speed higher than 10G.

Corresponding CLI command: ``P_DYNAMIC``

.. code-block:: python
    
    # Dynamic Traffic Rate
    await port.dynamic.set(on_off=enums.OnOff.OFF)
    await port.dynamic.set_off()
    await port.dynamic.set(on_off=enums.OnOff.ON)
    await port.dynamic.set_on()
    
    resp = await port.dynamic.get()
    resp.on_off