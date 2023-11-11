Control
=========================

Inter-frame Gap
---------------
The minimum gap between packets in the traffic generated for a port. The gap includes the Ethernet preamble.

Corresponding CLI command: ``P_INTERFRAMEGAP``

.. code-block:: python

    # Inter-frame Gap
    await port.interframe_gap.set(min_byte_count=20)

    resp = await port.interframe_gap.get()
    resp.min_byte_count


PAUSE Frames
---------------
Whether a port responds to incoming Ethernet PAUSE frames by holding back outgoing traffic.

Corresponding CLI command: ``P_PAUSE``

.. code-block:: python

    # PAUSE Frames
    await port.pause.set(on_off=enums.OnOff.ON)
    await port.pause.set_on()
    await port.pause.set(on_off=enums.OnOff.OFF)
    await port.pause.set_off()

    resp = await port.pause.get()
    resp.on_off


Auto-Train
-----------
The interval between sending out training packets, allowing a switch to learn
the port's MAC address. Layer-2 switches configure themselves automatically by
detecting the source MAC addresses of packets received on each port. If a port
only receives, and does not itself transmit test traffic, then the switch will
never learn its MAC address. Also, if transmission is very rare the switch will
age-out the learned MAC address. By setting the auto-train interval you instruct
the port to send switch training packets, independent of whether the port is
transmitting test traffic.

Corresponding CLI command: ``P_AUTOTRAIN``

.. code-block:: python

    # Auto-Train
    await port.autotrain.set(interval=1)

    resp = await port.autotrain.get()
    resp.interval


Gap Monitor
-----------
The gap-start and gap-stop criteria for the port's gap monitor. The gap monitor
expects a steady stream of incoming packets, and detects larger-than-allowed
gaps between them. Once a gap event is encountered it requires a certain number
of consecutive packets below the threshold to end the event.

Corresponding CLI command: ``P_GAPMONITOR``

.. code-block:: python

    # Gap Monitor
    await port.gap_monitor.set(start=100, stop=10)
    
    resp = await port.gap_monitor.get()
    resp.start
    resp.stop


Priority Flow Control
---------------------
This setting control whether a port responds to incoming Ethernet Priority Flow Control (PFC) frames, by holding back outgoing traffic for that priority.

Corresponding CLI command: ``P_PFCENABLE``

.. code-block:: python

    # Priority Flow Control
    await port.pfc_enable.set(
        cos_0=enums.OnOff.ON,
        cos_1=enums.OnOff.OFF,
        cos_2=enums.OnOff.ON,
        cos_3=enums.OnOff.OFF,
        cos_4=enums.OnOff.ON,
        cos_5=enums.OnOff.OFF,
        cos_6=enums.OnOff.ON,
        cos_7=enums.OnOff.OFF,
        )
    
    resp = await port.pfc_enable.get()
    resp.cos_0
    resp.cos_1
    resp.cos_2
    resp.cos_3
    resp.cos_4
    resp.cos_5
    resp.cos_6
    resp.cos_7


Loopback
--------
The loopback mode for a port. Ports can be configured to perform two different
kinds of loopback: (1) External RX-to-TX loopback, where the received packets
are re-transmitted immediately. The packets are still processed by the receive
logic, and can be captured and analyzed. (2) Internal TX-to-RX loopback, where
the transmitted packets are received directly by the port itself. This is mainly
useful for testing the generated traffic patterns before actual use.

Corresponding CLI command: ``P_LOOPBACK``

.. code-block:: python

    # Loopback
    await port.loop_back.set(mode=enums.LoopbackMode.L1RX2TX)
    await port.loop_back.set_l1rx2tx()
    await port.loop_back.set(mode=enums.LoopbackMode.L2RX2TX)
    await port.loop_back.set_l2rx2tx()
    await port.loop_back.set(mode=enums.LoopbackMode.L3RX2TX)
    await port.loop_back.set_l3rx2tx()
    await port.loop_back.set(mode=enums.LoopbackMode.NONE)
    await port.loop_back.set_none()
    await port.loop_back.set(mode=enums.LoopbackMode.PORT2PORT)
    await port.loop_back.set_port2port()
    await port.loop_back.set(mode=enums.LoopbackMode.TXOFF2RX)
    await port.loop_back.set_txoff2rx()
    await port.loop_back.set(mode=enums.LoopbackMode.TXON2RX)
    await port.loop_back.set_txon2rx()

    resp = await port.loop_back.get()
    resp.mode


BRR Mode
--------
Selects the Master/Slave setting of 100 Mbit/s, 1000 Mbit/s BroadR-Reach copper interfaces.

Corresponding CLI command: ``P_BRRMODE``

.. code-block:: python

    # BRR Mode
    await port.brr_mode.set(mode=enums.BRRMode.MASTER)
    await port.brr_mode.set_master()
    await port.brr_mode.set(mode=enums.BRRMode.SLAVE)
    await port.brr_mode.set_slave()

    resp = await port.brr_mode.get()
    resp.mode


MDI/MDIX Mode
-------------
Selects the MDI/MDIX behavior of copper interfaces.

Corresponding CLI command: ``P_MDIXMODE``

.. code-block:: python

    # MDI/MDIX Mode
    await port.mdix_mode.set(mode=enums.MDIXMode.AUTO)
    await port.mdix_mode.set_auto()
    await port.mdix_mode.set(mode=enums.MDIXMode.MDI)
    await port.mdix_mode.set_mdi()
    await port.mdix_mode.set(mode=enums.MDIXMode.MDIX)
    await port.mdix_mode.set_mdix()

    resp = await port.mdix_mode.get()
    resp.mode