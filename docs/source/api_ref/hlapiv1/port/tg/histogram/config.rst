Configuration
=========================

Enable
-----------------
Whether a histogram is currently active on a port. When turned on, all the bucket
counts are cleared to zero. Subsequently each packet matching the histogram source criteria is counted into one of the buckets. While a histogram is enabled its parameters cannot be changed.

Corresponding CLI command: ``PD_ENABLE``

.. code-block:: python

    await dataset.enable.set(on_off=enums.OnOff.ON)
    await dataset.enable.set_on()
    await dataset.enable.set(on_off=enums.OnOff.OFF)
    await dataset.enable.set_off()

    resp = await dataset.enable.get()
    resp.on_off


Data Source
-----------
The source criteria specifying what is counted, and for which packets, by a
histogram of a port.

Corresponding CLI command: ``PD_SOURCE``

.. code-block:: python

    await dataset.source.set(
        source_type=enums.SourceType.TX_IFG,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await dataset.source.set(
        source_type=enums.SourceType.TX_LEN,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await dataset.source.set(
        source_type=enums.SourceType.RX_IFG,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await dataset.source.set(
        source_type=enums.SourceType.RX_LEN,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await dataset.source.set(
        source_type=enums.SourceType.RX_LATENCY,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await dataset.source.set(
        source_type=enums.SourceType.RX_JITTER,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )

    resp = await dataset.source.get()
    resp.source_type
    resp.which_packets
    resp.identity


Data Range
---------------
The bucket ranges used for classifying the packets counted by a histogram of a
port. The packets are either counted by length, measured in bytes, by inter-
frame gap to the preceding packet, also measured in bytes, or by latency in
transmission measured in nanoseconds. There are a fixed number of buckets, each
middle bucket covering a fixed-size range of values which is a power of two.
The first and last buckets count all the packets that do not fit within the
ranges of the middle buckets. The buckets are placed at a certain offset by
specifying the first value that should be counted by the first middle bucket.

Corresponding CLI command: ``PD_RANGE``

.. code-block:: python

    await dataset.range.set(
        start=1, #first value going into the second bucket
        step=1, # the span of each middle bucket: (1) 1,2,4,8,16,32,64,128,256,512 (bytes, non-latency histograms).(2) 16,32,64,128,...,1048576,2097152 (nanoseconds, latency histograms).
        bucket_count=10 # the total number of buckets
    )

    resp = await dataset.range.get()
    resp.start
    resp.step
    resp.bucket_count


Data Samples
---------------

The current set of counts collected by a histogram for a port. There is one value
for each bucket, but any trailing zeros are left out. The list is empty if all
counts are zero.

Corresponding CLI command: ``PD_SAMPLES``

.. code-block:: python

    resp = await dataset.samples.get()
    resp.packet_counts

Remove
---------------

Delete an existing histogram definition.

Corresponding CLI command: ``PD_DELETE``

.. code-block:: python

    # Remove a histogram on the port with an explicit histogram index by the index manager of the port.
    await port.datasets.remove(position_idx=0)