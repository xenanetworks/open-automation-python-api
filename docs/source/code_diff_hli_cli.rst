Coding Differences between XOA Python HL-API and CLI
======================================================

If you are already very familiar with Xena CLI, the code comparison below will help you understand the coding differences between a XOA Python script and a Xena CLI script, which are doing the same thing.

* The CLI Script consists of two files: ``cli_script.py`` and ``config.txt``. Click to download the dependencies `TestUtilsL23 <https://github.com/xenadevel/xenascriptlibs/blob/master/layer23/python3/testutils/TestUtilsL23.py>`_. and `SocketDrivers <https://github.com/xenadevel/xenascriptlibs/blob/master/layer23/python3/testutils/SocketDrivers.py>`_.
* The XOA Python API script consists of three files: ``xoa_script.py``, ``config.py``, and ``config.txt``.

Both scripts result in the same port/stream configuration.

CLI Code Example
----------------------

`cli_script.py`
.. literalinclude:: code_example/diff_with_cli/cli_script.py


`config.txt`
.. literalinclude:: code_example/diff_with_cli/config.txt


XOA Python API Example
----------------------

`xoa_script.py`
.. literalinclude:: code_example/diff_with_cli/xoa_script.py

`config.py`
.. literalinclude:: code_example/diff_with_cli/config.py

`config.txt`
.. literalinclude:: code_example/diff_with_cli/config.txt
