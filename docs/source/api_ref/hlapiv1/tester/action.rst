Action
=========================

Shutdown/Restart
----------------
Shuts down the chassis, and either restarts it in a clean state or leaves it powered off.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_DOWN`

.. code-block:: python

    # Shutdown/Restart
    await tester.down.set(operation=enums.ChassisShutdownAction.POWER_OFF)
    await tester.down.set_poweroff()
    await tester.down.set(operation=enums.ChassisShutdownAction.RESTART)
    await tester.down.set_restart()

Flash
----------
Make all the test port LEDs flash on and off with a 1-second interval. This is
helpful if you have multiple chassis mounted side by side and you need to
identify a specific one.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_FLASH`

.. note::
    
    Require Tester to be reserved before change value.

.. code-block:: python

    # Flash
    await tester.flash.set(on_off=enums.OnOff.OFF)
    await tester.flash.set_off()
    await tester.flash.set(on_off=enums.OnOff.ON)
    await tester.flash.set_on()

    resp = await tester.flash.get()
    resp.on_off


Debug Log
----------
Allows to dump all the logs of a chassis.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_DEBUGLOGS`

.. code-block:: python

    # Debug Log
    resp = await tester.debug_log.get()
    resp.data
    resp.message_length
