Link Training
=========================

Configuration
-------------------------

Configuration LT out-of-sync preset and timeout

.. code-block:: python

    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.CURRENT, timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.CURRENT, timeout_mode=enums.TimeoutMode.DISABLED)
    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.IEEE, timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.l1.anlt.lt_config.set(oos_preset=enums.FreyaOutOfSyncPreset.IEEE, timeout_mode=enums.TimeoutMode.DISABLED)

Status
------

Get link training status.

.. code-block:: python

    resp = await port.l1.serdes[0].lt_status.get()
    resp.failure
    resp.mode
    resp.status

Info
-----

Get link training result info.

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

