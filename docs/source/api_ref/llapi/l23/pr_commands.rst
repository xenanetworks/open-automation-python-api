RX Statistics
=================================

This module contains the **L23 port RX statistics classes** that provide quantitative information about the received packets on a port.

The command names all have the form ``PR_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific received test payload id and a specific filter also have a sub-index id.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

-------

.. automodule:: xoa_driver.internals.commands.pr_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__, PR_FLOWTOTAL, PR_FLOWCLEAR

