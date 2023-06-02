Management Address
=========================

IP Address
-----------

.. code-block:: python

    await tester.management_interface.ip_address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.10.1"))
    await tester.management_interface.ip_address.get()

MAC Address
-----------

.. code-block:: python

    await tester.management_interface.macaddress.get()


Hostname
----------

.. code-block:: python

    await tester.management_interface.hostname.set(hostname="name")
    await tester.management_interface.hostname.get()


DHCP
----------

.. code-block:: python

    await tester.management_interface.dhcp.set_on()
    await tester.management_interface.dhcp.set_off()
    await tester.management_interface.dhcp.get()