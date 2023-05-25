Action
=========================

Shutdown/Restart
----------------

.. code-block:: python

    await tester.down.set_restart()
    await tester.down.set_poweroff()

Flash
----------

.. code-block:: python

    await tester.flash.set_off()
    await tester.flash.set_on()
    await tester.flash.get()


Debug Log
----------

.. code-block:: python

    await tester.debug_log.get()
