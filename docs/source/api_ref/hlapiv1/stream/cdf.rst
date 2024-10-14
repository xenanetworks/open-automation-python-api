Custom Data Field
=========================

.. note::

    Use ``await port.payload_mode.set_cdf()`` to set the port's payload mode to Custom Data Field.

Field Offset
---------------------
This command is part of the Custom Data Field (CDF) feature. The CDF offset
for the stream is the location in the stream data packets where the various CDF
data will be inserted. All fields for a given stream uses the same offset
value. The default value is zero (0) which means that the CDF data  will be
inserted at the very start of the packet, thus overwriting the packet protocol
headers.  If you want the CDF data to start immediately after the end of the
packet protocol headers you will have to set the CDF field offset manually. The
feature requires that the :class:`~xoa_driver.internals.commands.p_commands.P_PAYLOADMODE` command on the parent port has been
set to CDF. This enables the feature for all streams on this port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_CDFOFFSET`

.. code-block:: python

    # Custom Data Field
    # Use await port.payload_mode.set_cdf() to set the port's payload mode to Custom Data Field.

    # Field Offset
    await stream.cdf.offset.set(offset=1)
    
    resp = await stream.cdf.offset.get()
    resp.offset


Byte Count
-------------------------
This command is part of the Custom Data Field (CDF) feature. It controls the
number of custom data fields available for each stream. You can set a different number
of fields for each stream. Changing the field count value to a larger value will
leave all existing fields intact. Changing the field count value to a smaller
value will remove all existing fields with an index larger than or equal to the
new count. The feature requires that the :class:`~xoa_driver.internals.commands.p_commands.P_PAYLOADMODE` command on the parent
port has been set to CDF. This enables the feature for all streams on this port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.ps_commands.PS_CDFCOUNT`

.. code-block:: python

    # Byte Count
    await stream.cdf.count.set(cdf_count=1)
    
    resp = await stream.cdf.count.get()
    resp.cdf_count

