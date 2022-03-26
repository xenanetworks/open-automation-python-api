.. _xoa_python_api:

Xena OpenAutomation Python API
================================

Installation
----------------------

Install Using pip
^^^^^^^^^^^^^^^^^^^^^^^^

Make sure Python ``pip`` is installed on you system. If you are using virtualenv, then pip is already installed into environments created by virtualenv, and using sudo is not needed. If you do not have pip installed, download this file: https://bootstrap.pypa.io/get-pip.py and run ``python get-pip.py``.

To install the latest, use pip to install from pypi:

.. code-block:: shell
    
    ~/> pip install xoa-driver


To upgrade to the latest, use pip to upgrade from pypi:

.. code-block:: shell
    
    ~/> pip install xoa-driver --upgrade


Install From Source
^^^^^^^^^^^^^^^^^^^^^^^^

Make sure packages ``wheel``, ``setuptools`` are installed  on your system.

Install ``wheel`` and ``setuptools`` using pip:

.. code-block:: shell
    
    ~/> pip install wheel setuptools


Download the source distribution first. Unzip the zip archive and run the ``setup.py`` script to install the package:

.. code-block:: shell
    
    /xoa_driver> python setup.py install


Then you can build ``.whl`` file for distribution:

.. code-block:: shell
    
    /xoa_driver> python setup.py bdist_wheel



API Structure
----------------

XOA Python API consists of two layers on top of the tester proprietary binary commands, as shown in the diagram below.

The XOA High-Level API (HL-PYTHON) provides abstraction that helps developers to quickly develop scripts or program in an object-oriented fashion with explicit definition of commands of different *tester*, *module*, *port* types. In addition, the HL-PYTHON layer provides functionalities such as *auto connection keep-alive*, *auto index management*, *resources identification tracking for push notification*, etc. 

For example, to change the description of a tester, the HL-PYTHON is:

.. code-block:: python

    await tester.comment.set(comment="my tester")


The XOA Low-Level API (LL-PYTHON) contains the class definition of each command, and gives developers a direct control of the tester. However, the LL-PYTHON does not provide functionalities such as *auto connection keep-alive* and *auto index management*.

For example, to change the description of a tester by, the LL-PYTHON is:

.. code-block:: python

    await C_COMMENT(handler).set(comment="my tester")


::

    +---------------------------------+
    |           High-Level API        |
    +---------------------------------+
    +---------------------------------+
    |           Low-Level API         |
    +---------------------------------+ 
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    +---------------------------------+
    |    Binary Xena Management       |
    |      Protocol (proprietary)     |
    +---------------------------------+
    +---------------------------------+
    |     Xena Physical / Virtual     |
    |            Testers              |
    +---------------------------------+


Test Resource Structure and Management Rules
----------------------------------------------

Rules for Test Resource Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. To do ``set`` on a test resource, i.e. ``Tester``, ``Module``, or ``Port``, you must reserve the resource under your username.
2. To do ``get`` on a test resource or configuration, you don't need to reserve.
3. To reserve a tester, you must make sure all the modules and ports are either released or under your ownership.
4. To reserve a module, you must make sure all the ports are either released or under your ownership.


Valkyrie (L23) Tester (Physical)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


Commands Grouping
---------------------

Sending commands one by one using CLI is extremely slow in terms of execution speed. This is because the program needs to wait for the response from the tester. More, using CLI it is difficult to group commands together and send them in one round.

XOA Python API provides two ways to group commands together to send to testers, which greatly increase commands execution speed. This is very useful, when the developer has many ports and many streams to configure, as well as querying the port and stream statistics as quickly as possible.

Parallel Grouping
^^^^^^^^^^^^^^^^^^^^^^^^^

``asyncio.gather`` groups commands in a parallel way. Commands are sent out in parallel (with neglectable delay between each other). This is very useful when you want to send commands to different test resources, e.g. two different ports on the same tester, or two different ports on different testers.

.. code-block:: python

    await asyncio.gather(
        command_1,
        command_2,
        command_3,
        ...
    )


Sequential Grouping
^^^^^^^^^^^^^^^^^^^^^^^^^

``utils.apply`` groups commands in a sequential way. Commands are sent out in one large batch to the tester. This is very useful when you want to send many commands to the same test resource, e.g. a port on a tester.

.. code-block:: python

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

    commands = [
        command_1,
        command_2,
        command_3,
        ...
    ]
    async for response in utils.apply_iter(*commands):
        print(response)


Sending Command One by One
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you prefer sending commands in the old fashion like using CLI, you can certainly have only one command in the grouping, for example:

.. code-block:: python

    await command_1
    await command_2
    await command_3


.. note::

    Remember to use ``await`` before the command. Commands are defined as Coroutines and must be awaited.


Read more about Python `awaitable object`_.

.. _awaitable object: https://docs.python.org/3/library/asyncio-task.html#id2

