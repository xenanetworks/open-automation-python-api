Packet Engine
=========================

.. note::

    For Vulcan module only.


License Information
--------------------


.. code-block:: python

    await module.packet_engine.license_info.get()


Mode
--------------------


.. code-block:: python

    await module.packet_engine.mode.set_advanced()
    await module.packet_engine.mode.set_simple()
    await module.packet_engine.mode.get()


Reservation
--------------------


.. code-block:: python

    await module.packet_engine.reserve.set()
    await module.packet_engine.reserve.get()


Update
----------------------------


.. code-block:: python

    await module.license.update.set()


Update Status
----------------------------


.. code-block:: python

    await module.license.update_status.get()


Management Information
----------------------------


.. code-block:: python

    await module.license.management_info.get()


List License BSON Files
----------------------------


.. code-block:: python

    await module.license.list_bson.get()