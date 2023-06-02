Identification
=========================

Firmware Version
-----------------

.. code-block:: python

    await port.nic_firmware_version.get()


NIC Name
------------

.. code-block:: python

    await port.nic_name.get()

Status
------

.. code-block:: python
    
    await port.last_state_status.get()


License Info
-------------

.. code-block:: python

    await port.license_info.get()