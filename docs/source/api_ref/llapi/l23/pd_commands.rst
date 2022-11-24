Histogram Classes
=================================

This module contains the **L23 port histogram classes** that deal with configuration of data collection and retrieval of samples from a port.

The histogram command names all have the form ``PD_<xxx>`` and require both a module index id and a port index id, as well as a sub-index identifying a particular histogram.

A histogram has a number of *buckets* and counts the packets transmitted or received on a port, possibly limited to those with a particular test payload id. The packet length, inter-frame gap preceding it, or its latency is measured, and the bucket whose range contains this value is incremented.

While a histogram is actively collecting samples its parameters cannot be changed.

-------

.. currentmodule:: xoa_driver.internals.core.commands.pd_commands

PD_INDICES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PD_INDICES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PD_CREATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PD_CREATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PD_DELETE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PD_DELETE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PD_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PD_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PD_SOURCE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PD_SOURCE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PD_RANGE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PD_RANGE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PD_SAMPLES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PD_SAMPLES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

