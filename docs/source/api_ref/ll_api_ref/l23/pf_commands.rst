Filter
=================================

This module contains the **L23 port filter commands** that deal with configuration of the filters on the received traffic of a port.

The filter command names all have the form ``PF_<xxx>``, and require both a module index id and a port index id, as well as a sub-index identifying a particular filter.

Each filter specifies a compound Boolean condition on these true/false values to determine if the filter as a whole is true/false.

While a filter is enabled, neither its condition nor the definition of each match term or length term used by the condition can be changed.

.. currentmodule:: xoa_driver.internals.core.commands.pf_commands


PF_INDICES
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PF_INDICES
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PF_CREATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PF_CREATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PF_DELETE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PF_DELETE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PF_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PF_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PF_COMMENT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PF_COMMENT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PF_CONDITION
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PF_CONDITION
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PF_STRING
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PF_STRING
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

