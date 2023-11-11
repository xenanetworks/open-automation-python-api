License
=========================

.. note::

    For Vulcan module only.


Clock Windback
--------------------


.. code-block:: python

    await module.license.clock_windback.get()


Demo Information
--------------------


.. code-block:: python

    await module.license.demo_info.get()


Online Mode
--------------------


.. code-block:: python

    await module.license.online_mode.set_offline()
    await module.license.online_mode.set_online()
    await module.license.online_mode.get()


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