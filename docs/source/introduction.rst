Introduction
====================

Xena OpenAutomation (:term:`XOA`) Python API is a standalone Python library that provides a user-friendly and powerful interface for automating network testing tasks using Xena Networks test equipment. Xena test equipment is a high-performance network test device designed for testing and measuring the performance of network equipment and applications.

The XOA Python API is designed to be easy to use and integrate with other automation tools and frameworks. It provides a comprehensive set of methods and classes for interacting with Xena test equipment, including the ability to create and run complex test scenarios, generate and analyze traffic at line rate, and perform detailed analysis of network performance and behavior.

The XOA Python API simplifies the process of automating network testing tasks using Xena test equipment. It provides a simple, yet powerful, interface for interacting with Xena test equipment using the Python programming language. With the XOA Python API, network engineers and testing professionals can easily create and execute test scenarios, generate and analyze traffic, and perform detailed analysis of network performance and behavior, all while leveraging the power and flexibility of the Python programming language.

Additionally, the XOA Python API goes beyond providing object-oriented APIs and functions for executing test scripts. It seamlessly integrates with `CLI commands <https://docs.xenanetworks.com/projects/xoa-cli>`_, enabling users to work with them effortlessly.

Overall, the XOA Python API is a valuable tool for anyone looking to automate their network testing tasks using Xena test equipment. With its simple, yet powerful, interface and support for the Python programming language, the XOA Python API provides a flexible and extensible framework for automating network testing tasks and improving the quality of network infrastructure.

Differences Between XOA Python API and CLI
------------------------------------------

XOA CLI is a command-line interface for managing Xena Networks test equipment and automating network testing tasks. The XOA CLI is part of the Xena OpenAutomation platform, which provides a framework for automating network testing tasks using Xena test equipment. XOA CLI allows users to interact with Xena test equipment from the command line, using a set of commands and parameters that can be used to automate a variety of testing tasks. The XOA CLI is designed to be user-friendly and easy to use, with a simple syntax and intuitive command structure.

The XOA Python API and `XOA CLI <https://docs.xenanetworks.com/projects/xoa-cli>`_ are both tools for automating network testing tasks using Xena test equipment, but they differ in several ways:

* Interface: The XOA Python API provides a Pythonic interface to interact with Xena test equipment, while the XOA CLI provides a command-line interface to interact with Xena test equipment.

* Programming: The XOA Python API is a library that can be used with the Python programming language to create and execute complex test scenarios, generate and analyze traffic, and perform detailed analysis of network performance and behavior. The XOA CLI is a standalone tool that can be used to interact with Xena test equipment through the command line, without the need for programming.

* Functionality: While both tools can be used to create and execute test scenarios, generate and analyze traffic, and perform detailed analysis of network performance and behavior, the XOA Python API provides a more comprehensive and flexible set of functions for interacting with Xena test equipment. The XOA CLI provides a subset of the functionality available through the XOA Python API.

* Ease of use: The XOA Python API provides a more user-friendly and intuitive interface for interacting with Xena test equipment, while the XOA CLI can be more complex and requires knowledge of the command line interface.

Synergy Between XOA Python API and CLI
------------------------------------------

.. important::

    Starting from **v2.1.1**, the XOA Python API provides seamlessly integration with CLI commands and port configuration files from `ValkyrieManager <https://xenanetworks.com/product/valkyriemanager/>`_.

The synergy between the XOA Python API and XOA CLI lies in their integration capabilities. The XOA Python API seamlessly integrates with the XOA CLI, enabling users to work with CLI commands effortlessly within their Python scripts. This integration allows users to combine the flexibility and extensibility of the Python language with the precise control and configuration offered by the CLI commands.

The XOA Python API allows users to interact with Xena Networks test equipment using Python code, providing an object-oriented and user-friendly interface for automating network testing tasks. It enables users to create and execute test scenarios, generate traffic, and analyze network performance using Python programming language. On the other hand, the XOA CLI allows users to configure and control Xena test equipment through command-line commands. It provides a familiar and efficient way to interact with the equipment, allowing users to perform various configuration tasks, manage ports, and execute test commands.

By leveraging both the XOA Python API and XOA CLI, users can take advantage of the best of both worlds. They can harness the power of Python for automation, scripting, and advanced data analysis while utilizing the precise control and configuration options provided by the CLI commands. With the XOA Python API, users can seamlessly work with CLI commands and port configuration files from `ValkyrieManager <https://xenanetworks.com/product/valkyriemanager/>`_, streamlining the configuration process. Whether users prefer a programming approach or a straightforward command-line interface, both options are available to suit different requirements and preferences when working with Xena test equipment. This synergy enhances the overall testing experience, enabling users to perform complex testing tasks efficiently and effectively.

In summary, the XOA Python API and XOA CLI work together to provide a comprehensive and flexible testing solution. The Python API brings automation and scripting capabilities, while the CLI offers precise control and configuration options. The integration between the two allows users to leverage their respective strengths and achieve a synergistic testing workflow.

.. figure:: /_static/xoa_cli_synergy.png
    :scale: 100 %
    :align: left

    Synergy Between XOA Python API and CLI

        A1: Save port configurations from ValkyrieManager and conveniently load them at a later time.

        A2: Use CLI commands to manage and control testers.

        B1: Save port configurations from ValkyrieManager and conveniently load them using XOA Python API to facilitate the automation process.

        B2: Use CLI commands inside XOA Python API to manage and control testers.