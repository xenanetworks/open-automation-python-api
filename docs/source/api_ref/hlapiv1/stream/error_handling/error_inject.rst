Error Injection
=========================

Misorder Error
------------------------------

.. code-block:: python

    await stream.inject_err.misorder.set()


Payload Integrity Error
------------------------------

.. code-block:: python

    await stream.inject_err.payload_integrity.set()


Sequence Error
------------------------------

.. code-block:: python

    await stream.inject_err.sequence.set()


Test Payload Error
------------------------------

.. code-block:: python

    await stream.inject_err.test_payload.set()


Checksum Error
------------------------------

.. code-block:: python

    await stream.inject_err.frame_checksum.set()