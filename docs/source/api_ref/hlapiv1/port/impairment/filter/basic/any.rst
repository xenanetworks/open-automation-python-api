Any
==========================

.. note::

    Applicable to Chimera port only.


Configuration
-------------------
Basic mode only. Defines the ANY field filter configuration. The "ANY field"
filter will match 6 consecutive bytes in the incoming packets at a programmable
offset. Applying a mask, allows to only filter based on selected bits within the
6 bytes.

.. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_ANYCONFIG`

.. code-block:: python

    from xoa_driver import misc

    filter = await port.emulation.flows[1].shadow_filter.get_mode() # e.g. flow_id = 1
    if isinstance(filter, misc.BasicImpairmentFlowFilter):
        await filter.any.config.set(position=0, value=Hex("112233445566"), mask=Hex("112233445566"))

        resp = await filter.any.config.get()
        resp.position
        resp.value
        resp.mask


Settings
-------------------
Basic mode only. Defines if filtering on ANY field in a packet is used for flow filtering.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_ANYSETTINGS`

.. code-block:: python
    
    from xoa_driver import misc
    
    filter = await port.emulation.flows[1].shadow_filter.get_mode() # e.g. flow_id = 1
    if isinstance(filter, misc.BasicImpairmentFlowFilter):
        await filter.any.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE)
        await filter.any.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE)

        resp = filter.any.settings.get()
        resp.use
        resp.action

