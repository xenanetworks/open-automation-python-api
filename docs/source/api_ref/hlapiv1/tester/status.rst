Status
=========================

Health
----------------
Gets the chassis system health information.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_HEALTH`

.. code-block:: python

    # Health
    resp = await tester.health.all.get()
    resp = await tester.health.info.get()
    resp = await tester.health.uptime.get()
    resp.info