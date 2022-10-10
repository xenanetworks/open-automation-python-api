.. _glossary-label:

Glossary of Terms
=====================================================

.. glossary::
    :sorted:

    Test Resource
        Test chassis, test module, and test port, both hardware and virtual are referred to as test resources. A user must have the ownership of a test resource before be able to perform testing.

    XOA Python API
        The foundation of Xena OpenAutomation is its Python API (XOA Python API) that provides interfaces for engineers to manage Xena hardware and virtual test equipment.

    XOA CLI
        XOA Command-Line Interface. Xena provides a rich set of CLI commands for users to administer test chassis for test automation. `Read more here <https://xenanetworks.com/?knowledge-base=knowledge-base/automation/scripting-for-valkyrie-vantage-chimera/valkyrie-vantage-chimera-cli-scripting-guide/overview/intro>`_.

    XOA Core
        `Xena OpenAutomation Core <https://github.com/xenanetworks/open-automation-core>`_ is an open test suite framework to execute XOA Test Suites as its plugins.

    API 
        Application Programming Interface.

    HL-API
        Xena OpenAutomation High-Level Python API.

    LL-API
        Xena OpenAutomation Low-Level Python API.

    DUT
        Device Under Test.

    TGA
        Traffic Generation and Analysis.

    XOA
        Xena OpenAutomation

    Resource Manager
        HL-API provides an easy way to manage subtester test resources, including obtaining test resources and managing indices. 
    
    Module Manager
        A Module Manager helps you access test modules. There is one Module Manager per tester.

    Port Manager
        A Port Managers helps you access test ports. There is one Port Manager per test module.

    Index Manager
        An Index Manager manages the subport-level resource indices such as stream indices, filter indices, connection group indices, match term indices, length term indices, etc. It automatically ensures correct and conflict-free index assignment.

    Module Type
        Module Type corresponds to the model of a test module. Modules of different module types have different port counts, port speeds, capabilities, etc. Examples of module types are Loki-100G-5S-1P, Odin-10G-5S-6P-CU.

    Port Type
        Port Type corresponds to the module that the port belongs to. All ports on the same module have the same port type.

    TPLD
        Test Payload Data. Each Xena test packet contains a special proprietary data area called the Test Payload Data, which contains various information about the packet. The TPLD is located just before the Ethernet FCS.

    CG
        Connection Group. A Connection Group is a basic building block when creating L47 traffic, and it consists of a configurable number of TCP connections.

    TID
        Test Payload Identifier. It is used to identify a sending stream.

    PRBS
        Pseudorandom Binary Sequence is a binary sequence that, while generated with a deterministic algorithm, is difficult to predict and exhibits statistical behavior similar to a truly random sequence.

    Load Profile
        A load profile defines a start time and a duration of each of the ramp-up, steady, and ramp-down phases of a connection group.

    I2C
        I\ :sup:`2`\C (Inter-Integrated Circuit, eye-squared-C), alternatively known as I2C or IIC, is a synchronous, multi-controller/multi-target (controller/target), packet switched, single-ended, serial communication bus.

    CRUD 
        Create, read, update, and delete operations
