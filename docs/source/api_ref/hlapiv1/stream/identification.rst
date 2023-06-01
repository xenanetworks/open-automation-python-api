Identification
=========================

Description
-----------

.. code-block:: python

    await stream.comment.set(comment="description")
    await stream.comment.get()

Test Payload ID
---------------

.. code-block:: python

    await stream.tpld_id.set()
    await stream.tpld_id.get()

State
-------------

.. code-block:: python

    await stream.enable.set_off()
    await stream.enable.set_on()
    await stream.enable.set_suppress()
    await stream.enable.get()

