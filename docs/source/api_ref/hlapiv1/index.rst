High-Level API (V1)
========================

HL-API uses the classes defined in LL-API and lets you quickly develop scripts or program in an **object-oriented** fashion with explicit definition of commands of different *tester*, *module*, *port* types. In addition, the HL-API layer provides functionalities such as:

* :ref:`Auto connection keep-alive <session_label>`
* :ref:`Auto index management <resource_managers_label>`
* :ref:`Resources identification tracking for push notification <event_subscription_label>`

.. important::

    To continuously improve the usability of XOA Python API, the HL-API will be restructured, especially for the Layer-1 configuration APIs, in the next major release.
    
    For backward-compatibility, the current HL-API is marked as V1. The restructured will be called V2.

    You don't need to do change to your import path or code if you continue to use HL-API V1. Both versions will keep being maintained and supported.

    The restructuring won't affect the LL-API.

The HL-API (V1) are categorized into six groups:

* Testers
* Modules
* Ports
* Enums
* Exceptions
* Utils

.. toctree::

    api_map
    testers
    modules
    ports
    indices
    enums
    exceptions
