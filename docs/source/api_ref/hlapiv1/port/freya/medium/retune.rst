Tap Retune
===========

Trigger a new retuning of the receive equalizer on the PHY for one of the 25G
serdes. Useful if e.g. a direct attached copper cable or loop transceiver does
not go into sync after insertion. Note that the retuning will cause disruption
of the traffic on all serdes.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_PHYRETUNE`

.. code-block:: python

    # TX Tap Retune
    await port.serdes[0].phy.retune.set(dummy=1)