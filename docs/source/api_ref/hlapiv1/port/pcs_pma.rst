PCS/PMA
=========================

Auto-Negotiation
-------------------------

Settings
^^^^^^^^

.. code-block:: python

    await port.pcs_pma.auto_neg.settings.get()

Status
^^^^^^^^

.. code-block:: python

    await port.pcs_pma.auto_neg.status.get()


Selection
^^^^^^^^^

.. note::
    
    Only applicable to RJ45 ports

.. code-block:: python

    await port.autoneg_selection.set_on()
    await port.autoneg_selection.set_off()
    await port.autoneg_selection.get()


Link Training
-------------------------

Settings
^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.link_training.settings.set()
    await port.pcs_pma.link_training.settings.get()


Serdes Status
^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.link_training.per_lane_status[serdes_idx].get()


Forward Error Correction
-------------------------

FEC Mode
^^^^^^^^

.. code-block:: python

    await port.pcs_pma.phy.auto_neg.set()
    await port.fec_mode.set()
    await port.fec_mode.get()


Transmit Configuration
---------------------------

Error Counters
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.alarms.errors.get()


Error Generation Rate
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.error_gen.error_rate.get()


Error Generation Inject
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.error_gen.inject_one.set()


Error Injection
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].tx_error_inject.set_alignerror()
    await port.pcs_pma.lanes[lane_idx].tx_error_inject.set_bip8error()
    await port.pcs_pma.lanes[lane_idx].tx_error_inject.set_headererror()

Lane Configuration
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].tx_config.set()
    await port.pcs_pma.lanes[lane_idx].tx_config.get()


Receive Status
---------------------------

Error Counters
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].rx_status.errors.get()


Lock Status
^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].rx_status.lock.get()


Lane Status
^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.lanes[lane_idx].rx_status.status.get()


Statistics
----------

Clear Counters
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.rx.clear.set()


Clear Counters
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.rx.clear.set()


RX FEX Stats
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.rx.fec_status.get()


RX Total Stats
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.rx.total_status.get()


PMA Pulse Error Inject
----------------------

Control
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.pma_pulse_err_inj.enable.set_on()
    await port.pcs_pma.pma_pulse_err_inj.enable.set_off()
    await port.pcs_pma.pma_pulse_err_inj.enable.get()


Configuration
^^^^^^^^^^^^^^

.. code-block:: python

    await port.pcs_pma.pma_pulse_err_inj.params.set()
    await port.pcs_pma.pma_pulse_err_inj.params.get()