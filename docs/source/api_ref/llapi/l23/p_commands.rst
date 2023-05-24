.. _l23_p_commands:

Port
=================================

This module contains the **L23 port classes** that deal with basic information about, and configuration of L23 test ports. The L23 port command names all have the form ``P_<xxx>`` and require a module index id and a port index id. In general, port commands cannot be changed while traffic is on. Additionally, every stream must be disabled before changing parameters that affect the bandwidth of the port.

-------

.. automodule:: xoa_driver.internals.commands.p_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__, P_EMULATE, P_LOADMODE