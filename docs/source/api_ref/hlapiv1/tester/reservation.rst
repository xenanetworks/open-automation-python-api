Reservation
=========================

Action
-----------

.. code-block:: python

    await tester.reservation.set_release()
    await tester.reservation.set_relinquish()
    await tester.reservation.set_reserve()
    await tester.reservation.get()
    tester.on_reservation_change(_callback_func())

Reserved By
-----------

.. code-block:: python

    await tester.reserved_by.get()
    tester.on_reserved_by_change(_callback_func())
