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

The most commonly used resource managers are `Module Manager and Port Manager`_ | `Index Managers`_.

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
        |        |    --------------   ******************
        |        |----|  Port 0    | - | index managers |
        |        |    --------------   ******************
        |        |    --------------   ******************
        |        |----|  Port 1    | - | index managers |
        |        |    --------------   ******************
        |        |    --------------   ******************
        |        |----|  Port N-1  | - | index managers |
        |             --------------   ******************
        |
        |   --------------
        |---|  Module 1  |
        |   --------------
        |        |
        |    *******************
        |    |   port manager  |
        |    *******************
        |        |
        |        |    --------------   ******************
        |        |----|  Port 0    | - | index managers |
        |        |    --------------   ******************
        |        |    --------------   ******************
        |        |----|  Port 1    | - | index managers |
        |        |    --------------   ******************
        |        |    --------------   ******************
        |        |----|  Port N-1  | - | index managers |
        |             --------------   ******************
        |
        |   --------------
        |---| Module N-1 |
            --------------

.. note::

    Each :term:`resource manager` is an `iterable object <https://wiki.python.org/moin/Iterator>`_


Module Manager and Port Manager
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each tester object contains a :term:`Module Manager`, which can be accessed through attribute ``modules``, e.g. ``my_tester.modules``.
Each module object contains a :term:`Port Manager`, which can be accessed through attribute ``ports``, e.g. ``my_module.ports``.

.. important::

    Modules and ports are test resources that cannot be created or deleted, unless the tester is reconfigured either physically or virtually. Thus, in XOA Python API, there is no "create" or "delete" methods for these two types of objects. What we can do is to `obtain` the object that represents the underlying test resource. 

    A :term:`Module Manager` can contain modules of different :term:`Module Types<Module Type>`. This is because there can be various test modules installed in a physical tester. On the other hand, a :term:`Port Manager` contains ports of the same :term:`Port Type`. This is because the ports on a module are of the same type.

Obtain a single object
''''''''''''''''''''''''''''''''

Methods to retrieve a module or a port from a :term:`resource manager`:

**Syntax**:

.. code-block:: python

    obtain(<module-index> | <port-index>)

**Example**:

.. literalinclude:: /code_example/hl/obtain_one_module.py
    :linenos:
    :emphasize-lines: 9


Obtain multiple objects
''''''''''''''''''''''''''''''''

Methods to retrieve multiple resources from a :term:`resource manager`:

**Syntax**:

.. code-block:: python

    obtain_multiple(<module-index> | <port-index>, ...)

**Example**:

.. literalinclude:: /code_example/hl/obtain_multiple_module.py
    :linenos:
    :emphasize-lines: 10


Index Managers
^^^^^^^^^^^^^^^^^^^^

Each port object contains several :term:`Index Managers<Index Manager>` that manage the subport-level resource indices such as stream indices, filter indices, connection group indices, modifier indices, etc. It automatically ensures correct and conflict-free **index assignment**.
    
    For L23:
    * `Stream Index Manager` can be accessed through attribute ``streams``, e.g. ``my_l23_port.streams``.
    * `Filter Index Manager` can be accessed through attribute ``filters``, e.g. ``my_l23_port.filters``.
    * `Match Term Index Manager` can be accessed through attribute ``match_terms``, e.g. ``my_l23_port.match_terms``.
    * `Length Term Index Manager` can be accessed through attribute ``length_terms``, e.g. ``my_l23_port.length_terms``.
    * `Histogram Dataset Index Manager` can be accessed through attribute ``datasets``, e.g. ``my_l23_port.datasets``.
    * `Modifier Index Manager` can be accessed through attribute ``modifiers`` under ``packet.header`` of a stream object, e.g. ``my_stream.packet.header.modifiers``

    For L47:
    * `Connection Group Index Manager` can be accessed through attribute ``streams``, e.g. ``my_l47_port.connection_groups``.

.. important::

    Streams, connection groups, filters, modifiers, etc. are virtual. They can be created and deleted. Thus in XOA Python API, there are `create`, `delete`, and `remove` methods for you to manage these virtual resources.

    It is user's responsibility to create, retrieve, and delete those subport-level indices. Index Managers only takes care of the index assignment.

When you create an index instance under a port, e.g. a stream, the Stream Index Manager will pick an available value and assign it to the stream as the stream index. When you delete an index instance, the index manager will mark that index value as available. When you create an index instance again, the index manager will take the freed values first instead of creating a new one. This makes sure when the index manager cannot create more index instances is only because of the port capability, not because of the wasted index values.  

