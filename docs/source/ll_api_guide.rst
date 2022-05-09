.. _low-level-api-label:

Low-Level API
===================================

:term:`LL-API` gives the developer the complete direct control of the tester since the name of the API is the same as what is defined in the :term:`CLI`. But sometimes it is difficult to remember all the arguments, resulting a waste of time reading the length class definition. 

However, if the developer needs to migrate a :term:`CLI` script to :term:`XOA`, the :term:`LL-API` can explicitly show the command name, which may speed up the migration process.


API Notation and Namings
-----------------------------------

:term:`LL-API` aims to be semantic in function naming to avoid expectation conflict, as well as avoiding methods that can return values of different types. The key rule is: **one method, one action**. The following notations are used throughout this chapter.

:``<indices>``:
    
    Represents *stream indices*, *connection group indices*, *filter indices*, etc.

:``<prefix_command_group>``:
    
    A group of commands that manage the resources of the same kind but still stays at the same level as others. For example, ``P_SPEEDSELECTION`` and ``P_SPEEDS_SUPPORTED`` are in the ``P_`` category.

:``<command_name>``:
    
    The CLI name of the command. Commands of the same access level, which access or modify parameters of the same kind, are grouped under one command group as shown in the example below.

.. code-block::
    :linenos:

    P_SPEEDSELECTION
    P_SPEEDS_SUPPORTED

are represented as

.. code-block:: python
    :linenos:

    P_SPEEDSELECTION(TransportationHandler, <indices>)
    P_SPEEDS_SUPPORTED(TransportationHandler, <indices>)

.. note::

    If there is a method returning both a single value and multiple values, it is considered a bug.


Attributes and Methods
------------------------------

There are only two types of methods for each command, ``get`` and/or ``set``. ``get`` is used to query values, status, configuration of the command. ``set`` is the change.

To use ``get`` and ``set`` methods, you need to use ``await`` because they are all made asynchronous.

**Syntax**:

.. code-block:: python
    :linenos:

    await <command_name>(TransportationHandler, <indices>).get()

    await <command_name>(TransportationHandler, <indices>).set(<values>)

**Example**:

.. code-block:: python
    :linenos:

    await P_SPEEDS_SUPPORTED(TransportationHandler, 0).get()

    await P_SPEEDSELECTION(TransportationHandler, 0).set(PortSpeedMode.AUTO)


.. seealso::
    
    `Read more about Python awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_.


Code Examples
--------------------

The boilerplate code that is used to run all of the examples.

.. literalinclude:: /code_example/boilerplate.py
    :linenos:


Tester Connection
^^^^^^^^^^^^^^^^^^^^^^^^

Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

**Creating a connection to the tester**

.. literalinclude:: /code_example/ll/create_conn_to_tester.py
    :linenos:


**Create multiple connections**

.. literalinclude:: /code_example/ll/create_multiple_conns.py
    :linenos:


Obtain Resources
^^^^^^^^^^^^^^^^^^^^^^^^

**Obtain one module**

.. literalinclude:: /code_example/ll/obtain_one_module.py
    :linenos:


**Obtain multiple modules**

.. literalinclude:: /code_example/ll/obtain_multiple_modules.py
    :linenos:


Data Exchange
^^^^^^^^^^^^^^^^^^^^

**Querying parameters**

.. note::

    Resource reservation is not required to query information from the tester.

.. literalinclude:: /code_example/ll/query_parameters.py
    :linenos:

**Setting parameters**

.. note::
    
    Reservation is required to set parameter to ``Tester``, ``Module``, and ``Port``.

.. literalinclude:: /code_example/ll/setting_parameters.py
    :linenos:


Statistics Collection
^^^^^^^^^^^^^^^^^^^^^^^^

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

.. literalinclude:: /code_example/ll/stats_collection.py
    :linenos:


