Raw
=========================

.. note::

    Applicable to Vulcan port only.


Test Scenario
--------------

.. code-block:: python

    await cg.raw.test_scenario.set_echo()
    await cg.raw.test_scenario.set_download()
    await cg.raw.test_scenario.set_upload()
    await cg.raw.test_scenario.set_both()
    await cg.raw.test_scenario.get()


Utilization
--------------

.. code-block:: python

    await cg.raw.utilization.set()
    await cg.raw.utilization.get()


Transmission Config
-------------------

.. code-block:: python

    await cg.raw.tx.during_ramp.set()
    await cg.raw.tx.during_ramp.get()

    await cg.raw.tx.time_offset.set()
    await cg.raw.tx.time_offset.get()


Burst Config
-------------------

.. code-block:: python

    await cg.raw.bursty.transmission.set_on()
    await cg.raw.bursty.transmission.set_off()
    await cg.raw.bursty.transmission.get()

    await cg.raw.bursty.config.set()
    await cg.raw.bursty.config.get()

    
Connection Close
-------------------

.. code-block:: python

    await cg.raw.connection.close_condition.set_none()
    await cg.raw.connection.close_condition.set_client()
    await cg.raw.connection.close_condition.set_server()
    await cg.raw.connection.close_condition.get()


Connection Incarnation
----------------------

.. code-block:: python

    await cg.raw.connection.incarnation.set_once()
    await cg.raw.connection.incarnation.set_immortal()
    await cg.raw.connection.incarnation.set_reincarnate()
    await cg.raw.connection.incarnation.get()


Connection Lifetime
-------------------

.. code-block:: python

    await cg.raw.connection.lifetime.set_msecs()
    await cg.raw.connection.lifetime.set_seconds()
    await cg.raw.connection.lifetime.set_minutes()
    await cg.raw.connection.lifetime.set_hours()
    await cg.raw.connection.lifetime.get()


Connection Repetition
----------------------

.. code-block:: python

    await cg.raw.connection.repetitions.set_finite()
    await cg.raw.connection.repetitions.set_infinite()
    await cg.raw.connection.repetitions.get()


Download Request Content
-------------------------

.. code-block:: python

    await cg.raw.download_request.content.set()
    await cg.raw.download_request.content.get()


Download Request Server Wait
----------------------------

.. code-block:: python

    await cg.raw.download_request.server_must_wait.set_yes()
    await cg.raw.download_request.server_must_wait.set_no()
    await cg.raw.download_request.server_must_wait.get()



Download Request Transaction Limit
----------------------------------

.. code-block:: python

    await cg.raw.download_request.transactions_number.set_finite()
    await cg.raw.download_request.transactions_number.set_infinite()
    await cg.raw.download_request.transactions_number.get()


Payload Type
----------------------

.. code-block:: python

    await cg.raw.payload.type.set_fixed()
    await cg.raw.payload.type.set_increment()
    await cg.raw.payload.type.set_longrandom()
    await cg.raw.payload.type.set_random()
    await cg.raw.payload.type.get()


Payload Content
----------------------

.. code-block:: python

    await cg.raw.payload.content.set()
    await cg.raw.payload.content.get()


Payload Repeat Length
----------------------

.. code-block:: python

    await cg.raw.payload.repeat_length.set()
    await cg.raw.payload.repeat_length.get()


Payload Total Length
----------------------

.. code-block:: python

    await cg.raw.payload.total_length.set_finite()
    await cg.raw.payload.total_length.set_infinite()
    await cg.raw.payload.total_length.get()


Payload RX Length
----------------------

.. code-block:: python

    await cg.raw.payload.rx_length.set_infinite()
    await cg.raw.payload.rx_length.set_finite()
    await cg.raw.payload.rx_length.get()


