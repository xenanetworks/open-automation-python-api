Low-Level API User Guide
===========================

Low-level API gives the developer the complete direct control of the tester since the name of the API is the same as what is defined in the CLI. But sometimes it is difficult to remember all the arguments, resulting a waste of time reading the length class definition. 

However, if the developer needs to migrate a CLI script to XOA Python API script, the low-level API can explicitly show the command name, which may speed up the migration process.

Code API Notation and Namings
-------------------------------

The API trying to be semantic in function name patterns to avoid expectation conflicts, as well as avoiding methods which can return values of a different kind. The key rule is: **One Method One Action**:

**IMPORTANT**:
    If there is a method that returns a single item or a collection of items, it is considered a BUG.

``<indices>`` - representing ``Streams | Connection Groups`` indices etc.

``<prefix_command_group>`` - a group of commands that manage the resources of the same kind but still stays at the same level as others

``<command_name>`` - the name of the command's unmodified name. Commands of the same access level, which access or modify parameters of the same kind, are grouped under one ``p_commands`` group as shown in the example below:

.. code-block::

    P_SPEEDSELECTION
    P_SPEEDS_SUPPORTED

are represented as

.. code-block:: python

    P_SPEEDSELECTION(TransportationHandler, indices)
    P_SPEEDS_SUPPORTED(TransportationHandler, indices)


Attributes and Methods
-------------------------------

There are only two types of methods for each command, ``get`` and/or ``set``. ``get`` is used to query values, status, configuration of the command. ``set`` is the change.

To use ``get`` and ``set`` methods, you need to use ``await`` because they are all made asynchronous. Read more about Python `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_.

.. code-block:: python

    await <command_name>(TransportationHandler, indices).get()

    await <command_name>(TransportationHandler, indices).set(<values>)


Code Examples
-------------------------------

The boilerplate code that is used to run all of the examples.

.. literalinclude:: code_example/boilerplate.py


Tester Connection
^^^^^^^^^^^^^^^^^^^^^^

Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

**Creating a connection to the tester**
.. literalinclude:: code_example/low_level/create_conn_to_tester.py


**Create multiple connections**
.. literalinclude:: code_example/low_level/create_multiple_conns.py


Obtain Resources
^^^^^^^^^^^^^^^^^^^^^^

**Obtain one module**
.. literalinclude:: code_example/low_level/obtain_one_module.py


**Obtain multiple modules**
.. literalinclude:: code_example/low_level/obtain_multiple_modules.py


Data Exchange
^^^^^^^^^^^^^^^^^^^^^^

**Querying parameters**

**IMPORTANT**:
    Resource reservation is not required to query information from the tester.

.. literalinclude:: code_example/low_level/query_parameters.py

**Setting parameters**

**IMPORTANT**:
    Reservation is required to set parameter to ``Tester``, ``Module``, and ``Port``.

.. literalinclude:: code_example/low_level/setting_parameters.py


Statistics Collection
^^^^^^^^^^^^^^^^^^^^^^

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

.. literalinclude:: code_example/low_level/stats_collection.py
