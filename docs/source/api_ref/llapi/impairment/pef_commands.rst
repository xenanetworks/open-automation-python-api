Filter Classes
=================================

This module contains the **impairment port flow filter commands**.

There are 2 register copies used to configure the filters:
        
(1) ``Shadow-copy (type value = 0)``, temporary copy configured by sever. Values stored in ``shadow-copy`` have no immediate effect on the flow filters. `PEF_APPLY`_ will pass the values from the ``shadow-copy`` to the ``working-copy``.

(2) ``Working-copy (type value = 1)``, reflects what is currently used for filtering in the FPGA. ``Working-copy`` cannot be written directly. Only ``shadow-copy`` allows direct write.

(3) All ``set`` actions are performed on ``shadow-copy`` ONLY.

(4) Only when `PEF_APPLY`_ is called, ``working-copy`` and FPGA are updated with values from the ``shadow-copy``.


.. note::

    Flow filter is only applicable to flow ID from 1 to 7. You cannot place a filter on flow 0.


-------

.. currentmodule:: xoa_driver.internals.core.commands.pef_commands


PEF_INIT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_INIT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_APPLY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_APPLY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_ENABLE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_ENABLE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_ETHSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_ETHSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_ETHSRCADDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_ETHSRCADDR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_ETHDESTADDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_ETHDESTADDR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_L2PUSE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_L2PUSE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_VLANSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_VLANSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_VLANTAG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_VLANTAG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_VLANPCP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_VLANPCP
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_MPLSSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_MPLSSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_MPLSLABEL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_MPLSLABEL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_MPLSTOC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_MPLSTOC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_L3USE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_L3USE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV4SETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV4SETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV4SRCADDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV4SRCADDR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV4DESTADDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV4DESTADDR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV4DSCP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV4DSCP
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV6SETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV6SETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV6SRCADDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV6SRCADDR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV6DESTADDR
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV6DESTADDR
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_IPV6TC
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_IPV6TC
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_UDPSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_UDPSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_UDPSRCPORT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_UDPSRCPORT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_UDPDESTPORT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_UDPDESTPORT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_TCPSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_TCPSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_TCPSRCPORT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_TCPSRCPORT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_TCPDESTPORT
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_TCPDESTPORT
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_ANYSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_ANYSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_ANYCONFIG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_ANYCONFIG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_TPLDSETTINGS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_TPLDSETTINGS
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_TPLDCONFIG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_TPLDCONFIG
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_VALUE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_VALUE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_MASK
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_MASK
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_PROTOCOL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_PROTOCOL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_MODE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_MODE
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_ISSHADOWDIRTY
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_ISSHADOWDIRTY
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr


PEF_CANCEL
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. autoclass:: PEF_CANCEL
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr

