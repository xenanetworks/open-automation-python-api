Media
=========================

Media Configuration
-------------------
For the test modules that support media configuration (check :class:`~xoa_driver.internals.commands.m_commands.M_CAPABILITIES`), this command sets the desired media type (front port).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_MEDIA`

.. code-block:: python

    # Media Configuration
    await module.media.set(media_config=enums.MediaConfigurationType.BASE_T1)
    await module.media.set(media_config=enums.MediaConfigurationType.BASE_T1S)
    await module.media.set(media_config=enums.MediaConfigurationType.CFP)
    await module.media.set(media_config=enums.MediaConfigurationType.CFP4)
    await module.media.set(media_config=enums.MediaConfigurationType.CXP)
    await module.media.set(media_config=enums.MediaConfigurationType.OSFP800)
    await module.media.set(media_config=enums.MediaConfigurationType.OSFP800_ANLT)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP112)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP112_ANLT)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP28_NRZ)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP28_PAM4)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFP56_PAM4)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD_NRZ)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD_PAM4)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD800)
    await module.media.set(media_config=enums.MediaConfigurationType.QSFPDD800_ANLT)
    await module.media.set(media_config=enums.MediaConfigurationType.SFP112)
    await module.media.set(media_config=enums.MediaConfigurationType.SFP28)
    await module.media.set(media_config=enums.MediaConfigurationType.SFP56)
    await module.media.set(media_config=enums.MediaConfigurationType.SFPDD)

    resp = await module.media.get()
    resp.media_config

Supported Media
---------------
Shows the available speeds on a module. The structure of the returned value is
``[ <cage_type> <available_speed_count> [<ports_per_speed> <speed>] ]``.
``[<ports_per_speed> <speed>]`` is repeated until all speeds supported by the ``<cage_type>`` has been listed.
``[<cage_type> <available_speed_count>]`` is repeated for all cage types on the module including the related ``<ports_per_speed> <speed>`` information.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_MEDIASUPPORT`

.. code-block:: python

    resp = await module.available_speeds.get()
    resp.media_info_list


Port Configuration
------------------
This property defines the current number of ports and the speed of each of them
on a CFP test module. The following combinations are possible: 2x10G, 4x10G, 8x10G, 
2x25G, 4x25G, 8x25G, 1x40G, 2x40G, 2x50G, 4x50G, 8x50G, 1x100G, 2x100G, 4x100G, 2x200G, and 1x400G.

.. note::

    ``<portspeed_list>`` is a list of integers, where the first element is the number of ports followed by a number of port speeds in Mbps.

    The number of port speeds equals the value of the number of ports.
    
    For example if the configuration is 4x25G, ``<portspeed_list>`` will be ``[4, 25000, 25000, 25000, 25000]``.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_CFPCONFIGEXT`

.. code-block:: python

    # Port Configuration
    await module.cfp.config.set(portspeed_list=[1, 800000])
    await module.cfp.config.set(portspeed_list=[2, 400000, 400000])
    await module.cfp.config.set(portspeed_list=[4, 200000, 200000, 200000, 200000])
    await module.cfp.config.set(portspeed_list=[8, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])

    resp = await module.cfp.config.get()
    resp.portspeed_list
