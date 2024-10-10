Energy Efficiency Ethernet
==========================


Capabilities
------------
Read EEE capabilities of the port (variable size, one for each supported speed, returns 0s if no EEE).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_LPSUPPORT`

.. code-block:: python

    # EEE- Capabilities
    resp = await port.eee.capabilities.get()
    resp.eee_capabilities


Partner Capabilities
--------------------
Displays the EEE capabilities advertised during auto-negotiation by the far side (link partner).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_LPPARTNERAUTONEG`

.. code-block:: python

    # EEE - Partner Capabilities
    resp = await port.eee.partner_capabilities.get()
    resp.cap_1000base_t
    resp.cap_100base_kx
    resp.cap_10gbase_kr
    resp.cap_10gbase_kx4
    resp.cap_10gbase_t


Control
------------
Enables/disables Energy Efficient Ethernet (EEE) on the port.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_LPENABLE`

.. code-block:: python

    # EEE - Control
    await port.eee.enable.set(on_off=enums.OnOff.OFF)
    await port.eee.enable.set_off()
    await port.eee.enable.set(on_off=enums.OnOff.ON)
    await port.eee.enable.set_on()

    resp = await port.eee.enable.get()
    resp.on_off


Low Power TX Mode
-----------------
Enables/disables the transmission of Low Power Idles (LPIs) on the port. When enabled, the transmit side of the port will automatically enter low-power mode (and leave) low-power mode in periods of low or no traffic. LPIs will only be transmitted if the Link Partner (receiving port) has advertised EEE capability
for the selected port speed during EEE auto-negotiation.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_LPTXMODE`

.. code-block:: python

    # EEE - Low Power TX Mode
    await port.eee.mode.set(on_off=enums.OnOff.ON)
    await port.eee.mode.set_off()
    await port.eee.mode.set(on_off=enums.OnOff.OFF)
    await port.eee.mode.set_on()

    resp = await port.eee.mode.get()
    resp.on_off


RX Power
------------
Obtain the RX power recorded during training for the four channels.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_LPRXPOWER`

.. code-block:: python

    # EEE - RX Power
    resp = await port.eee.rx_power.get()
    resp.channel_a
    resp.channel_b
    resp.channel_c
    resp.channel_d


SNR Margin
------------
Displays the SNR margin on the four link channels (Channel A-D) as reported by the PHY. It is displayed in units of 0.1dB.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_LPSNRMARGIN`

.. code-block:: python

    # EEE - SNR Margin
    resp = await port.eee.snr_margin.get()
    resp.channel_a
    resp.channel_b
    resp.channel_c
    resp.channel_d


Status
------------
Displays the Energy Efficient Ethernet (EEE) status as reported by the PHY.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_LPSTATUS`

.. code-block:: python

    # EEE - Status
    resp = await port.eee.status.get()
    resp.link_up
    resp.rxc
    resp.rxh
    resp.txc
    resp.txh

