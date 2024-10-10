Advanced Timing
=========================

TX Clock Filter Loop Bandwidth
------------------------------
For test modules with advanced timing features, the loop bandwidth on the TX
clock filter.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_TXCLOCKFILTER_NEW`

.. code-block:: python

    # TX Clock Filter Loop Bandwidth
    await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW103HZ)
    await module.advanced_timing.clock_tx.filter.set_bw103hz()
    await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW1683HZ)
    await module.advanced_timing.clock_tx.filter.set_bw1683hz()
    await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW207HZ)
    await module.advanced_timing.clock_tx.filter.set_bw207hz()
    await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW416HZ)
    await module.advanced_timing.clock_tx.filter.set_bw416hz()
    await module.advanced_timing.clock_tx.filter.set(filter_bandwidth=enums.LoopBandwidth.BW7019HZ)
    await module.advanced_timing.clock_tx.filter.set_bw7019hz()

    resp = await module.advanced_timing.clock_tx.filter.get()
    resp.filter_bandwidth


TX Clock Source
----------------------------
For test modules with advanced timing features, select what clock drives the port TX
rates.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_TXCLOCKSOURCE_NEW`

.. code-block:: python

    # TX Clock Source
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.MODULELOCALCLOCK)
    await module.advanced_timing.clock_tx.source.set_modulelocalclock()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P0RXCLK)
    await module.advanced_timing.clock_tx.source.set_p0rxclk()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P1RXCLK)
    await module.advanced_timing.clock_tx.source.set_p1rxclk()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P2RXCLK)
    await module.advanced_timing.clock_tx.source.set_p2rxclk()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P3RXCLK)
    await module.advanced_timing.clock_tx.source.set_p3rxclk()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P4RXCLK)
    await module.advanced_timing.clock_tx.source.set_p4rxclk()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P5RXCLK)
    await module.advanced_timing.clock_tx.source.set_p5rxclk()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P6RXCLK)
    await module.advanced_timing.clock_tx.source.set_p6rxclk()
    await module.advanced_timing.clock_tx.source.set(tx_clock=enums.TXClockSource.P7RXCLK)
    await module.advanced_timing.clock_tx.source.set_p7rxclk()

    resp = await module.advanced_timing.clock_tx.source.get()
    resp.tx_clock


TX Clock Status
----------------------------
For test modules with advanced timing features, check whether a valid clock is present.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_TXCLOCKSTATUS_NEW`

.. code-block:: python

    # TX Clock Status
    resp = await module.advanced_timing.clock_tx.status.get()
    resp.status


SMA Status
----------------------------
For test modules with SMA connectors, this returns the status of the SMA input.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_SMASTATUS`

.. code-block:: python

    # SMA Status
    resp = await module.advanced_timing.sma.status.get()
    resp.status


SMA Input
----------------------------
For test modules with SMA (SubMiniature version A) connectors, selects the function of the SMA input.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_SMAINPUT`

.. code-block:: python

    # SMA Input
    await module.advanced_timing.sma.input.set(sma_in=enums.SMAInputFunction.NOT_USED)
    await module.advanced_timing.sma.input.set_notused()
    await module.advanced_timing.sma.input.set(sma_in=enums.SMAInputFunction.TX10MHZ)
    await module.advanced_timing.sma.input.set_tx10mhz()
    await module.advanced_timing.sma.input.set(sma_in=enums.SMAInputFunction.TX2MHZ)
    await module.advanced_timing.sma.input.set_tx2mhz()

    resp = await module.advanced_timing.sma.input.get()
    resp.sma_in


SMA Output
----------------------------
For test modules with SMA (SubMiniature version A) connectors, selects the function of the SMA output.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_SMAOUTPUT`

.. code-block:: python

    # SMA Output
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.DISABLED)
    await module.advanced_timing.sma.output.set_disabled()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P0RXCLK)
    await module.advanced_timing.sma.output.set_p0rxclk()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P0RXCLK2MHZ)
    await module.advanced_timing.sma.output.set_p0rxclk2mhz()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P0SOF)
    await module.advanced_timing.sma.output.set_p0sof()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P1RXCLK)
    await module.advanced_timing.sma.output.set_p1rxclk()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P1RXCLK2MHZ)
    await module.advanced_timing.sma.output.set_p1rxclk2mhz()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.P1SOF)
    await module.advanced_timing.sma.output.set_p1sof()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.PASSTHROUGH)
    await module.advanced_timing.sma.output.set_passthrough()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF10MHZ)
    await module.advanced_timing.sma.output.set_ref10mhz()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF125MHZ)
    await module.advanced_timing.sma.output.set_ref125mhz()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF156MHZ)
    await module.advanced_timing.sma.output.set_ref156mhz()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.REF2MHZ)
    await module.advanced_timing.sma.output.set_ref2mhz()
    await module.advanced_timing.sma.output.set(sma_out=enums.SMAOutputFunction.TS_PPS)
    await module.advanced_timing.sma.output.set_ts_pps()

    resp = await module.advanced_timing.sma.output.get()
    resp.sma_out