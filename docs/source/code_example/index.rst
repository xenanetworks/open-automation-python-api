Python Script Examples
======================

You can find various XOA Python scripts in our public GitHub repository `Xena OpenAutomation Script Example Library <https://github.com/xenanetworks/open-automation-script-library>`_. It includes script examples of how you can use XOA Python API to configure a Xena tester.

What Example Folder Contains
----------------------------

Each folder contains at least three files:

* Python script file - this is where the example code locates
* requirements.txt - dependencies to run the code. You should `pip install -r requirements.txt` to update your Python environment (either global or virtual) to have the necessary dependencies.

Installing XOA Driver
----------------------------

This section details how to install ``xoa-driver``. Installation is necessary to execute scripts that use XOA Python API.

Before installing ``xoa-driver``, please make sure your environment has installed `python>=3.10` and `pip`.

You can install the ``xoa-driver`` to your global or virtual environment for Windows, macOS, and Linux using the commands below. 

.. code-block:: python

    pip install xoa-driver -U            # latest version


Once the ``xoa-driver`` is installed, you can execute the script.
