L2+
==========================

.. note::

    Applicable to Chimera port only.


Type
-------------------

.. code-block:: python

    await filter.l2plus_use.set_vlan1()
    await filter.l2plus_use.set_vlan2()
    await filter.l2plus_use.set_mpls()
    await filter.l2plus_use.set_na()
    await filter.l2plus_use.get()


VLAN Inner Tag
-------------------

.. code-block:: python

    await filter.vlan.inner.pcp.set_on()
    await filter.vlan.inner.pcp.set_off()
    await filter.vlan.inner.pcp.get()

    await filter.vlan.inner.tag.set_on()
    await filter.vlan.inner.tag.set_off()
    await filter.vlan.inner.tag.get()

VLAN Outer Tag
-------------------

.. code-block:: python

    await filter.vlan.outer.pcp.set_on()
    await filter.vlan.outer.pcp.set_off()
    await filter.vlan.outer.pcp.get()

    await filter.vlan.outer.tag.set_on()
    await filter.vlan.outer.tag.set_off()
    await filter.vlan.outer.tag.get()


VLAN Settings
-------------------

.. code-block:: python

    await filter.vlan.settings.set()
    await filter.vlan.settings.get()


MPLS Label
-------------------

.. code-block:: python

    await filter.mpls.label.set_on()
    await filter.mpls.label.set_off()
    await filter.mpls.label.get()


MPLS TOC
-------------------

.. code-block:: python

    await filter.mpls.toc.set_on()
    await filter.mpls.toc.set_off()
    await filter.mpls.toc.get()


MPLS Settings
-------------------

.. code-block:: python

    await filter.mpls.settings.set()
    await filter.mpls.settings.get()