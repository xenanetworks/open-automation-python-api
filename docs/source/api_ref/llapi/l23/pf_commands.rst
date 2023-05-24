Filter
=================================

This module contains the **L23 port filter classes** that deal with configuration of the filters on the received traffic of a port.

The filter command names all have the form ``PF_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular filter.

Each filter specifies a compound Boolean condition on these true/false values to determine if the filter as a whole is true/false.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

-------

.. automodule:: xoa_driver.internals.commands.pf_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__

