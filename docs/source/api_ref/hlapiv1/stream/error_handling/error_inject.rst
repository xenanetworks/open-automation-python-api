Error Injection
=========================

Misorder Error
------------------------------
Force a misorder error by swapping the test payload sequence numbers in two of
the packets currently being transmitted from a stream. This can aid in analyzing
the error-detection functionality of the system under test. Traffic must be on
for the port, and the stream must be enabled and include test payloads.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_INJECTMISERR`

.. code-block:: python

    # Misorder Error Injection
    await stream.inject_err.misorder.set()


Payload Integrity Error
------------------------------
Force a payload integrity error in one of the packets currently being
transmitted from a stream. Payload integrity validation is only available for
incrementing payloads, and the error is created by changing a byte from the
incrementing sequence. The packet will have a correct frame checksum, but the
receiving Xena chassis will detect the invalid payload based on information in
the test payload. Traffic must be on for the port, and the stream must be
enabled and include test payloads.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_INJECTPLDERR`

.. code-block:: python

    # Payload Integrity Error Injection
    await stream.inject_err.payload_integrity.set()


Sequence Error
------------------------------
Force a sequence error by skipping a test payload sequence number in one of the
packets currently being transmitted from a stream. This can aid in analyzing the
error-detection functionality of the system under test. Traffic must be on for
the port, and the stream must be enabled and include test payloads.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_INJECTSEQERR`

.. code-block:: python

    # Sequence Error Injection
    await stream.inject_err.sequence.set()


Test Payload Error
------------------------------
Force a test payload error in one of the packets currently being transmitted
from a stream. This means that the test payload will not be recognized at the
receiving port, so it will be counted as a no-test-payload packet, and there
will be a lost packet for the stream. Traffic must be on for the port, and the
stream must be enabled and include test payloads.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_INJECTTPLDERR`

.. code-block:: python

    # Test Payload Error Injection
    await stream.inject_err.test_payload.set()


Checksum Error
------------------------------
Force a frame checksum error in one of the packets currently being transmitted
from a stream. This can aid in analyzing the error-detection functionality of
the system under test. Traffic must be on for the port, and the stream must be
enabled.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_INJECTFCSERR`

.. code-block:: python

    # Checksum Error Injection
    await stream.inject_err.frame_checksum.set()