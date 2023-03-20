Resource Management
===================

The following high-level functions handle test resource management, e.g. connection, port reservation, and port reset.

-------

.. currentmodule:: xoa_driver.hlfuncs.mgmt

HL Port Functions
-------------------------

.. autofunction:: reserve_port

.. autofunction:: reset_port

.. autofunction:: free_port

.. autofunction:: get_port

.. autofunction:: free_ports


HL Module Functions
---------------------------

.. autofunction:: reserve_module

.. autofunction:: free_module

.. autofunction:: get_module

.. autofunction:: get_module_supported_media

.. autofunction:: set_module_media_config

.. autofunction:: set_module_port_config

.. autofunction:: get_module_eol_date

.. autofunction:: get_module_eol_days

.. autofunction:: get_ports


HL Tester Functions
---------------------------

.. autofunction:: reserve_tester

.. autofunction:: free_tester

.. autofunction:: get_all_ports

.. autofunction:: get_modules