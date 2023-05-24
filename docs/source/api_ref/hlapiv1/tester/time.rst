Time and Timekeeper
=========================

Time
----------------

.. code-block:: python

    await tester.time.get()


TimeKeeper Configuration
----------------------------

.. code-block:: python

    await tester.time_keeper.config_file.set(config_file="filename")
    await tester.time_keeper.config_file.get()

TimeKeeper GPS State
----------------------------

.. code-block:: python

    await tester.time_keeper.gps_state.get()


TimeKeeper License File
----------------------------

.. code-block:: python

    await tester.time_keeper.license_file.set(license_content="")
    await tester.time_keeper.license_file.get()


TimeKeeper License State
----------------------------

.. code-block:: python

    await tester.time_keeper.license_state.get()


TimeKeeper Status
----------------------------

.. code-block:: python

    await tester.time_keeper.status.get()
    await tester.time_keeper.status_extended.get()
