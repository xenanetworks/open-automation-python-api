RX Statistics
=================================

This module contains the **L23 port RX statistics commands** that provide quantitative information about the received packets on a port.

The command names all have the form ``PR_<xxx>`` and require both a module index id and a port index id. Those commands dealing with a specific received test payload id and a specific filter also have a sub-index id.

All bit-and byte-level statistics are at layer-2, so they include the full Ethernet frame, and exclude the inter-frame gap and preamble.

-------

.. currentmodule:: xoa_driver.internals.core.commands.pr_commands


PR_TPLDJITTER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_TPLDJITTER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_TOTAL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_TOTAL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_NOTPLD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_NOTPLD
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_EXTRA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_EXTRA
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_TPLDS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_TPLDS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_TPLDTRAFFIC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_TPLDTRAFFIC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_TPLDERRORS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_TPLDERRORS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_TPLDLATENCY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_TPLDLATENCY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_FILTER
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_FILTER
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_CLEAR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_CLEAR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_CALIBRATE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_CALIBRATE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_UAT_STATUS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_UAT_STATUS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_UAT_TIME
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_UAT_TIME
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PR_PFCSTATS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PR_PFCSTATS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

