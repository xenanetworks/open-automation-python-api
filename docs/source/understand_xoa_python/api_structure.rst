API Structure
==================================

XOA Python API consists of three layers on top of the Xena proprietary binary API, as shown below.

    :term:`High-level Functions (HL-FUNC)<HL-FUNC>` provides high-level abstraction functions

    :term:`High-Level API (HL-API)<HL-API>` provides object-oriented APIs.

    :term:`Low-Level API (LL-API)<LL-API>` provides low-level class.

.. figure:: ../_static/api_structure.png
    :scale: 100 %
    :align: center

    XOA Python API Stack View

Descriptions of each layer (from bottom to top) are shown below.

.. rubric:: Low-Level API

LL-API is the bottom layer containing **low-level command classes** that convert human-readable parameters to and from binary data to communicate testers. The names of the low-level command classes are the same as the the CLI commands in :term:`XOA CLI`. This makes it easy for you to understand and use LL-API if you are already familiar with XOA CLI.

.. seealso::

    Read more about :doc:`llapi_guide`.


.. rubric:: High-Level API

On top of LL-API's command clases, HL-API provides **object-oriented** APIs and lets you quickly develop scripts or programs in an **object-oriented** fashion with explicit definition of commands of different *tester*, *module*, *port* types.

In addition, the HL-API layer provides functionalities such as:

    * :ref:`Auto connection keep-alive <session_label>`
    * :ref:`Auto index management <resource_managers_label>`
    * :ref:`Resources identification tracking for push notification <event_subscription_label>`

.. seealso::

    Read more about :doc:`hlapi_guide`.


.. rubric:: High-Level Functions

HL-FUNC provides **high-level abstraction** functions on top of the object-oriented APIs in HL-API, aiming to help you simplify code logics and increase readability and maintainability. HL-FUNC consists of sub-libraries where functions are grouped based on functionalities, such as :term:`ANLT<ANLT>`. Complex operation sequences are wrapped inside high-level functions, e.g. initiating link training, reserving ports, etc.

.. seealso::

    Read more about :doc:`hlfunc_guide`.