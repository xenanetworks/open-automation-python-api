Link Training
=========================

Configuration
-------------------------

Configuration LT out-of-sync preset and timeout

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_LINKTRAIN_CONFIG`

.. code-block:: python

    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.CURRENT, timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.CURRENT, timeout_mode=enums.TimeoutMode.DISABLED)
    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.IEEE, timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.IEEE, timeout_mode=enums.TimeoutMode.DISABLED)

Status
------

Get link training status.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_LINKTRAIN_STATUS`

.. code-block:: python

    resp = await port.l1.serdes[0].lt_status.get()
    resp.failure
    resp.mode
    resp.status

Info
-----

Get link training result info.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_LINKTRAININFO`

.. code-block:: python

    resp = await port.l1.serdes[0].lt_info.get()
    resp.duration_us
    """duration of the auto-negotiation process in microseconds, from autoneg is enabled on the port to the negotiation is finished."""
    resp.lock_lost_count: 
    """number of lost locks on auto-neg."""
    resp.pre1_current_level: 
    """c(-1) current level."""
    resp.pre1_rx_increment_req_count: 
    """c(-1) received number of increment requests."""
    resp.pre1_rx_decrement_req_count: 
    """c(-1) received number of decrement requests."""
    resp.pre1_rx_coeff_eq_limit_reached_count: 
    """c(-1) received number of maximum limits of coefficient and equalization requests reached."""
    resp.pre1_rx_eq_limit_reached_count: 
    """c(-1) received number of maximum limits of equalization requests reached."""
    resp.pre1_rx_coeff_not_supported_count: 
    """c(-1) received number of coefficients not supported."""
    resp.pre1_rx_coeff_at_limit_count: 
    """c(-1) received number of coefficients at limit."""
    resp.pre1_tx_increment_req_count: 
    """c(-1) transmitted number of increment requests."""
    resp.pre1_tx_decrement_req_count: 
    """c(-1) transmitted number of decrement requests."""
    resp.pre1_tx_coeff_eq_limit_reached_count: 
    """c(-1) transmitted number of maximum limits of coefficient and equalization requests reached."""
    resp.pre1_tx_eq_limit_reached_count: 
    """c(-1) transmitted number of maximum limits of equalization requests reached."""
    resp.pre1_tx_coeff_not_supported_count: 
    """c(-1) transmitted number of coefficients not supported."""
    resp.pre1_tx_coeff_at_limit_count: 
    """c(-1) transmitted number of coefficients at limit."""
    resp.main_current_level: 
    """c(0) current level."""
    resp.main_rx_increment_req_count: 
    """c(0) received number of increment requests."""
    resp.main_rx_decrement_req_count: 
    """c(0) received number of decrement requests."""
    resp.main_rx_coeff_eq_limit_reached_count: 
    """c(0) received number of maximum limits of coefficient and equalization requests reached."""
    resp.main_rx_eq_limit_reached_count: 
    """c(0) received number of maximum limits of equalization requests reached."""
    resp.main_rx_coeff_not_supported_count: 
    """c(0) received number of coefficients not supported."""
    resp.main_rx_coeff_at_limit_count: 
    """c(0) received number of coefficients at limit."""
    resp.main_tx_increment_req_count: 
    """c(0) transmitted number of increment requests."""
    resp.main_tx_decrement_req_count: 
    """c(0) transmitted number of decrement requests."""
    resp.main_tx_coeff_eq_limit_reached_count: 
    """c(0) transmitted number of maximum limits of coefficient and equalization requests reached."""
    resp.main_tx_eq_limit_reached_count: 
    """c(0) transmitted number of maximum limits of equalization requests reached."""
    resp.main_tx_coeff_not_supported_count: 
    """c(0) transmitted number of coefficients not supported."""
    resp.main_tx_coeff_at_limit_count: 
    """c(0) transmitted number of coefficients at limit."""
    resp.post1_current_level: 
    """c(1) current level."""
    resp.post1_rx_increment_req_count: 
    """c(1) received number of increment requests."""
    resp.post1_rx_decrement_req_count: 
    """c(1) received number of decrement requests."""
    resp.post1_rx_coeff_eq_limit_reached_count: 
    """c(1) received number of maximum limits of coefficient and equalization requests reached."""
    resp.post1_rx_eq_limit_reached_count: 
    """c(1) received number of maximum limits of equalization requests reached."""
    resp.post1_rx_coeff_not_supported_count: 
    """c(1) received number of coefficients not supported."""
    resp.post1_rx_coeff_at_limit_count: 
    """c(1) received number of coefficients at limit."""
    resp.post1_tx_increment_req_count: 
    """c(1) transmitted number of increment requests."""
    resp.post1_tx_decrement_req_count: 
    """c(1) transmitted number of decrement requests."""
    resp.post1_tx_coeff_eq_limit_reached_count: 
    """c(1) transmitted number of maximum limits of coefficient and equalization requests reached."""
    resp.post1_tx_eq_limit_reached_count: 
    """c(1) transmitted number of maximum limits of equalization requests reached."""
    resp.post1_tx_coeff_not_supported_count: 
    """c(1) transmitted number of coefficients not supported."""
    resp.post1_tx_coeff_at_limit_count: 
    """c(1) transmitted number of coefficients at limit."""
    resp.pre2_current_level: 
    """c(-2) current level."""
    resp.pre2_rx_increment_req_count: 
    """c(-2) received number of increment requests."""
    resp.pre2_rx_decrement_req_count: 
    """c(-2) received number of decrement requests."""
    resp.pre2_rx_coeff_eq_limit_reached_count: 
    """c(-2) received number of maximum limits of coefficient and equalization requests reached."""
    resp.pre2_rx_eq_limit_reached_count: 
    """c(-2) received number of maximum limits of equalization requests reached."""
    resp.pre2_rx_coeff_not_supported_count: 
    """c(-2) received number of coefficients not supported."""
    resp.pre2_rx_coeff_at_limit_count: 
    """c(-2) received number of coefficients at limit."""
    resp.pre2_tx_increment_req_count: 
    """c(-2) transmitted number of increment requests."""
    resp.pre2_tx_decrement_req_count: 
    """c(-2) transmitted number of decrement requests."""
    resp.pre2_tx_coeff_eq_limit_reached_count: 
    """c(-2) transmitted number of maximum limits of coefficient and equalization requests reached."""
    resp.pre2_tx_eq_limit_reached_count: 
    """c(-2) transmitted number of maximum limits of equalization requests reached."""
    resp.pre2_tx_coeff_not_supported_count: 
    """c(-2) transmitted number of coefficients not supported."""
    resp.pre2_tx_coeff_at_limit_count: 
    """c(-2) transmitted number of coefficients at limit."""
    resp.pre3_current_level: 
    """c(-3) current level."""
    resp.pre3_rx_increment_req_count: 
    """c(-3) received number of increment requests."""
    resp.pre3_rx_decrement_req_count: 
    """c(-3) received number of decrement requests."""
    resp.pre3_rx_coeff_eq_limit_reached_count: 
    """c(-3) received number of maximum limits of coefficient and equalization requests reached."""
    resp.pre3_rx_eq_limit_reached_count: 
    """c(-3) received number of maximum limits of equalization requests reached."""
    resp.pre3_rx_coeff_not_supported_count: 
    """c(-3) received number of coefficients not supported."""
    resp.pre3_rx_coeff_at_limit_count: 
    """c(-3) received number of coefficients at limit."""
    resp.pre3_tx_increment_req_count: 
    """c(-3) transmitted number of increment requests."""
    resp.pre3_tx_decrement_req_count: 
    """c(-3) transmitted number of decrement requests."""
    resp.pre3_tx_coeff_eq_limit_reached_count: 
    """c(-3) transmitted number of maximum limits of coefficient and equalization requests reached."""
    resp.pre3_tx_eq_limit_reached_count: 
    """c(-3) transmitted number of maximum limits of equalization requests reached."""
    resp.pre3_tx_coeff_not_supported_count: 
    """c(-3) transmitted number of coefficients not supported."""
    resp.pre3_tx_coeff_at_limit_count: 
    """c(-3) transmitted number of coefficients at limit."""
    resp.prbs_total_bits_high: 
    """PRBS total bits (most significant 32-bit)."""
    resp.prbs_total_bits_low: 
    """PRBS total bits  (least significant 32-bit)."""
    resp.prbs_total_error_bits_high: 
    """PRBS total error bits (most significant 32-bit, only bit 15-0 should be used)."""
    resp.prbs_total_error_bits_low: 
    """PRBS total error bits (least significant 32-bit)."""
    resp.frame_lock
    """frame lock status of the local end."""
    resp.emote_frame_lock
    """frame lock status of the remote end."""
    resp.num_frame_errors
    resp.num_overruns
    resp.last_ic_received
    resp.last_ic_sent

Preset Configuration
--------------------

Preset Configuration (Native)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure the preset values (native values) of a serdes and the response to the received IC request.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PRESET_CONFIG`

