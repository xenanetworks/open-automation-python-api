Reservation
=========================

Reservation Action
-------------------
You set this command to reserve, release, or relinquish the chassis itself.
The chassis must be reserved before any of the chassis-level parameters can be
changed. The owner of the session must already have been specified.
Reservation will fail if any modules or ports are reserved for other users.

.. note::

    Before reserve Tester need to reserve all the ports on it, otherwise ``<STATUS_NOTVALID>``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_RESERVATION`

.. code-block:: python

    # Reservation
    await tester.reservation.set(operation=enums.ReservedAction.RELEASE)
    await tester.reservation.set_release()
    await tester.reservation.set(operation=enums.ReservedAction.RELINQUISH)
    await tester.reservation.set_relinquish()
    await tester.reservation.set(operation=enums.ReservedAction.RESERVE)
    await tester.reservation.set_reserve()

    resp = await tester.reservation.get()
    resp.operation

Reserved By
-----------
Identify the user who has the chassis reserved. The empty string if the chassis
is not currently reserved.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_RESERVEDBY`

.. code-block:: python

    # Reserved By
    resp = await tester.reserved_by.get()
    resp.username
