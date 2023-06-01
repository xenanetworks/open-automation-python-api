Identification
=========================

Interface
----------

.. code-block:: python

    await port.interface.get()

    port.on_interface_change(_callback_func)


Description
-----------

.. code-block:: python

    await port.comment.set(comment="description")
    await port.comment.get()

Legacy Model
------------

.. code-block:: python

    await module.mode.get()

Model
-------------

.. code-block:: python

    await module.revision.get()


Serial Number
-----------------

.. code-block:: python

    await module.serial_number.get()


Firmware Version
-----------------

.. code-block:: python

    await module.version_number.get()


Port Count
------------

.. code-block:: python

    await module.port_count.get()

Status
------

.. code-block:: python
    
    await module.status.get()