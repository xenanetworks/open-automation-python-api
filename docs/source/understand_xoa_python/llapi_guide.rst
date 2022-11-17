.. _low_level_api_label:

Low-Level API
===================================

LL-API is the bottom layer containing low-level command classes that convert human-readable parameters to and from binary data to communicate testers. The names of the low-level command classes are the same as the the CLI commands in :term:`XOA CLI`. This makes it easy for you to understand and use LL-API if you are already familiar with XOA CLI.

You can use LL-API directly in your test scripts. Using LL-API is similar to CLI scripting where no object-oriented programming mindset is required. Thus, it is easy to start with if you prefer writing test scripts in a CLI fashion, for example:

.. code-block:: python
    
    # Directly using class P_RESERVATION. This is only valid when the port is not reserved by others.
    await P_RESERVATION(handler).set(operation=ReservedAction.RESERVE)

However, the trade-off using LL-API directly is that you need to handle the connection keep-alive in your code (no *auto connection keep-alive* feature) and you need to handle the creation and deletion of stream indices, filter indices, modifier indices, etc. (no *auto index management* feature). This means there will be more lines of code in your test scripts.


API Notation and Namings
-----------------------------------

LL-API aims to be semantic in function naming to avoid expectation conflict, as well as avoiding methods that can return values of different types. The key rule is: **one method, one action**. The following notations are used throughout this chapter.

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