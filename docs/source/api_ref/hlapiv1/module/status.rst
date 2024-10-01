Status
=========================

Health
----------------
Gets the module health information.

Corresponding CLI command: ``M_HEALTH``

.. code-block:: python

    # Health
    resp = await module.health.all.get()
    resp = await module.health.info.get()
    resp = await module.health.cage_insertion.get()