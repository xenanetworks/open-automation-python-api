Reservation
=========================

Action
-----------
You set this command to reserve, release, or relinquish a port. The port must be reserved before any of its configuration can be changed, including streams, filters, capture, and datasets.The owner of the session must already have been specified. Reservation will fail if the chassis or module is reserved to other users.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_RESERVATION`

.. code-block:: python

    # Reservation
    await port.reservation.set(operation=enums.ReservedAction.RELEASE)
    await port.reservation.set_release()
    await port.reservation.set(operation=enums.ReservedAction.RELINQUISH)
    await port.reservation.set_relinquish()
    await port.reservation.set(operation=enums.ReservedAction.RESERVE)
    await port.reservation.set_reserve()

    resp = await port.reservation.get()
    resp.status
    
    
Reserved By
-----------
Identify the user who has a port reserved. The empty string if the port is not currently reserved. Note that multiple connections can specify the same name with C_OWNER, but a resource can only be reserved to one connection. Therefore you cannot count on having the port just because it is reserved in your name. The port is reserved to this connection only if P_RESERVATION returns RESERVED_BY_YOU.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_RESERVEDBY`

.. code-block:: python

    # Reserved By
    resp = await port.reserved_by.get()
    resp.username
