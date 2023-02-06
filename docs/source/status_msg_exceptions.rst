Status Messages and Exceptions
========================================

When you do a ``set`` operation, XOA Python API converts it into a request message (binary encoded) and send to the server on the tester. Upon receiving the message, the server tries to execute it and returns a **status message** for you to check whether the ``set`` operation is successful. The returned message may cause an **exception** if it is not an ``<OK>``. 


Status Messages
-------------------------------

The ``set`` operations themselves simply produce a reply from the tester of: ``<OK>``

In case something is unacceptable to the tester, it will return one of the following status messages. In XOA Python API, all of them are considered as ``BadStatus``.

* ``<NOCONNECTIONS>`` Chassis has no available connection slots.
* ``<NOTLOGGEDON>`` You have not issued a ``C_LOGON`` providing the chassis password.
* ``<NOTRESERVED>`` You have not issued a ``x_RESERVATION`` for the resource you want to change.
* ``<NOTREADABLE>`` The command is write-only.
* ``<NOTWRITABLE>`` The command is read-only.

* ``<NOTVALID>`` The operation is not valid in the current chassis state, e.g. because traffic is on.
* ``<BADPARAMETER>`` Invalid CLI command.
* ``<BADMODULE>`` The module index value is out of bounds.
* ``<BADPORT>`` The port index value is out of bounds.
* ``<BADINDEX>`` A command sub-index value is wrong.
* ``<BADSIZE>`` The size of a parameter is invalid.
* ``<BADVALUE>`` A parameter is invalid.
* ``<FAILED>`` An operation failed to produce a result.
* ``<NOTSUPPORTED>`` Feature not supported.

* ``<MEMORYFAILURE>`` Failed to allocate memory.
* ``<PENDING>`` Status return will wait until command is executed.
* ``<MODULE_OPERATION_NOT_SUPPORTED_BY_CHASSIS>`` Module is not supported by chassis - e.g. because multi-image requires x64 OS..

* ``<XLSFAILED>`` Could not establish connection to Xena License Server.
* ``<XLSDENIED>`` Request for resource rejected by Xena License Server.
* ``<XLSINVALID>`` Request for wrong resource type.


Exceptions
----------------------

If the status message from the server is not ``<OK>``, an exception will be raised by XOA Python API. An example of an exception caused by a ``<NOTWRITABLE>`` reply is shown here:

.. code-block:: shell
    :emphasize-lines: 16

    Traceback (most recent call last):
    File "example.py", line 128, in <module>
        asyncio.run(main())
    File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/runners.py", line 44, in run
        return loop.run_until_complete(main)
    File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/asyncio/base_events.py", line 641, in run_until_complete
        return future.result()
    File "example.py", line 122, in main
        await my_awesome_func(stop_event)
    File "example.py", line 89, in my_awesome_func
        await my_port.eee.mode.set_off()
    File "/env/lib/python3.10/site-packages/xoa_driver/internals/core/transporter/token.py", line 36, in __ask
        raise e
    File "/env/lib/python3.10/site-packages/xoa_driver/internals/core/transporter/token.py", line 34, in __ask
        result = await fut
    xoa_driver.internals.core.transporter.exceptions.BadStatus: Bad status <CommandStatus.NOTWRITABLE: 4> of P_LPTXMODE!

    Response              : ['58', '45', '4e', '41', '00', '00', '00', '00', '04', '04', 'ff', 'ff', '00', '00', '01', 'ea']
    class_name           : P_LPTXMODE
    magic_word           : b'XENA'
    number_of_indices    : 0
    number_of_value_bytes: 0
    command_parameter    : 1028:Replied
    module_index         : 255
    port_index           : 255
    request_identifier   : 490
    index_values         : []
    values               : None


If your script doesn't catch the exception, its execution will be interrupted. Since you won't know what exception may happen before running your script, we **highly recommend you handle exceptions in your script**, especially when you want your script to keep running regardless of the replied status messages received from the server.


