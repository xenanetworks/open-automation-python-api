Capture
=========================

Trigger Criteria
----------------

.. code-block:: python

    await port.capturer.trigger.set()
    await port.capturer.trigger.get()


Frame to Keep
--------------

.. code-block:: python

    await port.capturer.keep.set_all()
    await port.capturer.keep.set_fcserr()
    await port.capturer.keep.set_filter()
    await port.capturer.keep.set_notpld()
    await port.capturer.keep.set_plderr()
    await port.capturer.keep.set_tpld()
    await port.capturer.keep.get()


State
-----------

.. code-block:: python

    await port.capturer.state.set_start()
    await port.capturer.state.set_stop()
    await port.capturer.state.get()


Statistics
-----------

.. code-block:: python

    await port.capturer.stats.get()

