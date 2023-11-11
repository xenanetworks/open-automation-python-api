Identification
=========================

Description
-----------
The description of a stream.

Corresponding CLI command: ``PS_COMMENT``

.. code-block:: python

    # Description
    await stream.comment.set(comment="description")
    
    resp = await stream.comment.get()
    resp.comment

Test Payload ID
---------------
The identifier of the test payloads inserted into packets transmitted for a
stream. A value of -1 disables test payloads for the stream. Test payloads are
inserted at the end of each packet, and contains time-stamp and sequence-number
information. This allows the receiving port to provide error-checking and
latency measurements, in addition to the basic counts and rate measurements
provided for all traffic. The test payload identifier furthermore allows the
receiving port to distinguish multiple different streams, which may originate
from multiple different chassis. Since test payloads are an inter-port and
inter-chassis mechanism, the test payload identifier assignments should be

Corresponding CLI command: ``PS_TPLDID``

.. code-block:: python

    # Test Payload ID
    await stream.tpld_id.set(test_payload_identifier=0)
    
    resp = await stream.tpld_id.get()
    resp.test_payload_identifier)

State
-------------
This property determines if a stream contributes outgoing packets for a port.
The value can be toggled between ON and SUPPRESS while traffic is enabled at the
port level. Streams in the OFF state cannot be set to any other value while
traffic is enabled. The sum of the rates of all enabled or suppressed streams
must not exceed the effective port rate.

Corresponding CLI command: ``PS_ENABLE``

.. code-block:: python

    # State
    await stream.enable.set(state=enums.OnOffWithSuppress.OFF)
    await stream.enable.set_off()
    await stream.enable.set(state=enums.OnOffWithSuppress.ON)
    await stream.enable.set_on()
    await stream.enable.set(state=enums.OnOffWithSuppress.SUPPRESS)
    await stream.enable.set_suppress()

    resp = await stream.enable.get()
    resp.state

