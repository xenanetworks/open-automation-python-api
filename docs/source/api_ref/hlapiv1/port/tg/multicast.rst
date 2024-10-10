Multicast
=========================

Mode
-----------
A multicast mode for a port. Ports can use the IGMPv2 protocol to join or leave multicast groups, either on an on-off basis or repeatedly.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MULTICAST`

.. code-block:: python

    # Multicast Mode
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.JOIN,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.JOIN,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.LEAVE,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.OFF,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.ON,
        second_count=10)

    resp = await port.multicast.mode.get()
    resp.ipv4_multicast_addresses
    resp.operation
    resp.second_count


Extended Mode
--------------
A multicast mode for a port. Ports can use the IGMPv2/IGMPv3 protocol to join or leave multicast groups, either on an on-off basis or repeatedly. 

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MULTICASTEXT`

.. code-block:: python

    # Multicast Extended Mode
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.EXCLUDE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV3
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.INCLUDE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV3
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.JOIN,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.LEAVE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.LEAVE_TO_ALL,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.GENERAL_QUERY,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.GROUP_QUERY,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.ON,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.OFF,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )

    resp = await port.multicast.mode_extended.get()
    resp.ipv4_multicast_addresses
    resp.operation
    resp.second_count
    resp.igmp_version


Source List
-----------
Multicast source list of the port. Only valid if the IGMP protocol version is IGMPv3 set by :class:`~xoa_driver.internals.commands.p_commands.P_MULTICAST`.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MCSRCLIST`

.. code-block:: python

    # Multicast Source List
    await port.multicast.source_list.set(ipv4_addresses=[])
    
    resp = await port.multicast.source_list.get()
    resp.ipv4_addresses


Header
-----------
Allows addition of a VLAN tag to IGMPv2 and IGPMv3 packets.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_MULTICASTHDR`

.. code-block:: python

    # Multicast Header
    await port.multicast.header.set(header_count=1, header_format=enums.MulticastHeaderFormat.VLAN, tag=10, pcp=0, dei=0)
    await port.multicast.header.set(header_count=0, header_format=enums.MulticastHeaderFormat.NOHDR, tag=10, pcp=0, dei=0)
    
    resp = await port.multicast.header.get()
    resp.header_count
    resp.header_format
    resp.tag
    resp.pcp
    resp.dei

