Transceiver
=========================


Status
------------------
Get various tcvr status information. RX loss status of the individual RX optical lanes (only 4 lanes are supported currently).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.p_commands.P_TCVRSTATUS`

.. code-block:: python
    
    # Transceiver Status
    resp = await port.tcvr_status.get()
    resp.rx_loss_lane_0
    resp.rx_loss_lane_1
    resp.rx_loss_lane_2
    resp.rx_loss_lane_3


Read & Write
-------------
Provides read and write access to the register interface supported by the port transceiver. It is possible to both read and write register values.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.px_commands.PX_RW`

.. code-block:: python

    # Transceiver Read & Write
    await port.transceiver.access_rw(page_address=0, register_address=0).set(value=Hex("FF"))
    
    resp = await port.transceiver.access_rw(page_address=0, register_address=0).get()
    resp.value

Sequential Read & Write
-----------------------
I2C sequential access to a transceiver's register.
When invoked, the ``<byte_count>`` number of bytes will be read or written in one I2C transaction, in which the ``<value>`` is read or written with only a single register address setup. A subsequent invocation will perform a second I2C transaction in the same manner.

``<_page_xindex>``: the transceiver page address, integer, 0-255.
``<_register_xaddress>``: the address within the page, integer, 0-255.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.px_commands.PX_RW_SEQ`

.. code-block:: python
    
    # Transceiver Sequential Read & Write
    await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).set(value=Hex("00FF00FF"))
    
    resp = await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).get()
    resp.value

Sequential Read & Write (Banked)
--------------------------------
I2C sequential access to a transceiver's register.
When invoked, the ``<byte_count>`` number of bytes will be read or written in one I2C transaction, in which the ``<value>`` is read or written with only a single register address setup. A subsequent invocation will perform a second I2C transaction in the same manner.

``<bank_xindex>``: the bank address, integer, 0-255.
``<_page_xindex>``: the transceiver page address, integer, 0-255.
``<_register_xaddress>``: the address within the page, integer, 0-255.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.px_commands.PX_RW_SEQ_BANK`

.. code-block:: python
    
    # Transceiver Sequential Read & Write (banked)
    await port.transceiver.access_rw_seq_bank(bank_address=1, page_address=0x9F, register_address=200, byte_count=1).set(value=Hex("00"))
    
    resp = await port.transceiver.access_rw_seq_bank(bank_address=1, page_address=0x9F, register_address=200, byte_count=1).get()
    resp.value

MII
------------------
Provides access to the register interface supported by the media-independent interface (MII) transceiver. It is possible to both read and write register values.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.px_commands.PX_MII`

.. code-block:: python
    
    # Transceiver MII
    await port.transceiver.access_mii(register_address=0).set(value=Hex("00"))
    
    resp = await port.transceiver.access_mii(register_address=0).get()
    resp.value


Temperature
------------------
Transceiver temperature in degrees Celsius.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.px_commands.PX_TEMPERATURE`

.. code-block:: python
    
    # Transceiver Temperature
    resp = await port.transceiver.access_temperature().get()
    resp.integral_part
    resp.fractional_part


RX Laser Power
--------------
Reading of the optical power level of the received signal. There is one value
for each laser/wavelength, and the number of these depends on the kind of CFP
transceiver used. The list is empty if the CFP transceiver does not support
optical power read-out.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_RXLASERPOWER`

.. code-block:: python
    
    # Transceiver RX Laser Power
    resp = await port.pcs_pma.transceiver.rx_laser_power.get()
    resp.nanowatts


TX Laser Power
--------------
Reading of the optical power level of the transmission signal. There is one
value for each laser/wavelength, and the number of these depends on the kind of CFP transceiver used. The list is empty if the CFP transceiver does not support optical power read-out.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pp_commands.PP_TXLASERPOWER`

.. code-block:: python
    
    # Transceiver TX Laser Power
    resp = await port.pcs_pma.transceiver.tx_laser_power.get()
    resp.nanowatts
