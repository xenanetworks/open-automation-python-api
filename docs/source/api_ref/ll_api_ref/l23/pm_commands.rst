Match Term
=================================

This module contains the **L23 port match term commands** that deal with configuration of the length term on the received traffic of a port.

The match term command names all have the form ``PM_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular match term.

The match terms provide basic true/false indications for each packet received on the port.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

-------

.. currentmodule:: xoa_driver.internals.core.commands.pm_commands


PM_INDICES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PM_INDICES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PM_CREATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PM_CREATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PM_DELETE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PM_DELETE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PM_PROTOCOL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PM_PROTOCOL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PM_POSITION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PM_POSITION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PM_MATCH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PM_MATCH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

