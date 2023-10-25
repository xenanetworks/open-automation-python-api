Code Examples
===================

You can find various code examples in `XOA Scripting Library <https://github.com/xenanetworks/open-automation-script-library>`_.

We recommend you start from `Quick Start <https://github.com/xenanetworks/open-automation-script-library/tree/main/quick_start>`_. Some highlighted examples that you may find helpful:

1. `XenaAsyncWrapper <https://github.com/xenanetworks/open-automation-script-library/tree/main/async_wrapper>`_: The APIs provided by xoa-driver are **async** functions. This means any function that uses the xoa-driver must be declared as **async**. This might be a problem for you if your existing framework doesn't support async functions. To solve this "incompatibility" issue, we have made an async wrapper class **XenaAsyncWrapper** for you to wrap xoa-driver's async function inside and use it as a regular Python function.

2. `Use XOA Python API to load port configuration file <https://github.com/xenanetworks/open-automation-script-library/tree/main/xpc_integration>`_ as you do on ValkyrieManager. 

3. `Send CLI via XOA Python API <https://github.com/xenanetworks/open-automation-script-library/tree/main/cli_integration>`_ demonstrates how to load ``.xpc`` file or send CLI commands via XOA Python API.

4. `Low-Level API <https://github.com/xenanetworks/open-automation-script-library/tree/main/low_level_api>`_ demonstrates how to use xoa-driver's low-level API if you are familiar with XOA CLI.

5. `Network Emulation <https://github.com/xenanetworks/open-automation-script-library/tree/main/chimera_automation>`_ demonstrates how to automate Chimera for network emulation.

6. `PPM Sweep and ANLT on Thor <https://github.com/xenanetworks/open-automation-script-library/tree/main/thor_ppm_anlt_eth>`_ demonstrates how to change media configuration, perform PPM sweep and AN&LT on Thor modules.

7. `IP ARP/NDP Table <https://github.com/xenanetworks/open-automation-script-library/tree/main/ip_streams_arp_table>`_ demonstrates how to generate ARP/NDP table on a port for IP streams.

8. `Packet Capture <https://github.com/xenanetworks/open-automation-script-library/tree/main/packet_capture>`_ demonstrates how to capture packets and read their content.

**More code examples can be found in** `XOA Scripting Library <https://github.com/xenanetworks/open-automation-script-library>`_.