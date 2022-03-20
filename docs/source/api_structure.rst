API Structure
==============

XOA Python API consists of two layers on top of the tester proprietary binary commands, as shown in the diagram below.

The high-level API provides abstraction that helps developers to quickly develop scripts or program in an object-oriented fashion with explicit definition of commands of different *tester*, *module*, *port* types. In addition, the high-level API layer provides functionalities such as *auto connection keep-alive*, *auto index management*, *resources identification tracking for push notification*, etc. 

For example, to change the description of a tester, the high-level API is:

.. code-block:: python

    await tester.comment.set(comment="my tester")


The low-level API contains the class definition of each command, and gives developers a direct control of the tester. However, the low-level API does not provide functionalities such as *auto connection keep-alive* and *auto index management*.

For example, to change the description of a tester by, the low-level API is:

.. code-block:: python

    await C_COMMENT(handler).set(comment="my tester")


::

    +---------------------------------+
    |           High-level API        |
    +---------------------------------+
    +---------------------------------+
    |           Low-level API         |
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

