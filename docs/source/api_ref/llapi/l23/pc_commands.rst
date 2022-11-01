Capture
=================================

This module contains the **L23 port capture commands** that deal with configuration of the capture criteria and inspection of the captured data from a port.

Whether the port is enabled for capturing packets is specified by the ``P_CAPTURE`` command. Captured packets are indexed starting from 0, and are stored in a buffer that is cleared before capture starts. While on, the capture configuration parameters cannot be changed.

The capture command names all have the form ``PC_<xxx>`` and require both a module index id and a port index id. The per-packet parameters also use a sub-index identifying a particular packet in the capture buffer.

-------

.. currentmodule:: xoa_driver.internals.core.commands.pc_commands


PC_TRIGGER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PC_TRIGGER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PC_KEEP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PC_KEEP
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PC_STATS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PC_STATS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PC_EXTRA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PC_EXTRA
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PC_PACKET
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PC_PACKET
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr
