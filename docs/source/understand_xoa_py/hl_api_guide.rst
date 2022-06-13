.. _high_level_api_label:

High-Level API Guide
===================================

:term:`HL-API` provides abstraction that helps developers to quickly develop scripts or program in an object-oriented fashion with explicit definition of commands of different *tester*, *module*, *port* types. In addition, HL-API provides features such as:

* :ref:`Auto connection keep-alive <session_label>`
* :ref:`Auto index management <resource_managers_label>`
* :ref:`Resources identification tracking for push notification <event_subscription_label>`

API Notation and Namings
--------------------------------

:term:`HL-API` aims to be semantic in function naming to avoid expectation conflict, as well as avoiding methods that can return values of different types. The key rule is: **one method, one action**. The following notations are used throughout this chapter.

:``<resource>``:
    
    Represents ``Tester | Module | Port | <indices> | <namespace_class>``.

:``<indices>``:
    
    Represents *stream indices*, *connection group indices*, *filter indices*, etc.

:``<namespace_class>``:

    A group of commands that manage the resources of the same kind but still stays at the same level as others.

:``<command_oo_name>``:

    command name adapted to the object-oriented programming concept. Commands of the same access level, which read or modify parameters of the same type, are grouped under one ``<namespace_class>``.
    
An example of :term:`HL-API` notation and namings based on the corresponding :term:`CLI` command names:

.. code-block::
    :caption: CLI command names
    :linenos:

    P_SPEEDSELECTION
    P_SPEEDS_SUPPORTED

are represented as

.. code-block:: python
    :caption: Corresponding HL-API naming
    :linenos:

    <resource>.speed.selection
    <resource>.speed.supported

.. note::

    If there is a method returning both a single value and multiple values, it is considered a bug.

Attributes and Methods
--------------------------------

There are only two types of methods for each command, ``get`` and/or ``set``:

* Method ``get`` is used to **query** the values, status, configuration of the resource.
* Method ``set`` is used to **change** the values, status, configuration of the resource.

To use ``get`` and ``set`` methods, you need to use ``await`` because they are all made asynchronous.

**Syntax**:

.. code-block:: python
    :linenos:

    await <resource>.<command_oo_name>.get()

    await <resource>.<command_oo_name>.set(<values>)

    await <resource>.<command_oo_name>.set_<variation_name>()

    await <resource>.<command_oo_name>.set_<variation_name>(<extra_value>)

**Example**:

.. code-block:: python
    :linenos:

    await <Port>.speed.supported.get()

    await <Port>.speed.selection.set(mode=PortSpeedMode.AUTO)

    await <Port>.<resource>.speed.selection.set_auto()

    await <Stream>.packet.length.set_incrementing(min_val=100, max_val=500)

.. seealso::

    `Learn more about Python awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_.


.. _event_subscription_label:

Event Subscription and Push Notification
----------------------------------------------------------------

Periodical querying of test resource information, such as port sync statue, is low in communication efficiency and less responsive. Different from :term:`CLI`, :term:`HL-API` supports push notification sent from the chassis server when the state or the configuration of a test resource changes. For instance, when a port starts generating traffic, its traffic state is changed from off to on, thus all the connected client programs will receive a push notification message of the new state from the chassis server.

:term:`HL-API` provides functions for you to subscribe to events, which are triggered test resource state/configuration changes. Thus, your script/application can catch the push notifications and act accordingly.

**Syntax**:

.. code-block:: python

    <resource>.on_<command_oo_name>_change(<async_callback_function>)

**Example**:

.. code-block:: python
    :linenos:
    
    port.on_traffic_change(my_calllback_function)

    import asyncio
    async def my_calllback_function(port, new_value)
        ...

.. important::
    
    The ``<async_callback_function>`` must be an `coroutine function <https://docs.python.org/3/library/asyncio-task.html#id1>`_
    
Parameters that are passed to your ``<async_callback_function>`` depend on the resource it is affiliated:

  * Under the Tester level: ``<ref_tester>, <new_value>``
  * Under the Module level: ``<ref_module>, <new_value>``
  * Under the Port level: ``<ref_port>, <new_value>``

.. attention::
    
    Exception to the rule above is the event ``on_disconnected``. The parameters passed to it are ``tuple(<tester_ip: str>, <tester_port: int>)``

.. note::

    A subscription to an event only provides a tool for notifying the external code. It is unnecessary to update the library instance state manually, because it is automatically handled by the library code.

    It is allowed to subscribe multiple callback functions to one event.

.. _resource_managers_label:

Resource Managers
-----------------------

Most of the subtester resources, which are organized into collections, are handled by :term:`Resource Managers<Resource Manager>`.

The most commonly used resource managers are `Module Manager and Port Manager`_ | `Index Manager`_.

An illustration of resource managers and :term:`test resources<test resource>` are shown below:

::

    ------------------
    |     Tester     |
    ------------------
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

.. note::

    Each :term:`resource manager` is an `iterable object <https://wiki.python.org/moin/Iterator>`_


Module Manager and Port Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each tester object contains a :term:`Module Manager`, which can be accessed through attribute ``modules``.

Each module object contains a :term:`Port Manager`, which can be accessed through attribute ``ports``.

.. note::

    A :term:`Module Manager` can contain modules of different :term:`Module Types<Module Type>`. This is because there can be various test modules installed in a physical tester. On the other hand, a :term:`Port Manager` contains ports of the same :term:`Port Type`. This is because the ports on a module are of the same type.

Retrieve a single item
''''''''''''''''''''''''''''''''

Methods to retrieve a module or a port from a :term:`resource manager`:

**Syntax**:

