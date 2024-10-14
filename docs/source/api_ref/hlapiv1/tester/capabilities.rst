Capabilities
=========================
A series of integer values specifying various internal limits (aka. capabilities) of the chassis.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_CAPABILITIES`

.. code-block:: python

    # Capabilities
    resp = await tester.capabilities.get()
    resp.version
    resp.max_name_len
    resp.max_comment_len
    resp.max_password_len
    resp.max_ext_rate
    resp.max_session_count
    resp.max_chain_depth
    resp.max_module_count
    resp.max_protocol_count
    resp.can_stream_based_arp
    resp.can_sync_traffic_start
    resp.can_read_log_files
    resp.can_par_module_upgrade
    resp.can_upgrade_timekeeper
    resp.can_custom_defaults
    resp.max_owner_name_length
    resp.can_read_temperatures
    resp.can_latency_f2f