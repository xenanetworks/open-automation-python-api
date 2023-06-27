Quick Start
===================

The XOA Python API offers more than just object-oriented APIs and functions for executing test scripts. It also provides a seamless integration with `CLI commands <https://docs.xenanetworks.com/projects/xoa-cli>`_ and port configuration files from ValkyrieManager.
, enabling you to effortlessly work with them.

.. note::

    Integration with CLI commands and ValkyrieManager is supported by version >= 2.1.1.


Scripting with XOA Python API
-----------------------------

The simple code example demonstrates some basics of using :term:`HL-API` and :term: `HL-FUNC`:

* Establish connection to a Valkyrie tester.
* Reserve a port.
* Create a stream on the port.
* Configure the stream.
* Start traffic.
* Collect statistics.
* Stop traffic

We will first walk you through step-by-step covering the topics above. At the end, you will see the whole example. If you want to try it out, you can simply copy and paste it into your environment and run. Remember to change the IP address to your tester's.

This is boilerplate. 

.. literalinclude:: quick_start.py
    :language: python
    :lines: 1-10, 115-124

To establish a connection to a tester is simple. 

.. literalinclude:: quick_start.py
    :language: python
    :lines: 12-13

Access module index 0 on the tester. The method ``obtain()`` is for accessing a test resource that cannot be deleted, such as a module or a port. You can read more about this method in :ref:`Module Manager and Port Manager <obtain-label>`.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 15-16

You need to check the type of the test module afterwards, so the driver can allow you to access the methods and attributes of module.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 18-19

After that, the driver knows you are using the desired module, and then you can access ports on the module. Let's use two ports, one as TX, the other RX.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 21-32

Now we have two ports ready to configure. Let's start creating a stream on the TX port.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 34-48

The ``await utils.apply()`` lets us group several commands bound for the same port into a larger "command". This is called :doc:`Sequential Grouping </command_grouping>`.

Then, we want to clear the statistics counters of both TX and RX ports. We can use :doc:`Parallel Grouping </command_grouping>` to group commands bound for different ports into a larger "command".

.. literalinclude:: quick_start.py
    :language: python
    :lines: 50-56

Now, let's start the traffic on the TX port for roughly 10 seconds and stop. It is "*roughly*" because we use ``sleep()`` to control the duration. It may feel accurate to you but for a Valkyrie tester that can generate 800Gbps traffic with time measurement to nanosecond range, ``sleep()`` is far from accurate in terms of time controlling. If your test requires high-accuracy time control, don't use software to control time. Instead, limit the port's TX time so that you can have down to microsecond-range traffic duration.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 58-65

After the traffic is stopped, we query statistic counters. You can also query counter as the traffic is running to get live statistics. 

.. literalinclude:: quick_start.py
    :language: python
    :lines: 67-107

At last, release the ports (It is absolutely OK if you don't release them.)

.. literalinclude:: quick_start.py
    :language: python
    :lines: 109-113

**The entire example is here.**

.. literalinclude:: quick_start.py
    :language: python
    :caption: Quick start for some basic.


Integrate with CLI and ValkyrieManager
--------------------------------------

.. versionadded:: 2.1.1

The simple code example demonstrates how to use XOA Python API :

* Establish connection to a Valkyrie tester.
* Reserve a port.
* Port configuration from `.xpc` file
* Port configuration from CLI commands
* Module configuration from file
* Module configuration from CLI commands
* Chassis configuration from file
* Chassis configuration from CLI commands

We will first walk you through step-by-step covering the topics above. At the end, you will see the whole example. If you want to try it out, you can simply copy and paste it into your environment and run. Remember to change the IP address to your tester's.

This is boilerplate. 

.. literalinclude:: quick_start_2.py
    :language: python
    :lines: 1-10, 67-76

To establish a connection to a tester is simple. 

.. literalinclude:: quick_start_2.py
    :language: python
    :lines: 11-12

Access module index 0 on the tester. The method ``obtain()`` is for accessing a test resource that cannot be deleted, such as a module or a port. You can read more about this method in :ref:`Module Manager and Port Manager <obtain-label>`.

.. literalinclude:: quick_start_2.py
    :language: python
    :lines: 14-15

You need to check the type of the test module afterwards, so the driver can allow you to access the methods and attributes of module.

.. literalinclude:: quick_start_2.py
    :language: python
    :lines: 16-17

After that, the driver knows you are using the desired module, and then you can access ports on the module.

You can use :guilabel:`Save Port Configuration` in ValkyrieManager to download port configuration files, which contain CLI commands inside. To "upload" the port configuration file generated by ValkyrieManager, simply do:

.. literalinclude:: quick_start_2.py
    :language: python
    :lines: 19-26

In addition to set port configuration from an `xpc` file, you can also send CLI commands using XOA Python API. 

.. literalinclude:: quick_start_2.py
    :language: python
    :lines: 28-36

You can set module or chassis configuration in the same way, either from a file or from command strings.

.. literalinclude:: quick_start_2.py
    :language: python
    :lines: 38-65

**The entire example is here.**

.. literalinclude:: quick_start_2.py
    :language: python
    :caption: Configuration By CLI