Thanks to the index assignment mechanism, you don't necessarily need to handle the index assignment but concentrating on the test logic. Methods to manage subport-level instances:

  * To create an index, use the method ``<index_manager>.create()`` under the index manager, e.g. ``my_stream = await my_port.streams.create()``.
  * To delete an index, you can use the method ``<index_manager>.remove(<index>)`` under the index manager, e.g. ``await my_port.streams.remove(0)``. However, the method ``remove`` expects the index value of the instance.
  * An easier way to delete an index is using method ``<index_instance>.delete()`` directly on the index instance, e.g. ``await my_stream.delete()``. The call of the function ``<index_instance>.delete()`` will delete the index from the port, and will automatically notify the index manager about the deletion.

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

Connect to Testers
^^^^^^^^^^^^^^^^^^^^

Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

**Creating a tester instance from one of the available tester types**

Available tester types are  ``L23Tester | L47Tester | L47VeTester``.

.. literalinclude:: /code_example/hl/create_a_tester_from_type.py
    :linenos:
    :emphasize-lines: 5


**Create a tester instance by using context manager**

.. literalinclude:: /code_example/hl/create_a_tester_context.py
    :linenos:
    :emphasize-lines: 5


**Create multiple tester instances**

.. literalinclude:: /code_example/hl/create_multi_testers.py
    :linenos:
    :emphasize-lines: 21


.. seealso::
    
    `Learn more about await asyncio.gather <https://docs.python.org/3/library/asyncio-task.html#asyncio.gather>`_.


Access Modules and Ports
^^^^^^^^^^^^^^^^^^^^^^^^^

**Access a single module**

.. literalinclude:: /code_example/hl/obtain_one_module.py
    :linenos:
    :emphasize-lines: 10


**Access multiple modules**

.. literalinclude:: /code_example/hl/obtain_multiple_module.py
    :linenos:
    :emphasize-lines: 11


**Access all modules**

.. literalinclude:: /code_example/hl/oper_on_all_modules.py
    :linenos:
    :emphasize-lines: 11
    

**Access a single port**

.. literalinclude:: /code_example/hl/obtain_one_port.py
    :linenos:
    :emphasize-lines: 17


**Access multiple ports**

The interface of obtaining multiple ports is equivalent to obtaining multiple modules with the following exceptions:

* all ports are of the same type
* all ports are aligned from index 0 to ``max_port_count-1``

.. literalinclude:: /code_example/hl/obtain_multiple_ports.py
    :linenos:
    :emphasize-lines: 13

**Access all ports**

.. literalinclude:: /code_example/hl/oper_on_all_portsy.py
    :linenos:
    :emphasize-lines: 13


Querying and Setting Parameters 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Querying parameters**

.. note::

    Resource reservation is not required to query information from the tester.

.. literalinclude:: /code_example/hl/query_parameters.py
    :linenos:
    :emphasize-lines: 14, 19, 20

**Setting parameters**

.. note::
    
    Reservation is required to set parameter to: ``Tester | Module | Port``.

.. literalinclude:: /code_example/hl/setting_parameters.py
    :linenos:
    :emphasize-lines: 26, 27, 31, 32


Create/Delete Streams
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    
    Reservation is required to create streams on ``Port``.

.. literalinclude:: /code_example/hl/streams.py
    :linenos:
    :emphasize-lines: 30, 31, 44



Create/Delete Modifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. note::
    
    Port reservation is required to create modifiers on streams.

.. note::
    
    The mechanism of creating and deleting modifiers is different from streams. In order to change the modifiers on a stream packet header, you need to re-configure all the modifiers again. An abstraction will be added to the HL Python API to provide users with the same API syntax, i.e. ``create()``. ``delete()``, and ``remove()`` in a future release of XOA Python API.

.. note::
    
    An easy way to configure the packet header content will be added to the HL Python API in a future release.


.. literalinclude:: /code_example/hl/modifiers.py
    :linenos:
    :emphasize-lines: 51, 52, 58, 59, 61, 65, 70, 71, 73, 78, 79



Start/Stop Traffic and Collect Statistics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

.. literalinclude:: /code_example/hl/stats_collection.py
    :linenos:
    :emphasize-lines: 10, 56, 62, 52


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

