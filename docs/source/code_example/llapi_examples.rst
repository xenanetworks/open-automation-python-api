Low-Level API
===================================

The boilerplate code that is used to run all of the examples.

.. literalinclude:: boilerplate.py


Connect to Tester
--------------------------------

Each tester class is represented as an `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_. When awaited, it establishes a TCP connection to the tester.

A tester instance also can be created without awaiting the connection establishment for more flexible manipulation of instances in user code.

.. literalinclude:: ll/create_conn_to_tester.py
    :caption: Create connection to a tester
    

.. literalinclude:: ll/create_multiple_conns.py
    :caption: Create multiple connections to testers
    


Access Modules
--------------------------------

The examples below help you gain access to the test modules on a tester.

.. literalinclude:: ll/obtain_one_module.py
    :caption: Access a single module on a tester
    

.. literalinclude:: ll/obtain_multiple_modules.py
    :caption: Access multiple modules on a tester
    


Querying & Setting
--------------------------------

Querying
^^^^^^^^^^^

.. note::

    Resource reservation is not required to query information from the tester.

.. literalinclude:: ll/query_parameters.py
    :caption: Query port
    

Setting
^^^^^^^^^^^^^

.. note::
    
    Reservation is required to do ``set`` to: `Testers`, `Modules`, and `Ports`. 

.. literalinclude:: ll/setting_parameters.py
    :caption: Configure port


Statistics Collection
--------------------------------

Statistics collection, such as latency and jitter, TX/RX rate, frame count, etc., can be done by Python standard library ``asyncio``. In case you are new to ``asyncio``, the example below may help you understand how to use ``asyncio`` to query counters.

.. literalinclude:: ll/stats_collection.py
    :caption: Collect statistics
    


