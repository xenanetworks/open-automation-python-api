Session
=========================

Information
-----------

The following are pre-fetched in cache when connection is established, thus no need to use ``await``.

.. code-block:: python

    tester.session.owner_name
    tester.session.keepalive
    tester.session.pwd
    tester.session.is_online
    tester.session.sessions_info
    tester.session.timeout
    tester.is_released()
    tester.is_reserved_by_me()

Logoff
----------
Terminates the current session. Courtesy only, the chassis will also
handle disconnection at the TCP/IP level.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.c_commands.C_LOGOFF`

.. code-block:: python

    await tester.session.logoff()
    tester.on_disconnected(_callback_func)