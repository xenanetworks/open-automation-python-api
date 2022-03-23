Test Resource Structure and Management Rules
====================================================

Rules for Test Resource Management
-----------------------------------------

1. To do ``set`` on a test resource, i.e. ``Tester``, ``Module``, or ``Port``, you must reserve the resource under your username.
2. To do ``get`` on a test resource or configuration, you don't need to reserve.
3. To reserve a tester, you must make sure all the modules and ports are either released or under your ownership.
4. To reserve a module, you must make sure all the ports are either released or under your ownership.


Valkyrie (L23) Tester (Physical)
----------------------------------

Valkyrie Tester (physical) has the following hierarchical structure.

Valkyrie Tester, Valkyrie Module, and Valkyrie Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Valkyrie Port is virtual resources that can be created, deleted, and configured as needed.

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


Vulcan (L47) Tester (Physical and Virtual)
---------------------------------------------

Vulcan Tester (physical) has the following hierarchical structure.

Vulcan Tester, Vulcan Module, and Vulcan Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Vulcan Port is virtual resources that can be created, deleted, and configured as needed.


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


::

    ----------------------
    |  Vulcan VE Tester  |
    ----------------------
        |
        |   ----------------------
        |---|  Vulcan VE Module  |
        |   ----------------------
        |        |
        |        |    -------------------- 
        |        |----|  Vulcan VE Port  | 
        |        |    -------------------- 
        |        |        |
        |        |        |    ************************ 
        |        |        |----|  Port Statistics     | 
        |        |        |    ************************ 
        |        |        |    ************************ 
        |        |        |----|  Connection Group    | 
        |        |        |    ************************
        |        |        |    



Chimera (Network Impairment) Emulator (Physical)
---------------------------------------------------

Chimera Emulator (physical) has the following hierarchical structure.

Chimera Emulator, Chimera Module, and Chimera Port are physical resources that correspond to the physical configuration. They cannot be created or deleted.

Everything below Chimera Port is virtual resources that can be created, deleted, and configured as needed.

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