.. code-block:: python

    obtain(<module-index> | <port-index>)

**Example**:

.. literalinclude:: /code_example/hl/obtain_one_module.py
    :linenos:
    :emphasize-lines: 9


Retrieve a multiple items
''''''''''''''''''''''''''''''''

Methods to retrieve multiple resources from a :term:`resource manager`:

**Syntax**:

.. code-block:: python

    obtain_multiple(<module-index> | <port-index>, ...)

**Example**:

.. literalinclude:: /code_example/hl/obtain_multiple_module.py
    :linenos:
    :emphasize-lines: 10


Index Manager
^^^^^^^^^^^^^^^^^^^^

:term:`Index Manager` manages the subport-level resource indices such as stream indices, filter indices, connection group indices, etc. It automatically ensures correct and conflict-free **index assignment**.

.. important::

    It is user's responsibility to create, retrieve, and remove those subport-level indices.

Thanks to the :term:`index manager` of a port, users don't necessarily need to handle the index assignment:

  * To create an index, use method ``create()``.
  * To remove an index, use method ``remove()``. An index also can be removed without accessing the manager but by calling ``<index_instance>.delete()``.

.. hint::
    
    The call of the function ``<index_instance>.delete()`` will remove a resource index from the port, and will automatically notify the index manager of the port about the removal.

The :term:`index manager` will make sure the freed index is used when the user creates again next time.

.. _session_label:

Session
-------------

A ``session`` will be created automatically after a TCP connection is established between the client and the tester.

Three attributes of a ``session`` are exposed:

    * ``is_online`` - property to validate if the TCP connection is alive.
    * ``logoff()`` - async method for gracefully closing the TCP connection to the tester.
    * ``sessions_info()`` - async method for getting information of the current active sessions on a tester.

Session Identification
^^^^^^^^^^^^^^^^^^^^^^^^^

* A tester does not use the tuple (source IP, source port, destination IP, destination port) to identify a session. Instead, it uses the username as the identification of a session. For instance, ``tester = await testers.L23Tester("192.168.1.200", "JonDoe")``, where the username is ``JonDoe``.

Session Recovery and Resource Reallocation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* To recover the session, the client only needs to establish a new TCP connection with the same username as the dropped session.
* All resources of the broken session will be automatically transferred to the new session because they have the same username.

Handling Multiple Same-Username Sessions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* If multiple sessions use the same username to connect to a tester after a broken session, the tester will give the control of the resources to a session in a first-come-first-served manner, and the others will be treated as observers. Thus, duplicated username should be avoided at the session level.
* If the controlling session is disconnected, the tester will automatically pass the control of the resources to the next session in the queue.


Local State
----------------

The access to the *local state* of a resource is done through property ``<resource>.info``. The info contains current status of the resource and information of its attributes, which cannot be changed during a running ``session``.


Code Examples
-------------------

The boilerplate code that is used to run the examples in this section:

.. literalinclude:: /code_example/boilerplate.py
    :linenos:

Tester Instance
^^^^^^^^^^^^^^^^^^^^

Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

**Creating a tester instance from one of the available tester types**

Available tester types are  ``L23Tester | L47Tester | L47VeTester``.

.. literalinclude:: /code_example/hl/create_a_tester_from_type.py
    :linenos:


**Create a tester instance by using context manager**

.. literalinclude:: /code_example/hl/create_a_tester_context.py
    :linenos:


**Create multiple tester instances**

.. literalinclude:: /code_example/hl/create_multi_testers.py
    :linenos:


.. seealso::
    
    `Learn more about await asyncio.gather <https://docs.python.org/3/library/asyncio-task.html#asyncio.gather>`_.


Obtain Resources
^^^^^^^^^^^^^^^^^^^^

**Obtain one module**

.. literalinclude:: /code_example/hl/obtain_one_module.py
    :linenos:


**Obtain multiple modules**

.. literalinclude:: /code_example/hl/obtain_multiple_module.py
    :linenos:


**Process operation on all modules**

.. literalinclude:: /code_example/hl/oper_on_all_modules.py
    :linenos:

**Obtain multiple ports**

The interface of obtaining multiple ports is equivalent to obtaining multiple modules with the following exceptions:

* all ports are of the same type
* all ports are aligned from index 0 to ``max_port_count-1``

.. literalinclude:: /code_example/hl/obtain_multiple_ports.py
    :linenos:


Data Exchange
^^^^^^^^^^^^^^^^^^^^

**Querying parameters**

.. note::

    Resource reservation is not required to query information from the tester.

.. literalinclude:: /code_example/hl/query_parameters.py
    :linenos:

**Setting parameters**

.. note::
    
    Reservation is required to set parameter to: ``Tester | Module | Port``.

.. literalinclude:: /code_example/hl/setting_parameters.py
    :linenos:


Statistics Collection
^^^^^^^^^^^^^^^^^^^^^^^^^

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

.. literalinclude:: /code_example/hl/stats_collection.py
    :linenos:


HL-API vs. CLI
-------------------------------

If you are already very familiar with :term:`CLI`, the comparison below will help you understand the differences between a :term:`XOA HL-API<HL-API>` script and a CLI script. Both scripts do the same thing and generate the same port/stream configuration.

Both scripts are using the configuration text file below:

.. literalinclude:: /code_example/hl_vs_cli/config.txt
    :caption: config.txt
    :linenos:


.. tab:: CLI

    .. literalinclude:: /code_example/hl_vs_cli/cli_script.py
        :caption: cli_script.py
        :linenos:

.. tab:: HL-API

    .. literalinclude:: /code_example/hl_vs_cli/xoa_script.py
        :caption: xoa_script.py
        :linenos:

