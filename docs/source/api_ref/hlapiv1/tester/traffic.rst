Traffic Control
=========================

Chassis Traffic
----------------

.. code-block:: python

    await tester.traffic.set(on_off=enums.OnOff.ON, module_ports=[0,0,0,1])
    await tester.traffic.set(on_off=enums.OnOff.OFF, module_ports=[0,0,0,1])
    await tester.traffic.set_on(module_ports=[0,0,0,1])
    await tester.traffic.set_off(module_ports=[0,0,0,1])

Synchronized Chassis Traffic
----------------------------

.. code-block:: python

    await tester.traffic_sync.set(on_off=enums.OnOff.ON, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set(on_off=enums.OnOff.OFF, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_on(timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_off(timestamp=1234567, module_ports=[0,0,0,1])

