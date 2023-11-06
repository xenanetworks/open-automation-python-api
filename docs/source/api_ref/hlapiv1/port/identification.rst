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


Status
------

.. code-block:: python
    
    await port.status.get()