High-Level API User Guide
===========================

Code API Notation and Namings
-------------------------------

High-level API aims to be semantic in function name patterns to avoid expectation conflicts, as well as avoiding methods which can return values of a different kind. The key rule is: **One Method One Action**:

**IMPORTANT**:
    If there is a method that returns a single item or a collection of items, it is considered a bug.


``<resource>`` - representing ``Tester | Module | Port | <indices> | <namespace_class>``

``<indices>`` - representing ``Streams | Connection Groups indices`` etc.

``<namespace_class>`` - a group of commands that manage the resources of the same kind but still stays at the same level as others

``<command_oo_name>`` - the name of the command modified to adapt to the object-oriented concept. Commands of the same access level, which access or modify parameters of the same kind, are grouped under one ``<namespace_class>`` as shown in the example below:


.. code-block::

    P_SPEEDSELECTION
    P_SPEEDS_SUPPORTED

are represented as

.. code-block:: python

    <resource>.speed.selection
    <resource>.speed.supported


Attributes and Methods
------------------------

There are only two types of methods for each command, ``get`` and/or ``set``. ``get`` is used to query values, status, configuration of the command. ``set`` is the change.

To use ``get`` and ``set`` methods, you need to use ``await`` because they are all made asynchronous. Read more about Python `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_.

.. code-block:: python

    await <resource>.<command_oo_name>.get()

    await <resource>.<command_oo_name>.set(<values>)

    await <resource>.<command_oo_name>.set_<variation__name>()

    await <resource>.<command_oo_name>.set_<variation__name>(<extra_value>)


Event Subscription and Push Notification
----------------------------------------------

Structure: ``<resource>.on_<command_oo_name>_change(<async_callback_function>)``

The ``<async_callback_function>`` must be an `coroutine <https://docs.python.org/3/library/asyncio-task.html#id1>`_ function. Parameters, which can be passed to ``<async_callback_function>``, depend on what resource it is affiliated. Examples are shown below:

Under the tester level
^^^^^^^^^^^^^^^^^^^^^^^^

::

    <ref_tester>, <new_value>


Under the Module level
^^^^^^^^^^^^^^^^^^^^^^^^

::

    <ref_module>, <new_value>


Under the Port level
^^^^^^^^^^^^^^^^^^^^^^^^

::
    <ref_port>, <new_value>


**Exception**:
    Exception to the rule above is the event ``on_disconnected``. The parameters passed to it are ``tuple(<tester_ip: str>, <tester_port: int>)``


**IMPORTANT**:
    A subscription to an event only provides a tool for notifying the external code. It is unnecessary to update the library instance state manually, because it is automatically handled by the library code.


**IMPORTANT**:
    It is allowed to subscribe multiple callback functions to one event.


Resource Managers
----------------------------------------------

Most of the sublevel resources, which are organized into collections, are handled by resource managers.

The most commonly used resource managers are ``Module Manager | Port Manager | Index Manager``.

**IMPORTANT**:
    Each resource manager is an `iterable object <https://wiki.python.org/moin/Iterator>`_


An illustration of the the resource managers and test resources are shown below:

::

    ------------
    |  Tester  |
    ------------
        |
    *******************
    |  module manager |
    *******************
        |
        |   --------------
        |---|  Module 0  |
        |   --------------
        |        |
        |    *******************
        |    |   port manager  |
        |    *******************
        |        |
        |        |    --------------   *****************
        |        |----|  Port 0    | - | index manager |
        |        |    --------------   *****************
        |        |    --------------   *****************
        |        |----|  Port 1    | - | index manager |
        |        |    --------------   *****************
        |        |    --------------   *****************
        |        |----|  Port N-1  | - | index manager |
        |             --------------   *****************
        |
        |   --------------
        |---|  Module 1  |
        |   --------------
        |        |
        |    *******************
        |    |   port manager  |
        |    *******************
        |        |
        |        |    --------------   *****************
        |        |----|  Port 0    | - | index manager |
        |        |    --------------   *****************
        |        |    --------------   *****************
        |        |----|  Port 1    | - | index manager |
        |        |    --------------   *****************
        |        |    --------------   *****************
        |        |----|  Port N-1  | - | index manager |
        |             --------------   *****************
        |
        |   --------------
        |---| Module N-1 |
            --------------


Module and Port Managers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each tester contains a ``Module Manager``, which can be accessed through attribute ``modules``. Each module contains a ``Port Manager``.

**IMPORTANT**:
    A ``Module Manager`` can contain modules of different **Module Types**. This is because there can be various test modules installed in a physical tester. On the other hand, a ``Port Manager`` contains ports of the same **Port Type**. This is because the ports on a module are of the same type.

