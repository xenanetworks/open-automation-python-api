Quick Start
===================

The simple code example demonstrates some basics:

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
    :lines: 1-10, 126-135

To establish a connection to a tester is simple. 

.. literalinclude:: quick_start.py
    :language: python
    :lines: 11-12

Access module index 0 on the tester. The method ``obtain()`` is for accessing a test resource that cannot be deleted, such as a module or a port. You can read more about this method in :ref:`Module Manager and Port Manager <obtain-label>`.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 14-15

You need to check the type of the test module afterwards, so the driver can allow you to access the methods and attributes of module.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 17-19

After that, the driver knows you are not using a Chimere module, and then you can access ports on the module. Let's use two ports, one as TX, the other RX.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 20-44

Now we have two ports ready to configure. Let's start creating a stream on the TX port.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 45-60

The ``await utils.apply()`` lets us group several commands bound for the same port into a larger "command". This is called :doc:`Sequential Grouping </understand_xoa_python/command_grouping>`.

Then, we want to clear the statistics counters of both TX and RX ports. We can use :doc:`Parallel Grouping </understand_xoa_python/command_grouping>` to group commands bound for different ports into a larger "command".

.. literalinclude:: quick_start.py
    :language: python
    :lines: 61-68

Now, let's start the traffic on the TX port for roughly 10 seconds and stop. It is "*roughly*" because we use ``sleep()`` to control the duration. It may feel accurate to you but for a Valkyrie tester that can generate 800Gbps traffic with time measurement to nanosecond range, ``sleep()`` is far from accurate in terms of time controlling. If your test requires high-accuracy time control, don't use software to control time. Instead, limit the port's TX time so that you can have down to microsecond-range traffic duration.

.. literalinclude:: quick_start.py
    :language: python
    :lines: 69-77

After the traffic is stopped, we query statistic counters. You can also query counter as the traffic is running to get live statistics. 

.. literalinclude:: quick_start.py
    :language: python
    :lines: 78-119

At last, release the ports (It is absolutely OK if you don't release them.)

.. literalinclude:: quick_start.py
    :language: python
    :lines: 120-125

**The entire example is here.**

.. literalinclude:: quick_start.py
    :language: python
    :caption: Quick start for some basic.