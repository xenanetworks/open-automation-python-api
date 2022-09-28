API Structure
==================================

XOA Python API consists of two layers, :term:`High-Level API (HL-API)<HL-API>` and :term:`Low-Level API (LL-API)<LL-API>`, on top of the Xena proprietary binary API, as shown in the diagram below.

:term:`LL-API` contains low-level API classes. The names of the classes match the command names in :term:`XOA CLI`, making it easy for developers to find the APIs you need for your test script.

.. seealso::

    Read more about LL-API in :ref:`Low-Level API <low_level_api_label>`

:term:`HL-API` uses the classes defined in LL-API and provides abstraction that helps developers to quickly develop scripts or program in an object-oriented fashion with explicit definition of commands of different *tester*, *module*, *port* types.

.. seealso::

    Read more about HL-API in :ref:`High-Level API <high_level_api_label>`

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


:term:`HL-API` provides abstraction that helps you quickly develop scripts or program in an object-oriented fashion with explicit definition of commands of different *tester*, *module*, *port* types. In addition, the HL-API layer provides functionalities such as:

    * :ref:`Auto connection keep-alive <session_label>`
    * :ref:`Auto index management <resource_managers_label>`
    * :ref:`Resources identification tracking for push notification <event_subscription_label>`

For example, to change the description of a tester using :term:`HL-API`:

.. code-block:: python
    
    await tester.comment.set(comment="my tester")


:term:`LL-API` contains the class definition of each command, giving you the direct control of the tester. However, the :term:`LL-API` does not provide functionalities such as *auto connection keep-alive* and *auto index management*.

For example, to change the description of a tester using :term:`LL-API`:

.. code-block:: python
    
    await C_COMMENT(handler).set(comment="my tester")

