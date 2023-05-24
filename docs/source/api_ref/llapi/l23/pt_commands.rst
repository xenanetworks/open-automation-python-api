TX Statistics
=================================

This module contains the **L23 port TX statistics classes** that provide quantitative information about the transmitted packets on a port.

The command names all have the form ``PT_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific transmitted stream also have a sub-index.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

-------

.. automodule:: xoa_driver.internals.commands.pt_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__, PT_FLOWTOTAL, PT_FLOWCLEAR

