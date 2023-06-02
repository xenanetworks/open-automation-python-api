High-Level API vs. Port Config File
================================================

In ValkyrieManager, port configurations are saved into files with extension ``.xpc`` in the same command format as used by `XOA CLI <https://docs.xenanetworks.com/projects/xoa-cli/>`_. This makes it very easy to go back and forth between a ValkyrieManager environment and a XOA CLI environment. For example, exporting a port configuration from ValkyrieCLIManager generates a configuration file in a simple text format that can be edited using a text editing tool such as Microsoft Notepad. It can then be imported back into ValkyrieManager.

Since XOA Python API and XOA CLI are using two different format of messages to control testers (binary by XOA Python API, text by XOA CLI), XOA Python API doesn't support importing and export port configurations to and from a tester yet. However, the example below shows you how you can convert a port configuration file into a HL-API Python script as a temporary solution.

.. note::

    The feature **importing and exporting port configurations files to and from a tester** is schedule in the next release. 


.. tab:: XPC

    .. literalinclude:: hlapiv1_vs_xpc/port_config.xpc
        :caption: Port Configuration File (.xpc) in XOA CLI
        

.. tab:: HL-API

    .. literalinclude:: hlapiv1_vs_xpc/port_config_hlapi.py
        :caption: Port Configuration Script in XOA HL-API
        
