Load Profile
=========================

.. note::

    Applicable to Vulcan port only.

Shape
------



.. code-block:: python

    await cg.load_profile.shape.set()
    await cg.load_profile.shape.get()


Time Scale
----------



.. code-block:: python

    await cg.load_profile.time_scale.set_msecs()
    await cg.load_profile.time_scale.set_seconds()
    await cg.load_profile.time_scale.set_minutes()
    await cg.load_profile.time_scale.set_hours()
    await cg.load_profile.time_scale.get()