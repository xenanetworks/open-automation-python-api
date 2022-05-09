.. _general-information-label:

General Information
==================================

API Structure
-------------------

XOA Python API consists of two layers, High-Level API (:term:`HL-API`) and Low-Level API (:term:`LL-API`), on top of the Xena proprietary binary API, as shown in the diagram below.

::
    
    +---------------------------------+
    |      High-Level Python API      |
    +---------------------------------+
    +---------------------------------+
    |      Low-Level Python API       |
    +---------------------------------+ 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    +---------------------------------+
    |    Xena Proprietary Binary API  |
    +---------------------------------+
    +---------------------------------+
    | Xena Hardware / Virtual Testers |
    +---------------------------------+


:term:`HL-API` provides abstraction that helps you quickly develop scripts or program in an object-oriented fashion with explicit definition of commands of different *tester*, *module*, *port* types. In addition, the HL-API layer provides functionalities such as *auto connection keep-alive*, *auto index management*, *resources identification tracking for push notification*, etc. 

For example, to change the description of a tester, the HL-API is:

.. code-block:: python
    :linenos:

    await tester.comment.set(comment="my tester")


:term:`LL-API` contains the class definition of each command, giving you the direct control of the tester. However, the LL-API does not provide functionalities such as *auto connection keep-alive* and *auto index management*.

For example, to change the description of a tester by, the LL-API is:

.. code-block:: python
    :linenos:

    await C_COMMENT(handler).set(comment="my tester")


Test Resource Management
----------------------------------------------

:term:`Test resource` can be the chassis itself, a test module on the chassis or a test port on a module.

This section describes:

* :term:`Test resource` hierarchy.
* :term:`Test resource` management principle.

If you are new to Xena testers, this section will help you understand the basics.

Test Resource Hierarchy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Valkyrie Tester (L23 Tester) 
''''''''''''''''''''''''''''''''''''

`Valkyrie <https://xenanetworks.com/valkyrie/>`_ is a full-featured stateless Ethernet traffic generator and analysis platform. Valkyrie tester has the following hierarchical structure.

::

    ---------------------
    |  Valkyrie Tester  |
    ---------------------
        |
        |   -----------------------
        |---|   Valkyrie Module   |
        |   -----------------------
        |        |
        |        |    ------------------- 
        |        |----|  Valkyrie Port  | 
        |        |    ------------------- 
        |        |        |
        |        |        |    ************************* 
        |        |        |----|  Port Statistics      | 
        |        |        |    ************************* 
        |        |        |    ************************* 
        |        |        |----|  Stream               | 
        |        |        |    ************************* 
        |        |        |        |
        |        |        |        |    **********************  
        |        |        |        |----|  Filter            | 
        |        |        |        |    **********************  
        |        |        |        |    **********************  
        |        |        |        |----|  Modifier          | 
        |        |        |        |    ********************** 
        |        |        |        |    **********************  
        |        |        |        |----|  Histogram         | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Length Term       | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Match Term        | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Test Payload      | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Stream Statistics | 
        |        |        |        |    **********************
        |        |        |        |    

Valkyrie Tester, Valkyrie Module, and Valkyrie Port are hardware resources that correspond to the hardware configuration. They cannot be created or deleted.

Everything below Valkyrie Port is virtual resources that can be created, deleted, and configured as needed.

Vulcan Tester (L47 Tester)
'''''''''''''''''''''''''''''''''''''''''''''

`Vulcan <https://xenanetworks.com/vulcan/>`_ generates stateful traffic over Ethernet. Vulcan Tester has the following hierarchical structure.

::

    ------------------
    |  Vulcan Tester |
    ------------------
        |
        |   -------------------
        |---|  Vulcan Module  |
        |   -------------------
        |        |
        |        |    ------------------ 
        |        |----|  Vulcan Port   | 
        |        |    ------------------ 
        |        |        |
        |        |        |    ************************ 
        |        |        |----|  Port Statistics     | 
        |        |        |    ************************
        |        |        |    ************************ 
        |        |        |----|  Connection Group    | 
        |        |        |    ************************
        |        |        |    

Vulcan Tester, Vulcan Module, and Vulcan Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Vulcan Port is virtual resources that can be created, deleted, and configured as needed.

VulcanVE Tester (L47VE Tester)
'''''''''''''''''''''''''''''''''''''''''''''

VulcanVE is the virtual edition of Vulcan. VulcanVE Tester has the following hierarchical structure, the same as Vulcan Tester.

::

    ----------------------
    |   VulcanVE Tester  |
    ----------------------
        |
        |   ----------------------
        |---|   VulcanVE Module  |
        |   ----------------------
        |        |
        |        |    -------------------- 
        |        |----|   VulcanVE Port  | 
        |        |    -------------------- 
        |        |        |
        |        |        |    ************************ 
        |        |        |----|  Port Statistics     | 
        |        |        |    ************************ 
        |        |        |    ************************ 
        |        |        |----|  Connection Group    | 
        |        |        |    ************************
        |        |        |    

Although VulcanVE Tester, VulcanVE Module, and VulcanVE Port are virtual resources, they cannot be created or deleted.

Everything below VulcanVE Port is virtual resources that can be created, deleted, and configured as needed.

Chimera Network Impairment Emulator (Impairment)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

