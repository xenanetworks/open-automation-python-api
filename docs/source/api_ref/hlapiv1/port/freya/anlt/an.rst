Auto-Negotiation
=========================

Abilities
---------

Return supported technology abilities, supported FEC modes, and supported pause modes.

.. code-block:: python

    resp = await port.l1.anlt.an.abilities.get()
    resp.fec_modes_supported
    resp.tech_abilities_supported
    resp.pause_modes_supported


Configuration
-------------

Configure the advertised technology abilities, FEC modes, and pause modes.

.. code-block:: python

    await port.l1.anlt.an.abilities.set(<advertised_tech_abilities>, <advertised_fec_abilities>, <advertised_pause_mode>)


Status
---------

Returns received technology abilities, FEC abilities, pause abilities, HCD technology ability, FEC mode result, and pause mode result.

.. code-block:: python

    resp = await port.l1.anlt.an.status.get()
    resp.mode
    resp.autoneg_state
    resp.received_tech_abilities
    resp.received_fec_abilities
    resp.received_pause_mode
    resp.tech_ability_hcd_status
    resp.tech_ability_hcd_value
    resp.fec_mode_result
    resp.pause_mode_result

Info
---------

Get L1 auto-negotiation information.

.. code-block:: python

    resp = await port.l1.anlt.an.info.get()
    resp.rx_link_codeword_count
    resp.rx_next_page_message_count
    resp.rx_next_page_unformatted_count
    resp.tx_link_codeword_count
    resp.tx_next_page_message_count
    resp.tx_next_page_unformatted_count
    resp.negotiation_hcd_fail_count
    resp.negotiation_fec_fail_count
    resp.negotiation_loss_of_sync_count
    resp.negotiation_timeout_count
    resp.negotiation_success_count
    resp.duration_us

