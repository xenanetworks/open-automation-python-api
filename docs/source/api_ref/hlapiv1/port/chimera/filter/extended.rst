Working Filter
=========================

.. note::

    Applicable to Chimera port only.


.. note::

    Use to verify the filter mode first.
    
    .. code-block:: python
        
        from xoa_driver import misc
        filter = await port.emulation.flows[flow_idx].shadow_filter.get_mode()
        if isinstance(filter, misc.ExtendedImpairmentFlowFilter):

Use Segments
-------------------

.. code-block:: python
    
    await filter.use_segments([...])

Get Segments
-------------------

.. code-block:: python
    
    segs = await filter.get_protocol_segments()
    segs.count
    segs[idx].segment_type
    segs[idx].mask
    segs[idx].value
