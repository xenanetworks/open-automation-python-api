Capabilities
=========================
Gets the module capabilities.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_CAPABILITIES`

.. code-block:: python

    # Capabilities
    resp = await module.capabilities.get()
    resp.can_advanced_timing
    resp.can_local_time_adjust
    resp.can_media_config
    resp.can_ppm_sweep
    resp.can_tsn
    resp.is_chimera
    resp.max_clock_ppm