Length Term
=================================

This module contains the **L23 port length term commands** that deal with configuration of the length term on the received traffic of a port.

The length term command names all have the form ``PL_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular length term.

The length terms provide basic true/false indications for each packet received on the port.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. currentmodule:: xoa_driver.internals.core.commands.pl_commands


PL_INDICES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PL_INDICES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PL_CREATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PL_CREATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PL_DELETE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PL_DELETE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PL_LENGTH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PL_LENGTH
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

