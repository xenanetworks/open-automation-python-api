TX Profile
=========================

Rate Fraction
---------------

.. code-block:: python

    await stream.rate.fraction.set()
    await stream.rate.fraction.get()


Packet Rate
-------------------------

.. code-block:: python

    await stream.rate.pps.set()
    await stream.rate.pps.get()


Bit Rate L2
--------------------------

.. code-block:: python

    await stream.rate.l2bps.set()
    await stream.rate.l2bps.get()



Packet Limit
--------------------------

.. code-block:: python

    await stream.packet.limit.set()
    await stream.packet.limit.get()


Burst Size and Density
--------------------------

.. code-block:: python

    await stream.burst.burstiness.set()
    await stream.burst.burstiness.get()


Inter Burst/Packet Gap
--------------------------

.. code-block:: python

    await stream.burst.gap.set()
    await stream.burst.gap.get()


Priority Flow
--------------------------

.. code-block:: python

    await stream.priority_flow.set()
    await stream.priority_flow.get()