Methods to retrieve a module or a port from a resource manager:
.. code-block:: python

    obtain(<module_slot_number> | <port_index>)

Code example:
.. literalinclude:: code_example/high_level/obtain_one_module.py


Methods to retrieve _multiple_ resources from a resource manager:
.. code-block:: python

    obtain_multiple(<module_index> | <port_index>, ...)

Code example:
.. literalinclude:: code_example/high_level/obtain_multiple_module.py


Index Manager
^^^^^^^^^^^^^^^^^^^^

``Index Manager`` manages the sub-port-level resource indices such as stream indices, filter indices, connection group indices, etc. It automatically ensures correct and conflict-free index assignment.

**IMPORTANT**:
    It is the user's responsibility to create, retrieve, and remove those sub-port-level indices.

Thanks to the index manager of a port, users don't necessarily need to handle the index assignment.

To create an index, use method ``create()``.
To remove an index, use method ``remove()``. An index also can be removed without accessing the manager but by calling ``<index_instance>.delete()``.

The call of the function ``<index_instance>.delete()`` will remove a resource index from the port, and will automatically notify the index manager of the port about the removal. The index manager will make sure the freed index is used when the user creates again next time.


Session
---------------

A ``session`` will be created automatically after a TCP connection is established between the client and the tester.

Three attributes of a ``session`` are exposed:
* ``is_online`` - property to validate if the TCP connection is alive.
* ``logoff()`` - async method for gracefully closing the TCP connection to the tester.
* ``sessions_info()`` - async method for getting information of the current active sessions on a tester.

Session Identification
^^^^^^^^^^^^^^^^^^^^^^^^^^

* A tester does not use the tuple (source IP, source port, destination IP, destination port) to identify a session. Instead, it uses the username as the identification of a session. For instance, ``tester = await testers.L23Tester("192.168.1.200", "JonDoe")``, where the username is ``JonDoe``.

Session Recovery and Resource Reallocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* To recover the session, the client only needs to establish a new TCP connection with the same username as the dropped session.
* All resources of the broken session will be automatically transferred to the new session because they have the same username.

Handling Multiple Same-Username Sessions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If multiple sessions use the same username to connect to a tester after a broken session, the tester will give the control of the resources to a session in a first-come-first-served manner, and the others will be treated as observers. Thus, duplicated username should be avoided at the session level.
* If the controlling session is disconnected, the tester will automatically pass the control of the resources to the next session in the queue.

Local State
---------------------

The access to the local state of a resource is done through property ``<resource>.info``. The info contains current status of the resource and information of its attributes, which cannot be changed during a running ``session``.


Code Examples
----------------------------

The boilerplate code that is used to run all of the examples.

.. literalinclude:: code_example/boilerplate.py

Tester Instance
^^^^^^^^^^^^^^^^^^^^^^

Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

**Creating a tester instance from one of the available tester types**

Available tester types are  ``L23Tester | L47Tester | L47VeTester``.

.. literalinclude:: code_example/high_level/create_a_tester_from_type.py


**Create a tester instance by using context manager**
.. literalinclude:: code_example/high_level/create_a_tester_contextm.py


**Create multiple tester instances**
.. literalinclude:: code_example/high_level/create_multi_testers.py


Read more about `await asyncio.gather <https://docs.python.org/3/library/asyncio-task.html#asyncio.gather>`_.


Obtain Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Obtain one module**
.. literalinclude:: code_example/high_level/obtain_one_module.py


**Obtain multiple modules**
.. literalinclude:: code_example/high_level/obtain_multiple_module.py


**Process operation on all modules**
.. literalinclude:: code_example/high_level/oper_on_all_modules.py

**Obtain multiple ports**
The interface of obtaining multiple ports is equivalent to obtaining multiple modules with the following exceptions:
* all ports are of the same type
* all ports are aligned from index 0 to ``max_port_count-1``

.. literalinclude:: code_example/high_level/obtain_multiple_ports.py


Data Exchange
^^^^^^^^^^^^^^^^^^

**Querying parameters**

**IMPORTANT**:
    Resource reservation is not required to query information from the tester.

.. literalinclude:: code_example/high_level/query_parameters.py

**Setting parameters**

**IMPORTANT**:
    Reservation is required to set parameter to: ``Tester | Module | Port``.

.. literalinclude:: code_example/high_level/setting_parameters.py


Statistics Collection
^^^^^^^^^^^^^^^^^^^^^^^^^^

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

.. literalinclude:: code_example/high_level/stats_collection.py