Handling Exceptions
----------------------------------------

Basic Exception Handling
^^^^^^^^^^^^^^^^^^^^^^^^^

If you know Python, you can simply write codes to handle exceptions caused by the reply from the server.

.. code-block:: python
    :emphasize-lines: 22-26

    import asyncio
    from xoa_driver import testers
    from xoa_driver import modules
    from xoa_driver import ports

    async def my_awesome_script():
        tester = await testers.L23Tester(host="10.20.1.253", username="XOA", debug=True)

        my_module = tester.modules.obtain(0)

        if isinstance(my_module, modules.ModuleChimera):
            return None # commands which used in this example are not supported by Chimera Module
            
        if my_module.is_reserved_by_me():
            await my_module.reservation.set_release()
        if not my_module.is_released():
            await my_module.reservation.set_relinquish()
        await my_module.reservation.set_reserve()

        my_port = my_module.ports.obtain(0)

        try:
            await my_port.eee.enable.set_off()
            await my_port.eee.mode.set_off()
        except Exception as e:
            print(e) # You decide how to handle the exception


.. seealso::
    
    Read more about `Handling Exceptions in Python <https://docs.python.org/3/tutorial/errors.html#handling-exceptions>`_.


Ignore Exceptions
^^^^^^^^^^^^^^^^^^^^^^^^

You can also use context manager ``suppress`` to **ignore exceptions** if you don't care about the ``BadStatus`` but just want to run the script.

.. note::
    
    A very common use case of ignoring exception is when you run your script to configure a port. Some ports may not support all the API calls in your script, and may return ``<NOTVALID>`` or ``<NOTSUPPORTED>``. But since your objective is to configure the port whatever it supports, you can ignore the exceptions and keep your script running to the end of it. 

.. code-block:: python
    :emphasize-lines: 2, 24

    import asyncio
    from contextlib import suppress
    from xoa_driver import testers
    from xoa_driver import modules
    from xoa_driver import ports
    from xoa_driver import exceptions

    async def my_awesome_script():
        tester = await testers.L23Tester(host="10.20.1.253", username="XOA", debug=True)

        my_module = tester.modules.obtain(0)

        if isinstance(my_module, modules.ModuleChimera):
            return None # commands which used in this example are not supported by Chimera Module
            
        if my_module.is_reserved_by_me():
            await my_module.reservation.set_release()
        if not my_module.is_released():
            await my_module.reservation.set_relinquish()
        await my_module.reservation.set_reserve()

        my_port = my_module.ports.obtain(0)

        with suppress(exceptions.BadStatus):
            await my_port.eee.enable.set_off()
            await my_port.eee.mode.set_off()
        
        print(f"your script will ignore the exception BadStatus and continue")


Show Exceptions In Command Grouping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to do **command grouping** (send multiple commands in one batch) **but at the same time want to know which one(s) raises exception**, you use ``asyncio.gather`` with ``return_exceptions=True`` as shown here:

.. code-block:: python
    :emphasize-lines: 22-28

    import asyncio
    from xoa_driver import testers
    from xoa_driver import modules
    from xoa_driver import ports

    async def my_awesome_script():
        tester = await testers.L23Tester(host="10.20.1.253", username="XOA", debug=True)

        my_module = tester.modules.obtain(0)

        if isinstance(my_module, modules.ModuleChimera):
            return None # commands which used in this example are not supported by Chimera Module
            
        if my_module.is_reserved_by_me():
            await my_module.reservation.set_release()
        if not my_module.is_released():
            await my_module.reservation.set_relinquish()
        await my_module.reservation.set_reserve()

        my_port = my_module.ports.obtain(0)

        responses = asyncio.gather(
            my_port.eee.enable.set_off(),
            my_port.eee.mode.set_off(),
            my_port.capabilities.get(),
            return_exceptions=True
        )
        print(responses)

        


