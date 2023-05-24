Session
=========================

Information
-----------

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

.. code-block:: python

    await tester.session.logoff()
    tester.on_disconnected(_callback_func)