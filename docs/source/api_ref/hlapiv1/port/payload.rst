Payload
=========================


Random Seed
-----------
A fixed seed value specified for a port. This value is used for a pseudo-random number generator used when generating traffic that requires random variation in packet length, payload, or modified fields. As long as no part of the port configuration is changed, the generated traffic patterns are reproducible when restarting traffic for the port. A specified seed value of -1 instead creates variation by using a new time-based seed value each time traffic generation is restarted.

Corresponding CLI command: ``P_RANDOMSEED``

.. code-block:: python

    # Random Seed
    await port.random_seed.set(seed=1)

    resp = await port.random_seed.get()
    resp.seed


Checksum Offset
------------------
Controls an extra payload integrity checksum, which also covers the header
protocols following the Ethernet header. It will therefore catch any
modifications to the protocol fields (which should therefore not have modifiers on them).

Corresponding CLI command: ``P_CHECKSUM``

.. code-block:: python
    
    # Checksum Offset
    await port.checksum.set(offset=14)

    resp = await port.checksum.get()
    resp.offset


Maximum Header Length
---------------------
The maximum number of header content bytes that can be freely specified for each generated stream. The remaining payload bytes of the packet are auto-generated.The default is 128 bytes. When a larger number is select there is a corresponding proportional reduction in the number of stream definitions that are available for the port. Possible values: 128 (default), 256, 512, 1024, 2048.

Corresponding CLI command: ``P_MAXHEADERLENGTH``

.. code-block:: python

    # Maximum Header Length
    await port.max_header_length.set(max_header_length=56)

    resp = await port.max_header_length.get()
    resp.max_header_length

MIX Weights
---------------------
Allow changing the distribution of the MIX packet length by specifying the
percentage of each of the 16 possible frame sizes used in the MIX.  The sum of the percentage values specified must be 100. The command will affect the mix-distribution for all streams on the port. The possible 16 frame sizes are: 56 (not valid for 40G/100G), 60, 64, 70, 78, 92, 256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.

Corresponding CLI command: ``P_MIXWEIGHTS``

.. code-block:: python

    # MIX Weights
    await port.mix.weights.set(
        weight_56_bytes:=0,
        weight_60_bytes:=0,
        weight_64_bytes:=70,
        weight_70_bytes:=15,
        weight_78_bytes:=15,
        weight_92_bytes:=0,
        weight_256_bytes:=0,
        weight_496_bytes:=0,
        weight_512_bytes:=0,
        weight_570_bytes:=0,
        weight_576_bytes:=0,
        weight_594_bytes:=0,
        weight_1438_bytes:=0,
        weight_1518_bytes:=0,
        weight_9216_bytes:=0,
        weight_16360_bytes:=0)
    
    resp = await port.mix.weights.get()
    resp.weight_56_bytes
    resp.weight_60_bytes
    resp.weight_64_bytes
    resp.weight_70_bytes
    resp.weight_78_bytes
    resp.weight_92_bytes
    resp.weight_256_bytes
    resp.weight_496_bytes
    resp.weight_512_bytes
    resp.weight_570_bytes
    resp.weight_576_bytes
    resp.weight_594_bytes
    resp.weight_1438_bytes
    resp.weight_1518_bytes
    resp.weight_9216_bytes
    resp.weight_16360_bytes


MIX Lengths
---------------------
Allows inspecting the frame sizes defined for each position of the P_MIXWEIGHTS command.  By default, the 16 frame sizes are: 56 (not valid for 40G/100G), 60, 64, 70, 78, 92, 256, 496, 512, 570, 576, 594, 1438, 1518, 9216, and 16360.  In addition to inspecting these sizes one by one, it also allows changing frame size for positions 0, 1, 14 and 15 (default values 56, 60, 9216 and 16360).

Corresponding CLI command: ``P_MIXLENGTH``

.. code-block:: python

    # MIX Lengths
    await port.mix.lengths[0].set(frame_size=56)
    await port.mix.lengths[1].set(frame_size=60)
    await port.mix.lengths[14].set(frame_size=9216)
    await port.mix.lengths[15].set(frame_size=16360)

    resp = await port.mix.lengths[0].get()
    resp.frame_size
    resp = await port.mix.lengths[1].get()
    resp.frame_size
    resp = await port.mix.lengths[14].get()
    resp.frame_size
    resp = await port.mix.lengths[15].get()
    resp.frame_size


Payload Mode
-------------
Set this command to configure the port to use different payload modes, i.e. normal, extend payload, and custom payload field, for ALL streams on this port. The extended payload feature allows the definition of a much larger (up to MTU) payload buffer for each stream. The custom payload field feature allows you to define a sequence of custom data fields for each stream. The data fields will then be used in a round robin fashion when packets are sent based on the stream definition.

Corresponding CLI command: ``P_PAYLOADMODE``

.. code-block:: python

    # Payload Mode
    await port.payload_mode.set(mode=enums.PayloadMode.NORMAL)
    await port.payload_mode.set_normal()
    await port.payload_mode.set(mode=enums.PayloadMode.EXTPL)
    await port.payload_mode.set_extpl()
    await port.payload_mode.set(mode=enums.PayloadMode.CDF)
    await port.payload_mode.set_cdf()

    resp = await port.payload_mode.get()
    resp.mode