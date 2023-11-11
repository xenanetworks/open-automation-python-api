Impairment
=========================

.. note::

    For Chimera module only.


Bypass Mode
--------------------
Set emulator bypass mode. Emulator bypass mode will bypass the entire emulator
for minimum latency.

Corresponding CLI command: ``M_EMULBYPASS``

.. code-block:: python

    # Chimera - Bypass Mode
    if isinstance(module, modules.ModuleChimera):
        await module.emulator_bypass_mode.set(on_off=enums.OnOff.ON)
        await module.emulator_bypass_mode.set_on()
        await module.emulator_bypass_mode.set(on_off=enums.OnOff.OFF)
        await module.emulator_bypass_mode.set_off()

        resp = await module.emulator_bypass_mode.get()
        resp.on_off


Latency Mode
--------------------
Configures the latency mode for Chimera module. In extended latency mode, the FPGA allows all latency parameters to be 10 times higher, at the cost of reduced latency precision.

.. note::

    When change the latency mode, all latency configurations are reset on all ports in chimera module.

Corresponding CLI command: ``M_LATENCYMODE``

.. code-block:: python

    # Chimera - Latency Mode
    if isinstance(module, modules.ModuleChimera):
        await module.latency_mode.set(mode=enums.ImpairmentLatencyMode.NORMAL)
        await module.latency_mode.set_normal()
        await module.latency_mode.set(mode=enums.ImpairmentLatencyMode.EXTENDED)
        await module.latency_mode.set_extended()

        resp = await module.latency_mode.get()
        resp.mode


TX Clock Source
--------------------
For test modules with advanced timing features, select what clock drives the port TX rates.

Corresponding CLI command: ``M_TXCLOCKSOURCE_NEW``

.. code-block:: python

    # Chimera - TX Clock Source
    if isinstance(module, modules.ModuleChimera):
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.MODULELOCALCLOCK)
        await module.tx_clock.source.set_modulelocalclock()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P0RXCLK)
        await module.tx_clock.source.set_p0rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P1RXCLK)
        await module.tx_clock.source.set_p1rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P2RXCLK)
        await module.tx_clock.source.set_p2rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P3RXCLK)
        await module.tx_clock.source.set_p3rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P4RXCLK)
        await module.tx_clock.source.set_p4rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P5RXCLK)
        await module.tx_clock.source.set_p5rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P6RXCLK)
        await module.tx_clock.source.set_p6rxclk()
        await module.tx_clock.source.set(tx_clock=enums.TXClockSource.P7RXCLK)
        await module.tx_clock.source.set_p7rxclk()

        resp = await module.tx_clock.source.get()
        resp.tx_clock


TX Clock Status
----------------------------
For test modules with advanced timing features, check whether a valid clock is present.

Corresponding CLI command: ``M_TXCLOCKSTATUS_NEW``

.. code-block:: python

    # Chimera - TX Clock Status
    if isinstance(module, modules.ModuleChimera):
        resp = await module.tx_clock.status.get()
        resp.status