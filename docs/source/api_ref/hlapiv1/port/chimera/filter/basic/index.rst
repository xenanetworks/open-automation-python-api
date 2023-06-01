Basic Filter Configuration
==========================

.. note::

    Applicable to Chimera port only.

.. note::

    Use to verify the filter mode first.
    
    .. code-block:: python
        
        from xoa_driver import misc
        filter = await port.emulation.flows[flow_idx].shadow_filter.get_mode()
        if isinstance(filter, misc.BasicImpairmentFlowFilter):
        
.. toctree::
    :glob:

    *
