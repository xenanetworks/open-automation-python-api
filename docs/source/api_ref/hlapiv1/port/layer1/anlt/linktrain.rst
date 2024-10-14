Link Training
=========================

Configuration
-------------------------
Link training settings

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_LINKTRAIN`

.. code-block:: python

    # Link Training Settings
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.DISABLED, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.STANDALONE, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DEFAULT)
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.INTERACTIVE, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DISABLED)
    await port.pcs_pma.link_training.settings.set(
        mode=enums.LinkTrainingMode.START_AFTER_AUTONEG, 
        pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
        nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
        nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
        timeout_mode=enums.TimeoutMode.DEFAULT)

    resp = await port.pcs_pma.link_training.settings.get()
    resp.mode
    resp.pam4_frame_size
    resp.nrz_pam4_init_cond
    resp.nrz_preset
    resp.timeout_mode


Per Serdes Status
-------------------------
Per lane Link training status

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_LINKTRAINSTATUS`

.. code-block:: python

    # Link Training Serdes Status
    resp = await port.pcs_pma.link_training.per_lane_status[0].get() # serdes lane 0
    resp.mode
    resp.failure
    resp.status

