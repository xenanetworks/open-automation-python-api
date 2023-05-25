Control
=========================

Inter-frame Gap
---------------

.. code-block:: python

    await port.interframe_gap.set()
    await port.interframe_gap.get()


PAUSE Frames
---------------

.. code-block:: python

    await port.pause.set_on()
    await port.pause.set_off()
    await port.pause.get()


Auto-Train
-----------

.. code-block:: python

    await port.autotrain.set()
    await port.autotrain.get()


Gap Monitor
-----------

.. code-block:: python

    await port.gap_monitor.set()
    await port.gap_monitor.get()


Priority Flow Control
---------------------

.. code-block:: python

    await port.pfc_enable.set()
    await port.pfc_enable.get()


Loopback
--------

.. code-block:: python

    await port.loop_back.set_l1rx2tx()
    await port.loop_back.set_l2rx2tx()
    await port.loop_back.set_l3rx2tx()
    await port.loop_back.set_none()
    await port.loop_back.set_port2port()
    await port.loop_back.set_txoff2rx()
    await port.loop_back.set_txon2rx()
    await port.loop_back.get()


BRR Mode
--------

.. code-block:: python

    await port.brr_mode.set_master()
    await port.brr_mode.set_slave()
    await port.brr_mode.get()


MDI/MDIX Mode
-------------

.. code-block:: python

    await port.mdix_mode.set_auto()
    await port.mdix_mode.set_mdi()
    await port.mdix_mode.set_mdix()
    await port.mdix_mode.get()