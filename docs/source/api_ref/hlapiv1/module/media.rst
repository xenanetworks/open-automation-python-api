Media
=========================

Media Configuration
-------------------

.. code-block:: python

    await module.media.set()
    await module.media.get()

Supported Media
---------------

.. code-block:: python

    await module.available_speeds.get()


Port Configuration
------------------

.. code-block:: python

    await module.cfp.config.set(portspeed_list=[1, 800000])
    await module.cfp.config.set(portspeed_list=[2, 400000, 400000])
    await module.cfp.config.set(portspeed_list=[4, 200000, 200000, 200000, 200000])
    await module.cfp.config.set(portspeed_list=[8, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])
    await module.cfp.config.get()


CFP Type
---------------

.. code-block:: python

    await module.cfp.type.get()