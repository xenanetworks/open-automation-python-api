System
=========================

.. note::

    For Vulcan module only.


Memory Information
--------------------


.. code-block:: python

    await module.memory_info.get()


Identifier
--------------------


.. code-block:: python

    await module.module_system.id.get()


Status
--------------------


.. code-block:: python

    await module.module_system.status.get()


Time
----------------------------


.. code-block:: python

    await module.module_system.time.set()
    await module.module_system.time.get()


Compatible Client Version
----------------------------


.. code-block:: python

    await module.compatible_client_version.get()