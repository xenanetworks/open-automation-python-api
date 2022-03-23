Commands Grouping
===================

Sending commands one by one using CLI is extremely slow in terms of execution speed. This is because the program needs to wait for the response from the tester. More, using CLI it is difficult to group commands together and send them in one round.

XOA Python API provides two ways to group commands together to send to testers, which greatly increase commands execution speed. This is very useful, when the developer has many ports and many streams to configure, as well as querying the port and stream statistics as quickly as possible.

Parallel Grouping
------------------

``asyncio.gather`` groups commands in a parallel way. Commands are sent out in parallel (with neglectable delay between each other). This is very useful when you want to send commands to different test resources, e.g. two different ports on the same tester, or two different ports on different testers.

.. code-block:: python

    await asyncio.gather(
        command_1,
        command_2,
        command_3,
        ...
    )


Sequential Grouping
---------------------

``utils.apply`` groups commands in a sequential way. Commands are sent out in one large batch to the tester. This is very useful when you want to send many commands to the same test resource, e.g. a port on a tester.

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


Sending Command One by One
----------------------------

If you prefer sending commands in the old fashion like using CLI, you can certainly have only one command in the grouping, for example:

.. code-block:: python

    await command_1
    await command_2
    await command_3


.. note::

    Remember to use ``await`` before the command. Commands are defined as Coroutines and must be awaited.


Read more about Python `awaitable object`_.

.. _awaitable object: https://docs.python.org/3/library/asyncio-task.html#id2