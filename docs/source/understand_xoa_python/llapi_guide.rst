.. _low_level_api_label:

Low-Level API
===================================

LL-API contains low-level API classes, giving you the direct control of the tester. The names of the classes are the same as the the CLI commands in :term:`XOA CLI`, making it easy for you to understand the Python API if you are already familiar with XOA CLI.

However, unlike HL-API, LL-API does not provide functionalities such as *auto connection keep-alive* and *auto index management*. This means you need to write more codes to handle those yourself.


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
    

    P_SPEEDSELECTION
    P_SPEEDS_SUPPORTED

are represented as

.. code-block:: python
    

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
    

    await <command_name>(TransportationHandler, <indices>).get()

    await <command_name>(TransportationHandler, <indices>).set(<values>)

**Example**:

.. code-block:: python
    

    await P_SPEEDS_SUPPORTED(TransportationHandler, 0).get()

    await P_SPEEDSELECTION(TransportationHandler, 0).set(PortSpeedMode.AUTO)


.. seealso::
    
    `Read more about Python awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_.