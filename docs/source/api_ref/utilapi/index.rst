Utility API Reference
=========================

UTIL provides high-level abstraction functions on top of the object-oriented APIs in HL-API, aiming to help you simplify code logics and increase readability and maintainability. UTIL consists of sub-libraries where functions are grouped based on functionalities, such as :term:`ANLT<ANLT>`. Complex operation sequences are wrapped inside high-level functions, e.g. initiating link training, reserving ports, etc.

UTIL can be used in two different ways:

* Library Mode: you can import the Python library into your test scripts and use the functions.

* Interactive Mode: an interactive shell for you to execute functions in a command-line fashion. This is very helpful when you need a command-line interface for interactive testing. 


.. toctree::

    anlt_util
    anlt_cli