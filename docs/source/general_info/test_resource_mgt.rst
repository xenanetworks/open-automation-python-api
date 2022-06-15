Test Resource Management
=================================

:term:`Test resource` can be the chassis itself, a test module on the chassis or a test port on a module.

This section describes:

* :term:`Test resource` hierarchy.
* :term:`Test resource` management principle.

If you are new to Xena testers, this section will help you understand the basics.

Test Resource Hierarchy
------------------------------------

Valkyrie Tester (L23 Tester) 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
-----------------------------------

Xena testers support multiple simultaneous connections from any mixture of Xena clients, such as the `ValkyrieManager <https://xenanetworks.com/product/valkyriemanager/>`_, scripting clients, etc. As soon as a client has successfully established a connection to the chassis, any :term:`test resource` can be inspected. But in order to change the :term:`test resource` configuration, the resource must first be reserved by the client.

To management :term:`test resources<test resource>`, i.e., read, write, create, delete, you must follow the principles below:

1. To do ``set`` (create/update/delete) on a :term:`test resource`, i.e. *tester*, *module*, or *port*, you must reserve the resource under your username.
2. To do ``get`` (read) on a :term:`test resource`, you don't need to reserve.
3. To reserve a tester, you must make sure **all the modules and ports are either released or under your ownership**.
4. To reserve a module, you must make sure **all the ports are either released or under your ownership**.

.. important::

    Starting traffic using ``C_TRAFFIC`` of ``C_TRAFFICSYNC`` does **NOT** require chassis reservation but port reservation, although their command prefix is ``C_`` and categorized as chassis-level commands.
