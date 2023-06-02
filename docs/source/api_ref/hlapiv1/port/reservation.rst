Reservation
=========================

Action
-----------

.. code-block:: python

    await port.reservation.set_release()
    await port.reservation.set_relinquish()
    await port.reservation.set_reserve()
    await port.reservation.get()
    port.is_released()
    port.on_reservation_change(_callback_func())
    
    
Reserved By
-----------

.. code-block:: python

    await port.reserved_by.get()
    port.is_reserved_by_me()
    port.is_reserved_by_others()
    port.on_reserved_by_change(_callback_func())
