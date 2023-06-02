Transceiver
=========================


Status
------------------

.. code-block:: python
    
    await port.tcvr_status.get()


Read & Write
-------------

.. code-block:: python

    await port.transceiver.access_rw(page_address, register_address).set()
    await port.transceiver.access_rw(page_address, register_address).get()


Sequential Read & Write
-----------------------

.. code-block:: python
    
    await port.transceiver.access_rw_seq(page_address, register_address, byte_count).set()
    await port.transceiver.access_rw_seq(page_address, register_address, byte_count).get()


MII
------------------

.. code-block:: python
    
    await port.transceiver.access_mii(register_address).set()
    await port.transceiver.access_mii(register_address).get()


Temperature
------------------

.. code-block:: python
    
    await port.transceiver.access_temperature().get()


RX Laser Power
--------------

.. code-block:: python
    
    await port.pcs_pma.transceiver.rx_laser_power.get()


TX Laser Power
--------------

.. code-block:: python
    
    await port.pcs_pma.transceiver.tx_laser_power.get()