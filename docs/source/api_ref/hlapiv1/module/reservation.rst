Reservation
=========================

Action
-----------

.. code-block:: python

    await module.reservation.set_release()
    await module.reservation.set_relinquish()
    await module.reservation.set_reserve()
    await module.reservation.get()
    module.is_released()
    module.on_reservation_change(_callback_func())
    
    
Reserved By
-----------

.. code-block:: python

    await module.reserved_by.get()
    module.is_reserved_by_me()
    module.on_reserved_by_change(_callback_func())

