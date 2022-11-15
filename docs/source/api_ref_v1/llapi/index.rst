Low-Level API Reference
=========================

LL-API contains low-level API classes, giving you the direct control of the tester. The names of the classes are the same as the the CLI commands in :term:`XOA CLI`, making it easy for you to understand the Python API if you are already familiar with XOA CLI.

However, unlike HL-API, LL-API does not provide functionalities such as *auto connection keep-alive* and *auto index management*. This means you need to write more codes to handle those yourself.

The low-level Python APIs are categorized into six groups:

* L23 (Valkyrie)
* L47 (Vulcan)
* Impairment (Chimera)
* Enums
* Exceptions
* Utilities


.. toctree::

    l23/index
    l47/index
    impairment/index
    enums
    utils
