Command Grouping
===================================

Using :term:`XOA CLI` to configure ports and streams is slow because a CLI script must wait for a chassis response to before sending the next command. Such a one-by-one fashion results in *N round trip time* (*N-RTT*), where *N* is the number of commands to send.

Because of the abovementioned N-RTT problem, it is difficult for a CLI script to collect traffic statistics of different ports at the same time (using for loops in the script is far from solving the problem). As a result, this will cause a wrong understanding of the test results.

When you are using HL-API or LL-API to develop your test scripts, you can use *Command Grouping* feature to group several commands and send to the tester in one batch. 

Depending on the destination the commands are bound for, either to the same or different ports, XOA Python API provides two ways of grouping commands, `Sequential Grouping`_ (all commands bound for the same port/module) and `Parallel Grouping`_ (commands are bound for different ports/modules).

Sequential Grouping
----------------------------------------

``utils.apply`` groups commands in a sequential way. Commands are sent out in one large batch to the tester. This is very useful when you want to send many commands to the same :term:`test resource`, e.g. a port on a tester.

.. code-block:: python
    

    commands = [
        command_1,
        command_2,
        command_3,
        ...
    ]
    async for response in utils.apply(*commands):
        print(response)

However, abusing this function can cause memory issue on your computer. This is because the computer needs to store all the grouped commands in the memory until the responses from the testers arrive. To avoid potential grouping abuse, a limit of **200** is place to the maximum number of  commands that you can group sequentially.


``utils.apply_iter`` does exactly the same thing as ``utils.apply`` except it does not aggregate responses but return them one by one as soon as they are ready. This allows sending large batches commands without causing memory issue.

.. code-block:: python
    

    commands = [
        command_1,
        command_2,
        command_3,
        ...
    ]
    async for response in utils.apply_iter(*commands):
        print(response)


Parallel Grouping
----------------------------------------

``asyncio.gather`` groups commands in a parallel way. Commands are sent out in parallel (with neglectable delay between each other). This is very useful when you want to send commands to different :term:`test resources<test resource>`, e.g. two different ports on the same tester, or two different ports on different testers.

.. code-block:: python
    

    await asyncio.gather(
        command_1,
        command_2,
        command_3,
        ...
    )


One-By-One
----------------------------------------

If you prefer sending commands one by one in the same way as using CLI, you can simply place only one command in the group, for example:

.. code-block:: python
    

    await command_1
    await command_2
    await command_3


.. note::

    Remember to use ``await`` before the command. Commands are defined as Coroutines and must be awaited.

.. seealso::
    
    Read more about Python `awaitable object <https://docs.python.org/3/library/asyncio-task.html#id2>`_.