.. code-block:: python

    await port_obj.l1.serdes[serdes_id].lt.preset1.native.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=84, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset1.native.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=84, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset2.native.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=84, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset2.native.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=84, post=0)
    
    await port_obj.l1.serdes[serdes_id].lt.preset3.native.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=84, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset3.native.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=84, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset4.native.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=84, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset4.native.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=84, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset5.native.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=84, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset5.native.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=84, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset_los.native.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=84, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset_los.native.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=84, post=0)

Preset Configuration (IEEE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure the preset values (IEEE coefficient values) of a serdes and the response to the received IC request.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PRESET_CONFIG_COEFF`

.. code-block:: python

    await port_obj.l1.serdes[serdes_id].lt.preset1.ieee.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=1000, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset1.ieee.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=1000, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset2.ieee.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=1000, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset2.ieee.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=1000, post=0)
    
    await port_obj.l1.serdes[serdes_id].lt.preset3.ieee.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=1000, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset3.ieee.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=1000, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset4.ieee.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=1000, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset4.ieee.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=1000, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset5.ieee.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=1000, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset5.ieee.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=1000, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset_los.ieee.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=1000, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset_los.ieee.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=1000, post=0)


Preset Configuration (mV/dB)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Configure the preset values (mV/dB values) of a serdes and the response to the received IC request.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PRESET_CONFIG_LEVEL`

.. code-block:: python

    await port_obj.l1.serdes[serdes_id].lt.preset1.level.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=998, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset1.level.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=998, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset2.level.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=998, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset2.level.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=998, post=0)
    
    await port_obj.l1.serdes[serdes_id].lt.preset3.level.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=998, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset3.level.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=998, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset4.level.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=998, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset4.level.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=998, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset5.level.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=998, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset5.level.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=998, post=0)

    await port_obj.l1.serdes[serdes_id].lt.preset_los.level.set(response=enums.FreyaPresetResponse.ACCEPT, pre3=0, pre2=0, pre=0, main=998, post=0)
    await port_obj.l1.serdes[serdes_id].lt.preset_los.level.set(response=enums.FreyaPresetResponse.IGNORE, pre3=0, pre2=0, pre=0, main=998, post=0)

