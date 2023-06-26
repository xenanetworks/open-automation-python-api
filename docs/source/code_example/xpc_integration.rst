Integration with Port Config
================================================

In ValkyrieManager, port configurations are saved into files with extension ``.xpc`` in the same command format as used by `XOA CLI <https://docs.xenanetworks.com/projects/xoa-cli/>`_. This makes it very easy to go back and forth between a ValkyrieManager environment and a XOA CLI environment. For example, exporting a port configuration from ValkyrieCLIManager generates a configuration file in a simple text format that can be edited using a text editing tool such as Microsoft Notepad. It can then be imported back into ValkyrieManager.

.. tab:: XPC

    .. literalinclude:: xpc_integration/port_config.xpc
        :caption: Port Configuration File (.xpc)
        

.. tab:: HL-API

    .. literalinclude:: xpc_integration/port_config_hlapi.py
        :caption: Port Configuration Script in XOA Python API
        
