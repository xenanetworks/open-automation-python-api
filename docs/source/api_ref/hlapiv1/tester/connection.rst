Connection
=========================

Creating a test object automatically create a TCP connection to the tester.

Valkyrie
----------

.. code-block:: python

    tester = await testers.L23Tester("0.0.0.0", "xoa")

Vulcan
----------

.. code-block:: python

    tester = await testers.L47Tester("0.0.0.0", "xoa")

ValkyrieVE
----------

.. code-block:: python

    tester = await testers.L23VeTester("0.0.0.0", "xoa")

VulcanVE
----------

.. code-block:: python

    tester = await testers.L47VeTester("0.0.0.0", "xoa")