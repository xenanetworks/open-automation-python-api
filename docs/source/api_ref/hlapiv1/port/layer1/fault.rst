Fault
=========================

Signaling
------------
Sets the remote/local fault signaling behavior of the port (performed by the Reconciliation Sub-layer). By default, the port acts according to the standard, i.e. when receiving a bad signal, it transmits "Remote Fault indications"on the output and when receiving a "Remote Fault indication"from the far-side it will
transmit IDLE sequences.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_FAULTSIGNALING`

.. code-block:: python

    # Fault - Signaling
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.DISABLED)
    await port.fault.signaling.set_disabled()
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.FORCE_LOCAL)
    await port.fault.signaling.set_force_local()
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.FORCE_REMOTE)
    await port.fault.signaling.set_force_remote()
    await port.fault.signaling.set(fault_signaling=enums.FaultSignaling.NORMAL)
    await port.fault.signaling.set_normal()

    resp = await port.fault.signaling.get()
    resp.fault_signaling


Status
------------
Shows if a local or remote fault is currently being detected by the Reconciliation Sub-layer of the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_FAULTSTATUS`

.. code-block:: python

    # Fault - Status
    resp = await port.fault.status.get()
    resp.local_fault_status
    resp.remote_fault_status