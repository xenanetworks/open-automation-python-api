Management Address
=========================

IP Address
-----------
The network configuration parameters of the chassis management port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_IPADDRESS`

.. code-block:: python

    import ipaddress

    # IP Address
    await tester.management_interface.ip_address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.10.1"))
    
    resp = await tester.management_interface.ip_address.get()
    resp.ipv4_address
    resp.subnet_mask
    resp.gateway


MAC Address
-----------
Get the MAC address for the chassis management port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_MACADDRESS`

.. code-block:: python

    # MAC Address
    resp = await tester.management_interface.macaddress.get()
    resp.mac_address


Hostname
----------
Get or set the chassis hostname used when DHCP is enabled.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_HOSTNAME`

.. code-block:: python

    # Hostname
    await tester.management_interface.hostname.set(hostname="name")

    resp = await tester.management_interface.hostname.get()
    resp.hostname


DHCP
----------
Controls whether the chassis will use DHCP to get the management IP address.
Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_DHCP`

.. code-block:: python

    # DHCP
    await tester.management_interface.dhcp.set(on_off=enums.OnOff.ON)
    await tester.management_interface.dhcp.set_on()
    await tester.management_interface.dhcp.set(on_off=enums.OnOff.OFF)
    await tester.management_interface.dhcp.set_off()

    resp = await tester.management_interface.dhcp.get()
    resp.on_off