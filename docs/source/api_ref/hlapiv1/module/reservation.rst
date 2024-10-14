Reservation
=========================

Reservation Action
-------------------
Set this command to reserve, release, or relinquish a module itself (as
opposed to its ports). The module must be reserved before its hardware image can
be upgraded. The owner of the session must already have been specified.
Reservation will fail if the chassis or any ports are reserved for other users.

.. note::

    The reservation parameters are slightly asymmetric with respect to set/get. When querying for the current reservation state, the chassis will use these values.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_RESERVATION`

.. code-block:: python

    # Reservation
    await module.reservation.set(operation=enums.ReservedAction.RELEASE)
    await module.reservation.set_release()
    await module.reservation.set(operation=enums.ReservedAction.RELINQUISH)
    await module.reservation.set_relinquish()
    await module.reservation.set(operation=enums.ReservedAction.RESERVE)
    await module.reservation.set_reserve()

    resp = await module.reservation.get()
    resp.operation
    
    
Reserved By
-----------
Identify the user who has a module reserved. Returns an empty string if the
module is not currently reserved by anyone.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_RESERVEDBY`

.. code-block:: python

    # Reserved By
    resp = await module.reserved_by.get()
    resp.username

