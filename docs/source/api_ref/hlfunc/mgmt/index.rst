Resource Management
===================

.. versionadded:: 1.1
    
.. warning:: 

    The high-level functions are still in beta mode. Functions are subject to changes in terms of naming and parameters.

The following high-level functions handle test resource management, e.g. connection, port reservation, and port reset.

-------

.. currentmodule:: xoa_driver.hlfuncs.mgmt

HL Port Functions
-------------------------

.. autofunction:: get_ports

.. autofunction:: reserve_port

.. autofunction:: reset_port

.. autofunction:: free_port


HL Module Functions
---------------------------

.. autofunction:: free_ports

.. autofunction:: reserve_module

.. autofunction:: free_module


HL Tester Functions
---------------------------

.. autofunction:: reserve_tester

.. autofunction:: free_tester