Reset
^^^^^

Reset the preset of the serdes to its default values.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PRESET_RESET`

.. code-block:: python

    await port_obj.l1.serdes[serdes_id].lt.preset1.reset.set()
    await port_obj.l1.serdes[serdes_id].lt.preset2.reset.set()
    await port_obj.l1.serdes[serdes_id].lt.preset3.reset.set()
    await port_obj.l1.serdes[serdes_id].lt.preset4.reset.set()
    await port_obj.l1.serdes[serdes_id].lt.preset5.reset.set()
    await port_obj.l1.serdes[serdes_id].lt.preset_los.reset.set()


Tap Range and Response Configuration
-------------------------------------

Tap Range and Response Configuration (Native)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configure the lower and the upper bound of transmit equalizer (native value) of the serdes, and how the serdes responds to an increment/decrement request when either bound is reached.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_LT_PHYTXEQ_RANGE`

.. code-block:: python

    await port_obj.l1.serdes[serdes_id].lt.range.pre3.native.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.native.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.native.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=0, max=44)

    await port_obj.l1.serdes[serdes_id].lt.range.pre2.native.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre2.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre2.native.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre2.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre2.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre2.native.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=0, max=44)

    await port_obj.l1.serdes[serdes_id].lt.range.pre.native.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.native.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.native.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=0, max=44)

    await port_obj.l1.serdes[serdes_id].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=0, max=44)

    await port_obj.l1.serdes[serdes_id].lt.range.post.native.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.post.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.post.native.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.post.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.post.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=0, max=44)
    await port_obj.l1.serdes[serdes_id].lt.range.post.native.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=0, max=44)

Tap Range and Response Configuration (IEEE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Configure the lower and the upper bound of transmit equalizer (IEEE coefficient value) of the serdes, and how the serdes responds to an increment/decrement request when either bound is reached.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_LT_PHYTXEQ_RANGE_COEFF`

.. code-block:: python

    await port_obj.l1.serdes[serdes_id].lt.range.pre3.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre3.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=-100, max=0)

    await port_obj.l1.serdes[serdes_id].lt.range.pre.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.pre.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=-100, max=0)

    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=-100, max=0)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=-100, max=0)

    await port_obj.l1.serdes[serdes_id].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=0, max=500)

    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.EQ_AT_LIMIT, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_EQ_AT_LIMIT, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_NOT_SUPPORTED, min=0, max=500)
    await port_obj.l1.serdes[serdes_id].lt.range.post.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.IGNORE, min=0, max=500)