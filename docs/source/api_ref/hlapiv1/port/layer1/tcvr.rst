Transceiver
=========================


Status
------------------
Get various tcvr status information. RX loss status of the individual RX optical lanes (only 4 lanes are supported currently).

Corresponding CLI command: ``P_TCVRSTATUS``

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

Corresponding CLI command: ``PX_RW``

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

Corresponding CLI command: ``PX_RW_SEQ``

.. code-block:: python
    
    # Transceiver Sequential Read & Write
    await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).set(value=Hex("00FF00FF"))
    
    resp = await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).get()
    resp.value


MII
------------------
Provides access to the register interface supported by the media-independent interface (MII) transceiver. It is possible to both read and write register values.

Corresponding CLI command: ``PX_MII``

.. code-block:: python
    
    # Transceiver MII
    await port.transceiver.access_mii(register_address=0).set(value=Hex("00"))
    
    resp = await port.transceiver.access_mii(register_address=0).get()
    resp.value


Temperature
------------------
Transceiver temperature in degrees Celsius.

Corresponding CLI command: ``PX_TEMPERATURE``

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

Corresponding CLI command: ``PP_RXLASERPOWER``

.. code-block:: python
    
    # Transceiver RX Laser Power
    resp = await port.pcs_pma.transceiver.rx_laser_power.get()
    resp.nanowatts


TX Laser Power
--------------
Reading of the optical power level of the transmission signal. There is one
value for each laser/wavelength, and the number of these depends on the kind of CFP transceiver used. The list is empty if the CFP transceiver does not support optical power read-out.

Corresponding CLI command: ``PP_TXLASERPOWER``

.. code-block:: python
    
    # Transceiver TX Laser Power
    resp = await port.pcs_pma.transceiver.tx_laser_power.get()
    resp.nanowatts
