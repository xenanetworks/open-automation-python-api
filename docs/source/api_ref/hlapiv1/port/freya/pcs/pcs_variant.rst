PCS Variant
=========================

.. code-block:: python

    resp = await port.l1.pcs_variant.get()
    resp.variant
    
    await port.l1.pcs_variant.set(variant=enums.FreyaPCSVariant.ETC)
    await port.l1.pcs_variant.set(variant=enums.FreyaPCSVariant.IEEE)