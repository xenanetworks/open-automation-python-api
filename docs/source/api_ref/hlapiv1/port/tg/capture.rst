Capture
=========================

Trigger Criteria
----------------
The criteria for when to start and stop the capture process for a port. Even
when capture is enabled with ``P_CAPTURE``, the actual capturing of packets can be
delayed until a particular start criteria is met by a received packet.
Likewise, a stop criteria can be specified, based on a received packet. If no
explicit stop criteria is specified, capture  stops when the internal buffer
runs full. In buffer overflow situations, if there is an explicit  stop
criteria, then the latest packets will be retained (and the early ones
discarded),  and otherwise, the earliest packets are retained (and the later
ones discarded).

Corresponding CLI command: ``PC_TRIGGER``

.. seealso::

    Detailed script example can be found in `here <https://github.com/xenanetworks/open-automation-script-library/blob/main/packet_capture/packet_capture.py>`_

.. code-block:: python

    # Capture Trigger Criteria, 
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.ON, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FULL, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.ON, start_criteria_filter=0, stop_criteria=enums.StopTrigger.USERSTOP, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.FCSERR, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FCSERR, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.PLDERR, start_criteria_filter=0, stop_criteria=enums.StopTrigger.PLDERR, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.FILTER, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FILTER, stop_criteria_filter=0)

    resp = await port.capturer.trigger.get()
    resp.start_criteria
    resp.start_criteria_filter
    resp.stop_criteria
    resp.stop_criteria_filter


Frame to Keep
--------------
Which packets to keep once the start criteria has been triggered for a port.
Also how big a portion of each packet to retain, saving space for more packets
in the capture buffer.

.. seealso::

    Detailed script example can be found in `here <https://github.com/xenanetworks/open-automation-script-library/blob/main/packet_capture/packet_capture.py>`_

Corresponding CLI command: ``PC_KEEP``

.. code-block:: python

    # Capture - Frame to Keep, 
    await port.capturer.keep.set(kind=enums.PacketType.ALL, index=0, byte_count=0)
    await port.capturer.keep.set_all()
    await port.capturer.keep.set(kind=enums.PacketType.FCSERR, index=0, byte_count=0)
    await port.capturer.keep.set_fcserr()
    await port.capturer.keep.set(kind=enums.PacketType.FILTER, index=0, byte_count=0)
    await port.capturer.keep.set_filter()
    await port.capturer.keep.set(kind=enums.PacketType.NOTPLD, index=0, byte_count=0)
    await port.capturer.keep.set_notpld()
    await port.capturer.keep.set(kind=enums.PacketType.PLDERR, index=0, byte_count=0)
    await port.capturer.keep.set_plderr()
    await port.capturer.keep.set(kind=enums.PacketType.TPLD, index=0, byte_count=0)
    await port.capturer.keep.set_tpld()

    resp = await port.capturer.keep.get()
    resp.kind
    resp.index
    resp.byte_count


State
-----------
Whether a port is capturing packets. When on, the port retains the received
packets and makes them available for inspection. The capture criteria are
configured using the ``PC_xxx`` parameters. While capture is on the capture
parameters cannot be changed.

Corresponding CLI command: ``P_CAPTURE``

.. code-block:: python

    # Capture - State
    await port.capturer.state.set(on_off=enums.StartOrStop.START)
    await port.capturer.state.set_start()
    await port.capturer.state.set(on_off=enums.StartOrStop.STOP)
    await port.capturer.state.set_stop()

    resp = await port.capturer.state.get()
    resp.on_off


Statistics
-----------
Obtains the number of packets currently in the capture buffer for a port. The
count is reset to zero when capture is turned on.

Corresponding CLI command: ``PC_STATS``

.. code-block:: python

    # Capture - Statistics
    resp = await port.capturer.stats.get()
    resp.start_time
    resp.status


Read Captured Packets
---------------------
Obtains the raw bytes of a captured packet for a port. The packet data may be
truncated if the :class:`PC_KEEP` command specified a limit on the number of bytes kept.

Corresponding CLI command: ``PC_PACKET``

.. code-block:: python

    # Read Captured Packets
    pkts = await port.capturer.obtain_captured()
    for i in range(len(pkts)):
        resp = await pkts[i].packet.get()
        print(f"Packet content # {i}: {resp.hex_data}")