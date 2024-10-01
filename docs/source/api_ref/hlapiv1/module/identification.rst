Identification
=========================

Name
----------
Gets the name of a module.

Corresponding CLI command: ``M_NAME``

.. code-block:: python

    # Name
    resp = await module.name.get()
    resp.name


Description
-----------
Gets the user-defined description string of a module.

Corresponding CLI command: ``M_COMMENT``

.. code-block:: python

    # Description
    await module.comment.set(comment="description")
    
    resp = await module.comment.get()
    resp.comment

Legacy Model
------------
Gets the legacy model P/N name of a Xena test module.

Corresponding CLI command: ``M_MODEL``

.. code-block:: python

    # Legacy Model
    resp = await module.model.get()
    resp.model

Model
-------------
Gets the model P/N name of a Xena test module.

Corresponding CLI command: ``M_REVISION``

.. code-block:: python

    # Model
    resp = await module.revision.get()
    resp.revision


Serial Number
-----------------
Gets the unique serial number of a module.

Corresponding CLI command: ``M_SERIALNO``

.. code-block:: python

    # Serial Number
    resp = await module.serial_number.get()
    resp.serial_number


Firmware Version
-----------------
Gets the version number of the hardware image installed on a module.

Corresponding CLI command: ``M_VERSIONNO``

.. code-block:: python

    # Firmware Version
    resp = await module.version_number.get()
    resp.version


Port Count
------------
Gets the maximum number of ports on a module.

.. note::

    For a CFP-type module this number refers to the maximum number of ports possible on the module regardless of the media configuration.

    So if a CFP-type module can be set in for instance either 1x100G mode or 8x10G mode then this command will always return 8.

    If you want the current number of ports for a CFP-type module you need to read the M_CFPCONFIGEXT command which returns the number of current ports.

Corresponding CLI command: ``M_PORTCOUNT``

.. code-block:: python

    # Port Count
    resp = await module.port_count.get()
    resp.port_count

Status
------
Get status readings for the test module itself.

Corresponding CLI command: ``M_STATUS``

.. code-block:: python
    
    # Status
    resp = await module.status.get()
    resp.temperature

Model Name
------------
Get the model name of the module.

Corresponding CLI command: ``M_MODEL_NAME``

.. code-block:: python

    # Model Name
    resp = await module.model_name.get()
    resp.name

Model Version String
--------------------
Returns the currently running module software version. Obsoletes ``M_VERSIONNO``.

Corresponding CLI command: ``M_VERSIONSTR``

.. code-block:: python

    # Model Version String
    resp = await module.version_str.get()
    resp.version_str
