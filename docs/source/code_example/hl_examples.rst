High-Level API Examples
===================================

The boilerplate code that is used to run the examples in this section:

.. literalinclude:: boilerplate.py
    

Connect to Tester
--------------------------------

To connect to a tester, create a tester object and the driver will automatically handle the connection. Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.


Available tester types are :ref:`L23Tester <l23tester>`, :ref:`L23VeTester <l23vetester>`, :ref:`L47Tester <l47tester>`, :ref:`L47VeTester <l47vetester>`.

.. literalinclude:: hl/create_tester_from_type.py
    :caption: Create tester instance

You can also create a tester instance using Python Context Manager

.. seealso::

    Read more about Python Context Manager: https://docs.python.org/3/library/contextlib.html


.. literalinclude:: hl/create_tester_context.py
    :caption: Create tester instance using Python Context Manager

To create multiple tester instances, you can do:

.. literalinclude:: hl/create_multi_testers.py
    :caption: Create multiple tester instances


.. seealso::
    
    `Learn more about await asyncio.gather <https://docs.python.org/3/library/asyncio-task.html#asyncio.gather>`_.


Access Modules
--------------------------------

The examples below help you gain access to the test modules on a tester.


.. literalinclude:: hl/obtain_one_module.py
    :caption: Access a single module on a tester


.. literalinclude:: hl/obtain_multiple_modules.py
    :caption: Access multiple modules on a tester


.. literalinclude:: hl/obtain_all_modules.py
    :caption: Access all modules on a tester
    

Access Ports
--------------------------------

The examples below help you gain access to the test ports on a tester.


.. literalinclude:: hl/obtain_one_port.py
    :caption: Access a single port on a module


The interface of obtaining multiple ports is equivalent to obtaining multiple modules with the following exceptions:

* all ports are of the same type
* all ports are aligned from index ``0`` to ``max_port_count-1``

.. literalinclude:: hl/obtain_multiple_ports.py
    :caption: Access multiple ports on a module


.. literalinclude:: hl/obtain_all_ports.py
    :caption: Access all ports on a module


Querying & Setting
--------------------------------

Querying
^^^^^^^^^^^

.. note::

    Resource reservation is not required to query information from the tester.

.. literalinclude:: hl/query_parameters.py
    :caption: Query module and port


Setting
^^^^^^^^^^^^^

.. note::
    
    Reservation is required to do ``set`` to: :ref:`Tester <tester>`, :ref:`Module <module>`, :ref:`Port <port>`, 

.. literalinclude:: hl/setting_parameters.py
    :caption: Configure module and port


Create/Delete Streams (L23)
--------------------------------

To generate L23 stateless traffic, stream configuration is necessary. The example below shows how to create/delete streams on a L23 port.

.. note::
    
    Reservation is required to do :terms: `CRUD`` operations streams on :ref:`Port <port>`.

.. literalinclude:: hl/streams.py
    :caption: Create and delete streams on a port


Create/Delete Modifiers
--------------------------------

To simulate traffic from many address, or when you want certain fields of a packet to change dynamically on a per packet basis, you can use modifiers. A modifier changes the field value per packet based on how you configure it. The example below shows how to create/delete modifiers on a stream.

.. note::
    
    Port reservation is required to create modifiers on streams.

.. note::
    
    The mechanism of creating and deleting modifiers is different from streams. In order to change the modifiers on a stream packet header, you need to re-configure all the modifiers again. An abstraction will be added to the HL Python API to provide users with the same API syntax, i.e. ``create()``. ``delete()``, and ``remove()`` in a future release of XOA Python API.

.. note::
    
    An easy way to configure the packet header content will be added to the HL Python API in a future release.


.. literalinclude:: hl/modifiers.py
    :caption: Create and delete modifiers on a stream



Start/Stop Traffic and Statistics
------------------------------------------

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., should be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

To show how to query statistics on-the-fly, the function ``my_awesome_func`` is slightly modified.

.. literalinclude:: hl/traffic_stats.py
    :caption: Traffic and statistics


Traffic Drop and Latency/Jitter Impairment
--------------------------------------------

.. note::

    Only applicable to a Chimera module. This is not meant to generate any traffic.


.. literalinclude:: hl/traffic_impairment.py
    :caption: Traffic drop and latency/jitter impairment
    

Read/Write Transceiver
--------------------------------------------

The example demonstrates how to read/write transceiver register of different types in different ways, as well as reading transceiver temperature.

.. literalinclude:: hl/transceiver_reg.py
    :caption: Read/write transceiver values