Status
=========================

Sync Status
-----------
Obtains the current in-sync status of a port's receive interface.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_RECEIVESYNC`

.. code-block:: python

    # Sync Status
    resp = await port.sync_status.get()
    resp.sync_status == enums.SyncStatus.IN_SYNC
    resp.sync_status == enums.SyncStatus.NO_SYNC
