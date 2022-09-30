TX Statistics
=================================

This module contains the **L23 port TX statistics commands** that provide quantitative information about the transmitted packets on a port.

The command names all have the form ``PT_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific transmitted stream also have a sub-index.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

-------

.. currentmodule:: xoa_driver.internals.core.commands.pt_commands


PT_TOTAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PT_TOTAL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PT_NOTPLD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PT_NOTPLD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PT_STREAM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PT_STREAM
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PT_CLEAR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PT_CLEAR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PT_EXTRA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PT_EXTRA
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr
