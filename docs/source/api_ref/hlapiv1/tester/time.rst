Time and Timekeeper
=========================

Time
----------------
Get local chassis time in seconds.

Corresponding CLI command: ``C_TIME``

.. code-block:: python

    # Time
    resp = await tester.time.get()
    resp.local_time


TimeKeeper Configuration
----------------------------
TimeKeeper config file content.

Corresponding CLI command: ``C_TKCONFIG``

.. code-block:: python

    # TimeKeeper Configuration
    await tester.time_keeper.config_file.set(config_file="filename")

    resp = await tester.time_keeper.config_file.get()
    resp.config_file

TimeKeeper GPS State
----------------------------
Get TimeKeeper GPS status.

Corresponding CLI command: ``C_TKGPSSTATE``

.. code-block:: python

    # TimeKeeper GPS State
    resp = await tester.time_keeper.gps_state.get()
    resp.status


TimeKeeper License File
----------------------------
TimeKeeper license file content.

Corresponding CLI command: ``C_TKLICFILE``

.. code-block:: python

    # TimeKeeper License File
    await tester.time_keeper.license_file.set(license_content="")
    
    resp = await tester.time_keeper.license_file.get()
    resp.license_content


TimeKeeper License State
----------------------------
State of TimeKeeper license file content.

Corresponding CLI command: ``C_TKLICSTATE``

.. code-block:: python

    # TimeKeeper License State
    resp = await tester.time_keeper.license_state.get()
    resp.license_errors
    resp.license_file_state
    resp.license_type


TimeKeeper Status
----------------------------
Version and status of TimeKeeper.

Corresponding CLI command: ``C_TKSTATUS``

.. code-block:: python

    # TimeKeeper Status
    resp = await tester.time_keeper.status.get()
    resp.status_string

    resp = await tester.time_keeper.status_extended.get()
    resp.status_string