`Chimera <https://xenanetworks.com/chimera/>`_ is a network impairment emulator that makes it easy to introduce consistent, accurate, well-defined and repeatable impairments (e.g. packet manipulation, packet drop, latency and jitter) to traffic between :term:`DUT` in the lab. 

Chimera Emulator has the following hierarchical structure.

::

    ------------------------
    |  Chimera Emulator    |
    ------------------------
        |
        |   ----------------------
        |---|  Chimera Module    |
        |   ----------------------
        |        |
        |        |    ----------------------
        |        |----|  Chimera Port      | 
        |        |    ----------------------
        |        |        |
        |        |        |    ************************* 
        |        |        |----|  Port Statistics      | 
        |        |        |    ************************* 
        |        |        |    *************************
        |        |        |----|  Flow                 | 
        |        |        |    *************************
        |        |        |        |
        |        |        |        |    ****************************
        |        |        |        |----|  Filter                  | 
        |        |        |        |    ****************************
        |        |        |        |    ****************************
        |        |        |        |----|  Impairment Config       | 
        |        |        |        |    ****************************
        |        |        |        |    ****************************
        |        |        |        |----|  Impairment Distribution | 
        |        |        |        |    ****************************
        |        |        |        |    ****************************
        |        |        |        |----|  Flow Statistics         | 
        |        |        |        |    ****************************
        |        |        |        |    

Chimera Emulator, Chimera Module, and Chimera Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Chimera Port is virtual resources that can be created, deleted, and configured as needed.

.. important::

    Chimera can be seamlessly integrated with Valkyrie by installing Chimera modules in a Valkyrie chassis.  

    ::

        ---------------------
        |  Valkyrie Tester  |
        ---------------------
            |
            |   -----------------------
            |---|   Valkyrie Module   |
            |   -----------------------
            |
            |   ----------------------
            |---|  Chimera Module    |
            |   ----------------------



Management Principle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Xena testers support multiple simultaneous connections from any mixture of Xena clients, such as the `ValkyrieManager <https://xenanetworks.com/product/valkyriemanager/>`_, scripting clients, etc. As soon as a client has successfully established a connection to the chassis, any :term:`test resource` can be inspected. But in order to change the :term:`test resource` configuration, the resource must first be reserved by the client.

To management test resources, i.e., read, write, create, delete, you must follow the principles below:

1. To do ``set`` (create/update/delete) on a :term:`test resource`, i.e. *tester*, *module*, or *port*, you must reserve the resource under your username.
2. To do ``get`` (read) on a :term:`test resource`, you don't need to reserve.
3. To reserve a tester, you must make sure **all the modules and ports are either released or under your ownership**.
4. To reserve a module, you must make sure **all the ports are either released or under your ownership**.

.. important::

    Starting traffic using ``C_TRAFFIC`` of ``C_TRAFFICSYNC`` does **NOT** require chassis reservation but port reservation, although their command prefix is ``C_`` and categorized as chassis-level commands.


Command Grouping
--------------------------------------------------------------

Using :term:`CLI` to configure ports and streams is slow because a CLI script must wait for a chassis response to before sending the next command. Such a one-by-one fashion results in *N round trip time* (*N-RTT*), where *N* is the number of commands to send.

Because of the abovementioned N-RTT problem, it is difficult for a CLI script to collect traffic statistics of different ports at the same time (using for loops in the script is far from solving the problem). As a result, this will cause a wrong understanding of the test results.

XOA Python API solves this problem by *Command Grouping*, i.e. grouping commands together and sending them to the chassis in one batch.

XOA Python API provides two different ways of grouping commands, *Parallel Grouping* and *Sequential Grouping*, for different needs.

Parallel Grouping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``asyncio.gather`` groups commands in a parallel way. Commands are sent out in parallel (with neglectable delay between each other). This is very useful when you want to send commands to different test resources, e.g. two different ports on the same tester, or two different ports on different testers.

.. code-block:: python
    :linenos:

    await asyncio.gather(
        command_1,
        command_2,
        command_3,
        ...
    )


Sequential Grouping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``utils.apply`` groups commands in a sequential way. Commands are sent out in one large batch to the tester. This is very useful when you want to send many commands to the same :term:`test resource`, e.g. a port on a tester.

.. code-block:: python
    :linenos:

    commands = [
        command_1,
        command_2,
        command_3,
        ...
    ]
    async for response in utils.apply(*commands):
        print(response)

However, abusing this function can cause memory issue on your computer. This is because the computer needs to store all the grouped commands in the memory until the responses from the testers arrive. To avoid potential grouping abuse, a limit of **200** is place to the maximum number of  commands that you can group sequentially.


``utils.apply_iter`` does exactly the same thing as ``utils.apply`` except it does not aggregate responses but return them one by one as soon as they are ready. This allows sending large batches commands without causing memory issue.

.. code-block:: python
    :linenos:

    commands = [
        command_1,
        command_2,
        command_3,
        ...
    ]
    async for response in utils.apply_iter(*commands):
        print(response)


One-by-One
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you prefer sending commands one by one in the same way as using CLI, you can simply place only one command in the group, for example:

.. code-block:: python
    :linenos:

    await command_1
    await command_2
    await command_3


.. note::

    Remember to use ``await`` before the command. Commands are defined as Coroutines and must be awaited.

.. seealso::
    
    Read more about Python `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_.

