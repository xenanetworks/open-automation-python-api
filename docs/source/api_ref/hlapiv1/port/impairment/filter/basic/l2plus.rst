L2+
==========================

.. note::

    Applicable to Chimera port only.


Type
-------------------
Defines what Layer 2+ protocols that are present and may be used for the filter.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_L2PUSE`

.. code-block:: python

    await filter.l2plus_use.set(use=enums.L2PlusPresent.VLAN1)
    await filter.l2plus_use.set_vlan1()
    await filter.l2plus_use.set(use=enums.L2PlusPresent.VLAN2)
    await filter.l2plus_use.set_vlan2()
    await filter.l2plus_use.set(use=enums.L2PlusPresent.MPLS)
    await filter.l2plus_use.set_mpls()
    await filter.l2plus_use.set(use=enums.L2PlusPresent.NA)
    await filter.l2plus_use.set_na()

    resp = await filter.l2plus_use.get()
    resp.use


VLAN Inner Tag
-------------------
Basic mode only. Defines the VLAN TAG settings for the VLAN filter.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_VLANTAG`

.. code-block:: python

    await filter.vlan.inner.tag.set(use=enums.OnOff.ON, value=1234, mask=Hex("0FFF"))
    await filter.vlan.inner.tag.set_on()
    await filter.vlan.inner.tag.set(use=enums.OnOff.OFF, value=1234, mask=Hex("0FFF"))
    await filter.vlan.inner.tag.set_off()

    resp = await filter.vlan.inner.tag.get()
    resp.use
    resp.value
    resp.mask


VLAN Inner PCP
-------------------
Basic mode only. Defines the VLAN PCP settings for the VLAN filter.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_VLANPCP`

.. code-block:: python

    await filter.vlan.inner.pcp.set(use=enums.OnOff.ON, value=3, mask=Hex("07"))
    await filter.vlan.inner.pcp.set_on()
    await filter.vlan.inner.pcp.set(use=enums.OnOff.OFF, value=3, mask=Hex("07"))
    await filter.vlan.inner.pcp.set_off()

    resp = await filter.vlan.inner.pcp.get()
    resp.use
    resp.value
    resp.mask


VLAN Outer Tag
-------------------
Basic mode only. Defines the VLAN TAG settings for the VLAN filter.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_VLANTAG`

.. code-block:: python

    await filter.vlan.outer.tag.set(use=enums.OnOff.ON, value=1234, mask=Hex("0FFF"))
    await filter.vlan.outer.tag.set_on()
    await filter.vlan.outer.tag.set(use=enums.OnOff.OFF, value=1234, mask=Hex("0FFF"))
    await filter.vlan.outer.tag.set_off()

    resp = await filter.vlan.outer.tag.get()
    resp.use
    resp.value
    resp.mask

VLAN Outer PCP
-------------------
Basic mode only. Defines the VLAN PCP settings for the VLAN filter.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_VLANPCP`

.. code-block:: python

    await filter.vlan.outer.pcp.set(use=enums.OnOff.ON, value=3, mask=Hex("07"))
    await filter.vlan.outer.pcp.set_on()
    await filter.vlan.outer.pcp.set(use=enums.OnOff.OFF, value=3, mask=Hex("07"))
    await filter.vlan.outer.pcp.set_off()

    resp = await filter.vlan.outer.pcp.get()
    resp.use
    resp.value
    resp.mask

VLAN Settings
-------------------
Defines what filter action is performed on the VLAN header.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_VLANSETTINGS`

.. code-block:: python

    await filter.vlan.settings.set(use=enums.FilterUse.OFF, action=enums.InfoAction.EXCLUDE)
    await filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE)
    await filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE)

    resp = await filter.vlan.settings.get()
    resp.use
    resp.action


MPLS Label
-------------------
Basic mode only. Defines the MPLS label settings for the filter.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_MPLSLABEL`

.. code-block:: python

    await filter.mpls.label.set(use=enums.OnOff.ON, value=1000, mask=Hex("FFFFF"))
    await filter.mpls.label.set(use=enums.OnOff.OFF, value=1000, mask=Hex("FFFFF"))

    resp = await filter.mpls.label.get()
    resp.use
    resp.value


MPLS TOC
-------------------
Basic mode only. Defines the MPLS TOC settings for the filter.

.. note::

    For SET, the only allowed ``_filter_type`` is ``shadow-copy``

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_MPLSTOC`

.. code-block:: python

    await filter.mpls.toc.set(use=enums.OnOff.ON, value=0, mask=Hex("07"))
    await filter.mpls.toc.set(use=enums.OnOff.OFF, value=0, mask=Hex("07"))

    resp = await filter.mpls.toc.get()
    resp.use
    resp.value


MPLS Settings
-------------------
Basic mode only. Defines what filter action is performed on the MPLS header.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pef_commands.PEF_MPLSSETTINGS`

.. code-block:: python

    await filter.mpls.settings.set(use=enums.FilterUse.OFF, action=enums.InfoAction.EXCLUDE)
    await filter.mpls.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE)
    await filter.mpls.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE)

    resp = await filter.mpls.settings.get()
    resp.use
    resp.action