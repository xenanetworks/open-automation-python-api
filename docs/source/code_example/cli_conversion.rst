Conversion from CLI
===================================

If you are already familiar with :term:`XOA CLI`, the comparison below will help you understand the differences between a :term:`XOA HL-API<HL-API>` script and a CLI script. Both scripts do the same thing and generate the same port/stream configuration.

Both scripts are using the configuration text file below:

.. literalinclude:: cli_conversion/config.txt
    :caption: Configuration for Both


.. tab:: CLI

    .. literalinclude:: cli_conversion/cli_script.py
        :caption: In XOA CLI
        

.. tab:: HL-API

    .. literalinclude:: cli_conversion/xoa_script.py
        :caption: In XOA HL Python API
        
