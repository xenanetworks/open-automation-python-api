High-Level API vs. CLI
===================================

If you are already familiar with :term:`XOA CLI`, the comparison below will help you understand the differences between a :term:`XOA HL-API<HL-API>` script and a CLI script. Both scripts do the same thing and generate the same port/stream configuration.

Both scripts are using the configuration text file below:

.. literalinclude:: hlapiv1_vs_cli/config.txt
    :caption: Configuration for Both


.. tab:: CLI

    .. literalinclude:: hlapiv1_vs_cli/cli_script.py
        :caption: In XOA CLI
        

.. tab:: HL-API

    .. literalinclude:: hlapiv1_vs_cli/xoa_script.py
        :caption: In XOA HL Python API
        
