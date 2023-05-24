Advanced Timing
=========================

TX Clock Filter Loop Bandwidth
---------------------------

.. code-block:: python

    await module.advanced_timing.clock_tx.filter.set_bw103hz()
    await module.advanced_timing.clock_tx.filter.set_bw1683hz()
    await module.advanced_timing.clock_tx.filter.set_bw207hz()
    await module.advanced_timing.clock_tx.filter.set_bw416hz()
    await module.advanced_timing.clock_tx.filter.set_bw7019hz()
    await module.advanced_timing.clock_tx.filter.get()


TX Clock Source
----------------------------

.. code-block:: python

    await module.advanced_timing.clock_tx.source.set_modulelocalclock()
    await module.advanced_timing.clock_tx.source.set_p0rxclk()
    await module.advanced_timing.clock_tx.source.set_p1rxclk()
    await module.advanced_timing.clock_tx.source.set_p2rxclk()
    await module.advanced_timing.clock_tx.source.set_p3rxclk()
    await module.advanced_timing.clock_tx.source.set_p4rxclk()
    await module.advanced_timing.clock_tx.source.set_p5rxclk()
    await module.advanced_timing.clock_tx.source.set_p6rxclk()
    await module.advanced_timing.clock_tx.source.set_p7rxclk()
    await module.advanced_timing.clock_tx.source.get()


TX Clock Status
----------------------------

.. code-block:: python

    await module.advanced_timing.clock_tx.status.get()


SMA Status
----------------------------

.. code-block:: python

    await module.advanced_timing.sma.status.get()


SMA Input
----------------------------

.. code-block:: python

    await module.advanced_timing.sma.input.set_notused()
    await module.advanced_timing.sma.input.set_tx10mhz()
    await module.advanced_timing.sma.input.set_tx2mhz()
    await module.advanced_timing.sma.input.get()


SMA Output
----------------------------

.. code-block:: python

    await module.advanced_timing.sma.output.set_disabled()
    await module.advanced_timing.sma.output.set_p0rxclk()
    await module.advanced_timing.sma.output.set_p0rxclk2mhz()
    await module.advanced_timing.sma.output.set_p0sof()
    await module.advanced_timing.sma.output.set_p1rxclk()
    await module.advanced_timing.sma.output.set_p1rxclk2mhz()
    await module.advanced_timing.sma.output.set_p1sof()
    await module.advanced_timing.sma.output.set_passthrough()
    await module.advanced_timing.sma.output.set_ref10mhz()
    await module.advanced_timing.sma.output.set_ref125mhz()
    await module.advanced_timing.sma.output.set_ref156mhz()
    await module.advanced_timing.sma.output.set_ref2mhz()
    await module.advanced_timing.sma.output.set_ts_pps()
    await module.advanced_timing.sma.output.get()