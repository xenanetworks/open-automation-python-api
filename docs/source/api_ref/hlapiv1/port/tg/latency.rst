Latency
=========================

Mode
------------
Latency is measured by inserting a time-stamp in each packet when it is transmitted, and relating it to the time when the packet is received. There are four separate modes for calculating the latency:

1. Last-bit-out to last-bit-in, which measures basic bit-transit time, independent of packet length.
2. First-bit-out to last-bit-in, which adds the time taken to transmit the packet itself.
3. Last-bit-out to first-bit-in, which subtracts the time taken to transmit the packet itself. The same latency mode must be configured for the transmitting port and the receiving port; otherwise invalid measurements will occur.
4. First-bit-out to first-bit-in, which adds the time taken to transmit the packet itself, and subtracts the time taken to transmit the packet itself. The same latency mode must be configured for the transmitting port and the receiving port; otherwise invalid measurements will occur.

Corresponding CLI command: ``P_LATENCYMODE``

.. code-block:: python

    # Latency Mode
    await port.latency_config.mode.set(mode=enums.LatencyMode.FIRST2FIRST)
    await port.latency_config.mode.set_first2first()
    await port.latency_config.mode.set(mode=enums.LatencyMode.FIRST2LAST)
    await port.latency_config.mode.set_first2last()
    await port.latency_config.mode.set(mode=enums.LatencyMode.LAST2FIRST)
    await port.latency_config.mode.set_last2first()
    await port.latency_config.mode.set(mode=enums.LatencyMode.LAST2LAST)
    await port.latency_config.mode.set_last2last()

    resp = await port.latency_config.mode.get()
    resp.mode


Offset
--------------
An offset applied to the latency measurements performed for received traffic containing test payloads. This value affects the minimum, average, and maximum latency values obtained through the PR_TPLDLATENCY command.

Corresponding CLI command: ``P_LATENCYOFFSET``

.. code-block:: python

    # Latency Offset
    await port.latency_config.offset.set(offset=5)

    resp = await port.latency_config.offset.get()
    resp.offset