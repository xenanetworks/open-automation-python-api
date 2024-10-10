PCS Variant
=========================

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PCS_VARIANT`

.. code-block:: python

    resp = await port.l1.pcs_variant.get()
    resp.variant
    
    await port.l1.pcs_variant.set(variant=enums.FreyaPCSVariant.ETC)
    await port.l1.pcs_variant.set(variant=enums.FreyaPCSVariant.IEEE)