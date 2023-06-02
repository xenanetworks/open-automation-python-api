Histogram
=================================

This module contains the **L23 port histogram classes** that deal with configuration of data collection and retrieval of samples from a port.

The histogram command names all have the form ``PD_<xxx>`` and require both a module index id and a port index id, as well as a sub-index identifying a particular histogram.

A histogram has a number of *buckets* and counts the packets transmitted or received on a port, possibly limited to those with a particular test payload id. The packet length, inter-frame gap preceding it, or its latency is measured, and the bucket whose range contains this value is incremented.

While a histogram is actively collecting samples its parameters cannot be changed.

-------

.. automodule:: xoa_driver.internals.commands.pd_commands
    :members:
    :no-undoc-members:
    :exclude-members: __init__
