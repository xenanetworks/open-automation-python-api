Replay
=========================

.. note::

    Applicable to Vulcan port only.


Utilization
--------------



.. code-block:: python

    await cg.replay.utilization.set()
    await cg.replay.utilization.get()


Replay File
-------------------



.. code-block:: python

    await cg.replay.files.indices.get()
    await cg.replay.files.clear_index(replay_file_idx)
    await cg.replay.files.name(replay_file_idx)


User Incarnation
-------------------



.. code-block:: python

    await cg.replay.user.incarnation.set_once()
    await cg.replay.user.incarnation.set_immortal()
    await cg.replay.user.incarnation.set_reincarnate()
    await cg.replay.user.incarnation.get()

    
User Repetition
-------------------



.. code-block:: python

    await cg.replay.user.repetitions.set_finite()
    await cg.replay.user.repetitions.set_infinite()
    await cg.replay.user.repetitions.get()


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


