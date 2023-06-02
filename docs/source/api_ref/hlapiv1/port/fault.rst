Fault
=========================

Signaling
------------

.. code-block:: python

    await port.fault.signaling.set_disabled()
    await port.fault.signaling.set_force_local()
    await port.fault.signaling.set_force_remote()
    await port.fault.signaling.set_normal()
    await port.fault.signaling.get()


Status
------------

.. code-block:: python

    await port.fault.status.get()