Action
=========================

Reset
----------------
Reset port-level parameters to default values, and delete all streams, filters,
capture, and dataset definitions.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_RESET`

.. code-block:: python

    # Reset
    await port.reset.set()


Flash
----------------
Make the test port LED for a particular port flash on and off with a 1-second
interval. This is helpful when you need to identify a specific port within a
chassis.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_FLASH`

.. code-block:: python

    # Flash
    await port.flash.set(on_off=enums.OnOff.ON)
    await port.flash.set_on()
    await port.flash.set(on_off=enums.OnOff.OFF)
    await port.flash.set_off()

    resp = await port.flash.get()
    resp.on_off