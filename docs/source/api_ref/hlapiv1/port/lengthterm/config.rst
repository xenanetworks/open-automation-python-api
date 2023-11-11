Configuration
=========================

Length
-----------------
The specification for a length-based check that is applied on the packets
received on the port.

Corresponding CLI command: ``PL_LENGTH``

.. code-block:: python

    await length_term.length.set(
        length_check_type=enums.LengthCheckType.AT_MOST,
        size=100)
    await length_term.length.set(
        length_check_type=enums.LengthCheckType.AT_LEAST,
        size=100)

    resp = await length_term.length.get()
    resp.length_check_type
    resp.size


