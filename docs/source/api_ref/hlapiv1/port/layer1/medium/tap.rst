Tap Configuration
=========================


TX Tap Autotune
-------------------------
Enable or disable the automatic receiving of PHY retuning (see :class:`~xoa_driver.internals.commands.pp_commands.PP_PHYRETUNE`), which
is performed on the 25G interfaces as soon as a signal is detected by the
transceiver. Useful if a bad signal causes the PHY to continuously retune or if
for some other reason it is preferable to use manual retuning (:class:`~xoa_driver.internals.commands.pp_commands.PP_PHYRETUNE`).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_PHYAUTOTUNE`

.. code-block:: python

    # TX Tap Autotune
    await port.serdes[0].phy.autotune.set(on_off=enums.OnOff.ON)
    await port.serdes[0].phy.autotune.set_on()
    await port.serdes[0].phy.autotune.set(on_off=enums.OnOff.OFF)
    await port.serdes[0].phy.autotune.set_off()

    resp = await port.serdes[0].phy.autotune.get()
    resp.on_off


TX Tap Retune
-------------------------
Trigger a new retuning of the receive equalizer on the PHY for one of the 25G
serdes. Useful if e.g. a direct attached copper cable or loop transceiver does
not go into sync after insertion. Note that the retuning will cause disruption
of the traffic on all serdes.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_PHYRETUNE`

.. code-block:: python

    # TX Tap Retune
    await port.serdes[0].phy.retune.set(dummy=1)


TX Tap Configuration
-------------------------
Control and monitor the equalizer settings of the on-board PHY in the
transmission direction (towards the transceiver cage) on Thor and Loki modules.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_PHYTXEQ`

.. code-block:: python

    # TX Tap Configuration
    await port.serdes[0].phy.tx_equalizer.set(pre2=0, pre1=0, main=86, post1=0, post2=0, post3=0)
    resp = await port.serdes[0].phy.tx_equalizer.get()
    resp.pre2
    resp.pre
    resp.main
    resp.post
    resp.pre3_post2 # pre3 for Freya (112G Serdes), post2 for Thor (56G Serdes)
    resp.post3


RX Tap Configuration
-------------------------
RX EQ parameters.

.. note::
    
    For non-Freya Modules.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_PHYRXEQ`

.. code-block:: python

    # RX Tap Configuration
    await port.serdes[0].phy.rx_equalizer.set(auto=0, ctle=0, reserved=0)
    
    resp = await port.serdes[0].phy.rx_equalizer.get()
    resp.auto
    resp.ctle
