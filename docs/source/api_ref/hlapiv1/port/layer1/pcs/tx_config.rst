TX Configuration
=========================

Error Counters
---------------------
Obtain the error count of each alarm, PCS Error, FEC Error, Header Error, Align
Error, BIP Error, and High BER Error.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_ALARMS_ERRORS`

.. code-block:: python

    # TX Configuration - Error Counters
    resp = await port.pcs_pma.alarms.errors.get()
    resp.total_alarms
    resp.los_error_count
    resp.total_align_error_count
    resp.total_bip_error_count
    resp.total_fec_error_count
    resp.total_header_error_count
    resp.total_higher_error_count
    resp.total_pcs_error_count
    resp.valid_mask


Error Generation Rate
---------------------
The rate of continuous bit-level error injection. Errors are injected evenly
across the SerDes where injection is enabled.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_TXERRORRATE`

.. code-block:: python

    # TX Configuration - Error Generation Rate
    resp = await port.pcs_pma.error_gen.error_rate.get()
    resp.rate


Error Generation Inject
-----------------------
Inject a single bit-level error into the SerDes where injection has been enabled.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_TXINJECTONE`

.. code-block:: python

    # TX Configuration - Error Generation Inject
    await port.pcs_pma.error_gen.inject_one.set()


Error Injection
---------------------
Inject a particular kind of CAUI error into a specific physical lane.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_TXLANEINJECT`

.. code-block:: python

    # TX Configuration - Error Injection
    await port.pcs_pma.lanes[0].tx_error_inject.set_alignerror()
    await port.pcs_pma.lanes[0].tx_error_inject.set_bip8error()
    await port.pcs_pma.lanes[0].tx_error_inject.set_headererror()


Lane Configuration
---------------------
The virtual lane index and artificial skew for data transmitted on a specified
physical lane.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_TXLANECONFIG`

.. code-block:: python

    # TX Configuration - Lane Configuration
    await port.pcs_pma.lanes[0].tx_config.set(virt_lane_index=1, skew=10)
    
    resp = await port.pcs_pma.lanes[0].tx_config.get()
    resp.virt_lane_index
    resp.skew
