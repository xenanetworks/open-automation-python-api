Port Filter
=================================

This module contains the **impairment port flow filter commands**.

There are 2 register copies used to configure the filters:
        
(1) ``Shadow-copy (type value = 0)``, temporary copy configured by sever. Values stored in ``shadow-copy`` have no immediate effect on the flow filters. :class:`PEF_APPLY` will pass the values from the ``shadow-copy`` to the ``working-copy``.

(2) ``Working-copy (type value = 1)``, reflects what is currently used for filtering in the FPGA. ``Working-copy`` cannot be written directly. Only ``shadow-copy`` allows direct write.

(3) All ``set`` actions are performed on ``shadow-copy`` ONLY.

(4) Only when :class:`PEF_APPLY` is called, ``working-copy`` and FPGA are updated with values from the ``shadow-copy``.


.. note::

    Flow filter is only applicable to flow ID from 1 to 7. You cannot place a filter on flow 0.


-------

.. automodule:: xoa_driver.internals.commands.pef_commands
    :members:
    :no-undoc-members:
    :exclude-members: GetDataAttr, SetDataAttr, __init__

