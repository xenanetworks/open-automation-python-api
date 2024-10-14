Traffic Control
=========================

Chassis Traffic
----------------
Starts or stops the traffic on a number of ports on the chassis simultaneously.
The ports are identified by pairs of integers (module port).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_TRAFFIC`

.. code-block:: python

    # Chassis Traffic
    await tester.traffic.set(on_off=enums.OnOff.ON, module_ports=[0,0,0,1])
    await tester.traffic.set(on_off=enums.OnOff.OFF, module_ports=[0,0,0,1])
    await tester.traffic.set_on(module_ports=[0,0,0,1])
    await tester.traffic.set_off(module_ports=[0,0,0,1])

Synchronized Chassis Traffic
----------------------------
Works just as the :class:`~xoa_driver.internals.commands.c_commands.C_TRAFFIC` command described above with an additional option to
specify a point in time where traffic should be started. This can be used to
start traffic simultaneously on multiple chassis. The ports are identified by
pairs of integers (module port).

.. note::

    This requires that the chassis in question all use the TimeKeeper option to keep their CPU clocks synchronized.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_TRAFFICSYNC`

.. code-block:: python

    # Synchronized Chassis Traffic
    await tester.traffic_sync.set(on_off=enums.OnOff.ON, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set(on_off=enums.OnOff.OFF, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_on(timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_off(timestamp=1234567, module_ports=[0,0,0,1])

