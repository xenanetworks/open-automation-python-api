Status
=========================

Health
----------------
Gets the chassis system health information.

Corresponding CLI command: ``C_HEALTH``

.. code-block:: python

    # Health
    resp = await tester.health.all.get()
    resp = await tester.health.info.get()
    resp = await tester.health.uptime.get()
    resp.info