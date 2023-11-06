Multicast
=========================

Mode
-----------

.. code-block:: python

    await port.multicast.mode.set_join()
    await port.multicast.mode.set_leave()
    await port.multicast.mode.set_off()
    await port.multicast.mode.set_on()
    await port.multicast.mode.get()


Extended Mode
--------------

.. code-block:: python

    await port.multicast.mode_extended.set()
    await port.multicast.mode_extended.get()


Source List
-----------

.. code-block:: python

    await port.multicast.source_list.set()
    await port.multicast.source_list.get()


Header
-----------

.. code-block:: python

    await port.multicast.header.set()
    await port.multicast.header.get()

