Properties
=========================

Description
---------------
Flow description.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pe_commands.PE_COMMENT`

.. code-block:: python

    flow = port.emulation.flows[0]
    await flow.comment.set(comment="Flow description")

    resp = await port.emulation.flows[0].comment.get()
    resp.comment

Initiation
---------------
Prepares for setting up a filter definition.  When called, all filter
definitions in the shadow-set which are not applied are discarded and replaced
with the default values (DEFAULT).

.. note::

    There are 2 register copies used to configure the filters:

    (1) ``Shadow-copy (type value = 0)`` temporary copy configured by sever.
        Values stored in ``shadow-copy`` have no immediate effect on the flow filters. PEF_APPLY will pass the values from the ``shadow-copy`` to the ``working-copy``.

    (2) ``Working-copy (type value = 1)`` reflects what is currently used for filtering in the FPGA.
        ``Working-copy`` cannot be written directly. Only ``shadow-copy`` allows direct write.

    (3) All ``set`` actions are performed on ``shadow-copy`` ONLY.

    (4) Only when PEF_APPLY is called, ``working-copy`` and FPGA are updated with values from the ``shadow-copy``.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_INIT`

.. code-block:: python

    flow = port.emulation.flows[0]
    await flow.shadow_filter.initiating.set()


Apply
------
Applies filter definitions from "shadow-copy" to "working-copy". This
also pushes these settings to the FPGA.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_APPLY`

.. code-block:: python

    flow = port.emulation.flows[0]
    await flow.shadow_filter.apply.set()


Enable
------
Defines if filtering is enabled for the flow.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``


Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_ENABLE`

.. code-block:: python

    flow = port.emulation.flows[0]
    await flow.shadow_filter.enable.set(state=enums.OnOff.ON)
    await flow.shadow_filter.enable.set(state=enums.OnOff.OFF)

    resp = await flow.shadow_filter.enable.get()
    resp.state


Cancel
------
Undo updates to shadow filter settings, sets dirty false.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_CANCEL`

.. code-block:: python

    flow = port.emulation.flows[0]
    await flow.shadow_filter.cancel.set()

Filter Mode
-----------
Control the filter mode.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_MODE`

.. code-block:: python

    flow = port.emulation.flows[0]
    await flow.shadow_filter.use_basic_mode()
    await flow.shadow_filter.use_extended_mode()

    filter = await flow.shadow_filter.get_mode()
    
    if isinstance(filter, misc.BasicImpairmentFlowFilter):
        ...

    if isinstance(filter, misc.ExtendedImpairmentFlowFilter):
        ...


